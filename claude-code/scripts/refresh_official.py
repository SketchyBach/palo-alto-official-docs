"""Refresh requested official documentation, retaining revisions and fetch receipts."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sqlite3
import time
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from urllib.parse import urljoin, urlparse
from urllib.request import Request, urlopen, build_opener, HTTPRedirectHandler

import ingest

ROOT = ingest.ROOT
AGENT = "Mozilla/5.0 (compatible; OfficialDocsRefresh/1.0)"
STAMP = ingest.now().replace(":", "-")


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


class OfficialRedirects(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        if urlparse(newurl).hostname not in self.hosts:
            raise ValueError("redirect outside authorized documentation hosts")
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def retrieve(url, hosts, max_bytes=25_000_000):
    handler = OfficialRedirects()
    handler.hosts = hosts
    opener = build_opener(handler)
    req = Request(url, headers={"User-Agent": AGENT, "Accept": "text/html,application/xml;q=0.9,*/*;q=0.8"})
    with opener.open(req, timeout=35) as response:
        raw = response.read(max_bytes + 1)
        if len(raw) > max_bytes:
            raise ValueError(f"response exceeds {max_bytes // 1_000_000} MB; retained as an explicit coverage gap")
        return raw, dict(response.headers), response.url


def prepare_db(c):
    ingest.setup(c)
    c.executescript("""
    CREATE TABLE IF NOT EXISTS page_revisions(
      id INTEGER PRIMARY KEY,url TEXT,archived_at TEXT,record_json TEXT,
      UNIQUE(url,record_json));
    CREATE TABLE IF NOT EXISTS fetch_receipts(
      id INTEGER PRIMARY KEY,run_label TEXT,url TEXT,checked_at TEXT,
      success INTEGER,error TEXT,content_hash TEXT,raw_path TEXT,final_url TEXT);
    """)


def archive(c, url):
    cur = c.execute("SELECT * FROM pages WHERE url=?", (url,))
    old = cur.fetchone()
    if old:
        record = dict(zip([col[0] for col in cur.description], old))
        c.execute("INSERT OR IGNORE INTO page_revisions(url,archived_at,record_json) VALUES(?,?,?)",
                  (url, ingest.now(), json.dumps(record, ensure_ascii=False, sort_keys=True)))


def parse_page(raw, headers, url):
    text = raw.decode("utf-8", "replace")
    content_type = headers.get("Content-Type", headers.get("content-type", "")).lower()
    if "html" in content_type:
        page = ingest.PageParser()
        page.feed(text)
        # Preserve navigation links for traversal, but index the article when available.
        main = re.search(r"<main\b[^>]*>(.*?)</main>", text, re.S | re.I)
        if main:
            article = ingest.PageParser()
            article.feed(main.group(1))
            if len(article.text()) >= 120:
                article.links = page.links
                article.title = page.title
                article.meta = page.meta
                page = article
    elif any(kind in content_type for kind in ("text/plain", "markdown")):
        page = ingest.TextPage(text, url)
    else:
        raise ValueError("unsupported content type: " + content_type)
    body = page.text()
    # Challenge pages lead with these messages. Searching a large prefix caused
    # false positives on legitimate release notes that discuss an "Access Denied"
    # product error.
    lead = body[:300].strip().lower()
    if len(body) < 120 or any(lead.startswith(marker) for marker in
                             ("access denied", "just a moment...", "enable javascript to run this app")):
        raise ValueError("access challenge or insufficient document content")
    return page


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", action="append", required=True)
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--discover-only", action="store_true")
    parser.add_argument("--discovery", help="Reuse a discovery receipt generated in this refresh session")
    parser.add_argument("--resume", help="Resume an interrupted run directory without discarding receipts")
    parser.add_argument("--retry-failures", action="store_true",
                        help="With --resume, retry URLs whose latest receipt failed")
    parser.add_argument("--max-response-mb", type=int, default=25,
                        help="Maximum page response size; increase for known large catalog pages")
    args = parser.parse_args()
    cfg = json.loads((ROOT / "sources.json").read_text(encoding="utf-8"))
    selected = [s for s in cfg["sources"] if s["name"] in args.source]
    if len(selected) != len(set(args.source)):
        raise SystemExit("Unknown source")
    hosts = set(cfg["policy"]["allowed_domains"])
    folder = Path(args.resume).resolve() if args.resume else ROOT / "data/refresh-runs" / STAMP
    folder.mkdir(parents=True, exist_ok=bool(args.resume))
    c = sqlite3.connect(ingest.DB, timeout=60)
    prepare_db(c)
    c.commit()
    # SQLite's online backup preserves the pre-refresh database consistently.
    if not args.discover_only and not args.resume:
        backup = sqlite3.connect(folder / "before.sqlite3")
        c.backup(backup)
        backup.close()
    urls = {}
    errors = []
    discoveries = []
    if args.discovery:
        discovery = json.loads(Path(args.discovery).read_text(encoding="utf-8"))
        urls = {u: s for u, s in discovery["urls"].items() if s in args.source}
        discoveries = discovery["sitemaps"]
        errors = discovery["errors"]
    prefixes = [p for s in selected for p in s["include_prefixes"]]
    for source in ([] if args.discovery else selected):
        print(json.dumps({"discovering": source["name"]}), flush=True)
        for u in source["seed_urls"]:
            urls[u] = source["name"]
        for (u,) in c.execute("SELECT url FROM pages WHERE source=?", (source["name"],)):
            urls[u] = source["name"]
        for prefix in source["include_prefixes"]:
            for (u,) in c.execute("SELECT url FROM pages WHERE url LIKE ?", (prefix + "%",)):
                urls[u] = source["name"]
        pending = [f"https://{h}/sitemap.xml" for h in {urlparse(u).hostname for u in source["seed_urls"]}]
        seen_sitemaps = set()
        while pending:
            sm = pending.pop(0)
            if sm in seen_sitemaps:
                continue
            seen_sitemaps.add(sm)
            try:
                raw, headers, final = retrieve(sm, hosts)
                path = folder / (digest(sm.encode())[:20] + ".xml")
                path.write_bytes(raw)
                tree = ET.fromstring(raw)
                is_index = tree.tag.endswith("sitemapindex")
                locs = [node.text.strip() for node in tree.iter() if node.tag.endswith("}loc") and node.text]
                discoveries.append({"url": sm, "sha256": digest(raw), "locations": len(locs), "path": str(path.relative_to(ROOT))})
                for loc in locs:
                    if urlparse(loc).hostname not in hosts:
                        continue
                    if is_index:
                        pending.append(loc)
                    elif ingest.allowed(loc, hosts, source["include_prefixes"]):
                        urls[loc] = source["name"]
            except Exception as exc:
                errors.append({"url": sm, "error": str(exc)})
    urls = {u: s for u, s in urls.items() if ingest.allowed(u, hosts, prefixes)}
    (folder / "discovery.json").write_text(json.dumps({"urls": urls, "sitemaps": discoveries, "errors": errors}, indent=2), encoding="utf-8")
    print(json.dumps({"run": str(folder), "discovered": len(urls), "discovery_errors": errors}), flush=True)
    if args.discover_only:
        return
    robots = {h: ingest.robot(h) for h in {urlparse(u).hostname for u in urls}}
    done = set()
    ok = failed = changed = new = 0
    if args.resume:
        latest = {}
        for line in (folder / "receipts.jsonl").read_text(encoding="utf-8").splitlines():
            rec = json.loads(line)
            latest[rec["url"]] = rec
        if args.retry_failures:
            done = {url for url, rec in latest.items() if rec["success"]}
            ok = len(done)
        else:
            done = set(latest)
            ok = sum(bool(rec["success"]) for rec in latest.values())
            failed = sum(not rec["success"] for rec in latest.values())

    def worker(url):
        try:
            rp = robots.get(urlparse(url).hostname)
            if rp and not rp.can_fetch(AGENT, url):
                raise ValueError("blocked by robots.txt")
            raw, headers, final = retrieve(url, hosts, args.max_response_mb * 1_000_000)
            return raw, headers, final, parse_page(raw, headers, final), None
        except Exception as exc:
            return None, {}, None, None, f"{type(exc).__name__}: {exc}"
        finally:
            time.sleep(max(0.35, cfg["policy"]["request_delay_seconds"]))

    with (folder / "receipts.jsonl").open("a", encoding="utf-8") as log:
        while pending_urls := [u for u in urls if u not in done]:
            with ThreadPoolExecutor(max_workers=args.workers) as pool:
                futures = {pool.submit(worker, u): u for u in pending_urls}
                for future in as_completed(futures):
                    u = futures[future]
                    raw, headers, final, page, error = future.result()
                    done.add(u)
                    prior = c.execute("SELECT content_hash,body FROM pages WHERE url=?", (u,)).fetchone()
                    raw_path = None
                    content_hash = None
                    if error:
                        failed += 1
                        # Never replace working content, timestamps or FTS with a failed response.
                        if not prior:
                            ingest.save(c, u, urls[u], 0, None, {}, error)
                    else:
                        ok += 1
                        content_hash = digest(page.text().encode())
                        changed += bool(prior and prior[0] != content_hash)
                        new += not bool(prior and prior[1])
                        raw_path = str((folder / (digest(u.encode())[:20] + ".raw")).relative_to(ROOT))
                        (ROOT / raw_path).write_bytes(raw)
                        archive(c, u)
                        ingest.save(c, u, urls[u], 200, page, headers)
                        for href in page.links:
                            link = ingest.canonical(href, final)
                            if link and link.endswith(".md") and link[:-3] in urls:
                                continue
                            if link and ingest.allowed(link, hosts, prefixes):
                                match = next(s for s in selected if any(link.startswith(p) for p in s["include_prefixes"]))
                                urls.setdefault(link, match["name"])
                    receipt = {"url": u, "checked_at": ingest.now(), "success": error is None, "error": error,
                               "content_hash": content_hash, "raw_sha256": digest(raw) if raw else None,
                               "raw_path": raw_path, "final_url": final}
                    log.write(json.dumps(receipt) + "\n")
                    log.flush()
                    c.execute("INSERT INTO fetch_receipts(run_label,url,checked_at,success,error,content_hash,raw_path,final_url) VALUES(?,?,?,?,?,?,?,?)",
                              (STAMP,u,receipt["checked_at"],int(error is None),error,content_hash,raw_path,final))
                    c.commit()
                    if len(done) % 50 == 0:
                        print(json.dumps({"completed": len(done), "discovered": len(urls), "ok": ok, "failed": failed}), flush=True)
    summary = {"run": STAMP, "finished_at": ingest.now(), "sources": args.source,
               "discovered": len(urls), "attempted": len(done), "ok": ok, "failed": failed,
               "changed": changed, "new": new, "discovery_errors": errors}
    (folder / "summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary, indent=2), flush=True)


if __name__ == "__main__":
    main()

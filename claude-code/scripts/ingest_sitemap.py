#!/usr/bin/env python3
"""Add every missing page from one allowlisted official sitemap source."""
from __future__ import annotations

import argparse
import hashlib
import json
import sqlite3
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from urllib.parse import urlparse

import ingest


ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / "data/index.sqlite3"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True)
    parser.add_argument("--workers", type=int, default=4)
    args = parser.parse_args()

    raw = (ROOT / "sources.json").read_bytes()
    cfg = json.loads(raw)
    policy = cfg["policy"]
    source = next((item for item in cfg["sources"] if item["name"] == args.source), None)
    if not source:
        raise SystemExit(f"Unknown source: {args.source}")

    domains = {urlparse(url).hostname for url in source["seed_urls"]}
    urls = set(source["seed_urls"])
    for domain in domains:
        urls.update(ingest.sitemap_urls(domain, policy["user_agent"], source["include_prefixes"]))
    urls = sorted(
        url for url in urls
        if ingest.allowed(url, set(policy["allowed_domains"]), source["include_prefixes"])
    )

    connection = sqlite3.connect(DB)
    ingest.setup(connection)
    existing = {
        row[0] for row in connection.execute(
            "SELECT url FROM pages WHERE body<>'' AND error IS NULL"
        )
    }
    pending = [url for url in urls if url not in existing]
    run_id = connection.execute(
        "INSERT INTO runs(started_at,config_hash) VALUES(?,?)",
        (ingest.now(), hashlib.sha256(raw).hexdigest()),
    ).lastrowid
    connection.commit()
    robots = {domain: ingest.robot(domain) for domain in domains}

    def retrieve(url):
        rp = robots.get(urlparse(url).hostname)
        if rp and not rp.can_fetch(policy["user_agent"], url):
            return url, 0, None, {}, "blocked by robots.txt"
        try:
            status, raw_page, headers = ingest.fetch(url, policy["user_agent"], None)
            content_type = headers.get("Content-Type", "").lower()
            decoded = raw_page.decode("utf-8", "replace")
            if "html" in content_type:
                parsed = ingest.PageParser()
                parsed.feed(decoded)
            elif any(kind in content_type for kind in ("text/plain", "text/markdown", "markdown")):
                parsed = ingest.TextPage(decoded, url)
            else:
                raise ValueError(f"unsupported content type: {content_type}")
            if len(parsed.text()) < 120:
                raise ValueError("too little extractable text")
            return url, status, parsed, headers, None
        except Exception as exc:
            return url, getattr(exc, "code", 0) or 0, None, {}, f"{type(exc).__name__}: {exc}"
        finally:
            time.sleep(policy["request_delay_seconds"])

    ok = failed = 0
    print(json.dumps({"sitemap_urls": len(urls), "already_present": len(urls) - len(pending), "pending": len(pending), "workers": args.workers}))
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = [pool.submit(retrieve, url) for url in pending]
        for completed, future in enumerate(as_completed(futures), 1):
            url, status, parsed, headers, error = future.result()
            ingest.save(connection, url, source["name"], status, parsed, headers, error)
            ok += error is None
            failed += error is not None
            connection.commit()
            if completed % 250 == 0:
                print(json.dumps({"completed": completed, "total": len(pending), "ok": ok, "failed": failed}), flush=True)

    connection.execute(
        "UPDATE runs SET finished_at=?,pages_ok=?,pages_failed=? WHERE id=?",
        (ingest.now(), ok, failed, run_id),
    )
    connection.commit()
    print(json.dumps({"run_id": run_id, "sitemap_urls": len(urls), "attempted": len(pending), "ok": ok, "failed": failed}, indent=2))


if __name__ == "__main__":
    main()

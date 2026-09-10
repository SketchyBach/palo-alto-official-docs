"""Import authenticated browser captures from the official KOI documentation site."""
from __future__ import annotations

import argparse
import hashlib
import json
import sqlite3
import time
from pathlib import Path
from urllib.parse import urlparse

import ingest

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DB = DATA / "index.sqlite3"
PAGES = DATA / "pages"


def now():
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("capture_dir", help="Directory of JSON pages captured from authenticated docs.koi.ai")
    args = parser.parse_args()
    capture_dir = Path(args.capture_dir).resolve()
    capture_files = sorted(capture_dir.glob("*.json"))
    capture_files = [p for p in capture_files if p.name not in {"home.json", "progress.json"}]

    connection = sqlite3.connect(DB)
    ingest.setup(connection)
    connection.executescript("""
    CREATE TABLE IF NOT EXISTS browser_imports(
      id INTEGER PRIMARY KEY, source TEXT, imported_at TEXT, capture_sha256 TEXT,
      records INTEGER, invalid INTEGER, receipt_path TEXT);
    CREATE TABLE IF NOT EXISTS page_revisions(
      id INTEGER PRIMARY KEY,url TEXT,archived_at TEXT,record_json TEXT,
      UNIQUE(url,record_json));
    """)
    PAGES.mkdir(parents=True, exist_ok=True)
    stamp = now()
    imported = invalid = 0
    receipt_pages = []
    capture_hash = hashlib.sha256()

    for path in capture_files:
        raw = path.read_bytes()
        capture_hash.update(path.name.encode())
        capture_hash.update(raw)
        try:
            record = json.loads(raw)
        except json.JSONDecodeError:
            invalid += 1
            continue
        url = (record.get("requested_url") or record.get("url") or "").split("#", 1)[0]
        title = (record.get("title") or "").removesuffix(" | Koi").strip()
        body = (record.get("text") or "").strip()
        captured_at = record.get("captured_at") or stamp
        parsed = urlparse(url)
        if parsed.scheme != "https" or parsed.hostname != "docs.koi.ai" or len(body) < 120:
            invalid += 1
            continue
        current = connection.execute("SELECT * FROM pages WHERE url=?", (url,))
        old = current.fetchone()
        if old:
            old_record = dict(zip([column[0] for column in current.description], old))
            connection.execute(
                "INSERT OR IGNORE INTO page_revisions(url,archived_at,record_json) VALUES(?,?,?)",
                (url, stamp, json.dumps(old_record, ensure_ascii=False, sort_keys=True)),
            )
        digest = hashlib.sha256(body.encode("utf-8")).hexdigest()
        rel = Path("data/pages") / (hashlib.sha256(url.encode()).hexdigest()[:20] + ".md")
        (ROOT / rel).write_text(
            f"---\nurl: {url}\nfetched_at: {captured_at}\nsource: koi-official-browser\n"
            f"capture_method: authenticated official browser\n---\n\n# {title}\n\n{body}\n",
            encoding="utf-8",
        )
        connection.execute("""INSERT INTO pages VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,1)
          ON CONFLICT(url) DO UPDATE SET source=excluded.source,title=excluded.title,
          body=excluded.body,fetched_at=excluded.fetched_at,checked_at=excluded.checked_at,
          modified_hint=excluded.modified_hint,content_hash=excluded.content_hash,
          http_status=excluded.http_status,error=NULL,local_path=excluded.local_path,authoritative=1""",
          (url, "koi-official-browser", title, body, captured_at, stamp,
           "Captured from authenticated official KOI documentation", None, None,
           digest, 200, None, rel.as_posix()))
        ingest.replace_fts(connection, url, title, body, "koi-official-browser")
        receipt_pages.append({
            "url": url,
            "sha256": digest,
            "capture_file": path.relative_to(ROOT).as_posix(),
            "capture_sha256": hashlib.sha256(raw).hexdigest(),
            "local_path": rel.as_posix(),
        })
        imported += 1
        if imported % 50 == 0:
            connection.commit()

    failures = []
    progress = capture_dir / "progress.json"
    if progress.is_file():
        failures = json.loads(progress.read_text(encoding="utf-8")).get("failures", [])
    aggregate_hash = capture_hash.hexdigest()
    receipt_dir = DATA / "koi-browser-imports"
    receipt_dir.mkdir(parents=True, exist_ok=True)
    receipt = {
        "source": "authenticated official KOI documentation",
        "host": "docs.koi.ai",
        "imported_at": stamp,
        "capture_sha256": aggregate_hash,
        "records": receipt_pages,
        "invalid": invalid,
        "failures": failures,
    }
    receipt_path = receipt_dir / f"receipt-{aggregate_hash[:16]}.json"
    receipt_path.write_text(json.dumps(receipt, indent=2), encoding="utf-8")
    connection.execute(
        "INSERT INTO browser_imports(source,imported_at,capture_sha256,records,invalid,receipt_path) VALUES(?,?,?,?,?,?)",
        ("koi-official-browser", stamp, aggregate_hash, imported, invalid,
         receipt_path.relative_to(ROOT).as_posix()),
    )
    connection.commit()
    print(json.dumps({"imported": imported, "invalid": invalid, "failures": len(failures),
                      "receipt": str(receipt_path)}, indent=2))
    if invalid:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

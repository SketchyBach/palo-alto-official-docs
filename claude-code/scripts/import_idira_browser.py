#!/usr/bin/env python3
"""Import browser-rendered Idira pages with an auditable capture receipt."""
from __future__ import annotations

import argparse
import hashlib
import json
import sqlite3
import time
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DB = DATA / "index.sqlite3"
PAGES = DATA / "pages"


def now():
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("capture", help="JSONL produced through the official interactive Idira portal")
    args = parser.parse_args()
    capture = Path(args.capture).resolve()
    raw = capture.read_bytes()
    records = [json.loads(line) for line in raw.decode("utf-8").splitlines() if line.strip()]

    connection = sqlite3.connect(DB)
    connection.execute("""CREATE TABLE IF NOT EXISTS browser_imports(
      id INTEGER PRIMARY KEY, source TEXT, imported_at TEXT, capture_sha256 TEXT,
      records INTEGER, invalid INTEGER, receipt_path TEXT)""")
    PAGES.mkdir(parents=True, exist_ok=True)
    imported = invalid = 0
    receipt_pages = []
    stamp = now()
    for record in records:
        url = record.get("url", "")
        title = (record.get("title") or "").strip()
        body = (record.get("body") or "").strip()
        captured_at = record.get("captured_at") or stamp
        parsed = urlparse(url)
        if parsed.scheme != "https" or parsed.hostname != "docs.cyberark.com" or len(body) < 120:
            invalid += 1
            continue
        digest = hashlib.sha256(body.encode("utf-8")).hexdigest()
        rel = Path("data/pages") / (hashlib.sha256(url.encode()).hexdigest()[:20] + ".md")
        (ROOT / rel).write_text(
            f"---\nurl: {url}\nfetched_at: {captured_at}\nsource: idira-docs\n"
            f"capture_method: official interactive browser\n---\n\n# {title}\n\n{body}\n",
            encoding="utf-8",
        )
        connection.execute("""INSERT INTO pages VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,1)
          ON CONFLICT(url) DO UPDATE SET source=excluded.source,title=excluded.title,
          body=excluded.body,fetched_at=excluded.fetched_at,checked_at=excluded.checked_at,
          modified_hint=excluded.modified_hint,content_hash=excluded.content_hash,
          http_status=excluded.http_status,error=NULL,local_path=excluded.local_path,authoritative=1""",
          (url, "idira-docs", title, body, captured_at, stamp,
           "Captured from official interactive portal", None, None, digest, 200, None,
           rel.as_posix()))
        connection.execute("DELETE FROM pages_fts WHERE url=?", (url,))
        connection.execute("INSERT INTO pages_fts VALUES(?,?,?,?)", (url, title, body, "idira-docs"))
        receipt_pages.append({"url": url, "sha256": digest, "local_path": rel.as_posix()})
        imported += 1

    receipt_dir = DATA / "idira-browser-imports"
    receipt_dir.mkdir(parents=True, exist_ok=True)
    capture_hash = hashlib.sha256(raw).hexdigest()
    receipt = {
        "source": "official interactive Idira portal",
        "host": "docs.cyberark.com",
        "imported_at": stamp,
        "capture_sha256": capture_hash,
        "records": receipt_pages,
        "invalid": invalid,
    }
    receipt_path = receipt_dir / f"receipt-{capture_hash[:16]}.json"
    receipt_path.write_text(json.dumps(receipt, indent=2), encoding="utf-8")
    connection.execute(
        "INSERT INTO browser_imports(source,imported_at,capture_sha256,records,invalid,receipt_path) VALUES(?,?,?,?,?,?)",
        ("idira-docs", stamp, capture_hash, imported, invalid, receipt_path.relative_to(ROOT).as_posix()),
    )
    connection.commit()
    print(json.dumps({"imported": imported, "invalid": invalid, "receipt": str(receipt_path)}, indent=2))
    if invalid:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

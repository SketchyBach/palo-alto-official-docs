#!/usr/bin/env python3
"""Record auditable live replacements for stale official documentation URLs.

The failed page remains in ``pages``.  This only creates a separate mapping when
the complete path after the PAN-OS version is identical to a successfully
captured official page in another version.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sqlite3
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / "data" / "index.sqlite3"
RECEIPTS = ROOT / "data" / "url-replacements"
PAN_OS = re.compile(r"^/pan-os/(?P<version>\d+-\d+)/(?P<rest>.+)$")


def version_key(url: str) -> tuple[int, int]:
    match = PAN_OS.match(urlsplit(url).path)
    return tuple(map(int, match.group("version").split("-"))) if match else (0, 0)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--db", type=Path, default=DB)
    args = parser.parse_args()
    now = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    connection = sqlite3.connect(args.db)
    connection.execute("""CREATE TABLE IF NOT EXISTS url_replacements(
        stale_url TEXT PRIMARY KEY,
        replacement_url TEXT NOT NULL,
        method TEXT NOT NULL,
        verified_at TEXT NOT NULL,
        stale_http_status INTEGER,
        replacement_content_hash TEXT NOT NULL,
        candidate_count INTEGER NOT NULL
    )""")
    rows = connection.execute(
        "SELECT url,http_status FROM pages WHERE url LIKE 'https://docs.paloaltonetworks.com/%' "
        "AND http_status=404"
    ).fetchall()
    live = connection.execute(
        "SELECT url,content_hash FROM pages WHERE url LIKE 'https://docs.paloaltonetworks.com/%' "
        "AND http_status BETWEEN 200 AND 299 AND length(body)>0"
    ).fetchall()
    by_rest: dict[str, list[tuple[str, str]]] = {}
    for url, content_hash in live:
        match = PAN_OS.match(urlsplit(url).path)
        if match:
            by_rest.setdefault(match.group("rest"), []).append((url, content_hash))

    records = []
    for stale_url, status in rows:
        match = PAN_OS.match(urlsplit(stale_url).path)
        if not match:
            continue
        candidates = [item for item in by_rest.get(match.group("rest"), []) if item[0] != stale_url]
        if not candidates:
            continue
        candidates.sort(key=lambda item: version_key(item[0]), reverse=True)
        replacement_url, content_hash = candidates[0]
        record = {
            "stale_url": stale_url,
            "replacement_url": replacement_url,
            "method": "exact-pan-os-path-newest-live-version",
            "verified_at": now,
            "stale_http_status": status,
            "replacement_content_hash": content_hash,
            "candidate_count": len(candidates),
        }
        connection.execute(
            "INSERT INTO url_replacements VALUES(:stale_url,:replacement_url,:method,:verified_at,"
            ":stale_http_status,:replacement_content_hash,:candidate_count) "
            "ON CONFLICT(stale_url) DO UPDATE SET replacement_url=excluded.replacement_url,"
            "method=excluded.method,verified_at=excluded.verified_at,"
            "stale_http_status=excluded.stale_http_status,"
            "replacement_content_hash=excluded.replacement_content_hash,"
            "candidate_count=excluded.candidate_count",
            record,
        )
        records.append(record)
    connection.commit()
    RECEIPTS.mkdir(parents=True, exist_ok=True)
    receipt = RECEIPTS / f"replacement-map-{now[:10]}.json"
    receipt.write_text(json.dumps({"generated_at": now, "records": records}, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"stale_404": len(rows), "mapped": len(records), "unmapped": len(rows)-len(records), "receipt": str(receipt.relative_to(ROOT))}))


if __name__ == "__main__":
    main()

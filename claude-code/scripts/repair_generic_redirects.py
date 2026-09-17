#!/usr/bin/env python3
"""Restore the pre-refresh record for URLs redirected to a generic landing page."""
from __future__ import annotations

import argparse
import json
import sqlite3
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / "data" / "index.sqlite3"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("receipts")
    args = parser.parse_args()
    latest = {}
    for line in Path(args.receipts).read_text(encoding="utf-8").splitlines():
        receipt = json.loads(line)
        latest[receipt["url"]] = receipt
    affected = sorted(
        url for url, receipt in latest.items()
        if receipt.get("success")
        and (receipt.get("final_url") or "").rstrip("/").endswith("/platform-explorer")
        and not url.rstrip("/").endswith("/platform-explorer")
    )
    generic_hashes = {
        receipt.get("content_hash") for receipt in latest.values()
        if receipt.get("success")
        and (receipt.get("final_url") or "").rstrip("/").endswith("/platform-explorer")
    }
    expected_hashes = {}
    for receipt_path in (ROOT / "data" / "url-replacements").glob("replacement-map-*.json"):
        replacement_map = json.loads(receipt_path.read_text(encoding="utf-8"))
        for item in replacement_map.get("records", []):
            expected_hashes[item["replacement_url"]] = item["replacement_content_hash"]
    connection = sqlite3.connect(DB)
    restored = 0
    for url in affected:
        rows = connection.execute(
            "SELECT record_json FROM page_revisions WHERE url=? ORDER BY id DESC", (url,)
        ).fetchall()
        records = [json.loads(row[0]) for row in rows]
        expected = expected_hashes.get(url)
        record = next((item for item in records if expected and item.get("content_hash") == expected), None)
        if not record:
            record = next((item for item in records if item.get("content_hash") not in generic_hashes), None)
        if not record:
            continue
        columns = list(record)
        assignments = ",".join(f"{column}=?" for column in columns if column != "url")
        values = [record[column] for column in columns if column != "url"] + [url]
        connection.execute(f"UPDATE pages SET {assignments} WHERE url=?", values)
        restored += 1
    connection.execute("DELETE FROM pages_fts")
    connection.execute(
        "INSERT INTO pages_fts(url,title,body) SELECT url,title,body FROM pages WHERE body<>''"
    )
    connection.commit()
    print(json.dumps({"affected": len(affected), "restored": restored}, indent=2))


if __name__ == "__main__":
    main()

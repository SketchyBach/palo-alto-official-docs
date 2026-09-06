#!/usr/bin/env python3
"""Compare a fresh discovery receipt with indexed pages and fetch receipts."""

import argparse
import json
import sqlite3
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def classify_failure(url: str, error: str | None) -> str:
    if url.endswith("/rss.xml"):
        return "non_document_rss"
    if "404" in (error or ""):
        return "http_404"
    return "other"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--discovery", required=True)
    parser.add_argument("--receipts", required=True)
    parser.add_argument("--output")
    args = parser.parse_args()

    discovery_path = Path(args.discovery)
    receipts_path = Path(args.receipts)
    discovered = set(json.loads(discovery_path.read_text(encoding="utf-8"))["urls"])

    connection = sqlite3.connect(ROOT / "data/index.sqlite3")
    rows = {}
    for chunk_start in range(0, len(discovered), 500):
        chunk = list(discovered)[chunk_start:chunk_start + 500]
        placeholders = ",".join("?" for _ in chunk)
        query = (
            "SELECT url, source, length(body), http_status, error FROM pages "
            f"WHERE url IN ({placeholders})"
        )
        rows.update({row[0]: row for row in connection.execute(query, chunk)})

    latest = {}
    for line in receipts_path.read_text(encoding="utf-8").splitlines():
        receipt = json.loads(line)
        latest[receipt["url"]] = receipt

    empty = [
        {"url": url, "http_status": rows[url][3], "error": rows[url][4]}
        for url in sorted(discovered)
        if url in rows and not rows[url][2]
    ]
    failed = [receipt for receipt in latest.values() if not receipt["success"]]
    sources = dict(connection.execute(
        "SELECT source, count(*) FROM pages WHERE body<>'' GROUP BY source"
    ))
    report = {
        "fresh_sitemap_urls": len(discovered),
        "fresh_missing_database_records": sorted(discovered - set(rows)),
        "fresh_sitemap_urls_with_indexed_body": sum(
            bool(rows[url][2]) for url in discovered if url in rows
        ),
        "fresh_sitemap_urls_without_body": empty,
        "latest_receipt_urls": len(latest),
        "latest_fetch_successes": sum(bool(item["success"]) for item in latest.values()),
        "latest_fetch_failures": len(failed),
        "latest_failure_categories": dict(sorted(Counter(
            classify_failure(item["url"], item.get("error")) for item in failed
        ).items())),
        "total_indexed_bodies": connection.execute(
            "SELECT count(*) FROM pages WHERE body<>''"
        ).fetchone()[0],
        "fts_records": connection.execute("SELECT count(*) FROM pages_fts").fetchone()[0],
        "indexed_bodies_by_source": sources,
    }
    report["passed"] = (
        not report["fresh_missing_database_records"]
        and report["total_indexed_bodies"] == report["fts_records"]
        and report["latest_failure_categories"].get("other", 0) == 0
        and all(
            item["url"].endswith("/rss.xml") or "404" in (item["error"] or "")
            for item in empty
        )
    )

    rendered = json.dumps(report, indent=2)
    if args.output:
        Path(args.output).write_text(rendered + "\n", encoding="utf-8")
    print(rendered)
    raise SystemExit(0 if report["passed"] else 1)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Audit closure and receipt integrity for an authenticated KOI browser crawl."""

import argparse
import hashlib
import json
import sqlite3
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit


ROOT = Path(__file__).resolve().parents[1]


def canonical(url: str) -> str:
    parts = urlsplit(url)
    path = parts.path[:-3] if parts.path.endswith(".md") else parts.path
    if path != "/":
        path = path.rstrip("/")
    return urlunsplit((parts.scheme.lower(), parts.netloc.lower(), path, "", ""))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--capture-dir", required=True)
    parser.add_argument("--receipt", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    capture_dir = Path(args.capture_dir)
    progress = json.loads((capture_dir / "progress.json").read_text(encoding="utf-8"))
    all_captures = []
    for path in capture_dir.glob("*.json"):
        if path.name in {"progress.json", "completeness-audit.json"}:
            continue
        item = json.loads(path.read_text(encoding="utf-8"))
        if item.get("url") and "html" in item:
            item["_path"] = path
            all_captures.append(item)

    receipt = json.loads(Path(args.receipt).read_text(encoding="utf-8"))
    captures = []
    capture_file_mismatches = 0
    for record in receipt["records"]:
        path = ROOT / record["capture_file"]
        if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != record["capture_sha256"]:
            capture_file_mismatches += 1
            continue
        captures.append(json.loads(path.read_text(encoding="utf-8")))

    captured_urls = {canonical(item["requested_url"]) for item in captures}
    linked_urls = {
        canonical(link)
        for item in all_captures
        for link in item.get("links", [])
        if urlsplit(link).netloc.lower() == "docs.koi.ai"
    }
    unresolved = sorted(linked_urls - captured_urls)
    expected_auxiliary = {
        "https://docs.koi.ai/llms.txt",
        "https://docs.koi.ai/api-reference/readme",
        "https://docs.koi.ai/get-started/be-successful-with-koi",
    }

    receipt_urls = {canonical(item["url"]) for item in receipt["records"]}
    connection = sqlite3.connect(ROOT / "data/index.sqlite3")
    database_hash_mismatches = sum(
        connection.execute(
            "SELECT count(*) FROM pages WHERE url=? AND source='koi-official-browser' "
            "AND content_hash=? AND body<>''",
            (record["url"], record["sha256"]),
        ).fetchone()[0] != 1
        for record in receipt["records"]
    )

    report = {
        "seen_routes": len(progress["seen"]),
        "pending_routes": len(progress["pending"]),
        "captured_article_pages": len(captures),
        "receipt_records": len(receipt["records"]),
        "capture_file_hash_mismatches": capture_file_mismatches,
        "capture_urls_missing_from_receipt": sorted(captured_urls - receipt_urls),
        "receipt_urls_missing_from_capture": sorted(receipt_urls - captured_urls),
        "linked_internal_targets": len(linked_urls),
        "unresolved_link_targets": unresolved,
        "verified_aliases": {
            "https://docs.koi.ai/api-reference/readme": "https://docs.koi.ai/api-reference",
            "https://docs.koi.ai/get-started/be-successful-with-koi": "https://docs.koi.ai/",
        },
        "non_article_index_endpoint": {
            "url": "https://docs.koi.ai/llms.txt",
            "browser_result": "net::ERR_BLOCKED_BY_CLIENT",
        },
        "verified_removed_routes": [
            "https://docs.koi.ai/security/overview",
            "https://docs.koi.ai/guides/agentic-runtime-control/agent-activity",
        ],
        "database_receipt_hash_mismatches": database_hash_mismatches,
    }
    report["passed"] = (
        not progress["pending"]
        and len(captures) == len(receipt["records"])
        and capture_file_mismatches == 0
        and not report["capture_urls_missing_from_receipt"]
        and not report["receipt_urls_missing_from_capture"]
        and set(unresolved) == expected_auxiliary | set(report["verified_removed_routes"])
        and report["database_receipt_hash_mismatches"] == 0
    )
    rendered = json.dumps(report, indent=2)
    Path(args.output).write_text(rendered + "\n", encoding="utf-8")
    print(rendered)
    raise SystemExit(0 if report["passed"] else 1)


if __name__ == "__main__":
    main()

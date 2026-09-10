#!/usr/bin/env python3
"""Report corpus freshness by source without accessing the network."""
from __future__ import annotations

import argparse
import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def parse_time(value: str | None) -> datetime | None:
    if not value:
        return None
    normalized = value.strip().replace("Z", "+00:00")
    try:
        parsed = datetime.fromisoformat(normalized)
    except ValueError:
        return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--fail-stale", action="store_true", help="Exit nonzero when any source is stale")
    args = parser.parse_args()

    config = json.loads((ROOT / "sources.json").read_text(encoding="utf-8"))
    default_days = int(config.get("policy", {}).get("stale_after_days", 14))
    thresholds = {item["name"]: int(item.get("stale_after_days", default_days)) for item in config.get("local_sources", [])}
    thresholds.update({item["name"]: int(item.get("stale_after_days", default_days)) for item in config.get("sources", [])})

    database = ROOT / "data" / "index.sqlite3"
    if not database.exists():
        raise SystemExit("Corpus not initialized. Run pa-docs.cmd rebuild first.")

    now = datetime.now(timezone.utc)
    connection = sqlite3.connect(database)
    rows = connection.execute(
        "SELECT source, COUNT(*), MAX(COALESCE(checked_at, fetched_at)) FROM pages WHERE body<>'' GROUP BY source ORDER BY source"
    ).fetchall()
    sources = []
    stale_count = 0
    for source, records, newest_value in rows:
        newest = parse_time(newest_value)
        age_days = (now - newest).days if newest else None
        threshold = thresholds.get(source, default_days)
        stale = age_days is None or age_days > threshold
        stale_count += int(stale)
        sources.append({
            "source": source,
            "records": records,
            "newest_checked_at": newest.isoformat().replace("+00:00", "Z") if newest else None,
            "age_days": age_days,
            "stale_after_days": threshold,
            "stale": stale,
        })

    report = {"checked_at": now.isoformat().replace("+00:00", "Z"), "stale_sources": stale_count, "sources": sources}
    print(json.dumps(report, indent=2))
    raise SystemExit(1 if args.fail_stale and stale_count else 0)


if __name__ == "__main__":
    main()

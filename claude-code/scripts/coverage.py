#!/usr/bin/env python3
"""Report verified corpus coverage by Palo Alto product family."""
from __future__ import annotations

import argparse
import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / "data" / "index.sqlite3"
PRODUCTS = {
    "NGFW and PAN-OS": ("ngfw", "pan-os", "panorama", "hardware"),
    "Software Firewalls": ("cloud-ngfw", "cloud-ngfw-aws", "cloud-ngfw-azure", "cn-series", "vm-series"),
    "Prisma SASE and Access": ("sase", "prisma-access", "prisma-access-agent", "prisma-sd-wan", "strata-cloud-manager", "autonomous-dem", "fedramp"),
    "Prisma Browser": ("prisma-access-browser", "prisma-browser"),
    "Cloud-Delivered Security": ("advanced-threat-prevention", "advanced-url-filtering", "advanced-wildfire", "dns-security", "enterprise-dlp", "iot", "next-gen-casb", "saas-agent-security", "saas-security"),
    "AI Security": ("ai-access-security", "ai-runtime-security"),
    "Cortex XDR and XSIAM": ("cortex-xdr-3.x", "cortex-xdr-5.x", "cortex-xdr-agent", "cortex-xsiam", "xdr-5-api", "xsiam-api", "xql-command-reference-guide"),
    "Cortex Cloud": ("cortex-cloud-runtime-security", "cortex-cloud-posture-management", "application-security", "cortex-cloud-api"),
    "Prisma Cloud": ("__prisma_cloud__",),
    "Cortex XSOAR and Xpanse": ("cortex-xsoar-8-saas", "cortex-xsoar-8-on-prem", "xsoar-6-administrator-guide", "cortex-xpanse"),
    "Cortex Agentix": ("cortex-agentix",),
    "Common Services": ("common-services", "hub", "strata-logging-service", "identity"),
    "Idira": ("welcome",),
    "KOI": ("__koi__",),
}


def parse_time(value: str | None) -> datetime | None:
    if not value:
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
        return parsed.replace(tzinfo=parsed.tzinfo or timezone.utc).astimezone(timezone.utc)
    except ValueError:
        return None


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--markdown", action="store_true")
    parser.add_argument("--output")
    parser.add_argument("--fail-empty", action="store_true")
    args = parser.parse_args()
    connection = sqlite3.connect(DB)
    rows = connection.execute(
        "SELECT url,source,title,body,COALESCE(checked_at,fetched_at) FROM pages "
        "WHERE authoritative=1 AND body<>'' AND error IS NULL"
    ).fetchall()
    now = datetime.now(timezone.utc)
    report = []
    for product, prefixes in PRODUCTS.items():
        matched = []
        for row in rows:
            url, source, title, body, checked = row
            if "__koi__" in prefixes:
                applies = source.startswith("koi-")
            elif "__prisma_cloud__" in prefixes:
                applies = source == "prisma-cloud"
            elif product == "Idira":
                applies = source.startswith("idira-")
            else:
                segment = urlparse(url).path.strip("/").split("/", 1)[0]
                applies = segment in prefixes
            if applies:
                matched.append(row)
        dates = [parse_time(row[4]) for row in matched]
        dates = [item for item in dates if item]
        report.append({
            "product_family": product,
            "pages": len(matched),
            "admin_guide_pages": sum(
                "administrator guide" in row[2].lower()
                or "/administration/" in row[0].lower()
                or "administrator-guide" in row[0].lower()
                for row in matched
            ),
            "newest_age_days": (now - max(dates)).days if dates else None,
            "oldest_age_days": (now - min(dates)).days if dates else None,
        })
    if args.json:
        rendered = json.dumps(report, indent=2)
    elif args.markdown:
        lines = [
            "# Product coverage",
            "",
            "Generated from authoritative records with indexed content and no active fetch error.",
            "",
            "| Product family | Pages | Admin-guide pages | Newest age (days) | Oldest age (days) |",
            "|---|---:|---:|---:|---:|",
        ]
        lines.extend(
            f"| {item['product_family']} | {item['pages']} | {item['admin_guide_pages']} | {item['newest_age_days']} | {item['oldest_age_days']} |"
            for item in report
        )
        lines.extend([
            "",
            "This inventory shows indexed coverage; it is not by itself proof that every live sitemap URL was captured. See the latest file under `data/coverage-audits/` for the sitemap completeness result.",
        ])
        rendered = "\n".join(lines)
    else:
        lines = ["Product family\tPages\tAdmin guide pages\tNewest age\tOldest age"]
        lines.extend(
            f"{item['product_family']}\t{item['pages']}\t{item['admin_guide_pages']}\t{item['newest_age_days']}\t{item['oldest_age_days']}"
            for item in report
        )
        rendered = "\n".join(lines)
    if args.output:
        Path(args.output).write_text(rendered + "\n", encoding="utf-8")
    print(rendered)
    if args.fail_empty and any(not item["pages"] for item in report):
        raise SystemExit(1)


if __name__ == "__main__":
    main()

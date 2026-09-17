#!/usr/bin/env python3
"""Fail when a major supported product family cannot be retrieved."""
from __future__ import annotations

import sqlite3
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / "data" / "index.sqlite3"
CHECKS = {
    "PAN-OS": "%docs.paloaltonetworks.com/pan-os/%",
    "NGFW": "%docs.paloaltonetworks.com/ngfw/%",
    "Panorama": "%docs.paloaltonetworks.com/panorama/%",
    "Hardware": "%docs.paloaltonetworks.com/hardware/%",
    "VM-Series": "%docs.paloaltonetworks.com/vm-series/%",
    "CN-Series": "%docs.paloaltonetworks.com/cn-series/%",
    "Cloud NGFW AWS": "%docs.paloaltonetworks.com/cloud-ngfw-aws/%",
    "Cloud NGFW Azure": "%docs.paloaltonetworks.com/cloud-ngfw-azure/%",
    "GlobalProtect": "%docs.paloaltonetworks.com/globalprotect/%",
    "Prisma Access": "%docs.paloaltonetworks.com/prisma-access/%",
    "Prisma Access Agent": "%docs.paloaltonetworks.com/prisma-access-agent/%",
    "Prisma SASE": "%docs.paloaltonetworks.com/sase/%",
    "Prisma SD-WAN": "%docs.paloaltonetworks.com/prisma-sd-wan/%",
    "Prisma Browser": "%docs.paloaltonetworks.com/prisma-access-browser/%",
    "Autonomous DEM": "%docs.paloaltonetworks.com/autonomous-dem/%",
    "Enterprise DLP": "%docs.paloaltonetworks.com/enterprise-dlp/%",
    "Advanced Threat Prevention": "%docs.paloaltonetworks.com/advanced-threat-prevention/%",
    "Advanced URL Filtering": "%docs.paloaltonetworks.com/advanced-url-filtering/%",
    "Advanced WildFire": "%docs.paloaltonetworks.com/advanced-wildfire/%",
    "DNS Security": "%docs.paloaltonetworks.com/dns-security/%",
    "Device Security": "%docs.paloaltonetworks.com/iot/%",
    "Next-Generation CASB": "%docs.paloaltonetworks.com/next-gen-casb%",
    "SaaS Agent Security": "%docs.paloaltonetworks.com/saas-agent-security/%",
    "SaaS Security": "%docs.paloaltonetworks.com/saas-security/%",
    "AI Access Security": "%docs.paloaltonetworks.com/ai-access-security/%",
    "Prisma AIRS": "%docs.paloaltonetworks.com/ai-runtime-security/%",
    "Strata Cloud Manager": "%docs.paloaltonetworks.com/strata-cloud-manager/%",
    "Strata Logging Service": "%docs.paloaltonetworks.com/strata-logging-service/%",
    "Common Services": "%docs.paloaltonetworks.com/common-services/%",
    "Prisma Cloud": "%docs.prismacloud.io/%",
    "Cortex XDR": "%cortex-docs.paloaltonetworks.com/%cortex-xdr%",
    "Cortex XSIAM": "%cortex-docs.paloaltonetworks.com/%cortex-xsiam%",
    "Cortex XSOAR": "%cortex-docs.paloaltonetworks.com/%xsoar%",
    "Cortex Cloud": "%cortex-docs.paloaltonetworks.com/%cortex-cloud%",
    "Cortex Xpanse": "%cortex-docs.paloaltonetworks.com/%cortex-xpanse%",
    "Cortex Agentix": "%cortex-docs.paloaltonetworks.com/%cortex-agentix%",
}


def main() -> None:
    connection = sqlite3.connect(DB)
    failures = []
    for name, pattern in CHECKS.items():
        count = connection.execute(
            "SELECT count(*) FROM pages WHERE authoritative=1 AND body<>'' AND error IS NULL AND lower(url) LIKE lower(?)",
            (pattern,),
        ).fetchone()[0]
        print(f"{name}: {count}")
        if count == 0:
            failures.append(name)
    idira = connection.execute(
        "SELECT count(*) FROM pages WHERE authoritative=1 AND body<>'' AND error IS NULL AND source LIKE 'idira-%'"
    ).fetchone()[0]
    print(f"Idira: {idira}")
    if not idira:
        failures.append("Idira")
    koi = connection.execute(
        "SELECT count(*) FROM pages WHERE authoritative=1 AND body<>'' AND error IS NULL AND source LIKE 'koi-%'"
    ).fetchone()[0]
    print(f"KOI: {koi}")
    if not koi:
        failures.append("KOI")
    if failures:
        raise SystemExit("Missing verified coverage: " + ", ".join(failures))
    print("All product-family smoke tests passed.")


if __name__ == "__main__":
    main()

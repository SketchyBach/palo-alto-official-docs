---
name: palo-alto-official-docs
description: Maintain, import, refresh, audit, repair, or inspect the local official Palo Alto Networks and KOI documentation corpus and its provenance. Use for corpus status, source coverage, freshness, crawling, KOI imports/recovery, integrity checks, search-index maintenance, or changing the documentation skills. Do not use for ordinary technical questions or integration procedures.
---

# Palo Alto Official Docs Maintenance

Preserve all source material and provenance. Never delete corpus data.

- Check integrity with `python scripts/audit.py`.
- Check coverage with `python scripts/status.py`.
- Refresh a web source with `python scripts/ingest.py --source <name> --max-pages <n>`.
- Import a normal KOI export with `python scripts/import_koi.py <directory>`.
- Import the exact 13-page KOI recovery artifact with `python scripts/import_koi_recovery.py <file>`.

Allow only configured official domains. Normal KOI pages require manifest hashes; the 13 recovered pages require exact failed-manifest URL matching and a recovery receipt with bundle and page hashes.

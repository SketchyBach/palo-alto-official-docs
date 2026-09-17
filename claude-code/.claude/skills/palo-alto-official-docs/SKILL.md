---
name: palo-alto-official-docs
description: Maintain, import, refresh, audit, repair, or inspect the local official Palo Alto Networks and KOI documentation corpus and its provenance. Use for corpus status, source coverage, freshness, crawling, KOI imports/recovery, integrity checks, search-index maintenance, or changing the documentation skills. Do not use for ordinary technical questions or integration procedures.
---

# Palo Alto Official Docs Maintenance

Preserve all source material and provenance. Never delete corpus data.

## Inspect before changing

1. Run `cmd /c pa-docs.cmd status` and `cmd /c pa-docs.cmd freshness`.
2. Confirm the requested product/source and whether authenticated browser capture is required.
3. Preserve existing pages, failure receipts, hashes, and timestamps. Updates are additive/upsert operations.

## Maintain the corpus

- Full integrity check: `cmd /c pa-docs.cmd verify`.
- Product coverage report: `cmd /c pa-docs.cmd coverage --fail-empty`.
- Cross-product retrieval smoke tests: `cmd /c pa-docs.cmd smoke-test`.
- Fresh sitemap completeness audit: `cmd /c pa-docs.cmd completeness --discovery <discovery.json> --receipts <receipts.jsonl> --output <report.json>`.
- Refresh one public web source: `cmd /c pa-docs.cmd update --source <name> --max-pages <n>`.
- Refresh the official multi-source snapshot: `cmd /c pa-docs.cmd refresh-official`.
- Import a manifest-verified KOI export: `cmd /c pa-docs.cmd import-koi <directory>`.
- Import an authenticated KOI browser capture: `cmd /c pa-docs.cmd import-koi-browser <capture.jsonl>`.
- Import only the exact 13-page recovery artifact: `cmd /c pa-docs.cmd recover-koi <file>`.
- Import Idira browser captures with `python scripts/import_idira_browser.py <capture.jsonl>` after verifying the URL is on `docs.cyberark.com`.

After every import or refresh, rebuild the index, run the integrity audit, check status and freshness, run the coverage report and smoke tests, and run focused searches for the changed product. Do not report success until all checks pass. Integrity proves internal consistency; it does not prove that every current sitemap URL was captured. For a completeness claim, also retain and audit a fresh sitemap discovery receipt.

## Publish safely

Build the public snapshot with `python scripts/build_public_snapshot.py <repository>`. Confirm private field evidence and credentials are excluded. Review `git status` and the exact remote, commit only the intended files, push the current branch, and verify the remote commit. If authentication or network access fails, state explicitly that the update remains local.

Allow only configured official domains. Normal KOI pages require manifest hashes; the 13 recovered pages require exact failed-manifest URL matching and a recovery receipt with bundle and page hashes.

Stop rather than guessing when an official page cannot be verified, a receipt/hash fails, the product scope is ambiguous, or a refresh is incomplete. Confidential field material may guide research but must not be copied into the public repository without official public corroboration.

# Palo Alto documentation corpus for Claude Code

This is a portable, read-first copy of the verified Palo Alto Networks and KOI documentation corpus. Private field-support emails are not included.

## Start

1. Install Python 3.10 or newer. No third-party Python packages are required.
2. Open this folder in a terminal.
3. Run `python scripts/rebuild_index.py` to create the Git-excluded SQLite index.
4. Run `python scripts/audit.py` to verify integrity.
5. Start Claude Code from this folder with `claude`.
6. Ask a Palo Alto Networks or KOI question normally. Claude reads `CLAUDE.md` automatically and uses the local skill instructions.

To test retrieval directly:

```text
python scripts/search.py "Cortex XDR broker VM" --mode answer --json
```

## Contents

- `CLAUDE.md` — project instructions for Claude Code.
- `.claude/skills/` — technical-answer, integration-guide, and corpus-maintenance workflows.
- `data/index.sqlite3` — generated searchable official-only index (created by `rebuild_index.py`; excluded from Git because of GitHub's file-size limit).
- `data/pages/` — locally stored official Palo Alto pages.
- `data/koi-official/` — verified KOI export and recovery records.
- `scripts/` — search, audit, status, ingestion, and KOI import tools.
- `sources.json` — allowlisted official sources.

Internet access is needed only when refreshing the corpus. Existing local searches and audits work offline.

The reconstructed corpus contains 24,215 searchable records, including 55 official Idira portal pages protected by SHA-256 capture receipts and 175 verified exact-path replacements for stale PAN-OS links.

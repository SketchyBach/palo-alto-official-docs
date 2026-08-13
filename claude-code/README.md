# Palo Alto documentation corpus for Claude Code

This is a portable, read-first copy of the verified Palo Alto Networks and KOI documentation corpus. Private field-support emails are not included.

## Start

1. Install Python 3.10 or newer. No third-party Python packages are required.
2. Open this folder in a terminal.
3. Run `python scripts/audit.py` to verify integrity.
4. Start Claude Code from this folder with `claude`.
5. Ask a Palo Alto Networks or KOI question normally. Claude reads `CLAUDE.md` automatically and uses the local skill instructions.

To test retrieval directly:

```text
python scripts/search.py "Cortex XDR broker VM" --mode answer --json
```

## Contents

- `CLAUDE.md` — project instructions for Claude Code.
- `.claude/skills/` — technical-answer, integration-guide, and corpus-maintenance workflows.
- `data/index.sqlite3` — searchable official-only index.
- `data/pages/` — locally stored official Palo Alto pages.
- `data/koi-official/` — verified KOI export and recovery records.
- `scripts/` — search, audit, status, ingestion, and KOI import tools.
- `sources.json` — allowlisted official sources.

Internet access is needed only when refreshing the corpus. Existing local searches and audits work offline.


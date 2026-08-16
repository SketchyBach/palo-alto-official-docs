# Palo Alto Official Documentation Assistants

This private repository contains two portable versions of the same verified official Palo Alto Networks and KOI documentation corpus:

- `codex/` — open this directory in Codex. It uses `AGENTS.md` and `.codex/skills/`.
- `claude-code/` — open this directory in Claude Code. It uses `CLAUDE.md` and `.claude/skills/`.

Both versions include an official-only searchable SQLite index. Private field-support email evidence, caches, and generated ZIP files are intentionally excluded.

The committed corpus currently reconstructs 24,215 searchable records. This includes 55 browser-captured pages from the official Idira portal with SHA-256 receipts. It also includes an audited map for 175 stale Palo Alto URLs whose exact document paths exist in newer live PAN-OS versions. Original failed-fetch evidence is retained in the maintenance workspace; it is not presented as page content.

Run the integrity audit from either directory with Python 3.10 or newer:

```text
python scripts/rebuild_index.py
python scripts/audit.py
python scripts/search.py "Prisma AIRS AI Runtime Security" --mode answer --json
```

The complete generated SQLite index is larger than GitHub's per-file limit, so it is rebuilt locally from the committed official page files after cloning.

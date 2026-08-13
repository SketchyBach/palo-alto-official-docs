# Palo Alto Official Documentation Assistants

This private repository contains two portable versions of the same verified official Palo Alto Networks and KOI documentation corpus:

- `codex/` — open this directory in Codex. It uses `AGENTS.md` and `.codex/skills/`.
- `claude-code/` — open this directory in Claude Code. It uses `CLAUDE.md` and `.claude/skills/`.

Both versions include an official-only searchable SQLite index. Private field-support email evidence, caches, and generated ZIP files are intentionally excluded.

Run the integrity audit from either directory with Python 3.10 or newer:

```text
python scripts/audit.py
```


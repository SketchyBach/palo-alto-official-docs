# Palo Alto Official Documentation Assistant

Private, verified documentation corpus and retrieval tools for Palo Alto Networks and KOI.

## Codex

Open the repository root in Codex. `AGENTS.md` routes technical questions, integration guides, and corpus-maintenance work through the project skills under `.codex/skills/`.

## Claude Code

The portable Claude Code version is in `palo-alto-docs-claude-code/`. Open that directory in a terminal and run `claude`; its `CLAUDE.md` and `.claude/skills/` provide the corresponding workflows.

## Verify the corpus

Python 3.10 or newer is required. No third-party packages are needed.

```text
python scripts/audit.py
python scripts/status.py
python scripts/search.py "Cortex XDR broker VM" --mode answer --json
```

Only allowlisted official Palo Alto Networks material and SHA-256-verified KOI records are authoritative. Private field-support correspondence is intentionally excluded from this repository.

# Palo Alto Official Documentation Assistant

Public-safe, verified documentation corpus and retrieval tools for Palo Alto Networks and KOI. Private field-support evidence is intentionally excluded.

## Codex

Open the repository root in Codex. `AGENTS.md` routes technical questions, integration guides, and corpus-maintenance work through the project skills under `.codex/skills/`.

## Claude Code

The portable Claude Code version is the sibling `../claude-code/` directory. Open that directory in a terminal and run `claude`; its `CLAUDE.md` and `.claude/skills/` provide the corresponding workflows.

## Verify the corpus

Python 3.10 or newer is required. No third-party packages are needed.

```text
python scripts/rebuild_index.py
python scripts/audit.py
python scripts/status.py
python scripts/search.py "Cortex XDR broker VM" --mode answer --json
```

The generated SQLite index is intentionally not stored in Git because the complete corpus index exceeds GitHub's per-file limit. Run `rebuild_index.py` once after cloning.

On Windows, use the bundled dispatcher so Codex's Python runtime can be found even when `python` is not on PATH:

```powershell
cmd /c pa-docs.cmd verify
cmd /c pa-docs.cmd freshness
cmd /c pa-docs.cmd search "Cortex XDR broker VM" --mode answer --json
```

The reconstructed corpus contains 44,309 searchable records, including 57 official Idira portal pages and 321 current authenticated KOI pages protected by SHA-256 capture receipts, plus 175 verified exact-path replacements for stale PAN-OS links.

Only allowlisted official Palo Alto Networks material, the official Idira portal at `docs.cyberark.com`, and SHA-256-verified KOI records are authoritative. Private field-support correspondence is intentionally excluded from this repository.

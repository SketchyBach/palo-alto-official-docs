# Palo Alto Official Documentation Assistants

This public-safe repository contains two portable versions of the same verified official Palo Alto Networks and KOI documentation corpus.

See [`PRODUCT_COVERAGE.md`](PRODUCT_COVERAGE.md) for the generated product-family inventory and the latest report under `data/coverage-audits/` for sitemap completeness evidence.

## New computer quick start

Give Codex or Claude Code this repository URL:

`https://github.com/SketchyBach/palo-alto-official-docs`

Ask it to clone the repository and use the appropriate package as the project root:

- Codex: open `codex/` so it loads `AGENTS.md` and `.codex/skills/`.
- Claude Code: open `claude-code/` so it loads `CLAUDE.md` and `.claude/skills/`.

Run the package's `scripts/rebuild_index.py` once after cloning. The complete documentation pages, provenance receipts, retrieval tools, and portfolio-aware skills are committed to `main`; only the generated SQLite index is excluded because of GitHub's file-size limit.

The repository contains:

- `codex/` — open this directory in Codex. It uses `AGENTS.md` and `.codex/skills/`.
- `claude-code/` — open this directory in Claude Code. It uses `CLAUDE.md` and `.claude/skills/`.

Both versions include the official-only corpus files and tools needed to rebuild the searchable SQLite index locally. Private field-support email evidence, caches, generated indexes, and generated ZIP files are intentionally excluded.

The committed corpus currently reconstructs 44,309 searchable records. This includes 57 browser-captured pages from the official Idira portal and 321 current authenticated KOI pages, all protected by SHA-256 receipts. It also includes an audited map for 175 stale Palo Alto URLs whose exact document paths exist in newer live PAN-OS versions. Original failed-fetch evidence is retained in the maintenance workspace; it is not presented as page content.

Run the integrity audit from either directory with Python 3.10 or newer:

```text
python scripts/rebuild_index.py
python scripts/audit.py
python scripts/search.py "Prisma AIRS AI Runtime Security" --mode answer --json
```

On Windows, the preferred equivalent from the repository root is:

```powershell
cmd /c codex\pa-docs.cmd verify
cmd /c codex\pa-docs.cmd search "Prisma AIRS AI Runtime Security" --mode answer --json
cmd /c codex\pa-docs.cmd freshness
python scripts\check_parity.py
cmd /c codex\pa-docs.cmd coverage --fail-empty
cmd /c codex\pa-docs.cmd smoke-test
```

Freshness is reported separately from integrity: an older official capture can remain hash-valid while still needing refresh. The parity check confirms that the Codex and Claude Code public snapshots remain synchronized.

Coverage is organized across Network Security, Software Firewalls, Prisma SASE and Access, Prisma Browser, Prisma Cloud, Cloud-Delivered Security Services, AI Security, Cortex Security Operations, Cortex Cloud, Cortex XSOAR/Xpanse, Cortex Agentix, Common Services, Idira, and KOI. A successful integrity audit proves that committed evidence is internally consistent; a fresh sitemap audit is still required before claiming that every current Admin Guide is present.

The complete generated SQLite index is larger than GitHub's per-file limit, so it is rebuilt locally from the committed official page files after cloning.

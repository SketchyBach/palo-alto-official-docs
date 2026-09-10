# Contributing

Only add material from the allowlisted official sources documented in `sources.json`, the official Idira portal, or a KOI export/browser capture with a valid SHA-256 receipt. Do not add confidential partner material, customer data, credentials, or private support correspondence.

Before publishing a change, synchronize both portable packages and run:

```powershell
cmd /c codex\pa-docs.cmd verify
python scripts\check_parity.py
```

Every corpus change must retain provenance, preserve earlier failure evidence, identify the source and refresh date, and describe incomplete coverage.

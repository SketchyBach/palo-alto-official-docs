#!/usr/bin/env python3
"""Ensure the portable Codex and Claude Code snapshots contain the same corpus."""
from __future__ import annotations

import hashlib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CODEX_ONLY_SCRIPTS = {"import_field_emails.py", "inspect_eml.py"}
PAIRS = (
    ("codex/data/pages", "claude-code/data/pages"),
    ("codex/data/koi-official", "claude-code/data/koi-official"),
    ("codex/data/koi-browser-imports", "claude-code/data/koi-browser-imports"),
    ("codex/data/idira-browser-imports", "claude-code/data/idira-browser-imports"),
    ("codex/data/url-replacements", "claude-code/data/url-replacements"),
    ("codex/scripts", "claude-code/scripts"),
    ("codex/.codex/skills", "claude-code/.claude/skills"),
)
FILES = ("pa-docs.cmd", "pa-docs.ps1", "requirements.txt", "sources.json")


def inventory(relative: str) -> dict[str, str]:
    base = ROOT / relative
    result = {}
    for path in sorted(item for item in base.rglob("*") if item.is_file()):
        if "__pycache__" in path.parts or path.suffix in {".pyc", ".sqlite3", ".wal", ".shm"}:
            continue
        if relative == "codex/scripts" and path.name in CODEX_ONLY_SCRIPTS:
            continue
        result[path.relative_to(base).as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
    return result


def main() -> None:
    failures = []
    for left, right in PAIRS:
        if inventory(left) != inventory(right):
            failures.append(f"Package mismatch: {left} != {right}")
    for name in FILES:
        left = ROOT / "codex" / name
        right = ROOT / "claude-code" / name
        if left.read_bytes() != right.read_bytes():
            failures.append(f"Package mismatch: codex/{name} != claude-code/{name}")
    if failures:
        raise SystemExit("\n".join(failures))
    print("Codex and Claude Code public snapshots match.")


if __name__ == "__main__":
    main()

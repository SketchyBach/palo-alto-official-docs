#!/usr/bin/env python3
"""Build the public-safe Codex and Claude Code corpus snapshots."""

import argparse
import filecmp
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ROOT_FILES = ("pa-docs.cmd", "pa-docs.ps1", "requirements.txt", "sources.json")
EXCLUDED_SCRIPTS = {"import_field_emails.py", "inspect_eml.py"}
DATA_DIRECTORIES = (
    "pages",
    "koi-official",
    "koi-browser-imports",
    "idira-browser-imports",
    "url-replacements",
)


def copy_file(source: Path, destination: Path, counters: dict[str, int]) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    if destination.is_file() and filecmp.cmp(source, destination, shallow=False):
        counters["unchanged"] += 1
        return
    shutil.copy2(source, destination)
    counters["copied"] += 1


def copy_tree(source: Path, destination: Path, counters: dict[str, int]) -> None:
    for path in source.rglob("*"):
        if path.is_file():
            copy_file(path, destination / path.relative_to(source), counters)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("destination", help="Repository containing codex/ and claude-code/")
    args = parser.parse_args()
    destination = Path(args.destination).resolve()
    counters = {"copied": 0, "unchanged": 0}

    for package_name in ("codex", "claude-code"):
        package = destination / package_name
        for name in ROOT_FILES:
            copy_file(ROOT / name, package / name, counters)
        for script in (ROOT / "scripts").glob("*.py"):
            if script.name not in EXCLUDED_SCRIPTS:
                copy_file(script, package / "scripts" / script.name, counters)
        for name in DATA_DIRECTORIES:
            copy_tree(ROOT / "data" / name, package / "data" / name, counters)

    copy_file(ROOT / "AGENTS.md", destination / "codex" / "AGENTS.md", counters)
    copy_tree(ROOT / ".codex" / "skills", destination / "codex" / ".codex" / "skills", counters)
    copy_tree(ROOT / ".codex" / "skills", destination / "claude-code" / ".claude" / "skills", counters)
    print(f"Public snapshot updated: {counters['copied']} copied, {counters['unchanged']} unchanged")


if __name__ == "__main__":
    main()

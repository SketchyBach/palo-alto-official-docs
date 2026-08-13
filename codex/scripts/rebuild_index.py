#!/usr/bin/env python3
"""Rebuild the searchable SQLite index from committed official page files."""
from __future__ import annotations

import hashlib
import re
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / "data/index.sqlite3"


def parse_page(path: Path):
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n\n?(.*)$", text, re.S)
    if not match:
        return None
    metadata = {}
    for line in match.group(1).splitlines():
        if ": " in line:
            key, value = line.split(": ", 1)
            metadata[key] = value
    body_with_title = match.group(2).strip()
    title_match = re.match(r"^#\s+(.+?)\n\n", body_with_title, re.S)
    title = title_match.group(1).strip() if title_match else path.stem
    body = body_with_title[title_match.end():] if title_match else body_with_title
    return metadata, title, body


def main():
    DB.parent.mkdir(parents=True, exist_ok=True)
    if DB.exists():
        DB.unlink()
    connection = sqlite3.connect(DB)
    connection.executescript("""
    PRAGMA journal_mode=WAL;
    CREATE TABLE pages(url TEXT PRIMARY KEY,source TEXT NOT NULL,title TEXT,body TEXT,fetched_at TEXT NOT NULL,checked_at TEXT NOT NULL,modified_hint TEXT,etag TEXT,last_modified TEXT,content_hash TEXT,http_status INTEGER,error TEXT,local_path TEXT,authoritative INTEGER NOT NULL DEFAULT 1);
    CREATE VIRTUAL TABLE pages_fts USING fts5(url UNINDEXED,title,body,source UNINDEXED,tokenize='porter unicode61');
    CREATE TABLE runs(id INTEGER PRIMARY KEY,started_at TEXT,finished_at TEXT,pages_ok INTEGER,pages_failed INTEGER,config_hash TEXT);
    """)
    imported = 0
    for path in sorted((ROOT / "data/pages").glob("*.md")):
        parsed = parse_page(path)
        if not parsed:
            continue
        metadata, title, body = parsed
        url = metadata.get("url")
        source = metadata.get("source")
        fetched = metadata.get("fetched_at")
        if not url or not source or not fetched:
            continue
        relative = path.relative_to(ROOT).as_posix()
        digest = hashlib.sha256(body.encode()).hexdigest()
        connection.execute("INSERT INTO pages VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,1)", (url, source, title, body, fetched, fetched, "", None, None, digest, 200, None, relative))
        connection.execute("INSERT INTO pages_fts VALUES(?,?,?,?)", (url, title, body, source))
        imported += 1
        if imported % 1000 == 0:
            connection.commit()
            print(f"Indexed {imported} pages")
    connection.commit()
    connection.execute("INSERT INTO runs(started_at,finished_at,pages_ok,pages_failed,config_hash) VALUES(datetime('now'),datetime('now'),?,0,'rebuilt-from-committed-pages')", (imported,))
    connection.commit()
    print(f"Rebuilt {DB} with {imported} official pages")


if __name__ == "__main__":
    main()

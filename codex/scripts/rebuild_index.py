#!/usr/bin/env python3
"""Rebuild the searchable SQLite index from committed official page files."""
from __future__ import annotations

import hashlib
import json
import re
import sqlite3
import time
from email import policy
from email.parser import BytesParser
from email.utils import parsedate_to_datetime, parseaddr
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
    CREATE TABLE browser_imports(id INTEGER PRIMARY KEY,source TEXT,imported_at TEXT,capture_sha256 TEXT,records INTEGER,invalid INTEGER,receipt_path TEXT);
    CREATE TABLE url_replacements(stale_url TEXT PRIMARY KEY,replacement_url TEXT NOT NULL,method TEXT NOT NULL,verified_at TEXT NOT NULL,stale_http_status INTEGER,replacement_content_hash TEXT NOT NULL,candidate_count INTEGER NOT NULL);
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

    koi = ROOT / "data/koi-official"
    manifest_path = koi / "manifest.json"
    manifest = json.loads(manifest_path.read_bytes())
    manifest_records = {record["url"]: record for record in manifest.get("records", [])}
    verified_koi = 0
    for url, record in manifest_records.items():
        if record.get("status") != "downloaded":
            continue
        path = koi / "docs" / record["relative_path"]
        raw = path.read_bytes()
        normalized = raw.replace(b"\r\n", b"\n")
        digest = hashlib.sha256(normalized).hexdigest()
        if digest != record.get("sha256"):
            raise SystemExit(f"KOI hash mismatch: {path}")
        body = normalized.decode("utf-8", "replace")
        title_match = re.search(r"(?m)^#\s+(.+?)\s*$", body)
        title = record.get("title") or (title_match.group(1).strip() if title_match else path.stem)
        fetched = record.get("downloaded_at") or manifest.get("generated_at")
        relative = path.relative_to(ROOT).as_posix()
        inserted = connection.execute("INSERT OR IGNORE INTO pages VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,1)", (url, "koi-official-export", title, body, fetched, fetched, manifest.get("generated_at", ""), None, None, digest, record.get("http_status") or 200, None, relative)).rowcount
        if inserted:
            connection.execute("INSERT INTO pages_fts VALUES(?,?,?,?)", (url, title, body, "koi-official-export"))
        verified_koi += 1

    receipt_path = koi / "recovered/recovery-receipt.json"
    receipt = json.loads(receipt_path.read_bytes())
    recovered_koi = 0
    for record in receipt.get("pages", []):
        url = record["url"]
        if url not in manifest_records or manifest_records[url].get("status") == "downloaded":
            raise SystemExit(f"Unexpected KOI recovery URL: {url}")
        path = ROOT / record["local_path"]
        raw = path.read_bytes()
        normalized = raw.replace(b"\r\n", b"\n")
        digest = hashlib.sha256(normalized).hexdigest()
        if digest != record["sha256"]:
            raise SystemExit(f"KOI recovery hash mismatch: {path}")
        body = normalized.decode("utf-8", "replace")
        title_match = re.search(r"(?m)^#\s+(.+?)\s*$", body)
        title = title_match.group(1).strip() if title_match else path.stem
        fetched = manifest.get("generated_at")
        inserted = connection.execute("INSERT OR IGNORE INTO pages VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,1)", (url, "koi-official-recovered", title, body, fetched, fetched, "Recovered from verified receipt", None, None, digest, 200, None, record["local_path"],)).rowcount
        if inserted:
            connection.execute("INSERT INTO pages_fts VALUES(?,?,?,?)", (url, title, body, "koi-official-recovered"))
        recovered_koi += 1

    expected_failed = sum(record.get("status") != "downloaded" for record in manifest_records.values())
    if recovered_koi != expected_failed:
        raise SystemExit(f"KOI recovery count mismatch: recovered {recovered_koi}, expected {expected_failed}")

    for receipt_path in sorted((ROOT / "data/idira-browser-imports").glob("receipt-*.json")):
        receipt = json.loads(receipt_path.read_bytes())
        for record in receipt.get("records", []):
            found = connection.execute(
                "SELECT content_hash FROM pages WHERE url=? AND source='idira-docs'", (record["url"],)
            ).fetchone()
            if not found or found[0] != record["sha256"]:
                raise SystemExit(f"Idira receipt mismatch: {record['url']}")
        connection.execute(
            "INSERT INTO browser_imports(source,imported_at,capture_sha256,records,invalid,receipt_path) VALUES(?,?,?,?,?,?)",
            ("idira-docs", receipt["imported_at"], receipt["capture_sha256"], len(receipt.get("records", [])),
             receipt.get("invalid", 0), receipt_path.relative_to(ROOT).as_posix()),
        )

    replacement_receipts = sorted((ROOT / "data/url-replacements").glob("replacement-map-*.json"))
    if replacement_receipts:
        replacement_receipt = json.loads(replacement_receipts[-1].read_bytes())
        for record in replacement_receipt.get("records", []):
            found = connection.execute(
                "SELECT content_hash FROM pages WHERE url=? AND http_status BETWEEN 200 AND 299 AND body<>''", (record["replacement_url"],)
            ).fetchone()
            # The receipt hash proves what was verified when the stale URL was
            # resolved. The live replacement page may legitimately change in a
            # later refresh, so rebuilds require a current non-empty 2xx page
            # without incorrectly freezing its content forever.
            if not found:
                raise SystemExit(f"Replacement receipt mismatch: {record['replacement_url']}")
            connection.execute(
                "INSERT INTO url_replacements VALUES(:stale_url,:replacement_url,:method,:verified_at,:stale_http_status,:replacement_content_hash,:candidate_count)",
                record,
            )
    connection.commit()
    email_paths = sorted((ROOT / "data/field-evidence/raw").glob("*.eml"))
    if email_paths:
        from import_field_emails import body as email_body, dec, tier, top_post
        connection.executescript("""CREATE TABLE IF NOT EXISTS field_evidence(id TEXT PRIMARY KEY,thread TEXT,subject TEXT,sent_at TEXT,sender_name TEXT,sender_address TEXT,evidence_tier TEXT,body TEXT,file_hash TEXT,local_path TEXT,attachment_manifest TEXT,imported_at TEXT);
        CREATE VIRTUAL TABLE IF NOT EXISTS field_fts USING fts5(id UNINDEXED,subject,body,evidence_tier UNINDEXED,tokenize='porter unicode61');""")
    for email_path in email_paths:
        raw = email_path.read_bytes()
        message = BytesParser(policy=policy.default).parsebytes(raw)
        digest = hashlib.sha256(raw).hexdigest()
        message_id = dec(message.get("Message-ID")).strip() or "sha256:" + digest
        sender_name, sender_address = parseaddr(dec(message.get("From")))
        try:
            sent_at = parsedate_to_datetime(dec(message.get("Date"))).isoformat()
        except (TypeError, ValueError):
            sent_at = dec(message.get("Date"))
        subject = dec(message.get("Subject"))
        evidence_tier = tier(sender_address)
        text = top_post(email_body(message))
        attachments = []
        for part in message.walk():
            if part.is_multipart():
                continue
            filename = dec(part.get_filename())
            if filename or part.get_content_disposition() == "attachment":
                payload = part.get_payload(decode=True) or b""
                attachments.append({"name": filename or "unnamed", "type": part.get_content_type(), "bytes": len(payload), "sha256": hashlib.sha256(payload).hexdigest()})
        imported_at = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(email_path.stat().st_mtime))
        local_path = email_path.relative_to(ROOT).as_posix()
        connection.execute("INSERT INTO field_evidence VALUES(?,?,?,?,?,?,?,?,?,?,?,?)", (message_id, "KOI Agent Hooks", subject, sent_at, sender_name, sender_address, evidence_tier, text, digest, local_path, json.dumps(attachments, ensure_ascii=False), imported_at))
        connection.execute("INSERT INTO field_fts VALUES(?,?,?,?)", (message_id, subject, text, evidence_tier))
    connection.commit()
    connection.execute("INSERT INTO runs(started_at,finished_at,pages_ok,pages_failed,config_hash) VALUES(datetime('now'),datetime('now'),?,0,'rebuilt-from-committed-pages')", (imported,))
    connection.commit()
    print(f"Rebuilt {DB} with {imported} web pages, {verified_koi} verified KOI pages, and {recovered_koi} recovered KOI pages")


if __name__ == "__main__":
    main()

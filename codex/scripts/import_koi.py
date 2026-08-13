#!/usr/bin/env python3
"""Verify and import an official KOI Markdown export without modifying its source."""
from __future__ import annotations
import argparse, hashlib, json, re, shutil, sqlite3, time
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]; DATA=ROOT/"data"; DB=DATA/"index.sqlite3"; DEST=DATA/"koi-official"
def now(): return time.strftime("%Y-%m-%dT%H:%M:%SZ",time.gmtime())
def setup(c):
    c.executescript("""PRAGMA journal_mode=WAL;
    CREATE TABLE IF NOT EXISTS pages(url TEXT PRIMARY KEY,source TEXT NOT NULL,title TEXT,body TEXT,fetched_at TEXT NOT NULL,checked_at TEXT NOT NULL,modified_hint TEXT,etag TEXT,last_modified TEXT,content_hash TEXT,http_status INTEGER,error TEXT,local_path TEXT,authoritative INTEGER NOT NULL DEFAULT 1);
    CREATE VIRTUAL TABLE IF NOT EXISTS pages_fts USING fts5(url UNINDEXED,title,body,source UNINDEXED,tokenize='porter unicode61');
    CREATE TABLE IF NOT EXISTS local_imports(id INTEGER PRIMARY KEY,source TEXT,imported_at TEXT,manifest_generated_at TEXT,verified INTEGER,missing INTEGER,invalid INTEGER,manifest_hash TEXT);""")
def title_of(text,path):
    m=re.search(r"(?m)^#\s+(.+?)\s*$",text); return m.group(1).strip() if m else path.stem.replace("-"," ").title()
def main():
    p=argparse.ArgumentParser(); p.add_argument("source",help="KOI export directory containing manifest.json and docs/"); a=p.parse_args(); src=Path(a.source).resolve(); manifest_path=src/"manifest.json"
    if not manifest_path.is_file() or not (src/"docs").is_dir(): raise SystemExit("Expected manifest.json and docs/ in KOI export")
    manifest_bytes=manifest_path.read_bytes(); manifest=json.loads(manifest_bytes); stamp=now(); DATA.mkdir(exist_ok=True); DEST.mkdir(parents=True,exist_ok=True); c=sqlite3.connect(DB); setup(c); verified=missing=invalid=0
    for rec in manifest.get("records",[]):
        url=rec.get("url",""); rel=rec.get("relative_path",""); status=rec.get("status")
        if not url.startswith("https://docs.koi.ai/") or not rel or Path(rel).is_absolute() or ".." in Path(rel).parts: invalid+=1; continue
        source_file=src/"docs"/Path(rel); dest_file=DEST/"docs"/Path(rel)
        if status!="downloaded":
            missing+=1
            c.execute("""INSERT INTO pages(url,source,title,body,fetched_at,checked_at,modified_hint,etag,last_modified,content_hash,http_status,error,local_path,authoritative) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,1)
              ON CONFLICT(url) DO UPDATE SET checked_at=excluded.checked_at,error=excluded.error,http_status=excluded.http_status""",
              (url,"koi-official-export",rec.get("title") or "","",rec.get("downloaded_at") or stamp,stamp,"","",None,None,rec.get("http_status") or 0,rec.get("error") or "missing from export",None)); continue
        if not source_file.is_file(): invalid+=1; continue
        raw=source_file.read_bytes(); digest=hashlib.sha256(raw).hexdigest()
        if digest!=rec.get("sha256"): invalid+=1; continue
        text=raw.decode("utf-8","replace"); dest_file.parent.mkdir(parents=True,exist_ok=True); shutil.copy2(source_file,dest_file); verified+=1
        local=str(dest_file.relative_to(ROOT)).replace("\\","/"); fetched=rec.get("downloaded_at") or manifest.get("generated_at") or stamp; title=rec.get("title") or title_of(text,source_file)
        c.execute("""INSERT INTO pages(url,source,title,body,fetched_at,checked_at,modified_hint,etag,last_modified,content_hash,http_status,error,local_path,authoritative) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,1)
          ON CONFLICT(url) DO UPDATE SET source=excluded.source,title=excluded.title,body=excluded.body,fetched_at=excluded.fetched_at,checked_at=excluded.checked_at,content_hash=excluded.content_hash,http_status=excluded.http_status,error=NULL,local_path=excluded.local_path,authoritative=1""",
          (url,"koi-official-export",title,text,fetched,stamp,manifest.get("generated_at") or "",None,None,digest,rec.get("http_status") or 200,None,local))
        c.execute("DELETE FROM pages_fts WHERE url=?",(url,)); c.execute("INSERT INTO pages_fts VALUES(?,?,?,?)",(url,title,text,"koi-official-export"))
    for name in ("manifest.json","KOI_INDEX.md","KOI_missing_pages_clean.md","PROJECT_INSTRUCTIONS.md","AGENTS.md"):
        f=src/name
        if f.is_file(): shutil.copy2(f,DEST/name)
    c.execute("INSERT INTO local_imports(source,imported_at,manifest_generated_at,verified,missing,invalid,manifest_hash) VALUES(?,?,?,?,?,?,?)",("koi-official-export",stamp,manifest.get("generated_at"),verified,missing,invalid,hashlib.sha256(manifest_bytes).hexdigest())); c.commit()
    result={"verified_and_imported":verified,"missing_in_export":missing,"invalid_or_hash_mismatch":invalid,"manifest_generated_at":manifest.get("generated_at"),"destination":str(DEST)}; print(json.dumps(result,indent=2))
    if invalid: raise SystemExit(1)
if __name__=="__main__": main()

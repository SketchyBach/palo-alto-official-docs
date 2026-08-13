#!/usr/bin/env python3
"""Import an exact recovery bundle for KOI records marked failed in manifest.json."""
from __future__ import annotations
import argparse, hashlib, json, re, shutil, sqlite3, time
from datetime import datetime, timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; DATA=ROOT/"data"; DB=DATA/"index.sqlite3"; KOI=DATA/"koi-official"
URL_RE=re.compile(r"(?m)^Source:\s+(https://docs\.koi\.ai/\S+\.md)\s*$",re.I)
def now(): return time.strftime("%Y-%m-%dT%H:%M:%SZ",time.gmtime())
def main():
    p=argparse.ArgumentParser(); p.add_argument("bundle"); a=p.parse_args(); bundle=Path(a.bundle).resolve()
    manifest=json.loads((KOI/"manifest.json").read_bytes()); expected={r["url"]:r for r in manifest["records"] if r.get("status")!="downloaded"}; raw=bundle.read_bytes(); text=raw.decode("utf-8","replace"); matches=list(URL_RE.finditer(text)); found={}
    for i,m in enumerate(matches):
        url=m.group(1); start=m.start(); end=matches[i+1].start() if i+1<len(matches) else len(text); body=text[start:end].strip()+"\n"
        if url in found: raise SystemExit(f"Duplicate page in recovery bundle: {url}")
        if len(body)<200 or not re.search(r"(?m)^#\s+\S",body): raise SystemExit(f"Incomplete recovered page: {url}")
        found[url]=body
    missing=sorted(set(expected)-set(found)); unexpected=sorted(set(found)-set(expected))
    if missing or unexpected: raise SystemExit(json.dumps({"missing_expected":missing,"unexpected":unexpected},indent=2))
    recovery=KOI/"recovered"; recovery.mkdir(parents=True,exist_ok=True); shutil.copy2(bundle,recovery/bundle.name); c=sqlite3.connect(DB); imported=[]
    # Archive extraction can rewrite file timestamps; use the export manifest date conservatively.
    fetched=manifest.get("generated_at") or now()
    for url,body in found.items():
        rec=expected[url]; rel=Path("data/koi-official/recovered/docs")/Path(rec["relative_path"]); dest=ROOT/rel; dest.parent.mkdir(parents=True,exist_ok=True); dest.write_text(body,encoding="utf-8"); digest=hashlib.sha256(body.encode("utf-8")).hexdigest(); title=(re.search(r"(?m)^#\s+(.+?)\s*$",body).group(1)).strip()
        c.execute("""UPDATE pages SET source=?,title=?,body=?,fetched_at=?,checked_at=?,modified_hint=?,content_hash=?,http_status=200,error=NULL,local_path=?,authoritative=1 WHERE url=?""",("koi-official-recovered",title,body,fetched,now(),"Recovered from official Markdown responses; original manifest record was unavailable",digest,str(rel).replace("\\","/"),url)); c.execute("DELETE FROM pages_fts WHERE url=?",(url,)); c.execute("INSERT INTO pages_fts VALUES(?,?,?,?)",(url,title,body,"koi-official-recovered")); imported.append({"url":url,"sha256":digest,"local_path":str(rel).replace("\\","/")})
    receipt={"imported_at":now(),"bundle":str(bundle),"bundle_sha256":hashlib.sha256(raw).hexdigest(),"pages":imported}; (recovery/"recovery-receipt.json").write_text(json.dumps(receipt,indent=2),encoding="utf-8"); c.commit(); print(json.dumps({"recovered":len(imported),"bundle_sha256":receipt["bundle_sha256"],"receipt":str(recovery/"recovery-receipt.json")},indent=2))
if __name__=="__main__": main()

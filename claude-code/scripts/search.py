#!/usr/bin/env python3
import argparse,json,re,sqlite3,sys
from datetime import datetime,timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; DB=ROOT/"data/index.sqlite3"
def main():
    if hasattr(sys.stdout,"reconfigure"): sys.stdout.reconfigure(encoding="utf-8",errors="replace")
    p=argparse.ArgumentParser(); p.add_argument("query",nargs="+"); p.add_argument("--limit",type=int); p.add_argument("--source"); p.add_argument("--json",action="store_true"); p.add_argument("--any",action="store_true",help="Match any term instead of requiring all terms"); p.add_argument("--mode",choices=("answer","integration"),default="answer"); p.add_argument("--include-field",action="store_true",help="Append clearly labeled non-authoritative troubleshooting correspondence"); a=p.parse_args(); limit=a.limit or (5 if a.mode=="answer" else 12)
    if not DB.exists(): raise SystemExit("Corpus not initialized; run scripts/ingest.py")
    tokens=re.findall(r"[A-Za-z0-9_.-]+"," ".join(a.query)); joiner=" OR " if a.any else " AND "; fts=joiner.join(f'"{t}"' for t in tokens) or '""'; sql="SELECT p.url,p.title,p.source,p.fetched_at,p.checked_at,p.modified_hint,p.local_path,p.content_hash,p.http_status,p.error,p.authoritative,snippet(pages_fts,2,'[[',']]',' … ',32),bm25(pages_fts,10.0,1.0) FROM pages_fts JOIN pages p ON p.url=pages_fts.url WHERE pages_fts MATCH ? AND p.authoritative=1 AND p.body<>'' AND p.error IS NULL AND p.url NOT LIKE '%/llms.txt'"; vals=[fts]
    if a.source: sql+=" AND p.source=?"; vals.append(a.source)
    sql+=" ORDER BY bm25(pages_fts,10.0,1.0) LIMIT ?"; vals.append(limit); rows=sqlite3.connect(DB).execute(sql,vals).fetchall(); now=datetime.now(timezone.utc); out=[]
    for u,t,s,f,checked,m,lp,digest,status,error,auth,snip,score in rows:
        age=(now-datetime.fromisoformat(f.replace('Z','+00:00'))).days; threshold=30 if s.startswith('koi-') else 14
        out.append({"title":t,"url":u,"source":s,"content_date":f,"integrity_checked_at":checked,"age_days":age,"freshness_threshold_days":threshold,"current_eligible":age<=threshold,"authoritative":bool(auth),"content_hash":digest,"http_status":status,"modified_hint":m,"local_path":lp,"evidence":snip,"rank":score})
    if a.include_field:
        try:
            field=sqlite3.connect(DB).execute("SELECT e.id,e.subject,e.sent_at,e.sender_name,e.evidence_tier,e.local_path,snippet(field_fts,2,'[[',']]',' … ',32),bm25(field_fts,8.0,1.0) FROM field_fts JOIN field_evidence e ON e.id=field_fts.id WHERE field_fts MATCH ? ORDER BY bm25(field_fts,8.0,1.0) LIMIT ?",(fts,limit)).fetchall()
            out.extend({"title":r[1],"url":None,"source":"field-email","content_date":r[2],"sender":r[3],"evidence_tier":r[4],"current_eligible":False,"authoritative":False,"local_path":r[5],"evidence":r[6],"rank":r[7]} for r in field)
        except sqlite3.OperationalError: pass
    if a.json: print(json.dumps(out,indent=2,ensure_ascii=False))
    elif not out: print("No verified local pages matched every query term. Use --any only for broader discovery, or refresh/import the relevant source.")
    else:
        for i,x in enumerate(out,1):
            if x["source"]=="field-email": print(f"[{i}] {x['title']}\nSource: field email | sender: {x['sender']} | tier: {x['evidence_tier']} | sent: {x['content_date']}\nAuthoritative: False\nEvidence: {x['evidence']}\n")
            else: print(f"[{i}] {x['title']}\nURL: {x['url']}\nSource: {x['source']} | content date: {x['content_date']} ({x['age_days']}d ago) | current eligible: {x['current_eligible']}\nEvidence: {x['evidence']}\n")
if __name__=="__main__": main()

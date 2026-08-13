#!/usr/bin/env python3
"""Import deduplicated EML top-posts as non-authoritative field evidence."""
import argparse, hashlib, json, re, shutil, sqlite3, sys, time
from email import policy
from email.header import decode_header, make_header
from email.parser import BytesParser
from email.utils import parsedate_to_datetime, parseaddr
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; DATA=ROOT/"data/field-evidence"; DB=ROOT/"data/index.sqlite3"
def dec(v):
    try:return str(make_header(decode_header(v or "")))
    except:return v or ""
def html_text(s):
    s=re.sub(r"(?is)<(script|style).*?>.*?</\1>","",s); s=re.sub(r"(?i)<br\s*/?>|</p>|</div>|</li>","\n",s); return re.sub(r"(?s)<[^>]+>"," ",s)
def body(msg):
    plain=[]; html=[]
    for part in msg.walk():
        if part.is_multipart() or part.get_content_disposition()=="attachment" or part.get_filename(): continue
        try:t=str(part.get_content())
        except:t=(part.get_payload(decode=True) or b"").decode(part.get_content_charset() or "utf-8","replace")
        if part.get_content_type()=="text/plain":plain.append(t)
        elif part.get_content_type()=="text/html":html.append(html_text(t))
    return "\n\n".join(plain).strip() or "\n\n".join(html).strip()
def top_post(text):
    cuts=[r"(?mi)^\s*On .{0,200}wrote:\s*$",r"(?mi)^\s*From:\s+",r"(?mi)^\s*מאת:\s*",r"(?m)^\s*-{5,}\s*Original Message\s*-{5,}",r"(?m)^\s*>+"]
    positions=[m.start() for p in cuts if (m:=re.search(p,text))]; text=text[:min(positions)] if positions else text
    text=re.sub(r"(?m)^\s*\[image:[^\]]+\]\s*$","",text); return re.sub(r"\n{3,}","\n\n",text).strip()
def tier(address):
    a=address.lower()
    if "mtarakin@paloaltonetworks.com" in a:return "support-derived-guidance"
    if "@paloaltonetworks.com" in a:return "vendor-correspondence"
    return "customer-observation-or-question"
def now():return time.strftime("%Y-%m-%dT%H:%M:%SZ",time.gmtime())
if __name__=="__main__":
    if hasattr(sys.stdout,"reconfigure"):sys.stdout.reconfigure(encoding="utf-8",errors="replace")
    p=argparse.ArgumentParser();p.add_argument("files",nargs="+");a=p.parse_args();DATA.mkdir(parents=True,exist_ok=True);(DATA/"raw").mkdir(exist_ok=True);c=sqlite3.connect(DB)
    c.executescript("""CREATE TABLE IF NOT EXISTS field_evidence(id TEXT PRIMARY KEY,thread TEXT,subject TEXT,sent_at TEXT,sender_name TEXT,sender_address TEXT,evidence_tier TEXT,body TEXT,file_hash TEXT,local_path TEXT,attachment_manifest TEXT,imported_at TEXT);
    CREATE VIRTUAL TABLE IF NOT EXISTS field_fts USING fts5(id UNINDEXED,subject,body,evidence_tier UNINDEXED,tokenize='porter unicode61');"""); imported=duplicates=0
    for fn in a.files:
        src=Path(fn);raw=src.read_bytes();msg=BytesParser(policy=policy.default).parsebytes(raw);mid=dec(msg.get("Message-ID")).strip() or "sha256:"+hashlib.sha256(raw).hexdigest(); exists=c.execute("SELECT 1 FROM field_evidence WHERE id=?",(mid,)).fetchone()
        if exists:duplicates+=1;continue
        sender=dec(msg.get("From"));sender_name,sender_address=parseaddr(sender);text=top_post(body(msg));attachments=[]
        for part in msg.walk():
            if part.is_multipart():continue
            fn2=dec(part.get_filename());disp=part.get_content_disposition()
            if fn2 or disp=="attachment":
                payload=part.get_payload(decode=True) or b"";attachments.append({"name":fn2 or "unnamed","type":part.get_content_type(),"bytes":len(payload),"sha256":hashlib.sha256(payload).hexdigest()})
        digest=hashlib.sha256(raw).hexdigest();dest=DATA/"raw"/(digest+".eml");shutil.copy2(src,dest)
        try:sent=parsedate_to_datetime(dec(msg.get("Date"))).isoformat()
        except:sent=dec(msg.get("Date"))
        subject=dec(msg.get("Subject"));ev=tier(sender_address);c.execute("INSERT INTO field_evidence VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",(mid,"KOI Agent Hooks",subject,sent,sender_name,sender_address,ev,text,digest,str(dest.relative_to(ROOT)).replace('\\','/'),json.dumps(attachments,ensure_ascii=False),now()));c.execute("INSERT INTO field_fts VALUES(?,?,?,?)",(mid,subject,text,ev));imported+=1
    c.commit();print(json.dumps({"imported":imported,"duplicates_skipped":duplicates,"total":c.execute("SELECT count(*) FROM field_evidence").fetchone()[0],"by_tier":dict(c.execute("SELECT evidence_tier,count(*) FROM field_evidence GROUP BY evidence_tier"))},indent=2))

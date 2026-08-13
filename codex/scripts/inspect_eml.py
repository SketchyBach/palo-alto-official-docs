#!/usr/bin/env python3
"""Read-only EML inventory: headers, plain text, and attachment metadata."""
import argparse, hashlib, json, re, sys
from email import policy
from email.parser import BytesParser
from email.header import decode_header, make_header
from pathlib import Path
def dec(v):
    try: return str(make_header(decode_header(v or "")))
    except Exception: return v or ""
def clean_html(s):
    s=re.sub(r"(?is)<(script|style).*?>.*?</\1>","",s); s=re.sub(r"(?i)<br\s*/?>|</p>|</div>|</li>","\n",s); s=re.sub(r"(?s)<[^>]+>"," ",s); return re.sub(r"\n{3,}","\n\n",s).strip()
if __name__=="__main__":
    if hasattr(sys.stdout,"reconfigure"): sys.stdout.reconfigure(encoding="utf-8",errors="replace")
    p=argparse.ArgumentParser(); p.add_argument("files",nargs="+"); p.add_argument("--summary",action="store_true"); a=p.parse_args(); result=[]
    for name in a.files:
        path=Path(name); raw=path.read_bytes(); msg=BytesParser(policy=policy.default).parsebytes(raw); plains=[]; htmls=[]; at=[]
        for part in msg.walk():
            if part.is_multipart(): continue
            ctype=part.get_content_type(); disp=part.get_content_disposition(); fn=dec(part.get_filename())
            payload=part.get_payload(decode=True) or b""
            if disp=="attachment" or fn:
                at.append({"name":fn or "unnamed","content_type":ctype,"bytes":len(payload),"sha256":hashlib.sha256(payload).hexdigest()}); continue
            try: text=part.get_content()
            except Exception: text=payload.decode(part.get_content_charset() or "utf-8","replace")
            if ctype=="text/plain": plains.append(str(text))
            elif ctype=="text/html": htmls.append(clean_html(str(text)))
        body="\n\n".join(plains).strip() or "\n\n".join(htmls).strip()
        result.append({"file":str(path),"file_sha256":hashlib.sha256(raw).hexdigest(),"message_id":dec(msg.get("Message-ID")),"in_reply_to":dec(msg.get("In-Reply-To")),"references":dec(msg.get("References")),"date":dec(msg.get("Date")),"from":dec(msg.get("From")),"to":dec(msg.get("To")),"cc":dec(msg.get("Cc")),"subject":dec(msg.get("Subject")),"body_chars":len(body),"body_preview":body[:1200] if a.summary else None,"body":None if a.summary else body,"attachments":at})
    print(json.dumps(result,indent=2,ensure_ascii=False))

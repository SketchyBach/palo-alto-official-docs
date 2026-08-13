#!/usr/bin/env python3
"""Incrementally crawl allowlisted official Palo Alto and Idira documentation into SQLite."""
from __future__ import annotations
import argparse, hashlib, html, json, re, sqlite3, time
from html.parser import HTMLParser
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urldefrag, urljoin, urlparse
from urllib.request import Request, urlopen
from urllib.robotparser import RobotFileParser

ROOT=Path(__file__).resolve().parents[1]; DATA=ROOT/"data"; DB=DATA/"index.sqlite3"; PAGES=DATA/"pages"

class PageParser(HTMLParser):
    SKIP={"script","style","svg","noscript","template"}; BLOCK={"p","div","section","article","main","li","tr","h1","h2","h3","h4","pre","br"}
    def __init__(self):
        super().__init__(convert_charrefs=True); self.skip=0; self.parts=[]; self.links=[]; self.title=""; self.in_title=False; self.title_parts=[]; self.meta={}
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag in self.SKIP: self.skip+=1
        if tag=="title": self.in_title=True
        if tag=="a" and a.get("href"): self.links.append(a["href"])
        if tag=="meta":
            key=(a.get("name") or a.get("property") or "").lower()
            if key and a.get("content"): self.meta[key]=a["content"]
        if not self.skip and tag in self.BLOCK: self.parts.append("\n")
    def handle_endtag(self,tag):
        if tag in self.SKIP and self.skip: self.skip-=1
        if tag=="title": self.in_title=False; self.title=" ".join(self.title_parts).strip()
        if not self.skip and tag in self.BLOCK: self.parts.append("\n")
    def handle_data(self,data):
        if self.in_title: self.title_parts.append(data)
        if not self.skip: self.parts.append(data)
    def text(self):
        value=html.unescape(" ".join(self.parts)); value=re.sub(r"[ \t\r\f\v]+"," ",value); return re.sub(r"\n\s*\n+","\n\n",value).strip()

class TextPage:
    def __init__(self,text,url):
        self._text=text.strip(); self.links=re.findall(r"https?://[^\s)>\]]+",text); self.meta={}; m=re.search(r"(?m)^#\s+(.+?)\s*$",text); self.title=m.group(1).strip() if m else Path(urlparse(url).path).name or url
    def text(self): return self._text

def now(): return time.strftime("%Y-%m-%dT%H:%M:%SZ",time.gmtime())
def setup(c):
    c.executescript("""PRAGMA journal_mode=WAL;
    CREATE TABLE IF NOT EXISTS pages(url TEXT PRIMARY KEY,source TEXT NOT NULL,title TEXT,body TEXT,fetched_at TEXT NOT NULL,checked_at TEXT NOT NULL,modified_hint TEXT,etag TEXT,last_modified TEXT,content_hash TEXT,http_status INTEGER,error TEXT,local_path TEXT,authoritative INTEGER NOT NULL DEFAULT 1);
    CREATE VIRTUAL TABLE IF NOT EXISTS pages_fts USING fts5(url UNINDEXED,title,body,source UNINDEXED,tokenize='porter unicode61');
    CREATE TABLE IF NOT EXISTS runs(id INTEGER PRIMARY KEY,started_at TEXT,finished_at TEXT,pages_ok INTEGER,pages_failed INTEGER,config_hash TEXT);""")
def canonical(raw,base):
    u=urldefrag(urljoin(base,raw))[0]; p=urlparse(u)
    if p.scheme not in {"http","https"}: return None
    return p._replace(scheme="https",path=re.sub(r"/{2,}","/",p.path or "/"),fragment="").geturl()
def allowed(u,domains,prefixes):
    p=urlparse(u)
    return p.hostname in domains and not p.query and not re.search(r"\.(?:png|jpe?g|gif|svg|css|js|zip|mp4|woff2?|ico|pdf)$",p.path,re.I) and any(u.startswith(x) for x in prefixes)
def robot(domain):
    url=f"https://{domain}/robots.txt"
    try:
        with urlopen(Request(url,headers={"User-Agent":"Mozilla/5.0"}),timeout=20) as res: lines=res.read().decode("utf-8","replace").splitlines()
        r=RobotFileParser(); r.set_url(url); r.parse(lines); return r
    except Exception: return None
def fetch(u,agent,prior):
    h={"User-Agent":agent,"Accept":"text/html,application/xhtml+xml"}
    if prior:
        if prior[0]: h["If-None-Match"]=prior[0]
        if prior[1]: h["If-Modified-Since"]=prior[1]
    try:
        with urlopen(Request(u,headers=h),timeout=40) as res: return res.status,res.read(12_000_000),res.headers
    except HTTPError as e:
        if e.code==304: return 304,b"",e.headers
        raise
def sitemap_urls(domain,agent,prefixes):
    """Return allowlisted page URLs from a sitemap or sitemap index."""
    pending=[f"https://{domain}/sitemap.xml"]; seen=set(); pages=[]
    while pending and len(seen)<100:
        sm=pending.pop(0)
        if sm in seen: continue
        seen.add(sm)
        try:
            with urlopen(Request(sm,headers={"User-Agent":agent}),timeout=40) as res: raw=res.read(20_000_000).decode("utf-8","replace")
        except Exception: continue
        locs=[html.unescape(x.strip()) for x in re.findall(r"<loc>(.*?)</loc>",raw,re.I|re.S)]
        for loc in locs:
            if "sitemap" in urlparse(loc).path.lower() and loc.lower().endswith(".xml"): pending.append(loc)
            elif any(loc.startswith(p) for p in prefixes): pages.append(loc)
    return pages
def save(c,u,source,status,parser,headers,error=None):
    stamp=now(); old=c.execute("SELECT fetched_at,local_path FROM pages WHERE url=?",(u,)).fetchone()
    if status==304 and old: c.execute("UPDATE pages SET checked_at=?,http_status=304,error=NULL WHERE url=?",(stamp,u)); return
    body=parser.text() if parser else ""; title=(parser.title or parser.meta.get("og:title","")).strip() if parser else ""; digest=hashlib.sha256(body.encode()).hexdigest() if body else None
    rel=str(Path("data/pages")/(hashlib.sha256(u.encode()).hexdigest()[:20]+".md"))
    if body: (ROOT/rel).write_text(f"---\nurl: {u}\nfetched_at: {stamp}\nsource: {source}\n---\n\n# {title}\n\n{body}\n",encoding="utf-8")
    hint=(parser.meta.get("article:modified_time") or parser.meta.get("last-modified") or parser.meta.get("date") or "") if parser else ""
    c.execute("""INSERT INTO pages VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,1) ON CONFLICT(url) DO UPDATE SET source=excluded.source,title=COALESCE(NULLIF(excluded.title,''),pages.title),body=COALESCE(NULLIF(excluded.body,''),pages.body),fetched_at=excluded.fetched_at,checked_at=excluded.checked_at,modified_hint=COALESCE(NULLIF(excluded.modified_hint,''),pages.modified_hint),etag=COALESCE(excluded.etag,pages.etag),last_modified=COALESCE(excluded.last_modified,pages.last_modified),content_hash=COALESCE(excluded.content_hash,pages.content_hash),http_status=excluded.http_status,error=excluded.error,local_path=COALESCE(excluded.local_path,pages.local_path)""",
      (u,source,title,body,stamp if body else (old[0] if old else stamp),stamp,hint,headers.get("ETag") if headers else None,headers.get("Last-Modified") if headers else None,digest,status,error,rel if body else (old[1] if old else None)))
    c.execute("DELETE FROM pages_fts WHERE url=?",(u,))
    if body: c.execute("INSERT INTO pages_fts VALUES(?,?,?,?)",(u,title,body,source))
def main():
    a=argparse.ArgumentParser(); a.add_argument("--config",default=str(ROOT/"sources.json")); a.add_argument("--source",action="append"); a.add_argument("--url",action="append",help="Refresh only an exact allowlisted URL; repeatable"); a.add_argument("--max-pages",type=int,default=500); a.add_argument("--max-depth",type=int,default=8); x=a.parse_args()
    raw=Path(x.config).read_bytes(); cfg=json.loads(raw); pol=cfg["policy"]; domains=set(pol["allowed_domains"]); selected=[s for s in cfg["sources"] if not x.source or s["name"] in x.source]; prefixes=[p for s in selected for p in s["include_prefixes"]]; queue=[(u,s["name"],0) for s in selected for u in s["seed_urls"]]
    for s in selected:
        source_prefixes=s["include_prefixes"]
        for domain in sorted({urlparse(u).hostname for u in s["seed_urls"]}):
            queue.extend((u,s["name"],0) for u in sitemap_urls(domain,pol["user_agent"],source_prefixes))
    if x.url:
        queue=[]
        for u in x.url:
            match=next((s for s in selected if any(u.startswith(p) for p in s["include_prefixes"])),None)
            if not match: raise SystemExit(f"URL is outside selected source prefixes: {u}")
            queue.append((u,match["name"],0))
    DATA.mkdir(exist_ok=True); PAGES.mkdir(parents=True,exist_ok=True); c=sqlite3.connect(DB); setup(c); rid=c.execute("INSERT INTO runs(started_at,config_hash) VALUES(?,?)",(now(),hashlib.sha256(raw).hexdigest())).lastrowid; robots={d:robot(d) for d in domains}; seen=set(); ok=failed=0
    while queue and len(seen)<x.max_pages:
        u,source,depth=queue.pop(0); u=canonical(u,u)
        if not u or u in seen or not allowed(u,domains,prefixes): continue
        seen.add(u); rp=robots.get(urlparse(u).hostname)
        if rp and not rp.can_fetch(pol["user_agent"],u): save(c,u,source,0,None,{},"blocked by robots.txt"); failed+=1; continue
        try:
            status,raw_page,headers=fetch(u,pol["user_agent"],c.execute("SELECT etag,last_modified FROM pages WHERE url=?",(u,)).fetchone())
            if status==304: save(c,u,source,status,None,headers); ok+=1; continue
            ctype=headers.get("Content-Type","").lower(); decoded=raw_page.decode("utf-8","replace")
            if "html" in ctype: parser=PageParser(); parser.feed(decoded)
            elif any(t in ctype for t in ("text/plain","text/markdown","markdown")) or u.lower().endswith((".md",".txt")): parser=TextPage(decoded,u)
            else: raise ValueError(f"unsupported content type: {ctype}")
            if len(parser.text())<120: raise ValueError("too little extractable text")
            save(c,u,source,status,parser,headers); ok+=1
            if depth<x.max_depth:
                for href in parser.links:
                    nxt=canonical(href,u)
                    if nxt and nxt not in seen and allowed(nxt,domains,prefixes): queue.append((nxt,source,depth+1))
        except Exception as e:
            # A single malformed/CDN response must never abort or corrupt an update run.
            save(c,u,source,getattr(e,"code",0) or 0,None,{},f"{type(e).__name__}: {e}"); failed+=1
        c.commit(); time.sleep(pol["request_delay_seconds"])
    c.execute("UPDATE runs SET finished_at=?,pages_ok=?,pages_failed=? WHERE id=?",(now(),ok,failed,rid)); c.commit(); print(json.dumps({"run_id":rid,"pages_checked":len(seen),"ok":ok,"failed":failed,"database":str(DB)},indent=2))
if __name__=="__main__": main()

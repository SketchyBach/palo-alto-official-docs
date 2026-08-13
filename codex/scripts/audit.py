#!/usr/bin/env python3
import json, sqlite3
from pathlib import Path
from urllib.parse import urlparse
root=Path(__file__).resolve().parents[1]; c=sqlite3.connect(root/"data/index.sqlite3")
rows=c.execute("SELECT url,source,local_path,body,error FROM pages").fetchall(); allowed={"cortex-docs.paloaltonetworks.com","docs.paloaltonetworks.com","docs.koi.ai"}
report={
 "records":len(rows), "body_records":sum(bool(r[3]) for r in rows), "fts_records":c.execute("SELECT count(*) FROM pages_fts").fetchone()[0],
 "duplicate_urls":c.execute("SELECT count(*) FROM (SELECT url FROM pages GROUP BY url HAVING count(*)>1)").fetchone()[0],
 "bad_hosts":sum(urlparse(r[0]).hostname not in allowed for r in rows),
 "missing_local_files":sum(bool(r[3]) and (not r[2] or not (root/r[2]).is_file()) for r in rows),
 "koi_unavailable":c.execute("SELECT count(*) FROM pages WHERE source='koi-official-export' AND error IS NOT NULL AND body='' ").fetchone()[0],
 "other_unavailable":c.execute("SELECT count(*) FROM pages WHERE source NOT IN ('koi-official-export','koi-official-recovered') AND error IS NOT NULL AND body='' ").fetchone()[0],
 "koi_recovered":c.execute("SELECT count(*) FROM pages WHERE source='koi-official-recovered' AND body<>'' AND error IS NULL").fetchone()[0]
}
report["passed"]=report["body_records"]==report["fts_records"] and not any(report[k] for k in ("duplicate_urls","bad_hosts","missing_local_files","koi_unavailable")) and report["koi_recovered"]==13
try:
 report["field_messages"]=c.execute("SELECT count(*) FROM field_evidence").fetchone()[0]; report["field_fts_records"]=c.execute("SELECT count(*) FROM field_fts").fetchone()[0]; report["passed"] = report["passed"] and report["field_messages"]==report["field_fts_records"]
except sqlite3.OperationalError: report["field_messages"]=report["field_fts_records"]=0
print(json.dumps(report,indent=2)); raise SystemExit(0 if report["passed"] else 1)

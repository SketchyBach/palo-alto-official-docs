#!/usr/bin/env python3
import json,sqlite3,sys
from pathlib import Path
if hasattr(sys.stdout,"reconfigure"): sys.stdout.reconfigure(encoding="utf-8",errors="replace")
db=Path(__file__).resolve().parents[1]/"data/index.sqlite3"
if not db.exists(): raise SystemExit("Corpus not initialized")
c=sqlite3.connect(db)
last_import=None
try: last_import=c.execute("SELECT source,imported_at,manifest_generated_at,verified,missing,invalid,manifest_hash FROM local_imports ORDER BY id DESC LIMIT 1").fetchone()
except sqlite3.OperationalError: pass
receipt=Path(__file__).resolve().parents[1]/"data/koi-official/recovered/recovery-receipt.json"
recovery=json.loads(receipt.read_text(encoding="utf-8")) if receipt.is_file() else None
try: field={"messages":c.execute("SELECT count(*) FROM field_evidence").fetchone()[0],"search_records":c.execute("SELECT count(*) FROM field_fts").fetchone()[0],"by_tier":dict(c.execute("SELECT evidence_tier,count(*) FROM field_evidence GROUP BY evidence_tier"))}
except sqlite3.OperationalError: field=None
print(json.dumps({"indexed_pages":c.execute("SELECT count(*) FROM pages WHERE body<>''").fetchone()[0],"unavailable_records":c.execute("SELECT count(*) FROM pages WHERE error IS NOT NULL AND body='' ").fetchone()[0],"by_source":dict(c.execute("SELECT source,count(*) FROM pages WHERE body<>'' GROUP BY source")),"field_evidence":field,"last_web_run":c.execute("SELECT id,started_at,finished_at,pages_ok,pages_failed FROM runs ORDER BY id DESC LIMIT 1").fetchone(),"last_local_import":last_import,"koi_recovery":{"imported_at":recovery.get("imported_at"),"pages":len(recovery.get("pages",[])),"bundle_sha256":recovery.get("bundle_sha256")} if recovery else None},indent=2))

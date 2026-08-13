---
url: https://docs.paloaltonetworks.com/ai-runtime-security/ai-red-teaming/identify-ai-system-risks-with-ai-red-teaming/get-started-with-prisma-airs-ai-red-teaming/targets/custom-target-adapters/adapter-contract/adapter-contract-examples
fetched_at: 2026-08-13T14:06:22Z
source: ai-security
---

# Adapter Contract Examples Clear

Adapter Contract Examples 

 Home 

 EN

 Location 

 Documentation Home 

 Palo Alto Networks 

 Support 

 Live Community 

 Knowledge Base 

 >

 Strata Copilot

 Adapter Contract Examples 

 Updated on 

 Fri Jul 24 03:07:12 PDT 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma AIRS Docs 

 Activation & Onboarding 

 Administration 

 AI Model Security 

 AI Red Teaming 

 Release Notes 

 New Features 

 Updated on 

 Fri Jul 24 03:07:12 PDT 2026 

 Focus 

 Home 

 Prisma AIRS 

 AI Red Teaming 

 Identify AI System Risks with AI Red Teaming 

 Get Started with Prisma AIRS AI Red Teaming 

 Targets 

 Custom Target Adapters 

 Adapter SDK Reference 

 Adapter Contract Examples 

 Download PDF 

 Prisma AIRS 

 Adapter Contract Examples 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma AIRS Docs 

 Activation & Onboarding 

 Administration 

 AI Model Security 

 AI Red Teaming 

 Release Notes 

 New Features 

 Previous 

 Error Signals 

 Next 

 Configure Authentication for a Target 

 Adapter Contract Examples 

 End-to-end adapter examples for common target types: a WebSocket target and an
 OAuth2 target with a stateful session. 

 Where Can I Use This? What Do I Need? 

 Prisma AIRS (AI Red Teaming) 

 AI Red Teaming License 

 Network Channel client v1.4.0 or
 later 

 Adapter sidecar
 enabled 

 WebSocket (call_target) 

 Uses the bundled websockets package to connect to a WebSocket
 target, send the prompt, and reassemble a streamed response frame by frame. 

 import json
import websockets.sync.client as ws

def call_target(context, inference_input):
 conn = ws.connect(
 context.vars["ws_url"],
 additional_headers={"Authorization": f"Bearer {context.auth['token']}"},
 )
 try:
 conn.send(json.dumps({"message": inference_input.prompt}))
 reply = ""
 for frame in conn:
 event = json.loads(frame)
 if event.get("type") == "chunk":
 reply += event["text"]
 elif event.get("type") == "done":
 break
 return CallTargetResult(output=reply)
 finally:
 conn.close() 

 OAuth2 and Stateful Session 

 A complete adapter for a target that requires OAuth2 client credentials, a
 server-side session created once per conversation, and a per-turn call that includes
 a UUID turn ID and a timestamp. 

 import time
import uuid

def authenticate(context):
 resp = context.http.post(
 context.vars["token_url"],
 data={
 "grant_type": "client_credentials",
 "client_id": context.secrets["client_id"],
 "client_secret": context.secrets["client_secret"],
 },
 )
 if resp.status_code != 200:
 raise_auth_error(f"token endpoint returned {resp.status_code}: {resp.text}")
 body = resp.json()
 return AuthResult(ttl=body.get("expires_in", 300), data={"token": body["access_token"]})

def session_pre_process(context):
 session_id = str(uuid.uuid4())
 resp = context.http.post(
 context.vars["session_url"],
 headers={"Authorization": f"Bearer {context.auth['token']}"},
 json={"session_id": session_id},
 )
 if resp.status_code not in (200, 201):
 raise_target_error(f"session create returned {resp.status_code}: {resp.text}")
 return SessionPreProcessResult(session_state={"session_id": session_id})

def call_target(context, inference_input):
 body = {
 "session_id": context.session["session_id"],
 "turn_id": str(uuid.uuid4()),
 "timestamp": int(time.time()),
 "prompt": inference_input.prompt,
 }
 if context.vars.get("model"):
 body["model"] = context.vars["model"]

 resp = context.http.post(
 context.vars["turn_url"],
 headers={"Authorization": f"Bearer {context.auth['token']}"},
 json=body,
 )
 if resp.status_code == 429:
 raise_rate_limited(retry_after=30)
 if resp.status_code == 401:
 raise_auth_error("turn rejected: token invalid or expired")
 if resp.status_code != 200:
 raise_target_error(f"turn endpoint returned {resp.status_code}: {resp.text}")
 return CallTargetResult(output=resp.json()["response"]) 

 Configuration for this example: 

 Variables: 
 token_url , session_url ,
 turn_url , model (optional) 

 Secrets: 
 client_id , client_secret 

 Previous 

 Error Signals 

 Next 

 Configure Authentication for a Target 

 On This Page 

 Activation & Onboarding 

 Strata Cloud Manager 

 Activate a License or Product 

 Cloud Identity Engine 

 Strata Logging Service 

 Device Associations 

 Hub 

 Identity and Access Management 

 Tenant Management 

 Next-Generation Firewalls 

 CN-Series 

 Firewalls 

 VM-Series 

 Cloud-Delivered Security Services 

 Advanced URL Filtering 

 Advanced Threat Prevention 

 Advanced DNS Security 

 Enterprise DLP 

 Network Security 

 Visibility & Monitoring 

 Dashboards 

 Incidents and Alerts 

 Reports 

 Autonomous DEM 

 AI Red Teaming 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

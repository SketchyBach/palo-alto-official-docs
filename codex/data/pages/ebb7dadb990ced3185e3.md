---
url: https://docs.paloaltonetworks.com/ai-runtime-security/ai-red-teaming/identify-ai-system-risks-with-ai-red-teaming/get-started-with-prisma-airs-ai-red-teaming/targets/custom-target-adapters/adapter-contract/adapter-contract-functions
fetched_at: 2026-08-13T14:06:18Z
source: ai-security
---

# Functions Clear

Functions 

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

 Functions 

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

 Functions 

 Download PDF 

 Prisma AIRS 

 Functions 

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

 Return Types 

 Next 

 Multi-Turn Conversations 

 Functions 

 Reference for each adapter function: when it runs, what it receives, what it
 returns, and a working code example. 

 Where Can I Use This? What Do I Need? 

 Prisma AIRS (AI Red Teaming) 

 AI Red Teaming License 

 Network Channel client v1.4.0 or
 later 

 Adapter sidecar
 enabled 

 pre_process(context, inference_input) 

 (Pattern A) Pattern A requires both pre_process() and
 post_process() . Returns the HTTP request details for AI Red
 Teaming to send to your target. AI Red Teaming makes the actual HTTP call and
 passes the response to post_process() . 

 Parameters 

 Input Parameter Type Description 

 context Context Object provided by AI Red Teaming exposing
 vars , secrets ,
 auth , session , and
 http . 

 inference_input InferenceInput The prompt and conversation history for the current
 turn. 

 Returns 

 PreProcessResult —The URL, headers, and body that AI Red
 Teaming sends to your target. url is the only required field.
 method defaults to POST . 

 Example 

 def pre_process(context, inference_input):
 return PreProcessResult(
 url=context.vars["endpoint"],
 headers={"Authorization": f"Bearer {context.secrets['api_key']}"},
 json_body={"message": inference_input.prompt},
 ) 

 post_process(context, raw_response) 

 (Pattern A) Pattern A requires both pre_process() and
 post_process() . Receives the HTTP response from AI Red Teaming
 and extracts the target's reply. 

 Parameters 

 Input Parameter Type Description 

 context Context Object provided by AI Red Teaming exposing
 vars , secrets ,
 auth , session , and
 http . 

 raw_response RawResponse The HTTP response returned by your target, including
 status_code , json_body , and
 headers . 

 Returns 

 PostProcessResult — output contains the
 reply text extracted from the target's HTTP response. For known failure conditions
 such as rate limiting or authentication errors, raise an error signal instead of
 returning error text as the reply. 

 Example 

 def post_process(context, raw_response):
 if raw_response.status_code == 429:
 raise_rate_limited(retry_after=30)
 return PostProcessResult(output=raw_response.json_body["reply"]) 

 call_target(context, inference_input) 

 (Pattern B) Pattern B requires only call_target() . Your
 adapter sends the request to the target and returns the reply directly to AI Red
 Teaming, without a separate post_process() step. Use
 call_target() instead of pre_process() and
 post_process() when the target uses a non-HTTP transport such
 as WebSocket, GraphQL, SDK-based clients, or custom framing and streaming protocols.
 For standard HTTP targets that require multiple calls, use
 context.http inside pre_process() instead. 

 Parameters 

 Input Parameter Type Description 

 context Context Object provided by AI Red Teaming exposing
 vars , secrets ,
 auth , session , and
 http . 

 inference_input InferenceInput The prompt and conversation history for the current
 turn. 

 Returns 

 CallTargetResult —The reply text and an optional session
 state update. Defining call_target() disables
 pre_process() and post_process() .
 authenticate() and session_pre_process() work
 identically with either pattern. 

 Example 

 def call_target(context, inference_input):
 resp = context.http.post(
 context.vars["endpoint"],
 headers={"Authorization": f"Bearer {context.secrets['api_key']}"},
 json={"message": inference_input.prompt},
 )
 return CallTargetResult(output=resp.json()["reply"]) 

 authenticate(context) 

 ( Optional ) ( Pattern A or B ) This function obtains and caches
 authentication credentials. AI Red Teaming calls this function, caches the result
 for the ttl you return, exposes it as context.auth 
 in your other functions, and re-authenticates automatically on expiry or on an
 authentication error (one retry). 

 Parameters 

 Input Parameter Type Description 

 context Context Object provided by AI Red Teaming exposing
 vars , secrets ,
 auth , session , and
 http . 

 Returns 

 AuthResult — The cached credentials and
 TTL. Per-request signing (HMAC, AWS SigV4, and similar) belongs in
 pre_process() or call_target() , not in
 authenticate() , because the specific request is not available
 inside this function. 

 Example 

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
 raise_auth_error(f"token endpoint returned {resp.status_code}")
 body = resp.json()
 return AuthResult(ttl=body["expires_in"], data={"token": body["access_token"]}) 

 session_pre_process(context) 

 ( Optional ) ( Pattern A or B ) Executes once on the first turn of
 every conversation. Use this function for one-time setup such as creating a
 server-side session. The returned session_state is available as
 context.session in pre_process() ,
 post_process() , and call_target() for that
 turn and every subsequent turn. 

 Parameters 

 Input Parameter Type Description 

 context Context Object provided by AI Red Teaming exposing
 vars , secrets ,
 auth , session , and
 http . 

 Returns 

 SessionPreProcessResult —Session state available as
 context.session on every subsequent turn.
 session_pre_process() runs on the first turn of every
 conversation, including single-turn attacks, regardless of the target's multi-turn
 setting. 

 Example 

 def session_pre_process(context):
 resp = context.http.post(
 context.vars["base_url"] + "/sessions",
 headers={"Authorization": f"Bearer {context.auth['token']}"},
 )
 return SessionPreProcessResult(session_state={"session_id": resp.json()["id"]}) 

 Previous 

 Return Types 

 Next 

 Multi-Turn Conversations 

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

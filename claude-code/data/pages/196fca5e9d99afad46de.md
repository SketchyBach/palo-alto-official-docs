---
url: https://docs.paloaltonetworks.com/ai-runtime-security/ai-red-teaming/identify-ai-system-risks-with-ai-red-teaming/get-started-with-prisma-airs-ai-red-teaming/targets/custom-target-adapters/adapter-contract/adapter-contract-error-signals
fetched_at: 2026-08-13T14:06:20Z
source: ai-security
---

# Error Signals Clear

Error Signals 

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

 Error Signals 

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

 Error Signals 

 Download PDF 

 Prisma AIRS 

 Error Signals 

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

 Multi-Turn Conversations 

 Next 

 Adapter Contract Examples 

 Error Signals 

 Helper functions for signaling expected target conditions so AI Red Teaming can
 classify and react correctly. 

 Where Can I Use This? What Do I Need? 

 Prisma AIRS (AI Red Teaming) 

 AI Red Teaming License 

 Network Channel client v1.4.0 or
 later 

 Adapter sidecar
 enabled 

 For expected target conditions, use the following helpers so AI Red Teaming can
 classify and react correctly. 

 Helper Use when Platform response 

 raise_rate_limited(message,
 retry_after=N) Target rate-limited the request (for example, HTTP 429) Retries after retry_after seconds 

 raise_auth_error(message) Token rejected or expired (for example, HTTP 401) Invalidates cached auth and retries once 

 raise_content_filtered(message) Target blocked or filtered the response (often an HTTP 200 with
 a filter flag in the body) Records the turn as filtered ; no retry 

 raise_target_error(message) Target failed in a retryable way Retries 

 How network failures are handled depends on the pattern: 

 Pattern A — the platform makes the call, so a timeout or connection
 error is classified automatically. 

 Pattern B ( call_target ) — you make the calls yourself.
 Catch network errors and signal raise_target_error(...) . An
 uncaught exception is reported as an adapter error, not a retryable target
 error. 

 Content-filter detection is the highest-value signal—AI Red Teaming cannot
 generically detect a filtered HTTP 200, but your adapter knows the target's response
 shape: 

 def post_process(context, raw_response):
 if raw_response.status_code == 429:
 raise_rate_limited(retry_after=int(raw_response.headers.get("Retry-After", 30)))
 if raw_response.status_code == 401:
 raise_auth_error("token expired")
 body = raw_response.json_body or {}
 if body.get("error", {}).get("code") == "content_filter":
 raise_content_filtered("blocked by safety filter")
 return PostProcessResult(output=body["reply"]) 

 Previous 

 Multi-Turn Conversations 

 Next 

 Adapter Contract Examples 

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

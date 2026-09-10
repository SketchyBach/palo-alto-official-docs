---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/secrets-security/appsec-secret-373
fetched_at: 2026-09-06T11:16:16Z
source: cortex-platform
---

# PostHog Public API Key detected in code | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 Secrets Security 

 PostHog Public API Key detected in code 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_SECRET_373 

 Category 

 Secrets 

 Severity 

 MEDIUM 

 Framework 

 Git 

 Impact 

 PostHog Public API keys are used for client-side analytics tracking. While less sensitive than private keys, exposed public keys could allow attackers to send false analytics data, pollute your metrics, or potentially identify your PostHog project. Rotate if exposed and implement rate limiting. 

 How to Fix 

 Rotate the PostHog Public API key if necessary. Implement rate limiting and data validation to prevent analytics pollution. 

 Previous PostHog Private API Key detected in code 

 Next Clerk Secret Key detected in code 

 Last updated 1 month ago 

 Was this helpful?

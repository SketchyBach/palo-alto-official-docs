---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/secrets-security/appsec-secret-241
fetched_at: 2026-09-16T09:11:44Z
source: cortex-platform
---

# NX Cloud token detected in code | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 Secrets Security 

 NX Cloud token detected in code 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_SECRET_241 

 Category 

 Sensitive Tokens 

 Severity 

 HIGH 

 Framework 

 Git 

 Impact 

 The NX Cloud token (read-write) grants access to the remote cache. 

 Exposure risks cache poisoning by uploading modified output files, allowing attackers to run arbitrary code on developer machines or CI systems. 

 How to Fix 

 To remediate exposed API & Service Keys: 

 Log in to the service provider's dashboard. 

 Navigate to the API or credentials settings to locate the exposed key. 

 Rotate or regenerate the compromised key immediately. 

 Update your application configuration or environment variables with the new key. 

 Next, remove the secret from your codebase: 

 Locate the exposed key in your codebase. 

 Replace the hardcoded value with a secure variable or reference. 

 Finally, clean your version control history: 

 Permanently remove the sensitive data from your version control history to ensure it cannot be retrieved. 

 Previous New Relic APM license key detected in code 

 Next Plaid access token detected in code 

 Last updated 1 month ago 

 Was this helpful?

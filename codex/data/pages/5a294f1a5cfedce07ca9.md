---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/secrets-security/appsec-secret-337
fetched_at: 2026-09-06T11:16:11Z
source: cortex-platform
---

# New Relic API Service Key detected in code | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 Secrets Security 

 New Relic API Service Key detected in code 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_SECRET_337 

 Category 

 Secrets 

 Severity 

 LOW 

 Framework 

 Git 

 Impact 

 The New Relic API Service Key allows ingestion and querying of observability data. 

 Exposure is a Medium Risk allowing an attacker to analyze application performance traces (which may inadvertently contain PII) or flood the system with false metrics to mask an ongoing attack. 

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

 Previous Artifactory Reference Token With Host detected in code 

 Next Artifactory Basic Auth Credentials detected in code 

 Last updated 1 month ago 

 Was this helpful?

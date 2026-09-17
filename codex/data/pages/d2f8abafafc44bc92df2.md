---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/secrets-security/appsec-secret-58
fetched_at: 2026-09-16T09:11:21Z
source: cortex-platform
---

# PlanetScale Token detected in code | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 Secrets Security 

 PlanetScale Token detected in code 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_SECRET_58 

 Category 

 Sensitive Tokens 

 Severity 

 LOW 

 Framework 

 Git 

 Impact 

 The PlanetScale Token grants programmatic access to database operations. 

 Exposure can lead to data breaches and unauthorized database operations against the managed database platform. 

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

 Previous PagerDuty Authorization Token detected in code 

 Next Postman API Key detected in code 

 Last updated 1 month ago 

 Was this helpful?

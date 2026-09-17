---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/secrets-security/appsec-secret-313
fetched_at: 2026-09-16T09:11:55Z
source: cortex-platform
---

# Sourcegraph Access Token v3 detected in code | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 Secrets Security 

 Sourcegraph Access Token v3 detected in code 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_SECRET_313 

 Category 

 Secrets 

 Severity 

 MEDIUM 

 Framework 

 Git 

 Impact 

 The Sourcegraph Access Token grants unauthenticated programmatic access to your organization's entire codebase, search history, and code insights. 

 Exposure is a Critical Risk that can lead to massive intellectual property theft and aids in reconnaissance to find other hardcoded credentials or vulnerabilities across your entire source code history. 

 How to Fix 

 To remediate exposed Source Control or CI/CD tokens: 

 Log in to the relevant system or provider. 

 Navigate to the settings menu to locate the exposed credential. 

 Revoke or delete the compromised token immediately. 

 Generate a new token if continued access is required. 

 Update any dependent systems or services with the new credential. 

 Next, remove the secret from your codebase: 

 Locate the exposed secret in your codebase. 

 Replace the hardcoded value with a secure variable or reference. 

 Finally, clean your version control history: 

 Permanently remove the sensitive data from your version control history to ensure it cannot be retrieved. 

 Previous Sourcegraph Access Token v1 detected in code 

 Next Dropbox Access Token detected in code 

 Last updated 1 month ago 

 Was this helpful?

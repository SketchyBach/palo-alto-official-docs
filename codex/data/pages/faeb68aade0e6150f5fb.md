---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/secrets-security/appsec-secret-27
fetched_at: 2026-09-06T11:15:08Z
source: cortex-platform
---

# Bitbucket Key detected in code | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 Secrets Security 

 Bitbucket Key detected in code 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_SECRET_27 

 Category 

 API Keys 

 Severity 

 MEDIUM 

 Framework 

 Git 

 Impact 

 A Bitbucket Key (Client ID/Secret) is used to authenticate programmatic access to Bitbucket Cloud APIs and repositories. 

 Exposure of this secret allows an attacker to tamper with version control, steal proprietary code, or perform unauthorized actions on Bitbucket resources. 

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

 Previous Auth0 Key detected in code 

 Next Buildkite Agent Token detected in code 

 Last updated 1 month ago 

 Was this helpful?

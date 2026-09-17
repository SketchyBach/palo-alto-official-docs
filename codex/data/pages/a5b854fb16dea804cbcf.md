---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/secrets-security/appsec-secret-274
fetched_at: 2026-09-16T09:11:48Z
source: cortex-platform
---

# Atlassian Access Token detected in code | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 Secrets Security 

 Atlassian Access Token detected in code 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_SECRET_274 

 Category 

 Secrets 

 Severity 

 LOW 

 Framework 

 Git 

 Impact 

 An Atlassian Access Token is a long-lived token used to authenticate programmatic access to Atlassian services like Jira, Confluence, or Bitbucket. 

 A leaked token grants the attacker the ability to impersonate the token owner and access project data, modify issue statuses, or download source code. 

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

 Previous Base64 Midtrans API Key detected in code 

 Next New Relic Insights Query Key detected in code 

 Last updated 1 month ago 

 Was this helpful?

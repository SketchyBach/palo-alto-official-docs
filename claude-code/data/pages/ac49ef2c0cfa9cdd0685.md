---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/secrets-security/appsec-secret-153
fetched_at: 2026-09-16T09:11:33Z
source: cortex-platform
---

# Azure Active Directory Client Secret detected in code | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 Secrets Security 

 Azure Active Directory Client Secret detected in code 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_SECRET_153 

 Category 

 API Keys 

 Severity 

 HIGH 

 Framework 

 Git 

 Impact 

 The Azure Active Directory (AAD) Client Secret (now Microsoft Entra ID) is used by an application to prove its identity and request access tokens. 

 Exposure grants an attacker the ability to impersonate the application identity, inheriting all of its delegated permissions. This is a Critical Compromise that can lead to unauthorized resource access and potential full account takeover within the organization. 

 How to Fix 

 To remediate exposed Cloud & Infrastructure credentials: 

 Log in to your cloud provider's console. 

 Locate the identity or service account associated with the compromised credentials. 

 Revoke or deactivate the compromised keys immediately. 

 Generate a new set of credentials. 

 Update your environment variables, secrets manager, or pipelines with the new values. 

 Next, remove the secret from your codebase: 

 Locate the exposed secret in your codebase. 

 Replace the hardcoded value with a secure variable or reference. 

 Finally, clean your version control history: 

 Permanently remove the sensitive data from your version control history to ensure it cannot be retrieved. 

 Warning: Revoking infrastructure keys may cause immediate downtime. Ensure you have identified all dependent services before revoking. 

 Previous Coveralls Token detected in code 

 Next DataDog Token detected in code 

 Last updated 1 month ago 

 Was this helpful?

---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/secrets-security/appsec-secret-216
fetched_at: 2026-09-16T09:11:40Z
source: cortex-platform
---

# OVH keys detected in code | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 Secrets Security 

 OVH keys detected in code 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_SECRET_216 

 Category 

 API Keys 

 Severity 

 MEDIUM 

 Framework 

 Git 

 Impact 

 OVH Keys (API key, public key, and confidential secret) are used to authenticate and authorize access to the cloud services and infrastructure. 

 Exposure of these keys grants an attacker unauthorized control over OVH resources, leading to data breaches, unauthorized resource management, and potential service outage. 

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

 Previous Sauce Labs keys detected in code 

 Next PingIdentity keys detected in code 

 Last updated 1 month ago 

 Was this helpful?

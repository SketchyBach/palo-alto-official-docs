---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/secrets-security/appsec-secret-252
fetched_at: 2026-09-16T09:11:45Z
source: cortex-platform
---

# DigitalOcean Spaces connection string detected in code | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 Secrets Security 

 DigitalOcean Spaces connection string detected in code 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_SECRET_252 

 Category 

 Cloud Service Provider Keys 

 Severity 

 MEDIUM 

 Framework 

 Git 

 Impact 

 The DigitalOcean Spaces Connection String contains the full set of credentials (endpoint, Access Key, and Secret Key). 

 Exposure is a Critical Risk as it provides an attacker with all necessary information for immediate, full access (Read/Write/Delete) to object storage buckets, resulting in massive data leakage or corruption. 

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

 Previous DigitalOcean Spaces secret detected in code 

 Next LaunchDarkly SDK key detected in code 

 Last updated 1 month ago 

 Was this helpful?

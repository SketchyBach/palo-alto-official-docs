---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/secrets-security/appsec-secret-7
fetched_at: 2026-09-06T11:15:04Z
source: cortex-platform
---

# IBM Cloud IAM Key detected in code | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 Secrets Security 

 IBM Cloud IAM Key detected in code 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_SECRET_7 

 Category 

 Cloud Service Provider Keys 

 Severity 

 HIGH 

 Framework 

 Git 

 Impact 

 An IBM Cloud IAM Key grants programmatic access to manage resources and configurations within the IBM Cloud environment. 

 Exposure allows an attacker to unauthorizedly manage resources, modify configurations, and potentially access sensitive data across various IBM Cloud services. 

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

 Previous Base64 High Entropy String detected in code 

 Next IBM COS HMAC credential detected in code 

 Last updated 1 month ago 

 Was this helpful?

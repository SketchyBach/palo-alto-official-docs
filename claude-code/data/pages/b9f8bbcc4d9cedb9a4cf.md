---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/secrets-security/appsec-secret-319
fetched_at: 2026-09-16T09:11:54Z
source: cortex-platform
---

# HashiCorp Vault Recovery token detected in code | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 Secrets Security 

 HashiCorp Vault Recovery token detected in code 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_SECRET_319 

 Category 

 Secrets 

 Severity 

 HIGH 

 Framework 

 Git 

 Impact 

 The HashiCorp Vault Recovery Token is the ultimate "break-glass" credential, designed solely for emergency unsealing or regenerating root access. 

 Exposure is an Extremely Critical Risk that bypasses all access policies, allowing an attacker to completely own the secrets infrastructure and decrypt every stored credential. 

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

 Previous HashiCorp Vault Batch Token detected in code 

 Next Groq API Key detected in code 

 Last updated 1 month ago 

 Was this helpful?

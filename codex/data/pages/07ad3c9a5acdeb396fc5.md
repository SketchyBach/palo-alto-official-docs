---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/secrets-security/appsec-secret-340
fetched_at: 2026-09-06T11:16:12Z
source: cortex-platform
---

# Hashicorp Vault AppRole Authentication detected in code | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 Secrets Security 

 Hashicorp Vault AppRole Authentication detected in code 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_SECRET_340 

 Category 

 Secrets 

 Severity 

 LOW 

 Framework 

 Git 

 Impact 

 The HashiCorp Vault AppRole (RoleID/SecretID) is the standard method for machine authentication. 

 Exposure is a Critical Risk enabling an attacker to impersonate a trusted workload and request every secret (DB passwords, API keys) that the specific AppRole is authorized to access. 

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

 Previous Datadog Secret detected in code 

 Next Snowflake Connector Credentials detected in code 

 Last updated 1 month ago 

 Was this helpful?

---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/secrets-security/appsec-secret-266
fetched_at: 2026-09-06T11:15:58Z
source: cortex-platform
---

# Azure Functions App Key Header detected in code | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 Secrets Security 

 Azure Functions App Key Header detected in code 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_SECRET_266 

 Category 

 Secrets 

 Severity 

 HIGH 

 Framework 

 Git 

 Impact 

 The Azure Functions App Key (Header) secures access to a specific Function endpoint when passed via the HTTP Authorization Header. 

 Exposure allows unauthorized requests to be processed, leading to misuse of the function's logic, unauthorized access to linked data or resources, and potential escalation of privileges. 

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

 Previous Figma Personal Access Token detected in code 

 Next Azure Functions App Key Query Parameter detected in code 

 Last updated 1 month ago 

 Was this helpful?

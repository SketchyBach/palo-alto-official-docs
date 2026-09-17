---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/secrets-security/appsec-secret-343
fetched_at: 2026-09-16T09:11:57Z
source: cortex-platform
---

# Azure Logic App Shared Access Signature detected in code | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 Secrets Security 

 Azure Logic App Shared Access Signature detected in code 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_SECRET_343 

 Category 

 Secrets 

 Severity 

 LOW 

 Framework 

 Git 

 Impact 

 The Azure Logic App Shared Access Signature (SAS) is a URI-based token. 

 Exposure is a High Risk allowing anyone with the link to trigger serverless workflows (HTTP triggers) without further authentication, potentially abusing business logic or incurring execution costs. 

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

 Previous Artifactory Reference Token detected in code 

 Next Gitlab Trigger Token detected in code 

 Last updated 1 month ago 

 Was this helpful?

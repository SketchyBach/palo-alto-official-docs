---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/secrets-security/appsec-secret-16
fetched_at: 2026-09-06T11:15:06Z
source: cortex-platform
---

# Square OAuth Secret detected in code | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 Secrets Security 

 Square OAuth Secret detected in code 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_SECRET_16 

 Category 

 Sensitive Tokens 

 Severity 

 LOW 

 Framework 

 Git 

 Impact 

 The Square OAuth Secret is used to obtain permission to manage seller account resources. 

 Exposure is a Critical Risk that allows an attacker to initiate unauthorized transactions, steal sensitive customer payment or management data, and commit financial fraud. 

 How to Fix 

 To remediate exposed API & Service Keys: 

 Log in to the service provider's dashboard. 

 Navigate to the API or credentials settings to locate the exposed key. 

 Rotate or regenerate the compromised key immediately. 

 Update your application configuration or environment variables with the new key. 

 Next, remove the secret from your codebase: 

 Locate the exposed key in your codebase. 

 Replace the hardcoded value with a secure variable or reference. 

 Finally, clean your version control history: 

 Permanently remove the sensitive data from your version control history to ensure it cannot be retrieved. 

 Previous SoftLayer Credential detected in code 

 Next Stripe Access Key detected in code 

 Last updated 1 month ago 

 Was this helpful?

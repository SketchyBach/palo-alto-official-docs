---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/secrets-security/appsec-secret-90
fetched_at: 2026-09-16T09:11:28Z
source: cortex-platform
---

# Shopify Generic App Token detected in code | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 Secrets Security 

 Shopify Generic App Token detected in code 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_SECRET_90 

 Category 

 Sensitive Tokens 

 Severity 

 MEDIUM 

 Framework 

 Git 

 Impact 

 The Shopify App Token grants programmatic access to store data (customer lists, sales, products). 

 Exposure is a Critical Risk allowing an attacker to read or modify sensitive store data, leading to a major data breach or e-commerce fraud. 

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

 Previous Docker Swarm Join Token detected in code 

 Next Mapbox Token detected in code 

 Last updated 1 month ago 

 Was this helpful?

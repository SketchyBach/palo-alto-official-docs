---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/secrets-security/appsec-secret-170
fetched_at: 2026-09-16T09:13:15Z
source: cortex-platform
---

# Codeclimate key detected in code | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 Secrets Security 

 Codeclimate key detected in code 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_SECRET_170 

 Category 

 API Keys 

 Severity 

 MEDIUM 

 Framework 

 Git 

 Impact 

 The Codeclimate Key grants access to sensitive data about the development process and code quality metrics. 

 Exposure allows an attacker to read sensitive security vulnerability data and manipulate quality gates. 

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

 Previous Azure Service Management Certificate detected in code 

 Next Docker Swarm Unlock Key detected in code 

 Last updated 1 month ago 

 Was this helpful?

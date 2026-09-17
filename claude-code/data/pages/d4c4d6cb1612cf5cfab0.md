---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/ci-cd-security/credential-hygiene/appsec-cicd-74
fetched_at: 2026-09-16T09:10:48Z
source: cortex-platform
---

# Variable is not scoped to an environment | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 CI/CD Security 

 Credential Hygiene 

 Variable is not scoped to an environment 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_CICD_74 

 Category 

 Credential Hygiene 

 Severity 

 MEDIUM 

 Impact 

 Repository CI/CD environment variables in projects and groups can be scoped to project environments in order to limit access of pipelines to them. Sensitive variables that are not scoped can be accessed by in secure pipelines (for example, on test environments), without proper controls on accessing these variables. 

 Recommended Solution - Buildtime 

 To limit a variable scope: 

 Browse to the relevant project or group Settings . 

 Under CI/CD , expand Variables . 

 Edit the environment variable and assign it to an environment scope. 

 Previous Jenkins credentials stored with global scope 

 Next Accesses to cloud providers using insecure long-term credentials 

 Last updated 1 month ago 

 Was this helpful?

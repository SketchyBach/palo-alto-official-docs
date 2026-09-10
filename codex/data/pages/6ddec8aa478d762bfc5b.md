---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/ci-cd-security/dependency-chains/appsec-cicd-268
fetched_at: 2026-09-06T11:14:42Z
source: cortex-platform
---

# Deprecated package used in NPM project | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 CI/CD Security 

 Dependency Chains 

 Deprecated package used in NPM project 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_CICD_268 

 Category 

 Dependency Chains 

 Severity 

 HIGH 

 Impact 

 Deprecated packages can pose security risks to the project such as code vulnerabilities that can be discovered overtime and malicious package takeover due to configuration that change over time like the maintainer's email domain expiring. 

 Recommended Solution - Buildtime 

 Remove the deprecated package from the project by executing ‘npm uninstall <PACKAGE_NAME>’. 

 Previous Secret exposed in registry URL within '.npmrc' file 

 Next Potential dependency confusion due to package name or scope available in registry 

 Last updated 1 month ago 

 Was this helpful?

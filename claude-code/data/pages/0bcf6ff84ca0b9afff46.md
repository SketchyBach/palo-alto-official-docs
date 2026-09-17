---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/ci-cd-security/dependency-chains/appsec-cicd-291
fetched_at: 2026-09-16T09:11:03Z
source: cortex-platform
---

# Unencrypted channel used by '.npmrc' file of an Azure repository to download dependencies from proxy | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 CI/CD Security 

 Dependency Chains 

 Unencrypted channel used by '.npmrc' file of an Azure repository to download dependencies from proxy 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_CICD_291 

 Category 

 Dependency Chains 

 Severity 

 MEDIUM 

 Impact 

 Using HTTP instead of HTTPS to download packages through a proxy can make them vulnerable to man-in-the-middle attacks. These attacks could potentially inject malicious code into the packages, which may then be executed on the CI or developer's endpoints. This also poses a risk of exposing internal packages to tampering. 

 Previous Potential dependency confusion in an Azure repository due to package name or scope available in regi 

 Next Unencrypted channel used by '.npmrc' file of an Azure repository to download dependencies from regis 

 Last updated 1 month ago 

 Was this helpful?

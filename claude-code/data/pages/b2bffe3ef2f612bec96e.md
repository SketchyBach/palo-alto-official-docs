---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/ci-cd-security/data-protection/appsec-cicd-19
fetched_at: 2026-09-16T09:10:50Z
source: cortex-platform
---

# Forking of a private repository is allowed | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 CI/CD Security 

 Data Protection 

 Forking of a private repository is allowed 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_CICD_19 

 Category 

 Data Protection 

 Severity 

 MEDIUM 

 Impact 

 Misconfiguration of private repositories may allow sensitive code to be inadvertently/intentionally leaked. A user account might fork the repository to another project, leading to leakage of code. It can also lead to the creation of pull requests from the forked repository to the original repository. This can lead to the execution of malicious code on the CI, even by users with read-only permissions on the original repository. 

 Recommended Solution - Buildtime 

 When not required, disable the forking of private repositories. 

 To restrict forking of a private repository: 

 Browse to project Settings . 

 Under Visibility , select Project Features . 

 Disable the Fork setting under the Permissions section. 

 Previous BitBucket webhooks sent over unencrypted channel 

 Next Forking of BitBucket private repository is allowed 

 Last updated 1 month ago 

 Was this helpful?

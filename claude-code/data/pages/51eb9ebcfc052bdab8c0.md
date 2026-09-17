---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/ci-cd-security/dependency-chains/appsec-cicd-265
fetched_at: 2026-09-16T09:10:57Z
source: cortex-platform
---

# Missing '.npmrc' file in repository | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 CI/CD Security 

 Dependency Chains 

 Missing '.npmrc' file in repository 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_CICD_265 

 Category 

 Dependency Chains 

 Severity 

 MEDIUM 

 Impact 

 The .npmrc file is a configuration file used by npm, the Node Package Manager, to manage settings and options related to package installation and publishing. Failing to store the .npmrc file in the repository can make the project vulnerable during pipelines to both dependency confusion, by allowing an internal package to be fetched from the public registry, as well as insecure use of credentials. 

 Recommended Solution - Buildtime 

 Create a .npmrc file in the repository and configure it according to the best practices detailed in the npm documentation: 

 Authentication related configurations must be scoped to a specific registry by prefixing with a URI fragment: https://docs.npmjs.com/cli/v9/configuring-npm/npmrc#auth-related-configuration 

 Use a variable to represent tokens used in the '.npmrc' file: https://docs.npmjs.com/using-private-packages-in-a-ci-cd-workflow 

 Previous Possible Python typosquatting detected in an Azure repository 

 Next Secret exposed in proxy URL within '.npmrc' file 

 Last updated 1 month ago 

 Was this helpful?

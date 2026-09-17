---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/ci-cd-security/credential-hygiene/appsec-cicd-78
fetched_at: 2026-09-16T09:10:48Z
source: cortex-platform
---

# GitLab CI/CD accesses cloud provider using insecure long-term credentials | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 CI/CD Security 

 Credential Hygiene 

 GitLab CI/CD accesses cloud provider using insecure long-term credentials 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_CICD_78 

 Category 

 Credential Hygiene 

 Severity 

 MEDIUM 

 Impact 

 Long-term credentials intended to be used by GitLab CI/CD to authenticate to a cloud provider account are stored on GitLab as variables. This increases the impact of credential theft, since stolen credentials can be used long after a pipeline run is complete. 

 Previous Accesses to cloud providers using insecure long-term credentials 

 Next Secrets detected in pipeline's console output 

 Last updated 1 month ago 

 Was this helpful?

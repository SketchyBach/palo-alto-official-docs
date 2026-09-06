---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/ci-cd-security/artifact-integrity-validation/appsec-cicd-106
fetched_at: 2026-09-06T11:14:27Z
source: cortex-platform
---

# Missing integrity check for downloaded executable in pipeline | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 CI/CD Security 

 Artifact Integrity Validation 

 Missing integrity check for downloaded executable in pipeline 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_CICD_106 

 Category 

 Artifact Integrity Validation 

 Severity 

 MEDIUM 

 Impact 

 Executables are downloaded and executed during a pipeline run without being validated for integrity, a check which verifies the executable's content. An attacker who compromises the executable can execute code in the pipeline that can exfiltrate credentials or affect the build process in order to ship malicious code or artifacts to production. 

 Recommended Solution - Buildtime 

 Follow the vendor’s instructions on how to validate the signature of the downloaded executable. 

 For Codecov see https://docs.codecov.com/docs/codecov-uploader#integrity-checking-the-uploader. 

 Previous Artifact Integrity Validation 

 Next Missing integrity check for downloaded executable in CircleCI pipeline 

 Last updated 1 month ago 

 Was this helpful?

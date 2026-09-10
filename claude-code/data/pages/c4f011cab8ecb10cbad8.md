---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/compute/appsec-docker-10
fetched_at: 2026-09-06T11:11:33Z
source: cortex-platform
---

# Docker WORKDIR values are not absolute paths misconfiguration detected in code | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 Compute 

 Docker WORKDIR values are not absolute paths misconfiguration detected in code 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_DOCKER_10 

 Category - Subcategory 

 Compute - Startup Script Leaks 

 Provider 

 OTHER 

 Severity 

 LOW 

 Framework 

 DOCKER 

 Impact 

 This rule detects whether all WORKDIR values specified in Dockerfiles are absolute paths. Absolute paths prevent ambiguity, ensure correct directory navigate to the intended directory structure, and contribute to predictable behavior during image build and runtime. Therefore, we recommend always using absolute paths for WORKDIR instruction in Dockerfiles. 

 How to Fix 

 To mitigate this issue, ensure that all WORKDIR instructions in your Dockerfile use absolute paths. 

 Example: [source,go] 

 WORKDIR relative/path 

 WORKDIR /absolute/path 

 Previous Docker APT is used misconfiguration detected in code 

 Next Docker From alias is not unique for multistage builds misconfiguration detected in code 

 Last updated 1 month ago 

 Was this helpful?

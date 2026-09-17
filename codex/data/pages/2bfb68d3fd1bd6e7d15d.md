---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/compute/appsec-docker-4
fetched_at: 2026-09-16T09:09:02Z
source: cortex-platform
---

# Copy is not used instead of Add in Dockerfiles misconfiguration detected in code | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 Compute 

 Copy is not used instead of Add in Dockerfiles misconfiguration detected in code 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_DOCKER_4 

 Category - Subcategory 

 Compute - Startup Script Leaks 

 Provider 

 OTHER 

 Severity 

 LOW 

 Framework 

 DOCKER 

 Impact 

 The Copy instruction simply copies files from the local host machine to the container file system. The Add instruction could potentially retrieve files from remote URLs and perform operations such as unpacking them. The Add instruction, therefore, introduces security risks. For example, malicious files may be directly accessed from URLs without scanning, or there may be vulnerabilities associated with decompressing them We recommend you use the Copy instruction instead of the Add instruction in the Dockerfile. 

 How to Fix 

 [source,go] 

 ADD config.txt /app/ 

 Previous A user for the container has not been created misconfiguration detected in code 

 Next Update instructions are used alone in a Dockerfile misconfiguration detected in code 

 Last updated 1 month ago 

 Was this helpful?

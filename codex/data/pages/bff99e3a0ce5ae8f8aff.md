---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/ci-cd-security/data-protection/appsec-cicd-92
fetched_at: 2026-09-06T11:14:34Z
source: cortex-platform
---

# Certificate not verified by pipeline command | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 CI/CD Security 

 Data Protection 

 Certificate not verified by pipeline command 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_CICD_92 

 Category 

 Data Protection 

 Severity 

 MEDIUM 

 Impact 

 Not verifying certificates through pipeline commands allows attackers to plant their own certificate and impersonate a server in order to perform a man-in-the-middle attack to intercept, tamper with and/or steal information, to possibly run code in the build system and to reach the production environment. 

 Recommended Solution - Buildtime 

 Remove flags from the commands found in the pipeline that disable the certificate check: 

 For wget command remove: --no-check-certificate 

 For curl command remove: --insecure or -k flags 

 Consider removing the command entirely from the pipeline if the server certificate cannot be authenticated. 

 Previous Private repository made public 

 Next Pipeline commands transmit data over an unencrypted channel 

 Last updated 1 month ago 

 Was this helpful?

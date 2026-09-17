---
url: https://cortex-docs.paloaltonetworks.com/application-security/application-security/onboard-data-sources/ingest-third-party-data-sources/generic-3rd-party-appsec-collector/references/technical-requirements-and-sarif-specifications
fetched_at: 2026-09-16T08:49:04Z
source: cortex-platform
---

# Reference A: System requirements | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center shield-alt shield-alt

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex Cloud 

 Application Security 

 Application Security 

 Onboard data sources 

 Ingest third-party data sources 

 Generic 3rd Party AppSec Collector 

 References 

 Reference A: System requirements 

 Review system requirements before uploading SARIF findings. 

 Before utilizing a Collector, verify the following system requirements. 

 Requirement 

 Description 

 Input Format 

 Valid SARIF v2.1.0 JSON strictly adhering to the standard. The collector will not ingest files with invalid formats or schema violations. 

 File Size 

 Maximum 10 MB per upload. Larger files must be split. 

 Network 

 Outbound HTTPS (port 443) access to the public API. TLS 1.2+ required. 

 Previous References 

 Next Reference B: SARIF format and mapping 

 Last updated 1 month ago 

 Was this helpful?

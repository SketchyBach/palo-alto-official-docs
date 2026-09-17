---
url: https://cortex-docs.paloaltonetworks.com/cortex-cloud-runtime-security/endpoint-security/endpoint-dlp/cortex-data-loss-prevention-dlp-module-overview/true-file-type-detection
fetched_at: 2026-09-16T08:44:35Z
source: cortex-platform
---

# True-file type detection | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex Cloud 

 Cortex CLOUD Runtime Security 

 Endpoint security 

 Endpoint DLP 

 Cortex Data Loss Prevention (DLP) module overview 

 Cortex Cloud Runtime 

 True-file type detection 

 When Cortex Data Loss Prevention (DLP) scans a file, true file-type detection identifies the file based on its actual internal format rather than relying on its file extension. 

 This ensures consistent policy enforcement and prevents users from intentionally bypassing DLP rules by masking files. 

 Accurate Enforcement : DLP recognizes the sensitive data inside the file and applies the matching data-in-motion rule, regardless of the file's current extension. 

 Evasion Prevention : If a user renames a restricted document (for example, changing report.pdf to report.log ), DLP still identifies the true file type as a PDF, scans the embedded sensitive data, and enforces the appropriate rule. 

 Supported file scans on Windows and macOS 

 Previous Archive file classification 

 Next Personas workflow for DLP 

 Last updated 20 days ago 

 Was this helpful?

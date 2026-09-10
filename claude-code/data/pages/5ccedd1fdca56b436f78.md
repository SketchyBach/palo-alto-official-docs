---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/storage/appsec-azure-52
fetched_at: 2026-09-06T11:14:10Z
source: cortex-platform
---

# MSSQL is not using the latest version of TLS encryption misconfiguration detected in code | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 Storage 

 MSSQL is not using the latest version of TLS encryption misconfiguration detected in code 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_AZURE_52 

 Category - Subcategory 

 Public Exposure - Encryption And Protocols 

 Provider 

 AZURE 

 Severity 

 MEDIUM 

 Framework 

 ARM, Bicep, Terraform, Terraform Plan 

 Mapped CSPM/KSPM Rule 

 72f2c9e3-cbbd-4643-8978-e8319e5087b1 

 Impact 

 The Transport Layer Security (TLS) protocol secures transmission of data between servers and web browsers over the internet using standard encryption technology. To follow security best practices and the latest PCI compliance standards, enable the latest version of TLS protocol (i.e. TLS 1.2) for all your MSSQL servers. 

 How to Fix 

 Resource: azurerm_mssql_server 

 Arguments: minimum_tls_version [source,go] 

 resource "azurerm_mssql_server" "examplea" { ... 

 minimum_tls_version = "1.2" ... } 

 Previous Azure Storage Account using insecure TLS version misconfiguration detected in code 

 Next Azure Automation account variables are not encrypted misconfiguration detected in code 

 Last updated 1 month ago 

 Was this helpful?

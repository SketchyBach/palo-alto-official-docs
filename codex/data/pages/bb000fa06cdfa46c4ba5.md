---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/public-exposure/appsec-azure-113
fetched_at: 2026-09-06T11:13:23Z
source: cortex-platform
---

# SQL Server is enabled for public network access misconfiguration detected in code | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 Public Exposure 

 SQL Server is enabled for public network access misconfiguration detected in code 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_AZURE_113 

 Category - Subcategory 

 Public Exposure - Database Endpoints 

 Provider 

 AZURE 

 Severity 

 LOW 

 Framework 

 ARM, Bicep, Terraform, Terraform Plan 

 Impact 

 By ensuring that your SQL server is not public, you can help protect your data from unauthorized access or tampering. Public SQL servers are accessible over the internet, which can make them vulnerable to external threats such as hackers or malware. By making it private, you can help ensure that only authorized users can access the data. 

 How to Fix 

 Resource: azurerm_mssql_server 

 Arguments: public_network_access_enabled [source,go] 

 resource "azurerm_mssql_server" "example" { ... 

 public_network_access_enabled = false } 

 Previous Azure IoT Hub enables public network access misconfiguration detected in code 

 Next Azure Virtual machine NIC has IP forwarding enabled misconfiguration detected in code 

 Last updated 1 month ago 

 Was this helpful?

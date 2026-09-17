---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/public-exposure/appsec-azure-108
fetched_at: 2026-09-16T09:09:47Z
source: cortex-platform
---

# Azure IoT Hub enables public network access misconfiguration detected in code | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 Public Exposure 

 Azure IoT Hub enables public network access misconfiguration detected in code 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_AZURE_108 

 Category - Subcategory 

 Public Exposure - APIs 

 Provider 

 AZURE 

 Severity 

 MEDIUM 

 Framework 

 Terraform, Terraform Plan 

 Impact 

 By ensuring that your IoT Hub is not public, you can help protect your data from unauthorized access or tampering. Public IoT Hubs are accessible over the internet, which can make them vulnerable to external threats such as hackers or malware. By making it private, you can help ensure that only authorized users can access the data. 

 How to Fix 

 Resource: azurerm_iothub 

 Arguments: public_network_access_enabled [source,go] 

 resource "azurerm_iothub" "example" { ... 

 public_network_access_enabled = false route { name = "export" source = "DeviceMessages" condition = "true" endpoint_names = ["export"] enabled = true } ... } 

 Previous Azure Event Grid domain public network access is enabled misconfiguration detected in code 

 Next SQL Server is enabled for public network access misconfiguration detected in code 

 Last updated 1 month ago 

 Was this helpful?

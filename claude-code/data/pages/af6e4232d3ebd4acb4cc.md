---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/public-exposure/appsec-azure-193
fetched_at: 2026-09-06T11:13:26Z
source: cortex-platform
---

# Azure Event Grid Topic Public Network Access misconfiguration detected in code | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 Public Exposure 

 Azure Event Grid Topic Public Network Access misconfiguration detected in code 

 Azure Event Grid Topic Public Network Access misconfiguration detected in code 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_AZURE_193 

 Category - Subcategory 

 Public Exposure - APIs 

 Provider 

 AZURE 

 Severity 

 MEDIUM 

 Framework 

 ARM, Bicep, Terraform, Terraform Plan 

 Impact 

 Ensure public network access is disabled for Azure Event Grid Topic 

 How to Fix 

 Resource: 

 azurerm_eventgrid_topic 

 Arguments: 

 public_network_access_enabled [source,go] 

 resource "azurerm_eventgrid_topic" "example" { name = "example-topic" location = azurerm_resource_group.example.location resource_group_name = azurerm_resource_group.example.name 

 ... other configurations ... 

 public_network_access_enabled = false 

 ... other configurations ... 

 } 

 Previous Azure storage account has a blob container with public access misconfiguration detected in code 

 Next Azure SignalR Service not Using Paid SKU for its SLA misconfiguration detected in code 

 Last updated 1 month ago 

 Was this helpful?

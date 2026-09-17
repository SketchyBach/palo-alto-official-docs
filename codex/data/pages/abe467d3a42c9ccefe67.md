---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/networking/appsec-azure-109
fetched_at: 2026-09-16T09:09:29Z
source: cortex-platform
---

# Key vault does not allow firewall rules settings misconfiguration detected in code | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 Networking 

 Key vault does not allow firewall rules settings misconfiguration detected in code 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_AZURE_109 

 Category - Subcategory 

 Public Exposure - Encryption And Protocols 

 Provider 

 AZURE 

 Severity 

 MEDIUM 

 Framework 

 ARM, Bicep, Terraform, Terraform Plan 

 Impact 

 Key vault's firewall prevents unauthorized traffic from reaching your key vault and provides an additional layer of protection for your secrets. Enable the firewall to make sure that only traffic from allowed networks can access your key vault. By defining "bypass=AzureServices" and "default_action= "deny" - only matched ip_rules and/or virtual_network_subnet_ids will be passed 

 How to Fix 

 Resource: azurerm_key_vault 

 Arguments: network_acls.default_action [source,go] 

 resource "azurerm_key_vault" "example" { ... 

 network_acls { 

 default_action = "Deny" 

 bypass = "AzureServices" } } 

 Previous API management services do not use virtual networks misconfiguration detected in code 

 Next AKS is not enabled for private clusters misconfiguration detected in code 

 Last updated 1 month ago 

 Was this helpful?

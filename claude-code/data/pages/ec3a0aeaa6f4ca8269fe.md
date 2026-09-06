---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/public-exposure/appsec-azure-160
fetched_at: 2026-09-06T11:13:25Z
source: cortex-platform
---

# Azure HTTP (port 80) access from the internet is not restricted misconfiguration detected in code | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 Public Exposure 

 Azure HTTP (port 80) access from the internet is not restricted misconfiguration detected in code 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_AZURE_160 

 Category - Subcategory 

 Public Exposure - Sensitive Ports 

 Provider 

 AZURE 

 Severity 

 LOW 

 Framework 

 ARM, Bicep, Terraform, Terraform Plan 

 Impact 

 Restricting access to Azure HTTP (port 80) from the internet can help improve the security of your resources. Port 80 is used for HTTP traffic, and allowing access to it from the internet can expose your resources to potential security threats, such as malware, data breaches, and unauthorized access. 

 How to Fix 

 Resource: azurerm_network_security_rule 

 Arguments: destination_port_range [source,go] 

 resource "azurerm_network_security_rule" "https" { name = "example" access = "Allow" direction = "Inbound" network_security_group_name = "azurerm_network_security_group.example.name" priority = 100 protocol = "Tcp" resource_group_name = "azurerm_resource_group.example.name" 

 destination_port_range = 443 source_address_prefix = "Internet" } 

 Previous Azure App service slot does not have debugging disabled misconfiguration detected in code 

 Next Azure Spring Cloud API Portal is not enabled for HTTPS misconfiguration detected in code 

 Last updated 1 month ago 

 Was this helpful?

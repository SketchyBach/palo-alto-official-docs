---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/public-exposure/appsec-azure-162
fetched_at: 2026-09-06T11:13:25Z
source: cortex-platform
---

# Azure Spring Cloud API Portal Public Access Is Enabled misconfiguration detected in code | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 Public Exposure 

 Azure Spring Cloud API Portal Public Access Is Enabled misconfiguration detected in code 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_AZURE_162 

 Category - Subcategory 

 Public Exposure - APIs 

 Provider 

 AZURE 

 Severity 

 LOW 

 Framework 

 Terraform 

 Impact 

 Disabling the public network access property improves security by ensuring your Spring Cloud API Portals can only be accessed from a private endpoint. This configuration strictly disables access from any public address space outside of Azure IP range and denies all logins that match IP or virtual network-based firewall rules. 

 How to Fix 

 Resources: azurerm_spring_cloud_api_portal 

 Attribute: public_network_access_enabled (default is "false") [source,go] 

 resource "azurerm_spring_cloud_api_portal" "pass" { name = "default" spring_cloud_service_id = azurerm_spring_cloud_service.example.id gateway_ids = [azurerm_spring_cloud_gateway.example.id] https_only_enabled = false public_network_access_enabled = false instance_count = 1 sso { client_id = "test" client_secret = "secret" issuer_uri = "https://www.example.com/issueToken" scope = ["read"] } } 

 Previous Azure Spring Cloud API Portal is not enabled for HTTPS misconfiguration detected in code 

 Next API Management Without Minimum TLS 1.2 misconfiguration detected in code 

 Last updated 1 month ago 

 Was this helpful?

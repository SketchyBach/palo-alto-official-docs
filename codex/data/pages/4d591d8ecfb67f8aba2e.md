---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/public-exposure/appsec-azure-145
fetched_at: 2026-09-06T11:13:24Z
source: cortex-platform
---

# Azure Function App doesn't use latest TLS version misconfiguration detected in code | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 Public Exposure 

 Azure Function App doesn't use latest TLS version misconfiguration detected in code 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_AZURE_145 

 Category - Subcategory 

 Public Exposure - Encryption And Protocols 

 Provider 

 AZURE 

 Severity 

 LOW 

 Framework 

 ARM, Bicep, Terraform, Terraform Plan 

 Mapped CSPM/KSPM Rule 

 c82a5f89-cd01-4bcf-8fa3-99396a4c848d 

 Impact 

 The Transport Layer Security (TLS) protocol secures transmission of data between servers and web browsers, over the Internet, using standard encryption technology. To follow security best practices and the latest PCI compliance standards, enable the latest version of TLS protocol (i.e. TLS 1.2) for all your Azure Function apps. 

 How to Fix 

 Resource: azurerm_function_app 

 Arguments: site_config.min_tls_version [source,go] 

 resource "azurerm_function_app" "pass2" { name = "test-azure-functions" location = azurerm_resource_group.example.location resource_group_name = azurerm_resource_group.example.name app_service_plan_id = azurerm_app_service_plan.example.id storage_account_name = azurerm_storage_account.example.name storage_account_access_key = azurerm_storage_account.example.primary_access_key https_only = false 

 site_config { dotnet_framework_version = "v4.0" scm_type = "LocalGit" min_tls_version = 1.2 ftps_state = "AllAllowed" http2_enabled = false cors { allowed_origins = ["*"] } } } 

 Previous Azure AKS cluster nodes have public IP addresses misconfiguration detected in code 

 Next Azure Redis Cache does not use the latest version of TLS encryption misconfiguration detected in cod 

 Last updated 1 month ago 

 Was this helpful?

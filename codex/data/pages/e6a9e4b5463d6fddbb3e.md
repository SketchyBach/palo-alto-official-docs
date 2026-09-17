---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/logging/appsec-azure-159
fetched_at: 2026-09-16T09:09:16Z
source: cortex-platform
---

# Azure Built-in logging for Azure function app is disabled misconfiguration detected in code | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 Logging 

 Azure Built-in logging for Azure function app is disabled misconfiguration detected in code 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_AZURE_159 

 Category - Subcategory 

 Logging - Disabled or missing 

 Provider 

 AZURE 

 Severity 

 LOW 

 Framework 

 Terraform 

 Impact 

 It is recommended to have a proper logging process for Azure function app in order to track configuration changes conducted manually and programmatically and trace back unapproved changes. 

 // Runtime - Buildtime 

 How to Fix 

 Resource: azurerm_function_app_slot 

 Arguments: enable_builtin_logging [source,go] 

 resource "azurerm_function_app_slot" "pass2" { name = "test-azure-functions-slot" location = azurerm_resource_group.example.location resource_group_name = azurerm_resource_group.example.name app_service_plan_id = azurerm_app_service_plan.example.id function_app_name = azurerm_function_app.example.name storage_account_name = azurerm_storage_account.example.name storage_account_access_key = azurerm_storage_account.example.primary_access_key enable_builtin_logging = true site_config { http2_enabled = false } auth_settings { enabled = false } } 

 Previous Azure SQL Server does not have default auditing policy configured misconfiguration detected in code 

 Next Ledger feature is disabled on the database misconfiguration detected in code 

 Last updated 1 month ago 

 Was this helpful?

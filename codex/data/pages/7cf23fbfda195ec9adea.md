---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/public-exposure/appsec-azure-155
fetched_at: 2026-09-16T09:09:48Z
source: cortex-platform
---

# Azure App service slot does not have debugging disabled misconfiguration detected in code | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 Public Exposure 

 Azure App service slot does not have debugging disabled misconfiguration detected in code 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_AZURE_155 

 Category - Subcategory 

 Public Exposure - APIs 

 Provider 

 AZURE 

 Severity 

 LOW 

 Framework 

 ARM, Bicep, Terraform, Terraform Plan 

 Impact 

 Disabling debugging for your Azure App Service slot can help improve the security of your app. Debugging allows you to troubleshoot issues with your app by providing access to detailed information about how the app is functioning. However, it can also make it easier for attackers to gain access to sensitive information about your app, such as its code and configuration. 

 How to Fix 

 Resource: azurerm_app_service_slot 

 Arguments: remote_debugging_enabled (default is false) [source,go] 

 resource "azurerm_app_service_slot" "pass2" { name = "ted" app_service_name = azurerm_app_service.example.name location = azurerm_resource_group.example.location resource_group_name = azurerm_resource_group.example.name app_service_plan_id = azurerm_app_service_plan.example.id 

 https_only = false #thedefault 

 site_config { dotnet_framework_version = "v4.0" min_tls_version = "1.2" #the default is 1.2 remote_debugging_enabled = false #default is false } 

 app_settings = { "SOME_KEY" = "some-value" } 

 connection_string { name = "Database" type = "SQLServer" value = "Server=some-server.mydomain.com;Integrated Security=SSPI" } } 

 Previous Azure App's service slot does not use the latest version of TLS encryption misconfiguration detected 

 Next Azure HTTP (port 80) access from the internet is not restricted misconfiguration detected in code 

 Last updated 1 month ago 

 Was this helpful?

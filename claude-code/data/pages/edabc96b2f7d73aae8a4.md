---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/networking/appsec-azure-62
fetched_at: 2026-09-16T09:09:29Z
source: cortex-platform
---

# CORS allows resources to access function apps misconfiguration detected in code | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 Networking 

 CORS allows resources to access function apps misconfiguration detected in code 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_AZURE_62 

 Category - Subcategory 

 Public Exposure - APIs 

 Provider 

 AZURE 

 Severity 

 LOW 

 Framework 

 ARM, Bicep, Terraform, Terraform Plan 

 Impact 

 Cross-Origin Resource Sharing (CORS) should not allow all domains to access your Function app. Allow only required domains to interact with your Function app. 

 How to Fix 

 Resource: azurerm_function_app 

 Arguments: site_config.cors [source,go] 

 resource "azurerm_function_app" "example" { ... site_config { 

 cors { 

 allowed_origins = ["192.0.0.1"] } } } 

 Previous Azure RDP Internet access is not restricted misconfiguration detected in code 

 Next Azure Function App doesn't use HTTP 2.0 misconfiguration detected in code 

 Last updated 1 month ago 

 Was this helpful?

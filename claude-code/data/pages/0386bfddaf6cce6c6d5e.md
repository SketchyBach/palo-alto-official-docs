---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/iam/appsec-azure-71
fetched_at: 2026-09-16T09:09:10Z
source: cortex-platform
---

# Azure App Service Web app doesn't have a Managed Service Identity misconfiguration detected in code | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 IAM 

 Azure App Service Web app doesn't have a Managed Service Identity misconfiguration detected in code 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_AZURE_71 

 Category - Subcategory 

 IAM - Authentication Policies 

 Provider 

 AZURE 

 Severity 

 LOW 

 Framework 

 ARM, Bicep, Terraform, Terraform Plan 

 Mapped CSPM/KSPM Rule 

 b6caba6b-cdb1-4db5-8045-9d0354a602de 

 Impact 

 Managed service identity in App Service makes the app more secure by eliminating secrets from the app, such as credentials in the connection strings. When registering with Azure Active Directory in the app service, the app will connect to other Azure services securely without the need of username and passwords. 

 How to Fix 

 Resource: azurerm_app_service 

 Arguments: identity.type [source,go] 

 resource "azurerm_app_service" "example" { ... 

 identity { 

 type = "SystemAssigned" } } 

 Previous Azure Function App authentication is off misconfiguration detected in code 

 Next AKS does not use Azure policies add-on misconfiguration detected in code 

 Last updated 1 month ago 

 Was this helpful?

---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/public-exposure/appsec-azure-70
fetched_at: 2026-09-16T09:09:46Z
source: cortex-platform
---

# Azure Function App doesn't redirect HTTP to HTTPS misconfiguration detected in code | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 Public Exposure 

 Azure Function App doesn't redirect HTTP to HTTPS misconfiguration detected in code 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_AZURE_70 

 Category - Subcategory 

 Public Exposure - APIs 

 Provider 

 AZURE 

 Severity 

 MEDIUM 

 Framework 

 ARM, Bicep, Terraform, Terraform Plan 

 Mapped CSPM/KSPM Rule 

 82d945cb-49c0-4163-89ef-7ac3c194d4cb 

 Impact 

 By ensuring that function apps are only accessible over HTTPS, you can help to protect the data transmitted to and from your app from being accessed or modified by unauthorized parties. This can help to improve the security of your app and protect it from potential threats such as man-in-the-middle attacks or data breaches. 

 How to Fix 

 Resource: azurerm_app_service 

 Arguments: https_only [source,go] 

 resource "azurerm_app_service" "example" { ... 

 https_only = true } 

 Previous PostgreSQL server does not disable public network access misconfiguration detected in code 

 Next Azure Network Security Group having Inbound rule overly permissive to all traffic on UDP protocol mi 

 Last updated 1 month ago 

 Was this helpful?

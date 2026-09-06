---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/public-exposure/appsec-azure-34
fetched_at: 2026-09-06T11:13:20Z
source: cortex-platform
---

# Azure storage account has a blob container that is publicly accessible misconfiguration detected in | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 Public Exposure 

 Azure storage account has a blob container that is publicly accessible misconfiguration detected in 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_AZURE_34 

 Category - Subcategory 

 Public Exposure - Storage Buckets 

 Provider 

 AZURE 

 Severity 

 HIGH 

 Framework 

 ARM, Bicep, Terraform, Terraform Plan 

 Impact 

 Ensure that 'Public access level' is set to Private for blob containers 

 How to Fix 

 Resource: azurerm_storage_container 

 Arguments: container_access_type [source,go] 

 resource "azurerm_storage_container" "example" { ... 

 container_access_type = "private" } 

 Previous Azure PostgreSQL database server with SSL connection disabled misconfiguration detected in code 

 Next Azure Storage Account default network access is set to 'Allow' misconfiguration detected in code 

 Last updated 1 month ago 

 Was this helpful?

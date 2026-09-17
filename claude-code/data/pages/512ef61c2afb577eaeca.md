---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/storage/appsec-azure-76
fetched_at: 2026-09-16T09:10:30Z
source: cortex-platform
---

# Azure Batch account does not use key vault to encrypt data misconfiguration detected in code | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 Storage 

 Azure Batch account does not use key vault to encrypt data misconfiguration detected in code 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_AZURE_76 

 Category - Subcategory 

 Storage - Encryption 

 Provider 

 AZURE 

 Severity 

 LOW 

 Framework 

 ARM, Bicep, Terraform, Terraform Plan 

 Impact 

 Use customer-managed keys to manage the encryption at rest of your Batch account data. By default, customer data is encrypted with service-managed keys, but customer-managed keys are commonly required to meet regulatory compliance standards. Customer-managed keys enable the data to be encrypted with an Azure Key Vault key created and owned by you. You have full control and responsibility for the key lifecycle, including rotation and management. 

 How to Fix 

 Resource: azurerm_batch_account 

 Arguments: key_vault_reference [source,go] 

 resource "azurerm_batch_account" "example" { ... 

 key_vault_reference { id = "test" url = "https://test.com" } } 

 Previous Azure Data Explorer cluster double encryption is disabled misconfiguration detected in code 

 Next App services do not use Azure files misconfiguration detected in code 

 Last updated 1 month ago 

 Was this helpful?

---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/storage/appsec-azure-110
fetched_at: 2026-09-16T09:10:37Z
source: cortex-platform
---

# Azure Key Vault Purge protection is not enabled misconfiguration detected in code | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 Storage 

 Azure Key Vault Purge protection is not enabled misconfiguration detected in code 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_AZURE_110 

 Category - Subcategory 

 Storage - Backups 

 Provider 

 AZURE 

 Severity 

 LOW 

 Framework 

 ARM, Bicep, Terraform, Terraform Plan 

 Mapped CSPM/KSPM Rule 

 df4f009d-f049-4e04-bbdf-06d98b1b040f 

 Impact 

 Purge protection is an optional Key Vault behavior and is not enabled by default. Purge protection can only be enabled once soft-delete is enabled. It can be turned on via CLI or PowerShell. When purge protection is on, a vault or an object in the deleted state cannot be purged until the retention period has passed. Soft-deleted vaults and objects can still be recovered, ensuring that the retention policy will be followed. The default retention period is 90 days, but it is possible to set the retention policy interval to a value from 7 to 90 days through the Azure portal. Once the retention policy interval is set and saved it cannot be changed for that vault. 

 How to Fix 

 Resource: azurerm_key_vault 

 Arguments: purge_protection_enabled - (Optional) Is Purge Protection enabled for this Key Vault? 

 Defaults to false. [source,go] 

 resource "azurerm_key_vault" "example" { ... 

 purge_protection_enabled = true } 

 Previous Unencrypted Data Lake Store accounts misconfiguration detected in code 

 Next Key vault does not enable soft-delete misconfiguration detected in code 

 Last updated 1 month ago 

 Was this helpful?

---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/storage/appsec-azure-93
fetched_at: 2026-09-06T11:14:12Z
source: cortex-platform
---

# Managed disks do not use a specific set of disk encryption sets for customer-managed key encryption | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 Storage 

 Managed disks do not use a specific set of disk encryption sets for customer-managed key encryption 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_AZURE_93 

 Category - Subcategory 

 Storage - Encryption 

 Provider 

 AZURE 

 Severity 

 LOW 

 Framework 

 ARM, Bicep, Terraform, Terraform Plan 

 Impact 

 Requiring a specific set of disk encryption sets to be used with managed disks give you control over the keys used for encryption at rest. You are able to select the allowed encrypted sets and all others are rejected when attached to a disk. 

 How to Fix 

 Resource: azurerm_managed_disk 

 Arguments: disk_encryption_set_id [source,go] 

 resource "azurerm_managed_disk" "source" { name = "acctestmd1" location = "West US 2" resource_group_name = azurerm_resource_group.example.name storage_account_type = "Standard_LRS" create_option = "Empty" disk_size_gb = "1" 

 disk_encryption_set_id = "koko" tags = { environment = "staging" } } 

 Previous Not only SSL are enabled for cache for Redis misconfiguration detected in code 

 Next My SQL server disables geo-redundant backups misconfiguration detected in code 

 Last updated 1 month ago 

 Was this helpful?

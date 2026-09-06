---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/storage/appsec-azure-105
fetched_at: 2026-09-06T11:14:12Z
source: cortex-platform
---

# Unencrypted Data Lake Store accounts misconfiguration detected in code | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 Storage 

 Unencrypted Data Lake Store accounts misconfiguration detected in code 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_AZURE_105 

 Category - Subcategory 

 Storage - Encryption 

 Provider 

 AZURE 

 Severity 

 MEDIUM 

 Framework 

 ARM, Bicep, Terraform, Terraform Plan 

 Impact 

 Azure Data Lake Storage Gen2 is a set of capabilities dedicated to big data analytics, built on Azure Blob storage. Data Lake Storage Gen2 converges the capabilities of Azure Data Lake Storage Gen1 with Azure Blob storage. Data Lake Storage Gen1 supports encryption of data both at rest and in transit. For data at rest, Data Lake Storage Gen1 supports "on by default," transparent encryption. 

 How to Fix 

 Resource: xyz 

 Arguments: encryption_state - (Optional) Is Encryption enabled on this Data Lake Store Account? 

 Possible values are Enabled or Disabled. Defaults to Enabled. encryption_type - (Optional) The Encryption Type used for this Data Lake Store Account. Currently can be set to ServiceManaged when encryption_state is Enabled - and must be a blank string when it's Disabled. [source,go] 

 { "resource "azurerm_data_lake_store" "example" { ... encryption_state = "Enabled" encryption_type = "ServiceManaged" } 

 ", } 

 Previous PostgreSQL server enables geo-redundant backups misconfiguration detected in code 

 Next Azure Key Vault Purge protection is not enabled misconfiguration detected in code 

 Last updated 1 month ago 

 Was this helpful?

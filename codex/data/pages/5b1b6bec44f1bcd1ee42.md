---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/monitoring/appsec-azure-custom-1
fetched_at: 2026-09-16T09:09:22Z
source: cortex-platform
---

# Azure resources that support tags do not have tags misconfiguration detected in code | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 Monitoring 

 Azure resources that support tags do not have tags misconfiguration detected in code 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_AZURE_CUSTOM_1 

 Category - Subcategory 

 Monitoring - Tags and metadata 

 Provider 

 AZURE 

 Severity 

 LOW 

 Framework 

 Terraform, Terraform Plan 

 Impact 

 Many different types of Azure resources support tags. Tags allow you to add metadata to a resource to help identify ownership, perform cost / billing analysis, and to enrich a resource with other valuable information, such as descriptions and environment names. While there are many ways that tags can be used, we recommend you follow a tagging practice. View Microsoft's recommended tagging best practices https://docs.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/naming-and-tagging[here]. 

 How to Fix 

 The example below shows how to tag a security group in Terraform. The syntax is generally the same for any taggable resource type. [source,go] 

 resource "azurerm_resource_group" "example" { name = "example-resources" location = "West Europe" } 

 resource "azurerm_managed_disk" "example" { name = "acctestmd" location = "West US 2" resource_group_name = azurerm_resource_group.example.name storage_account_type = "Standard_LRS" create_option = "Empty" disk_size_gb = "1" 

 tags = { 

 environment = "staging" } 

 } ", 

 } 

 Previous Azure Microsoft Defender for Cloud set to Off for Resource Manager misconfiguration detected in code 

 Next GCP Kubernetes Engine Clusters have Cloud Monitoring disabled misconfiguration detected in code 

 Last updated 1 month ago 

 Was this helpful?

---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/compute/appsec-azure-45
fetched_at: 2026-09-16T09:09:01Z
source: cortex-platform
---

# Secrets are exposed in Azure VM customData misconfiguration detected in code | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 Compute 

 Secrets are exposed in Azure VM customData misconfiguration detected in code 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_AZURE_45 

 Category - Subcategory 

 Public Exposure - Encryption And Protocols 

 Provider 

 AZURE 

 Severity 

 HIGH 

 Framework 

 ARM, Bicep, Terraform, Terraform Plan 

 Impact 

 Ensure that no sensitive credentials are exposed in VM custom_data 

 How to Fix 

 Remove the following attribute from the Terraform resource. [source,go] 

 resource "azurerm_virtual_machine" "main" { name = "${var.prefix}-vm" ... os_profile { ... 

 custom_data = "MY_SECRET_VALUE" } ... } 

 Previous AWS SQS queue access policy is overly permissive misconfiguration detected in code 

 Next Azure Linux scale set does not use an SSH key misconfiguration detected in code 

 Last updated 1 month ago 

 Was this helpful?

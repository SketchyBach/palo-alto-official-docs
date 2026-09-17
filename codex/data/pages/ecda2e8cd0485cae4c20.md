---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/logging/appsec-azure-224
fetched_at: 2026-09-16T09:09:16Z
source: cortex-platform
---

# Ledger feature is disabled on the database misconfiguration detected in code | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 Logging 

 Ledger feature is disabled on the database misconfiguration detected in code 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_AZURE_224 

 Category - Subcategory 

 Logging - Disabled or missing 

 Provider 

 AZURE 

 Severity 

 MEDIUM 

 Framework 

 Terraform, Terraform Plan 

 Impact 

 This rule refers to the enabling of the Ledger feature in Azure databases. The Ledger feature is a way of recording all changes to the data within a database, maintaining a history of all data modifications. This is important for auditing, security, and data recovery purposes. If the Ledger feature is not enabled, it might lead to difficulties in tracking changes, detecting malicious activity, or recovering lost data. Therefore, it's bad practice not to activate this feature due to the potential security risks and data management issues. 

 How to Fix 

 Resource: azurerm_mssql_database 

 Arguments: ledger_enabled 

 To fix this issue, you have to modify the azurerm_mssql_database resource in the Terraform code to include the ledger_enabled argument and set it to true . [source,go] 

 resource "azurerm_mssql_database" "pass" { name = "example-database" ... 

 ledger_enabled = true } 

 Previous Azure Built-in logging for Azure function app is disabled misconfiguration detected in code 

 Next GCP Kubernetes Engine Clusters have Cloud Logging disabled misconfiguration detected in code 

 Last updated 1 month ago 

 Was this helpful?

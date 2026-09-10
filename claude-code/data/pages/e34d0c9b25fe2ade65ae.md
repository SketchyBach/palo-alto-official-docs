---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/ai-and-machine-learning/appsec2-azure-48
fetched_at: 2026-09-06T11:11:17Z
source: cortex-platform
---

# Azure Databricks Workspaces not using customer-managed key for root DBFS encryption misconfiguration | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 AI And Machine Learning 

 Azure Databricks Workspaces not using customer-managed key for root DBFS encryption misconfiguration 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC2_AZURE_48 

 Category - Subcategory 

 Storage - Encryption 

 Provider 

 AZURE 

 Severity 

 LOW 

 Framework 

 ARM, Bicep, Terraform, Terraform Plan 

 Impact 

 This rule checks whether Databricks Workspaces leverage a customer-managed key for root DBFS encryption. DBFS (Databricks File System) is the distributed file system used by Databricks clusters. Encrypting the root DBFS adds an extra layer of security, ensuring that even in the event of unauthorized access, the data remains inaccessible and secure. Customer-managed keys enhance security by giving you control over encryption, strengthening your security posture. 

 How to Fix 

 Resource: Microsoft.Databricks/workspaces 

 Arguments: prepareEncryption/value 

 Set the customer_managed_key_enabled attribute to true during Azure Databricks workspace creation. This enables customer-managed key encryption for your DBFS root data at rest. [source,go] 

 "resources": [ { "type": "Microsoft.Databricks/workspaces", "properties": { ... "parameters": { "prepareEncryption": { 

 Ask Copy 

 "value": true 
 }, 

 Ask Copy 

 "encryption": { 

 Ask Copy 

 "value": { 

 Ask Copy 

 ... 

 Ask Copy 

 } 
 }, 
 } 

 } } ] 

 Previous Azure Synapse Workspace vulnerability assessment is disabled misconfiguration detected in code 

 Next Azure Machine learning workspace configured with overly permissive network access misconfiguration d 

 Last updated 1 month ago 

 Was this helpful?

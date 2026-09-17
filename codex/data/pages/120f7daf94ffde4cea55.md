---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/storage/appsec-gcp-121
fetched_at: 2026-09-16T09:10:40Z
source: cortex-platform
---

# BigQuery tables do not have deletion protection enabled misconfiguration detected in code | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 Storage 

 BigQuery tables do not have deletion protection enabled misconfiguration detected in code 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_GCP_121 

 Category - Subcategory 

 Public Exposure - Database Endpoints 

 Provider 

 GCP 

 Severity 

 MEDIUM 

 Framework 

 Terraform, Terraform Plan 

 Impact 

 This rule (APPSEC_GCP_121) is looking to confirm that deletion protection is enabled for all BigQuery tables in a Google Cloud Platform (GCP) environment. The reason this is important is because tables without deletion protection can be deleted either accidentally or maliciously. In both cases, valuable data could be permanently lost. By ensuring deletion protection is enabled, the data within the tables is safeguarded from such accidental or malicious deletions, maintaining its integrity and availability. 

 How to Fix 

 Resource: google_bigquery_table 

 Arguments: deletion_protection 

 To fix this issue, you need to enable deletion protection in your BigQuery tables. This can be done by setting the deletion_protection argument to true in the BigQuery table resource block in your Terraform code. 

 The above code is secure because it ensures that BigQuery tables have deletion protection enabled. This means that these tables cannot be deleted without first disabling the deletion protection, greatly reducing the risk of tables being accidentally deleted. This is a crucial safeguard to prevent the accidental loss of data. [source,go] 

 resource "google_bigquery_table" "example" { dataset_id = google_bigquery_dataset.example.dataset_id table_id = "example_table" 

 deletion_protection = true } 

 Previous Spanner Database does not have drop protection enabled misconfiguration detected in code 

 Next Big Table Instances do not have deletion protection enabled misconfiguration detected in code 

 Last updated 1 month ago 

 Was this helpful?

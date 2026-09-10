---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/storage/appsec-gcp-58
fetched_at: 2026-09-06T11:14:18Z
source: cortex-platform
---

# GCP SQL Server instance database flag 'cross db ownership chaining' is enabled misconfiguration dete | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 Storage 

 GCP SQL Server instance database flag 'cross db ownership chaining' is enabled misconfiguration dete 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_GCP_58 

 Category - Subcategory 

 Public Exposure - Database Endpoints 

 Provider 

 GCP 

 Severity 

 LOW 

 Framework 

 Terraform, Terraform Plan 

 Mapped CSPM/KSPM Rule 

 1f618d6e-42c5-4861-b7bb-6636a597aeac 

 Impact 

 Use the cross db ownership chaining database flag to configure cross-database ownership chaining for an instance of Microsoft SQL Server. This server option allows you to control cross-database ownership chaining at database-level, or to allow cross-database ownership chaining for all databases. We recommend you disable the cross db ownership chaining flag for Cloud SQL SQL Server instances, by setting it to Off . Enabling cross db ownership chaining is only effective when all of the databases hosted by the instance of SQL Server participate in cross-database ownership chaining, and you are aware of the security implications of this setting. 

 How to Fix 

 Resource: google_sql_database_instance 

 Arguments: database_version = "SQLSERVER_* " settings::database_flags: key:"cross db ownership chaining", value: by default set to "on" [source,go] 

 resource "google_sql_database_instance" "default" { name = "master-instance" database_version = "SQLSERVER_2017_STANDARD" region = "us-central1" 

 settings { 

 database_flags { 

 name = "cross db ownership chaining"" 

 value = "off" } } } 

 Previous GCP MySQL instance with local_infile database flag is not disabled misconfiguration detected in code 

 Next GCP SQL Server instance database flag 'contained database authentication' is enabled misconfiguratio 

 Last updated 1 month ago 

 Was this helpful?

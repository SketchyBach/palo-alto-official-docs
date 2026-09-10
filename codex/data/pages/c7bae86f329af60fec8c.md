---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/storage/appsec-oci-7
fetched_at: 2026-09-06T11:14:22Z
source: cortex-platform
---

# OCI Object Storage bucket does not emit object events misconfiguration detected in code | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 Storage 

 OCI Object Storage bucket does not emit object events misconfiguration detected in code 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_OCI_7 

 Category - Subcategory 

 Storage - Alerting 

 Provider 

 ORACLE 

 Severity 

 LOW 

 Framework 

 Terraform, Terraform Plan 

 Impact 

 This rule identifies the OCI Object Storage buckets that are disabled with object events emission. Monitoring and alerting on object events of bucket objects will help in identifying changes bucket objects. It is recommended that buckets should be enabled to emit object events. 

 How to Fix 

 Resource: oci_objectstorage_bucket 

 Arguments: agent_config.is_monitoring_disabled [source,go] 

 resource "oci_objectstorage_bucket" "pass" { ... object_events_enabled = true ... } 

 Previous OCI Block Storage Block Volumes are not encrypted with a Customer Managed Key (CMK) misconfiguration 

 Next OCI Object Storage Bucket has object Versioning disabled misconfiguration detected in code 

 Last updated 1 month ago 

 Was this helpful?

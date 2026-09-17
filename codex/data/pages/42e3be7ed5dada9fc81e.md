---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/logging/appsec-ali-35
fetched_at: 2026-09-16T09:09:15Z
source: cortex-platform
---

# Alibaba Cloud RDS instance does not have log_duration enabled misconfiguration detected in code | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 Logging 

 Alibaba Cloud RDS instance does not have log_duration enabled misconfiguration detected in code 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_ALI_35 

 Category - Subcategory 

 Logging - Disabled or missing 

 Provider 

 ALIBABA_CLOUD 

 Severity 

 LOW 

 Framework 

 Terraform 

 Impact 

 This rule ensures that the log_duration parameter is enabled for Alibaba Cloud RDS instances. Enabling this parameter helps log the duration of each completed statement, providing valuable insights into query performance and execution time. This data is critical for monitoring database performance and identifying slow queries. 

 Failing to enable this parameter can limit visibility into query execution metrics, making it difficult to diagnose performance issues and optimize database operations. 

 How to Fix 

 Resource: alicloud_rds_instance 

 Arguments: log_duration 

 To mitigate this issue, ensure the log_duration parameter is set to on in the RDS instance configuration. 

 Example: [source,go] 

 resource "alicloud_rds_instance" "example" { ... 

 parameter { 

 name = "log_duration" 

 value = "on" } } 

 Previous Alibaba Cloud RDS Instance SQL Collector Retention Period is less than 180 misconfiguration detected 

 Next Alibaba Cloud RDS instance has log_disconnections disabled misconfiguration detected in code 

 Last updated 1 month ago 

 Was this helpful?

---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/logging/appsec-ali-25
fetched_at: 2026-09-06T11:12:31Z
source: cortex-platform
---

# Alibaba Cloud RDS Instance SQL Collector Retention Period is less than 180 misconfiguration detected | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 Logging 

 Alibaba Cloud RDS Instance SQL Collector Retention Period is less than 180 misconfiguration detected 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_ALI_25 

 Category - Subcategory 

 Logging - Retention 

 Provider 

 ALIBABA_CLOUD 

 Severity 

 LOW 

 Framework 

 Terraform 

 Impact 

 This rule ensures that Alibaba Cloud RDS (Relational Database Service) instances have the SQL collector enabled and its retention period set to 180 days or more. Enabling the SQL collector and setting an adequate retention period helps in tracking and analyzing the SQL queries made to the database, which can be useful for performance tuning, troubleshooting, and security analysis. 

 Failing to enable the SQL collector or setting a short retention period may result in insufficient data for analysis, making it difficult to identify performance issues or security threats. 

 How to Fix 

 Resource: alicloud_db_instance 

 Arguments: sql_collector_status, sql_collector_config_value 

 To mitigate this issue, ensure that the sql_collector_status attribute is set to Enabled , and the sql_collector_config_value attribute is set to 180 or more in the alicloud_db_instance resource. 

 Example: [source,go] 

 resource "alicloud_db_instance" "example" { ... 

 sql_collector_status = "Enabled" 

 sql_collector_config_value = 180 } 

 Previous Alibaba Cloud OSS bucket has access logging enabled misconfiguration detected in code 

 Next Alibaba Cloud RDS instance does not have log_duration enabled misconfiguration detected in code 

 Last updated 1 month ago 

 Was this helpful?

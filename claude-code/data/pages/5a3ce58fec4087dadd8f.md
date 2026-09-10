---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/logging/appsec-ali-38
fetched_at: 2026-09-06T11:12:31Z
source: cortex-platform
---

# Alibaba Cloud RDS log audit is disabled misconfiguration detected in code | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 Logging 

 Alibaba Cloud RDS log audit is disabled misconfiguration detected in code 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_ALI_38 

 Category - Subcategory 

 Logging - Disabled or missing 

 Provider 

 ALIBABA_CLOUD 

 Severity 

 LOW 

 Framework 

 Terraform 

 Impact 

 This rule ensures that log auditing is enabled for Alibaba Cloud RDS instances. Enabling log audit provides detailed records of database activities, including user actions, queries, and system events. These logs are essential for detecting anomalies, investigating incidents, and maintaining compliance with regulatory and organizational requirements. 

 Failing to enable log auditing can lead to a lack of visibility into database activity, increasing the risk of undetected malicious actions or compliance violations. 

 How to Fix 

 Resource: alicloud_log_audit 

 Arguments: variable_map.rds_enabled 

 To mitigate this issue, ensure the rds_enabled attribute in the alicloud_log_audit resource is set to True. 

 Example: [source,go] 

 resource "alicloud_log_audit" "example" { ... variable_map = [ { 

 rds_enabled = true } ] } 

 Previous Alibaba Cloud RDS instance has log_disconnections disabled misconfiguration detected in code 

 Next AWS CloudTrail log validation is not enabled in all regions misconfiguration detected in code 

 Last updated 1 month ago 

 Was this helpful?

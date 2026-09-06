---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/logging/appsec-aws-243
fetched_at: 2026-09-06T11:12:36Z
source: cortex-platform
---

# AWS MWAA environment has worker logs disabled misconfiguration detected in code | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 Logging 

 AWS MWAA environment has worker logs disabled misconfiguration detected in code 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_AWS_243 

 Category - Subcategory 

 Logging - Disabled or missing 

 Provider 

 AWS 

 Severity 

 LOW 

 Framework 

 Terraform 

 Impact 

 It is recommended to have a proper logging process for AWS MWAA environment worker in order to track configuration changes conducted manually and programmatically and trace back unapproved changes. 

 How to Fix 

 [source,go] 

 resource "aws_mwaa_environment" "pass" { dag_s3_path = "dags/" execution_role_arn = "aws_iam_role.example.arn" 

 logging_configuration { worker_logs { enabled = true log_level = "CRITICAL" } } 

 name = "example" 

 network_configuration { security_group_ids = ["aws_security_group.example.id"] subnet_ids = "aws_subnet.private[*].id" } 

 source_bucket_arn = "aws_s3_bucket.example.arn" } 

 Previous AWS MWAA environment has scheduler logs disabled misconfiguration detected in code 

 Next AWS MWAA environment has webserver logs disabled misconfiguration detected in code 

 Last updated 1 month ago 

 Was this helpful?

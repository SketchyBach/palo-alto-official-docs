---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/logging/appsec-aws-176
fetched_at: 2026-09-16T09:09:15Z
source: cortex-platform
---

# AWS WAF Web Access Control Lists logging is disabled misconfiguration detected in code | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 Logging 

 AWS WAF Web Access Control Lists logging is disabled misconfiguration detected in code 

 AWS WAF Web Access Control Lists logging is disabled misconfiguration detected in code 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_AWS_176 

 Category - Subcategory 

 Logging - Disabled or missing 

 Provider 

 AWS 

 Severity 

 LOW 

 Framework 

 Terraform, Terraform Plan 

 Impact 

 Amazon WAF is a web application firewall service that lets you monitor web requests that are forwarded to Amazon API Gateway APIs, Amazon CloudFront distributions, or Application Load Balancers in order to help protect them from attacks. To get detailed information about the web traffic analyzed by your Web Access Control Lists (Web ACLs) you must enable logging. The log entries include the time that Amazon WAF received the request from your AWS resource, detailed information about the request, and the action for the rule that each request matched. You can also send these logs to an Amazon Kinesis Firehose delivery stream with a configured storage destination. 

 How to Fix 

 Resource: aws_waf_web_acl 

 Attribute: logging_configuration [source,go] 

 { "resource "aws_waf_web_acl" "example" { 

 ... other configuration ... 

 logging_configuration { log_destination = "${aws_kinesis_firehose_delivery_stream.example.arn}" 

 redacted_fields { field_to_match { type = "URI" } 

 field_to_match { data = "referer" type = "HEADER" } 

 } } 

 } ", } 

 Previous AWS CloudWatch Log groups encrypted using default encryption key instead of KMS CMK misconfiguration 

 Next AWS AppSync's logging is disabled misconfiguration detected in code 

 Last updated 1 month ago 

 Was this helpful?

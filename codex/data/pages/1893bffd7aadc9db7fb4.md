---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/logging/appsec2-aws-39
fetched_at: 2026-09-06T11:12:45Z
source: cortex-platform
---

# Domain Name System (DNS) query logging is not enabled for Amazon Route 53 hosted zones misconfigurat | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 Logging 

 Domain Name System (DNS) query logging is not enabled for Amazon Route 53 hosted zones misconfigurat 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC2_AWS_39 

 Category - Subcategory 

 Logging - Disabled or missing 

 Provider 

 AWS 

 Severity 

 LOW 

 Framework 

 Terraform, Terraform Plan 

 Impact 

 This rule detects if DNS query logging is not enabled for Amazon Route 53 hosted zones. 

 How to Fix 

 Resource: aws_route53_query_logging_config, aws_route53_zone 

 Arguments: query_logging_config and zone_id 

 To fix this issue, enable DNS query logging for the Route 53 hosted zones in your Terraform code. You can do this by adding the query_logging_config argument along with the corresponding zone_id argument to the aws_route53_zone resource block in your Terraform code. 

 Secure code example: 

 The above code enables DNS query logging for a Route 53 hosted zone by creating a aws_route53_query_logging_config resource and associating it with the corresponding aws_route53_zone resource. The aws_cloudwatch_log_group resource is created as well, providing a destination for the logged DNS queries. 

 This configuration ensures that DNS query logging is enabled for the specified Route 53 hosted zone. [source,go] 

 resource "aws_route53_query_logging_config" "example" { name = "example-logging-config" record_type = "QUERY_LOGGING" cloudwatch_logs_group_arn = aws_cloudwatch_log_group.example.arn } 

 resource "aws_route53_zone" "example" { name = "example.com." query_logging_config { id = aws_route53_query_logging_config.example.id region = "us-east-1" } } 

 resource "aws_cloudwatch_log_group" "example" { name = "example-logs" } 

 Previous AWS Codecommit is not associated with an approval rule misconfiguration detected in code 

 Next AWS Config Recording is disabled misconfiguration detected in code 

 Last updated 1 month ago 

 Was this helpful?

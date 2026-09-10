---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/logging/appsec-aws-48
fetched_at: 2026-09-06T11:12:32Z
source: cortex-platform
---

# Amazon MQ Broker logging is not enabled misconfiguration detected in code | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 Logging 

 Amazon MQ Broker logging is not enabled misconfiguration detected in code 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_AWS_48 

 Category - Subcategory 

 Logging - Disabled or missing 

 Provider 

 AWS 

 Severity 

 MEDIUM 

 Framework 

 Terraform, Terraform Plan 

 Impact 

 Amazon MQ is a broker service built on Apache ActiveMQ. As a message broker, MQ allows applications to communicate using various programming languages, operating systems and formal messaging protocols. Amazon MQ is integrated with CloudTrail and provides a record of the Amazon MQ calls made by a user, role, or AWS service. It supports logging both the request parameters and the responses for APIs as events in CloudTrail. Logging MQ ensures developers can trace all requests and responses, and ensure they are only used for their predefined message brokering settings. We recommend you enable Amazon MQ Broker Logging. 

 How to Fix 

 [source,go] 

 resource "aws_mq_broker" "enabled" { broker_name = "example" engine_type = "ActiveMQ" engine_version = "5.16.3" host_instance_type = "mq.t3.micro" 

 user { password = "admin123" username = "admin" } 

 logs { general = true } } 

 Previous AWS EKS control plane logging disabled misconfiguration detected in code 

 Next AWS CloudWatch Log groups not configured with definite retention days misconfiguration detected in c 

 Last updated 1 month ago 

 Was this helpful?

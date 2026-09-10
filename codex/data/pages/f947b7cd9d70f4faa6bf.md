---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/public-exposure/appsec-aws-69
fetched_at: 2026-09-06T11:13:14Z
source: cortex-platform
---

# AWS MQ is publicly accessible misconfiguration detected in code | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 Public Exposure 

 AWS MQ is publicly accessible misconfiguration detected in code 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_AWS_69 

 Category - Subcategory 

 Public Exposure - Database Endpoints 

 Provider 

 AWS 

 Severity 

 LOW 

 Framework 

 CloudFormation, Serverless, Terraform, Terraform Plan 

 Mapped CSPM/KSPM Rule 

 ac5e8046-6e9f-4eba-8132-9a6500fd760e 

 Impact 

 This rule identifies the AWS MQ brokers which are publicly accessible. It is advisable to use MQ brokers privately only from within your AWS Virtual Private Cloud (VPC). Ensure that the AWS MQ brokers provisioned in your AWS account are not publicly accessible from the Internet to avoid sensitive data exposure and minimize security risks. 

 How to Fix 

 To fix this issue, ensure that the publicly_accessible property in the aws_mq_broker resource is set to false . 

 Example: 

 Resources: MyMQBroker: Type: AWS::AmazonMQ::Broker Properties: ... PubliclyAccessible: false ... 

 [source,go] 

 resource "aws_mq_broker" "example" { ... publicly_accessible = false ... } 

 CloudFormation 

 To fix this issue, ensure that the PubliclyAccessible property in the AWS::AmazonMQ::Broker resource is set to false . 

 Example: 

 [source,yaml] 

 Previous AWS API gateway methods are publicly accessible misconfiguration detected in code 

 Next AWS Elasticsearch domain is not configured with HTTPS misconfiguration detected in code 

 Last updated 1 month ago 

 Was this helpful?

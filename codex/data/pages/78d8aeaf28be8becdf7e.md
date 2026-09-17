---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/storage/appsec-aws-215
fetched_at: 2026-09-16T09:10:32Z
source: cortex-platform
---

# AWS Appsync API Cache is not encrypted in transit misconfiguration detected in code | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 Storage 

 AWS Appsync API Cache is not encrypted in transit misconfiguration detected in code 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_AWS_215 

 Category - Subcategory 

 Storage - Encryption 

 Provider 

 AWS 

 Severity 

 LOW 

 Framework 

 Terraform 

 Impact 

 This rule identifies the AWS Appsync API that are configured with disabled in-transit data encryption. It is recommended that these resources will be configured with in-transit data encryption to minimize risk for sensitive data being leaked. 

 How to Fix 

 [source,go] 

 resource "aws_appsync_api_cache" "pass" { api_id = aws_appsync_graphql_api.default.id transit_encryption_enabled = true at_rest_encryption_enabled = true ttl = 60 type = "SMALL" api_caching_behavior = "FULL_REQUEST_CACHING" } 

 Previous AWS Appsync API Cache is not encrypted at rest misconfiguration detected in code 

 Next AWS CodePipeline artifactStore is not encrypted by Key Management Service (KMS) using a Customer Man 

 Last updated 1 month ago 

 Was this helpful?

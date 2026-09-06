---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/storage/appsec-aws-214
fetched_at: 2026-09-06T11:14:00Z
source: cortex-platform
---

# AWS Appsync API Cache is not encrypted at rest misconfiguration detected in code | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 Storage 

 AWS Appsync API Cache is not encrypted at rest misconfiguration detected in code 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_AWS_214 

 Category - Subcategory 

 Storage - Encryption 

 Provider 

 AWS 

 Severity 

 LOW 

 Framework 

 Terraform 

 Impact 

 Encryption of data at rest is a security feature that helps prevent unauthorized access to your data. The feature uses AWS Key Management Service (AWS KMS) to store and manage your encryption keys and the Advanced Encryption Standard algorithm with 256-bit keys (AES-256) to perform the encryption. If enabled, the feature encrypts the domain's: indices, logs, swap files, all data in the application directory, and automated snapshots. We recommend you implement encryption at rest in order to protect a data store containing sensitive information from unauthorized access, and fulfill compliance requirements. 

 How to Fix 

 [source,go] 

 resource "aws_appsync_api_cache" "pass" { api_id = aws_appsync_graphql_api.default.id transit_encryption_enabled = true at_rest_encryption_enabled = true ttl = 60 type = "SMALL" api_caching_behavior = "FULL_REQUEST_CACHING" } 

 Previous AWS EBS Volume is not encrypted by Key Management Service (KMS) using a Customer Managed Key (CMK) m 

 Next AWS Appsync API Cache is not encrypted in transit misconfiguration detected in code 

 Last updated 1 month ago 

 Was this helpful?

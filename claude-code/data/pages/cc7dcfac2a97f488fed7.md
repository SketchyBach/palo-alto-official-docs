---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/storage/appsec-aws-221
fetched_at: 2026-09-16T09:10:20Z
source: cortex-platform
---

# AWS Code Artifact Domain is not encrypted by KMS using a Customer Managed Key (CMK) misconfiguration | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 Storage 

 AWS Code Artifact Domain is not encrypted by KMS using a Customer Managed Key (CMK) misconfiguration 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_AWS_221 

 Category - Subcategory 

 Storage - Encryption 

 Provider 

 AWS 

 Severity 

 LOW 

 Framework 

 Terraform 

 Impact 

 This rule identifies Code Artifact Domains which are encrypted with default KMS keys and not with Keys managed by Customer. It is a best practice to use customer managed KMS Keys to encrypt your Code Artifact Domain data. It gives you full control over the encrypted data. 

 How to Fix 

 [source,go] 

 resource "aws_codeartifact_domain" "pass" { domain = "example" encryption_key = aws_kms_key.example.arn tags = { "key" = "value" } } 

 Previous AWS CodePipeline artifactStore is not encrypted by Key Management Service (KMS) using a Customer Man 

 Next AWS copied AMIs are not encrypted misconfiguration detected in code 

 Last updated 1 month ago 

 Was this helpful?

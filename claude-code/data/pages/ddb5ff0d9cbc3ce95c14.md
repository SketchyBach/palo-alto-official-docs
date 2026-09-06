---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/storage/appsec-aws-147
fetched_at: 2026-09-06T11:13:54Z
source: cortex-platform
---

# CodeBuild projects are not encrypted misconfiguration detected in code | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 Storage 

 CodeBuild projects are not encrypted misconfiguration detected in code 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_AWS_147 

 Category - Subcategory 

 Storage - Encryption 

 Provider 

 AWS 

 Severity 

 MEDIUM 

 Framework 

 Terraform, Terraform Plan 

 Impact 

 Encrypting your CodeBuild projects helps protect your data from unauthorized access or tampering. That way, you can ensure that only authorized users can access and modify the contents of your projects. Such action can help protect against external threats such as hackers or malware, as well as internal threats such as accidental or unauthorized access. 

 How to Fix 

 Resource: aws_codebuild_project 

 Arguments: encryption_key [source,go] 

 resource "aws_codebuild_project" "example" { ... 

 encryption_key = "AWS_Key_Management_Service_example" } 

 Previous AWS RDS DB snapshot is not encrypted misconfiguration detected in code 

 Next AWS Secrets Manager secret not encrypted by Customer Managed Key (CMK) misconfiguration detected in 

 Last updated 1 month ago 

 Was this helpful?

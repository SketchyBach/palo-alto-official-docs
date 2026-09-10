---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/iam/appsec-aws-205
fetched_at: 2026-09-06T11:12:03Z
source: cortex-platform
---

# AWS AMI launch permissions are not limited misconfiguration detected in code | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 IAM 

 AWS AMI launch permissions are not limited misconfiguration detected in code 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_AWS_205 

 Category - Subcategory 

 IAM - Overly Permissive 

 Provider 

 AWS 

 Severity 

 LOW 

 Framework 

 Terraform 

 Impact 

 It is recommended not to give the ability to launch AMIs across multiple accounts, and if it is implemented, make sure it is properly used. 

 How to Fix 

 [source,go] 

 resource "aws_ami_launch_permission" "remove_equivalent_block" { 

 image_id = "ami-2345678" 

 account_id = "987654321" 

 } 

 Previous SNS topic policy is public and access is not restricted to specific services or principals misconfig 

 Next AWS Key Management Service (KMS) key is disabled misconfiguration detected in code 

 Last updated 1 month ago 

 Was this helpful?

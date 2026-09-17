---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/iam/appsec-aws-13
fetched_at: 2026-09-16T09:09:08Z
source: cortex-platform
---

# AWS IAM password policy does allow password reuse misconfiguration detected in code | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 IAM 

 AWS IAM password policy does allow password reuse misconfiguration detected in code 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_AWS_13 

 Category - Subcategory 

 IAM - Authentication Policies 

 Provider 

 AWS 

 Severity 

 HIGH 

 Framework 

 Terraform, Terraform Plan 

 Impact 

 Password policies are used to enforce the creation and use of password complexity. Your IAM password policy must prevent reuse of passwords. Each password should be brand new to increase security, especially from a brute force attack. 

 How to Fix 

 [source,go] 

 resource "aws_iam_account_password_policy" "strict" { ... 

 apassword_reuse_prevention = 24 } 

 Previous AWS IAM password policy does not have a number misconfiguration detected in code 

 Next AWS IAM password policy does not have a symbol misconfiguration detected in code 

 Last updated 1 month ago 

 Was this helpful?

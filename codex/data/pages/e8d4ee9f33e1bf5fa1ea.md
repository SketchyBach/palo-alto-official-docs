---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/iam/appsec-aws-301
fetched_at: 2026-09-16T09:09:09Z
source: cortex-platform
---

# AWS Lambda Function resource-based policy is overly permissive misconfiguration detected in code | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 IAM 

 AWS Lambda Function resource-based policy is overly permissive misconfiguration detected in code 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_AWS_301 

 Category - Subcategory 

 IAM - Overly Permissive 

 Provider 

 AWS 

 Severity 

 LOW 

 Framework 

 Terraform, Terraform Plan 

 Mapped CSPM/KSPM Rule 

 dc0d3fb7-4c3e-4930-b68b-931908d36d71 

 Impact 

 This rule is examining AWS Lambda functions to ensure they aren't publicly accessible. Having AWS Lambda functions that can be accessed by anyone can lead to sinister activities such as data theft, data manipulation, or other forms of unauthorized access. It's considered bad practice and a security risk, as it allows any anonymous user to invoke the function, potentially leading to misuse of the function or exposure of sensitive information. Therefore, it's important to have controls on who can execute the function, for example, authenticated or identified users only. 

 How to Fix 

 Resource: aws_lambda_permission 

 Arguments: principal 

 To fix this issue, ensure the AWS Lambda function is not publicly accessible by restricting access to trusted entities only. Set 'principal' to a specific AWS resource or user-account other than '*'. [source,go] 

 resource "aws_lambda_permission" "with_s3" { statement_id = "AllowExecutionFromS3Bucket" action = "lambda:InvokeFunction" function_name = aws_lambda_function.example.function_name 

 principal = "*" source_arn = "arn:aws:s3:::example_bucket" } 

 Previous IAM policies allow write access without constraints misconfiguration detected in code 

 Next Authorization type for API GatewayV2 routes is not specified misconfiguration detected in code 

 Last updated 1 month ago 

 Was this helpful?

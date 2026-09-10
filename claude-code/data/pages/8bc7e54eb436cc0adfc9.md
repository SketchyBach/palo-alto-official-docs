---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/compute/appsec-aws-272
fetched_at: 2026-09-06T11:11:24Z
source: cortex-platform
---

# AWS Lambda function is not configured to validate code-signing misconfiguration detected in code | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 Compute 

 AWS Lambda function is not configured to validate code-signing misconfiguration detected in code 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_AWS_272 

 Category - Subcategory 

 Compute - Default Credentials Or Auth 

 Provider 

 AWS 

 Severity 

 HIGH 

 Framework 

 Terraform, Terraform Plan 

 Impact 

 This rule ensures that an AWS Lambda function has been properly configured to validate code-signing. If not correctly set up, it could mean that your AWS Lambda function is running code that has not been authenticated. This lack of validation raises a significant security concern, as your service could be running code that has been tampered with or injected with malicious code. This could lead to unauthorized access, data leaks, or compromise of the service. Therefore, it is vital to check and ensure that Lambda functions are enforced to validate code-signing for security. 

 How to Fix 

 Resource: aws_lambda_function 

 Arguments: code_signing_config_arn 

 To address the issue, you need to enable the code-signing configuration for your AWS Lambda function. Code-signing adds an extra layer of security to your application by ensuring that the deployed code is not tampered with. 

 Example: 

 In the above code, aws_lambda_function is configured with the code_signing_config_arn attribute. [source,go] 

 resource "aws_lambda_function" "example" { function_name = "example" s3_bucket = aws_signer_signing_job.job.signed_object[0].s3[0].bucket s3_key = aws_signer_signing_job.this.signed_object[0].s3[0].key handler = "exports.test" runtime = "nodejs12.x" 

 code_signing_config_arn = aws_lambda_code_signing_config.example.arn } 

 resource "aws_lambda_code_signing_config" "example" { allowed_publishers { signing_profile_version_arns = [aws_signer_signing_profile.example.version_arn] } 

 policies { untrusted_artifact_on_deployment = "Enforce" } } 

 Previous AWS HTTP and HTTPS target groups do not define health check misconfiguration detected in code 

 Next API Gateway method setting is not set to encrypted caching misconfiguration detected in code 

 Last updated 1 month ago 

 Was this helpful?

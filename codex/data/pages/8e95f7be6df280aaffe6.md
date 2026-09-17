---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/iam/appsec-aws-355
fetched_at: 2026-09-16T09:09:09Z
source: cortex-platform
---

# IAM policy document allows all resources with restricted actions misconfiguration detected in code | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 IAM 

 IAM policy document allows all resources with restricted actions misconfiguration detected in code 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_AWS_355 

 Category - Subcategory 

 IAM - Overly Permissive 

 Provider 

 AWS 

 Severity 

 HIGH 

 Framework 

 Terraform, Terraform Plan 

 Impact 

 This rule checks IAM policies for statements that allow unrestricted resource access ('*') for actions that can and should be restricted to specific resources. This behavior is potentially unsafe because it broadens the scope of access controls and increases the risk of unauthorized access. Prisma Cloud checks the AWS documentation for IAM actions that can be restricted to a resource and recommends defining a specific resource rather than '*'. For example, the s3:PutObject action can be restricted to a specific S3 bucket instead of allowing uploads to any S3 bucket using '*'. It is best security practice to define granular permissions to each user access, as unrestricted access can lead to unwanted manipulations or data breaches. Therefore, it is recommended to specify restrictions and assign minimum necessary access rights. 

 How to Fix 

 Resource: aws_iam_policy 

 Arguments: policy 

 Review your IaC IAM policies to identify if any resources are set to "*" that can be restricted, which grants full access to all resources of that type. For each identified statement, replace "*" with the specific Amazon Resource Names (ARNs) corresponding to the resources users or roles actually need access to. 

 The following Terraform code example describes how to define specific resources in the Resource field of the Statement block, replacing "*". [source,go] 

 resource "aws_iam_policy" "example" { name = "test_policy" path = "/" description = "My test policy" 

 policy = jsonencode({ Version = "2012-10-17" Statement = [ { Action = [ "states:CreateStateMachine", ] Effect = "Allow" 

 Resource = "*" 

 Resource = "arn:aws:<resource_type>:::" }, ] }) } 

 Previous AWS Access key enabled on root account misconfiguration detected in code 

 Next Data source IAM policy document allows all resources with restricted actions misconfiguration detect 

 Last updated 1 month ago 

 Was this helpful?

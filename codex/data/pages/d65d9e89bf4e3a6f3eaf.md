---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/compute/appsec-aws-153
fetched_at: 2026-09-16T09:09:00Z
source: cortex-platform
---

# Autoscaling groups did not supply tags to launch configurations misconfiguration detected in code | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 Compute 

 Autoscaling groups did not supply tags to launch configurations misconfiguration detected in code 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_AWS_153 

 Category - Subcategory 

 Compute - Startup Script Leaks 

 Provider 

 AWS 

 Severity 

 LOW 

 Framework 

 Terraform, Terraform Plan 

 Impact 

 This rule detects whether autoscaling groups supply tags to their launch configurations. Tags provide several benefits: they enable tag-based access control through conditions in your IAM policies, they aid in identifying and organizing AWS resources, and they allow for resource-level permissions in your Amazon EC2 Auto Scaling identity-based policies. By tagging resources, you can apply the same tag across different AWS services to indicate related resources, and gain fine-grained control over which resources users can manage. 

 How to Fix 

 Resource: aws_autoscaling_group 

 Arguments: launch_configuration, tags 

 To mitigate this issue, ensure that the aws_autoscaling_group resource includes the tag or tags attribute with appropriate key-value pairs. [source,go] 

 resource "aws_autoscaling_group" "example" { ... 

 tags = concat( [ { "key" = "interpolation1" "value" = "value3" "propagate_at_launch" = true }, ... ] ) } 

 Previous AWS API Gateway caching is disabled misconfiguration detected in code 

 Next ECR image scan on push is not enabled misconfiguration detected in code 

 Last updated 1 month ago 

 Was this helpful?

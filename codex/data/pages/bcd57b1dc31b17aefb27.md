---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/iam/appsec-aws-309
fetched_at: 2026-09-06T11:12:05Z
source: cortex-platform
---

# Authorization type for API GatewayV2 routes is not specified misconfiguration detected in code | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 IAM 

 Authorization type for API GatewayV2 routes is not specified misconfiguration detected in code 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_AWS_309 

 Category - Subcategory 

 IAM - Authentication Policies 

 Provider 

 AWS 

 Severity 

 MEDIUM 

 Framework 

 Terraform, Terraform Plan 

 Impact 

 This rule is reviewing AWS API GatewayV2 configurations to ensure that all routes specify an authorization type. Without specifiying an authorization type within the routes, it might allow unauthorized users to access sensitive data or execute harmful operations. Therefore, not setting an authorization type can potentially lead to data leakage or other security issues. 

 How to Fix 

 Resource: aws_apigatewayv2_route 

 Arguments: authorization_type 

 To fix this issue, you should explicitly define the authorization type for the API GatewayV2 route of either "AWS_IAM", "CUSTOM", or "JWT". 

 The provided code is secure because it specifies the authorization type for the API GatewayV2 route which controls who can access the API. In this specific case, we are using AWS_IAM as the authorization type which restricts access to users with the necessary IAM policies. By specifying the authorization type, you can ensure that only authorized users can access your API, thus reducing the risk of unauthorized access. [source,go] 

 resource "aws_apigatewayv2_route" "example" { api_id = aws_apigatewayv2_api.example.id route_key = "$default" target = "integrations/${aws_apigatewayv2_integration.example.id}" authorization_type = "AWS_IAM" } 

 Previous AWS Lambda Function resource-based policy is overly permissive misconfiguration detected in code 

 Next AWS Access key enabled on root account misconfiguration detected in code 

 Last updated 1 month ago 

 Was this helpful?

---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/networking/appsec2-aws-75
fetched_at: 2026-09-16T09:09:34Z
source: cortex-platform
---

# AWS Lambda function URL having overly permissive cross-origin resource sharing permissions misconfig | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 Networking 

 AWS Lambda function URL having overly permissive cross-origin resource sharing permissions misconfig 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC2_AWS_75 

 Category 

 Networking 

 Provider 

 AWS 

 Severity 

 MEDIUM 

 Framework 

 CloudFormation, Terraform, Terraform Plan 

 Mapped CSPM/KSPM Rule 

 c7ce78c7-5412-43f0-ae9c-c90410957502 

 Impact 

 AWS Lambda functions with overly permissive CORS configurations expose sensitive data and functionality to unauthorized access. Improperly configured CORS settings, specifically using wildcard characters in 'allowOrigins', enable any origin to invoke the function. 

 Lambda functions act as crucial components in serverless architectures. Misconfiguration of CORS settings allows malicious actors to send unauthorized requests, potentially leading to data breaches, denial-of-service attacks, or exploitation of the function's logic via cross-site scripting. This undermines the security of your application and its associated data. 

 The impact of this misconfiguration is significant, potentially resulting in unauthorized data access, application logic manipulation, and service disruption. Restricting CORS configuration to specific origins and HTTP methods ensures that only legitimate clients can interact with the Lambda function, mitigating these risks. 

 To remediate, configure Lambda function CORS settings to explicitly list allowed origins ('allowOrigins') and HTTP methods ('allowMethods'). Avoid using wildcard characters. Regularly review and update these settings as your application's access needs change. Employ least privilege principles in configuring your Lambda function's access control. 

 How to Fix 

 To ensure that no open CORS policy is applied to your S3 buckets, configure the cors_rule . Set appropriate allowed origins, allowed methods, and other parameters to restrict access as necessary. [source,go] 

 Example: Type: AWS::Lambda::Function Properties: ... 

 Example: Type: AWS::Lambda::Url Properties: FunctionName: !Ref Example Cors: AllowOrigins: 

 "*" 

 https://example.com AllowMethods: 

 "*" 

 GET ServiceToken: "arn:aws:lambda:us-west-2:123456789012:function:dummy-token" 

 Previous AWS Load Balancers do not use strong ciphers misconfiguration detected in code 

 Next Azure Automation account configured with overly permissive network access misconfiguration detected 

 Last updated 1 month ago 

 Was this helpful?

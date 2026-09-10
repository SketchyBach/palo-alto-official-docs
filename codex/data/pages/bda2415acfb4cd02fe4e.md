---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/iam/appsec-aws-63
fetched_at: 2026-09-06T11:12:02Z
source: cortex-platform
---

# AWS IAM policy documents allow * (asterisk) as a statement's action misconfiguration detected in cod | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 IAM 

 AWS IAM policy documents allow * (asterisk) as a statement's action misconfiguration detected in cod 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_AWS_63 

 Category - Subcategory 

 IAM - Overly Permissive 

 Provider 

 AWS 

 Severity 

 HIGH 

 Framework 

 CloudFormation, Serverless, Terraform, Terraform Plan 

 Impact 

 This rule ensures that IAM policy documents do not allow " " as a statement's actions. Allowing " " in the actions of an IAM policy grants permissions to all actions, which can lead to potential security risks and unauthorized access. This rule checks whether any IAM policy documents contain statements with "Action": "*" , which should be avoided. 

 How to Fix 

 To fix this issue, ensure that the IAM policy statements do not use "*" in the actions. Instead, specify the specific actions that are required. 

 Example: [source,go] 

 Resources: MyIAMRole: Type: AWS::IAM::Role Properties: ... Policies: 

 PolicyName: "example-policy" PolicyDocument: Version: "2012-10-17" Statement: 

 Effect: "Allow" Action: 

 "*" Resource: 

 "arn:aws:s3:::example-bucket" 

 "arn:aws:s3:::example-bucket/*" 

 Previous AWS IAM policies that allow full "-" administrative privileges are created misconfiguration detected 

 Next SQS policy allows all actions misconfiguration detected in code 

 Last updated 1 month ago 

 Was this helpful?

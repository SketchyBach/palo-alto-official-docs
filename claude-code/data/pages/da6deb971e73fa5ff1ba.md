---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/iam/appsec-aws-111
fetched_at: 2026-09-16T09:09:08Z
source: cortex-platform
---

# Write access allowed without constraint misconfiguration detected in code | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 IAM 

 Write access allowed without constraint misconfiguration detected in code 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_AWS_111 

 Category - Subcategory 

 IAM - Overly Permissive 

 Provider 

 AWS 

 Severity 

 LOW 

 Framework 

 CloudFormation, Serverless, Terraform, Terraform Plan 

 Impact 

 This policy allows actions that permit modification of resource-based policies or can otherwise can expose AWS resources to the public via similar actions that can lead to resource exposure. 

 For example: 

 . s3:PutBucketPolicy, s3:PutBucketAcl, and s3:PutObjectAcl grant permissions to modify the properties of S3 buckets or objects for new or existing objects in an S3 bucket, which could expose objects to rogue actors or to the internet. . ecr:SetRepositoryPolicy could allow an attacker to exfiltrate container images (which sometimes unintentionally contain secrets and non-public information), tamper with container images, or otherwise modify. . iam:UpdateAssumeRolePolicy could allow an attacker to create a backdoor by assuming a privileged role in the victim account from an external account. 

 The ability to modify AWS Resource Access Manager, which could allow a malicious actor to share a VPC hosting sensitive or internal services to rogue AWS accounts. Attackers can easily exploit Resource Exposure permissions to expose resources to rogue users or the internet, as shown by endgame, an AWS pentesting tool that was also released by Salesforce. 

 For more info, visit https://cloudsplaining.readthedocs.io/en/latest/glossary/resource-exposure/[cloudsplaning documentation.] 

 How to Fix 

 Example: [source,go] 

 MyRolePolicy: Type: 'AWS::IAM::Policy' Properties: PolicyName: 'MyRolePolicy' Roles: 

 Ref: 'MyRole' PolicyDocument: Version: '2012-10-17' Statement: 

 Effect: Allow Action: 

 's3:PutBucketPolicy' # Remove this Action 

 's3:GetBucketLocation' 

 's3:ListBucket' 

 's3:GetObject' Resource: 

 'arn:aws:s3:::myBucket' 

 'arn:aws:s3:::myBucket/*' 

 Previous IAM policies allow privilege escalation misconfiguration detected in code 

 Next Respective logs of Amazon RDS are disabled misconfiguration detected in code 

 Last updated 1 month ago 

 Was this helpful?

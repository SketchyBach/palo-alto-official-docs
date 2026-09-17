---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/storage/appsec-aws-56
fetched_at: 2026-09-16T09:10:15Z
source: cortex-platform
---

# AWS S3 bucket RestrictPublicBucket is not set to True misconfiguration detected in code | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 Storage 

 AWS S3 bucket RestrictPublicBucket is not set to True misconfiguration detected in code 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_AWS_56 

 Category - Subcategory 

 Storage - Permissions 

 Provider 

 AWS 

 Severity 

 MEDIUM 

 Framework 

 CloudFormation, Serverless, Terraform, Terraform Plan 

 Impact 

 The S3 Block Public Access configuration enables specifying whether S3 should restrict public bucket policies for buckets in this account. Setting RestrictPublicBucket to TRUE restricts access to buckets with public policies to only AWS services and authorized users within this account. Enabling this setting does not affect previously stored bucket policies. Public and cross-account access within any public bucket policy, including non-public delegation to specific accounts, is blocked. 

 How to Fix 

 Resource: AWS::S3::Bucket 

 Arguments: Properties.PublicAccessBlockConfiguration.RestrictPublicBuckets [source,go] 

 Type: 'AWS::S3::Bucket' Properties: ... PublicAccessBlockConfiguration: ... 

 RestrictPublicBuckets: true 

 Previous AWS S3 bucket IgnorePublicAcls is not set to True misconfiguration detected in code 

 Next AWS S3 Bucket has an ACL defined which allows public WRITE access misconfiguration detected in code 

 Last updated 1 month ago 

 Was this helpful?

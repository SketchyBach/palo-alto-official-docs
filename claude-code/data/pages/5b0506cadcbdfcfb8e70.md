---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/iam/appsec-aws-162
fetched_at: 2026-09-06T11:12:02Z
source: cortex-platform
---

# AWS RDS cluster not configured with IAM authentication misconfiguration detected in code | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 IAM 

 AWS RDS cluster not configured with IAM authentication misconfiguration detected in code 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_AWS_162 

 Category - Subcategory 

 IAM - Authentication Policies 

 Provider 

 AWS 

 Severity 

 LOW 

 Framework 

 CloudFormation, Serverless, Terraform, Terraform Plan 

 Mapped CSPM/KSPM Rule 

 f79f0e00-fcf1-49ef-ab0c-b3db225b086d 

 Impact 

 This rule identifies RDS clusters that are not configured with IAM authentication. If you enable IAM authentication you don't need to store user credentials in the database, because authentication is managed externally using IAM. IAM database authentication provides the network traffic to and from database clusters is encrypted using Secure Sockets Layer (SSL), Centrally manage access to your database resources and Profile credentials instead of a password, for greater security. 

 How to Fix 

 Resource: AWS::RDS::DBCluster 

 Arguments: Properties.EnableIAMDatabaseAuthentication [source,go] 

 Resources: Enabled: Type: 'AWS::RDS::DBCluster' Properties: ... 

 EnableIAMDatabaseAuthentication: true 

 Previous RDS database does not have IAM authentication enabled misconfiguration detected in code 

 Next Glacier Vault access policy is public and not restricted to specific services or principals misconfi 

 Last updated 1 month ago 

 Was this helpful?

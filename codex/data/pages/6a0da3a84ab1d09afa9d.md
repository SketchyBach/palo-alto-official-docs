---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/storage/appsec-aws-90
fetched_at: 2026-09-16T09:10:16Z
source: cortex-platform
---

# DocDB TLS is disabled misconfiguration detected in code | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 Storage 

 DocDB TLS is disabled misconfiguration detected in code 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_AWS_90 

 Category - Subcategory 

 Public Exposure - Encryption And Protocols 

 Provider 

 AWS 

 Severity 

 MEDIUM 

 Framework 

 CloudFormation, Serverless, Terraform, Terraform Plan 

 Impact 

 TLS can be used to encrypt the connection between an application and a DocDB cluster. By default, encryption in transit is enabled for newly created clusters. It can optionally be disabled when the cluster is created, or at a later time. When enabled, secure connections using TLS are required to connect to the cluster. 

 How to Fix 

 Resource: AWS::DocDB::DBClusterParameterGroup 

 Argument: Parameters.tls [source,go] 

 Resources: DocDBParameterGroupEnabled: Type: AWS::DocDB::DBClusterParameterGroup Properties: ... Parameters: ... 

 tls: "disabled" 

 tls: "enabled" 

 Previous Athena workgroup does not prevent disabling encryption misconfiguration detected in code 

 Next S3 bucket policy allows lockout all but root user misconfiguration detected in code 

 Last updated 1 month ago 

 Was this helpful?

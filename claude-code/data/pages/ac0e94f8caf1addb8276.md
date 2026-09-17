---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/storage/appsec-aws-327
fetched_at: 2026-09-16T09:10:25Z
source: cortex-platform
---

# AWS RDS DB cluster is encrypted using default KMS key instead of CMK misconfiguration detected in co | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 Storage 

 AWS RDS DB cluster is encrypted using default KMS key instead of CMK misconfiguration detected in co 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_AWS_327 

 Category - Subcategory 

 Storage - Encryption 

 Provider 

 AWS 

 Severity 

 LOW 

 Framework 

 Terraform, Terraform Plan 

 Mapped CSPM/KSPM Rule 

 bbd7ca6b-c899-4edf-9e92-f5262ce8311d 

 Impact 

 This rule is verifying if an Amazon Relational Database Service (RDS) cluster is encrypted using a Key Management Service (KMS) Customer Master Key (CMK). Without this type of encryption, the stored data is not protected against unwanted access or potential security risks. This could lead to data breaches or unauthorized disclosures which can result in regulatory sanctions and loss of customer trust. Therefore, it's important to ensure that the data stored within RDS clusters is encrypted for paramount security measures. 

 How to Fix 

 Resource: aws_rds_cluster 

 Arguments: kms_key_id 

 To fix this issue, you need to ensure that your RDS clusters are encrypted using KMS CMKs. You can do it by adding the "kms_key_id" parameter to the "aws_rds_cluster" resource in your Terraform code. Here is an example of how to do it: [source,go] 

 resource "aws_rds_cluster" "default" { cluster_identifier = "aurora-cluster-demo" availability_zones = ["us-west-2a", "us-west-2b", "us-west-2c"] database_name = "mydb" master_username = "foo" master_password = "bar" backup_retention_period = 5 preferred_backup_window = "07:00-09:00" kms_key_id = "arn:aws:kms:us-west-2:111122223333:key/abcd1234-a123-456a-a12b-a123b4cd56ef" // ensure to replace with your own KMS key ARN } 

 Previous RDS Aurora Clusters do not have backtracking enabled misconfiguration detected in code 

 Next EFS Access Points are not enforcing a root directory misconfiguration detected in code 

 Last updated 1 month ago 

 Was this helpful?

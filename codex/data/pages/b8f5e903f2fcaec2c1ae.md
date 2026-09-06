---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/public-exposure/appsec2-aws-7
fetched_at: 2026-09-06T11:13:38Z
source: cortex-platform
---

# Amazon EMR clusters' security groups are open to the world misconfiguration detected in code | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 Public Exposure 

 Amazon EMR clusters' security groups are open to the world misconfiguration detected in code 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC2_AWS_7 

 Category - Subcategory 

 Public Exposure - Ingress Controls 

 Provider 

 AWS 

 Severity 

 LOW 

 Framework 

 Terraform, Terraform Plan 

 Impact 

 It is generally a good security practice to ensure that the security groups for your Amazon EMR clusters are not open to the world, as this means that the clusters are only accessible from within your private network or from certain approved IP addresses or security groups. This can help to protect your EMR clusters from unauthorized access, as external parties will not be able to connect to them over the internet. 

 How to Fix 

 Resource: aws_emr_cluster and aws_security_group 

 Arguments: ingress of aws_security_group [source,go] 

 resource "aws_emr_cluster" "cluster_ok" { name = "emr-test-arn" release_label = "emr-4.6.0" applications = ["Spark"] 

 ec2_attributes { emr_managed_master_security_group = aws_security_group.block_access_ok.id emr_managed_slave_security_group = aws_security_group.block_access_ok.id instance_profile = "connected_to_aws_iam_instance_profile" } } 

 resource "aws_security_group" "block_access_ok" { name = "block_access" description = "Block all traffic" 

 ingress { from_port = 0 to_port = 0 protocol = "-1" cidr_blocks = ["10.0.0.0/16"] } 

 egress { from_port = 0 to_port = 0 protocol = "-1" cidr_blocks = ["10.0.0.0/16"] } } 

 Previous S3 Bucket does not have public access blocks misconfiguration detected in code 

 Next AWS Default Security Group does not restrict all traffic misconfiguration detected in code 

 Last updated 1 month ago 

 Was this helpful?

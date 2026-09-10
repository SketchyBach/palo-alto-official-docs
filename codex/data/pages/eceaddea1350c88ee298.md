---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/public-exposure/appsec2-aws-5
fetched_at: 2026-09-06T11:13:38Z
source: cortex-platform
---

# Security Groups are not attached to EC2 instances or ENIs misconfiguration detected in code | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 Public Exposure 

 Security Groups are not attached to EC2 instances or ENIs misconfiguration detected in code 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC2_AWS_5 

 Category - Subcategory 

 Public Exposure - Ingress Controls 

 Provider 

 AWS 

 Severity 

 LOW 

 Framework 

 Terraform, Terraform Plan 

 Impact 

 Security groups are an important layer of security for Amazon EC2 instances and network interfaces (ENIs). They act as a virtual firewall for your instances, controlling inbound and outbound traffic to and from your instances. By attaching security groups to your EC2 instances or ENIs, you can specify which traffic is allowed to reach your instances, and which traffic is blocked. This can help to protect your instances from unauthorized access and prevent potential security vulnerabilities. 

 How to Fix 

 Resource: aws_network_interface, aws_instance, aws_security_group 

 Arguments: security_groups of aws_instance or aws_security_group { "resource "aws_network_interface" "test" { subnet_id = "aws_subnet.public_a.id" security_groups = [aws_security_group.ok_sg.id] } 

 resource "aws_instance" "test" { ami = "data.aws_ami.ubuntu.id" instance_type = "t3.micro" security_groups = [aws_security_group.ok_sg.id] } 

 resource "aws_security_group" "ok_sg" { ingress { description = "TLS from VPC" from_port = 443 to_port = 443 protocol = "tcp" cidr_blocks = 0.0.0.0/0 } 

 } ", } 

 Previous AWS Network ACL is not in use misconfiguration detected in code 

 Next S3 Bucket does not have public access blocks misconfiguration detected in code 

 Last updated 1 month ago 

 Was this helpful?

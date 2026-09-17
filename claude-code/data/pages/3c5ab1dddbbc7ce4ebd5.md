---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/compute/appsec-aws-336
fetched_at: 2026-09-16T09:09:01Z
source: cortex-platform
---

# AWS ECS task definition is not configured with read-only access to container root filesystems miscon | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 Compute 

 AWS ECS task definition is not configured with read-only access to container root filesystems miscon 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_AWS_336 

 Category - Subcategory 

 Compute - Default Credentials Or Auth 

 Provider 

 AWS 

 Severity 

 LOW 

 Framework 

 Terraform, Terraform Plan 

 Mapped CSPM/KSPM Rule 

 3215813a-f857-45b9-b6bc-f2ae2cce8b41 

 Impact 

 This rule is checking to ensure that Elastic Container Service (ECS) containers are restricted to read-only access to root file systems. The rule's monitoring is primarily concerned with maintaining a high level of security for the system. 

 Allowing write access to the root file system can pose a high security risk. If a containerized application is compromised, it could enable an attacker to alter the root file system of the host machine, thus compromising the entire system or application. This could lead to significant data loss, system crashes, or a broader security breach. Therefore, it's essential to limit all ECS containers to read-only access to restrict the potential actions of a compromised container. 

 How to Fix 

 Resource: aws_ecs_task_definition 

 Arguments: container_definitions.readonlyRootFilesystem 

 To fix the issue, you need to specify the read_only parameter for each one of your ECS containers in your terraform files. By setting this parameter to true , you guarantee that the ECS container will have read-only access to the root file system. 

 The readonlyRootFilesystem attribute is set to true which restricts the writable access to the root file system. This is secure because it prevents the ECS containers from making changes to the root filesystem. This can be essential in preventing or minimizing damage caused by compromised containers. [source,go] 

 resource "aws_ecs_task_definition" "task_definition" { family = "service" cpu = "256" memory = "512" network_mode = "awsvpc" requires_compatibilities = ["FARGATE"] execution_role_arn = aws_iam_role.ecs_execution_iam_role.arn 

 container_definitions = <<DEFINITION [ { "name": "container", "image": "http://dockr.io/example:latest", "cpu": 256, "memory": 512, "essential": true, "networkMode": "awsvpc", "logConfiguration": { "logDriver": "awslogs", "options": { "awslogs-group": "awslogs-example", "awslogs-region": "us-west-2", "awslogs-stream-prefix": "awslogs-example" } }, "mountPoints": [ { "sourceVolume": "my_volume", "containerPath": "/mnt/my_volume", "readOnly": true } ], "readonlyRootFilesystem": true } ] DEFINITION } 

 Previous ECS task definitions have their own unique process namespace or share the host's process namespace m 

 Next AWS Elastic Beanstalk environment managed platform updates are not enabled misconfiguration detected 

 Last updated 1 month ago 

 Was this helpful?

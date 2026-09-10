---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/storage/appsec-aws-81
fetched_at: 2026-09-06T11:13:51Z
source: cortex-platform
---

# AWS MSK cluster encryption in transit is not enabled misconfiguration detected in code | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 Storage 

 AWS MSK cluster encryption in transit is not enabled misconfiguration detected in code 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_AWS_81 

 Category - Subcategory 

 Storage - Encryption 

 Provider 

 AWS 

 Severity 

 MEDIUM 

 Framework 

 CloudFormation, Terraform, Terraform Plan 

 Mapped CSPM/KSPM Rule 

 18d55f5a-c4de-4fc1-9346-c95b523f58d0 

 Impact 

 This rule identifies AWS Managed Streaming for Apache Kafka clusters having in-transit encryption in a disabled state. 

 In-transit encryption secures data while it's being transferred between brokers. Without it, there's a risk of data interception during transit. 

 It is recommended to enable in-transit encryption among brokers within the cluster. This ensures that all data exchanged within the cluster is encrypted, effectively protecting it from potential eavesdropping and unauthorized access. 

 How to Fix 

 To fix this issue, ensure that the EncryptionInfo property in the AWS::MSK::Cluster resource includes EncryptionInTransit settings with ClientBroker set to TLS and InCluster set to true . 

 Example: [source,go] 

 Resources: MyMSKCluster: Type: AWS::MSK::Cluster Properties: ClusterName: example-cluster KafkaVersion: 2.8.0 NumberOfBrokerNodes: 3 BrokerNodeGroupInfo: ... EncryptionInfo: EncryptionAtRest: DataVolumeKMSKeyId: arn:aws:kms:us-west-2:123456789012:key/example-key-arn EncryptionInTransit: ClientBroker: TLS InCluster: true ... 

 Previous CodeBuild project encryption is disabled misconfiguration detected in code 

 Next Athena workgroup does not prevent disabling encryption misconfiguration detected in code 

 Last updated 1 month ago 

 Was this helpful?

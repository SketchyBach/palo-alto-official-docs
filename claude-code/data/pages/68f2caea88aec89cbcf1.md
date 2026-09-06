---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/public-exposure/appsec2-aws-72
fetched_at: 2026-09-06T11:13:41Z
source: cortex-platform
---

# AWS CloudFront origin protocol policy does not enforce HTTPS-only misconfiguration detected in code | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 Public Exposure 

 AWS CloudFront origin protocol policy does not enforce HTTPS-only misconfiguration detected in code 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC2_AWS_72 

 Category - Subcategory 

 Public Exposure - Encryption And Protocols 

 Provider 

 AWS 

 Severity 

 MEDIUM 

 Framework 

 CloudFormation, Terraform, Terraform Plan 

 Mapped CSPM/KSPM Rule 

 701c180d-c57a-4cc0-bf1b-93d7c5c1a488 

 Impact 

 This rule detects whether the AWS CloudFront distribution is configured to use HTTPS as the only allowed protocol for communication between CloudFront and its origin. Enforcing HTTPS-only ensures that data transmitted over the network is encrypted. Using HTTPS helps protect sensitive information, maintain data integrity, and secure communication channels. If this configuration is not enforced, data could be sent using unencrypted HTTP, which is vulnerable to interception and eavesdropping by malicious actors. 

 How to Fix 

 Resource: AWS::CloudFront::Distribution 

 Arguments: DistributionConfig.Origins.CustomOriginConfig.OriginProtocolPolicy 

 In this example, the origin protocol policy in your AWS CloudFront distribution enforces HTTPS-only communication by configuring the OriginProtocolPolicy attribute to https-only . [source,go] 

 ExamplePassHttpsOnlyDistribution: Type: "AWS::CloudFront::Distribution" Properties: DistributionConfig: Enabled: true Origins: 

 DomainName: "example.data.mediastore.amazonaws.com" # contains important domain name Id: "custom-origin-example" CustomOriginConfig: OriginProtocolPolicy: "https-only" # HTTPS only ... 

 Previous MWAA environment is publicly accessible misconfiguration detected in code 

 Next Azure PostgreSQL Database Server 'Allow access to Azure services' enabled misconfiguration detected 

 Last updated 1 month ago 

 Was this helpful?

---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsiam/configure-cortex-xsiam/cortex-xsiam-data-sources/cloud-service-provider-csp-onboarding/amazon-web-services-cloud-onboarding/aws-post-deployment-verification
fetched_at: 2026-09-06T09:26:58Z
source: cortex-platform
---

# AWS post-deployment verification | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSIAM 

 Cortex XSIAM Documentation 

 Configure Cortex XSIAM 

 Cortex XSIAM Data Sources and Connectors 

 Cloud service provider (CSP) onboarding 

 Amazon Web Services cloud onboarding 

 Cortex XSIAM Data Ingestion Onboarding 

 AWS post-deployment verification 

 After you have completed the AWS onboarding wizard and you have deployed the authentication template in AWS (using CloudFormation or Terraform), verify that the deployment succeeded. 

 After you have deployed the authentication template in Amazon Web Services (AWS), verify that it was successfully deployed. In Cortex XSIAM, select Data Sources & Integrations → Cloud Accounts . Verify the following: 

 The original cloud instance remains in "Pending" state. For more details on pending instances, see Understand pending instances. 

 A new cloud instance appears in the cloud accounts list (separate from the pending instance). 

 The new cloud instance shows status "Connected". 

 The discovery scan starts automatically for every discovered account. 

 Assets appear in the Asset Inventory as discovery progresses. 

 Troubleshooting AWS onboarding 

 If no new cloud instance appears: 

 Check the CloudFormation stack status in the AWS console. The status should be CREATE_COMPLETE . 

 Check the Lambda execution logs in AWS CloudWatch for errors. If the Lambda notification to Cortex XSIAM is not executed, Cortex XSIAM does not create a new cloud instance in Connected stated. 

 You can Manually connect an instance to create the instance from the pending cloud instance. 

 Previous Grant cross-account KMS key access for Control Tower BYOB log collection 

 Next Microsoft Azure cloud onboarding 

 Last updated 1 month ago 

 Was this helpful?

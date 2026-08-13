---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsiam/configure-cortex-xsiam/cortex-xsiam-data-sources/cloud-service-provider-csp-onboarding/amazon-web-services-cloud-onboarding/aws-post-deployment-verification
fetched_at: 2026-08-13T14:57:49Z
source: cortex-platform
---

# AWS post-deployment verification | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

AWS post-deployment verification | Cortex Documentation Portal 

 ⌘ Ctrl k 

 Blog Support 
 More 

 Home 

 Products 

 Guides 

 Release Notes 

 API 

 Reference 

 AI Assistant 

 Good afternoon 
 I'm here to help you with the docs. 

 What is this page about? What should I read next? Can you give an example? 

 ⌘ Ctrl i 

 AI Based on your context 
 Send 

 Learn about Cortex XSIAM 

 Navigate the Cortex XSIAM docs 

 Get started with Cortex XSIAM 

 Agentic AI in Cortex XSIAM 

 Cortex XSIAM product licenses 

 In-product support ticket creation 

 Supported web browsers 

 Use the interface 

 Manage API keys 

 Onboard Cortex XSIAM 

 How to onboard Cortex XSIAM 

 Plan and prepare 

 Deployment steps 

 Post-deployment 

 Configure Cortex XSIAM 

 Learn how to configure Cortex XSIAM 

 Data management 

 Cortex XSIAM Data Sources and Connectors 

 What are Cortex XSIAM data sources and connectors? 

 Complete data source and connector catalog 

 Vendor-specific data sources and connectors 

 Connectors 

 Standard data sources 

 Cloud service provider (CSP) onboarding 

 Understand CSP onboarding tiers and licensing 

 Amazon Web Services cloud onboarding 

 AWS security capabilities and deployment planning 

 AWS resource inventory 

 AWS security model and authentication 

 Cortex XSIAM and AWS audit log collection architecture 

 Onboard Amazon Web Services 

 Prerequisites for onboarding AWS 

 How to onboard Amazon Web Services 

 Deploy the authentication template in AWS 

 Post-deployment: Custom (BYOB) and Control Tower audit log collection 

 Grant cross-account KMS key access for Control Tower BYOB log collection 

 AWS post-deployment verification 

 Microsoft Azure cloud onboarding 

 Google Cloud Platform cloud onboarding 

 Oracle Cloud Infrastructure cloud onboarding 

 Alibaba Cloud cloud onboarding 

 Outpost onboarding 

 Introduction to Terraform for Cloud service provider (CSP) onboarding 

 Manually connect a cloud instance 

 Manage cloud instances 

 Pending cloud instances 

 Edit your onboarded CSP configuration 

 Update cloud permissions after Cortex release updates 

 Troubleshoot errors on cloud instances 

 Cloud service provider permissions 

 Generic on-premise data collectors 

 Palo Alto Networks integrations 

 Cloud Posture and Runtime Security data sources 

 External alerts using External Issue Mapping 

 Administration and troubleshooting 

 Marketplace 

 Configure the Cortex Agentic Assistant 

 Cortex MCP server 

 Automations 

 Engines 

 Remote repository management 

 Customize cases and issues 

 XQL query management 

 Multi-Tenant 

 Managed Services configuration in Cortex 

 Protect your endpoints 

 Endpoint security 

 Endpoint DLP 

 Detect, Investigate, and respond to threats 

 Monitor dashboards and reports 

 Investigation and response 

 Agentic Assistant chat 

 Asset management 

 Threat management 

 Attack surface management 

 Vulnerability management 

 Exposure management 

 Cortex Advanced Email Security 

 Identity Threat Detection and Response (ITDR) 

 Cloud Security 

 Monitor and track compliance adherence 

 Cloud security rules and policies 

 Cortex Cloud Data Classification 

 Cortex Data Security 

 Cloud Identity Security 

 Network exposure detection 

 Cortex Cloud SaaS Security 

 Cortex Cloud AI Security 

 Serverless function posture security 

 Cortex Cloud Application Security 

 Cloud workload policies and rules 

 Base image rules 

 Web and API Security (WAAS) 

 Serverless function runtime security 

 Reference and developer docs 

 Cortex XSIAM XQL 

 Graph Search 

 Cortex CLI 

 Role-Based Access Control 

 API documentation 

 Reference 

 Migrating to a new Broker VM image 

 Learn more about migrating to the latest broker VM image 

 Standalone Broker VM 

 Broker VM high availability cluster node 

 On this page 

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

 Previous Grant cross-account KMS key access for Control Tower BYOB log collection Next Microsoft Azure cloud onboarding 

 Last updated 20 days ago 

 Was this helpful? 

 ‍ 

 Trust Center 

 ‍ 

 Privacy 

 ‍ 

 Terms of Use 

 ‍ 

 Legal 

 © 2026 Palo Alto Networks, Inc. All rights reserved. 

 Was this helpful?

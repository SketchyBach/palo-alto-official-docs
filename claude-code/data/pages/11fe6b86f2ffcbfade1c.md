---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsiam/configure-cortex-xsiam/cortex-xsiam-data-sources/cloud-service-provider-csp-onboarding/pending-cloud-instances
fetched_at: 2026-08-13T15:00:44Z
source: cortex-platform
---

# Pending cloud instances | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

Pending cloud instances | Cortex Documentation Portal 

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

 Pending cloud instances 

 In Cortex Cloud, a pending cloud instance refers to a cloud instance created after Cortex Cloud generates an authentication template, but before that template has been fully executed within the Cloud Service Provider (CSP) environment. 

 A pending cloud instance is created each time you complete the onboarding wizard for a new CSP and click Save . You can view all cloud instances, including those in a pending state, by navigating to Cloud Instances . Ensure you remove any default filters that might exclude instances with a "pending" status. 

 A single pending instance can be leveraged to create multiple cloud instances, all sharing the same configurations defined during the cloud onboarding process. Pending instances are automatically deleted after 30 days. 

 Manage pending cloud instances 

 There are some actions that can be performed specifically on cloud instances with a status of "pending". 

 Action 

 Instructions 

 Manually connect an instance 

 After the authentication template has been executed in the CSP, you can manually connect the Cortex Cloud cloud instance to the CSP by right-clicking the pending cloud instance and selecting Manually connect an instance . For more about this process, see Manually connect a cloud instance . 

 View Details 

 To review the configuration settings defined in the onboarding wizard for a pending instance, right-click the instance and select View Details . This is helps you distinguish between pending instances when you want to create a new cloud instance from an existing pending instance or when you want to manually connect an instance. 

 Re-download Connection Template 

 The authentication template that you download from the onboarding wizard is valid for seven days from when it was downloaded. If you want to create a new cloud instance from a pending instance after the authentication template has expired, you can right-click the pending instance and select Re-download Connection Template . You must then execute the template in the CSP. 

 Delete 

 To delete a pending instance, right-click the pending instance and select Delete . 

 Previous Manage cloud instances Next Edit your onboarded CSP configuration 

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

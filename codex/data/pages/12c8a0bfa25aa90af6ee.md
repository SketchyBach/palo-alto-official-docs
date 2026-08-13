---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsiam/configure-cortex-xsiam/cortex-xsiam-data-sources/cloud-posture-and-runtime-security-data-sources/how-to-onboard-on-premise-assets-to-cloud-data-security
fetched_at: 2026-08-13T15:03:29Z
source: cortex-platform
---

# How to onboard on-premise assets to Cloud Data Security | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

How to onboard on-premise assets to Cloud Data Security | Cortex Documentation Portal 

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

 Generic on-premise data collectors 

 Palo Alto Networks integrations 

 Cloud Posture and Runtime Security data sources 

 How to onboard on-premise assets to Cloud Data Security 

 Activate DSPM Fileshare 

 How to onboard Databricks 

 How to onboard Microsoft 365 

 Ingest logs and data from Okta 

 How to onboard Snowflake 

 Activate AppSec Transporter 

 Container Registries 

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

 Cloud Posture and Runtime Security data sources 

 How to onboard on-premise assets to Cloud Data Security 

 How to onboard on-premise assets to Cortex Cloud Data Security 

 Notice 

 The data sources are included in Cloud Posture Security, Cloud Runtime Security, or Cortex XSIAM Premium license. 

 The following applets enable you to monitor and secure assets residing in your on-premise environment: 

 File share protection with the DSPM Fileshare applet : By activating the DSPM Fileshare applet, you extend security coverage to your physical infrastructure, enabling classification for SMB and NFS file shares. This allows you to automatically discover stored content, identify sensitive data, and locate shadow backups, ensuring continuous visibility and consistent governance across hybrid and legacy environments. 

 Database visibility with the DSPM Database applet : The DSPM Database applet provides insights into risks associated with data stored in on-premise databases, PostgreSQL and MySQL instances. Whether you are transitioning to the cloud or maintaining assets on-premise, activating this applet offers a customizable way to manage data security and compliance within a single, unified platform. 

 To extend the capabilities of Cortex Cloud Data Security to your on-premise infrastructure, you use the Broker VM and a specialized application called an applet. The Broker VM is a virtual machine deployed within your local network that acts as a secure, local collector and gateway. It is essential for unifying and packaging data from your on-premise resources before sending them to Cloud Data Security. 

 For information about working with Broker VM, see What is the Broker VM? . 

 Note 

 Your data is scanned on the Broker VM itself, and only the metadata and classification results are transmitted from the on-premise environment to Cortex XSIAM. 

 DSPM Fileshare applet 

 The DSPM Fileshare applet is an application installed directly onto the Broker VM. The applet’s primary role is to establish and manage connections with your on-premise network file shares, including those using the SMB (Server Message Block) and NFS (Network File Sharing) protocols. 

 Once configured, this applet continuously: 

 Accesses the designated file share paths. 

 Ingests the file and folder metadata. 

 Classifies files and identifies sensitive information. 

 Transmits the collected metadata and results securely through the Broker VM to Cortex XSIAM. 

 Note 

 For information about activating the DSPM Fileshare applet, see Activate DSPM Fileshare . 

 DSPM Database applet 

 The DSPM Database applet is an application installed directly onto the Broker VM. It is the core component responsible for auditing and securing your on-premises PostgreSQL and MySQL databases, providing visibility into the risks associated with your stored data. 

 Once configured, this applet continuously: 

 Accesses your on-premise databases, including those containing regulated or confidential information. 

 Identifies data that must be stored in accordance with specific compliance standards. 

 Classifies database content to identify sensitive information. 

 Transmits the collected insights and risk metadata securely through the Broker VM to Cortex Cloud Data Security. 

 Note 

 For information about activating the DSPM Database applet, see Activate DSPM Database. 

 Previous Cloud Posture and Runtime Security data sources Next Activate DSPM Fileshare 

 Last updated 17 days ago 

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

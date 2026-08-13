---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsiam/configure-cortex-xsiam/cortex-xsiam-data-sources/cloud-posture-and-runtime-security-data-sources/ingest-logs-and-data-from-okta
fetched_at: 2026-08-13T15:03:42Z
source: cortex-platform
---

# Ingest logs and data from Okta | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

Ingest logs and data from Okta | Cortex Documentation Portal 

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

 Ingest logs and data from Okta 

 Configure Okta log and configuration data ingestion. 

 Product availability and licensing 

 The options available in the UI depend on your specific product license: 

 Collect logs: Available for all Cortex XSIAM licenses 

 Collect Configuration. Available for Cortex XSIAM, Cloud Posture Security, or Cloud Runtime Security licenses. 

 Feature 

 Cortex XSIAM NG SIEM, Cortex XSIAM Enterprise, and Cortex XSIAM Premium 

 Cortex XSIAM Enterprise Plus 

 Collect Logs 

 Enabled 

 Enabled 

 Collect Configuration 

 Enabled with Cloud Posture Security or Cloud Runtime Security add-on 

 Disabled 

 Prerequisite 

 Administrator privileges : Your Okta user must have a role capable of creating API tokens, such as Read-only Administrator, Super Administrator, or Organization Administrator. For more information, see the Okta Administrators Documentation . 

 To receive logs and configuration data from Okta, configure the Data Sources & Integrations settings in Cortex XSIAM. Once enabled, the system immediately begins ingesting activity logs and identity configuration metadata, according to your configuration settings. 

 Activity logs are searchable in the okta_sso_raw dataset and normalized to xdr_data or saas_audit_logs . 

 When enabled with a Cloud Posture Security or Cloud Runtime Security add-on, activity logs are also searchable using advanced Identity Security queries using Cortex Query Language (XQL). For more information, see Perform advanced Identity Security investigations using XQL . 

 Activity logs are also searchable using advanced Identity Security queries using Cortex Query Language (XQL). For more information, see Perform advanced Identity Security investigations using XQL . 

 Configuration data is used for Identity Security visibility and is searchable in Identity Security → Identity Asset Inventory and using the ciem_permissions_with_last_access dataset. 

 API rate limits and monitoring 

 The Okta API enforces concurrent rate limits. To prevent service disruption: 

 The Okta data collector includes a mechanism that automatically reduces the number of requests whenever an error is received from the Okta API indicating that too many requests have already been sent. 

 To ensure you are notified when this occurs, an alert is displayed in the Notification Area, and a record is added to the Management Audit Logs. 

 How to configure the Okta collection? 

 Step 1: Configure Okta for integration 

 Perform these steps in your Okta Admin Console to prepare for the connection. 

 Identify your Okta Domain: 

 From the Okta Dashboard, click the down arrow under your name in the top-right corner. 

 Copy the Org URL, such as https://example.okta.com , and save it for the Okta Domain field in Cortex XSIAM. 

 For more information, see the Okta Documentation . 

 Obtain your authentication token in Okta: 

 Select Security → API → Tokens, and click Create token. 

 Set the following parameters for the token: 

 What do you want your token to be named?: Specify the name for your token, which is used for tracking API calls. 

 API calls made with this token must originate from: Select Any IP. 

 Click Create token. You may need to log inlogin to Okta again using your MFA administrator credentials. 

 Your token is successfully created. Copy the Token Value and record it immediately. You will need this for the TOKEN field in Cortex XSIAM. Once you close the dialog box by clicking Ok, got it, you won't be able to access the token again and will have to create a new one if you didn't record it. 

 Step 2: Configure the Okta Collector in Cortex XSIAM 

 Select Settings → Data Sources & Integrations. 

 On the Data Sources & Integrations page, click + Add New, search for Okta, then hover over it and click Add. 

 Integrate the Okta authentication service with Cortex XSIAM: 

 Enter the Okta Domain (Org URL) and Token obtained in Step 1. 

 Collect Logs: Select this option to ingest activity logs. 

 (Optional) Define an Event Filter to configure collection for events of your choosing. 

 All events are collected by default unless you define an Okta API Filter expression, such as filter=eventType eq “user.session.start” . 

 For Okta information to be woven into authentication stories, “user.authentication.sso” events must be collected. 

 Collect Configuration: Select this option to provide deep visibility into identities and permissions, offering comprehensive insights into users, user groups, and applications. It specifically highlights the permissions granted to Okta users in cloud environments, centralizing group memberships to secure your identity landscape. 

 Test the connection. 

 Click Enable. 

 Step 3. Accessing the data 

 Data is routed differently depending on which collection option is enabled: 

 Activity Data (using Collect Logs) 

 XQL : Searchable using the okta_sso_raw dataset. 

 Normalization : Depending on the event type, data is normalized to either xdr_data or saas_audit_logs datasets. 

 Enabled with a Cloud Posture Security or Cloud Runtime Security add-on : Searchable using advanced Identity Security queries using Cortex Query Language (XQL). For more information, see Perform advanced Identity Security investigations using XQL. 

 Configuration data (using Collect Configuration) 

 Identity inventory : Access the data in the Identity Asset Inventory within the Cortex Cloud Identity Security module (Identity Security → Identity Asset Inventory). 

 XQL : Use the following dataset for CIEM (Cloud Infrastructure Entitlements Management) visibility: ciem_permissions_with_last_access 

 Previous How to onboard Microsoft 365 Next How to onboard Snowflake 

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

 Product availability and licensing 

 API rate limits and monitoring 

 How to configure the Okta collection? 

 Was this helpful?

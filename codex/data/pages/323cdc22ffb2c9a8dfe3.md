---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsiam/configure-cortex-xsiam/cortex-xsiam-data-sources/cloud-posture-and-runtime-security-data-sources/how-to-onboard-snowflake
fetched_at: 2026-08-13T15:03:46Z
source: cortex-platform
---

# How to onboard Snowflake | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

How to onboard Snowflake | Cortex Documentation Portal 

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

 How to onboard Snowflake 

 Add Snowflake as a Cortex Cloud Data Security data source. 

 How to onboard Snowflake 

 Notice 

 This feature is included with a Cortex XSIAM Premium license. It is also included with any other Cortex XSIAM license that has the Cloud Posture Security or Cloud Runtime Security add-on. 

 Integrate Cloud Data Security with your Snowflake account to gain comprehensive visibility into any data and posture risk existing in your Snowflake environment. This integration enables automated scanning of all assets in Snowflake, including data classification and risk assessment. 

 You can add Snowflake as a third-party data source in Cloud Data Security. 

 Prerequisite 

 To use Snowflake, you must be registered with one of these cloud providers: Amazon AWS, Microsoft Azure, or Google Cloud Platform (GCP). 

 Ensure you have the necessary account permissions to onboard. It is recommended to use Account Admin as the role for the onboarding. 

 Configuration Step 

 Navigate to Settings → Data Sources & Integrations . 

 On the Data Sources & Integrations page, click + Add New . 

 On the Add Data Sources or Integrations page, search for Snowflake , then hover over it and click Add . 

 On the New Data Source Snowflake integration instance settings page, do the following: 

 Enter a display name for your Snowflake integration instance. 

 Enter a Data Sharing Account Identifier. 

 Note 

 The account identifier can be found using the user information at the bottom left. Hover over the account you wish to onboard and select the copy option at the top right. The account identifier is usually of the format: 

 (organization).[account] 

 (Optional) If you have a Snowflake account that is protected by a network policy, turn on the My Snowflake account is protected by network policies toggle button. The network policies are related to the IP allow list. 

 Select a cloud platform and choose a region. 

 (Optional) If you want to use an existing user: 

 Click Show advance settings and then turn on the Use an existing user toggle button. 

 Enter the user name and the login name. 

 Click Next . 

 Establish Connection Step 

 Open your Snowflake console in a new tab. 

 Using the copy or download icons, copy or download the script in the Generated script text box and paste it into a new worksheet in Snowflake. 

 Select the entire script and select Run all . 

 Once the script runs without errors, come back to the Snowflake screen and click Verify Connection to check if the instance is detected. 

 Verify Connection Step 

 A success or failure message appears on the screen. 

 If a success message appears, you can do the following: 

 View the instance's information in the Snowflake Posture instances. 

 View the assets in Asset Inventory, once the first scan is complete. 

 Delete a Snowflake instance 

 Navigate to Settings → Data Sources & Integrations . 

 On the Data Sources & Integrations page, select the Snowflake integration or filter to search for it and then select it. 

 On the Snowflake page, right click the row of the integration instance you want to delete. 

 From the drop down menu, select Settings and from the integration instance settings page select the Delete checkbox and then click Delete . 

 The Snowflake instance is now removed, including all previous scans. 

 Previous Ingest logs and data from Okta Next Activate AppSec Transporter 

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

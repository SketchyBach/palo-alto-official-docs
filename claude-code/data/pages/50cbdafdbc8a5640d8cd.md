---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsiam/configure-cortex-xsiam/cortex-xsiam-data-sources/administration-and-troubleshooting/about-health-issues/investigate-and-resolve-health-issues
fetched_at: 2026-08-13T15:05:32Z
source: cortex-platform
---

# Investigate and resolve health issues | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

Investigate and resolve health issues | Cortex Documentation Portal 

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

 External alerts using External Issue Mapping 

 Administration and troubleshooting 

 Manage instances 

 Integrations 

 Verify collector connectivity 

 Overview of data ingestion metrics 

 About health issues 

 Investigate and resolve health issues 

 Monitor data ingestion health (BETA) 

 Monitor Correlation rules 

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

 Administration and troubleshooting 

 About health issues 

 Investigate and resolve health issues 

 The following tasks explain how to investigate and resolve health issues. You can see health issues on the following pages: 

 Go to Settings → Health Issues 

 Go to Cases & Issues → Issues and change the table view to Health Domain. 

 Investigate data ingestion errors 

 A data ingestion issue identifies disruption in the data ingestion pipeline. For example, a data source is not sending logs, or there is a significant drop in log collection compared to the calculated ingestion baseline. 

 Identify the error: Type = Ingestion. 

 Right-click and select Investigate in XQL query. 

 The Query Builder opens and runs a prefilled query to display related data ingestion metrics entries. 

 Review the query results. 

 The results provide context for the issue and the events leading up to it. For more information about data ingestion metrics and setting up correlation rules with your own data ingestion logic, see Monitor data ingestion health . 

 Investigate data collector errors. Return to the Health Issues page, right-click the issue, and select Pivot to views → View collector details. 

 Depending on the type of collector in error, the relevant data collector settings page opens, filtered by data collector. 

 Investigate collection errors 

 A collection issue identifies connectivity disruption in your collection integrations, custom collectors, and Marketplace integrations. 

 Identify the error: Type = Collection. 

 See the current status of the collector. 

 Right-click and select Pivot to views → View collector details. Depending on the type of collector in error, the relevant data collector settings page opens, filtered by data collector. 

 If the data collector is still in error, you can update the collector settings as required. 

 Investigate the collector error status. 

 Run a query on the collection_auditing dataset to see all the connectivity changes of the collector over time, the escalation or recovery of the connectivity status, and the error, warning, and informational messages related to status changes. 

 This example searches for status changes for the "instance1" data collector integration: 

 Ask Copy 

 dataset = collection_auditing 
 |filter collector_type = "STRATA_IOT" and instance = "instance1" 

 For more information about troubleshooting collector errors and setting up correlation rules to trigger additional collection issues, see Verify collector connectivity . 

 Investigate correlation errors 

 A correlation issue identifies errors in your correlation rules. 

 Identify the error: Type = Correlation. 

 Right-click and select Investigate Correlation Auditing. 

 The Query Builder opens and runs a prefilled query to display related correlation execution records. 

 Review the query results. 

 Identify the correlation rule in error and take steps to resolve the error. For more information about how Cortex XSIAM identifies correlation rule errors, see Monitor correlation rules . 

 Investigate automation errors 

 Automation issues identify potential misconfigurations in automations, enabling you to take a proactive approach to fixing misconfiguration issues before they affect system performance. 

 Identify the error: Type = Automation. 

 Click the automation health issue to view the details of the related case or component. 

 Based on the details of the automation health issue, review any related automations, such as playbooks and integrations, for possible misconfigurations. 

 Previous About health issues Next Monitor data ingestion health (BETA) 

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

 Investigate data ingestion errors 

 Investigate collection errors 

 Investigate correlation errors 

 Investigate automation errors 

 Was this helpful?

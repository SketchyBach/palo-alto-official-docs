---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsiam/configure-cortex-xsiam/data-management/dataset-management/monitor-datasets-and-dataset-views-activity
fetched_at: 2026-08-13T14:15:18Z
source: cortex-platform
---

# Monitor datasets and dataset views activity | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

Monitor datasets and dataset views activity | Cortex Documentation Portal 

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

 Optimize data management in Cortex XSIAM 

 Configure Cortex Data Lake tier 

 Broker VM 

 Dataset management 

 What are datasets? 

 Lookup datasets 

 Import a lookup dataset 

 Download JSON file of lookup dataset 

 Set time to live for lookup datasets 

 Monitor datasets and dataset views activity 

 Archived data 

 Parsing Rules 

 Data Model Rules 

 Manage Event Forwarding 

 Manage compute units 

 Cortex XSIAM Data Sources and Connectors 

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

 Data management 

 Dataset management 

 Monitor datasets and dataset views activity 

 Prerequisite 

 Dataset Management requires View/Edit RBAC permissions for Data Management (under Configurations → Data Management ), which are the same permissions required for Parsing Rules, Data Model Rules, and Event Forwarding. 

 Cortex XSIAM logs entries for events related to datasets and dataset views monitored activities. Cortex XSIAM stores the logs for 365 days. To view the datasets and dataset views audit logs, select Settings → Management Audit Logs . 

 You can customize your view of the logs by adding or removing filters to the Management Audit Logs table. You can also filter the page result to narrow down your search. The following table describes the default and optional fields that you can view in the Cortex XSIAM Management Audit Logs table: 

 Note 

 Certain fields are exposed and hidden by default. An asterisk (*) is beside every field that is exposed by default. 

 Field 

 Description 

 Description* 

 Log message that describes the action. 

 Email 

 Email of the user who performed the action. 

 Host Name* 

 This field is not applicable for datasets and dataset views logs. 

 ID 

 Unique ID of the action. 

 Reason 

 This field is not applicable for datasets and dataset views logs. 

 Result* 

 The result of the action ( Success , Fail , or N/A ) 

 Severity* 

 Severity associated with the log: Critical , High , Medium , Low , or Informational . 

 Timestamp* 

 Date and time when the action occurred. 

 Type* and Sub-Type* 

 Additional classifications of dataset and dataset view logs. Datasets: Create Dataset, Delete Dataset, and Update Dataset. Dataset Views: Create Dataset View, Delete Dataset View, and Update Dataset View. 

 User Name* 

 Name of the user who performed the action. 

 Previous Set time to live for lookup datasets Next Archived data 

 Last updated 22 days ago 

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

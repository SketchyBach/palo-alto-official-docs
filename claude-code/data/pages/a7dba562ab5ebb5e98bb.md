---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsiam/configure-cortex-xsiam/data-management/parsing-rules/create-parsing-rules
fetched_at: 2026-08-13T14:15:59Z
source: cortex-platform
---

# Create Parsing Rules | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

Create Parsing Rules | Cortex Documentation Portal 

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

 Archived data 

 Parsing Rules 

 Parsing Rules editor views 

 Parsing Rules file structure and syntax 

 Create Parsing Rules 

 Troubleshooting Parsing rules errors 

 Parsing Rules Raw Dataset 

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

 Parsing Rules 

 Create Parsing Rules 

 Prerequisite 

 Parsing Rules requires View/Edit RBAC permissions for Data Management (under Configurations → Data Management ), which are the same permissions required for Dataset Management, Data Model Rules, and Event Forwarding. 

 Cortex XSIAM provides a number of default Parsing Rules that you can easily override or extend as required using XQL and additional custom syntax that is specific to creating Parsing Rules. Before creating your own Parsing Rules, we recommend you review the following: 

 Parsing Rules editor views 

 Parsing Rules file structure and syntax 

 Important 

 When creating Parsing Rules, the _time field is a mandatory field. If the field is null or invalid, the _insert_time field is used instead. This field can be automatically parsed depending on the type of data being ingested. For example, for CEF or LEEF logs, the parser first tries to ingest timestamps from these fields in the following order: rt , start , end , and _insert_time . 

 How to create Parsing Rules 

 In Cortex XSIAM , select Settings → Configurations → Data Management → Parsing Rules . 

 Select the Parsing Rules editor view for writing your Parsing Rules. 

 You can select one of the following views. 

 User Defined : Leave the default view open and write your Parsing Rules directly in the editor. 

 Default Rules : Select this view to understand which parsing rules are provided by default with Cortex XSIAM in read-only mode. 

 Both : Select this view to see the Parsing Rules editor as well as the default rules as you write your Parsing Rules. 

 Simulate : Select this view to test your Parsing Rules on actual logs and validate their outputs as you write your Parsing Rules. 

 Write your Parsing Rules using XQL syntax and the syntax specific for Parsing Rules. 

 (Optional) Test your Parsing Rules on actual logs and validate their outputs using the Simulate view. 

 Note 

 You need Cortex XSIAM administrator or Instance Administrator permissions to access the Simulate view and perform these tests. 

 Select the Simulate view. 

 For the User defined rules that you want to test, select the logs from the XQL Samples listed that you want to use to simulate the rule. For each Vendor and Product , up to 5 different samples are available to choose from. 

 Simulate the rules based on the logs selected. 

 You can also pivot (right-click) any of the logs that you’ve selected to Simulate the rules. 

 Review the results in the Logs output table to determine if your User defined rules are fine or need further changes. 

 The Logs output table displays the following columns per dataset at the bottom of the window. 

 Dataset : Displays the applicable dataset name and a line number associated with this dataset in the User defined rules section. 

 Vendor : The vendor associated with this dataset. 

 Product : The product associated with this dataset. 

 Output Logs : Displays the available output log. When there is no output log to display, the text Output logs is not available with the corresponding error message is displayed. When there is no output due to a missing rule in the User defined rules section for the logs selected, the text No output logs. You can change your parsing rules and try again is displayed. 

 Input Logs : Displays the relevant input log with a right-click pivot to Show diff between the Output Logs and Input Logs . 

 (Optional) Modify your User defined rules and repeat steps #2-4 until you are satisfied with the results. 

 (Optional) Override the default Parsing Rules raw dataset . 

 Save your changes. 

 Previous EXTEND Next Troubleshooting Parsing rules errors 

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

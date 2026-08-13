---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsiam/protect-your-endpoints/endpoint-security/install-and-manage-endpoints/define-endpoint-groups
fetched_at: 2026-08-13T15:12:58Z
source: cortex-platform
---

# Define endpoint groups | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

Define endpoint groups | Cortex Documentation Portal 

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

 Endpoint protection 

 Install and manage endpoints 

 Set up endpoint protection 

 Define endpoint groups 

 Configure global agent settings 

 Apply profiles to endpoints 

 Create an agent installation package 

 Harden endpoint security 

 Manage endpoint protection 

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

 Protect your endpoints 

 Endpoint security 

 Install and manage endpoints 

 Define endpoint groups 

 You can define an endpoint group and then apply policy rules and manage specific endpoints. If you set up Cloud Identity Engine, you can also leverage your Active Directory user, group, and computer details to define endpoint groups. 

 Do one of the following: 

 Create a dynamic group by enabling Cortex XSIAM to populate your endpoint group dynamically using endpoint characteristics, such as an endpoint tag, partial hostname or alias, full or partial domain or workgroup name, IP address, range or subnets, installation type (VDI, temporary session or standard endpoint), agent version, endpoint type (workstation, server, mobile), user or operating system version. 

 Create a static group by selecting a list of specific endpoints. 

 Note 

 Configuration based on user granular policy is optimized for VDI and session-persistent environments; it is not recommended for decentralized or traditional endpoint architectures. 

 After you define an endpoint group, you can then use it to target policy and actions to specific recipients. The Endpoint Groups page displays all endpoint groups along with the number of endpoints and policy rules linked to the endpoint group. 

 How to define an endpoint group 

 Select Inventory → Endpoints → Groups → +Add Group . 

 Select one of the following: 

 Create New to create an endpoint group from scratch 

 Upload From File using plain text files with a new line separator, to populate a static endpoint group from a file containing IP addresses, hostnames, or aliases. 

 Enter a Group Name and optional description to identify the endpoint group. The name you assign to the group will be visible when you assign endpoint security profiles to endpoints. 

 Determine the endpoint properties for creating an endpoint group: 

 Dynamic: Use the filters to define the criteria you want to use to dynamically populate an endpoint group. Dynamic groups support multiple criteria selections and can use AND or OR operators. For endpoint names and aliases, and domains and workgroups, you can use * to match any string of characters. As you apply filters, Cortex XSIAM displays any registered endpoint matches to help you validate your filter criteria. 

 Static: Select specific registered endpoints that you want to include in the endpoint group. Use the filters, as needed, to reduce the number of results. 

 When you create a static endpoint group from a file, the IP address, hostname, or alias of the endpoint must match an existing agent that has registered with Cortex XSIAM. You can select up to 250 endpoints. 

 Note 

 Disconnecting Cloud Identity Engine in your Cortex XSIAM deployment can affect existing endpoint groups and policy rules based on Active Directory properties. 

 Create the endpoint group. 

 After you save your endpoint group, it is ready for use to assign security profiles to endpoints and in other places where you can use endpoint groups. 

 At any time, you can return to the Groups page to view and manage your endpoint groups. To manage a group, right-click the group and select the desired action: 

 Edit: View the endpoints that match the group definition, and optionally refine the membership criteria using filters. 

 Delete: Remove the endpoint group. 

 Save as new: Duplicate the endpoint group and save it as a new group. 

 Export group: Export the list of endpoints that match the endpoint group criteria to a tab separated values (TSV) file. 

 View endpoints: Pivot from an endpoint group to a filtered list of endpoints on the All Endpoints page where you can quickly view and initiate actions on the endpoints within the group. 

 Previous Set up Identity profiles Next Configure global agent settings 

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

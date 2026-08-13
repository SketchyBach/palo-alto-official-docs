---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsiam/configure-cortex-xsiam/multi-tenant/dynamic-license-allocation
fetched_at: 2026-08-13T15:11:24Z
source: cortex-platform
---

# Dynamic license allocation | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

Dynamic license allocation | Cortex Documentation Portal 

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

 What is Cortex XSIAM multi-tenant? 

 Multi-tenant central licensing management 

 Onboard Cortex multi-tenant 

 Dynamic license allocation 

 Child tenant management 

 About managed threat hunting 

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

 Multi-Tenant 

 Dynamic license allocation 

 In a multi-tenant central licensing management environment, you can dynamically edit child tenant allocations, add child tenants, and delete child tenants with the license pool automatically updated. 

 In a multi-tenant environment with central licensing management, in Cortex Gateway you can edit child tenant allocations, add child tenants, and delete child tenants. When you delete a child tenant, the tenant's allocations of endpoints, employees, and GBs are returned to the main account's pool and can immediately be used for existing child tenants or for creating new child tenants. 

 Edit tenant allocations 

 You can edit the child tenant allocations by increasing or decreasing the amount of endpoints, employees, and GBs allocated to the tenant. The total available count for the multi-tenant environment is updated accordingly. 

 Note 

 Changing the tenant's allocations might result in a short downtime of your tenant. 

 In Cortex Gateway, locate the main account and then hover over the child tenant until the three-dot menu appears and click Edit Tenant Allocations . 

 In the Edit Tenant Allocations window, assign the number of Gigabytes and endpoints you want to allocate to this child tenant. The amount used and the total amount available to this multi-tenant environment are displayed. Ensure you meet the minimum allocation requirements . Click Done . 

 Add a child tenant 

 When you have enough license allocations available in your multi-tenant central licensing environment, you can add a child tenant to the main account in Cortex Gateway. 

 In the Cortex Gateway, hover over the main account you activated previously until the three-dot menu appears and click Add Child Tenant . 

 Add the following details: 

 Parameter 

 Description 

 Child Tenant Name 

 Give the Cortex XSIAM tenant an easily recognizable name. 

 Choose a name that is 59 or fewer characters and is unique across your company account. 

 Region 

 View the region for the child tenant. 

 Child Tenant Subdomain 

 Give your Cortex XSIAM instance an easy-to-recognize name that is used to access the tenant directly using the full URL. 

 https://<subdomain>.crtx.<region>.paloaltonetworks.com 

 Note 

 This is a public FQDN, so be careful with sensitive information such as the company name. 

 After activating a child tenant, you can only change the child tenant subdomain once. 

 Child Units Allocation 

 Assign the number of employees and Gigabytes you want to allocate to this child tenant. The amount used and the total amount available to this multi-tenant environment are displayed. 

 Note 

 Ensure that you meet the minimum requirements for child tenant allocation. 

 Add Ons 

 If any license add-ons were purchased with your multi-tenant license, they are listed here. If you acquired compute units (CU) or forensics, you can allocate how many units to allocate to this child tenant. 

 Confirm approval of the terms and conditions of the privacy policy and click Activate . 

 Activation can take up to an hour. You should receive notification by email that the child tenant has completed the activation process. 

 (Optional) Add another child tenant by repeating steps 1 and 2 or access your newly created tenant. 

 In the Cortex Gateway, under your main account, you can see the total number of tenants you are licensed for and how many you have created. 

 Note 

 If you reach your limit for child tenants, depending on your license, you may be able to create more tenants. You may be charged for additional tenants. Contact Customer Support if you are approaching your authorized limit. 

 Delete a child tenant 

 Deleting a child tenant deletes all of its data and content permanently. The child tenant's license allocations are returned to the total available in the multi-tenant environment and can be allocated to other child tenants. 

 Note 

 In a multi-tenant central licensing management environment, you cannot unpair a child tenant from the main account. The only way to remove the connection to the main account is to delete the tenant. 

 In Cortex Gateway, locate the main account and then hover over the child tenant until the three-dot menu appears and click Delete Tenant . 

 In the Delete Tenant window, confirm that you want to delete the child tenant by typing 'Delete' and click Confirm Deletion . 

 Previous Step 3. Pair a parent tenant with a child tenant Next Child tenant management 

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

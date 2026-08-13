---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsiam/onboard-cortex-xsiam/deployment-steps/activate-cortex-xsiam
fetched_at: 2026-08-13T14:11:27Z
source: cortex-platform
---

# Activate Cortex XSIAM | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

Activate Cortex XSIAM | Cortex Documentation Portal 

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

 Cortex XSIAM onboarding checklist 

 Activate Cortex XSIAM 

 Bring your own keys 

 Cortex XSIAM supported regions 

 Enable access to required PANW resources 

 Set up users, groups, and roles 

 Set up authentication 

 Configure content 

 Set up Cloud Identity Engine 

 Install Cortex XDR agents 

 Cortex XSIAM - Analytics 

 FedRAMP overview 

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

 Onboard Cortex XSIAM 

 Deployment steps 

 Activate Cortex XSIAM 

 Learn how to activate your tenant. 

 To activate a tenant, you need to log in to Cortex Gateway, a centralized portal for activating and managing tenants, users, roles, and user groups. After activating the tenant, you can then access the tenant. You must repeat this task for each tenant if you have multiple tenants. The activation process involves accessing Cortex Gateway, activating the tenant, and then accessing the tenant's resources. 

 Prerequisite 

 The Cortex XSIAM activation email. 

 A Customer Support Portal (CSP) account. 

 You need to set up your CSP account. For more information, see How to Create Your CSP User Account . 

 When you create a CSP account, you can set up two-factor authentication (2FA) to log into the CSP by using an Email, Okta Verify, or Google Authenticator (non-FedRAMP accounts). For more information, see How to Enable a Third Party IdP . 

 You have one of the following roles assigned: 

 Role 

 Description 

 CSP role 

 The Super User role is assigned to your CSP account. The user who creates the CSP account is granted the Super User role. 

 Cortex role 

 You must have the Account Admin role. 

 If you are the first user to access Cortex Gateway with the CSP Super User role, you are automatically granted Account Admin permissions for the Cortex Gateway. You can also add Account Admin users as required. 

 In the Cortex Gateway, you can activate new tenants, access existing tenants, and create and manage role-based access control (RBAC) for all of your tenants. 

 How to activate Cortex XSIAM 

 Log in to Cortex Gateway. 

 You can also access the link from the activation email. 

 Enter your username and password or multi-factor authentication (if set up) by using your Customer Support Portal account credentials to sign in. 

 After you sign in, you can view the following: 

 If you are a CSP Account Admin, you can see tenants allocated to your CSP account and ready for activation. After activation, you cannot move your tenant to a different CSP account. 

 Tenant details such as license type, number of endpoints, and purchase date. 

 Tenants that were activated and are now available. If you have more than one Customer Support Portal account, the tenants are displayed according to the Customer Support Portal account name. 

 In the Available for Activation section, use the serial number to locate the tenant that needs activation, and then click Activate . 

 Note 

 When you activate, a production tenant is first activated. After activation, you can set up a development tenant (subject to your license). 

 On the Tenant Activation page, define the following: 

 Parameter 

 Description 

 Tenant Name 

 Enter the name of the tenant. Use a unique name across your company account up to 59 characters long. 

 Region 

 Geographic location where your tenant will be hosted. For more information about supported regions, see Cortex XSIAM supported regions . 

 Tenant Subdomain 

 DNS record associated with your tenant. Enter a name that will be used to access the tenant directly using the full URL: 

 https://<subdomain>xdr.<region>.paloaltonetworks.com 

 Encryption Method 

 (Optional) If you want to bring your own keys for encrypting your data, under Advanced , select BYOK and follow the instructions of the wizard as detailed in Encryption Method . 

 Default encryption (recommended) 

 All data stored by Cortex XSIAM is encrypted at rest using a dedicated key management system. Cortex XSIAM provides strict key access controls and auditing, and encrypts user data at rest according to AES-256 encryption standards. We recommend using this default system. 

 BYOK (Bring your own keys) 

 BYOK (Bring Your Own Keys) enables you to generate your own encryption keys and securely import and manage them via Cortex Gateway to retain greater control over your tenant data and encryption. This requires further setup . 

 Review and agree to the terms and conditions of the Privacy policy, Terms of Use, and EULA , and then Activate your tenant. 

 Activation can take about an hour and does not require you to remain on the activation page. Cortex XSIAM sends a notification to your email when the process is complete. 

 After activation, from Cortex Gateway, in the Available Tenants , when hovering over the activated tenant, do the following: 

 Ensure that you can successfully access the tenant by clicking the Cortex XSIAM tenant name (when the tenant is active). 

 In the dialog box, view the tenant status, region, serial number, and license details. 

 If you want to change your tenant's name, the subdomain, or activate a development tenant (subject to license), on the right-hand side, click the ellipsis. 

 You can only change the subdomain once, and it cannot be undone. 

 After deleting the subdomain, you can reuse it after 7 days. 

 Enable and verify access to Cortex XSIAM communication servers, storage buckets, and various resources in your firewall configuration. For more information, see Enable access to required PANW resources . 

 Previous Cortex XSIAM onboarding checklist Next Bring your own keys 

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

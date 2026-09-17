---
url: https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/configuration-scm/manage-configuration-ngfw-and-prisma-access/objects/saas-application-management/microsoft-365
fetched_at: 2026-09-16T11:47:24Z
source: palo-alto-main
---

# Microsoft 365 Clear

Updated on 

 Sun Sep 06 22:14:59 PDT 2026 

 Focus 

 Home 

 Strata Cloud Manager 

 Strata Cloud Manager Getting Started 

 Configuration: Strata Cloud Manager 

 Configuration:
 NGFW and Prisma Access 

 Configuration:
 Objects 

 SaaS Application Management 

 Microsoft 365 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 Deutsch (German) 

 Strata Cloud Manager 

 Microsoft 365 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Strata Cloud Manager Docs 

 Activation & Onboarding 

 Subscription & Tenant Management 

 Getting Started 

 AIOps 

 Release Notes 

 New Features 

 Previous 

 SaaS Application Management 

 Next 

 Google Apps 

 Microsoft 365 

 Prisma Access gives you simple, centralized management
for your SaaS applications, including Microsoft 365 apps. 

 Prisma Access gives you simple, centralized
management for your SaaS applications, including Microsoft 365 apps. 

 Easy M365 Enablement —Use the built-in
settings and guided walkthrough to safely enable M365 in just a
few clicks. 

 M365 for Enterprise Use —See all the controls
available to you to safely enable M365: 

 Microsoft 365 Endpoint Lists 

 Microsoft 365 Tenant Restrictions 

 Easy M365 Enablement 

 Built-in security and decryption rules, as
well as a guided walkthrough, mean you can safely enable M365 in
just a few clicks. 

 Built-in security rules allow M365
apps, and ensure that they connect only to Microsoft endpoints 

 Built-in decryption rules skip decryption for traffic destined
to Microsoft-categorized Optimize endpoints (this is Microsoft’s
recommendation) 

 The guided walkthrough will get you up and running with M365
in two steps. 

 M365 for Enterprise Use 

 Safely enable your Microsoft apps for enterprise
use by: 

 Ensuring that Microsoft
apps connect only to Microsoft endpoints 

 Restricting app access
to enterprise accounts (disallow personal use) 

 To manage Microsoft 365 usage, go to Configuration NGFW and Prisma Access . Select Prisma Access configuration scope,
 go to Objects SaaS App Management and edit Microsoft 365 settings. 

 Microsoft 365 Endpoint Lists 

 Microsoft publishes lists of the IP addresses
and URL endpoints their SaaS applications use, and frequently updates
these lists. 

 Palo Alto Networks hosts these lists for you,
and from within Prisma Access, you can subscribe to the lists that
are relevant to you (including optional and required lists). You
can use the lists you’re subscribe to in policy. As Microsoft refreshes
their endpoint lists, your policy dynamically enforces the latest
version of the list; there’s no need for you to monitor list changes
or make manual policy updates to catch the latest updates. 

 Subscribe to an endpoint list 

 Edit Microsoft 365 settings and go to Endpoint
Lists . 

 Select Customize Subscription and choose the
 endpoint lists you want to subscribe to, based on the services
 you’re using and the list type (IPv4, IPv6, or URL). 

 Add the endpoint list to a security policy rule 

 Your subscribed lists are available for you to use as match
criteria in a security policy rule. 

 Go to Configuration NGFW and Prisma Access Security Services Security Policy and add or edit a rule. 

 Add SaaS Application Endpoint lists as
match criteria for the rule. 

 Microsoft 365 Tenant Restrictions 

 Tenant restrictions give you a way limit app
usage to enterprise accounts (stop users from accessing their personal
Microsoft accounts on the company network). To put tenant restrictions
in place: 

 Specify the Microsoft 365 tenants to which you want
to allow access. 

 Specify the Microsoft 365 domains and tenants
to which you want to allow access. 

 Add the tenant restrictions to a security policy rule. 

 While you can add tenant restrictions to a security policy
rule directly from the Microsoft 365 settings here, any tenant restrictions
you’ve configured can also be easily added to new and existing security
policy rules: 

 Previous 

 SaaS Application Management 

 Next 

 Google Apps

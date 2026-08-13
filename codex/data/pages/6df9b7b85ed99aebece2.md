---
url: https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-admin/app-id/manage-new-app-ids-introduced-in-content-releases/allow-new-app-ids
fetched_at: 2026-08-13T17:04:07Z
source: palo-alto-main
---

# Ensure Critical New App-IDs are Allowed Clear

Ensure Critical New App-IDs are Allowed 

 Home 

 EN

 Location 

 Documentation Home 

 Palo Alto Networks 

 Support 

 Live Community 

 Knowledge Base 

 >

 Strata Copilot

 Ensure Critical New App-IDs are Allowed 

 Updated on 

 Aug 3, 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Next-Generation Firewall Docs 

 Getting Started 

 Administration 

 Networking 

 Quick Start 

 Reference 

 Incidents & Alerts 

 Release Notes 

 Select a Document 

 PAN-OS 12.2 

 PAN-OS 12.1 

 PAN-OS 11.2 

 PAN-OS 11.1 

 PAN-OS 11.0 (EoL) 

 PAN-OS 10.2 

 PAN-OS 10.1 (EoL) 

 PAN-OS 10.0 (EoL) 

 PAN-OS 9.1 (EoL) 

 PAN-OS 9.0 (EoL) 

 PAN-OS 8.1 (EoL) 

 Help 

 Select a Document 

 PAN-OS 12.2 

 PAN-OS 12.1 

 PAN-OS 11.2 

 PAN-OS 11.1 

 PAN-OS 10.2 

 PAN-OS 10.1 

 New Features 

 Updated on 

 Aug 3, 2026 

 Focus 

 Home 

 Next-Generation Firewall 

 App-ID 

 Manage New and Modified App-IDs 

 Ensure Critical New App-IDs are Allowed 

 Download PDF 

 Next-Generation Firewall 

 Ensure Critical New App-IDs are Allowed 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Next-Generation Firewall Docs 

 Getting Started 

 Administration 

 Networking 

 Quick Start 

 Reference 

 Incidents & Alerts 

 Release Notes 

 Select a Document 

 PAN-OS 12.2 

 PAN-OS 12.1 

 PAN-OS 11.2 

 PAN-OS 11.1 

 PAN-OS 11.0 (EoL) 

 PAN-OS 10.2 

 PAN-OS 10.1 (EoL) 

 PAN-OS 10.0 (EoL) 

 PAN-OS 9.1 (EoL) 

 PAN-OS 9.0 (EoL) 

 PAN-OS 8.1 (EoL) 

 Help 

 Select a Document 

 PAN-OS 12.2 

 PAN-OS 12.1 

 PAN-OS 11.2 

 PAN-OS 11.1 

 PAN-OS 10.2 

 PAN-OS 10.1 

 New Features 

 Previous 

 See How New and Modified App-IDs Impact Your Security Policy 

 Next 

 Monitor New App-IDs 

 Ensure Critical New App-IDs are Allowed 

 Create security policy rules that allow critical App-IDs to get the latest threat
 prevention without worrying about how the accompanying new App-IDs impact security policy
 enforcement. 

 Where Can I Use This? What Do I Need? 

 Prisma Access 

 Next-Generation Firewall 

 This is a core Network Security feature for NGFWs and Prisma
 Access; no prerequisites needed. 

 New App-IDs can cause a change in policy enforcement
for traffic that is newly-identified as belonging to a certain application.
To mitigate any impact to security policy enforcement, you can use
the New App-ID characteristic in a security
policy rule so that the rule always enforces the most recently introduced
App-IDs without requiring you to make configuration changes when
new App-IDs are installed. The New App-ID characteristic always
matches to only the new App-IDs in the most recently installed content
releases. When a new content release is installed, the new App-ID
characteristic automatically begins to match only to the new App-IDs
in that content release version. 

 You can choose to enforce
all new App-IDs, or target the security policy rule to enforce certain
types of new App-IDs that might have network-wide or critical impact
(for example, enforce only authentication or software development
applications). Set the security policy rule to Allow to
ensure that even if an App-ID release introduces expanded or more
precise coverage for critical applications, the firewall continues
to allow them. 

 New App-IDs are released monthly, so a policy
rule that allows the latest App-IDs gives you a month’s time (or,
if the firewall is not installing content updates on a schedule,
until the next time you manually install content) to assess how
newly-categorized applications might impact security policy enforcement
and make any necessary adjustments. 

 Select Objects Application Filters and Add a
new application filter. 

 Define the types of new applications for which you want
to ensure constant availability based on subcategory or characteristic.
For example, select the category “auth-service” to ensure that any newly-installed
applications that are known to perform or support authentication
are allowed. 

 Only after narrowing the types of new applications that
you want to allow immediately upon installation, select Apply
to New App-IDs only . 

 Select Policies Security and add or edit a
security policy rule that is configured to allow matching traffic. 

 Select Application and add the
new Application Filter to the policy rule
as match criteria. 

 Click OK and Commit to
save your changes. 

 To continue to adjust your security policy to account
for any changes to enforcement that new App-IDs introduce: 

 Monitor
New App-IDs —Monitor and get reports on new App-ID activity. 

 See
the New and Modified App-IDs in a Content Release —See how
the newly-installed App-IDs impact your existing security policy
rules. 

 Previous 

 See How New and Modified App-IDs Impact Your Security Policy 

 Next 

 Monitor New App-IDs 

 On This Page 

 Activation & Onboarding 

 Strata Cloud Manager 

 Activate a License or Product 

 Cloud Identity Engine 

 Strata Logging Service 

 Device Associations 

 Hub 

 Identity and Access Management 

 Tenant Management 

 Next-Generation Firewalls 

 AIOps for NGFW 

 Cloud Management for NGFWs 

 Cloud NGFW for AWS 

 Cloud NGFW for Azure 

 CN-Series 

 Firewalls 

 PAN-OS 

 PAN-OS SD-WAN 

 Service Provider 

 VM-Series 

 SASE 

 Prisma Access 

 Strata Multitenant Cloud Manager 

 AI-Powered ADEM 

 Prisma Access Monitoring and Visibility 

 Prisma SD-WAN 

 ION Devices 

 Next-Generation CASB 

 Cloud-Delivered Security Services 

 Advanced WildFire 

 Advanced URL Filtering 

 Advanced Threat Prevention 

 Advanced DNS Security 

 Device Security 

 Enterprise DLP 

 SaaS Security 

 Network Security 

 Shared Policy for NGFWs and Prisma Access 

 Visibility & Monitoring 

 Dashboards 

 Incidents and Alerts 

 Reports 

 Autonomous DEM 

 Best Practices 

 Best Practices Library 

 Experts Corner 

 Solutions Docs from Product Experts 

 Network Security 

 PAN-OS 

 Next-Generation Firewall 

 Administration 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

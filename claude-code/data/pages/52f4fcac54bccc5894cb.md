---
url: https://docs.paloaltonetworks.com/enterprise-dlp/administration/configure-enterprise-dlp/email-dlp/onboard-microsoft-exchange-online/obtain-your-microsoft-exchange-domain-and-relay-host
fetched_at: 2026-08-13T15:32:16Z
source: palo-alto-main
---

# Obtain Your Microsoft Exchange Domain and Relay Host Clear

Obtain Your Microsoft Exchange Domain and Relay Host 

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

 Obtain Your Microsoft Exchange Domain and Relay Host 

 Updated on 

 Fri Jul 10 12:56:22 PDT 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Enterprise DLP Docs 

 Activation & Onboarding 

 Getting Started 

 Administration 

 Reference 

 Release Notes 

 New Features by OS Version 

 New Features by Month 

 Updated on 

 Fri Jul 10 12:56:22 PDT 2026 

 Focus 

 Home 

 Enterprise DLP 

 Administration 

 Configure Enterprise DLP 

 Email DLP 

 Onboard Microsoft Exchange Online 

 Obtain Your Microsoft Exchange Domain and Relay Host 

 Download PDF 

 Enterprise DLP 

 Obtain Your Microsoft Exchange Domain and Relay Host 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Enterprise DLP Docs 

 Activation & Onboarding 

 Getting Started 

 Administration 

 Reference 

 Release Notes 

 New Features by OS Version 

 New Features by Month 

 Previous 

 Create Microsoft Exchange Transport Rules 

 Next 

 Onboard Gmail 

 Obtain Your Microsoft Exchange Domain and Relay Host 

 Obtain your Microsoft Exchange domain and relay host to connect Microsoft
 Exchange to Enterprise Data Loss Prevention (E-DLP) . 

 On May 7, 2025 , Palo Alto Networks is introducing new Evidence Storage and Syslog Forwarding service IP
 addresses to improve performance and expand availability for these services
 globally. 

 You must allow these new service IP addresses on your network
 to avoid disruptions for these services. Review the Enterprise DLP 
 Release Notes for more
 information. 

 Where Can I Use This? What Do I Need? 

 Data Security 

 One of the following licenses that include the Enterprise DLP license 

 Review the Supported
 Platforms for details on the required license
 for each enforcement point. 

 Prisma Access CASB license 

 Next-Generation
CASB for Prisma Access and NGFW (CASB-X) license 

 Data Security license 

 Email DLP license 

 You must obtain your Microsoft Exchange domain and relay host to connect Microsoft
 Exchange and Enterprise Data Loss Prevention (E-DLP) for inline inspection and prevention of
 sensitive data exfiltration contained in outbound emails. 

 Log in
 to the Microsoft Office 365 Admin Portal . 

 Select Settings Domains . 

 Make note of the Microsoft Exchange domains listed in the Domain
 name list. 

 Enterprise DLP supports inline inspection of emails from multiple
 domains. If you use multiple Microsoft Exchange domains, make sure to make
 note of all email domains for which you want inline inspection of
 emails. 

 Obtain the relay host for the Microsoft Exchange domain. 

 Repeat this step for all Microsoft Exchange domains you want to connect to
 Enterprise DLP . 

 Click the Microsoft Exchange domain. 

 Select DNS records . 

 In the Microsoft Exchange section, locate
 the MX record. 

 The Value column for the MX record lists
 the relay host for the domain. An example of a relay host is shown
 below. 

 The MX record displays a 0 before
 the relay host. This character is not required to connect
 Microsoft Exchange to Enterprise DLP . 

 Previous 

 Create Microsoft Exchange Transport Rules 

 Next 

 Onboard Gmail 

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

 SaaS Security 

 Endpoints 

 GlobalProtect 

 Visibility & Monitoring 

 Dashboards 

 Incidents and Alerts 

 Reports 

 Autonomous DEM 

 Best Practices 

 Best Practices Library 

 Experts Corner 

 Solutions Docs from Product Experts 

 Administration 

 Cloud-Delivered Security Services 

 Data Filtering 

 Enterprise DLP 

 Task 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

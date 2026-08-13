---
url: https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-admin/user-id/deploy-user-id-in-a-large-scale-network
fetched_at: 2026-08-13T17:10:05Z
source: palo-alto-main
---

# Deploy User-ID in a Large-Scale Network Clear

Deploy User-ID in a Large-Scale Network 

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

 Deploy User-ID in a Large-Scale Network 

 Updated on 

 Mon Aug 03 13:41:44 PDT 2026 

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

 Mon Aug 03 13:41:44 PDT 2026 

 Focus 

 Home 

 Next-Generation Firewall 

 User-ID 

 Deploy User-ID in a Large-Scale Network 

 Download PDF 

 Next-Generation Firewall 

 Deploy User-ID in a Large-Scale Network 

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

 Verify the User-ID Configuration 

 Next 

 Deploy User-ID for Numerous Mapping Information Sources 

 Deploy User-ID in a Large-Scale Network 

 A large-scale network can have hundreds of information
sources that firewalls query to map IP addresses to usernames and
to map usernames to user groups. You can simplify User-ID administration
for such a network by aggregating the user mapping and group mapping
information before the User-ID agents collect it, thereby reducing
the number of required agents. 

 A large-scale network can also have numerous firewalls that use
the mapping information to enforce policies. You can reduce the
resources that the firewalls and information sources use in the
querying process by configuring some firewalls to acquire mapping
information through redistribution instead of direct querying. Redistribution
also enables the firewalls to enforce user-based policies when users
rely on local sources for authentication (such as regional directory
services) but need access to remote services and applications (such
as global data center applications). 

 If you Configure Authentication Policy , your firewalls
must also redistribute the Authentication Timestamps associated
with user responses to authentication challenges. Firewalls use
the timestamps to evaluate the timeouts for Authentication policy
rules. The timeouts allow a user who successfully authenticates
to later request services and applications without authenticating
again within the timeout periods. Redistributing timestamps enables
you to enforce consistent timeouts for each user even if the firewall
that initially grants a user access is not the same firewall that
later controls access for that user. 

 If you have configured multiple virtual systems, you can share
IP address-to-username mapping information across virtual systems
by selecting a virtual system as a User-ID hub. 

 Deploy User-ID for Numerous Mapping Information Sources 

 Redistribute Data and Authentication Timestamps 

 Share User-ID Mappings Across Virtual Systems 

 Previous 

 Verify the User-ID Configuration 

 Next 

 Deploy User-ID for Numerous Mapping Information Sources 

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

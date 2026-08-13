---
url: https://docs.paloaltonetworks.com/iot/release-notes/network-discovery-plugin-for-panorama/network-discovery-plugin-2-1-0/features-introduced-in-network-discovery-2-1-0
fetched_at: 2026-08-13T16:37:58Z
source: palo-alto-main
---

# Features Introduced in Network Discovery 2.1 Clear

Features Introduced in Network Discovery 2.1 

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

 Features Introduced in Network Discovery 2.1 

 Updated on 

 Tue Jul 28 18:47:47 PDT 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Device Security Docs 

 Activation & Onboarding 

 Getting Started 

 Administration 

 Enterprise Administration 

 Integrations 

 Release Notes 

 Best Practice 

 New Features 

 Updated on 

 Tue Jul 28 18:47:47 PDT 2026 

 Focus 

 Home 

 Device Security 

 Release Notes 

 Panorama Network Discovery Plugin 

 Network Discovery Plugin 2.1 

 Features Introduced in Network Discovery 2.1 

 Download PDF 

 Device Security 

 Features Introduced in Network Discovery 2.1 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Device Security Docs 

 Activation & Onboarding 

 Getting Started 

 Administration 

 Enterprise Administration 

 Integrations 

 Release Notes 

 Best Practice 

 New Features 

 Previous 

 Network Discovery Plugin 2.1 

 Next 

 Known Issues in Network Discovery 2.1 

 Features Introduced in Network Discovery 2.1 

 Review the features introduced in the Network Discovery plugin 2.1. 

 Where Can I Use This? What Do I Need? 

 NGFW (Managed by PAN-OS or Panorama) 

 One of the following subscriptions: 

 Device Security subscription

 Precision AI bundle subscription

 Device Security X subscription

 Review the features introduced in the Network Discovery plugin 2.1. 

 What's New in Network Discovery 2.1.0 

 Review the new features introduced in Network Discovery plugin 2.1.0. 

 New Feature Description 

 SNMP Crawling Settings Enhancements 

 PAN-OS 10.2.14 and later 10.2 releases 

 PAN-OS 11.1 and later 11 releases 

 Network Discovery adds support for multiple entry switches,
 multiple SNMP credentials, and site creation for more thorough
 SNMP crawling .

 You can define up to 10 entry switches for SNMP crawling and
 choose which switch the crawling job starts from. At least one
 entry switch must be defined.

 You can add up to 15 SNMP credentials for Network Discovery to
 use when crawling switches, and you can choose the order in
 which Network Discovery tries the credentials. Network Discovery
 tries the credentials until it finds one that works or until
 all credentials have been tried. When you are adding a new
 credential, you can choose which entry point switch to test the
 credential on.

 When a subnet is learned through SNMP crawling, you can define
 site mapping based on entry point switch. If the subnet is
 already assigned to a site in Device Security , then the
 subnet's site mapping will be overwritten based on the site
 assigned to the entry point in the Network Discovery plugin.
 Network Discovery won't overwrite any sites that you
 manually configured.

 Previous 

 Network Discovery Plugin 2.1 

 Next 

 Known Issues in Network Discovery 2.1 

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

 Firewalls 

 PAN-OS 

 PAN-OS SD-WAN 

 Service Provider 

 VM-Series 

 SASE 

 Prisma Access 

 Strata Multitenant Cloud Manager 

 Device Security 

 Release Notes 

 Plugins 

 Cloud-Delivered Security Services 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

---
url: https://docs.paloaltonetworks.com/iot/release-notes/network-discovery-plugin-for-panorama/network-discovery-plugin-2-0-0/features-introduced-in-network-discovery-2-0-0
fetched_at: 2026-08-13T16:37:58Z
source: palo-alto-main
---

# Features Introduced in Network Discovery 2.0 Clear

Features Introduced in Network Discovery 2.0 

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

 Features Introduced in Network Discovery 2.0 

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

 Network Discovery Plugin 2.0 

 Features Introduced in Network Discovery 2.0 

 Download PDF 

 Device Security 

 Features Introduced in Network Discovery 2.0 

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

 Network Discovery Plugin 2.0 

 Next 

 Known Issues in Network Discovery 2.0 

 Features Introduced in Network Discovery 2.0 

 Review the features introduced in the Network Discovery plugin 2.0. 

 Where Can I Use This? What Do I Need? 

 NGFW (Managed by PAN-OS or Panorama) 

 One of the following subscriptions: 

 Device Security subscription

 Precision AI bundle subscription

 Device Security X subscription

 Review the features introduced in the Network Discovery plugin 2.0. 

 What's New in Network Discovery 2.0.2 

 Review the new features introduced in Network Discovery plugin 2.0.2. 

 New Feature Description 

 SNMP Crawling Settings Enhancements 

 PAN-OS 11.1 and later 11 releases 

 Network Discovery adds configuration options to
 SNMP crawling 
 to help target specific parts of the network and control
 resource consumption.

 For SNMP network discovery or for SNMP network data
 refreshment jobs, you can set the maximum duration for the
 jobs to run.

 When Network Discovery queries SNMP switches, you can specify
 the name of the site where the job queries switches, and
 configure the maximum number of hops to crawl from the entry
 switch. Additionally, you can specify how long to wait for a
 response before an attempt times out, as well as how many times
 to retry querying a switch.

 Polling Protocols Support 

 PAN-OS 11.1 and later 11 releases 

 Network Discovery adds support for
 polling 
 with the following protocols:

 FANUC Focas 

 IEC 61850 MMS 

 Mitsubishi MELSOFT TCP 

 Omron FINS 

 Profinet 

 UMAS Modbus 

 UPnP 

 What's New in Network Discovery 2.0.1 

 Review the new features introduced in Network Discovery plugin 2.0.1. 

 New Feature Description 

 Enable Debug Logs 

 PAN-OS 11.1 and later 11 releases 

 Enable debug logs from Network Discovery polling using the following command in the admin terminal. 

request plugins debug networkdiscovery level [high|low|medium|off]

 What's New in Network Discovery 2.0.0 

 Review the new features introduced in Network Discovery plugin 2.0.0. 

 New Feature Description 

 Learn Device Attributes by Polling 

 PAN-OS 11.1 and later 11 releases 

 You can now
 learn device attributes by
 polling 
 using various protocols through the Network Discovery plugin.
 When the Network Discovery plugin successfully polls a device,
 Device Security adds whatever attributes it didn't yet have for the
 device. When it learns attributes for assets that aren't yet in
 its database, it creates new entries for the devices. If
 Device Security learns only an IP address, it adds a new entry to
 the IP Endpoints page.

 Previous 

 Network Discovery Plugin 2.0 

 Next 

 Known Issues in Network Discovery 2.0 

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

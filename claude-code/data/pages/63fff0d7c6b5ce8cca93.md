---
url: https://docs.paloaltonetworks.com/sd-wan/release-notes/panorama-plugin-for-sd-wan/sd-wan-plugin-220/features-introduced-in-sd-wan-2-2
fetched_at: 2026-08-13T17:35:58Z
source: palo-alto-main
---

# Features Introduced in SD-WAN Plugin 2.2 Clear

Features Introduced in SD-WAN Plugin 2.2 

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

 Features Introduced in SD-WAN Plugin 2.2 

 Updated on 

 Thu Jul 30 23:22:25 PDT 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 SD-WAN Docs 

 Activation & Onboarding 

 Getting Started 

 Administration 

 Help 

 Select a Document 

 3.4 

 3.3 

 3.2 

 3.1 

 3.0 

 2.2 

 2.1 

 2.0 

 1.0 

 Release Notes 

 New Features 

 Updated on 

 Thu Jul 30 23:22:25 PDT 2026 

 Focus 

 Home 

 SD-WAN 

 Panorama Plugin for SD-WAN 

 Panorama Plugin for SD-WAN 2.2 

 Features Introduced in SD-WAN Plugin 2.2 

 Download PDF 

 SD-WAN 

 Features Introduced in SD-WAN Plugin 2.2 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 SD-WAN Docs 

 Activation & Onboarding 

 Getting Started 

 Administration 

 Help 

 Select a Document 

 3.4 

 3.3 

 3.2 

 3.1 

 3.0 

 2.2 

 2.1 

 2.0 

 1.0 

 Release Notes 

 New Features 

 Previous 

 Panorama Plugin for SD-WAN 2.2 

 Next 

 Known Issues in SD-WAN Plugin 2.2 

 Features Introduced in SD-WAN Plugin 2.2 

 Features introduced in SD-WAN Plugin 2.2 releases. 

 Our SD-WAN subscription integrates with
PAN-OS to provide intelligent, dynamic path selection on top of
the industry leading security that PAN-OS software already delivers.
Secure SD-WAN provides the optimal end-user experience by leveraging multiple
ISP links to ensure application performance and scale capacity.
See Upgrade/Downgrade Considerations and Upgrade
the SD-WAN Plugin in the PAN-OS Upgrade Guide 10.1. 

 The SD-WAN Administrator’s Guide
2.2 provides information about how to use the SD-WAN plugin
features in this release. 

 What's New in SD-WAN Plugin 2.2.7 

 What's New in SD-WAN Plugin 2.2.6 

 What's New in SD-WAN Plugin 2.2.5 

 What's New in SD-WAN Plugin 2.2.4 

 What's New in SD-WAN Plugin 2.2.3 

 What’s New in SD-WAN
Plugin 2.2.2 

 What’s New in SD-WAN Plugin 2.2.1 

 What’s New in SD-WAN
Plugin 2.2.0 

 What's New in SD-WAN Plugin 2.2.7 

 New Feature Description 

 SD-WAN Plugin Improvements 

 Earlier to SD-WAN plugin 2.2.7 version, the SD-WAN generated
 configurations (such as the IKE ID and tunnel names) uses the
 active firewall's serial number. Therefore, whenever a HA
 failover occurs, the SD-WAN generated configurations would reset
 with the active firewall's serial number that results in
 temporary tunnel flaps. 

 We have improved the SD-WAN plugin 2.2.7 version by using the
 lower serial number among the HA devices for generating the
 SD-WAN configurations that remove tunnel flaps. This improvement
 also introduces the following SD-WAN configuration changes: 

 the IKE key ID is formed with the lower serial number
 between the HA devices. 

 the SD-WAN generated configurations, such as route table
 entry in virtual router, tunnel name, IKE gateway name, BGP
 import rule name, routing profile, BGP peer, and BGP
 filtering profile will be reset. 

 Tunnel names and corresponding IP address would change as
 the tunnel names are created from a lower serial number
 among the two HA devices. 

 MongoDB HA Synchronization CLI Commands 

 We have introduced the following mongoDB related HA peer
 synchronization commands that must be executed only on the
 active HA peer: 

 debug plugins sd_wan mongo-db
 sync-db-to-peer —Use this command to
 synchronize the SD-WAN mongo database from active HA peer
 with the passive HA peer. You must execute this command in
 the following cases: 
 when the mongo database of HA peers goes out of
 synchronization. 

 when you convert a
 SD-WAN enabled standalone Panorama to a Panorama
 HA or replace a SD-WAN
 enabled Panorama HA peer . 

 when the HA synchronization job of the passive HA
 peer fails with The active DB's is not
 synchronized with passive's error
 message. 

 We recommend you to check the status of the
 operation log by executing debug plugins
 sd_wan mongo-db sync-status command
 before executing debug plugins sd_wan
 mongo-db sync-db-to-peer command.
 Because, the SD-WAN mongo DB operation log
 synchronization must be successful before you
 synchronize the HA peers. 

 debug plugins sd_wan mongo-db
 sync-status —Use this command to check the
 synchronization status of the operation log (oplog). This
 command only checks the operation logs. 

 What's New in SD-WAN Plugin 2.2.6 

 The SD-WAN plugin 2.2.6 release provides bug and performance fixes. 

 What's New in SD-WAN Plugin 2.2.5 

 The SD-WAN plugin 2.2.5 release provides bug and performance fixes. 

 What's New in SD-WAN Plugin 2.2.4 

 The SD-WAN plugin 2.2.4 release provides bug and performance fixes. 

 What's New in SD-WAN Plugin 2.2.3 

 The SD-WAN plugin 2.2.3 release provides bug and performance fixes. 

 What’s New in SD-WAN Plugin 2.2.2 

 The SD-WAN plugin 2.2.2 release provides bug and performance fixes. 

 What’s New in SD-WAN Plugin 2.2.1 

 Key features introduced with the SD-WAN plugin 2.2.1
release: 

 New SD-WAN Feature Description 

 Copy ToS Header Support 

 SD-WAN hubs and branches allow you to automatically
copy the ToS or Differentiated Services Code Point (DSCP) markings
from the inner IPv4 header to the VPN header of packets so that
traffic going through the VPN tunnel can preserve that information
for QoS. 

 What’s New
in SD-WAN Plugin 2.2.0 

 Key features introduced with the SD-WAN plugin 2.2.0
release: 

 New SD-WAN Feature Description 

 Prisma Access Hub Support 

 As more internet services move to the cloud, PAN-OS
Secure SD-WAN now offers security in the cloud using Prisma Access,
in addition to security on-premises using PAN-OS firewalls. The
SD-WAN hub-and-spoke topology now supports a Prisma Access hub.
You can secure your internet traffic for specific applications at
the branch location or in the cloud with Prisma Access and have
this traffic fail over to any other VPN tunnel if necessary. 

 This
feature is available for early evaluation and will go live in January,
2022. Until then, ask your sale representative to request a manual upgrade
of your Prisma Access IPSec Termination Nodes to run PAN-OS 10.0.7,
so you can participate in the early evaluation and onboard a branch
office to the Prisma Access Hub. 

 Previous 

 Panorama Plugin for SD-WAN 2.2 

 Next 

 Known Issues in SD-WAN Plugin 2.2 

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

 IoT Security 

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

 Release Notes 

 Network Security 

 PAN-OS 

 Next-Generation Firewall 

 Plugins 

 Panorama 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

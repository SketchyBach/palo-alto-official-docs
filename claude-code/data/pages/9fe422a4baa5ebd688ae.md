---
url: https://docs.paloaltonetworks.com/sd-wan/release-notes/panorama-plugin-for-sd-wan/panorama-plugin-for-sd-wan-3-5/features-introduced-in-sd-wan-plugin-3-5
fetched_at: 2026-08-13T17:35:56Z
source: palo-alto-main
---

# Features Introduced in SD-WAN Plugin 3.5 Clear

Features Introduced in SD-WAN Plugin 3.5 

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

 Features Introduced in SD-WAN Plugin 3.5 

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

 Panorama Plugin for SD-WAN 3.5 

 Features Introduced in SD-WAN Plugin 3.5 

 Download PDF 

 SD-WAN 

 Features Introduced in SD-WAN Plugin 3.5 

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

 Panorama Plugin for SD-WAN 3.5 

 Next 

 Known Issues in SD-WAN Plugin 3.5 

 Features Introduced in SD-WAN Plugin 3.5 

 New features for SD-WAN 3.5. 

 The SD-WAN Administrator’s Guide 3.2 & Later provides
 information about how to use the SD-WAN plugin features in this release. 

 What’s New in SD-WAN Plugin 3.5.0 

 What’s New in SD-WAN Plugin 3.5.0 

 Key features introduced with the SD-WAN plugin 3.5.0 release: 

 New SD-WAN Feature Description 

 SD-WAN Bandwidth-Based Path Selection 

 PAN-OS® software supports bandwidth as a path quality metric for
 SD-WAN traffic distribution. You can now define bandwidth
 thresholds and sensitivity levels within SD-WAN Path Quality
 profiles to ensure links have sufficient capacity before the
 firewall selects them for application traffic. The firewall
 evaluates path quality based on jitter, latency, packet loss,
 and now, bandwidth. 

 The system calculates real-time bandwidth usage across all
 dataplanes to monitor link capacity. During session setup, the
 firewall compares the current link usage against your configured
 thresholds. If a link’s usage exceeds the specified threshold,
 the system disqualifies that path to prevent congestion. By
 adding bandwidth to the path selection logic, you gain granular
 control over traffic steering. 

 This ensures that applications use links with available
 capacity, maintaining performance alongside existing jitter,
 latency, and packet loss parameters. 

 Dedicated Tunnels for Panorama Connectivity 

 To ensure uninterrupted connectivity between the SD-WAN devices
 and Panorama, the SD-WAN plugin introduces an option to
 configure the dedicated tunnel to Panorama. Unlike the SD-WAN
 overlay network connectivity to Panorama that may go down, which
 causes unreachability of SD-WAN devices to Panorama, the
 dedicated tunnel stays connected all the time. 

 This feature is supported only on
 physical Ethernet interfaces. It is not supported on
 subinterfaces or aggregate interfaces. 

 The dedicated tunnel to
 Panorama establishes a persistent and dedicated IPSec
 tunnels from your branch devices to Panorama through designated
 termination devices using direct internet access (DIA)
 interfaces. With dedicated tunnels in place, even if your
 primary SD-WAN overlay network becomes unavailable, your devices
 can still reach Panorama to receive configuration updates and
 troubleshooting commands. 

 Previous 

 Panorama Plugin for SD-WAN 3.5 

 Next 

 Known Issues in SD-WAN Plugin 3.5 

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

 Next-Generation Firewall 

 SD-WAN for NGFW Plugin 

 Plugins 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

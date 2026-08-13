---
url: https://docs.paloaltonetworks.com/prisma-sd-wan/release-notes/6-1/prisma-sd-wan-ion-device-release-6-1/upgrade-downgrade-considerations-in-prisma-sd-wan-ion-release-6-1
fetched_at: 2026-08-13T17:31:28Z
source: palo-alto-main
---

# Upgrade or Downgrade Considerations in  ION
Release 6.1 Clear

Upgrade or Downgrade Considerations in ION
Release 6.1 

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

 Upgrade or Downgrade Considerations in ION
Release 6.1 

 Updated on 

 Thu Feb 05 02:55:06 PST 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma SD-WAN Docs 

 Activation & Onboarding 

 Administration 

 CloudBlades 

 Select a Document 

 CloudBlade Integrations 

 CloudBlades Integration with Prisma Access 

 Deployment 

 Incidents & Alerts 

 Reference 

 Release Notes 

 Select a Document 

 ION 6.8 

 ION 6.6 

 ION 6.5 

 ION 6.4 

 ION 6.3 

 ION 6.1 

 ION 5.6 

 Prisma SD-WAN Controller 

 Prisma SD-WAN On-Premises Controller 

 Prisma SD-WAN CloudBlades 

 Prisma Access CloudBlade Cloud Managed 

 Prisma Access CloudBlade Panorama Managed 

 New Features 

 Updated on 

 Thu Feb 05 02:55:06 PST 2026 

 Focus 

 Home 

 Prisma SD-WAN 

 ION Device Release 6.1 

 Upgrade or Downgrade Considerations in ION
Release 6.1 

 Download PDF 

 Prisma SD-WAN 

 Upgrade or Downgrade Considerations in ION
Release 6.1 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma SD-WAN Docs 

 Activation & Onboarding 

 Administration 

 CloudBlades 

 Select a Document 

 CloudBlade Integrations 

 CloudBlades Integration with Prisma Access 

 Deployment 

 Incidents & Alerts 

 Reference 

 Release Notes 

 Select a Document 

 ION 6.8 

 ION 6.6 

 ION 6.5 

 ION 6.4 

 ION 6.3 

 ION 6.1 

 ION 5.6 

 Prisma SD-WAN Controller 

 Prisma SD-WAN On-Premises Controller 

 Prisma SD-WAN CloudBlades 

 Prisma Access CloudBlade Cloud Managed 

 Prisma Access CloudBlade Panorama Managed 

 New Features 

 Previous 

 Features Introduced in ION Release 6.1 

 Next 

 CLI Commands in ION Release 6.1 

 Upgrade or Downgrade Considerations in ION
Release 6.1 

 Learn about the device upgrade and downgrade considerations
for Release 6.1. 

 The following section details the upgrade path to 
 release 6.1.x. Review the upgrade and downgrade considerations before upgrading to this
 release. The table describes the ION element software release naming convention for
 release 6.1.x. 

 ION ELEMENT SOFTWARE (SW) RELEASE NAMING
 CONVENTION 

 1st Digit - Primary Release 2nd Digit - Release Number 3rd Digit - Main Release Number 4th Digit - SW Build Number 

 6 1 1 b1 

 Prerequisite —Prior to upgrading branch ION devices
to 6.1.X, ensure that all data center ION devices are running ION
software version 5.4.x or higher. 

 Upgrade Or Downgrade Path 

 Use the following paths to upgrade to release 6.1.x, and use
the path in reverse to rollback to the version you started from: 

 4.7.1 -> 5.0.x -> 5.1.x -> 5.4.x -> 5.6.x -> 6.1.x 

 4.7.1 -> 5.0.x -> 5.2.x -> 5.5.x -> 5.6.x -> 6.1.x 

 5.0.x -> 5.2.x -> 5.5.x -> 5.6.x -> 6.1.x 

 5.1.x -> 5.4.x -> 5.6.x ->6.1.x 

 5.2.x -> 5.5.x -> 5.6.x -> 6.1.x 

 5.4.x -> 5.6.x -> 6.1.x 

 Upgrade or Downgrade Considerations in ION Device Release 6.1.1 

 Upgrade/Downgrade Path for Virtual Form Factor in FIPS Mode 

 Upgrade or Downgrade Considerations in ION Device
 Release 6.1.1 

 The following table lists the new features that have upgrade or
 downgrade impact. Make sure you understand all upgrade/downgrade considerations
 before you upgrade to or downgrade from release
 6.1.1. 

 Feature Upgrade Considerations Downgrade Considerations 

 Support for IPv6 

 The device software downgrade will proceed only when
 the target device software is compatible with the IP address type.
 When the device is unassigned, the controller will revert the
 cellular IP address type to the default value. 

 Upgrade/Downgrade Path for Virtual Form Factor in FIPS Mode 

 When upgrading from 6.1.x or 5.6.x to 6.2.x or later images of virtual form
 factor (VFF), there may be a disruption of service links, stats/logs connections,
 and remote sessions in FIPS mode. This issue is observed only when the VFF in FIPS
 mode is upgraded to 6.2.1 or later. 

 Upgrade or Downgrade Versions 

 Follow the below steps if you are on a VFF pre-6.2.1 with FIPS mode enabled
 and upgrading to software version greater than or equal to 6.2.1 (includes 6.2.2,
 6.3.4, 6.3.5 and 6.4.1), (excluding 6.2.3, 6.3.1, 6.3.2, 6.3.3 already blocked on
 the Controller). 

 First, disable FIPS mode on VFF. 

 Upgrade to the desired software version. 

 Then, enable FIPS mode. Enabling FIPS mode can take up to 20 minutes. 

 The above steps do not apply when upgrading directly from 6.1.x to
 6.4.2 or higher. 

 Considering these known limitations and FIPS certified versions are 6.1.2
 and 6.4.2 or higher, for VFF in FIPS mode on any older software version (<
 6.2.1), Palo Alto Networks recommend the upgrade path to be 6.4.2 and all later
 versions. 

 Upgrade Advisory 

 The following ION platforms (ION 1000, ION 2000, and ION 1200) if consistently use
 greater than 80% of memory, are at risk of experiencing unexpected reboots after an
 upgrade. The risk increases when upgrading from 5.x to 6.x due to the overall
 software architecture difference between the release series. Before performing any
 upgrades, Palo Alto Networks recommends that you assess available system memory on
 the target devices. For guidance on memory management best practices, see here . 

 Previous 

 Features Introduced in ION Release 6.1 

 Next 

 CLI Commands in ION Release 6.1 

 On This Page 

 Activation & Onboarding 

 Strata Cloud Manager 

 Activate a License or Product 

 Cloud Identity Engine 

 Hub 

 Identity and Access Management 

 Tenant Management 

 SASE 

 Prisma Access 

 Strata Multitenant Cloud Manager 

 AI-Powered ADEM 

 Prisma Access Monitoring and Visibility 

 Visibility & Monitoring 

 Dashboards 

 Incidents and Alerts 

 Reports 

 Autonomous DEM 

 FedRAMP 

 Prisma SASE for FedRAMP 

 Hardware Reference 

 ION 1000 

 ION 1200 

 ION 1200-S 

 ION 2000 

 ION 3000 

 ION 3200 and ION 3200H 

 ION 5200 

 ION 7000 

 ION 9000 

 ION 9200 

 Hardware Quick Start Guides 

 ION 1200 

 ION 1200 4G 

 ION 1200 5G 

 ION 1200-S 

 ION 1200-S 4G 

 ION 1200-S 5G 

 ION 3200 

 ION 3200H 

 ION 3200H 5G 

 ION 5200 

 ION 9200 

 Virtual ION Deployment 

 Virtual ION on AWS 

 Virtual ION on Azure 

 Virtual ION on GCP 

 Virtual ION on Alibaba Cloud 

 Virtual ION on KVM for NFV 

 Virtual ION on OCI 

 Virtual ION on VMware 

 Virtual ION on Megaport Virtual Edge 

 Virtual ION on Dell PowerEdge 

 Prisma SD-WAN Integration 

 AWS Cloud-WAN Integration (GRE Connect) 

 AWS Cloud-WAN Integration (Tunnel-less Connect) 

 Checkpoint Integration 

 LiveAction Integration 

 Netskope Integration 

 Symantec Web Security Services Integration 

 Prisma SD-WAN Experts Corner 

 Network Policy 

 QoS Whitepaper 

 Security Architecture Whitepaper 

 External Antennas for ION-C Series 

 Dynamic Path Selection 

 Best Practices 

 Best Practices Library 

 Resources 

 All Products A - Z 

 Compatibility Matrix 

 Release Notes 

 6.1 

 Prisma SASE 

 Prisma SD-WAN 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

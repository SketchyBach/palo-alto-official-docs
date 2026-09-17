---
url: https://docs.paloaltonetworks.com/prisma-sd-wan/release-notes/6-1/prisma-sd-wan-ion-device-release-6-1/upgrade-downgrade-considerations-in-prisma-sd-wan-ion-release-6-1
fetched_at: 2026-09-16T07:48:51Z
source: strata-and-sase
---

# Upgrade or Downgrade Considerations in  ION
Release 6.1 Clear

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

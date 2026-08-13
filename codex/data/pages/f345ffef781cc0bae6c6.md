---
url: https://docs.paloaltonetworks.com/autonomous-dem/administration/types-of-application-experience-monitoring/adem-monitoring-and-tests-for-remote-networks
fetched_at: 2026-08-13T15:29:45Z
source: palo-alto-main
---

# Remote Sites Clear

Remote Sites 

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

 Remote Sites 

 Updated on 

 Wed Aug 12 08:13:05 PDT 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Autonomous DEM Docs 

 Activation & Onboarding 

 Administration 

 Select a Document 

 AI-Powered ADEM 

 Autonomous DEM for China 

 User Guide 

 Release Notes 

 New Features 

 Updated on 

 Wed Aug 12 08:13:05 PDT 2026 

 Focus 

 Home 

 Autonomous DEM 

 Types of Application Experience Monitoring 

 Remote Sites 

 Download PDF 

 Autonomous DEM 

 Remote Sites 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Autonomous DEM Docs 

 Activation & Onboarding 

 Administration 

 Select a Document 

 AI-Powered ADEM 

 Autonomous DEM for China 

 User Guide 

 Release Notes 

 New Features 

 Remote Sites 

 ADEM lets you create synthetic tests for remote sites. These tests provide a good
 baseline view of the digital experience segment-by-segment across all monitored
 applications 

 You can use ADEM to monitor the application experience of users connecting from two kinds of
 SD-WAN remote sites: 
 a Prisma SD-WAN ION device 

 a next-generation firewall (NGFW) with an SD-WAN subscription 
 ADEM supports monitoring through three paths—the Prisma Access path, the Secure
 Fabric path, and the direct path. 

 SD-WAN device monitoring —The ADEM agent on the ION device or the NGFW monitors the
 following: 

 CPU utilization 

 Memory utilization 

 Historical trends 

 Remote site traffic visibility —ADEM provides continuous visibility into real traffic usage
 between SD-WAN remote sites and applications and for traffic traversing Prisma Access , including traffic to SaaS applications, Infrastructure as a
 Service (IaaS) applications, as well as traffic to applications in your own data
 center. 

 Synthetic Monitoring —The ADEM-enabled SD-WAN site and the cloud agents within Prisma Access use synthetic tests to baseline end-to-end network quality
 metrics—latency, jitter, and loss—for each segment from the remote site to the
 monitored applications on all WAN paths (active and backup). In addition,
 ADEM-enabled SD-WAN site and the cloud agents within Prisma Access also use
 synthetic tests to collect web performance metrics, which capture metrics about
 the HTTP and HTTPS transactions to a specific application, including application
 availability and uptime, DNS lookup, TCP connect, SSL connect, server response
 time, time-to-first-byte, data transfer rate, and time-to-last-byte. 

 Because the synthetic tests are layered,
they give a good baseline view of the digital experience segment-by-segment
across all monitored applications, and allow you to quickly visualize
when and where a change occurred that led to degradation of your
users’ digital experience. 

 An ADEM enabled SD-WAN site can monitor all WAN paths (active and backup) based on forwarding
 policies configured on the SD-WAN. It can monitor Prisma Access path, Secure
 Fabric path as well as Direct Access path. 

 The three paths shown in the above image are described in detail
below: 

 Prisma Access Path 

 This path is used for applications that are configured to use Prisma Access for security. 

 Prisma SD-WAN 

 NGFW 

 Secure Fabric (SD-WAN) Path 

 When using this path, ADEM can monitor applications hosted on SaaS, IaaS, or private applications
 hosted in a data center through the Secure Fabric tunnel between the SD-WAN
 remote site device and an SD-WAN data center device. 

 Prisma SD-WAN 

 NGFW 

 Direct Access Path 

 When using this path, ADEM monitors SaaS applications directly from the SD-WAN remote site over
 the internet. This test does not go through the Prisma Access or the Secure
 Fabric path. 

 Prisma SD-WAN 

 NGFW 

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

 SASE 

 Prisma Access 

 Strata Multitenant Cloud Manager 

 AI-Powered ADEM 

 Prisma Access Monitoring and Visibility 

 Prisma SD-WAN 

 ION Devices 

 Next-Generation CASB 

 Visibility & Monitoring 

 Dashboards 

 Incidents and Alerts 

 Reports 

 SASE 

 Administration 

 Autonomous DEM 

 Prisma SASE 

 Strata Cloud Manager 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

---
url: https://docs.paloaltonetworks.com/prisma-sd-wan/administration/prisma-sd-wan-sites-and-devices/set-up-sites/add-a-branch
fetched_at: 2026-08-13T17:28:24Z
source: palo-alto-main
---

# Add a Branch Site Clear

Add a Branch Site 

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

 Add a Branch Site 

 Updated on 

 Mon Aug 10 04:14:37 PDT 2026 

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

 Mon Aug 10 04:14:37 PDT 2026 

 Focus 

 Home 

 Prisma SD-WAN 

 Prisma SD-WAN Administrator’s Guide 

 Prisma SD-WAN Sites and Devices 

 Set Up Sites 

 Add a Branch Site 

 Download PDF 

 Prisma SD-WAN 

 Add a Branch Site 

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

 Set Up Sites 

 Next 

 Add a Data Center 

 Add a Branch Site 

 As you may already know, having multiple branches within an enterprise network can be a
 complex task. However, with our platform, the process becomes simpler and more efficient. 

 An enterprise may have one or more branches within a network. As part of creating a
 data center, you can select a circuit categories, circuit labels, circuit
 specifications, and device specifications. 

 Select Configuration Prisma SD-WAN Branch Sites Add Site . 

 On the Site Information tab, enter basic information for
 the Site Name , City , and
 Country for the site and click
 Next to proceed to configure circuits for the site. 

 Complete Site Name and Address (Using address search is recommended). 

 Enable Configure as a Branch Gateway site to convert
 an existing branch site to a branch gateway site. This
 provides the policy transit and LQM server capabilities of a data center
 site along with the visibility and path selection of a branch site. 

 Verify the Static SGI value to be
 between 1 and 65533 for the ION generated traffic. The Security
 Group Information option is enabled by default for Static
 tag configuration. 

 On the Domain & Policies tab, select a
 Domain from the drop-down. 

 By default, a preset domain is displayed for a branch site. 

 Click Associate Branch With Default Data Center
 Cluster to associate the newly created branch with the
 default cluster. It will be checked (by default) and unchecked to choose
 a different cluster from the list. 

 Configure Policies and click
 Next . 

 Ensure that the default Path Policy Stack ,
 Performance Policy Stack , QoS
 Policy Stack , Security Policy
 Stack , and NAT Policy Stack 
 are selected. 

 On the WAN Circuits and Devices tab, click
 Add Circuits to add Internet Circuits and Private WAN
 Circuits. 

 By default, there are a few pre-defined configure circuits in the
 system that you may use when you configure the site. You can edit these
 labels or rename any of the remaining categories through Circuit Categories
 under Stacked Policies. 

 Select Assign Devices and select from the available
 devices to assign or Create Device Shells to create up to
 2 Device Shells to pre-provision and assign to the Data
 Center Site depending on your requirement. Click Save &
 Exit . 

 You can view the summary of the newly added branch. 

 Previous 

 Set Up Sites 

 Next 

 Add a Data Center 

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

 SASE 

 Administration 

 Prisma SD-WAN 

 Strata Cloud Manager 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

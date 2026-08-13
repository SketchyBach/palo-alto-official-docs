---
url: https://docs.paloaltonetworks.com/prisma-sd-wan/deployment/overview-of-on-premises-controller/minimum-system-requirements
fetched_at: 2026-08-13T17:29:25Z
source: palo-alto-main
---

# Minimum Hardware Requirements Clear

Minimum Hardware Requirements 

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

 Minimum Hardware Requirements 

 Updated on 

 Wed Feb 25 07:20:45 PST 2026 

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

 Wed Feb 25 07:20:45 PST 2026 

 Focus 

 Home 

 Prisma SD-WAN 

 Overview of On-Premises Controller 

 Minimum Hardware Requirements 

 Download PDF 

 Prisma SD-WAN 

 Minimum Hardware Requirements 

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

 Overview of On-Premises Controller 

 Next 

 Understand Installation Workflow 

 Minimum Hardware Requirements 

 Understand the minimum hardware requirements before installing the On-Premises
 Controller for Prisma SD-WAN . 

 Where Can I Use This? What Do I Need? 

 Prisma SD-WAN 

 Prisma SD-WAN 

 On-premises controller is supported on all ION device models. You can increase
 the hardware resource size to scale the required number of devices or sites. 

 For any installation support, contact Customer Support or the
 Product Management team. 

 For 10 sites/20 Devices : 

 CPU: 8 Cores CPU. 
 2nd Generation Intel® Xeon® Sandy Bridge or later OR Tiger Lake or later
 Celeron or Pentium processor. 

 AMD® x86-64 Bulldozer or later. 

 2.10Ghz Base Frequency/3.90Ghz Boost frequency or better. 

 Memory: 64 GB DDR4 - 3200 MHz. 

 Storage size: 500 GB SSD. 

 Storage performance: 500 IOPS. 

 Networking: 1GE NIC. 

 For 500 Sites/1000 Devices : 

 CPU: 64 Cores CPU. 
 2nd Generation Intel® Xeon® Sandy Bridge or later OR Tiger Lake or later
 Celeron or Pentium processor. 

 AMD® x86-64 Bulldozer or later. 

 2.10 Ghz Base Frequency/3.90 Ghz Boost frequency or better. 

 Memory: 256 GB DDR4 - 3200 MHz. 

 Storage size: 4 TB SSD. 

 Storage performance: 1200 IOPS. 

 Networking: 1 GE NIC. 

 For 1000 sites, the assumption for the hardware scaling
 requirement is 65 flows/10sec per device. 

 9 Nodes HA Setup 

 App Nodes (3) 
 CPU: 32 Cores CPU 

 Memory:128 GB 

 Storage Size: 400 GB 

 Storage performance: 1000 IOPS 

 Stats Nodes (3) 
 CPU: 24 Cores CPU 

 Memory: 160 GB 

 Storage Size: 3600 GB 

 Storage performance: 1800 IOPS 

 Ops Nodes (3) 
 CPU: 8 Cores CPU 

 Memory: 16 GB 

 Storage Size: 300 GB 

 Storage performance: 500 IOPS 

 3 Nodes non-HA Setup 

 App Node (1) 
 CPU: 16 Cores 

 Memory: 64 GB 

 Storage Size: 250 GB 

 Storage performance: 500 IOPS 

 Stats Node (1) 
 CPU: 6 Cores 

 Memory: 40 GB 

 Storage Size: 800 GB 

 Storage performance: 900 IOPS 

 Ops Nodes (1) 
 CPU: 4 Core 

 Memory: 8 GB 

 Storage Size: 200 GB 

 Storage performance: 500 IOPS 

 Multiple Node Set Up for HA 

 The on-premises controller supports high availability (HA) topology with multiple
 nodes, in addition to the single-node deployment. For the HA deployment, you need a
 minimum of 9 servers for a nine-node deployment. This deployment supports controller
 HA in the form of clustering for both scalability and enhanced resiliency. 

 You cannot convert a single-node deployment to a multiple-node HA
 deployment. The HA multi-node deployment requires a new installation from scratch.
 If you select a single-node template during installation, you will need to reinstall
 the entire controller from scratch to later migrate to HA. Plan your deployment
 topology before installing. Refer to system requirements for the HA
 deployment. 

 The 9 nodes are: 

 3 Application nodes —used for core controller and management
 services. 

 3 Operator nodes —used for device software management, onboarding the
 devices, and monitoring the management services. 

 3 Statistics nodes —used for statistics of all devices such as CPU,
 memory, link quality, bandwidth, throughput, and so on. 

 You must connect the hosts on the same LAN/VLAN and provision a network load
 balancer. 

 The HA deployment architecture is: 

 Previous 

 Overview of On-Premises Controller 

 Next 

 Understand Installation Workflow 

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

 Deployment 

 Prisma SASE 

 Prisma SD-WAN 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

---
url: https://docs.paloaltonetworks.com/panorama/getting-started/set-up-panorama/set-up-the-m-series-appliance/m-series-appliance-interfaces
fetched_at: 2026-08-13T17:18:28Z
source: palo-alto-main
---

# M-Series Appliance Interfaces Clear

M-Series Appliance Interfaces 

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

 M-Series Appliance Interfaces 

 Updated on 

 Tue Jul 14 08:53:35 PDT 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Panorama Docs 

 Getting Started 

 Administration 

 New Features 

 Updated on 

 Tue Jul 14 08:53:35 PDT 2026 

 Focus 

 Home 

 Panorama 

 Set Up Panorama 

 Set Up the M-Series Appliance 

 M-Series Appliance Interfaces 

 Download PDF 

 Panorama 

 M-Series Appliance Interfaces 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Panorama Docs 

 Getting Started 

 Administration 

 New Features 

 Previous 

 Set Up the M-Series Appliance 

 Next 

 Perform Initial Configuration of the M-Series Appliance 

 M-Series Appliance Interfaces 

 Where Can I Use This? What Do I Need? 

 NGFW (Managed by Panorama) 

 M-series hardware appliance 

 The Panorama M-700, M-600, M-300, and M-200 appliances have several interfaces for communicating
 with other systems such as managed firewalls and the client systems of Panorama
 administrators. Panorama communicates with these systems to perform various services,
 including managing devices (firewalls, Log Collectors, and WildFire appliances and
 appliance clusters), collecting logs, communicating with Collector Groups, deploying
 software and content updates to devices, and providing administrative access to
 Panorama. By default, Panorama uses its management (MGT) interface for all these
 services. However, you can improve security by reserving the MGT interface for
 administrative access and dedicating separate interfaces for the other services. In a
 large-scale network with multiple subnetworks and heavy log traffic, using multiple
 interfaces for device management and log collection also enables network segmentation
 and load balancing (see Configure Panorama to Use Multiple Interfaces ). 

 When assigning Panorama services to various interfaces, keep in mind that only the MGT interface
 allows administrative access to Panorama for configuration and monitoring tasks. You can
 assign any interface to the other services when you Perform Initial Configuration of the M-Series Appliance . The M-Series Appliance Hardware Reference Guides explain where to attach cables
 for the interfaces. 

 The M-Series appliances, with the exception of the M-700,
do not support Link Aggregation Control Protocol (LACP) for aggregating
interfaces. The M-700 supports LACP for aggregate interface bond1. 

 Supported Interfaces 

 Interfaces can be used for device management, log collection, Collector
Group communication, licensing and software updates. See Configure Panorama to Use Multiple Interfaces for more information on
network segmentation. 

 Interface 

 Maximum Speed 

 M-700 Appliance 

 M-600 Appliance 

 M-300 Appliance 

 M-200 Appliance 

 Management (MGT) 

 1Gbps 

 — 

 — 

 10Gbps 

 — 

 — 

 Ethernet 1 (Eth1) 

 1Gbps 

 — 

 — 

 10Gbps 

 — 

 — 

 Ethernet 2 (Eth2) 

 1Gbps 

 — 

 — 

 Ethernet 3 (Eth3) 

 1Gbps 

 — 

 — 

 Ethernet 4 (Eth4) 

 10Gbps 

 — 

 — 

 — 

 Ethernet 5 (Eth5) 

 10Gbps 

 — 

 — 

 — 

 The M-700 Appliance has two ports on its back panel labeled Ethernet 1/2 and
 Ethernet 1/3; however, the appliance uses a 20Gb aggregate software interface
 called bond1 instead of separate Eth2 and Eth3
 subinterfaces. 

 Logging Rates 

 Review the logging rates for the all M-Series appliance models. To achieve the logging rates
 listed below, the M-Series appliance must be a single log collector in a collector
 group and you must install all the logging disks for your M-Series model. 

 Model Capacities and Features 

 M-700 Appliance 

 M-600 Appliance 

 M-300 Appliance 

 M-200 Appliance 

 Maximum Logging Rate for Panorama in Management Only mode 

 Local log storage is not supported 

 Maximum Logging Rate for Panorama in Panorama Mode 

 36,500 logs/second 

 25,000 logs/second 

 16,500 logs/second 

 10,000 logs/second 

 Maximum Logging Rate for Panorama in Log Collector Mode 

 73,000 logs/second 

 50,000 logs/second 

 33,000 logs/second 

 28,000 logs/second 

 Maximum Log Storage on Appliance 

 48TB (12x8TB RAID disk) 

 48TB (12x8TB RAID disk) 

 16TB (4x8TB RAID disk) 

 16TB (4x8TB RAID disk) 

 Default Log Storage on Appliance 

 16TB (4x8TB RAID disks) 

 16TB (4x8TB RAID disks) 

 16TB (4x8TB RAID disks) 

 16TB (4x8TB RAID disks) 

 SSD Storage on Appliance (for logs that M-Series appliances
 generate) 

 240GB 

 240GB 

 240GB 

 240GB 

 NFS Attached Log Storage 

 Not available 

 Previous 

 Set Up the M-Series Appliance 

 Next 

 Perform Initial Configuration of the M-Series Appliance 

 On This Page 

 Activation and Onboarding 

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

 Panorama 

 Service Provider 

 VM-Series 

 Plugins 

 SASE 

 Prisma Access 

 Prisma SASE Multitenant Platform 

 AI-Powered ADEM 

 Prisma Access Monitoring & Visibility 

 Prisma SD-WAN 

 ION Devices 

 Next-Generation CASB 

 Cloud-Delivered Security Services 

 Advanced WildFire 

 Advanced URL Filtering 

 Advanced Threat Prevention 

 Advanced DNS Security 

 AI Access Security 

 Device Security 

 Enterprise DLP 

 SaaS Security 

 Network Security 

 Shared Policy for NGFWs and Prisma Access 

 IPSec VPN 

 Security Policy 

 Quantum Security 

 Endpoints 

 GlobalProtect 

 Remote Browser Isolation 

 Prisma Access Agent 

 Visibility & Monitoring 

 Dashboards 

 Incidents and Alerts 

 Reports 

 Autonomous DEM 

 FedRAMP 

 Prisma SASE for FedRAMP 

 Autonomous DEM for FedRAMP 

 Prisma SD-WAN Experts Corner 

 Network Policy 

 QoS Whitepaper 

 Security Architecture Whitepaper 

 External Antennas for ION-C Series 

 Dynamic Path Selection 

 Best Practices 

 Best Practices Library 

 Experts Corner 

 Solutions Docs from Product Experts 

 Resources 

 All Products A - Z 

 All Release Notes 

 Compatibility Matrix 

 Experts Corner 

 Network Security Platform 

 Security Policy 

 Decryption 

 Device-ID 

 IPSec VPN 

 Quality of Service 

 Quantum Security 

 11.1 & Later 

 Next-Generation Firewall 

 Getting Started 

 Panorama 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

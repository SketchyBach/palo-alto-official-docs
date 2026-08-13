---
url: https://docs.paloaltonetworks.com/panorama/getting-started/set-up-panorama/set-up-the-m-series-appliance/configure-panorama-to-use-multiple-interfaces/multiple-interfaces-for-network-segmentation-example
fetched_at: 2026-08-13T17:18:27Z
source: palo-alto-main
---

# Multiple
Interfaces for Network Segmentation Example Clear

Multiple
Interfaces for Network Segmentation Example 

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

 Multiple
Interfaces for Network Segmentation Example 

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

 Configure Panorama to Use Multiple Interfaces 

 Multiple
Interfaces for Network Segmentation Example 

 Download PDF 

 Panorama 

 Multiple
Interfaces for Network Segmentation Example 

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

 Configure Panorama to Use Multiple Interfaces 

 Next 

 Configure Panorama for Network Segmentation 

 Multiple
Interfaces for Network Segmentation Example 

 Where Can I Use This? What Do I Need? 

 NGFW (Managed by Panorama) 

 M-series hardware appliance 

 Figure 1 illustrates
a deployment that uses multiple interfaces on M-500 appliances in Panorama
mode and Log Collector mode. In this example, the interfaces support network
segmentation as follows: 

 Panorama management network —To protect the Panorama
web interface, CLI, and XML API from unauthorized access, the MGT
interface on Panorama connects to a subnetwork that only administrators
can access. 

 Internet —Panorama uses the MGT interface to communicate
with external services such as the Palo Alto Networks Update Server. 

 Perimeter Gateway and Data Center —Panorama
uses a separate pair of interfaces to manage the firewalls and Log Collectors
in each of these subnetworks. Managing firewalls typically generates less
traffic than querying Log Collectors for report information. Therefore, Panorama
uses 1Gbps interfaces (Eth1 and Eth2) for managing the firewalls
and uses 10Gbps interfaces (Eth4 and Eth5) for querying and managing
the Log Collectors. Each Log Collector uses its MGT interface to
respond to the queries but uses its Eth4 and Eth5 interfaces for
the heavier traffic associated with collecting logs from the firewalls. 

 Software and content updates —The firewalls and Log
Collectors in both subnetworks retrieve software and content updates
over the Eth3 interface on Panorama. 

 Multiple Panorama Interfaces 

 Previous 

 Configure Panorama to Use Multiple Interfaces 

 Next 

 Configure Panorama for Network Segmentation 

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

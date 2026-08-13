---
url: https://docs.paloaltonetworks.com/prisma-access/integration/integrate-third-party-sd-wans-with-prisma-access/aryaka-sd-wan-solution-guide
fetched_at: 2026-08-13T17:26:44Z
source: palo-alto-main
---

# Aryaka SD-WAN Solution Guide Clear

Aryaka SD-WAN Solution Guide 

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

 Aryaka SD-WAN Solution Guide 

 Updated on 

 Thu Mar 26 14:01:29 PDT 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma Access Docs 

 Release Notes 

 Select a Document 

 6.2 Preferred and Innovation 

 6.1 Preferred and Innovation 

 6.0 Preferred and Innovation 

 5.2 Preferred and Innovation 

 5.1 Preferred and Innovation 

 5.0 Preferred and Innovation 

 4.2 Preferred 

 4.1 Preferred 

 4.0 Preferred 

 3.2 Preferred and Innovation 

 Activation & Onboarding 

 Administration 

 Select a Document 

 4.0 & Later 

 Prisma Access China 

 Integrations 

 Incidents & Alerts 

 New Features 

 Updated on 

 Thu Mar 26 14:01:29 PDT 2026 

 Focus 

 Home 

 Prisma Access 

 Integrate Third-Party SD-WANs with Prisma Access 

 Aryaka SD-WAN Solution Guide 

 Download PDF 

 Prisma Access 

 Aryaka SD-WAN Solution Guide 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma Access Docs 

 Release Notes 

 Select a Document 

 6.2 Preferred and Innovation 

 6.1 Preferred and Innovation 

 6.0 Preferred and Innovation 

 5.2 Preferred and Innovation 

 5.1 Preferred and Innovation 

 5.0 Preferred and Innovation 

 4.2 Preferred 

 4.1 Preferred 

 4.0 Preferred 

 3.2 Preferred and Innovation 

 Activation & Onboarding 

 Administration 

 Select a Document 

 4.0 & Later 

 Prisma Access China 

 Integrations 

 Incidents & Alerts 

 New Features 

 Previous 

 Integrate Prisma Access with Aruba SD-WAN 

 Next 

 Integrate Prisma Access with Aryaka SD-WAN 

 Aryaka SD-WAN Solution Guide 

 Integrate an Aryaka SD-WAN with Prisma Access. 

 Where Can I Use This? What Do I Need? 

 Prisma Access (Managed by Strata Cloud Manager) 

 Prisma Access (Managed by Panorama) 

 Prisma Access license 

 Aryaka SmartConnect subscription 

 Aryaka and Prisma Access seamlessly integrate to deliver a joint solution of a
 cloud-native global SD-WAN that includes private connectivity, WAN optimization, and
 application acceleration capabilities with a next-generation security platform that
 provides a consistent level of security in both physical and virtual environments. 

 Aryaka's SmartConnect delivers service level agreement (SLA)-based reliable global
 connectivity and faster application performance for both on-premises and cloud/SaaS
 applications, while Prisma Access adds a layer of advanced security controls required
 for internet- and cloud-bound traffic. 

 The Aryaka edge device, Aryaka Network Access Point (ANAP), can seamlessly forward all
 internet traffic from branch locations to Prisma Access using a secure IPSec tunnel. 

 Together, Aryaka and Prisma Access deliver a best-of-breed SD-WAN and security platform
 for enterprises accessing mission-critical internally hosted applications, as well
 accessing cloud applications using the internet. 

 This solution guide provides you with the tasks you perform to integrate a branch
 location using Aryaka SmartConnect with Prisma Access. 

 Supported IKE and IPSec Cryptographic Profiles 

 You onboard your SD-WAN edge devices using a remote network connection between the
 edge device at the branch site, HQ, or hub to Prisma Access. To do this you will
 onboard a remote network, ensuring that you use supported IKE and IPSec
 cryptographic settings. 

 The following table documents the IKE/IPSec crypto settings that are supported with
 Prisma Access and the Aryaka SD-WAN. In addition, the supported architecture types
 are listed at the end of the table. A check mark indicates that the profile or
 architecture type is supported; a dash (—) indicates that it's not supported.
 Default and Recommended settings are noted in the table. 

 Crypto Profiles Prisma Access Aryaka SmartConnect 

 Tunnel Type IPSec Tunnel 

 √ 

 √ 

 GRE Tunnel — — 

 Routing Static Routes 

 √ 

 √ 

 Dynamic Routing (BGP) 

 √ 

 — 

 Dynamic Routing (OSPF) — — 

 IKE Versions IKE v1 

 √ 

 √ 

 IKE v2 

 √ 

 — 

 IPSec Phase 1 DH-Group Group 1 

 √ 

 — 

 Group 2 
 √ 
 (Default) 
 √ 
 (Default) 

 Group 5 

 √ 

 √ 

 Group 14 

 √ 

 √ 

 Group 19 

 √ 

 — 

 Group 20 
 √ 
 (Recommended) — 

 IPSec Phase 1 Auth 
 If you use
 IKEv2 with certificate-based authentication, only SHA1 is
 supported in IKE crypto profiles (Phase 1). 
 MD5 

 √ 

 √ 

 SHA1 
 √ 
 (Default) 
 √ 
 (Default) 

 SHA256 

 √ 

 √ 

 SHA384 

 √ 

 √ 

 SHA512 
 √ 
 (Recommended) 

 √ 

 IPSec Phase 1 Encryption DES 

 √ 

 — 

 3DES 
 √ 
 (Default) 

 √ 

 AES-128-CBC 
 √ 
 (Default) 
 √ 
 (Default) 

 AES-192-CBC 

 √ 

 — 

 AES-256-CBC 
 √ 
 (Recommended) — 

 IPSec Phase 1 Key Lifetime Default 
 √ 
 (8 Hours) 
 √ 
 (8 Hours) 

 IPSec Phase 1 Peer
 Authentication Pre-Shared Key 

 √ 

 √ 

 Certificate 

 √ 

 — 

 IKE Peer Identification FQDN 

 √ 

 √ 

 IP Address 

 √ 

 √ 

 User FQDN 

 √ 

 — 

 IKE Peer As Static Peer 

 √ 

 √ 

 As Dynamic Peer 

 √ 

 — 

 Options NAT Traversal 

 √ 

 √ 

 Passive Mode 

 √ 

 — 

 Ability to Negotiate
 Tunnel Per Subnet Pair 

 √ 

 — 

 Per Pair of Hosts 

 √ 

 — 

 Per Gateway Pair 

 √ 

 — 

 IPSec Phase 2 DH-Group Group 1 

 √ 

 — 

 Group 2 
 √ 
 (Default) 
 √ 
 (Default) 

 Group 5 

 √ 

 √ 

 Group 14 

 √ 

 √ 

 Group 19 

 √ 

 — 

 Group 20 
 √ 
 (Recommended) — 

 No PFS 

 √ 

 √ 

 IPSec Phase 2 Auth MD5 

 √ 

 — 

 SHA1 
 √ 
 (Default) 
 √ 
 (Default) 

 SHA256 

 √ 

 √ 

 SHA384 

 √ 

 √ 

 SHA512 
 √ 
 (Recommended) 

 √ 

 None 

 √ 

 √ 

 IPSec Phase 2 Encryption DES 

 √ 

 — 

 3DES 
 √ 
 (Default) 

 √ 

 AES-128-CBC 
 √ 
 (Default) 

 √ 

 AES-192-CBC 

 √ 

 — 

 AES-256-CBC 

 √ 

 — 

 AES-128-CCM 

 √ 

 — 

 AES-128-GCM 

 √ 

 — 

 AES-256-GCM 
 √ 
 (Recommended) — 

 NULL 

 √ 

 √ 

 IPSec Protocol ESP 

 √ 

 √ 

 AH 

 √ 

 — 

 IPSec Phase 2 Key Lifetime Default 
 √ 
 (1 Hour) 
 √ 
 (1 Hour) 

 Tunnel Monitoring
 Fallback Dead Peer Detection (DPD) 

 √ 

 √ 

 ICMP — — 

 Bidirectional Forwarding Detection (BFD) — — 

 SD-WAN Architecture Type With Regional Hub/Gateway/Data Center N/A 

 √ 

 No Regional Hub/Gateway/Data Center NA 

 √ 

 Previous 

 Integrate Prisma Access with Aruba SD-WAN 

 Next 

 Integrate Prisma Access with Aryaka SD-WAN 

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

 Hardware Reference 

 ION 1000 

 ION 1200 

 ION 1200-S 

 ION 2000 

 ION 3000 

 ION 3200 

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

 ION 5200 

 ION 9200 

 Virtual ION Deployment 

 Virtual ION on AWS 

 Virtual ION on Azure 

 Virtual ION on GCP 

 Virtual ION on KVM for NFV 

 Virtual ION on OCI 

 Virtual ION on VMware 

 3rd Party Integrations 

 AWS Cloud-WAN Integration (GRE Connect) 

 AWS Cloud-WAN Integration (Tunnel-less Connect) 

 Checkpoint Integration 

 LiveAction Integration 

 Netskope Integration 

 Symantec Web Security Services Integration 

 Best Practices 

 Best Practices Library 

 Experts Corner 

 Solutions Docs from Product Experts 

 Panorama 

 Prisma Access 

 SASE 

 Integrations 

 Strata Cloud Manager 

 Prisma SASE 

 4.0 & Later 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

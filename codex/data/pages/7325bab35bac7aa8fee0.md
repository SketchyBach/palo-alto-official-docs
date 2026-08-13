---
url: https://docs.paloaltonetworks.com/prisma-sd-wan/ion-cli-reference/use-cli-commands/inspect-commands/inspect-servicelink-sa
fetched_at: 2026-08-13T17:31:03Z
source: palo-alto-main
---

# inspect servicelink SA Clear

inspect servicelink SA 

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

 inspect servicelink SA 

 Updated on 

 Tue Jun 02 09:34:24 PDT 2026 

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

 Tue Jun 02 09:34:24 PDT 2026 

 Focus 

 Home 

 Prisma SD-WAN 

 Use CLI Commands 

 Inspect Commands 

 inspect servicelink SA 

 Download PDF 

 Prisma SD-WAN 

 inspect servicelink SA 

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

 inspect servicelink SA 

 Use the inspect servicelink SA command to inspect the security
 association (SA) of VPN tunnels. Information displayed includes the Proposals selected
 —DH Group, Encryption, Hash/PRF. 

 Command 

 inspect servicelink SA ( all | sldev= | slname= ) 

 Options 

 all Enter all to view the parameters for all the VPN
 paths for a device. 

 sldev Enter the VPN ID to view the parameters for a
 specific VPN. 

 slname Enter the VPN interface name to view the parameters
 for a specific VPN. 

 Command Notes 

 Role Super, Read Only 

 Related Commands — 

 Introduced in Release 6.5.1 

 Example 

 inspect servicelink SA all
sl1: #21, ESTABLISHED, IKEv2, 408897e92ca70524_i* c78d678376b34f53_r
 local '10.65.27.23' @ 10.65.27.23[4501]
 remote '10.65.27.44' @ 10.65.27.44[4500]
 AES_GCM_16-256/PRF_HMAC_SHA2_256/MODP_1024
 established 3893s ago, rekeying in 81983s, reauth in 81067s
 sl1childsa: #3, reqid 2, INSTALLED, TUNNEL, ESP:AES_GCM_16-256
 installed 3893s ago, rekeying in 23562s, expires in 24908s
 in 961cb37a (-|0x00004e21), 14346 bytes, 223 packets
 out ccdc94a8 (-|0x00004e21), 23402 bytes, 380 packets
 local 0.0.0.0/0
 remote 0.0.0.0/0
sl2: #1, ESTABLISHED, IKEv2, 41f62fa9e70fa572_i* 883349dcb0cd961d_r
 local '10.65.27.23' @ 10.65.27.23[4501]
 remote '10.65.27.43' @ 10.65.27.43[4500]
 AES_CBC-256/HMAC_SHA2_256_128/PRF_HMAC_SHA2_256/MODP_1024
 established 4589s ago, rekeying in 81576s, reauth in 80364s
 sl2childsa: #1, reqid 1, INSTALLED, TUNNEL, ESP:AES_CBC-256/HMAC_SHA2_256_128
 installed 4589s ago, rekeying in 22746s, expires in 24211s
 in a361f4b0 (-|0x00004e22), 19888 bytes, 318 packets
 out cc02094c (-|0x00004e22), 29367 bytes, 477 packets
 local 0.0.0.0/0
 remote 0.0.0.0/0 

 inspect servicelink SA sldev=sl1
sl1: #21, ESTABLISHED, IKEv2, 408897e92ca70524_i* c78d678376b34f53_r
 local '10.65.27.23' @ 10.65.27.23[4501]
 remote '10.65.27.44' @ 10.65.27.44[4500]
 AES_GCM_16-256/PRF_HMAC_SHA2_256/MODP_1024
 established 3846s ago, rekeying in 82030s, reauth in 81114s
 sl1childsa: #3, reqid 2, INSTALLED, TUNNEL, ESP:AES_GCM_16-256
 installed 3846s ago, rekeying in 23609s, expires in 24955s
 in 961cb37a (-|0x00004e21), 14223 bytes, 221 packets
 out ccdc94a8 (-|0x00004e21), 23039 bytes, 374 packets
 local 0.0.0.0/0
 remote 0.0.0.0/0 

 inspect servicelink SA slname=ToSV2
sl1: #21, ESTABLISHED, IKEv2, 408897e92ca70524_i* c78d678376b34f53_r
 local '10.65.27.23' @ 10.65.27.23[4501]
 remote '10.65.27.44' @ 10.65.27.44[4500]
 AES_GCM_16-256/PRF_HMAC_SHA2_256/MODP_1024
 established 3838s ago, rekeying in 82038s, reauth in 81122s
 sl1childsa: #3, reqid 2, INSTALLED, TUNNEL, ESP:AES_GCM_16-256
 installed 3838s ago, rekeying in 23617s, expires in 24963s
 in 961cb37a (-|0x00004e21), 14100 bytes, 219 packets
 out ccdc94a8 (-|0x00004e21), 22916 bytes, 372 packets
 local 0.0.0.0/0
 remote 0.0.0.0/0 

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

 CLI 

 Reference 

 Prisma SD-WAN ION CLI Reference 

 SASE 

 Prisma SD-WAN 

 Prisma SASE 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

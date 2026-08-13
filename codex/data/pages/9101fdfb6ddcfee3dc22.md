---
url: https://docs.paloaltonetworks.com/prisma-sd-wan/ion-cli-reference/use-cli-commands/inspect-commands/inspect-servicelink-connection
fetched_at: 2026-08-13T17:31:03Z
source: palo-alto-main
---

# inspect servicelink conn Clear

inspect servicelink conn 

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

 inspect servicelink conn 

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

 inspect servicelink conn 

 Download PDF 

 Prisma SD-WAN 

 inspect servicelink conn 

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

 inspect servicelink conn 

 Use the inspect servicelink conn command to inspect the active VPN
 connections. Information includes the authentication selected, Internet Key Exchange
 (IKE) protocol details, and Dead Peer Detection (DPD) details. 

 Command 

 inspect servicelink conn ( all | sldev= | slname= ) 

 Options 

 all Enter all to view all the active VPN connections for
 a device. 

 sldev Enter the VPN ID to view the parameters for a
 specific active VPN. 

 slname Enter the VPN interface name to view the parameters
 for a specific active VPN. 

 Command Notes 

 Role Super, Read Only 

 Related Commands — 

 Introduced in Release 6.5.1 

 Example 

 inspect servicelink conn all
sl2: IKEv2, reauthentication every 86400s, rekeying every 86400s, dpd delay 1s
 local: 10.65.27.23
 remote: 10.65.27.43
 local pre-shared key authentication:
 id: 10.65.27.23
 remote pre-shared key authentication:
 id: %any
 sl2childsa: TUNNEL, rekeying every 27900s, dpd action is start
 local: 0.0.0.0/0
 remote: 0.0.0.0/0
sl1: IKEv2, no reauthentication, rekeying every 86400s, dpd delay 1s
 local: 10.65.27.23
 remote: 10.65.27.44
 local pre-shared key authentication:
 id: 10.65.27.23
 remote pre-shared key authentication:
 id: %any
 sl1childsa: TUNNEL, rekeying every 27900s, dpd action is start
 local: 0.0.0.0/0
 remote: 0.0.0.0/0

 inspect servicelink conn sldev=sl1
sl1: IKEv2, no reauthentication, rekeying every 86400s, dpd delay 1s
 local: 10.65.27.23
 remote: 10.65.27.44
 local pre-shared key authentication:
 id: 10.65.27.23
 remote pre-shared key authentication:
 id: %any
 sl1childsa: TUNNEL, rekeying every 27900s, dpd action is start
 local: 0.0.0.0/0
 remote: 0.0.0.0/0 

 inspect servicelink conn slname=ToSV2
sl1: IKEv2, no reauthentication, rekeying every 86400s, dpd delay 1s
 local: 10.65.27.23
 remote: 10.65.27.44
 local pre-shared key authentication:
 id: 10.65.27.23
 remote pre-shared key authentication:
 id: %any
 sl1childsa: TUNNEL, rekeying every 27900s, dpd action is start
 local: 0.0.0.0/0
 remote: 0.0.0.0/0 

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

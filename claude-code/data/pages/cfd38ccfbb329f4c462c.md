---
url: https://docs.paloaltonetworks.com/prisma-access/administration/ztna-connector-in-prisma-access/ztna-connector-server-initiated-traffic
fetched_at: 2026-08-13T17:25:47Z
source: palo-alto-main
---

# ZTNA Connector Server Initiated Traffic Clear

ZTNA Connector Server Initiated Traffic 

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

 ZTNA Connector Server Initiated Traffic 

 Updated on 

 Mon Aug 10 14:01:14 PDT 2026 

 Focus 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 Deutsch (German) 

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

 Mon Aug 10 14:01:14 PDT 2026 

 Focus 

 Home 

 Prisma Access 

 Prisma Access Administration 

 Prisma Access ZTNA Connector 

 ZTNA Connector Server Initiated Traffic 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 Deutsch (German) 

 Prisma Access 

 ZTNA Connector Server Initiated Traffic 

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

 Private AWS Application Target Discovery 

 Next 

 Security Policy for Apps Enabled with ZTNA Connector 

 ZTNA Connector Server Initiated Traffic 

 Enabling server-initiated traffic on ZTNA Connector Groups. 

 Where Can I Use This? What Do I Need? 

 Prisma Access (Managed by Strata Cloud Manager) 

 We require a minimum version of Prisma Access 5.0 to
 enable ZTNA Connector support. 

 Prisma Access license includes 10 connectors, 20,000
 FQDNs, and 1024 IP subnets. This functionality is provided
 for the purpose of trying out ZTNA Connectors in your
 environment. 

 The Private App add-on license
 includes 200 ZTNA Connectors, 20,000 FQDNs, and 1024 IP subnet
 functionality. 

 ZTNA Connector is a critical component of the Zero Trust security offering, providing
 secure access to your private applications. To deliver a comprehensive and flexible
 security solution, the ZTNA Connector has been enhanced to support server-initiated
 traffic flow . Now, applications running in your data center can initiate
 connections to clients across the Prisma Access ® 
 fabric. 

 When you enable server-initiated traffic on a ZTNA Connector Group, it establishes a
 bidirectional communication capability. Your data center servers can now establish
 TCP, UDP, and ICMP sessions to the following destinations: 
 GlobalProtect users connected to a GlobalProtect gateway 

 Remote network hosts 

 IP subnet hosts in other ZTNA Connector data centers 
 This functionality is essential for applications such as remote troubleshooting,
 device inventory and patch distribution systems, and Voice Over IP (VoIP) applications.
 All server-initiated traffic flows are Source NATed (SNAT) using the ZTNA Connector's
 IPSec tunnel IP address (this address is from the /27 prefix that the connector got from
 the connector IP blocks), therefore mobile user/remote network destinations don't need
 private data center IP prefixes in their routing tables. 

 The data center router can learn the routes into the Prisma Access 
 network through the data center connectors in two ways: 

 Static route configuration— Users manually enters all the destination prefixes with
 ZTNA Connector IP addresses as next-hops. 

 Dynamic BGP routing— ZTNA Connector automatically advertises the destination
 prefixes to the data center router though a BGP peering connection. 

 Server-initiated traffic reduces operational complexity while maintaining network
 integrity. 

 Server-initiated traffic establishes server-to-client flows; for optimal organization and
 management. Palo Alto Networks recommends that the client-initiated flows and
 server-initiated traffic flows should be configured in separate ZTNA Connector
 Groups. 

 Upon receiving the flow, ZTNA Connector first performs a route check based on the
 configured destination prefix security rule (the union of MU Pools, RN Prefixes, and
 ZTNA IP Subnet targets). If permitted, the Connector then performs Source NAT
 (SNAT) , translating the data center server's IP to the ZTNA Connector's IPSec
 tunnel interface IP. The SNATed traffic is then routed through the Prisma Access Fabric
 towards the destination endpoint. You are responsible for enforcing any necessary
 security policy on traffic after it exits Prisma Access . Finally,
 the GP User or RN Host receives the connection, with the source appearing as the ZTNA
 Connector's IPSec IP, and return traffic naturally follows the reverse path back to the
 SNAT address, maintaining path symmetry. 

 Prerequisties 
 Onboard the Connector . 

 Upgrade the Connector with 6.2.8-ztna-connector-b1 image. 

 Configure server-initiated traffic using the following steps: 
 Go to Configuration ZTNA Connector Connector Groups and select the Connector Group. 

 Select Settings and Enable Server Initiated
 Traffic . 

 Configure the Destinations for server-initiated
 traffic: 
 If you want to enable server-initiated connections to GlobalProtect users, select the
 Mobile User Pools checkbox to allow access to
 all mobile user pools. 

 If you want to enable server-initiated connections to hosts on remote
 networks, select the Remote Network Pools 
 checkbox and enter the specific IP subnets within the remote network to
 allow access. 

 If you want to server-initiated connections to destinations in another
 ZTNA Connector group's IP subnet targets, select the ZTNA
 Connector Data Center checkbox, and then select the IP
 subnet(s) to allow access. 

 Currently, there
 is no support for ZTNA Connector FQDN targets. 

 Go to Routing and select the settings icon. Under
 Connectors with Server Initiated Traffic Enabled ,
 select the Connector for which you want to configure the data center routing.

 You can select routing as either
 Dynamic or
 Static . 

 Select the Routing Type as
 Dynamic or Static : 
 For Dynamic : add AS
 Number , Peer AS ,
 Peer IP Address , and
 Secret , if required. 

 For Static : configure the mobile users
 prefixes, remote network prefixes and ZTNA Connector prefixes at
 the data center router where ZTNA connectors and this group
 reside. 

 When using static
 routing, you must configure every router involved to forward
 traffic through the connectors. 

 The server-initiated connections make flow logs in the ZTNA Connector and the
 destination mobile user, remote network, or the other ZTNA Connector. You can
 view the ZTNA Connector logs . 

 Previous 

 Private AWS Application Target Discovery 

 Next 

 Security Policy for Apps Enabled with ZTNA Connector 

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

 SASE 

 Administration 

 Prisma Access 

 6.1 Preferred and Innovation 

 Prisma SASE 

 Prisma Access 

 Strata Cloud Manager 

 4.0 & Later 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

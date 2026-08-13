---
url: https://docs.paloaltonetworks.com/prisma-sd-wan/ion-cli-reference/use-cli-commands/dump-commands/dump-routing-ospf-vrf
fetched_at: 2026-08-13T17:30:29Z
source: palo-alto-main
---

# dump routing ospf Clear

dump routing ospf 

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

 dump routing ospf 

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

 Dump Commands 

 dump routing ospf 

 Download PDF 

 Prisma SD-WAN 

 dump routing ospf 

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

 dump routing multicast status 

 Next 

 dump routing peer advertised routes 

 dump routing ospf 

 Use the dump routing ospf command to display the open shortest
 path first (OSPF) specific configurations of a device. 

 Command 

 dump routing ospf ( global-config | vrf ( config | interface = <all | interface name | neighbor | statistics> | routes | database | discovered-neighbors | reachable-prefixes ) 

 Options 

 global-config Enter global-config to see all the configured and managed OSPF
 global settings/parameters. 

 vrf Enter vrf to see all the attached VRFs Global and
 customised). 

 config Enter config to know all the VRF specific
 configurations of a device. 

 interface Enter interface name or all to know the interfaces on
 which ospf traffic is forwarded or replicated. 
 neighbor: Displays
 the router ID of the router (neighbor) on the other side of the
 virtual link. 

 statistics: Displays the statistics of the
 routes. 

 routes Enter routes to see all the routes of the network,
 router, and external routing table of the OSPF. 

 database Enter database to see the 

 discovered-neighbors Enter discovered-neighbors to know the two
 OSPF-enabled routers connected by a shared network and in the same
 OSPF area form a relationship and are OSPF neighbors. 

 reachable-prefixes 

 Command Notes 

 Role Super, Read Only, Monitor 

 Related Commands 

 clear routing ospf 

 Introduced in Release 6.4.1 

 Example 

 dump routing ospf global-config 
ID : 1707121524214025528
Router ID : 40.40.40.50
Cost : 
Dead Interval : 40
Hello Interval : 10
Retransmit Interval : 5
Md5 Secret : 
Md5 KeyID : 
Prefix Advertisement Type : default
Transmit Delay : 1

 dump routing ospf vrf Global config 
Name : G
Description : 
Tags : 
Scope : global
VRF : Name - Global, Vni - 0, ID - 1695187971257016928
Config ID : 1713256072536012828
Shutdown : false
Router ID : 
Prefix Advertisement Type : unaggregated
Prefix Advertisement Route-map : 
BGP Prefix Redistribution : false
BGP Prefix Redistribution Route-map : 
Areas
+----------------------+----------------------+
| Area ID | Area Type |
+----------------------+----------------------+
| 0 | normal |
+----------------------+----------------------+
Interfaces
+------------------------------------------+---------------------------+
| Interface | OSPF Config |
+------------------------------------------+---------------------------+
| Interface : 1 (eth1) | Cost: |
| Interface ID: 1706795250766004028 | Dead Interval: 40 |
| Area ID: 0 | Hello Interval: 10 |
| Area Type: normal | Retransmit Interval: 5 |
| | Transmit Delay: 1 |
| | Md5 Secret: qwerty |
| | Md5 KeyID: 1 |
+------------------------------------------+---------------------------+
| Interface : 2.1 (eth2.1) | Cost: |
| Interface ID: 1707583634718019928 | Dead Interval: 40 |
| Area ID: 0 | Hello Interval: 10 |
| Area Type: normal | Retransmit Interval: 5 |
| | Transmit Delay: 1 |
| | Md5 Secret: |
| | Md5 KeyID: |
+------------------------------------------+---------------------------+ 

 dump routing ospf vrf Global interface eth1 neighbor 

Neighbor ID Pri State Dead Time Address Interface RXmtL RqstL DBsmL
1.1.1.1 4 Full/DR 37.813s 22.22.22.2 eth1:22.22.22.22 0 0 0 

 dump routing ospf vrf Global database 
VRF Name: default

 OSPF Router with ID (40.40.40.50)

 Router Link States (Area 0.0.0.0)

Link ID ADV Router Age Seq# CkSum Link count
1.1.1.1 1.1.1.1 619 0x80006b77 0xa00e 2
3.3.3.3 3.3.3.3 572 0x80000359 0xce1c 2
40.40.40.50 40.40.40.50 617 0x80000081 0xff79 2

 Net Link States (Area 0.0.0.0)

Link ID ADV Router Age Seq# CkSum
22.22.22.2 1.1.1.1 569 0x800017f7 0x87cd
33.33.33.1 3.3.3.3 562 0x800002c8 0xa9bf

 AS External Link States

Link ID ADV Router Age Seq# CkSum Route
0.0.0.0 40.40.40.50 465 0x80000087 0xeeb1 E2 0.0.0.0/0 [0x0]
1.1.1.0 40.40.40.50 1128 0x8000005f 0xd9d8 E2 1.1.1.0/24 [0x0]
12.12.12.0 40.40.40.50 465 0x80000001 0x09e6 E2 12.12.12.0/24 [0x0]
13.13.13.0 40.40.40.50 465 0x80000001 0xe408 E2 13.13.13.0/24 [0x0]
22.22.22.0 40.40.40.50 607 0x80000061 0xde92 E2 22.22.22.0/24 [0x0]
33.33.33.0 40.40.40.50 1228 0x8000005f 0x55fc E2 33.33.33.0/24 [0x0] 

 dump routing ospf vrf Global reachable-prefixes 
VRF : Name - Global, ID - 1695187971257016928
OSPF Config ID : 1713256072536012828
Reachable IPv4 Prefixes Count : 2
Redistribute : true
Reachable IPv4 Prefixes
+----------------------+----------------------+
| Network | Nexthop |
+----------------------+----------------------+
| 11.11.11.0/24 | 22.22.22.2 |
| 9.9.9.0/24 | 33.33.33.1 |
+----------------------+----------------------+ 

 Previous 

 dump routing multicast status 

 Next 

 dump routing peer advertised routes 

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

 CLI 

 Reference 

 Prisma SASE 

 Prisma SD-WAN ION CLI Reference 

 Prisma SD-WAN 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

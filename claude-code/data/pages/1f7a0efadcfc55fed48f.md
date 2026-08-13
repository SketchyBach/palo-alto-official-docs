---
url: https://docs.paloaltonetworks.com/prisma-sd-wan/ion-cli-reference/use-cli-commands/inspect-commands/inspect-system-ipv6-neighbor
fetched_at: 2026-08-13T17:31:04Z
source: palo-alto-main
---

# inspect system ipv6-neighbor Clear

inspect system ipv6-neighbor 

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

 inspect system ipv6-neighbor 

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

 inspect system ipv6-neighbor 

 Download PDF 

 Prisma SD-WAN 

 inspect system ipv6-neighbor 

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

 inspect system arp 

 Next 

 inspect system vrf 

 inspect system ipv6-neighbor 

 Use the inspect system ipv6-neighbor command
to inspect all the IPv6 system neighbors. 

 Command 

 inspect system ipv6-neighbor ( all | interface
 interface-name )

 Options 

 all Enter all to inspect all system IPv6 neighbors
for a device. 

 interface Enter interface name to list the names of system
IPv6 neighbors for a device. 

 Command Notes 

 Role Super, Read Only 

 Related Commands — 

 Introduced in Release 6.0.1 

 Example 

 inspect system ipv6-neighbor all
 fe80::250:56ff:fe95:edf dev eth1 lladdr 00:50:56:95:0e:df STALE
 fe80::250:56ff:feab:42c4 dev eth2 lladdr 00:50:56:ab:42:c4 router STALE
 fe80::fcde:feff:fe28:5143 dev eth1 lladdr 00:50:56:95:0e:df router STALE
 fe80::250:56ff:fe95:db52 dev eth1 lladdr 00:50:56:95:db:52 STALE
 fe80::8c61:66ff:fe7a:f943 dev v-ppp1-p lladdr 9e:5a:9a:4d:30:9a PERMANENT
 fe80::700a:a5ff:fe6d:5d55 dev v-eth1-p lladdr ce:92:5f:14:e9:d9 PERMANENT
 2008::33 dev eth1 INCOMPLETE
 fe80::250:56ff:feab:90e5 dev eth2 lladdr 00:50:56:ab:90:e5 router STALE
 2008::55 dev eth1 INCOMPLETE
 fe80::250:56ff:fe88:e61d dev eth1 lladdr 00:50:56:88:e6:1d router STALE 

 Previous 

 inspect system arp 

 Next 

 inspect system vrf 

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

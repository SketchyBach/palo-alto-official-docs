---
url: https://docs.paloaltonetworks.com/prisma-sd-wan/ion-cli-reference/use-cli-commands/inspect-commands/inspect-app-l4-prefix-lookup
fetched_at: 2026-08-13T17:30:50Z
source: palo-alto-main
---

# inspect app-l4-prefix lookup Clear

inspect app-l4-prefix lookup 

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

 inspect app-l4-prefix lookup 

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

 inspect app-l4-prefix lookup 

 Download PDF 

 Prisma SD-WAN 

 inspect app-l4-prefix lookup 

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

 inspect app-flow-table 

 Next 

 inspect app-map 

 inspect app-l4-prefix lookup 

 Use the inspect app-l4-prefix lookup command
to identify lookup on a given destination address in TCPPROXY L4-Prefix-Lookup
table and also configures at the device level. 

 Command 

 inspect app-l4-prefix lookup dstv4=192.168.20.100 dstport=805 protocol= [ protocol=tcp|udp|ip ] 

 Options 

 tcp Enter tcp to look up a given destination address
in TCP L4-Prefix-Lookup table. 

 udp Enter udp to look up a given destination address
in UDP L4-Prefix-Lookup table. 

 ip Enter ip to look up a given destination address
in non-TCP-UDP L4-Prefix-Lookup table. 

 Command Notes 

 Role Super, Read Only 

 Related Commands — 

 Introduced in Release 5.4.1 

 Example 

 inspect app-l4-prefix lookup dstv4=192.168.20.100 dstport=907protocol=udp
 {
 "App Found": "ring-central3",
 "App ID": 3888,
 "dscp": 0,
 "App Name": "ring-central3",
 "Order Number": 32768
 }

 inspect app-l4-prefix lookup dstv4=192.168.20.100 dstport=907protocol=tcp
 {
 "App Found": "disk",
 "App ID": 65,
 "dscp": 0,
 "App Name": "disk",
 "Order Number": 32768
 }

 inspect app-l4-prefix lookup dstv4=192.168.20.100 dstport=907protocol=tcp
 {
 "App NOT Found": []
 } 

 Previous 

 inspect app-flow-table 

 Next 

 inspect app-map 

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

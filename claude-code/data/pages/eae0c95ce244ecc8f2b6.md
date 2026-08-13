---
url: https://docs.paloaltonetworks.com/prisma-sd-wan/ion-cli-reference/use-cli-commands/inspect-commands/inspect-connection
fetched_at: 2026-08-13T17:30:52Z
source: palo-alto-main
---

# inspect connection Clear

inspect connection 

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

 inspect connection 

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

 inspect connection 

 Download PDF 

 Prisma SD-WAN 

 inspect connection 

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

 inspect cgnxinfra role 

 Next 

 inspect dhcplease 

 inspect connection 

 Use the inspect connection command
to inspect the established connections and to debug connections
that match user-specified options. It displays the protocol, time
after which connection times out, source IP, destination IP, source
port, and destination port. 

 Command 

 inspect connection (all | srcv4=src-ipv4 | destv4=dst-ipv4 | srcv6=src-ipv6 | destv6=dst-ipv6 | srcport=src-port | dstport=dst-port | proto= ( udp | tcp | icmp | other )) 

 Options 

 srcv4 Enter the source IPv4 address. 

 dstv4 Enter the destination IPv4 address. 

 srcv6 Enter the source IPv6 address. 

 dstv6 Enter the destination IPv6 address. 

 srcport Enter the source port. 

 dstport Enter the destination port. 

 proto Tab to select UDP, TCP, or ICMP. Or, enter
a protocol number ranging from 0 - 255. 

 Command Notes 

 Role Super, Read Only 

 Related Commands — 

 Introduced in Release 5.0.1 

 Example 

 inspect connection proto=udp
 PROTO TIMEOUT SRC DST SPORT DPORT t-src t-dst tsport tdport
 udp 6 127.0.0.1 127.0.0.1 51884 53 127.0.0.1 127.0. 0.1 51884 53
 udp 12 0.0.0.0 255.255.255.255 68 67 0.0.0.0 255.255.255.255 68 67
 udp 29 10.24.18.20 210.24.18.101 51409 3784 10.24.18.20 210.24.18.101 51409 3784

 inspect connection all

 PROTO TIMEOUT SRC DST SPORT DPORT t-src t-dst t-sport t-dport

 tcp 3524 fd13::2 2001:800::2 52754 9999 2001:800::1 2001:800::2 52754 9999

 udp 29 100.64.0.36 100.64.0.37 52634 3784 100.64.0.36 100.64.0.37 52634 3784

 udp 29 100.64.0.38 100.64.0.39 62944 3784 100.64.0.38 100.64.0.39 62944 3784 

 Previous 

 inspect cgnxinfra role 

 Next 

 inspect dhcplease 

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

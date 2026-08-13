---
url: https://docs.paloaltonetworks.com/ngfw/help/12-1/network/network-network-profiles/network-network-profiles-zone-protection/packet-based-attack-protection/ip-drop
fetched_at: 2026-08-13T16:50:11Z
source: palo-alto-main
---

# IP Drop Clear

IP Drop 

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

 IP Drop 

 Updated on 

 Thu Jun 25 18:50:04 PDT 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Next-Generation Firewall Docs 

 Getting Started 

 Administration 

 Networking 

 Quick Start 

 Reference 

 Incidents & Alerts 

 Release Notes 

 Select a Document 

 PAN-OS 12.2 

 PAN-OS 12.1 

 PAN-OS 11.2 

 PAN-OS 11.1 

 PAN-OS 11.0 (EoL) 

 PAN-OS 10.2 

 PAN-OS 10.1 (EoL) 

 PAN-OS 10.0 (EoL) 

 PAN-OS 9.1 (EoL) 

 PAN-OS 9.0 (EoL) 

 PAN-OS 8.1 (EoL) 

 Help 

 Select a Document 

 PAN-OS 12.2 

 PAN-OS 12.1 

 PAN-OS 11.2 

 PAN-OS 11.1 

 PAN-OS 10.2 

 PAN-OS 10.1 

 New Features 

 Updated on 

 Thu Jun 25 18:50:04 PDT 2026 

 Focus 

 Home 

 Next-Generation Firewall 

 Network 

 Network > Network Profiles 

 Network > Network Profiles > Zone Protection 

 Packet Based Attack Protection 

 IP Drop 

 Download PDF 

 Next-Generation Firewall 

 IP Drop 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Next-Generation Firewall Docs 

 Getting Started 

 Administration 

 Networking 

 Quick Start 

 Reference 

 Incidents & Alerts 

 Release Notes 

 Select a Document 

 PAN-OS 12.2 

 PAN-OS 12.1 

 PAN-OS 11.2 

 PAN-OS 11.1 

 PAN-OS 11.0 (EoL) 

 PAN-OS 10.2 

 PAN-OS 10.1 (EoL) 

 PAN-OS 10.0 (EoL) 

 PAN-OS 9.1 (EoL) 

 PAN-OS 9.0 (EoL) 

 PAN-OS 8.1 (EoL) 

 Help 

 Select a Document 

 PAN-OS 12.2 

 PAN-OS 12.1 

 PAN-OS 11.2 

 PAN-OS 11.1 

 PAN-OS 10.2 

 PAN-OS 10.1 

 New Features 

 Previous 

 Packet Based Attack Protection 

 Next 

 TCP Drop 

 IP Drop 

 To instruct the firewall what to do with certain IP
packets it receives in the zone, specify the following settings. 

 Zone Protection Profile Settings—Packet
Based Attack Protection 

 Configured In 

 Description 

 Spoofed IP address 

 Network Network Profiles Zone Protection Packet Based Attack Protection IP Drop 

 Check that the source IP address of the
ingress packet is routable and the routing interface is in the same
zone as the ingress interface. If either condition is not true,
discard the packet. 

 The firewall does not consider Policy Based
Forwarding (PBF) rules during this check; it considers only routes
listed in the routing table (RIB), that is, routes listed under
the CLI output for show routing route . 

 On internal zones only, drop spoofed IP
address packets to ensure that on ingress, the source address matches
the firewall routing table. 

 Strict IP Address Check 

 Check that both conditions are true: 

 The source IP address is not the subnet broadcast IP address
of the ingress interface. 

 The source IP address is routable over the exact ingress interface. 

 If
either condition is not true, discard the packet. 

 The
firewall does not consider Policy Based Forwarding (PBF) rules during
this check; it considers only routes listed in the routing table
(RIB), that is, routes listed under the CLI output for show routing route . 

 For
a firewall in Common Criteria (CC) mode, you can enable logging
for discarded packets. On the firewall web interface, select Device Log Settings .
In the Manage Logs section, select Selective Audit and
enable Packet Drop Logging . 

 Fragmented traffic 

 Discard fragmented IP packets. 

 IP Option Drop 

 Select the settings in this group to enable
the firewall to drop packets containing these IP Options. 

 Strict Source Routing 

 Discard packets with the Strict Source Routing
IP option set. Strict Source Routing is an option whereby a source
of a datagram provides routing information through which a gateway
or host must send the datagram. 

 Drop
packets with strict source routing because source routing allows
adversaries to bypass Security policy rules that use the destination
IP address as the matching criteria. 

 Loose Source Routing 

 Discard packets with the Loose Source Routing
IP option set. Loose Source Routing is an option whereby a source
of a datagram provides routing information and a gateway or host
is allowed to choose any route of a number of intermediate gateways
to get the datagram to the next address in the route. 

 Drop packets with loose source routing
because source routing allows adversaries to bypass Security policy
rules that use the destination IP address as the matching criteria. 

 Timestamp 

 Discard packets with the Timestamp IP option
set. 

 Record Route 

 Discard packets with the Record Route IP
option set. When a datagram has this option, each router that routes
the datagram adds its own IP address to the header, thus providing the
path to the recipient. 

 Security 

 Discard packets if the security option is
defined. 

 Stream ID 

 Discard packets if the Stream ID option
is defined. 

 Unknown 

 Discard packets if the class and number
are unknown. 

 Discard unknown packets. 

 Malformed 

 Discard packets if they have incorrect combinations
of class, number, and length based on RFCs 791, 1108, 1393, and 2113. 

 Discard malformed packets. 

 Previous 

 Packet Based Attack Protection 

 Next 

 TCP Drop 

 On This Page 

 Activation & Onboarding 

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

 Service Provider 

 VM-Series 

 SASE 

 Prisma Access 

 Strata Multitenant Cloud Manager 

 AI-Powered ADEM 

 Prisma Access Monitoring and Visibility 

 Prisma SD-WAN 

 ION Devices 

 Next-Generation CASB 

 Cloud-Delivered Security Services 

 Advanced WildFire 

 Advanced URL Filtering 

 Advanced Threat Prevention 

 Advanced DNS Security 

 Device Security 

 Enterprise DLP 

 SaaS Security 

 Network Security 

 Shared Policy for NGFWs and Prisma Access 

 Visibility & Monitoring 

 Dashboards 

 Incidents and Alerts 

 Reports 

 Autonomous DEM 

 Best Practices 

 Best Practices Library 

 Experts Corner 

 Solutions Docs from Product Experts 

 Network Security 

 PAN-OS 

 Next-Generation Firewall 

 12.1 

 Help 

 Web Interface 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

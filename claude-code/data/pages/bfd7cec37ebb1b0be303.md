---
url: https://docs.paloaltonetworks.com/prisma-sd-wan/new-features/by-date/prisma-sd-wan/september-2025#0cea42253a48f6797d710251f3ccf528
fetched_at: 2026-09-16T07:48:47Z
source: strata-and-sase
---

# New Features - Prisma SD-WAN - September 2025 Clear Clear Clear Clear Clear Clear Clear Clear Clear Clear Clear Clear Clear Clear Clear

Focus 

 Home 

 Prisma SD-WAN 

 New Features - Prisma SD-WAN - September 2025 

 Download PDF 

 IPv6 for BGP Support 

 Release Date: September 2025 
 | 
 Last Updated: May 2026 

 To configure dynamic routing using Border Gateway Protocol ( BGP ) for your branch or data center, use the following guidelines. This BGP capability allows your ION devices to integrate seamlessly with existing network routing infrastructure. 

 To peer with a BGP router via the private WAN interface, enable L3 Direct Private WAN Forwarding. You must enable L3 Direct Private WAN Forwarding and L3 LAN Forwarding to use dynamic LAN routing. 

 The configuration you use on a branch ION device is identical to the data center's configuration, with the exception of prefix advertisement in a branch and additional core and edge peers in a data center. You can now use IPv6 for BGP with Prisma SD-WAN (available in software version 5.5 and later). 

 Prisma SD-WAN

 ION Device

 September 2025

 Prisma SD-WAN

 Core

 September 2025

 VRF- Support for Standard VPN, NTP, Syslog, and SNMP 

 Release Date: September 2025 
 | 
 Last Updated: May 2026 

 Prisma SD-WAN now supports Standard VPNs for existing Virtual Routing and Forwarding tables (VRFs) tables. This new feature enables robust network segmentation by quickly associating a Standard VPN with any VRF, such as the Guest VRF. 

 Implement traffic steering in two ways: 

 For specific traffic : To redirect traffic from a specific VRF to the Standard VPN, simply configure path policies. 

 For all VRF traffic : When all user traffic across multiple VRFs must utilize the Standard VPN, first, configure a route leak to ensure basic L3 reachability. Once reachability is established, apply path policies for more granular traffic engineering and Quality of Service (QoS) control. 

 Prisma SD-WAN

 Core

 September 2025

 Prisma SD-WAN

 September 2025

 Virtual Routing Forwarding for WAN Segmentation 

 Release Date: September 2025 
 | 
 Last Updated: May 2026 

 Prisma SD-WAN supports Virtual Routing and Forwarding ( VRF ) to provide secure WAN segmentation of application traffic. This capability is valuable when you need to isolate traffic for different business units or customers who share the same WAN infrastructure. 

 To configure segmentation, you must first define WAN Segments in global VRF profiles. 

 You then bind these VRF profiles to sites and configure interfaces with the appropriate VRF. When traffic enters the interface, it only considers destinations that have the same VRF locally or across the fabric. If the traffic is destined to go across the fabric, the Prisma SD-WAN device automatically encapsulates the traffic with a unique VRF-specific identifier. When the traffic reaches the remote ION, it egresses onto the configured VRF. 

 Prisma SD-WAN

 Core

 September 2025

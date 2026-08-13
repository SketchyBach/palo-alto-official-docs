---
url: https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-admin/zone-protection-and-dos-protection/zone-defense/zone-protection-profiles/flood-protection
fetched_at: 2026-08-13T17:05:38Z
source: palo-alto-main
---

# Zone Protection Profiles Clear

Zone Protection Profiles 

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

 Zone Protection Profiles 

 Updated on 

 Aug 3, 2026 

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

 Aug 3, 2026 

 Focus 

 Home 

 Next-Generation Firewall 

 Zone Protection and DoS Protection 

 Zone Defense 

 Zone Protection Profiles 

 Download PDF 

 Next-Generation Firewall 

 Zone Protection Profiles 

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

 How to Measure CPS 

 Next 

 Configure Reconnaissance Protection 

 Zone Protection Profiles 

 Protect zones against floods, reconnaissance, packet-based attacks,
 non-IP-protocol-based attacks, and Security Group Tags with Zone Protection profiles. 

 Where Can I Use This? What Do I Need? 

 NGFW (Managed by PAN-OS or Panorama) 

 No prerequisites needed 

 Apply a Zone Protection profile to each zone to defend it based on the aggregate traffic
 entering the ingress zone. 

 Flood Protection 

 Reconnaissance Protection 

 Packet-Based Attack Protection 

 Protocol Protection 

 Ethernet SGT Protection 

 In addition to configuring zone protection and DoS protection, apply the best practice Vulnerability Protection
 profile to each Security policy rule to help defend against DoS
 attacks. 

 Flood Protection 

 A Zone Protection profile with flood protection configured defends an entire ingress
 zone against SYN, ICMP, ICMPv6, UDP, and other IP flood attacks. The firewall
 measures the aggregate amount of each flood type entering the zone in new
 connections-per-second (CPS) and compares the totals to the thresholds you configure
 in the Zone Protection profile. (You protect critical individual devices within a
 zone with DoS Protection profiles and policy
 rules .) 

 Measure and monitor firewall dataplane CPU consumption to ensure that each
 firewall is properly sized to support DoS and Zone Protection and any other
 features that consume CPU cycles, such as decryption. If you use Panorama to
 manage your firewalls, Device Monitoring ( Panorama Managed Devices Health All Devices ) shows you the CPU and memory consumption of each managed
 firewall. It can also show you a 90-day trend line of CPU average and peak use
 to help you understand the typical available capacity of each firewall. 

 For each flood type, you set three thresholds for new CPS entering the zone, and you
 can set a drop Action for SYN floods. If you know the
 baseline CPS rates for the zone, use these guidelines to set the initial thresholds,
 and then monitor and adjust the thresholds as necessary. 

 Alarm Rate —The new CPS threshold to trigger an alarm. Target setting
 the Alarm Rate to 15-20% above the average CPS rate
 for the zone so that normal fluctuations don’t cause alerts. 

 Activate —The new CPS threshold to activate the flood protection
 mechanism and begin dropping new connections. For ICMP, ICMPv6, UDP, and
 other IP floods, the protection mechanism is Random Early Drop (RED, also
 known as Random Early Detection). For SYN floods only, you can set the drop
 Action to SYN Cookies or RED. Target setting the
 Activate rate to just above the peak CPS rate for
 the zone to begin mitigating potential floods. 

 Maximum —The number of connections-per-second to drop incoming packets
 when RED is the protection mechanism. Target setting the
 Maximum rate to approximately 80-90% of firewall
 capacity, taking into account other features that consume firewall
 resources. 

 If you don’t know the baseline CPS rates for the zone, start by setting the
 Maximum CPS rate to approximately 80-90% of firewall
 capacity and use it to derive reasonable flood mitigation alarm and activation
 rates. Set the Alarm Rate and Activate 
 rate based on the Maximum rate. For example, you could set the Alarm
 Rate to half the Maximum rate and adjust it
 depending on how many alarms you receive and the firewall resources being consumed.
 Be careful setting the Activate Rate since it begins to drop
 connections. Because normal traffic loads experience some fluctuation, it’s best not
 to drop connections too aggressively. Err on the high side and adjust the rate if
 firewall resources are impacted. 

 SYN Flood Protection is the only type for which you set the drop
 Action . Start by setting the
 Action to SYN Cookies . SYN
 Cookies treats legitimate traffic fairly and only drops traffic that fails the
 SYN handshake, while using Random Early Drop drops traffic randomly, so RED may
 affect legitimate traffic. However, SYN Cookies is more resource-intensive
 because the firewall acts as a proxy for the target server and handles the
 three-way handshake for the server. The tradeoff is not dropping legitimate
 traffic (SYN Cookies) versus preserving firewall resources (RED). Monitor the
 firewall, and if SYN Cookies consumes too many resources, switch to RED. If you
 don’t have a dedicated DDoS prevention device in front of the firewall, always
 use RED as the drop mechanism. 

 When SYN Cookies is activated, the firewall does not honor
 the TCP options that the server sends because it does not know these values at
 the time that it proxies the SYN/ACK. Therefore, values such as the TCP server’s
 window size and MSS values cannot be negotiated during the TCP handshake and the
 firewall will use its own default values. In the scenario where the MSS of the
 path to the server is smaller than the firewall’s default MSS value, the packet
 will need to be fragmented. 

 The default threshold values are high so that activating a Zone Protection profile
 doesn’t unexpectedly drop legitimate traffic. Adjust the thresholds to values
 appropriate for your network’s traffic. The best method for understanding how to set
 reasonable flood thresholds is to take baseline measurements of average and peak CPS
 for each flood type to determine the normal traffic conditions for each zone and to
 understand the capacity of the firewall, including the impact of other
 resource-consuming features such as decryption. Monitor and adjust the flood
 thresholds as needed and as your network evolves. 

 Firewalls with multiple dataplane processors (DPs) distribute connections across
 DPs. In general, the firewall divides the CPS threshold settings equally across
 its DPs. For example, if a firewall has five DPs and you set the
 Alarm Rate to 20,000 CPS, each DP has an
 Alarm Rate of 4,000 CPS (20,000 / 5 = 4,000), so if
 the new sessions on a DP exceeds 4,000, it triggers the Alarm
 Rate threshold for that DP. 

 Reconnaissance Protection 

 Similar to the military definition of reconnaissance, the network security definition
 of reconnaissance is when attackers attempt to gain information about your network’s
 vulnerabilities by secretly probing the network to find weaknesses. Reconnaissance
 activities are often preludes to a network attack. Enable Reconnaissance
 Protection on all zones to defend against port scans and host sweeps: 

 Port scans discover open ports on a network. A port scanning tool
 sends client requests to a range of port numbers on a host, with the goal of
 locating an active port to exploit in an attack. Zone Protection profiles
 defend against TCP and UDP port scans. 

 Host sweeps examine multiple hosts to determine if a specific port is
 open and vulnerable. 

 IP protocol scans cycle through IP protocol numbers to determine the
 IP protocols and thus services supported by target machines. 

 You can use reconnaissance tools for legitimate purposes such as pen testing of
 network security or the strength of a firewall. You can specify up to 20 IP
 addresses or netmask address objects to exclude from Reconnaissance Protection so
 that your internal IT department can conduct pen tests to find and fix network
 vulnerabilities. 

 You can set the action to take when reconnaissance traffic (excluding pen testing
 traffic) exceeds the configured threshold when you configure reconnaissance protection .
 Retain the default Interval and
 Threshold to log a few packets for analysis before
 blocking the reconnaissance operation. 

 Packet-Based Attack Protection 

 Packet-based attacks take many forms. Zone Protection profiles check IP, TCP, ICMP,
 IPv6, and ICMPv6 packet headers and protect a zone by: 

 Dropping packets with undesirable characteristics. 

 Stripping undesirable options from packets before admitting them to the
 zone. 

 Select the drop characteristics for each packet type when you Configure Packet Based Attack Protection . The best practices for each IP protocol are: 

 IP Drop —Drop Unknown and
 Malformed packets. Also drop Strict
 Source Routing and Loose Source
 Routing because allowing these options allows adversaries to
 bypass Security policy rules that use the Destination IP address as the
 matching criteria. For internal zones only, check Spoofed IP
 Address so only traffic with a source address that matches
 the firewall routing table can access the zone. 

 TCP Drop —Retain the default TCP SYN with
 Data and TCP SYNACK with Data drops,
 drop Mismatched overlapping TCP segment and
 Split Handshake packets, and strip the
 TCP Timestamp from packets. 

 Enabling Rematch Sessions ( Device Setup Session Session Settings ) is a best practice that applies committed newly
 configured or edited Security Policy rules to existing sessions.
 However, if you configure Tunnel Content
 Inspection on a zone and Rematch
 Sessions is enabled, you must also disable
 Reject Non-SYN TCP (change the selection from
 Global to No ), or else
 when you enable or edit a Tunnel Content Inspection policy, the firewall
 drops all existing tunnel sessions. Create a separate Zone Protection
 profile to disable Reject Non-SYN TCP only on
 zones that have Tunnel Content Inspection policies and only when you
 enable Rematch Sessions . 

 ICMP Drop —There are no standard best practice settings
 because dropping ICMP packets depends on how you use ICMP (or if you use
 ICMP). For example, if you want to block ping activity, you can block
 ICMP Ping ID 0 . 

 IPv6 Drop —If compliance matters, ensure that the
 firewall drops packets with non-compliant routing headers, extensions,
 etc. 

 ICMPv6 Drop —If compliance matters, ensure that the
 firewall drops certain packets if the packets don’t match a Security policy
 rule. 

 Protocol Protection 

 In a Zone Protection profile, Protocol Protection defends against non-IP protocol
 based attacks. Enable Protocol Protection to block or allow non-IP protocols between
 security zones on a Layer 2 VLAN or on a virtual wire, or between interfaces
 within a single zone on a Layer 2 VLAN (Layer 3 interfaces and zones drop
 non-IP protocols so non-IP Protocol Protection doesn’t apply). Configure Protocol
 Protection to reduce security risks and facilitate regulatory compliance by
 preventing less secure protocols from entering a zone, or an interface in a
 zone. 

 If you don’t configure a Zone Protection profile that prevents non-IP protocols
 in the same zone from going from one Layer 2 interface to another, the firewall
 allows the traffic because of the default intrazone allow Security policy rule.
 You can create a Zone Protection profile that blocks protocols such as LLDP within a
 zone to prevent discovery of networks reachable through other zone
 interfaces. 

 If you need to discover which non-IP protocols are running on your network, use
 monitoring tools such as NetFlow, Wireshark, or other third-party tools discover
 non-IP protocols on your network. Examples of non-IP protocols you can block or
 allow are LLDP, NetBEUI, Spanning Tree, and Supervisory Control and Data Acquisition
 (SCADA) systems such as Generic Object Oriented Substation Event (GOOSE), among many
 others. 

 Create an Exclude List or an Include
 List to configure Protocol Protection for a zone. The
 Exclude List is a block list—the firewall blocks all of
 the protocols you place in the Exclude List and allows all
 other protocols. The Include List is an allow list—the
 firewall allows only the protocols you specify in the list and blocks all other
 protocols. 

 Use include lists for Protocol Protection instead of exclude lists. Include lists
 specifically sanction only the protocols you want to allow and block the
 protocols you don’t need or didn’t know were on your network, which reduces the
 attack surface and blocks unknown traffic. 

 A list supports up to 64 Ethertype entries, each identified by its IEEE hexadecimal Ethertype code. Other
 sources of Ethertype codes are standards.ieee.org/develop/regauth/ethertype/eth.txt and
 http://www.cavebear.com/archive/cavebear/Ethernet/type.html . When you
 configure zone protection for non-IP protocols on zones that have Aggregated
 Ethernet (AE) interfaces, you can’t block or allow a non-IP protocol on only one AE
 interface member because AE interface members are treated as a group. 

 Protocol Protection doesn’t allow blocking IPv4 (Ethertype 0x0800), IPv6
 (0x86DD), ARP (0x0806), or VLAN-tagged frames (0x8100). The firewall always
 implicitly allows these four Ethertypes in an Include
 List even if you don’t explicitly list them and doesn’t permit
 you to add them to an Exclude List . 

 Ethernet SGT Protection 

 In a Cisco TrustSec network, a Cisco Identity Services Engine (ISE)
 assigns a Layer 2 Security Group Tag (SGT) of 16 bits to a user’s or endpoint’s
 session. You can create a Zone Protection profile 
 with Ethernet SGT protection when your firewall is part of a Cisco TrustSec network.
 The firewall can inspect headers with 802.1Q (Ethertype 0x8909) for specific Layer 2
 security group tag (SGT) values and drop the packet if the SGT matches the list you
 configure for the Zone Protection profile attached to the interface. Determine which
 SGT values you want to deny access to a zone. 

 Previous 

 How to Measure CPS 

 Next 

 Configure Reconnaissance Protection 

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

 Administration 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

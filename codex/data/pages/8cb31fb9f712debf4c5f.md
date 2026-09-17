---
url: https://docs.paloaltonetworks.com/ngfw/help/12-2/network/network-network-profiles/network-network-profiles-zone-protection/packet-based-attack-protection/icmp-drop
fetched_at: 2026-09-16T07:31:54Z
source: palo-alto-main
---

# ICMP Drop Clear

Updated on 

 Wed Aug 19 00:09:31 PDT 2026 

 Focus 

 Home 

 Next-Generation Firewall 

 PAN-OS Web Interface Help 

 Network 

 Network > Network Profiles 

 Network > Network Profiles > Zone Protection 

 Packet Based Attack Protection 

 ICMP Drop 

 Download PDF 

 Next-Generation Firewall 

 ICMP Drop 

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

 TCP Drop 

 Next 

 IPv6 Drop 

 ICMP Drop 

 To instruct the firewall to drop certain ICMP packets
it receives in the zone, select the following settings to enable
them. 

 Zone Protection Profile Settings—Packet Based Attack Protection 

 Configured In 

 Description 

 ICMP Ping ID 0 

 Network Network Profiles Zone Protection Packet Based Attack Protection ICMP Drop 

 Discard packets if the ICMP ping packet
has an identifier value of 0. 

 ICMP Fragment 

 Discard packets that consist of ICMP fragments. 

 ICMP Large Packet (>1024) 

 Discard ICMP packets that are larger than
1024 bytes. 

 Discard ICMP embedded with error message 

 Discard ICMP packets that are embedded with
an error message. 

 Suppress ICMP TTL Expired Error 

 Stop sending ICMP TTL expired messages. 

 Suppress ICMP Frag Needed 

 Stop sending ICMP fragmentation needed messages
in response to packets that exceed the interface MTU and have the
do not fragment (DF) bit set. This setting will interfere with the
PMTUD process performed by hosts behind the firewall. 

 Previous 

 TCP Drop 

 Next 

 IPv6 Drop

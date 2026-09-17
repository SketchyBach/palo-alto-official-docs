---
url: https://docs.paloaltonetworks.com/ngfw/help/11-1/monitor/monitor-packet-capture/packet-capture-overview
fetched_at: 2026-09-16T07:28:32Z
source: palo-alto-main
---

# Packet Capture Overview Clear

Updated on 

 Thu Jun 25 17:39:35 PDT 2026 

 Focus 

 Home 

 Next-Generation Firewall 

 Monitor 

 Monitor > Packet Capture 

 Packet Capture Overview 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 한국어 (Korean) 

 Next-Generation Firewall 

 Packet Capture Overview 

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

 Monitor > Packet Capture 

 Next 

 Building Blocks for a Custom Packet Capture 

 Packet Capture Overview 

 You can configure a Palo Alto Networks firewall to perform
a custom packet capture or a threat packet capture. 

 Custom Packet Capture —Capture packets for all
traffic or traffic based on filters you define. For example, you can
configure the firewall to capture only packets to and from a specific
source and destination IP address or port. Use these packet captures
to troubleshoot network traffic-related issues or to gather application
attributes to write custom application signatures ( Monitor Packet Capture ).
You define the file name based on the stage (Drop, Firewall, Receive,
or Transmit) and, after the PCAP is complete, you download the PCAP
in the Captured Files section. 

 Threat Packet Capture —Capture packets when the firewall
detects a virus, spyware, or vulnerability. You enable this feature
in Antivirus, Anti-Spyware, and Vulnerability Protection security
profiles. These packet captures provide context around a threat
to help you determine if an attack is successful or to learn more
about the methods used by an attacker. The action for the threat
must be set to either allow or alert; otherwise, the threat is blocked
and packets cannot be captured. You configure this type of packet
capture in the Objects Security Profiles .
To download ( 

 ) pcaps, select Monitor Threat . 

 Previous 

 Monitor > Packet Capture 

 Next 

 Building Blocks for a Custom Packet Capture

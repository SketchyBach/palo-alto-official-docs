---
url: https://docs.paloaltonetworks.com/service-providers/11-1/mobile-network-infrastructure-getting-started/5g-security/5g-multi-edge-security
fetched_at: 2026-08-13T17:36:49Z
source: palo-alto-main
---

# 5G Multi-access Edge Computing Security Clear

5G Multi-access Edge Computing Security 

 Home 

 EN

 Location 

 Documentation Home 

 Palo Alto Networks 

 Support 

 Live Community 

 Knowledge Base 

 Strata Copilot

 Mobile Network Infrastructure Getting Started 

 : 
 5G Multi-access Edge Computing Security 

 Updated on 

 Fri Oct 31 17:02:18 PDT 2025 

 Focus 

 Download PDF 

 Filter

 Version 

 11.1 & Later 

 11.1 & Later 

 11.0 (EoL) 

 10.2 

 10.1 (EoL) 

 Expand all | Collapse all 

 Stream Control Transmission Protocol (SCTP) 

 SCTP Introduction 

 SCTP Association 

 SCTP Multihoming 

 SCTP Packets and Chunks 

 SCTP Use Cases 

 SCTP Security Measures on the Firewall 

 Configure SCTP Security 

 Configure SCTP INIT Flood Protection 

 Monitor SCTP Security 

 SCTP Event Types 

 Manage SCTP from Panorama 

 GPRS Tunneling Protocol (GTP) 

 GTP Overview 

 GTP Deployments 

 RAN Security 

 Roaming Security 

 Non-3GPP Access Security 

 CIoT Security 

 Configure GTP Stateful Inspection 

 Mobile Network Protection Profile 

 Monitor GTP Traffic 

 View GTP Logs 

 GTP Information on the ACC 

 Generate Mobile Network Reports 

 GTP Event Types and Severity 

 GTP Event Codes 

 GTP Cause Values in Logs 

 GTP Message Type 

 Get a Packet Capture of a GTP Event 

 Disable Tunnel Acceleration 

 5G-Ready K2 Next-Generation Firewalls 

 Express Mode and Secure Mode 

 Restore Express Mode 

 Upgrade Line Cards to K2 Secure Mode 

 5G Security 

 5G Network Slice Security 

 5G Equipment ID and Subscriber ID Security 

 Configure 5G Network Slice Security 

 Configure 5G Equipment ID Security 

 Configure 5G Subscriber ID Security 

 5G Multi-access Edge Computing Security 

 Configure 5G Multi-access Edge Computing Security 

 PFCP Event Types 

 4G Equipment ID and Subscriber ID Security 

 4G Equipment ID Security 

 4G Subscriber ID Security 

 Configure 4G Equipment ID Security 

 Configure 4G Subscriber ID Security 

 Intelligent Security and User Equipment Correlation with IP Addresses 

 Intelligent Security and the UEIP Database 

 Intelligent Security with PFCP for User Equipment to IP Address Correlation 

 Configure Intelligent Security using PFCP for User Equipment to IP Address Correlation 

 Configure Intelligent Security Using RADIUS for User Equipment to IP Address Correlation 

 Configure Intelligent Security Using GTP for User Equipment to IP Address Correlation 

 Updated on 

 Fri Oct 31 17:02:18 PDT 2025 

 Focus 

 Home 

 Service Providers 

 Mobile Network Infrastructure Getting Started 

 5G Security 

 5G Multi-access Edge Computing Security 

 Download PDF 

 Mobile Network Infrastructure Getting Started 

 5G Multi-access Edge Computing Security 

 Table of Contents 

 Filter

 Version 

 11.1 & Later 

 11.1 & Later 

 11.0 (EoL) 

 10.2 

 10.1 (EoL) 

 Expand all | Collapse all 

 Stream Control Transmission Protocol (SCTP) 

 SCTP Introduction 

 SCTP Association 

 SCTP Multihoming 

 SCTP Packets and Chunks 

 SCTP Use Cases 

 SCTP Security Measures on the Firewall 

 Configure SCTP Security 

 Configure SCTP INIT Flood Protection 

 Monitor SCTP Security 

 SCTP Event Types 

 Manage SCTP from Panorama 

 GPRS Tunneling Protocol (GTP) 

 GTP Overview 

 GTP Deployments 

 RAN Security 

 Roaming Security 

 Non-3GPP Access Security 

 CIoT Security 

 Configure GTP Stateful Inspection 

 Mobile Network Protection Profile 

 Monitor GTP Traffic 

 View GTP Logs 

 GTP Information on the ACC 

 Generate Mobile Network Reports 

 GTP Event Types and Severity 

 GTP Event Codes 

 GTP Cause Values in Logs 

 GTP Message Type 

 Get a Packet Capture of a GTP Event 

 Disable Tunnel Acceleration 

 5G-Ready K2 Next-Generation Firewalls 

 Express Mode and Secure Mode 

 Restore Express Mode 

 Upgrade Line Cards to K2 Secure Mode 

 5G Security 

 5G Network Slice Security 

 5G Equipment ID and Subscriber ID Security 

 Configure 5G Network Slice Security 

 Configure 5G Equipment ID Security 

 Configure 5G Subscriber ID Security 

 5G Multi-access Edge Computing Security 

 Configure 5G Multi-access Edge Computing Security 

 PFCP Event Types 

 4G Equipment ID and Subscriber ID Security 

 4G Equipment ID Security 

 4G Subscriber ID Security 

 Configure 4G Equipment ID Security 

 Configure 4G Subscriber ID Security 

 Intelligent Security and User Equipment Correlation with IP Addresses 

 Intelligent Security and the UEIP Database 

 Intelligent Security with PFCP for User Equipment to IP Address Correlation 

 Configure Intelligent Security using PFCP for User Equipment to IP Address Correlation 

 Configure Intelligent Security Using RADIUS for User Equipment to IP Address Correlation 

 Configure Intelligent Security Using GTP for User Equipment to IP Address Correlation 

 5G Multi-access Edge Computing Security 

 For enterprises and service providers that use Multi-access
Edge Computing (MEC), 5G Multi-access Edge Computing Security not
only provides security at the subscriber, equipment, and network
slice level, but also at the protocol level through stateful inspection
for Packet Forwarding Control Protocol (PFCP) traffic in 5G networks.
This level of security protects and secures devices and users that
connect to MEC, as well as applications hosted on MEC, from attacks
such as Denial of Service (DoS) and spoofing, as well as other potential threats
such as vulnerabilities, malware, and viruses. 5G Multi-access Edge Computing
Security delivers granular visibility and control, as well as context-based
visibility into threats. 

 In the following 5G MEC deployment scenario, the User Plane Function
(UPF) is located on the MEC in the service provider’s edge location
or on the public cloud edge and the 5G Core is located remotely
in a central core site or the public cloud. To enforce security
policy for user and control traffic, the firewall must be positioned
on the 5G interfaces, including the User Plane (N3) and the Control
Plane (N4). 

 For complete subscriber-level
and equipment-level visibility and security policy control for network
traffic threats, enable GTP Security . 

 The
second firewall in the diagram is positioned on the perimeter (the
N6 interface connected to the internet and the enterprise IT datacenter). 

 For platform support and capacity information, see the Compatibility Matrix . 

 Select one of the following topics to learn more about 5G Multi-access
Edge Computing Security: 

 Configure 5G Multi-access Edge Computing Security 

 PFCP Event Types 

 Previous 

 Configure 5G Subscriber ID Security 

 Next 

 Configure 5G Multi-access Edge Computing Security 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

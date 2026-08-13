---
url: https://docs.paloaltonetworks.com/service-providers/11-1/mobile-network-infrastructure-getting-started/4g-equipment-id-subscriber-id-security
fetched_at: 2026-08-13T17:36:46Z
source: palo-alto-main
---

# 4G Equipment ID and Subscriber ID Security Clear

4G Equipment ID and Subscriber ID Security 

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
 4G Equipment ID and Subscriber ID Security 

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

 10.0 (EoL) 

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

 4G Equipment ID and Subscriber ID Security 

 Download PDF 

 Mobile Network Infrastructure Getting Started 

 4G Equipment ID and Subscriber ID Security 

 Table of Contents 

 Filter

 Version 

 11.1 & Later 

 11.1 & Later 

 11.0 (EoL) 

 10.2 

 10.1 (EoL) 

 10.0 (EoL) 

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

 4G Equipment ID and Subscriber ID Security 

 Topics related to 4G/LTE security on supported next-generation
firewalls. 

 To protect 4G/LTE networks, you can enable
security and correlation based on equipment ID and subscriber ID
for the following supported firewall models: 

 PA-7500 Series 

 PA-7000 Series 

 PA-5500 Series ( PAN-OS 12.1.2 only ) 

 PA-5400 Series, including the PA-5450 firewall 

 PA-3400 Series 

 PA-440, PA-450, PA-450R, PA-450R-5G, and PA-460 firewalls 

 VM-700, VM-500, VM-300, and VM-100 Series 

 Software Next-Generation Firewall Credits 

 See the Palo Alto Networks Compatibility Matrix for more information about Mobile Network Infrastructure Feature
 Support . 

 In the following deployment scenario of a private 4G/LTE network,
the 4G core is located on-premises. To enforce security policy for
user and control traffic, the firewall must be positioned on the
4G/LTE interfaces, including the User Plane (S1-U) and the Control
Plane (S11). 

 For complete subscriber-level
and equipment-level visibility and security policy control for network
traffic threats, enable GTP Security . 

 The
second firewall in this diagram is positioned on the perimeter (the
SGI interface connected to the internet and the enterprise IT datacenter). 

 Learn about and configure the following: 

 4G Equipment ID Security 

 4G Subscriber ID Security 

 Configure 4G Equipment ID Security 

 Configure 4G Subscriber ID Security 

 Previous 

 PFCP Event Types 

 Next 

 4G Equipment ID Security 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

---
url: https://docs.paloaltonetworks.com/service-providers/11-0/mobile-network-infrastructure-getting-started/4g-equipment-id-subscriber-id-security/4g-subscriber-id-security
fetched_at: 2026-08-13T17:36:32Z
source: palo-alto-main
---

# 4G Subscriber ID Security Clear

4G Subscriber ID Security 

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
 4G Subscriber ID Security 

 Updated on 

 Jun 12, 2025 

 Focus 

 Download PDF 

 End-of-Life (EoL)

 Filter

 Version 

 11.0 (EoL) 

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

 Configure Intelligent Security using PFCP for User Equipment to IP Address Correlation 

 Configure Intelligent Security Using RADIUS for User Equipment to IP Address Correlation 

 Updated on 

 Jun 12, 2025 

 Focus 

 Home 

 Service Providers 

 Mobile Network Infrastructure Getting Started 

 4G Equipment ID and Subscriber ID Security 

 4G Subscriber ID Security 

 Download PDF 

 Mobile Network Infrastructure Getting Started 

 4G Subscriber ID Security 

 Table of Contents 

 Filter

 Version 

 11.0 (EoL) 

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

 Configure Intelligent Security using PFCP for User Equipment to IP Address Correlation 

 Configure Intelligent Security Using RADIUS for User Equipment to IP Address Correlation 

 End-of-Life (EoL)

 4G Subscriber ID Security 

 Conceptual information about 4G Subscriber ID security. 

 4G/LTE mobile networks are used by billions of subscribers
worldwide, increasingly to connect the Internet of Things. This
evolution needs context-aware security in the network to prevent
financial and operational risks for service providers and enterprise
customers using private 4G networks. Malware that infects User Equipment
(UE), including smart phones, tablets, laptops connected via a dongle,
and cellular IoT devices, could prevent the UE from accessing the
mobile network and could be part of a botnet launching an attack
against the mobile network infrastructure. 

 The impact of such malware to the customer includes battery exhaustion damage
to the device, degraded service, excessive billing, and more. The
impact to the service provider can include customer churn, help
desk calls, billing issues, excessive use of network resources by
compromised subscribers and devices, and more. Detection of these
threats in 4G/LTE mobile networks requires identification of compromised
subscribers; prevention requires the ability to apply network security
based on subscriber ID, which is an International Mobile Subscriber
Identity (IMSI). 

 You can use GTP security to investigate
a security event related to a subscriber or user in a 4G network
based on the IMSI. You can look at the traffic, threat, URL filtering
and WildFire ® logs and reports. 

 You can apply network security based
on the subscriber identity of a user who is trying to access your
4G network. 

 The following graphic illustrates two 4G deployment options.
In the first option, the firewall is on the S11 and S1-U interfaces.
S11 is the interface between the MME and SGW; S1-U is the interface
between the eNodeB and SGW in the 4G/LTE network. In the second
option, the firewall is on the S5/S8 interfaces, which are between
the SGW and PGW in the 4G/LTE network. 

 You can apply the following per equipment ID: 

 application control 

 Antivirus 

 Anti-Spyware 

 URL filtering 

 intrusion prevention 

 advanced threat prevention with WildFire based on an IMSI or
a group of IMSIs 

 Security policy rules allow you to specify external dynamic lists
(EDLs) that can specify IMSIs so that you can dynamically add IMSIs
to the rule. 

 When deciding which firewall model to purchase, consider the
total number of 3G, 4G, and 5G network identifiers (Subscriber IDs
and Equipment IDs) you need to include as EDL entries or static
entries. The table in 5G Equipment ID and Subscriber ID Security provides
capacities of EDL entries and static entries for each firewall model. 

 Previous 

 4G Equipment ID Security 

 Next 

 Configure 4G Equipment ID Security 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

---
url: https://docs.paloaltonetworks.com/service-providers/10-1/mobile-network-infrastructure-getting-started/sctp/configure-sctp-init-flood-protection
fetched_at: 2026-08-13T17:36:15Z
source: palo-alto-main
---

# Configure SCTP INIT Flood Protection Clear

Configure SCTP INIT Flood Protection 

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
 Configure SCTP INIT Flood Protection 

 Updated on 

 Wed May 06 15:01:43 PDT 2026 

 Focus 

 Download PDF 

 End-of-Life (EoL)

 Filter

 Version 

 10.1 (EoL) 

 11.1 & Later 

 11.0 (EoL) 

 10.2 

 10.1 (EoL) 

 10.0 (EoL) 

 9.1 (EoL) 

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

 Updated on 

 Wed May 06 15:01:43 PDT 2026 

 Focus 

 Home 

 Service Providers 

 Mobile Network Infrastructure Getting Started 

 Stream Control Transmission Protocol (SCTP) 

 Configure SCTP INIT Flood Protection 

 Download PDF 

 Mobile Network Infrastructure Getting Started 

 Configure SCTP INIT Flood Protection 

 Table of Contents 

 Filter

 Version 

 10.1 (EoL) 

 11.1 & Later 

 11.0 (EoL) 

 10.2 

 10.1 (EoL) 

 10.0 (EoL) 

 9.1 (EoL) 

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

 End-of-Life (EoL)

 Configure SCTP INIT Flood Protection 

 Protect a zone against flooding of SCTP INIT packets
by creating a zone protection profile. 

 Configure zone protection to protect a zone
against flooding of SCTP INIT packets. When you Configure
SCTP Security (enable SCTP), the option to protect against
a flood of SCTP INIT packets becomes available. 

 Create a Zone Protection profile to protect against
flooding of SCTP INIT packets. 

 Select Network Network Profiles Zone Protection Flood Protection and enable
(select) SCTP INIT . 

 Specify the threshold Alarm Rate (cps)
of SCTP INIT packets (not matching an existing session) for the
zone, above which the firewall generates an alert. You can view
alerts on the Dashboard and in the threat log (range is 0 to 2,000,000).
The default varies per firewall model as follows: 

 PA-5280 —10,000 

 PA-5260 —7,000 

 PA-5250 —5,000 

 PA-5220 —3,000 

 VM-Series —1,000 

 Specify the threshold rate (cps) of SCTP INIT packets
(not matching an existing session) for the zone, above which the
firewall will Activate the behavior to drop
subsequent SCTP INIT packets. The firewall uses an algorithm to
progressively drop more packets as the rate increases until the
rate reaches the Maximum rate. The firewall stops dropping SCTP
INIT packets if the incoming rate drops below the Activate threshold
(range is 1 to 2,000,000; the default varies per firewall model
as specified above for the Alarm Rate action). 

 Specify the Maximum rate (cps)
of SCTP INIT packets (not matching an existing session) allowed
for the zone. When the threshold is exceeded, new connections that
arrive are dropped (range is 1 to 2,000,000). The default varies
per firewall model as follows: 

 PA-5280 —20,000 

 PA-5260 —14,000 

 PA-5250 —10,000 

 PA-5220 —6,000 

 VM-Series —2,000 

 Click OK . 

 The Zone Protection profile summary includes a column
that indicates whether SCTP INIT Flood protection is enabled. 

 Apply the Zone Protection profile to a zone. 

 Select Network Zones and select a zone or Configure Interfaces and Zones to configure
a new zone. 

 For the Zone Protection Profile ,
select the profile you just created. 

 Click OK . 

 Commit your changes. 

 Previous 

 Configure SCTP Security 

 Next 

 Monitor SCTP Security 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

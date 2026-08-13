---
url: https://docs.paloaltonetworks.com/service-providers/10-1/mobile-network-infrastructure-getting-started/sctp/monitor-sctp-security
fetched_at: 2026-08-13T17:36:16Z
source: palo-alto-main
---

# Monitor SCTP Security Clear

Monitor SCTP Security 

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
 Monitor SCTP Security 

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

 Monitor SCTP Security 

 Download PDF 

 Mobile Network Infrastructure Getting Started 

 Monitor SCTP Security 

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

 Monitor SCTP Security 

 Monitor SCTP traffic by viewing logs, ACC displays generated
from SCTP logs, and predefined and custom reports. 

 You can enable SCTP association start logs
and end logs for SCTP endpoints configured in a Security policy
rule from an SCTP Protection profile. All other SCTP traffic logs
are event-based logs that are generated based on the options you
enable in the SCTP Protection profile. 

 To help you monitor
SCTP traffic, the firewall uses the SCTP logs to create a visual
display on the Mobile Network Activity tab in the ACC. The firewall
also gives you predefined reports and the ability to generate custom
reports. 

 SCTP logs are event-based logs that include information
on a wide range of SCTP attributes, including SCTP event type, chunk
type, payload protocol ID, SCTP cause code, association ID, stream
ID, and chunks, in addition to the general information that the
firewall identifies, such as source and destination address, source
and destination port, and timestamp. The SCTP logs also provide
additional information on some applications running over SCTP, including
Diameter and SS7 protocols. View the SCTP logs to verify that your
SCTP Protection profile settings are securing SCTP traffic as you
intend. 

 You must allocate a log storage quota for SCTP
when you Configure SCTP Security before
you can view SCTP log events. 

 View SCTP logs to see, for example,
source and destination IP addresses of SCTP traffic, whether control
chunks were allowed, whether data chunks were filtered by their
PPID, and when SCTP associations started and ended. 

 Select Monitor Logs SCTP . 

 Select the Detailed Log View ( 

 ) for
a specific log to view details about that log, such as the names
of the Security policy rule and the SCTP filter that applied to
the packets, the Verifications Tags, the Diameter Application ID,
the Diameter Command Code, and the SCCP Calling Party SSN. 

 View a detailed traffic log for an SCTP association,
including the name of the Security policy rule that applied to the
packet, the association ID, and the numbers of chunks sent and received. 

 Select Monitor Logs Traffic and,
in the filter field, enter app eq sctp and
apply the filter to filter the traffic logs. 

 Select the Detailed Log View ( 

 ) for
a specific log where the Application is sctp . 

 ( Optional ) Clear SCTP logs based on your operational
requirements. 

 Select Device Log Settings . 

 In the Manage Logs section, Clear SCTP
Logs . 

 Use ACC to view SCTP events and association activity. 

 Select ACC Mobile Network Activity . 

 Select the Virtual System you want to view or select All (default). 

 Select a Time period. 

 In the SCTP Events window, select an association ID
to see details of that association, such as chunks, source address,
and destination address. 

 View predefined reports about SCTP events and errors. 

 Select Device Setup Management . 

 Edit the Logging and Reporting Settings and select Pre-Defined
Reports . 

 In the SCTP Report section, select any of the following: SCTP
Events Summary , SCTP Security Events ,
or SCTP Error Causes (enabled by default). 

 Click OK . 

 Create a custom report on SCTP events. 

 Select Monitor Manage Custom Reports and Add a
custom report. 

 Enter a Name for the report. 

 For the Database , select SCTP from
Summary Databases or Detailed Logs (Slower). 

 Generate Custom Reports to create your
report and build queries based on SCTP elements, such as Chunk Type,
PPID, and SCTP Event Type. 

 Previous 

 Configure SCTP INIT Flood Protection 

 Next 

 SCTP Event Types 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

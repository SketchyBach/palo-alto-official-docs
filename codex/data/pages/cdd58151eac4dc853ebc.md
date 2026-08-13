---
url: https://docs.paloaltonetworks.com/ngfw/help/11-2/device/device-setup-session/session-timeouts
fetched_at: 2026-08-13T16:47:26Z
source: palo-alto-main
---

# Session Timeouts Clear

Session Timeouts 

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

 Session Timeouts 

 Updated on 

 Thu Jun 25 17:41:47 PDT 2026 

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

 Thu Jun 25 17:41:47 PDT 2026 

 Focus 

 Home 

 Next-Generation Firewall 

 Device 

 Device > Setup > Session 

 Session Timeouts 

 Download PDF 

 Next-Generation Firewall 

 Session Timeouts 

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

 Session Settings 

 Next 

 TCP Settings 

 Session Timeouts 

 Some session timeouts define the duration for which
PAN-OS maintains a session on the firewall after inactivity in the
session. By default, when the session timeout for the protocol expires,
PAN-OS closes the session. The Discard session timeouts define the
maximum time that a session remains open after PAN-OS denies the
session based on Security policy rules. 

 On the firewall, you can define a number of timeouts for TCP,
UDP, ICMP, and SCTP sessions in particular. The Default timeout
applies to any other type of session. All of these timeouts are
global, meaning they apply to all of the sessions of that type on
the firewall. 

 In addition to the global settings, you have the flexibility
to define timeouts for an individual application in the Objects Applications tab.
The timeouts available for that application appear in the Options
window. The firewall applies application timeouts to an application
that is in Established state. When configured, timeouts for an application
override the global TCP, UDP, or SCTP session timeouts. 

 Use the options in this section to configure global session timeout settings —specifically for TCP,
UDP, ICMP, SCTP, and for all other types of sessions. 

 The defaults are optimal values and the best practice is to use
the default values. However, you can modify these according to your network
needs. Setting a value too low could cause sensitivity to minor
network delays and could result in a failure to establish connections with
the firewall. Setting a value too high could delay failure detection. 

 Session Timeouts Settings 

 Description 

 Default 

 Maximum length of time, in seconds, that
a non-TCP/UDP, non-SCTP, or non-ICMP session can be open without
a response (range is 1 to 15,999,999; default is 30). 

 Discard Default 

 Maximum length of time (in seconds) that
a non-TCP/UDP/SCTP session remains open after PAN-OS denies the
session based on Security policy rules configured on the firewall
(range is 1 to 15,999,999; default is 60). 

 Discard TCP 

 Maximum length of time (in seconds) that
a TCP session remains open after PAN-OS denies the session based
on Security policy rules configured on the firewall (range is 1
to 15,999,999; default is 90). 

 Discard UDP 

 Maximum length of time (in seconds) that
a UDP session remains open after PAN-OS denies the session based
on Security policy rules configured on the firewall (range is 1
to 15,999,999; default is 60). 

 ICMP 

 Maximum length of time that an ICMP session
can be open without an ICMP response (range is 1 to 15,999,999;
default is 6). 

 Scan 

 Maximum length of time, in seconds, that
a session can be inactive before the firewall clears the session
and recovers the buffer resources the session was using. The inactive
time is the length of time that has passed since the session was
last refreshed by a packet or an event. Range is 5 to 30; default
is 10. 

 TCP 

 Maximum length of time that a TCP session
remains open without a response, after a TCP session is in the Established
state (after the handshake is complete and/or data transmission
has started); (range is 1 to 15,999,999; default is 3,600). 

 TCP handshake 

 Maximum length of time, in seconds, between
receiving the SYN-ACK and the subsequent ACK to fully establish
the session (ranges is 1 to 60; default is 10). 

 TCP init 

 Maximum length of time, in seconds, between
receiving the SYN and SYN-ACK before starting the TCP handshake
timer (ranges is 1 to 60; default is 5). 

 TCP Half Closed 

 Maximum length of time, in seconds, between
receiving the first FIN and receiving the second FIN or a RST (range
is 1 to 604,800; default is 120). 

 TCP Time Wait 

 Maximum length of time, in seconds, after
receiving the second FIN or a RST (range is 1 to 600; default is
15). 

 Unverified RST 

 Maximum length of time, in seconds, after
receiving a RST that cannot be verified (the RST is within the TCP
window but has an unexpected sequence number, or the RST is from
an asymmetric path); (ranges is 1 to 600; default is 30). 

 UDP 

 Maximum length of time, in seconds, that
a UDP session remains open without a UDP response (range is 1 to
1,599,999; default is 30). 

 Authentication Portal 

 The authentication session timeout in seconds
for the Authentication Portal web form (default is 30, range is
1 to 1,599,999). To access the requested content, the user must
enter the authentication credentials in this form and be successfully
authenticated. 

 The authentication session timeout in seconds
for the Authentication Portal web form (default is 30, range is
1 to 1,599,999). To access the requested content, the user must
enter the authentication credentials in this form and be successfully
authenticated. 

 SCTP INIT 

 Maximum length of time, in seconds, from
receiving an SCTP INIT chunk that the firewall must receive the
INIT ACK chunk before the firewall stops the SCTP association initiation (range is
1 to 60; default is 5). 

 SCTP COOKIE 

 Maximum length of time, in seconds, from
receiving an SCTP INIT ACK chunk with the state COOKIE parameter
that the firewall must receive the COOKIE ECHO chunk with the cookie
before the firewall stops the SCTP association initiation (range
is 1 to 600; default is 60). 

 Discard SCTP 

 Maximum length of time, in seconds, that
an SCTP association remains open after PAN-OS
denies the session based on Security policy rules configured on
the firewall (range is 1 to 604,800; default is 30). 

 SCTP 

 Maximum length of time, in seconds, that
can elapse without SCTP traffic for an association before
all sessions in the association time out (range is 1 to 604,800;
default is 3,600). 

 SCTP Shutdown 

 Maximum length of time, in seconds, that
the firewall waits after an SCTP SHUTDOWN chunk to receive a SHUTDOWN ACK
chunk before the firewall disregards the SHUTDOWN chunk (range is
1 to 600; default is 30). 

 Previous 

 Session Settings 

 Next 

 TCP Settings 

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

 11.2 

 Help 

 Panorama 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

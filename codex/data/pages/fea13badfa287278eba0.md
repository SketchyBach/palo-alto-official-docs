---
url: https://docs.paloaltonetworks.com/ngfw/administration/firewall-administration/reference-port-number-usage/ports-used-for-user-id
fetched_at: 2026-08-13T16:39:54Z
source: palo-alto-main
---

# Ports Used for User-ID Clear

Ports Used for User-ID 

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

 Ports Used for User-ID 

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

 Firewall Administration 

 Reference: Port Number Usage 

 Ports Used for User-ID 

 Download PDF 

 Next-Generation Firewall 

 Ports Used for User-ID 

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

 Ports Used for GlobalProtect 

 Next 

 Ports Used for IPSec 

 Ports Used for User-ID 

 Network ports and protocols used by User-ID functionality in PAN-OS firewalls and
 security operations. 

 User-ID is
a feature that enables mapping of user IP addresses to usernames
and group memberships, enabling user- or group-based policy and
visibility into user activity on your network (for example, to be
able to quickly track down a user who may be the victim of a threat).
To perform this mapping, the firewall, the User-ID agent (either
installed on a Windows-based system or the PAN-OS integrated agent
running on the firewall), and/or the Terminal Server agent must be
able to connect to directory services on your network to perform Group
Mapping and User
Mapping . Additionally, if the agents are running on systems
external to the firewall, they must be able to connect to the firewall
to communicate the IP address to username mappings to the firewall.
The following table lists the communication requirements for User-ID
along with the port numbers required to establish connections. 

 Destination Port 

 Protocol 

 Description 

 389 

 TCP 

 Port the firewall uses to connect to an
LDAP server (plaintext or Start Transport Layer Security ( Start TLS ) to Map
Users to Groups . 

 3268 

 TCP 

 Port the firewall uses to connect to an
Active Directory global catalog server (plaintext or Start TLS ) to Map
Users to Groups . 

 636 

 TCP 

 Port the firewall uses for LDAP over SSL
connections with an LDAP server to Map
Users to Groups . 

 3269 

 TCP 

 Port the firewall uses for LDAP over SSL
connections with an Active Directory global catalog server to Map
Users to Groups . 

 514 

 6514 

 TCP 

 UDP 

 SSL 

 Port the User-ID agent listens on for authentication
syslog messages if you Configure
User-ID to Monitor Syslog Senders for User Mapping . The port
depends on the type of agent and protocol: 

 PAN-OS
integrated User-ID agent—Port 6514 for SSL and port 514 for UDP. 

 Windows-based User-ID agent—Port 514 for both TCP and UDP. 

 5007 

 TCP 

 Port the firewall listens on for user mapping
information. The agent sends the IP address and username mapping
along with a timestamp whenever it learns of a new or updated mapping.
In addition, it refreshes known mappings. 

 5006 

 TCP 

 Port the User-ID agent listens on for XML
API requests. The source for this communication is typically
the system running a script that invokes the API. 

 88 

 UDP/TCP 

 Port the User-ID agent uses to authenticate
to a Kerberos server. The firewall tries UDP first and falls back
to TCP. 

 1812 

 UDP 

 Port the User-ID agent uses to authenticate
to a RADIUS server. 

 49 

 TCP 

 Port the User-ID agent uses to authenticate
to a TACACS+ server. 

 135 

 TCP 

 Port the User-ID agent uses to establish
TCP-based WMI connections with the Microsoft Remote Procedure Call
(RPC) Endpoint Mapper. The Endpoint Mapper then assigns the agent
a randomly assigned port in the 49152-65535 port range. The agent uses
this connection to make RPC queries for Exchange Server or AD server
security logs, session tables. This is also the port used to access
Terminal Servers. 

 The User-ID agent also uses this port to
connect to client systems to perform Windows Management Instrumentation (WMI) probing . 

 139 

 TCP 

 Port the User-ID agent uses to establish
TCP-based NetBIOS connections to the AD server so that it can send
RPC queries for security logs and session information. 

 445 

 TCP 

 Port the User-ID agent uses
to connect to the Active Directory (AD) using TCP-based SMB connections
to the AD server for access to user logon information (print spooler
and Net Logon). 

 5985 

 HTTP 

 Port the User-ID agent uses
to monitor security logs and session information with the WinRM
protocol over HTTP. 

 5986 

 HTTPS 

 Port the User-ID agent uses to monitor security
logs and session information with the WinRM protocol over HTTPS. 

 5009 

 TCP 

 Port the firewall uses to connect to the
Terminal Server Agent. 

 Previous 

 Ports Used for GlobalProtect 

 Next 

 Ports Used for IPSec 

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

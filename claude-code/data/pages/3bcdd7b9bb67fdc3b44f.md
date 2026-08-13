---
url: https://docs.paloaltonetworks.com/ngfw/help/10-2/network/network-gre-tunnels/gre-tunnels
fetched_at: 2026-08-13T16:43:47Z
source: palo-alto-main
---

# GRE Tunnels Clear

GRE Tunnels 

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

 GRE Tunnels 

 Updated on 

 Thu Jun 25 17:37:48 PDT 2026 

 Focus 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 한국어 (Korean) 

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

 Thu Jun 25 17:37:48 PDT 2026 

 Focus 

 Home 

 Next-Generation Firewall 

 Network 

 Network > GRE
Tunnels 

 GRE Tunnels 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 한국어 (Korean) 

 Next-Generation Firewall 

 GRE Tunnels 

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

 Network > GRE Tunnels 

 Next 

 Network > DHCP 

 GRE Tunnels 

 Configure a logical, point-to-point tunnel to encapsulate
a payload protocol. 

 Network > GRE Tunnels 

 First configure a tunnel interface ( Network > Interfaces
> Tunnel ). Then add a generic routing encapsulation (GRE)
Tunnel and provide the following information, referencing the tunnel
interface you created: 

 GRE Tunnel Fields 

 Description 

 Name 

 Name of the GRE tunnel. 

 Interface 

 Select the interface to use as the local GRE
tunnel endpoint (source interface), which is an Ethernet interface
or subinterface, an Aggregate Ethernet (AE) interface, a loopback interface,
or a VLAN interface. 

 Local Address 

 Select the local IP address of the interface
to use as the tunnel interface address. 

 Peer Address 

 Enter the IP address at the opposite end of
the GRE tunnel. 

 Tunnel Interface 

 Select the Tunnel interface that you configured.
(This interface identifies the tunnel when it is the next hop for
routing.) 

 TTL 

 Enter the TTL for the IP packet encapsulated
in the GRE packet (range is 1 to 255; default is 64). 

 ERSPAN 

 Select to enable the firewall to decapsulate
Encapsulated Remote Switched Port Analyzer (ERSPAN) data sent through
the GRE tunnel. You can configure a network switch to use ERSPAN
to send mirrored traffic through a GRE tunnel to the firewall for
use by Security services like IoT Security. After decapsulating
the data, the firewall inspects it similar to how it inspects traffic
received on a TAP port. It then creates enhanced application logs (EALs)
and traffic, threat, WildFire, URL, data, GTP (when GTP is enabled), SCTP
(when SCTP is enabled), tunnel, auth, and decryption logs. The firewall forwards
these logs to the logging service where IoT Security accesses and analyzes
the data. 

 Copy ToS Header 

 Select to copy the Type of Service (ToS) field
from the inner IP header to the outer IP header of the encapsulated
packets to preserve the original ToS information. 

 Keep Alive 

 Select to enable the Keep Alive function for
the GRE tunnel (disabled by default). If you enable Keep Alive,
by default it takes three unreturned keepalive packets (Retries)
at 10-second intervals for the GRE tunnel to go down, and it takes
five Hold Timer intervals at 10-second intervals for the GRE tunnel
to come back up. 

 Interval (sec) 

 Set the interval between keepalive packets
that the local end of the GRE tunnel sends to the tunnel peer, and
the interval that each Hold Timer waits after successful keepalive
packets before the firewall re-establishes communication with the
tunnel peer (range is 1 to 50; default is 10). 

 Retry 

 Set the number of intervals that keepalive
packets are not returned before the firewall considers the tunnel
peer to be down (range is 1 to 255; default is 3). 

 Hold Timer 

 Set the number of intervals that keepalive
packets are successful before the firewall re-establishes communication
with the tunnel peer (range is 1 to 64; default is 5). 

 Previous 

 Network > GRE Tunnels 

 Next 

 Network > DHCP 

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

 PAN-OS 

 10.2 

 Next-Generation Firewall 

 Help 

 Web Interface 

 Panorama 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

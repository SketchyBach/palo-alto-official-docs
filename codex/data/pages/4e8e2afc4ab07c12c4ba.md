---
url: https://docs.paloaltonetworks.com/ngfw/help/10-2/device/device-setup-services/global-services-settings
fetched_at: 2026-08-13T16:43:20Z
source: palo-alto-main
---

# Global Services Settings Clear

Global Services Settings 

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

 Global Services Settings 

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

 Device 

 Device > Setup > Services 

 Global Services Settings 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 한국어 (Korean) 

 Next-Generation Firewall 

 Global Services Settings 

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

 Configure Services for Global and Virtual Systems 

 Next 

 IPv4 and IPv6 Support for Service Route Configuration 

 Global Services Settings 

 Device > Setup > Services 

 To control and redirect DNS queries between shared and specific
virtual systems, you can use a DNS proxy and a DNS Server profile . 

 Global Services Settings 

 Description 

 Services 

 Update Server 

 Represents the IP address or host name of
the server from which to download updates from Palo Alto Networks.
The current value is updates.paloaltonetworks.com .
Do not change this setting unless instructed by technical support. 

 Verify Update Server Identity 

 If you enable this option, the firewall
or Panorama will verify that the server from which the software
or content package is download has an SSL certificate signed by
a trusted authority. This adds an additional level of security for
the communication between firewalls or Panorama servers and the update
server. 

 Verify the update server identity
to validate that the server has an SSL certificate signed by a trusted
authority. 

 DNS Settings 

 Choose the type of DNS service— Servers or DNS
Proxy Object —for all DNS queries that the firewall initiates
in support of FQDN address objects, logging, and firewall management.
Options include: 

 Primary and secondary DNS servers
to provide domain name resolution. 

 A DNS proxy configured on the firewall as an alternative
to configuring DNS servers. If you enable a DNS proxy, you must
enable Cache and EDNS Cache Responses ( Network DNS Proxy Advanced ). 

 Primary DNS Server 

 Enter the IP address of the primary DNS
server for DNS queries from the firewall. For example, to find the
update server, to resolve DNS entries in logs, or resolve FDQN-based
address objects. 

 Secondary DNS Server 

 ( Optional ) Enter the IP address
of a secondary DNS server to use if the primary server is unavailable. 

 Minimum FQDN Refresh Time (sec) 

 Set a limit on how fast the firewall refreshes
FQDNs that it receives from a DNS. The firewall refreshes an FQDN
based on the TTL of the FQDN as long as the TTL is greater than
or equal to this Minimum FQDN Refresh Time (in
seconds). If the TTL is less than this Minimum FQDN Refresh Time,
the firewall refreshes the FQDN based on this Minimum FQDN Refresh
Time (that is, the firewall does not honor TTLs faster than this setting).
The timer starts when the firewall receives a DNS response from
the DNS server or DNS proxy object resolving the FQDN (range is
0 to 14,400; default is 30). A setting of 0 means the firewall will
refresh the FQDN based on the TTL value in the DNS and does not
enforce a minimum FQDN refresh time. 

 If
the TTL for the FQDN in the DNS is short, but FQDN resolutions don’t
change as frequently as the TTL timeframe so don’t require a faster
refresh, you should set a minimum FQDN Refresh Time to avoid unnecessary
FQDN refresh attempts. 

 FQDN Stale Entry Timeout (min) 

 Specify the length of time (in minutes)
that the firewall continues to use stale FQDN resolutions in the
event of a network failure or unreachable DNS server —when an FQDN
is not getting refreshed (range is 0 to 10,080; default is 1,440).
A value of 0 means the firewall does not continue to use a stale entry.
If the DNS server is still unreachable at the end of the state timeout,
the FQDN entry becomes unresolved (stale resolutions are removed). 

 Make sure the FQDN Stale Entry Timeout value
is short enough to not allow incorrect traffic forwarding (which
poses a security risk), but is long enough to allow traffic continuity
without causing an unplanned network outage. 

 Proxy Server section 

 Server 

 If the firewall needs to use a proxy server
to reach Palo Alto Networks update services, enter the IP address
or host name of the proxy server. 

 Port 

 Enter the port for the proxy server. 

 User 

 Enter the username for the administrator
to enter when accessing the proxy server. 

 Password/Confirm Password 

 Enter and confirm the password for the administrator
to enter when accessing the proxy server. 

 Use proxy to send logs to Strata Logging Service 

 Enable the firewall to send logs to Strata Logging Service through the proxy server. 

 NTP 

 NTP Server Address 

 Enter the IP address or hostname of an NTP
server that you will use to synchronize the clock on the firewall.
Optionally, you can enter the IP address or hostname of a second
NTP server to synchronize the clock on the firewall if the primary
server becomes unavailable. 

 When an
NTP server keeps all network firewall clocks synchronized, scheduled
jobs run as expected and timestamps can help identify the root causes
of issues that involve multiple devices. Configure a primary and
a secondary NTP server in case the primary NTP server becomes unreachable. 

 Authentication Type 

 You can enable the firewall to authenticate
time updates from an NTP server. For each NTP server, select the
type of authentication for the firewall to use: 

 None (default)—Select
this option to disable NTP Authentication. 

 Symmetric Key —Select this option for the
firewall to use symmetric key exchange (shared secrets) to authenticate time
updates from the NTP server. If you select Symmetric Key, continue
by specifying the following values: 

 Key
ID —Enter the Key ID (1–65534). 

 Algorithm —Select the MD5 or SHA1 algorithm
to use for NTP authentication. 

 Authentication Key/Confirm Authentication Key —Enter
and confirm the authentication key for the authentication algorithm. 

 Autokey —Select this option for the firewall
to use autokey (public key cryptography) to authenticate time updates
from the NTP server. 

 Enable
NTP server authentication so that the NTP server approves the client
and provides synchronized updates. 

 Previous 

 Configure Services for Global and Virtual Systems 

 Next 

 IPv4 and IPv6 Support for Service Route Configuration 

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

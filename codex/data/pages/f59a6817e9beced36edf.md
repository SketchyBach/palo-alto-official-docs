---
url: https://docs.paloaltonetworks.com/ngfw/help/11-1/policies/policies-sd-wan/sd-wan-source-tab
fetched_at: 2026-08-13T16:46:56Z
source: palo-alto-main
---

# SD-WAN Source Tab Clear

SD-WAN Source Tab 

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

 SD-WAN Source Tab 

 Updated on 

 Thu Jun 25 17:39:35 PDT 2026 

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

 Thu Jun 25 17:39:35 PDT 2026 

 Focus 

 Home 

 Next-Generation Firewall 

 Policies 

 Policies > SD-WAN 

 SD-WAN Source Tab 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 한국어 (Korean) 

 Next-Generation Firewall 

 SD-WAN Source Tab 

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

 SD-WAN General Tab 

 Next 

 SD-WAN Destination Tab 

 SD-WAN Source Tab 

 Source tab in the SD-WAN policy rule configuration window. 

 Policies SD-WAN Source 

 Select the Source tab to
define the source zones, source addresses, and source users that
define the incoming packets to which the SD-WAN policy applies. 

 Field 

 Description 

 Source Zone 

 To specify a source zone, select Add and
select one or more zones, or select Any zone. 

 Specifying
multiple zones can simplify management. For example, if you have
three branches in different zones and you want the remaining match
criteria and path selection to be the same for the three branches,
you can create one SD-WAN rule and specify the three source zones
to cover the three branches. 

 Only Layer 3 type zones
are supported for SD-WAN policy rules. 

 Source Address 

 To specify source addresses, Add source
addresses or external dynamic lists (EDL), select from the drop-down,
or select Address and create a new address
object. Alternatively, select Any source
address (default). 

 Source User 

 To specify certain users, select Add (the
type then indicates select ) and enter a user,
list of users, or groups of users. Alternatively, select a type
of user: 

 any —(default) Include
any user, regardless of user data. 

 pre-logon —Include remote users who
are connected to the network using GlobalProtect™, but are not logged
into their system. When the Pre-logon option is configured on the
Portal for GlobalProtect apps, any user who is not currently logged
into their machine will be identified with the username pre-logon.
You can then create policies for pre-logon users and although the
user is not logged in directly, their machines are authenticated
on the domain as if they were fully logged in. 

 known-user —Includes all authenticated
users, which means any IP address with user data mapped. This option
is equivalent to the “domain users” group on a domain. 

 unknown —Includes all unauthenticated
users, which means IP addresses that are not mapped to a user. For
example, you could select unknown for guest-level
access to something because they will have an IP address on your
network, but will not be authenticated to the domain and will not
have IP address-to-user mapping information on the firewall. 

 If
the firewall collects user information from a RADIUS, TACACS+, or
SAML identity provider server and not from the User-ID™ agent, the
list of users does not display; you must enter user information
manually. 

 Previous 

 SD-WAN General Tab 

 Next 

 SD-WAN Destination Tab 

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

 11.1 

 Next-Generation Firewall 

 Help 

 Web Interface 

 Panorama 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

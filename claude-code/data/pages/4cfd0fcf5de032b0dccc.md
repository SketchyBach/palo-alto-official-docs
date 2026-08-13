---
url: https://docs.paloaltonetworks.com/ngfw/networking/dhcp/configure-the-management-interface-as-a-dhcp-client
fetched_at: 2026-08-13T16:53:54Z
source: palo-alto-main
---

# Configure the Management Interface as a DHCP Client Clear

Configure the Management Interface as a DHCP Client 

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

 Configure the Management Interface as a DHCP Client 

 Updated on 

 Tue Aug 04 17:04:37 PDT 2026 

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

 Tue Aug 04 17:04:37 PDT 2026 

 Focus 

 Home 

 Next-Generation Firewall 

 DHCP 

 Configure the Management Interface as a DHCP Client 

 Download PDF 

 Next-Generation Firewall 

 Configure the Management Interface as a DHCP Client 

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

 Configure an Interface as a DHCPv6 Client with Prefix Delegation 

 Next 

 Configure the Management Interface for Dynamic IPv6 Address Assignment 

 Configure the Management Interface as a DHCP Client 

 Procedure to configure the management interface as a DHCP client. 

 Where Can I Use This? What Do I Need? 

 NGFW (Managed by PAN-OS or Panorama) 

 The management interface on the firewall supports
DHCP client for IPv4, which allows the management interface to receive
its IPv4 address from a DHCP server. The management interface also
supports DHCP Option 12 and Option 61, which allow the firewall
to send its hostname and client identifier, respectively, to DHCP
servers. 

 Beginning in PAN-OS 11.1.0, the management interface also
 supports Dynamic IPv6 Address
 Assignment . 

 By default, VM-Series firewalls deployed in AWS and
Azure™ use the management interface as a DHCP client to obtain its IP
address, rather than a static IP address, because cloud deployments
require the automation this feature provides. DHCP on the management
interface is turned off by default for the VM-Series firewall except
for the VM-Series firewall in AWS and Azure. The management interfaces
on WildFire and Panorama models do not support this DHCP functionality. 

 For hardware-based firewall models
(not VM-Series), configure the management interface with a static
IP address when possible. 

 If the firewall acquires a management interface address through DHCP, assign a MAC address
 reservation on the DHCP server that serves that firewall. The reservation
 ensures that the firewall retains its management IP address after a restart.
 If the DHCP server is a Palo Alto Networks ® firewall, see Step 6
 of Configure an Interface as
 a DHCP Server for reserving an address. 

 If
you configure the management interface as a DHCP client, the following
restrictions apply: 

 You cannot use the management
interface in an HA configuration for control link (HA1 or HA1 backup),
data link (HA2 or HA2 backup), or packet forwarding (HA3) communication. 

 You cannot select MGT as the Source
Interface when you customize service routes ( Device Setup Services Service
Route Configuration Customize ).
However, you can select Use default to route
the packets via the management interface. 

 You cannot use the dynamic IP address of the management interface
to connect to a Hardware Security Module (HSM). The IP address on
the HSM client firewall must be a static IP address because HSM
authenticates the firewall using the IP address, and operations
on HSM would stop working if the IP address were to change during
runtime. 

 A prerequisite for this task is that the
management interface must be able to reach a DHCP server. 

 Configure the Management interface as a DHCP client
so that it can receive its IP address (IPv4), netmask (IPv4), and
default gateway from a DHCP server. 

 Optionally, you can also send the hostname and client identifier
of the management interface to the DHCP server if the orchestration
system you use accepts this information. 

 Select Device Setup Interfaces and select the Management 
 interface. 

 Selections unrelated to a dynamic address
 (such as speed, MTU, permitted IP addresses, administrative
 management services, and network services) are documented in the
 PAN-OS Administrator's Guide: Getting Started / Integrate the
 Firewall into Your Management Network / Initial
 Configuration . 

 Select IPv4 . 

 For Type , select DHCP
 Client . 

 ( Optional ) Select one or both options for the firewall to send to the DHCP server in
 DHCP Discover or Request messages: 

 Send Hostname —Sends the Hostname (as
defined in Device Setup Management ) as part of DHCP
Option 12. 

 Send Client ID —Sends the client identifier
as part of DHCP Option 61. A client identifier uniquely identifies
a DHCP client, and the DHCP Server uses it to index its configuration
parameter database. 

 Click OK . 

 ( Optional ) Configure the firewall to accept
the host name and domain from the DHCP server. 

 Select Device Setup Management and
edit General Settings. 

 Select one or both options: 

 Accept DHCP server provided Hostname —Allows
the firewall to accept the hostname from the DHCP server (if valid).
When enabled, the hostname from the DHCP server overwrites any existing Hostname specified
in Device Setup Management . Don’t select this
option if you want to manually configure a hostname. 

 Accept DHCP server provided Domain —Allows
the firewall to accept the domain from the DHCP Server. The domain
(DNS suffix) from the DHCP Server overwrites any existing Domain specified
in Device Setup Management . Don’t select this
option if you want to manually configure a domain. 

 Click OK . 

 Commit your changes. 

 Click Commit . 

 View DHCP client information. 

 Select Device Setup Interfaces and select the Management interface. 

 Click Show DHCP Client Runtime Info . 

 ( Optional ) Renew the DHCP lease with
the DHCP server, regardless of the lease term. 

 This option is convenient if you are testing or troubleshooting
network issues. 

 Select Device Setup Interfaces and select the Management interface. 

 Click Show DHCP Client Runtime Info . 

 Click Renew . 

 ( Optional ) Release the following DHCP options
that came from the DHCP server: 

 IP Address 

 Netmask 

 Default Gateway 

 DNS Server (primary and secondary) 

 NTP Server (primary and secondary) 

 Domain (DNS Suffix) 

 A
release frees the IP address, which drops your network connection
and renders the firewall unmanageable if no other interface is configured
for management access. 

 Use the CLI operational command request dhcp client management-interface release . 

 Previous 

 Configure an Interface as a DHCPv6 Client with Prefix Delegation 

 Next 

 Configure the Management Interface for Dynamic IPv6 Address Assignment 

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

 Networking 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

---
url: https://docs.paloaltonetworks.com/pan-os/10-1/pan-os-networking-admin/configure-interfaces/use-interface-management-profiles-to-restrict-access
fetched_at: 2026-08-13T17:02:36Z
source: palo-alto-main
---

# Use Interface Management Profiles to Restrict Access Clear

Use Interface Management Profiles to Restrict Access 

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

 Use Interface Management Profiles to Restrict Access 

 Updated on 

 Aug 4, 2026 

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

 Aug 4, 2026 

 Focus 

 Home 

 Next-Generation Firewall 

 Configure Interfaces 

 Use Interface Management Profiles to Restrict Access 

 Download PDF 

 Next-Generation Firewall 

 Use Interface Management Profiles to Restrict Access 

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

 Configure Bonjour Reflector for Network Segmentation 

 Next 

 Configure a Breakout Port Interface and Subinterface 

 Use Interface Management Profiles to Restrict Access 

 Restrict protocols, services, and IP addresses on Layer 3 Ethernet interfaces or
 subinterfaces, or on logical interfaces (aggregate group, VLAN, loopback, and tunnel
 interfaces). 

 Where Can I Use This? What Do I Need? 

 NGFW (Managed by PAN-OS or Panorama) 

 An Interface Management profile protects the
firewall from unauthorized access by defining the protocols, services,
and IP addresses that a firewall interface permits for management
traffic. For example, you might want to prevent users from accessing
the firewall web interface over the ethernet1/1 interface but allow
that interface to receive SNMP queries from your network monitoring
system. In this case, you would enable SNMP and disable HTTP/HTTPS
in an Interface Management profile and assign the profile to ethernet1/1. 

 You
can assign an Interface Management profile to Layer 3 Ethernet interfaces
(including subinterfaces) and to logical interfaces (aggregate group,
VLAN, loopback, and tunnel interfaces). If you do not assign an
Interface Management profile to an interface, it denies access for
all IP addresses, protocols, and services by default. 

 The
management (MGT) interface does not require an Interface Management
profile. You restrict protocols, services, and IP addresses for
the MGT interface when you perform initial configuration of
the firewall. In case the MGT interface goes down, allowing management
access over another interface enables you to continue managing the
firewall. 

 When enabling access
to a firewall interface using an Interface Management profile, do
not enable management access (HTTP, HTTPS, SSH, or Telnet) from
the internet or from other untrusted zones inside your enterprise
security boundary, and never enable HTTP or Telnet access because
those protocols transmit in cleartext. Follow the Best Practices for Securing Administrative
Access to ensure that you are properly securing management
access to your firewall. 

 Configure the Interface Management profile. 

 Select Network Network Profiles Interface Mgmt and
click Add . 

 Select the protocols that the interface permits for
management traffic: Ping , Telnet , SSH , HTTP , HTTP
OCSP , HTTPS , or SNMP . 

 Don’t enable HTTP or Telnet because
those protocols transmit in cleartext and therefore aren’t secure. 

 Select the services that the interface permits for
management traffic: 

 Response Pages —Use to enable
response pages for: 

 Captive Portal —To serve
Captive Portal response pages, the firewall leaves ports open on
Layer 3 interfaces: 6081 for Captive Portal in transparent mode
and 6082 for Captive Portal in redirect mode. For details, see Authentication Policy and Authentication
Portal . 

 URL Admin Override —For details, see Allow Password Access to Certain
Sites . 

 User-ID —Use to Redistribute Data and Authentication
Timestamps . 

 User-ID Syslog Listener-SSL or User-ID
Syslog Listener-UDP —Use to Configure User-ID to Monitor
Syslog Senders for User Mapping over SSL or UDP. 

 ( Optional ) Add the
Permitted IP Addresses that can access the interface. If you don’t
add entries to the list, the interface has no IP address restrictions. 

 Click OK . 

 Assign the Interface Management profile to an interface. 

 Select Network Interfaces , select the type
of interface ( Ethernet , VLAN , Loopback ,
or Tunnel ), and select the interface. 

 Select Advanced Other info and select the Interface Management
Profile you just added. 

 Click OK and Commit . 

 Previous 

 Configure Bonjour Reflector for Network Segmentation 

 Next 

 Configure a Breakout Port Interface and Subinterface 

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

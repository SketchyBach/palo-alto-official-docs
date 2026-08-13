---
url: https://docs.paloaltonetworks.com/ngfw/networking/configure-interfaces/configure-a-pppoe-client-on-a-subinterface/configure-a-pppoe-client-on-a-subinterface-pan-os
fetched_at: 2026-08-13T16:53:47Z
source: palo-alto-main
---

# Configure a PPPoE Client on a Subinterface (PAN-OS) Clear

Configure a PPPoE Client on a Subinterface (PAN-OS) 

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

 Configure a PPPoE Client on a Subinterface (PAN-OS) 

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

 Configure Interfaces 

 Configure a PPPoE Client on a Subinterface 

 Configure a PPPoE Client on a Subinterface (PAN-OS) 

 Download PDF 

 Next-Generation Firewall 

 Configure a PPPoE Client on a Subinterface (PAN-OS) 

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

 Configure a PPPoE Client on a Subinterface (PAN-OS) 

 Configure a PPPoE Client on a subinterface to connect to your ISP using an 802.1Q
 VLAN tag in PAN-OS. 

 Configure a subinterface as a PPPoE client (termination point). 

 Select Network Interfaces Ethernet and highlight a Layer 3 Ethernet interface. 

 Add Subinterface . 

 To the right of the Interface Name and dot,
 enter the subinterface number; use the VLAN tag number that your ISP
 provided. This subinterface number is for reference purposes; the VLAN
 tag ID is read from the Tag field. 

 Enter the Tag , which is the VLAN tag number that
 your ISP provided. The actual VLAN tag ID is read from this Tag
 field. 

 Select IPv4 . 

 Select the Type of address as
 PPPoE . 

 Select General and Enable 
 the subinterface. 

 Enter the Username for the authentication you
 will choose in the next step. 

 Enter the Password and Confirm
 Password . 

 Configure additional characteristics of the PPPoE subinterface. 

 Select Advanced . 

 Select the type of Authentication : 

 None —(default) If you keep this setting,
 the firewall selects auto as the
 authentication protocol. 

 CHAP —Firewall uses Challenge Handshake
 Authentication Protocol (CHAP). 

 PAP —Firewall uses Password Authentication
 Protocol (PAP). PAP sends usernames and passwords in plain text,
 and is less secure than CHAP. 

 auto —Firewall negotiates the
 authentication method (CHAP or PAP) with the PPPoE server. 

 To request that the PPPoE server assign a certain IPv4 address for the
 subinterface, specify a Static Address . (The
 PPPoE server may assign the requested address or a different address at
 its discretion.) Default is None . 

 To automatically create a default route that points to the default
 gateway that the PPPoE server provides, select automatically
 create default route pointing to peer . 

 Enter the Default Route Metric (priority level)
 of the PPPoE connection; range is 1 to 65,535; default is 10. A route
 with a lower number has higher priority during route selection. For
 example, a route with a metric of 10 is used before a route with a
 metric of 100. 

 Enter the name of the Access Concentrator that
 your ISP provided, if any (string value of 0 to 255 characters). The
 firewall will connect with this Access Concentrator. 

 Enter the Service that your ISP provided, if any
 (string value of 0 to 255 characters). 

 If you want the PPPoE client (firewall) to wait for the PPPoE server to
 initiate a connection, select Passive . If Passive
 is not selected, the firewall is allowed to initiate a connection. 

 Click OK . 

 Commit the changes. 

 View information about the PPPoE client. The Local IP Address, Primary DNS,
 Secondary DNS, Primary WINS, Secondary WINS, Remote IP Address, Access
 Concentrator name, and AC MAC address were received from the PPPoE server. 

 Select Network Interfaces Ethernet and in the row of the subinterface that you configured,
 select Dynamic-PPPoE . 

 Alternatively, you can select the
 subinterface, IPv4 , and Show PPPoE
 Client Runtime Info . 

 Close the window. 

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

 © 2026 Palo Alto Networks, Inc. All rights reserved.

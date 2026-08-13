---
url: https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-networking-admin/nat/configure-nat/enable-clients-on-the-internal-network-to-access-your-public-servers-destination-u-turn-nat
fetched_at: 2026-08-13T17:11:08Z
source: palo-alto-main
---

# Enable Clients on the Internal Network to Access your Public
Servers (Destination U-Turn NAT) Clear

Enable Clients on the Internal Network to Access your Public
Servers (Destination U-Turn NAT) 

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

 Enable Clients on the Internal Network to Access your Public
Servers (Destination U-Turn NAT) 

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

 NAT 

 Configure NAT 

 Enable Clients on the Internal Network to Access your Public
Servers (Destination U-Turn NAT) 

 Download PDF 

 Next-Generation Firewall 

 Enable Clients on the Internal Network to Access your Public
Servers (Destination U-Turn NAT) 

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

 Create a Source NAT Rule with Persistent DIPP 

 Next 

 Enable Bi-Directional Address Translation for Your Public-Facing Servers (Static Source NAT) 

 Enable Clients on the Internal Network to Access your Public
Servers (Destination U-Turn NAT) 

 Configure destination U-turn NAT to enable clients on the internal network to access
 your public servers. 

 Where Can I Use This? What Do I Need? 

 NGFW (Managed by PAN-OS or Panorama) 

 When a user on the internal network sends
a request for access to the corporate web server in the DMZ, the
DNS server will resolve it to the public IP address. When processing
the request, the firewall will use the original destination in the
packet (the public IP address) and route the packet to the egress
interface for the untrust zone. In order for the firewall to know
that it must translate the public IP address of the web server to
an address on the DMZ network when it receives requests from users
on the trust zone, you must create a destination NAT rule that will
enable the firewall to send the request to the egress interface
for the DMZ zone as follows. 

 Create an address object for the web server. 

 Select Objects Addresses and Add a Name and
optional Description for the address object. 

 For Type , select IP
Netmask and enter the public IP address of the web server,
203.0.113.11 in this example. 

 You can switch the address object type from IP
Netmask to FQDN by clicking Resolve ,
and when the FQDN appears, click Use this FQDN .
Alternatively, for Type , select FQDN and
enter the FQDN to use for the address object. If you enter an FQDN
and click Resolve , the IP address to which
the FQDN resolves appears in the field. To switch the address object Type from
an FQDN to an IP Netmask using this IP address, click Use
this address and the Type will
switch to IP Netmask with the IP address
appearing in the field. 

 Click OK . 

 Create the NAT policy. 

 Select Policies NAT and click Add . 

 On the General tab, enter a
descriptive Name for the NAT rule. 

 On the Original Packet tab,
select the zone you created for your internal network in the Source
Zone section (click Add and then
select the zone) and the zone you created for the external network
from the Destination Zone list. 

 In the Destination Address section, Add the
address object you created for your public web server. 

 On the Translated Packet tab,
for Destination Address Translation, for Translation
Type , select Static IP and then
enter the IP address that is assigned to the web server interface
on the DMZ network, 10.1.1.11 in this example. Alternatively, you
can select Translation Type to be Dynamic
IP (with session distribution) and enter the Translated
Address to be an address object or address group that
uses an IP netmask, IP range, or FQDN. Any of these can return multiple addresses
from DNS. If the translated destination address resolves to more
than one address, the firewall distributes incoming NAT sessions
among the multiple addresses based on one of several methods you
can select: Round Robin (the default method), Source
IP Hash , IP Modulo , IP
Hash , or Least Sessions . 

 Click OK . 

 Click Commit . 

 Previous 

 Create a Source NAT Rule with Persistent DIPP 

 Next 

 Enable Bi-Directional Address Translation for Your Public-Facing Servers (Static Source NAT) 

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

---
url: https://docs.paloaltonetworks.com/ngfw/networking/using-proxy-arp-dhcp-relay-overwrite/configure-proxy-arp
fetched_at: 2026-08-13T16:54:21Z
source: palo-alto-main
---

# Configure Proxy ARP on a Layer 3 Interface Clear

Configure Proxy ARP on a Layer 3 Interface 

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

 Configure Proxy ARP on a Layer 3 Interface 

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

 Proxy ARP and DHCP Relay Overwrite 

 Configure Proxy ARP on a Layer 3 Interface 

 Download PDF 

 Next-Generation Firewall 

 Configure Proxy ARP on a Layer 3 Interface 

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

 Proxy ARP and DHCP Relay Overwrite 

 Next 

 DHCP Relay Overwrite 

 Configure Proxy ARP on a Layer 3 Interface 

 Enable Proxy ARP on a Layer 3 interface so the firewall intercepts ARP requests and
 redirects intra-VLAN traffic for security inspection and policy enforcement. 

 Where Can I Use This? What Do I Need? 

 NGFW 

 PAN-OS 12.2.2 or a later release 

 One of these licenses when using Strata Cloud Manager 
 Strata Cloud Manager Essentials 

 Strata Cloud Manager Pro 

 Once Proxy ARP is enabled on an interface, the firewall intercepts ARP
 requests for all addresses within the interface's subnet by default and replies with
 its own MAC address. The requesting device then sends its traffic to the firewall
 instead of directly to the destination device, enabling the firewall to apply
 security policy, including App-ID™, User-ID™, and Device-ID inspection, before
 forwarding the traffic. 

 Apart from interface subnets, you can configure additional address entries
 for Proxy ARP. You can configure negate entries to exclude specific addresses from
 Proxy ARP. When a device sends an ARP request for a negated address, the firewall
 does not respond, allowing that traffic to bypass Proxy ARP. 

 You can configure up to 500 Proxy ARP address entries per interface.
 Individual IP addresses and subnets each count as one entry. IP address ranges are
 expanded into CIDR prefixes, and each resulting prefix counts as one entry. The
 overall number of devices the firewall can proxy ARP for is also bounded by the
 firewall's ARP table limit; when the table is full, new ARP entries cannot be
 created and devices may lose the ability to reach each other through the firewall.
 When you configure both a range and a specific address within that range with
 different negate settings, configure the more specific entry (such as a /32 single
 address) before the broader range entry. The firewall uses longest-prefix match to
 select the applicable entry, so a more specific entry takes priority. 

 Hosts cache ARP entries until a timer expires. If a host is added to the negate list
 on the firewall, the device can still continue to send traffic until its cached ARP
 entry expires. When you add a negate entry to an existing Proxy ARP configuration,
 devices that already have the firewall's MAC address cached for that address
 continue to send traffic to the firewall until their ARP cache expires. The negate
 entry takes effect only for new ARP requests. 

 After enabling the feature, confirm it is active by running show counter
 global | match proxy and verifying the
 flow_proxyarp_resp_sent counter is incrementing. 

 Configure Proxy ARP on a Layer 3 Interface (PAN-OS & Panorama) 

 Configure Proxy ARP on a Layer 3 Interface (Strata Cloud Manager) 

 Configure Proxy ARP on a Layer 3 Interface (PAN-OS & Panorama) 

 Enable Proxy ARP on a Layer 3 interface so the firewall intercepts ARP requests and
 redirects intra-VLAN traffic for security inspection and policy enforcement. 

 Select an interface. 

 Select Network Interfaces , then select Ethernet (and 
 Interface Type as Layer 3 ),
 VLAN , or Aggregate
 Ethernet (and Interface Type as
 Layer 3 ). 

 For a sub-interface, expand the parent interface and select the
 sub-interface. 

 Enable Proxy ARP in the Layer 3 interface. 

 Select Advanced Proxy ARP and enable Proxy ARP . 

 Add the IP addresses for which the firewall intercepts and responds to ARP
 requests. 

 In the Address table, click
 Add and enter one of the following: 

 An individual IP address, for example
 192.168.100.10 

 A subnet in CIDR notation, for example
 192.168.100.0/24 

 An IP address range, for example
 192.168.100.10-192.168.100.50 

 Repeat to add an entry for each device, subnet, or range on the VLAN. 

 ( Optional ) To prevent the firewall from responding to ARP requests for
 a specific address, enable Negate for that entry.
 Configure more specific negate entries, such as individual /32 addresses, before
 broader range entries to ensure correct longest-prefix-match behavior. 

 Select OK and then Commit . 

 After committing, confirm the configuration is active. Run test proxy-arp
 interface <interface-name> target-ip <ip-address> on the CLI. The
 output Proxy ARP entry found - proxy ARP will respond for this
 address confirms the firewall responds to ARP requests for that
 address. The output Proxy ARP entry not found - proxy ARP will not respond
 for this address indicates the address is not in the Proxy ARP list or
 is negated. 

 Configure Proxy ARP on a Layer 3 Interface (Strata Cloud Manager) 

 Enable Proxy ARP on a Layer 3 interface so the firewall intercepts ARP requests and
 redirects intra-VLAN traffic for security inspection and policy enforcement. 

 Log in to Strata Cloud Manager. 

 Configure Layer 3 interface . 

 Enable Proxy ARP in the Layer 3 interface. 

 Select Advanced Proxy ARP and enable Proxy ARP . 

 Add the IP addresses for which the firewall intercepts and responds to ARP
 requests. 

 In the Address table, click Add 
 and enter one of the following: 

 An individual IP address, for example
 192.168.100.10 

 A subnet in CIDR notation, for example
 192.168.100.0/24 

 An IP address range, for example
 192.168.100.10-192.168.100.50 

 Repeat to add an entry for each device, subnet, or range on the VLAN. 

 ( Optional ) To prevent the firewall from responding to ARP requests for
 a specific address, enable Negate for that entry.
 Configure more specific negate entries, such as individual /32 addresses, before
 broader range entries to ensure correct longest-prefix-match behavior. 

 Select OK and then Commit . 

 After committing, confirm the configuration is active. Run test proxy-arp
 interface <interface-name> target-ip <ip-address> on the CLI. The
 output Proxy ARP entry found - proxy ARP will respond for this
 address confirms the firewall responds to ARP requests for that
 address. The output Proxy ARP entry not found - proxy ARP will not respond
 for this address indicates the address is not in the Proxy ARP list or
 is negated. 

 Previous 

 Proxy ARP and DHCP Relay Overwrite 

 Next 

 DHCP Relay Overwrite 

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

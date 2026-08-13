---
url: https://docs.paloaltonetworks.com/ngfw/networking/configure-interfaces/layer-3-interfaces/manage-ipv6-hosts-using-neighbor-discovery-protocol-ndp
fetched_at: 2026-08-13T16:53:49Z
source: palo-alto-main
---

# Manage IPv6 Hosts Using Neighbor Discovery Protocol (NDP) Clear

Manage IPv6 Hosts Using Neighbor Discovery Protocol (NDP) 

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

 Manage IPv6 Hosts Using Neighbor Discovery Protocol (NDP) 

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

 Layer 3 Interfaces 

 Manage IPv6 Hosts Using Neighbor Discovery Protocol (NDP) 

 Download PDF 

 Next-Generation Firewall 

 Manage IPv6 Hosts Using Neighbor Discovery Protocol (NDP) 

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

 Configure Layer 3 Interfaces 

 Next 

 Enable NDP Monitoring 

 Manage IPv6 Hosts Using Neighbor Discovery Protocol (NDP) 

 Use NDP to manage IPv6 hosts; configure RDNS servers and DNS search list for IPv6
 router advertisements. 

 Where Can I Use This? What Do I Need? 

 NGFW (Managed by PAN-OS or Panorama) 

 The firewall implementation of Neighbor Discovery (ND) is enhanced so
 that you can provision IPv6 hosts with the Recursive DNS Server (RDNSS) Option and
 DNS Search List (DNSSL) Option per RFC 6106 , IPv6 Router Advertisement Options for DNS Configuration .
 When you Configure
 Layer 3 Interfaces , you configure these DNS options on the firewall so
 the firewall can provision your IPv6 hosts. Therefore, you don’t need a separate
 DHCPv6 server to provision the hosts. The firewall sends IPv6 Router Advertisements
 (RAs) containing these options to IPv6 hosts as part of their DNS configuration to
 fully provision them to reach internet services. Thus, your IPv6 hosts are
 configured with: 

 The addresses of RDNS servers that can resolve DNS queries. 

 A list of domain names (suffixes) that the DNS client appends (one at a time)
 to an unqualified domain name before entering the domain name into a DNS
 query. 

 IPv6 Router Advertisement for DNS configuration is supported for Ethernet interfaces,
 subinterfaces, Aggregated Ethernet interfaces, and Layer 3 VLAN interfaces on all
 PAN-OS platforms. 

 The capability of the firewall to send IPv6 RAs for DNS
 configuration allows the firewall to perform a role similar to DHCP, and is
 unrelated to the firewall being a DNS proxy, DNS client or DNS server. 

 After you configure the firewall with the addresses of RDNS servers, the firewall
 provisions an IPv6 host (the DNS client) with those addresses. The IPv6 host uses
 one or more of those addresses to reach an RDNS server. Recursive DNS refers to a
 series of DNS requests by an RDNS Server, as shown with three pairs of queries and
 responses in the following figure. For example, when a user tries to access
 www.paloaltonetworks.com, the local browser sees that it does not have the IP
 address for that domain name in its cache, nor does the client’s operating system
 have it. The client’s operating system launches a DNS query to a Recursive DNS
 Server belonging to the local ISP. 

 An IPv6 Router Advertisement can contain multiple DNS Recursive Server Address
 options, each with the same or different lifetimes. A single DNS Recursive DNS
 Server Address option can contain multiple Recursive DNS Server addresses as long as
 the addresses have the same lifetime. 

 A DNS Search List is a list of domain names (suffixes) that the firewall advertises
 to a DNS client. The firewall thus provisions the DNS client to use the suffixes in
 its unqualified DNS queries. The DNS client appends the suffixes, one at a time, to
 an unqualified domain name before it enters the name into a DNS query, thereby using
 a fully qualified domain name (FQDN) in the DNS query. For example, if a user (of
 the DNS client being configured) tries to submit a DNS query for the name “quality”
 without a suffix, the router appends a period and the first DNS suffix from the DNS
 Search List to the name and transmits a DNS query. If the first DNS suffix on the
 list is “company.com”, the resulting DNS query from the router is for the FQDN
 “quality.company.com”. 

 If the DNS query fails, the client appends the second DNS suffix from the list to the
 unqualified name and transmits a new DNS query. The client uses the DNS suffixes in
 order until a DNS lookup succeeds (ignoring the remaining suffixes) or the router
 has tried all of the suffixes on the list. 

 You configure the firewall with the suffixes that you want to provide to the DNS
 client router in an ND DNSSL option; the DNS client receiving the DNS Search List
 option is provisioned to use the suffixes in its unqualified DNS queries. 

 Perform this task to configure IPv6 router advertisements for DNS configuration of IPv6 hosts.
 You will specify RDNS servers and a DNS search list. 

 Enable the firewall to send IPv6 router advertisements (RAs) from an
 interface. 

 Select Network Interfaces and Ethernet or
 VLAN . 

 Select the interface to configure. 

 On the IPv6 tab, select Enable IPv6
 on the interface . 

 On the Router Advertisement tab, select
 Enable Router Advertisement . 

 Click OK . 

 Specify the Recursive DNS Server addresses and DNS Search List the firewall
 will advertise in ND router advertisements from this interface. 

 The RDNS servers and DNS Search List are part of the DNS configuration for
 the DNS client so that the client can resolve IPv6 DNS requests. 

 Select Network Interfaces and Ethernet or
 VLAN . 

 Select the interface you are configuring. 

 Select IPv6 DNS Support . 

 Include DNS information in Router Advertisement 
 to enable the firewall to send IPv6 DNS information. 

 For DNS Server , Add the
 IPv6 address of a Recursive DNS Server. Add up to
 eight Recursive DNS servers. The firewall sends server addresses in an
 ICMPv6 Router Advertisement in order from top to bottom. 

 Specify the Lifetime in seconds, which is the
 maximum length of time the client can use the specific RDNS Server to
 resolve domain names. 

 The Lifetime range is any value equal
 to or between the Max Interval (that
 you configured on the Router
 Advertisement tab) and two times that
 Max Interval . For example, if
 your Max Interval is 600 seconds, the Lifetime range is 600
 to 1,200 seconds. 

 The default Lifetime is 1,200
 seconds. 

 For DNS Suffix, Add a DNS
 Suffix (domain name of a maximum of 255 bytes).
 Add up to eight DNS suffixes. The firewall
 sends suffixes in an ICMPv6 Router Advertisement in order from top to
 bottom. 

 Specify the Lifetime in seconds, which is the
 maximum length of time the client can use the suffix. The Lifetime has
 the same range and default value as the
 Server . 

 Click OK . 

 Commit your changes. 

 Previous 

 Configure Layer 3 Interfaces 

 Next 

 Enable NDP Monitoring 

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

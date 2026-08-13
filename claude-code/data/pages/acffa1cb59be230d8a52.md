---
url: https://docs.paloaltonetworks.com/ngfw/help/11-1/network/network-virtual-routers/more-runtime-stats-for-a-virtual-router/routing-tab
fetched_at: 2026-08-13T16:46:13Z
source: palo-alto-main
---

# Routing Tab Clear

Routing Tab 

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

 Routing Tab 

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

 Network 

 Network > Virtual Routers 

 More Runtime Stats for a Virtual Router 

 Routing Tab 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 한국어 (Korean) 

 Next-Generation Firewall 

 Routing Tab 

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

 More Runtime Stats for a Virtual Router 

 Next 

 RIP Tab 

 Routing Tab 

 The following table describes the virtual router’s runtime
stats for the Route
Table , Forwarding
Table , and the Static
Route Monitoring table. 

 Runtime Stat 

 Description 

 Route Table 

 Route Table 

 Select Unicast or Multicast to
display either the unicast or multicast route table. 

 Display Address Family 

 Select IPv4 Only , IPv6
Only , or IPv4 and IPv6 (default)
to control which group of addresses to display in the table. 

 Destination 

 IPv4 address and netmask or IPv6 address
and prefix length of networks the virtual router can reach. 

 Next Hop 

 IP address of the device at the next hop
toward the Destination network. A next hop of 0.0.0.0 indicates
the default route. 

 Metric 

 Metric for the route. When a routing protocol
has more than one route to the same destination network, it prefers
the route with the lowest metric value. Each routing protocol uses
a different type of metric; for example, RIP uses hop count. 

 Weight 

 Weight for the route. For example, when
BGP has more than one route to the same destination, it will prefer
the route with the highest weight. 

 Flags 

 A?B —Active
and learned via BGP 

 A C —Active and a result of an internal
interface (connected) - Destination = network 

 A H —Active and a result of an internal
interface (connected) - Destination = Host only 

 A R —Active and learned via RIP 

 A S —Active and static 

 S —Inactive (because this route has
a higher metric) and static 

 O1 —OSPF external type-1 

 O2 —OSPF external type-2 

 Oi —OSPF intra-area 

 Oo —OSPF inter-area 

 Age 

 Age of the route entry in the routing table.
Static routes have no age. 

 Interface 

 Egress interface of the virtual router that
will be used to reach the next hop. 

 Refresh 

 Click to refresh the runtime stats in the
table. 

 Forwarding Table 

 The
firewall chooses the best route—from the route table (RIB) toward
a destination network—to place in the FIB. 

 Display Address Family 

 Select IPv4 Only , IPv6
Only , or IPv4 and IPv6 (default)
to control which route table to display. 

 Destination 

 Best IPv4 address and netmask or IPv6 address
and prefix length to a network the virtual router can reach, selected
from the Route Table. 

 Next Hop 

 IP address of the device at the next hop
toward the Destination network. A next hop of 0.0.0.0 indicates
the default route. 

 Flags 

 u —Route is
up. 

 h —Route is to a host. 

 g —Route is to a gateway. 

 e —Firewall selected this route using
Equal Cost Multipath (ECMP). 

 * —Route is the preferred path to a
destination network. 

 Interface 

 Egress interface the virtual router will
use to reach the next hop. 

 MTU 

 Maximum transmission unit (MTU); maximum
number of bytes that the firewall will transmit in a single TCP
packet to this destination. 

 Refresh 

 Click to refresh the runtime stats in the
table. 

 Static Route Monitoring 

 Destination 

 IPv4 address and netmask or IPv6 address
and prefix length of a network the virtual router can reach. 

 Next Hop 

 IP address of the device at the next hop
toward the Destination network. A next hop of 0.0.0.0 indicates
the default route. 

 Metric 

 Metric for the route. When there is more
than one static route to the same destination network, the firewall
prefers the route with the lowest metric value. 

 Weight 

 Weight for the route. 

 Flags 

 A?B —Active
and learned via BGP 

 A C —Active and a result of an internal
interface (connected) - Destination = network 

 A H —Active and a result of an internal
interface (connected) - Destination = Host only 

 A R —Active and learned via RIP 

 A S —Active and static 

 S —Inactive (because this route has
a higher metric) and static 

 O1 —OSPF external type-1 

 O2 —OSPF external type-2 

 Oi —OSPF intra-area 

 Oo —OSPF inter-area 

 Interface 

 Egress interface of the virtual router that
will be used to reach the next hop. 

 Path Monitoring (Fail On) 

 If path monitoring is enabled for this static
route, Fail On indicates: 

 All —Firewall
considers the static route down and will fail over if all of the
monitored destinations for the static route are down. 

 Any —Firewall considers the static
route down and will fail over if any one of the monitored destinations
for the static route is down. 

 If static route path
monitoring is disabled, Fail On indicates Disabled . 

 Status 

 Status of the static route based on ICMP
pings to the monitored destinations: Up , Down ,
or path monitoring for the static route is Disabled . 

 Refresh 

 Refreshes the runtime stats in the table. 

 Previous 

 More Runtime Stats for a Virtual Router 

 Next 

 RIP Tab 

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

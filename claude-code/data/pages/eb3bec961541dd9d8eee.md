---
url: https://docs.paloaltonetworks.com/ngfw/help/10-1/network/network-routing-logical-routers/bgp-routing-for-a-logical-router
fetched_at: 2026-08-13T16:42:05Z
source: palo-alto-main
---

# BGP Routing for a Logical Router Clear

BGP Routing for a Logical Router 

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

 BGP Routing for a Logical Router 

 Updated on 

 Mon Jan 12 14:16:08 PST 2026 

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

 Mon Jan 12 14:16:08 PST 2026 

 Focus 

 Home 

 Next-Generation Firewall 

 Network 

 Network > Routing > Logical Routers 

 BGP Routing for a Logical Router 

 Download PDF 

 Next-Generation Firewall 

 BGP Routing for a Logical Router 

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

 Static Routes for a Logical Router 

 Next 

 Network > Routing > Routing Profiles > BGP 

 BGP Routing for a Logical Router 

 Configure BGP for the logical router to use to route
BGP traffic. 

 Network > Routing> Logical Routers > BGP 

 The table describes the settings to configure
BGP, peer groups, peers, and redistribution for a logical router
on an Advanced Routing Engine. 

 BGP Settings 

 Description 

 General 

 Enable 

 Enable BGP for the logical router. 

 Router ID 

 Assign a Router ID to BGP for the logical
router, which is typically an IPv4 address to ensure the Router
ID is unique. 

 Local AS 

 Assign the local autonomous system (AS)
to which the logical router belongs based on the Router ID (range
for a 2-byte or 4-byte AS number is to 1 to 4,294,967,295). 

 Global BFD Profile 

 Select a BFD profile to apply to BGP globally.
Default is None (Disable BFD) . 

 Install Route 

 Enforce First AS 

 Select to cause the firewall to drop an
incoming Update message from an EBGP peer that does not list the
EBGP peer’s own AS number as the first AS number in the AS_PATH
attribute. (Enabled by default.) 

 Default Local Preference 

 Specify the default local preference that
can be used to determine preferences among different paths to the
same destination; range is 0 to 4,294,967,295;
default is 100. 

 ECMP Multiple AS Support 

 Enable if you configured ECMP and you want
to run ECMP over multiple BGP autonomous systems. 

 Fast Failover 

 Fast failover of EBGP is enabled by default.
Disable EBGP fast failover if it causes the firewall to unnecessarily
withdraw BGP routes. 

 Graceful Restart—Enable 

 Enables graceful restart for BGP so that
packet forwarding is not disrupted during a BGP restart (enabled
by default). 

 Stale Route Time 

 Specify the length of time, in seconds,
that a route can stay in the stale state (range is 1 to 3,600; default
is 120). 

 Max Peer Restart Time 

 Specify the maximum length of time, in seconds,
that the local device accepts as a grace period restart time for
peer devices (range is 1 to 3,600; default is 120). 

 Local Restart Time 

 Path Selection—Always Compare MED 

 Select to choose paths from neighbors in
different autonomous systems; default is disabled. The Multi-Exit
Discriminator (MED) is an external metric that lets neighbors know
about the preferred path into an AS. A lower value is preferred
over a higher value. 

 Deterministic MED Comparison 

 Select to choose between routes that are
advertised by IBGP peers (BGP peers in the same AS). Default is
enabled. 

 Peer Group 

 Name 

 Add a BGP peer group by Name. 

 Enable 

 Enable the peer group. 

 Type 

 Select the type of peer group as IBGP (Internal
BGP, peering within an AS) or EBGP (External
BGP—peering between two autonomous systems). 

 AFI IPv4 Unicast 

 Select or create an AFI IPv4 profile to
apply the settings in the profile to the peer group; default is None . 

 AFI IPv6 Unicast 

 Select or create an AFI IPv6 profile to
apply the settings in the profile to the peer group; default is None . 

 Filtering IPv4 Unicast 

 Apply all the elements of a Filtering Profile
to the peer group. 

 Filtering IPv6 Unicast 

 Apply all the elements of a Filtering Profile
to the peer group. 

 Auth Profile 

 Select or create an authentication profile
that is used to authenticate BGP peer communications; default is None . 

 Timer Profile 

 Select or create a Timers profile to apply
to the peer group; default is None . 

 Multi Hop 

 Set the time-to-live (TTL) value in the
IP header. Range is 1 to 255; a setting of 0 means use the default
value: 1 for EBGP; 255 for IBGP. 

 Dampening Profile 

 Peer 

 Name 

 Add a BGP peer by name, which must start
with an alphanumeric character and contain a maximum of 31 characters,
including letters, numbers, underscore, hyphen, period, and space. 

 Enable 

 Enable the BGP peer. 

 Passive 

 Peer AS 

 Enter the AS to which the peer belongs;
range is 1 to 4,294,967,295. 

 Peer—Addressing 

 Inherit 

 Yes —Select for
the peer to inherit the AFI and Subsequent AFI (SAFI) configuration
from the peer group. 

 No — 

 AFI IPv4 Unicast 

 ( Available if Inherit No )
Select or create an AFI IPv4 profile to apply the settings in the
profile to the peer; default is None . 

 AFI IPv6 Unicast 

 ( Available if Inherit No )
Select or create an AFI IPv6 profile to apply the settings in the
profile to the peer; default is None . 

 Filtering IPv4 Unicast 

 ( Available if Inherit No ) Default
is None . 

 Filtering IPv6 Unicast 

 ( Available if Inherit No ) Default
is None . 

 Local Address - Interface 

 ( Available if Inherit Yes )
Select the Layer 3 interface for which you are configuring BGP.
Interfaces configured with a static IP address and interfaces configured
as a DHCP client are available to select. If you select an interface
where DHCP assigns the address, the IP address
will indicate None . DHCP will later assign
an IP address to the interface; you can see the address when you
view More Runtime Stats for the logical router. 

 IP Address 

 ( Available if Inherit Yes )
If the interface has more than one IP address, enter the IP address
and netmask you want to use. 

 Peer Address - IP 

 ( Available if Inherit Yes )
Enter the IP address of the peer. 

 Peer—Connection Options These
settings override the same option you have set for the peer group
to which the peer belongs. 

 Auth Profile 

 Select or create an Authentication profile.
Alternatively, select inherit (Inherit from Peer-Group) or None ,
both of which cause the peer to use the Auth profile specified for
the peer group. 

 Timer Profile 

 Select or create a Timers profile. Alternatively,
select inherit (Inherit from Peer-Group) or None ,
both of which cause the peer to use the Timers profile specified
for the peer group. 

 Multi Hop 

 Select inherit (Inherit from
Peer-Group) or None , both of
which cause the peer to use the value specified for the peer group. 

 Dampening Profile 

 Peer—Advanced 

 Enable Sender Side Loop Detection 

 Select to cause the firewall to check the AS_PATH attribute of a route in the BGP RIB before it
 sends the route in an Update, to ensure that the peer AS number
 isn't in the AS_PATH list. The firewall doesn't advertise the route
 if the peer AS number is in the AS_PATH list. Usually the receiver
 performs loop detection, but this optimization feature has the
 sender perform loop detection. Disable this feature to have the
 receiver perform loop detection. 

 BFD Profile 

 Inherit-vr-global-setting (Inherit
Protocol’s Global BFD Profile) Default
is None (Disable BFD) 

 BGP Redistribution 

 Redistribution Rules 

 IPv4 Unicast 

 Select or create a Redistribution profile
to specify which static or connected IPv4 routes to redistribute
to the IPv4 unicast route table. Default is None . 

 IPv6 Unicast 

 Select or create a Redistribution profile
to specify which static or connected IPv6 routes to redistribute
to the IPv6 unicast route table. Default is None . 

 Network 

 IPv4 or IPv6 

 Select IPv4 or IPv6 . 

 Network 

 Add a corresponding IPv4 or IPv6 network
address; subnets with matching network addresses are advertised
to BGP peers of the logical router. 

 Unicast 

 Select to install the matching routes into
the Unicast routing table of all BGP peers. 

 Previous 

 Static Routes for a Logical Router 

 Next 

 Network > Routing > Routing Profiles > BGP 

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

 10.1 

 PAN-OS 

 Next-Generation Firewall 

 Help 

 Web Interface 

 Panorama 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

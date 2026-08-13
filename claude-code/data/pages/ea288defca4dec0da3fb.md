---
url: https://docs.paloaltonetworks.com/prisma-sd-wan/administration/prisma-sd-wan-branch-and-data-center-routing/configure-dynamic-routing/configure-bgp-global-parameters
fetched_at: 2026-08-13T17:27:44Z
source: palo-alto-main
---

# Configure BGP Global Parameters Clear

Configure BGP Global Parameters 

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

 Configure BGP Global Parameters 

 Updated on 

 Aug 10, 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma SD-WAN Docs 

 Activation & Onboarding 

 Administration 

 CloudBlades 

 Select a Document 

 CloudBlade Integrations 

 CloudBlades Integration with Prisma Access 

 Deployment 

 Incidents & Alerts 

 Reference 

 Release Notes 

 Select a Document 

 ION 6.8 

 ION 6.6 

 ION 6.5 

 ION 6.4 

 ION 6.3 

 ION 6.1 

 ION 5.6 

 Prisma SD-WAN Controller 

 Prisma SD-WAN On-Premises Controller 

 Prisma SD-WAN CloudBlades 

 Prisma Access CloudBlade Cloud Managed 

 Prisma Access CloudBlade Panorama Managed 

 New Features 

 Updated on 

 Aug 10, 2026 

 Focus 

 Home 

 Prisma SD-WAN 

 Prisma SD-WAN Administrator’s Guide 

 Prisma SD-WAN Branch and Data Center Routing 

 Configure Dynamic Routing 

 Configure BGP Global Parameters 

 Download PDF 

 Prisma SD-WAN 

 Configure BGP Global Parameters 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma SD-WAN Docs 

 Activation & Onboarding 

 Administration 

 CloudBlades 

 Select a Document 

 CloudBlade Integrations 

 CloudBlades Integration with Prisma Access 

 Deployment 

 Incidents & Alerts 

 Reference 

 Release Notes 

 Select a Document 

 ION 6.8 

 ION 6.6 

 ION 6.5 

 ION 6.4 

 ION 6.3 

 ION 6.1 

 ION 5.6 

 Prisma SD-WAN Controller 

 Prisma SD-WAN On-Premises Controller 

 Prisma SD-WAN CloudBlades 

 Prisma Access CloudBlade Cloud Managed 

 Prisma Access CloudBlade Panorama Managed 

 New Features 

 Previous 

 Enable BGP for Private WAN and LAN 

 Next 

 Global or Local Scope for BGP Peers 

 Configure BGP Global Parameters 

 Lets learn about configuring BGP Global Parameters in Prisma SD-WAN. You can configure
 the local AS #, optional MD5 secret and router ID, prefix advertisements, and BGP
 timers. 

 Where Can I Use
 This? What Do I
 Need? 

 Prisma SD-WAN (Managed by Strata Cloud Manager ) 

 Prisma SD-WAN 

 Configure BGP global attributes before creating
BGP peers. You can configure the local AS #, optional MD5 secret
and router ID, prefix advertisements, and BGP timers. 

 Configure local AS number. 

 Select Configuration Prisma SD-WAN ION Devices Claimed Configure the device Routing BGP/Peers BGP Global Config for ION device Edit . 

 Enter a Local AS Number between 1 and 4294967295
 or as A.B, where A and B are both numbers between 1 and 4294967295. 

 The web interface displays converted values of the AS number entered.
 If the number entered is an A.B format, the web interface displays
 the corresponding 32-bit conversion below the entered value. If the
 number entered is a 32-bit format, the web interface displays the
 corresponding A.B value below the entered value. The
 Local AS Number is mandatory. 

 (Optional) Enter an MD5 Secret between
1 and 32 characters. 

 The default value is 0. 

 (Optional) Configure prefixes to advertise to
WAN and LAN. 

 Branch ION devices can learn or advertise prefixes based on the scope 
 configured. The device advertises only LAN networks, static routes,
 and interface addresses. To advertise any of these prefixes, set the
 Scope to Global 
 when configuring a BGP peer. 

 Configure Prefix Advertisement to LAN in any of
 the following ways: 

 Default—The device advertises only the default prefix
 (0.0.0.0/0) and (::/0) . This
 is the default setting for LAN prefix advertisement. 

 Unaggregated—The device advertises prefixes as is. 

 Auto-Aggregated—The device summarizes the unaggregated
 prefixes into the largest possible blocks and advertises the
 prefixes. 

 The device advertises only Default ,
 Unaggregated or
 Auto-Aggregated to the LAN. 

 Configure Prefix Advertisement to WAN in any of
 the following ways: 

 None (--)—The device does not advertise prefixes. This is the
 default setting for WAN prefix advertisement. 

 Unaggregated—The device advertises prefixes
 as is. 

 Auto-Aggregated—The device summarizes the unaggregated
 prefixes into the largest possible blocks and advertises the
 prefixes. 

 Manually Aggregated—You can configure a set of prefixes which
 the device aggregates and advertises. 

 Manual Summary Aggregate Only—You can configure a set of
 prefixes which the device summarizes into the largest
 possible blocks and advertises these prefixes. 

 Check the IP Prefix to Advertise to WAN IP
 Addresses displayed. 

 (Optional) Configure advanced options. 

 Keepalive Time —Enter a keep-alive
time between 3 - 200 seconds. If you have configured a BGP peer,
the device uses the value specified in the BGP peer configuration.
If you do not configure a BGP peer or do not specify a value in
the BGP global configuration, the keep-alive time defaults to 30
seconds. 

 Hold Time —Enter a hold time between
3 - 600 seconds. The hold time needs to be three times greater than
the keep-alive time. If you have configured a BGP peer, the device
uses the value specified in the BGP peer configuration. If you have not
configured a BGP peer, the device uses the value from the BGP global
configuration. If you do not configure a BGP peer or do not specify
a value in the BGP global configuration, the Hold Time defaults
to 90 seconds. 

 Multihop Limit —Enter a multi-hop limit
between 1 - 255 hops. The default is 1 hop. 

 Max Paths —Enter a max path between
1 - 255. The default is 1. 

 Advertise Interval — Enter an advertisement
interval between 0 - 300 seconds. The default is 1 second. 

 Peer Retry Time —Enter a peer retry
time between 0 - 65535 seconds. The default is 120 seconds. 

 Graceful Restart —By default graceful
restart is Off . Select On to
change the default setting. 

 StalePath Time —Enter a stalepath time
between 1 - 3600 seconds. The default is 120 seconds. 

 Admin Distance —Enter a value between
1 - 255. The device sets the default Admin Distance of
all learned prefixes to 20. The Admin Distance configured
for a static route overrides the Admin Distance configured
for a BGP route. 

 On the Router ID tab, enter the IP address of the ION
 device to Globally Associated Router ID . 

 (Optional) Add Router ID or enter the
 IP address of the ION device. 

 Enter a valid IPv4 address in the Route ID field (for example,
 192.0.2.11). 

 (Optional) In the Custom Router ID for each
 VRF section, click Add VRF . 

 Use this step if your device requires distinct Router IDs for traffic
 isolation across different VRFs. 

 Choose the specific VRF (such as Global) from the dropdown list. 

 Enter the Router ID for the selected VRF (for example,
 192.0.2.2). 

 To apply your changes and close the window, click
 Submit . 

 This feature requires ION devices running
 software version 6.6.1 or later. 

 View the Summary to review BGP global configuration and
 then Save & Exit. 

 Related CLIs 

 configure interface 

 dump routing summary 

 dump routing peer advertised
 routes 

 Previous 

 Enable BGP for Private WAN and LAN 

 Next 

 Global or Local Scope for BGP Peers 

 On This Page 

 Activation & Onboarding 

 Strata Cloud Manager 

 Activate a License or Product 

 Cloud Identity Engine 

 Hub 

 Identity and Access Management 

 Tenant Management 

 SASE 

 Prisma Access 

 Strata Multitenant Cloud Manager 

 AI-Powered ADEM 

 Prisma Access Monitoring and Visibility 

 Visibility & Monitoring 

 Dashboards 

 Incidents and Alerts 

 Reports 

 Autonomous DEM 

 FedRAMP 

 Prisma SASE for FedRAMP 

 Hardware Reference 

 ION 1000 

 ION 1200 

 ION 1200-S 

 ION 2000 

 ION 3000 

 ION 3200 and ION 3200H 

 ION 5200 

 ION 7000 

 ION 9000 

 ION 9200 

 Hardware Quick Start Guides 

 ION 1200 

 ION 1200 4G 

 ION 1200 5G 

 ION 1200-S 

 ION 1200-S 4G 

 ION 1200-S 5G 

 ION 3200 

 ION 3200H 

 ION 3200H 5G 

 ION 5200 

 ION 9200 

 Virtual ION Deployment 

 Virtual ION on AWS 

 Virtual ION on Azure 

 Virtual ION on GCP 

 Virtual ION on Alibaba Cloud 

 Virtual ION on KVM for NFV 

 Virtual ION on OCI 

 Virtual ION on VMware 

 Virtual ION on Megaport Virtual Edge 

 Virtual ION on Dell PowerEdge 

 Prisma SD-WAN Integration 

 AWS Cloud-WAN Integration (GRE Connect) 

 AWS Cloud-WAN Integration (Tunnel-less Connect) 

 Checkpoint Integration 

 LiveAction Integration 

 Netskope Integration 

 Symantec Web Security Services Integration 

 Prisma SD-WAN Experts Corner 

 Network Policy 

 QoS Whitepaper 

 Security Architecture Whitepaper 

 External Antennas for ION-C Series 

 Dynamic Path Selection 

 Best Practices 

 Best Practices Library 

 Resources 

 All Products A - Z 

 Compatibility Matrix 

 SASE 

 Administration 

 Prisma SD-WAN 

 Strata Cloud Manager 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

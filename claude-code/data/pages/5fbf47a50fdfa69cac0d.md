---
url: https://docs.paloaltonetworks.com/ngfw/networking/static-routes/configure-path-monitoring-for-a-static-route
fetched_at: 2026-08-13T16:54:17Z
source: palo-alto-main
---

# Configure Path Monitoring for a Static Route Clear

Configure Path Monitoring for a Static Route 

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

 Configure Path Monitoring for a Static Route 

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

 Static Routes 

 Configure Path Monitoring for a Static Route 

 Download PDF 

 Next-Generation Firewall 

 Configure Path Monitoring for a Static Route 

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

 Configure a Static Route 

 Next 

 Configure RIP 

 Configure Path Monitoring for a Static Route 

 Procedure to remove a static route based on path monitoring. 

 Where Can I Use This? What Do I Need? 

 NGFW (Managed by PAN-OS or Panorama) 

 Use the following procedure to configure Static
Route Removal Based on Path Monitoring . 

 Enable path monitoring for a static route. 

 Select Network Virtual Routers and select
a virtual router. 

 Select Static Routes , select IPv4 or IPv6 ,
and select the static route you want to monitor. You can monitor
up to 128 static routes. 

 Select Path Monitoring to enable
path monitoring for the route. 

 Configure the monitored destination(s) for the static
route. 

 Add a monitored destination
by Name . You can add up to eight monitored
destinations per static route. 

 Select Enable to monitor the
destination. 

 For Source IP , select the IP
address that the firewall uses in the ICMP ping to the monitored
destination: 

 If the interface has multiple IP addresses, select
one. 

 If you select an interface, the firewall uses the first IP
address assigned to the interface by default. 

 If you select DHCP (Use DHCP Client address) ,
the firewall uses the address that DHCP assigned to the interface.
To see the DHCP address, select Network Interfaces Ethernet and
in the row for the Ethernet interface, click on Dynamic
DHCP Client . The IP Address displays in the Dynamic
IP Interface Status window. 

 For Destination IP , enter an
IP address or address object to which the firewall will monitor
the path. The monitored destination and static route destination
must use the same address family (IPv4 or IPv6). 

 The destination IP address should belong
to a reliable endpoint; you wouldn’t want to base path monitoring
on a device that itself is unstable or unreliable. 

 ( Optional ) Specify the ICMP Ping
Interval (sec) in seconds to determine how frequently
the firewall monitors the path (range is 1-60; default is 3). 

 ( Optional ) Specify the ICMP Ping
Count of packets that don’t return from the destination
before the firewall considers the static route down and removes
it from the RIB and FIB (range is 3-10; default is 5). 

 Click OK . 

 Determine whether path monitoring for the static route
is based on one or all monitored destinations, and set the preemptive
hold time. 

 Select a Failure Condition ,
whether Any or All of
the monitored destinations for the static route must be unreachable
by ICMP for the firewall to remove the static route from the RIB
and FIB and add the static route that has the next lowest metric
going to the same destination to the FIB. 

 Select All to
avoid the possibility of any single monitored destination signaling
a route failure when the destination is simply offline for maintenance,
for example. 

 ( Optional ) Specify the Preemptive
Hold Time (min) , which is the number of minutes a downed
path monitor must remain in Up state before the firewall reinstalls
the static route into the RIB. The path monitor evaluates all of
its monitored destinations for the static route and comes up based
on the Any or All failure
condition. If a link goes down or flaps during the hold time, when
the link comes back up, the path monitor can come back up; the timer
restarts when the path monitor returns to Up state. 

 A Preemptive Hold Time of zero causes
the firewall to reinstall the route into the RIB immediately upon
the path monitor coming up. Range is 0-1,440; default is 2. 

 Click OK . 

 Commit. 

 Click Commit . 

 Verify path monitoring on static routes. 

 Select Network Virtual Routers and in the
row of the virtual router you are interested in, select More
Runtime Stats . 

 From the Routing tab, select Static
Route Monitoring . 

 For a static route (Destination), view whether Path
Monitoring is Enabled or Disabled. The Status column indicates whether
the route is Up, Down, or Disabled. Flags for the static route are:
A—active, S—static, E—ECMP. 

 Select Refresh periodically
to see the latest state of the path monitoring (health check). 

 Hover over the Status of a route to view the monitored
IP addresses and results of the pings sent to the monitored destinations
for that route. For example, 3/5 means that a ping interval of 3
seconds and a ping count of 5 consecutive missed pings (the firewall
receives no ping in the last 15 seconds) indicates path monitoring
detects a link failure. Based on the Any or All failure
condition, if path monitoring is in failed state and the firewall
receives a ping after 15 seconds, the path can be deemed up and
the Preemptive Hold Time starts. 

 The State indicates the last monitored ping results: success
or failed. Failed indicates that the series of ping packets (ping
interval multiplied by ping count) was not successful. A single
ping packet failure does not reflect a failed ping state. 

 View the RIB and FIB to verify that the static route
is removed. 

 Select Network Virtual Routers and in the
row of the virtual router you are interested in, select More
Runtime Stats . 

 From the Routing tab, select Route
Table (RIB) and then the Forwarding Table (FIB)
to view each, respectively. 

 Select Unicast or Multicast to
view the appropriate route table. 

 For Display Address Family ,
select IPv4 and IPv6 , IPv4 Only ,
or IPv6 Only . 

 ( Optional ) In the filter field, enter the
route you are searching for and select the arrow, or use the scroll
bar to move through pages of routes. 

 See if the route is removed or present. 

 Select Refresh periodically
to see the latest state of the path monitoring (health check). 

 To view the events logged for path monitoring, select Monitor Logs System .
View the entry for path-monitor-failure ,
which indicates path monitoring for a static route destination failed,
so the route was removed. View the entry for path-monitor-recovery ,
which indicates path monitoring for the static route destination
recovered, so the route was restored. 

 Previous 

 Configure a Static Route 

 Next 

 Configure RIP 

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

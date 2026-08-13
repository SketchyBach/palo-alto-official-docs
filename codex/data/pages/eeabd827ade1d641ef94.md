---
url: https://docs.paloaltonetworks.com/ngfw/networking/static-routes/static-route-removal-based-on-path-monitoring
fetched_at: 2026-08-13T16:54:17Z
source: palo-alto-main
---

# Static Route Removal Based on Path Monitoring Clear

Static Route Removal Based on Path Monitoring 

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

 Static Route Removal Based on Path Monitoring 

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

 Static Routes 

 Static Route Removal Based on Path Monitoring 

 Download PDF 

 Next-Generation Firewall 

 Static Route Removal Based on Path Monitoring 

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

 Static Routes 

 Next 

 Configure a Static Route 

 Static Route Removal Based on Path Monitoring 

 Learn about why you would want to remove a static route based on path
 monitoring. 

 Where Can I Use This? What Do I Need? 

 NGFW (Managed by PAN-OS or Panorama) 

 When you Configure Path Monitoring
 for a Static Route , the firewall uses path monitoring to detect when the path
 to one or more monitored
 destinations
 has gone down. The firewall can then reroute traffic using alternative routes. The
 firewall uses path monitoring for static routes much like path monitoring for HA or
 policy-based forwarding (PBF), as follows: 

 The firewall sends ICMP ping
messages (heartbeat messages) to one or more monitored destinations
that you determine are robust and reflect the availability of the
static route. 

 If pings to any or all of the monitored destinations fail,
the firewall considers the static route down too and removes it
from the Routing Information Base (RIB) and Forwarding Information
Base (FIB). The RIB is the table of static routes the firewall is
configured with and dynamic routes it has learned from routing protocols.
The FIB is the forwarding table of routes the firewall uses for
forwarding packets. The firewall selects an alternative static route
to the same destination (based on the route with the lowest metric)
from the RIB and places it in the FIB. 

 The firewall continues to monitor the failed route. When
the route comes back up, and (based on the Any or All failure
condition) the path monitor returns to Up state, the preemptive
hold timer begins. The path monitor must remain up for the duration
of the hold timer; then the firewall considers the static route
stable and reinstates it into the RIB. The firewall then compares
metrics of routes to the same destination to decide which route goes
in the FIB. 

 Path monitoring is a desirable mechanism to avoid silently discarding
traffic for: 

 A static or default route. 

 A static or default route redistributed into a routing protocol. 

 A static or default route when one peer does not support
BFD. (The best practice is not to enable both BFD and path monitoring
on a single interface.) 

 A static or default route instead of using PBF path monitoring, which doesn’t
 remove a failed static route from the RIB, FIB, or redistribution policy. 

 In the following figure, the firewall is connected to two ISPs
for route redundancy to the internet. The primary default route
0.0.0.0 (metric 10) uses Next Hop 192.0.2.10; the secondary default
route 0.0.0.0 (metric 50) uses Next Hop 198.51.100.1. The customer
premises equipment (CPE) for ISP A keeps the primary physical link
active, even after internet connectivity goes down. With the link
artificially active, the firewall can’t detect that the link is
down and that it should replace the failed route with the secondary
route in its RIB. 

 To avoid silently discarding traffic to a failed link, configure
path monitoring of 192.0.2.20, 192.0.2.30, and 192.0.2.40 and if
all (or any) of the paths to these destinations fail, the firewall
presumes the path to Next Hop 192.0.2.10 is also down, removes the
static route 0.0.0.0 (that uses Next Hop 192.0.2.10) from its RIB,
and replaces it with the secondary route to the same destination
0.0.0.0 (that uses Next Hop 198.51.100.1), which also accesses the
internet. 

 When you Configure
a Static Route , one of the required fields is the Next Hop
toward that destination. The type of next hop you configure determines the
action the firewall takes during path monitoring, as follows: 

 If Next Hop Type
in Static Route is: 

 Firewall Action for
ICMP Ping 

 IP Address 

 The firewall uses the source IP address
and egress interface of the static route as the source address and
egress interface in the ICMP ping. It uses the configured Destination
IP address of the monitored destination as the ping’s destination
address. It uses the static route’s next hop address as the ping’s
next hop address. 

 Next VR 

 The firewall uses the static route's source IP address as the source
 address for ICMP ping packets. The egress interface is determined by
 performing a route lookup in the next hop's virtual router. The
 ping's destination address is the configured Destination IP of the
 monitored target. 

 For the configuration to commit successfully, you must specify an
 interface that belongs to the virtual router in the static route
 configuration, even though the interface setting is redundant in
 this scenario. Without an interface configured, the commit will fail
 because an interface is a mandatory parameter for path
 monitoring. 

 None 

 The firewall uses the destination IP address
of the path monitor as the next hop and sends the ICMP ping to the
interface specified in the static route. 

 When path monitoring for a static or default route fails, the
firewall logs a critical event (path-monitor-failure). When the
static or default route recovers, the firewall logs another critical
event (path-monitor-recovery). 

 Firewalls synchronize path monitoring configurations for an active/passive
HA deployment, but the firewall blocks egress ICMP ping packets
on a passive HA peer because it is not actively processing traffic.
The firewall doesn’t synchronize path monitoring configurations
for active/active HA deployments. 

 Previous 

 Static Routes 

 Next 

 Configure a Static Route 

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

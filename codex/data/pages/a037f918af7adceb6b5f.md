---
url: https://docs.paloaltonetworks.com/prisma-sd-wan/administration/prisma-sd-wan-branch-and-data-center-routing/prisma-sd-wan-multicast-routing/view-multicast-interface-statistics
fetched_at: 2026-09-16T07:47:38Z
source: strata-and-sase
---

# View LAN Statistics for Multicast Clear

Updated on 

 Mon Aug 24 08:54:44 PDT 2026 

 Focus 

 Home 

 Prisma SD-WAN 

 Prisma SD-WAN Administrator’s Guide 

 Prisma SD-WAN Branch and Data Center Routing 

 Prisma SD-WAN Multicast Routing 

 View LAN Statistics for Multicast 

 Download PDF 

 Prisma SD-WAN 

 View LAN Statistics for Multicast 

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

 Learn Rendezvous Points (RPs) Dynamically 

 Next 

 View WAN Statistics for Multicast 

 View LAN Statistics for Multicast 

 View LAN multicast statistics for an interface in Prisma SD-WAN . The PIM
 neighbors discovered by the ION device for an interface across all multicast enabled
 interfaces in the network. 

 Where Can I Use
 This? What Do I
 Need? 

 Prisma SD-WAN (Managed by Strata Cloud Manager ) 

 Prisma SD-WAN 

 View LAN multicast statistics for interfaces
with multicast enabled. 

 Select Configuration Prisma SD-WAN ION Devices Claimed Configure the device Routing Multicast LAN Statistics . 

 Select an interface to view the neighbor information
for the interface. 

 The neighbor information table displays information about
the PIM neighbors discovered by the ION device for an interface across
all multicast enabled interfaces in the network. 

 Field Description 

 Port Number Displays the neighbor information for the selected interface. 

 State Displays the state of the selected interface—up
or down. 

 Address Displays the address of the selected interface. 

 PIM Neighbor Displays a PIM neighbor’s IP address. 

 DR Indicates if the neighbor is a designated router. 

 DR Priority Indicates the priority associated with the
interface on the device for DR election. 

 Uptime Indicates the time for which the neighbor has
been up. 

 Expires Indicates the time remaining before a neighbor
is timed out and the next PIM Hello message is received. 

 Click Statistics to view detailed
multicast traffic, IGMP, and PIM statistics for the interface. 

 The descriptions for the fields are based on descriptions
outlined in RFC 2362 (https://www.rfc-editor.org/rfc/rfc2362.html) and
RFC 2236 (https://datatracker.ietf.org/doc/html/rfc2236) 

 Multicast
Traffic Statistics 

 Field Description 

 RX PKTS Indicates the number of multicast traffic packets
received at the interface. 

 RX BYTES Indicates the volume of multicast traffic received
in bytes at the interface. 

 TX PKTS Indicates the number of multicast traffic packets transmitted
from the interface. 

 TX BYTES Indicates the volume of multicast traffic sent
in bytes at the interface. 

 PIM Statistics 

 Message Type (MSG TYPE) Description Received Packets (RX PKTS) Transmitted Packets (TX PKTS) 

 Hello Periodic messages sent between PIM neighbors
aid in discovery of neighbors and maintaining the relationship with
neighbors. Displays the packets received for a PIM Hello
message. Displays the packets sent for a PIM Hello message. 

 Register A DR sends a message to an RP indicating interest
in receiving multicast traffic meant for a group. Displays the packets received for a PIM Register
message. Displays the packets sent for a PIM Register message. 

 Register Stop 
 The ION device acting as an RP indicates
to the DR when either of the following conditions are met: 

 There are
no active listeners, so receivers have stopped requesting multicast information
from the RP. 

 The RP stops serving a multicast group. 

 Multicast traffic has switched from a Rendezvous Point Tree (RPT)
to the Shortest Path Tree (SPT). 

 Displays the packets received for a PIM Register
Stop message. Displays the packets sent for a PIM Register Stop
message. 

 Join/Prune 
 Routers send Join/Prune messages to join a
branch or prune off a branch from the multicast distribution tree.
A single message contains a join listas well as a prune list. 

 Join
messages are sent by: 

 DRs (near receivers) to RPs indicating
an interest in receiving multicast traffic via RPT. 

 DRs to source when triggering SPT switchovers. 

 RPs to source when triggering SPT switchovers. 

 Prune
messages are sent by PIM devices to upstream devices to stop forwarding
multicast traffic to the network segment in which the PIM device resides. 
 Displays the join and prune packets received
for a PIM Join/Prune message. Displays the join and prune packets sent for a
PIM Join/Prune message. 

 Assert 
 PIM elects a single forwarding router to
forward messages to avoid duplication of messages. 
 Displays the number of packets received for Assert
messages. Displays the number of packets transmitted for
Assert messages. 

 BSM 
 PIM routers in the network will communicate with
each other using Bootstrap messages (BSM). 
 Displays the number of packets received for Bootstrap
messages. Displays the number of packets transmitted for
Bootstrap messages. 

 IGMP Statistics 

 IGMP statistics indicate
the number of messages exchanged between individual hosts in a LAN
and multicast routers to dynamically register with or unregister
from a multicast group. Routers periodically send out IGMP queries
to check which multicast groups are active or inactive in their
subnet. Hosts send out IGMP membership reports for a particular
multicast group to indicate their interest in joining that group. 

 Message Type (MSG TYPE) Description Received Packets (RX PKTS) Transmitted Packets (TX PKTS) 

 IGMP v1 Membership query Used by IGMP v1 multicast routers to learn
which multicast groups are being used by the hosts on the local
network. Displays the packets received for an IGMP v1
membership query. Displays the packets sent in response to an IGMP
v1 membership query. 

 IGMP v1 Membership report Identifies this message as an IGMPv1 membership report. Displays the packets received for an IGMP v1
membership report. Displays the packets sent in response to an IGMP
v1 membership report. 

 IGMP v2 Membership query Used by IGMP v2 multicast routers to learn
which multicast groups are being used by the hosts on the local
network. Displays the packets received for an IGMP v2
membership query. Displays the packets sent in response to an IGMP
v2 membership query. 

 IGMP v2 Membership report Identifies this message as an IGMP v2 membership report. Displays the packets received for an IGMP v2
membership report. Displays the packets sent in response to an IGMP
v2 membership report. 

 IGMP v3 Membership query Used by IGMP v3 multicast routers to learn
which multicast groups are being used by the hosts on the local
network. Displays the packets received for an IGMP v3
membership query. Displays the packets sent in response to an IGMP
v3 membership query. 

 IGMP v3 Membership report Identifies this message as an IGMP v3 membership report. Displays the packets received for an IGMP v3
membership report. Displays the packets sent in response to an IGMP
v3 membership report. 

 IGMP v2 Leave report Used by IGMP v2 hosts to indicate that they
are leaving the multicast group. Displays the packets received for an IGMP v2
leave report. Displays the packets sent in response to an IGMP
v2 leave report. 

 Related CLIs 

 debug routing multicast log 

 debug routing multicast pimd 

 dump routing multicast configuration 

 dump routing multicast igmp 

 dump routing multicast interface 

 dump routing multicast internal vif
 entries 

 dump routing multicast mroute 

 dump routing multicast pim 

 dump routing multicast sources 

 dump routing multicast statistics 

 dump routing multicast status 

 inspect routing multicast fc site
 iface 

 inspect routing multicast interface 

 inspect routing multicast mroute 

 clear routing multicast statistics

 Previous 

 Learn Rendezvous Points (RPs) Dynamically 

 Next 

 View WAN Statistics for Multicast

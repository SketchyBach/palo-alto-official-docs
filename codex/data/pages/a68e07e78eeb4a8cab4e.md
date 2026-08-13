---
url: https://docs.paloaltonetworks.com/pan-os/10-1/pan-os-networking-admin/tunnel-content-inspection/tunnel-content-inspection-overview
fetched_at: 2026-08-13T17:03:06Z
source: palo-alto-main
---

# Tunnel Content Inspection Overview Clear

Tunnel Content Inspection Overview 

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

 Tunnel Content Inspection Overview 

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

 Tunnel Content Inspection 

 Tunnel Content Inspection Overview 

 Download PDF 

 Next-Generation Firewall 

 Tunnel Content Inspection Overview 

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

 Tunnel Content Inspection 

 Next 

 Configure Tunnel Content Inspection 

 Tunnel Content Inspection Overview 

 Understand the process of inner tunnel inspection and outer tunnel inspection that
 the firewall performs. 

 Where Can I Use This? What Do I Need? 

 NGFW (Managed by PAN-OS or Panorama) 

 Your firewall can inspect tunnel content anywhere on
the network where you do not have the opportunity to terminate the
tunnel first. As long as the firewall is in the path of a GRE, non-encrypted
IPSec, GTP-U, or VXLAN tunnel, the firewall
can inspect the tunnel content. 

 Enterprise customers who want tunnel content inspection
can have some or all of the traffic on the firewall tunneled using
GRE, VXLAN, or non-encrypted IPSec. For security, QoS, and reporting
reasons, you want to inspect the traffic inside the tunnel. 

 Service Provider customers use GTP-U to tunnel data traffic
from mobile devices. You want to inspect the inner content without
terminating the tunnel protocol, and you want to record user data
from your users. 

 The firewall supports tunnel content inspection on Ethernet interfaces,
subinterfaces, AE interfaces, VLAN interfaces, and VPN and LSVPN
tunnel interfaces. (The cleartext tunnel that the firewall inspects
can be inside a VPN or LSVPN tunnel that terminates at the firewall,
hence a VPN or LSVPN tunnel interface. In other words, when the
firewall is a VPN or LSVPN endpoint, the firewall can inspect the
traffic of any non-encrypted tunnel protocols that tunnel content
inspection supports.) 

 Tunnel content inspection is supported in Layer 3, Layer 2, virtual
wire, and tap deployments. Tunnel content inspection works on shared
gateways and on virtual system-to-virtual system communications. 

 The preceding figure illustrates the two levels of tunnel inspection
the firewall can perform. When a firewall configured with Tunnel
Inspection policy rules receives a packet: 

 The firewall first performs a Security policy check to
determine whether the tunnel protocol (Application) in the packet
is permitted or denied. (IPv4 and IPv6 packets are supported protocols
inside the tunnel.) 

 If the Security policy allows the packet, the firewall matches
the packet to a Tunnel Inspection policy rule based on source zone,
source address, source user, destination zone, and destination address.
The Tunnel Inspection policy rule determines the tunnel protocols
that the firewall inspects, the maximum level of encapsulation allowed
(a single tunnel or a tunnel within a tunnel), whether to allow
packets containing a tunnel protocol that doesn’t pass strict header
inspection per RFC 2780 , and whether
to allow packets containing unknown protocols. 

 If the packet passes the Tunnel Inspection policy rule’s
match criteria, the firewall inspects the inner content, which is
subject to your Security policy ( required ) and optional
policies you can specify. (The supported policy types for the original
session are listed in the following table). 

 If the firewall instead finds another tunnel, the firewall
recursively parses the packet for the second header and is now at
level two of encapsulation, so the second tunnel inspection policy
rule, which matches a tunnel zone, must allow a maximum tunnel inspection
level of two levels for the firewall to continue processing the
packet. 

 If your rule allows two levels of inspection,
the firewall performs a Security policy check on this inner tunnel
and then the Tunnel Inspection policy check. The tunnel protocol
you use in an inner tunnel can differ from the tunnel protocol you
use in the outer tunnel. 

 If your rule doesn’t allow two levels of inspection, the
firewall bases its action on whether you configured it to drop packets
that have more levels of encapsulation than the maximum tunnel inspection
level you configured. 

 By default, the content encapsulated in a tunnel belongs to the
same security zone as the tunnel, and is subject to the Security
policy rules that protect that zone. However, you can configure
a tunnel zone , which gives you the flexibility to configure
Security policy rules for inside content that differ from the Security
policy rules for the tunnel. If you use a different tunnel inspection
policy for the tunnel zone, it must always have a maximum tunnel inspection
level of two levels because by definition the firewall is looking
at the second level of encapsulation. 

 The firewall doesn’t support a Tunnel Inspection policy rule
that matches traffic for a tunnel that terminates on the firewall;
the firewall discards packets that match the inner tunnel session.
For example, when an IPSec tunnel terminates on the firewall, don’t
create a Tunnel Inspection policy rule that matches the tunnel you
terminate. The firewall already inspects the inner tunnel traffic
so no Tunnel Inspection policy rule is needed. 

 Although tunnel content inspection works on shared gateways
and on virtual system-to-virtual system communications, you can’t
assign tunnel zones to shared gateways or virtual system-to-virtual
system communications; they are subject to the same Security policy
rules as the zones to which they belong. 

 Both the inner tunnel sessions and the outer tunnel sessions
count toward the maximum session capacity for the firewall model. 

 The following table indicates which types of policy you can apply to an outer tunnel session, an
 inner tunnel session, and the inside, original session: 

 Policy Type 

 Outer Tunnel Session 

 Inner Tunnel Session 

 Inside, Original Session 

 App-Override 

 Yes 

 VXLAN
Only 

 No 

 Yes 

 DoS Protection 

 Yes 

 Yes 

 Yes 

 NAT 

 Yes 

 No 

 No 

 Policy-Based Forwarding (PBF) and Symmetric
Return 

 Yes 

 No 

 No 

 QoS 

 No 

 No 

 Yes 

 Security ( required ) 

 Yes 

 Yes 

 Yes 

 User-ID 

 Yes 

 Yes 

 Yes 

 Zone Protection 

 Yes 

 Yes 

 Yes 

 VXLAN is different than other protocols. The firewall can use
either of two different sets of session keys to create outer tunnel
sessions for VXLAN. 

 VXLAN UDP Session—A six-tuple key (zone, source IP, destination
IP, protocol, source port, and destination port) creates a VXLAN
UDP Session. 

 VNI Session—A five-tuple key that incorporates the tunnel ID
(the VXLAN Network Identifier, or VNI) and uses zone, source IP,
destination IP, protocol, and tunnel ID (VNI) to create a VNI Session. 

 You can View
Inspected Tunnel Activity on the ACC or View
Tunnel Information in Logs . To facilitate quick viewing,
configure a Monitor tag so you can monitor tunnel activity and filter
log results by that tag. 

 The ACC tunnel activity provides data in various views. For the
Tunnel ID Usage, Tunnel Monitor Tag, and Tunnel Application Usage,
the data for bytes , sessions , threats , content ,
and URLs come from the Traffic Summary database.
For the Tunnel User, Tunneled Source IP and Tunneled Destination
IP Activity, data for bytes and sessions come
from Traffic Summary database, data for threats come
from the Threat Summary, data for URLs come
from the URL Summary, and data for contents come
from the Data database, which is a subset of the Threat logs. 

 If you enable NetFlow on the interface, NetFlow will capture
statistics for the outer tunnel only, to avoid double-counting (counting
bytes of both outer and inner flows). 

 For the Tunnel Inspection policy rule and tunnel zone capacities for your firewall model, see the
 Product Selection tool . 

 The following figure illustrates a corporation that runs multiple
divisions and uses different Security policies and a Tunnel Inspection
policy. A Central IT team provides connectivity between regions.
A tunnel connects Site A to Site C; another tunnel connects Site
A to Site D. Central IT places a firewall in the path of each tunnel;
the firewall in the tunnel between Sites A and C performs tunnel
inspection; the firewall in the tunnel between Sites A and D has
no tunnel inspection policy because the traffic is very sensitive. 

 Previous 

 Tunnel Content Inspection 

 Next 

 Configure Tunnel Content Inspection 

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

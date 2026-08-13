---
url: https://docs.paloaltonetworks.com/pan-os/10-1/pan-os-new-features/networking-features/network-packet-broker
fetched_at: 2026-08-13T17:03:10Z
source: palo-alto-main
---

# Network Packet Broker Clear

Network Packet Broker 

 Home 

 EN

 Location 

 Documentation Home 

 Palo Alto Networks 

 Support 

 Live Community 

 Knowledge Base 

 Strata Copilot

 PAN-OS ® New Features Guide 

 : 
 Network Packet Broker 

 Updated on 

 Mon Aug 28 18:43:40 PDT 2023 

 Focus 

 Download PDF 

 Filter

 Version 

 10.1 

 10.1 

 Expand all | Collapse all 

 App-ID Features 

 App-ID Cloud Engine 

 SaaS Policy Rule Recommendation 

 Management Features 

 Audit Tracking for Administrator Activity 

 Device Certificate for Cortex Data Lake 

 PAN-OS OpenConfig Support 

 Persistent Uncommitted Changes on PAN-OS 

 Panorama Features 

 Authentication Key for Secure Onboarding 

 Optimization for Deploying Changes for Multiple Virtual Systems of the Same Firewall 

 Scheduled Configuration Push to Managed Firewalls 

 Unique Master Key for a Managed Firewall 

 Networking Features 

 LSVPN Cookie Expiry Extension 

 Persistent NAT for DIPP 

 Aggregate Group Members on Multiple Cards 

 Network Packet Broker 

 Identity Features 

 Cloud Identity Engine 

 User-ID Features 

 Group Mapping Centralization for Virtual System Hubs 

 URL Filtering Features 

 Enhanced Handling of SSL/TLS Handshakes for Decrypted Traffic 

 Advanced URL Filtering Security Subscription 

 SD-WAN Features 

 Prisma Access Hub Support 

 SD-WAN Support for AE and Subinterfaces 

 SD-WAN Support for Layer 3 Subinterfaces 

 GlobalProtect Features 

 Security Policy Enforcement for Inactive GlobalProtect Sessions 

 Support for Gzip Encoding in Clientless VPN 

 Virtualization Features 

 DPDK Support for Different NIC Types 

 CN-Series Firewall as a k8s Service 

 Intelligent Traffic Offload Service for VM‑Series on KVM 

 Customize Dataplane Cores 

 Mobile Infrastructure Security Features 

 5G Multi-access Edge Computing Security 

 Updated on 

 Mon Aug 28 18:43:40 PDT 2023 

 Focus 

 Home 

 PAN-OS 

 PAN-OS ® New Features Guide 

 Networking Features 

 Network Packet Broker 

 Download PDF 

 PAN-OS ® New Features Guide 

 Network Packet Broker 

 Table of Contents 

 Filter

 Version 

 10.1 

 10.1 

 Expand all | Collapse all 

 App-ID Features 

 App-ID Cloud Engine 

 SaaS Policy Rule Recommendation 

 Management Features 

 Audit Tracking for Administrator Activity 

 Device Certificate for Cortex Data Lake 

 PAN-OS OpenConfig Support 

 Persistent Uncommitted Changes on PAN-OS 

 Panorama Features 

 Authentication Key for Secure Onboarding 

 Optimization for Deploying Changes for Multiple Virtual Systems of the Same Firewall 

 Scheduled Configuration Push to Managed Firewalls 

 Unique Master Key for a Managed Firewall 

 Networking Features 

 LSVPN Cookie Expiry Extension 

 Persistent NAT for DIPP 

 Aggregate Group Members on Multiple Cards 

 Network Packet Broker 

 Identity Features 

 Cloud Identity Engine 

 User-ID Features 

 Group Mapping Centralization for Virtual System Hubs 

 URL Filtering Features 

 Enhanced Handling of SSL/TLS Handshakes for Decrypted Traffic 

 Advanced URL Filtering Security Subscription 

 SD-WAN Features 

 Prisma Access Hub Support 

 SD-WAN Support for AE and Subinterfaces 

 SD-WAN Support for Layer 3 Subinterfaces 

 GlobalProtect Features 

 Security Policy Enforcement for Inactive GlobalProtect Sessions 

 Support for Gzip Encoding in Clientless VPN 

 Virtualization Features 

 DPDK Support for Different NIC Types 

 CN-Series Firewall as a k8s Service 

 Intelligent Traffic Offload Service for VM‑Series on KVM 

 Customize Dataplane Cores 

 Mobile Infrastructure Security Features 

 5G Multi-access Edge Computing Security 

 Network Packet Broker 

 Use Network Packet Broker to forward traffic to external
security chains 

 The new Network Packet Broker feature
replaces Decryption Broker and expands its capabilities to filter
and forward not only decrypted TLS traffic, but also non-decrypted
TLS and non-TLS traffic, to one or more third-party appliances (a
security chain). The ability to filter and forward all traffic to
a security chain eliminates complications from dedicated decryption
devices and security chain management devices, thus simplifying
your network and reducing capital and operating costs. Network Packet
Broker checks path health to and from the security chain and filters
traffic based on applications, users, devices, IP addresses, and
zones. These features are especially valuable in very high security
environments such as financial and government institutions that
require offloading traffic to external security chains. 

 To get started with Network Packet Broker: 

 Install a free Network Packet
Broker license and enable the App-ID cache . Without the free
license, you can’t access the Packet Broker policy and profile configuration. 

 Identify the traffic that you want to forward to one or more
security chains. 

 The firewall must have at least two available Layer 3 Ethernet
interfaces to use as dedicated packet broker forwarding interfaces
to connect to the first and last devices in a security chain. You
can configure multiple pairs of packet broker forwarding interfaces
to connect to different security chains. Decide which pairs of firewall
interfaces to use as dedicated Network Packet Broker forwarding
interfaces. 

 Network Packet Broker supports routed Layer
3 security chains and Transparent Bridge Layer 1 security chains.
For routed Layer 3 chains, one pair of packet broker forwarding
interfaces can connect to multiple Layer 3 security chains using
a properly configured switch, router, or other device to perform
the required Layer 3 routing between the firewall and the security
chains. 

 Configure a Transparent Bridge security
chain or a routed layer 3 security
chain on the firewall using Packet Broker profiles and Network Packet
Broker policy rules. 

 None of the devices in the security
chain can modify the source or destination IP address, source or
destination port, or protocol of the original session because the
firewall would be unable to match the modified session to the original
session and therefore would drop the traffic. 

 You
can use Policy Optimizer to review
and tighten Network Packet Broker policy rules. 

 Network Packet Broker supports: 

 Decrypted TLS, non-decrypted TLS, and non-TLS traffic. 

 SSL Forward Proxy and SSL Inbound Inspection traffic. 

 Routed Layer 3 security chains. 

 Transparent Bridge Layer 1 security chains. 

 You
can configure both routed Layer 3 and Layer 1 Transparent Bridge
security chains on the same firewall but you must use different pairs
of forwarding interfaces for each type. 

 Unidirectional traffic flow through the chain: all traffic
to the chain egresses the firewall on one dedicated firewall interface
and returns to the firewall on another dedicated firewall interface,
so all traffic flows in the same direction. 

 Both firewall
forwarding interfaces must be in the same zone. 

 Bidirectional traffic flow through the security chain: 

 Client-to-server (c2s) traffic egresses the firewall on one
dedicated firewall broker interface and returns to the firewall
on another dedicated firewall broker interface. 

 Server-to-client (s2c) traffic uses the same two dedicated
firewall broker interfaces as c2s traffic, but the traffic flows
in the opposite direction through the security chain. The firewall
broker interface on which the s2c traffic goes to the chain is the
same interface on which the c2s traffic returns from the chain to
the firewall. The firewall broker interface on which the s2c traffic
returns to the firewall is the same interface on which the c2s traffic
egresses to the chain. 

 Network Packet Broker does not support multicast, broadcast,
or SSH traffic. 

 Previous 

 Aggregate Group Members on Multiple Cards 

 Next 

 Identity Features 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

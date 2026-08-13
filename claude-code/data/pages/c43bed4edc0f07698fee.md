---
url: https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-networking-admin/network-packet-broker/user-interface-changes-for-network-packet-broker
fetched_at: 2026-08-13T17:06:15Z
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

 >

 Strata Copilot

 Network Packet Broker 

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

 Network Packet Broker 

 Download PDF 

 Next-Generation Firewall 

 Network Packet Broker 

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

 Disable Tunnel Acceleration 

 Next 

 How Network Packet Broker Works 

 Network Packet Broker 

 Network Packet Broker sends decrypted, encrypted, and cleartext traffic to external
 chains of security appliances. 

 Where Can I Use This? What Do I Need? 

 NGFW (Managed by PAN-OS or Panorama) 

 NGFW (Managed by Strata
 Cloud Manager) 

 Network Packet Broker filters and forwards network traffic
to an external security chain of one or more third-party security
appliances. Network Packet Broker replaces the Decryption Broker
feature introduced in PAN-OS 8.1 and expands its capabilities to
include forwarding non-decrypted TLS traffic and non-TLS traffic
(cleartext) as well as decrypted TLS traffic. The ability to handle
all types of traffic is especially valuable in very high security
environments such as financial and government institutions. 

 Network Packet Broker is supported for PA-7000 Series, PA-7000b, PA-5400 Series, PA-5200 Series,
 PA-3400 Series, PA-3200 Series devices and VM-300 and VM-700 models. It requires SSL
 Forward Proxy decryption to be enabled, where the firewall is established as a trusted
 third party (or man-in-the-middle) to session traffic. 

 A firewall interface cannot be both a decryption broker and a GRE tunnel endpoint. 

 If you use one or more third-party security appliances (a security chain) as
 part of your overall security suite, you can use Network Packet Broker to filter and
 forward network traffic to those security appliances. Network Packet Broker replaces the
 Decryption Broker feature introduced in PAN-OS 8.1. 

 Like Decryption Broker, Network Packet Broker provides decryption
 capabilities and security chain management. This simplifies your network by eliminating
 complications from supporting dedicated devices for those functions and reduces capital
 and operating costs. Also like Decryption Broker, Network Packet Broker provides health
 checks to ensure that the path to the security chain is healthy and options for handling
 traffic if a chain goes down. 

 Network Packet Broker expands the firewall’s security chain forwarding
 capabilities so that you can filter and forward not only decrypted TLS traffic, but also
 non-decrypted TLS and non-TLS (cleartext) traffic to one or more security chains based
 on applications, users, devices, IP addresses, and zones. These features are especially
 valuable in very high security environments such as financial and government
 institutions. 

 Upgrade and downgrade: 

 When you upgrade to PAN-OS 11.1 on firewalls that have a Decryption Broker
 license: 

 The license name changes automatically to Network Packet Broker after you
 reboot the firewall. 

 You must reboot the firewall to make the license
 take effect and update the user interface regardless of whether the
 firewall is a standalone firewall, part of an HA pair, or if you push
 Network Packet Broker licenses to firewalls from Panorama. 

 PAN-OS translates any existing Decryption Broker Forwarding profiles ( Profiles Decryption Forwarding Profile ) into Packet Broker profiles. 

 PAN-OS translates any existing Decryption Policy rules for forwarding
 traffic to security chains into Network Packet Broker policy rules. 

 PAN-OS removes the Decryption Broker profile from the user interface and
 replaces it with the Packet Broker profile ( Profiles Packet Broker ), and also adds the Network Packet Broker policy ( Policies Network Packet Broker ). 

 When you downgrade to PAN-OS 10.0 from PAN-OS 10.1: 

 PAN-OS translates any existing Packet Broker profiles into Decryption
 Broker Forwarding profiles. 

 PAN-OS removes the Network Packet Broker rulebase and prints a warning
 message. You must reconfigure the Network Packet Broker policy rules as
 Decryption policy rules for Decryption Forwarding. 

 The license name remains Network Packet Broker (the license name changes
 from Decryption Broker to Network Packet Broker in all PAN-OS versions
 after a reboot and does not affect the operation of Decryption Broker).
 However, the functionality is Decryption Broker functionality, not
 Network Packet Broker functionality. 

 PAN-OS removes the Network Packet Broker profile from the user interface
 and replaces it with the Decryption Forwarding profile, and also removes
 the Network Packet Broker policy from the user interface (there is no
 replacement; you use Decryption Policy rules to forward only decrypted
 Forward Proxy traffic to security chains). 

 Requirements for using Network Packet Broker: 

 You must install a free Packet Broker license on the firewall. Without the free
 license, you can’t access the Packet Broker policy and profile in the interface.

 The firewall must have at least two available layer 3 Ethernet interfaces to use
 as a dedicated pair of packet broker forwarding interfaces. 

 You can configure multiple pairs of dedicated Network Packet Broker
 forwarding interfaces to connect to different security chains. 

 For each security chain, the pair of dedicated Network Packet Broker
 interfaces must be in the same security zone. 

 Security policy must allow traffic between each
 paired set of Network Packet Broker interfaces. The
 intrazone-default Security policy rule allows
 traffic within the same zone by default. However, if you have a “deny
 all” policy rule earlier in the policy rulebase, then you must create an
 explicit allow rule to allow the Network Packet Broker traffic. 

 The pair of dedicated interfaces connect to the first and last devices in
 a security chain. 

 Network Packet Broker supports routed layer 3 security
 chains and Transparent Bridge Layer 1 security chains. For routed layer 3
 chains, one pair of packet broker forwarding interfaces can connect to multiple
 layer 3 security chains using a properly configured switch, router, or other
 device to perform the required layer 3 routing between the firewall and the
 security chains. 

 Dedicated Network Packet Broker forwarding interfaces cannot use dynamic routing
 protocols. 

 None of the devices in the security chain can modify the source or destination IP
 address, source or destination port, or protocol of the original session because
 the firewall would not be able to match the modified session to the original
 session and therefore would drop the traffic. 

 You must enable the firewall to Allow forwarding of decrypted
 content ( Device Setup Content-ID ). 

 Network Packet Broker supports: 

 Decrypted TLS, non-decrypted TLS, and non-TLS traffic. 

 SSL Forward Proxy, SSL Inbound Inspection, and encrypted SSH traffic. 

 Routed layer 3 security chains. 

 Transparent Bridge layer 1 security chains. 

 You can configure both routed layer 3 and layer 1
 Transparent Bridge security chains on the same firewall but you must use
 different pairs of forwarding interfaces for each type. 

 Unidirectional traffic flow through the chain: all traffic to the chain egresses
 the firewall on one dedicated interface and returns to the firewall on another
 dedicated interface, so all traffic flows in the same direction through the pair
 of dedicated Network Packet Broker interfaces. 

 Both firewall forwarding interfaces must be in the same
 zone. 

 Bidirectional traffic flow through the security chain: 

 Client-to-server (c2s) traffic egresses the firewall on one dedicated
 firewall broker interface and returns to the firewall on another
 dedicated firewall broker interface. 

 Server-to-client (s2c) traffic uses the same two dedicated firewall
 broker interfaces as c2s traffic, but the traffic flows in the opposite
 direction through the security chain. The firewall broker interface on
 which the s2c traffic goes to the chain is the same interface on which
 the c2s traffic returns from the chain to the firewall. The firewall
 broker interface on which the s2c traffic returns to the firewall is the
 same interface on which the c2s traffic egresses to the chain. 

 Both firewall forwarding interfaces must be in the same
 zone. 

 Network Packet Broker does not support multicast, broadcast, or
 decrypted SSH traffic. 

 Previous 

 Disable Tunnel Acceleration 

 Next 

 How Network Packet Broker Works 

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

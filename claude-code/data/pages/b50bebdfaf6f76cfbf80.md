---
url: https://docs.paloaltonetworks.com/network-security/security-policy/administration/all-policy-types/nat
fetched_at: 2026-08-13T16:38:24Z
source: palo-alto-main
---

# NAT Clear

NAT 

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

 NAT 

 Updated on 

 Aug 5, 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Network Security Docs 

 Security Policy 

 IPsec VPN 

 Decryption 

 Device-ID 

 Quantum Security 

 Quality of Service 

 Updated on 

 Aug 5, 2026 

 Focus 

 Home 

 Network Security 

 Network Security: Security Policy 

 All Policy Types 

 NAT 

 Download PDF 

 Network Security 

 NAT 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Network Security Docs 

 Security Policy 

 IPsec VPN 

 Decryption 

 Device-ID 

 Quantum Security 

 Quality of Service 

 Previous 

 All Policy Types 

 Next 

 QoS 

 NAT 

 Where Can I Use This? What Do I Need? 

 NGFW (PAN-OS & Panorama Managed) 

 Prisma Access (Managed by Panorama) 

 Prisma SD-WAN 

 Check for any license or role requirements for the products you're using. 

 If you use private IP addresses within
your internal networks, you must use NAT to translate the private
addresses to public addresses that can be routed on external networks.
If you define Layer 3 interfaces on the firewall, you can configure a Network Address Translation
(NAT) policy to specify whether source or destination IP
addresses and ports are converted between public and private addresses
and ports. For example, private source addresses can be translated
to public addresses on traffic sent from an internal (trusted) zone
to a public (untrusted) zone. NAT is also supported on virtual wire
interfaces. 

 The NAT64 option translates
between IPv6 and IPv4 addresses, providing connectivity between
networks using disparate IP addressing schemes, and therefore a
migration path to IPv6 addressing. IPv6-to-IPv6 Network Prefix Translation
( NPTv6 ) translates one
IPv6 prefix to another IPv6 prefix. 

 Since NAT allows you to translate private, non-routable addresses
to one or more globally-routable addresses, it helps conserve an
organization’s routable IP addresses. NAT allows you to not disclose
the real IP addresses of hosts that need access to public addresses
and to manage traffic by performing port forwarding. You can use
NAT to solve network design challenges, enabling networks with identical
IP subnets to communicate with each other. The firewall supports
NAT on Layer 3 and virtual wire interfaces. 

 NAT rules are based on source and destination zones, source and
destination addresses, and application service (such as HTTP). Like
Security policies, NAT security rules are compared against incoming
traffic in sequence, and the first rule that matches the traffic
is applied. 

 As needed, add static routes to the local router so that traffic
to all public addresses is routed to the firewall. You may also
need to add static routes to the receiving interface on the firewall
to route traffic back to the private address. 

 PAN-OS 

 In PAN-OS, you create NAT security rules that instruct the firewall
which packet addresses and ports need translation and what the translated
addresses and ports are. 

 NAT Security Rules 

 Source NAT and Destination NAT 

 Destination NAT with DNS Rewrite
Use Cases 

 NAT Rule Capacities 

 Dynamic IP and Port NAT Oversubscription 

 Dataplane NAT Memory Statistics 

 Configure NAT 

 NAT Configuration Examples 

 NAT in Active/Active HA Mode 

 Prisma SD-WAN 

 Prisma SD-WAN 
 NAT Policies 

 Add a NAT Stack 

 Add NAT Policy Sets 

 Add a NAT Policy Rule 

 Add a NAT Policy Set to a NAT
Stack 

 Prisma Access 

 Secure Inbound Access Examples 

 Previous 

 All Policy Types 

 Next 

 QoS 

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

 Security Policy 

 Prisma Access 

 Panorama 

 Strata Cloud Manager 

 Security Policy 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

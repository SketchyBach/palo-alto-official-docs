---
url: https://docs.paloaltonetworks.com/advanced-ip-defense/getting-started/introducing-advanced-ip-defense
fetched_at: 2026-08-13T15:23:35Z
source: palo-alto-main
---

# Introducing Advanced IP Defense Clear

Introducing Advanced IP Defense 

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

 Introducing Advanced IP Defense 

 Updated on 

 May 22, 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Advanced IP Defense Docs 

 Activation & Onboarding 

 Getting Started 

 Administration 

 Release Notes 

 New Features 

 Updated on 

 May 22, 2026 

 Focus 

 Home 

 Advanced IP Defense 

 Introducing Advanced IP Defense 

 Download PDF 

 Advanced IP Defense 

 Introducing Advanced IP Defense 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Advanced IP Defense Docs 

 Activation & Onboarding 

 Getting Started 

 Administration 

 Release Notes 

 New Features 

 Previous 

 Verify Advanced IP Defense Cloud Connectivity 

 Next 

 How Advanced IP Defense Works 

 Introducing Advanced IP Defense 

 Advanced IP Defense is a cloud-delivered security service that provides real-time
 IP intelligence and direct-to-IP detection to stop outbound direct-to-IP threats and inbound
 attacks from masked origins. 

 Where Can I Use This? What Do I Need? 

 NGFW (Managed by Strata Cloud Manager ) 

 NGFW (Managed by PAN-OS or the Panorama® management server ) 

 VM-Series 

 Cloud NGFW for AWS 

 Cloud NGFW on Azure 

 Prisma Access 

 Advanced IP Defense license 

 PAN-OS 12.2 and later 

 Attackers frequently bypass traditional DNS-based and URL-based security controls by
 connecting directly to IP addresses. Malware establishes command-and-control (C2) channels
 through hardcoded IPs, and threat actors use proxies, anonymizers, and bulletproof hosting
 to mask their origins. Static third-party IP feeds suffer from delayed enforcement, can't
 distinguish between a malicious tenant and legitimate services on shared cloud
 infrastructure, and create significant operational overhead. 

 Palo Alto Networks Advanced IP Defense closes these gaps by combining two core
 capabilities: real-time IP intelligence that classifies public IP addresses across more
 than 19 dynamic attributes, and direct-to-IP detection that identifies connections made without
 a preceding DNS resolution. The Advanced IP Defense cloud service delivers these
 verdicts in real time, enabling your enforcement point to alert on or block traffic based on
 granular IP attribute categories and direct-to-IP behavior. Because Advanced IP Defense 
 operates at the network layer (IP and port), it does not require SSL/TLS decryption to
 deliver its security benefits. 

 With Advanced IP Defense , you can block outbound C2 connections that bypass DNS
 and URL inspection, restrict access to high-risk infrastructure such as anonymizers and
 bulletproof hosting without disrupting legitimate traffic on shared cloud IPs, and
 replace capacity-constrained static IP feeds with a cloud-scale intelligence service
 that tracks millions of malicious IP addresses and updates in real time. 

 Advanced IP Defense operates independently from other cloud-delivered security
 services. You do not need an Advanced DNS Security license to use Advanced IP Defense , and new IP attribute categories or tags can be delivered through content updates
 without requiring a PAN-OS upgrade. 

 IP Intelligence 

 Direct-to-IP Detection 

 IP Intelligence 

 Advanced IP Defense classifies publicly routable IPv4 addresses using dynamic,
 cloud-sourced attributes organized into seven categories. 

 The Advanced IP Defense cloud service continuously evaluates publicly routable IP
 addresses and assigns security attributes based on observed behavior, infrastructure
 ownership, and threat intelligence. Each attribute has a defined lifespan (TTL) that
 determines how long it remains active without new evidence. The Advanced IP Defense cloud service sets and
 unsets attributes immediately when positive or negative evidence is observed, keeping
 verdicts current and reducing the false positives common with static IP feeds. 

 Attributes are organized into seven categories. You reference these categories and their
 individual tags when building match rules in an Advanced IP Defense security
 profile. 

 Category Tags Description 

 Anonymizers and Proxies Tor Exit Node, Open Proxy, Private Proxy, Commercial VPN IP addresses associated with anonymizing services that mask the true
 origin of traffic, including Tor exit nodes, open and private proxy
 servers, and commercial VPN endpoints. 

 Netblock Owner CDN, AWS Cloud, GCP Cloud, Azure Cloud, OCI Cloud, Public Cloud,
 Residential ISP Infrastructure classification based on the registered owner of the IP
 address block. Use these tags to build rules that differentiate between
 cloud-hosted, CDN-hosted, and residential traffic. 

 Abuse Scanning and Brute-force IP addresses actively conducting scanning or brute-force activities
 confirmed with solid evidence. 

 Malware and C2 Malware C2, Malware Download, In Shellcode, Malware Communicated,
 Hardcoded in Malware IP addresses linked to malware distribution, command-and-control
 communication, exploitation payloads, or sandbox-observed
 connections. 

 High Risk Bulletproof Hosting IP addresses or subnets belonging to bulletproof hosting
 infrastructure that knowingly shelters malicious content and resists
 takedown requests. 

 Direct to IP (No individual tags) Connections made directly to an IP address without a preceding DNS
 resolution. This category is unique because it reflects connection
 behavior rather than a static IP attribute. 

 Vulnerable Services Exposed Vulnerable Service Publicly reachable services on IP addresses that are vulnerable to
 known CVEs or exploits. 

 Attributes are assigned per IP address, not per subnet. Threat-related attributes
 (Anonymizers and Proxies, Abuse, Malware and C2, High Risk, Vulnerable Services) use
 shorter TTL values to stay current with rapidly changing threats, while infrastructure
 attributes (Netblock Owner) use longer TTL values because they change less
 frequently. 

 The category and tag definitions are delivered through the PAN-OS content
 update package. When Palo Alto Networks adds new categories or tags, you receive them
 through a content update and they become available in the profile configuration UI without
 a PAN-OS upgrade. 

 Direct-to-IP Detection 

 Advanced IP Defense direct-to-IP detection identifies outbound connections made
 directly to IP addresses without a preceding DNS resolution, exposing potential C2 channels
 and data exfiltration attempts. 

 Attackers and unauthorized applications frequently bypass DNS-based security controls by
 connecting directly to IP addresses. Malware can communicate with C2 servers through
 hardcoded IPs, and data exfiltration can occur through direct IP connections to ephemeral
 cloud addresses that can't be blocked long-term. Direct-to-IP detection applies a zero trust
 approach to IP-based traffic by flagging any connection where the destination IP was not
 resolved through DNS. 

 How Direct-to-IP Detection Works 

 Your enforcement point forwards a copy of DNS response data (IP address and TTL pairs) to the
 Advanced IP Defense cloud service. The Advanced IP Defense cloud service builds a DNS Seen Table
 unique to your tenant that tracks every IP address resolved through DNS and when that
 resolution expires. 

 When your enforcement point queries the Advanced IP Defense cloud service about an IP address, the service checks
 whether that IP appears in your tenant's DNS Seen Table with a valid (non-expired)
 entry. If the IP has no DNS history or the entry has expired beyond a grace period,
 the Advanced IP Defense cloud service returns a direct-to-IP verdict. The grace period (currently 300 seconds)
 accounts for transmission delays and clients that use slightly expired cache
 entries. 

 Direct-to-IP detection applies only to publicly routable IP addresses in outbound traffic.
 All private IP ranges are allowlisted, so protocols that operate exclusively on
 internal networks (such as DHCP, mDNS, and NetBIOS) do not trigger false positives.
 Do not apply direct-to-IP rules to inbound traffic — direct-to-IP detection is designed
 for outbound sessions where a client initiates a connection without resolving the
 destination through DNS. 

 Profiling Period 

 When you first enable Advanced IP Defense on an enforcement point, a seven-day profiling
 period begins for that device. During this period: 

 The Advanced IP Defense cloud service learns your traffic patterns and
 identifies legitimate direct-to-IP connections specific to your environment. 

 An offline classification system analyzes direct-to-IP traffic using threat
 intelligence to distinguish benign connections from malicious ones. 

 Confirmed-benign direct-to-IP traffic is added to a customized allowlist for your
 enforcement point. 

 Direct-to-IP rules are not enforced during this period to prevent false
 positives. 

 After the profiling period completes, the direct-to-IP rules in your Advanced IP Defense profile begin enforcing. The Advanced IP Defense cloud service continues to monitor traffic patterns
 and updates the customized allowlist as your environment changes. 

 Allowlists 

 Advanced IP Defense uses three types of allowlists to reduce false positives and
 unnecessary cloud lookups: 

 Golden Allowlist — Applied to all customers and contains
 definitively-benign IP addresses such as well-known DNS resolvers and private IP
 ranges. Traffic to these IPs bypasses the Advanced IP Defense cloud lookup
 entirely. 

 Customized Allowlist — Generated per enforcement point based on traffic patterns
 learned during the profiling period and through ongoing analysis. Traffic to these
 IPs also bypasses the cloud lookup. 

 Direct-to-IP Allowlist — Contains IP addresses, ports, and IP-port combinations
 for protocols that legitimately use direct-to-IP connections (such as BGP, SIP,
 STUN, and BitTorrent). These entries skip only the direct-to-IP check while still
 allowing other IP attribute checks to proceed. 

 Your enforcement point downloads updated allowlists periodically. Entries are prioritized so
 that if memory constraints require truncation, the most critical entries are
 retained. 

 Previous 

 Verify Advanced IP Defense Cloud Connectivity 

 Next 

 How Advanced IP Defense Works 

 On This Page 

 Activation and Onboarding 

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

 Panorama 

 Service Provider 

 VM-Series 

 Plugins 

 SASE 

 Prisma Access 

 Prisma SASE Multitenant Platform 

 AI-Powered ADEM 

 Prisma Access Monitoring & Visibility 

 Prisma SD-WAN 

 ION Devices 

 Next-Generation CASB 

 Cloud-Delivered Security Services 

 Advanced WildFire 

 Advanced URL Filtering 

 Advanced Threat Prevention 

 Advanced DNS Security 

 AI Access Security 

 Device Security 

 Enterprise DLP 

 SaaS Security 

 Network Security 

 Shared Policy for NGFWs and Prisma Access 

 IPSec VPN 

 Security Policy 

 Quantum Security 

 Endpoints 

 GlobalProtect 

 Remote Browser Isolation 

 Prisma Access Agent 

 Visibility & Monitoring 

 Dashboards 

 Incidents and Alerts 

 Reports 

 Autonomous DEM 

 FedRAMP 

 Prisma SASE for FedRAMP 

 Autonomous DEM for FedRAMP 

 Hardware Reference 

 ION 1000 

 ION 1200 

 ION 1200-S 

 ION 2000 

 ION 3000 

 ION 3200 

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

 ION 5200 

 ION 9200 

 Virtual ION Deployment 

 Virtual ION on AWS 

 Virtual ION on Azure 

 Virtual ION on GCP 

 Virtual ION on Alibaba Cloud 

 Virtual ION on KVM for NFV 

 Virtual ION on Dell PowerEdge 

 Virtual ION on OCI 

 Virtual ION on VMware 

 Virtual ION on Megaport Virtual Edge 

 3rd Party Integrations 

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

 Experts Corner 

 Solutions Docs from Product Experts 

 Resources 

 All Products A - Z 

 All Release Notes 

 Compatibility Matrix 

 Experts Corner 

 Network Security Platform 

 Security Policy 

 Decryption 

 Device-ID 

 IPSec VPN 

 Quality of Service 

 Quantum Security 

 Advanced IP Defense 

 Getting Started 

 Cloud-Delivered Security Services 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

---
url: https://docs.paloaltonetworks.com/advanced-ip-defense/getting-started/introducing-advanced-ip-defense
fetched_at: 2026-09-15T15:08:17Z
source: palo-alto-main
---

# Introducing Advanced IP Defense Clear

Updated on 

 Fri Aug 28 11:54:00 PDT 2026 

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

 PAN-OS 12.2.3 and later 

 Attackers frequently bypass traditional DNS-based and URL-based security controls by
 connecting directly to IP addresses. Malware establishes command-and-control (C2) channels
 through hardcoded IPs, and threat actors use proxies, anonymizers, and bulletproof hosting
 to mask their origins. Static third-party IP feeds suffer from delayed enforcement, can't
 distinguish between a malicious tenant and legitimate services on shared cloud
 infrastructure, and create significant operational overhead. 

 Palo Alto Networks Advanced IP Defense closes these gaps by combining two core
 capabilities: real-time IP intelligence that classifies publicly routable IPv4 addresses across more
 than 19 dynamic attributes, and direct-to-IP detection that identifies connections made without
 a preceding DNS resolution. The Advanced IP Defense cloud service delivers these
 verdicts in real time, enabling your enforcement point to alert on or block traffic based on
 granular IP attribute categories and direct-to-IP behavior. Because Advanced IP Defense 
 operates at the network layer (IP and port), it does not require SSL/TLS decryption to
 deliver its security benefits. 

 With Advanced IP Defense , you can block outbound C2 connections that bypass DNS
 and URL inspection, defend against inbound attacks from attacker infrastructure such as
 scanners, exploit tools, and botnets, restrict access to high-risk services such as
 anonymizers and bulletproof hosting without disrupting legitimate traffic on shared cloud
 IPs, and replace capacity-constrained static IP feeds with a cloud-scale intelligence
 service that tracks millions of malicious IP addresses and updates in real time. 

 Advanced IP Defense operates independently from other cloud-delivered security
 services. You do not need an Advanced DNS Security license to use Advanced IP Defense , and content updates deliver new IP attribute categories or tags without requiring
 a PAN-OS upgrade. 

 IP Intelligence 

 Direct-to-IP Detection 

 IP Intelligence 

 Advanced IP Defense classifies publicly routable IPv4 addresses using dynamic,
 cloud-sourced attributes organized into seven categories. 

 Advanced IP Defense continuously evaluates publicly routable IP
 addresses and assigns security attributes based on observed behavior, infrastructure
 ownership, and threat intelligence. Each attribute has a defined lifespan (TTL) that
 determines how long it remains active without new evidence. Advanced IP Defense sets and
 unsets attributes immediately when positive or negative evidence is observed, keeping
 verdicts current and reducing the false positives common with static IP feeds. 

 Attributes are organized into seven categories. You reference these categories and their
 individual tags when building match rules in an Advanced IP Defense security
 profile. 

 Category Tags Description 

 Anonymizers and Proxies Tor Exit Node, Open Proxy, Private Proxy, Commercial VPN IP addresses associated with anonymizing services that mask the true
 origin of traffic, including Tor exit nodes, open and private proxy
 servers, and commercial VPN endpoints. 

 Association CDN, AWS Cloud, GCP Cloud, Azure Cloud, OCI Cloud, Public Cloud,
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

 Advanced IP Defense assigns attributes per IP address, not per subnet. Threat-related attributes
 (Anonymizers and Proxies, Abuse, Malware and C2, High Risk, Vulnerable Services) use
 shorter TTL values to stay current with rapidly changing threats, while infrastructure
 attributes (Association) use longer TTL values because they change less
 frequently. 

 The PAN-OS content update package delivers the category and tag definitions.
 When Palo Alto Networks adds new categories or tags, you receive them
 through a content update and they become available in the security profile configuration without
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

 Your enforcement point passively inspects DNS traffic crossing each zone and maintains
 a local DNS Seen Table of IP address and TTL pairs for each resolved domain. It also
 forwards a copy of this DNS response data to Advanced IP Defense . Advanced IP Defense then builds a DNS Seen Table unique to your tenant that
 tracks every IP address resolved through DNS and when that resolution expires,
 enabling cross-firewall detection in asymmetric routing environments. 

 When your enforcement point queries Advanced IP Defense about an IP address, Advanced IP Defense checks
 whether that IP appears in your tenant's DNS Seen Table with a valid (non-expired)
 entry. If the IP has no DNS history or the entry has expired beyond a grace period,
 Advanced IP Defense returns a direct-to-IP verdict. The grace period (currently 300 seconds)
 accounts for transmission delays and clients that use slightly expired cache
 entries. 

 Direct-to-IP detection applies only to publicly routable IP addresses in outbound traffic.
 Advanced IP Defense allowlists all private IP ranges, so protocols that operate exclusively on
 internal networks (such as DHCP, mDNS, and NetBIOS) do not trigger false positives.
 Do not apply direct-to-IP rules to inbound traffic — direct-to-IP detection is designed
 for outbound sessions where a client initiates a connection without resolving the
 destination through DNS. 

 Limitations 

 DNS-over-HTTPS (DoH) and DNS-over-TLS (DoT) 

 Direct-to-IP detection requires the firewall to passively inspect DNS traffic
 crossing a zone and parse IP-TTL pairs from DNS responses. If clients use
 DNS-over-HTTPS (DoH) or DNS-over-TLS (DoT), their DNS queries are encrypted within
 HTTPS or TLS sessions. This prevents the firewall from parsing the DNS responses,
 so resolved IPs are never registered in the DNS Seen Table. Subsequent connections
 to those IPs are then incorrectly flagged as direct-to-IP under a blocking
 policy. 

 Asymmetric routing 

 In networks with asymmetric routing, the DNS query and the subsequent application
 session may traverse different firewalls. If a client resolves a domain through one
 firewall but initiates the connection through a second firewall, the second firewall
 has no local record of the DNS resolution. While Advanced IP Defense builds a
 shared per-tenant DNS Seen Table in the cloud to mitigate this, synchronization
 delays can cause the second firewall to evaluate the connection as direct-to-IP
 before the cloud table is updated. The default fail-open cache-miss behavior
 minimizes disruption on the first packet, but strict enforcement rules in heavily
 asymmetric paths may produce intermittent false positives. 

 Initial Deployment Guidance 

 When you first enable direct-to-IP detection, configure your Advanced IP Defense 
 profile rules to use the Alert (Permit and Log) action for at
 least seven days before switching to Block (Drop & Log) .
 This observation period allows you to: 

 Identify legitimate direct-to-IP connections in your environment (such as
 infrastructure services, APIs, or health checks that connect without prior DNS
 resolution). 

 Create exceptions for known-good traffic before enforcement begins. 

 Evaluate detection accuracy and tune rules based on your specific traffic
 patterns. 

 After the observation period, review your threat logs to confirm that remaining
 direct-to-IP detections are genuine threats, then change the action to Block for
 high-confidence rules. 

 Allowlists 

 Advanced IP Defense uses allowlists to reduce false positives and
 unnecessary cloud lookups: 

 AIPD Allowlist — A cloud-maintained list of confirmed-benign IP addresses
 (such as well-known DNS resolvers and major infrastructure providers). Traffic to
 these IPs bypasses the Advanced IP Defense cloud lookup entirely. 

 No-DNS Allowlist — Contains IP addresses, ports, and IP-port
 combinations for protocols that legitimately use direct-to-IP connections.
 These entries skip the direct-to-IP check while still allowing other IP
 attribute checks to proceed. 

 Your enforcement point downloads updated allowlists periodically. Advanced IP Defense prioritizes entries so
 that if memory constraints require truncation, the most critical entries are
 retained.

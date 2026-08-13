---
url: https://docs.paloaltonetworks.com/advanced-ip-defense/getting-started/advanced-ip-defense-ip-attributes-reference
fetched_at: 2026-08-13T15:23:34Z
source: palo-alto-main
---

# Advanced IP Defense IP Attributes and Categories Clear

Advanced IP Defense IP Attributes and Categories 

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

 Advanced IP Defense IP Attributes and Categories 

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

 Advanced IP Defense IP Attributes and Categories 

 Download PDF 

 Advanced IP Defense 

 Advanced IP Defense IP Attributes and Categories 

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

 How Advanced IP Defense Works 

 Next 

 Advanced IP Defense Predefined EDLs (PAN-OS 11.1 and PAN-OS 12.1) 

 Advanced IP Defense IP Attributes and Categories 

 Reference guide for all IP attributes available in Advanced IP Defense for creating policy rules and configuring security policies. 

 Advanced IP Defense provides real-time IP attributes that enable granular, context-aware
 security policies. Each IP attribute represents a specific classification or
 characteristic of an IP address, allowing you to create policy rules based on the threat
 profile and behavior of the IP. This reference guide documents all available IP
 attributes organized by category. 

 IP Attribute Overview 

 IP attributes are assigned to publicly routable IPv4 addresses based on real-time threat intelligence and behavioral analysis. Each attribute has the following characteristics: 

 Attribute ID: A unique identifier for the attribute maintained by the Advanced IP Defense cloud service 

 Short Name: A human-readable identifier used in policy rules and logs 

 Description: A detailed explanation of what the attribute represents 

 Value Type: Boolean (true/false), integer, or string 

 Cache TTL: The time-to-live (TTL) in seconds that the attribute is cached locally before requiring a new cloud lookup 

 Block Action Disable: Indicates whether the attribute can be disabled for blocking actions 

 Advanced IP Defense only provides attributes for publicly routable IPv4 addresses. Private IP addresses are automatically allowlisted and do not receive IP attributes. 

 Anonymizers & Proxies 

 Attributes in this category identify IP addresses used for anonymization and proxy services. These attributes help detect traffic from users or systems attempting to mask their identity or bypass geographical restrictions. 

 Attribute Description 

 Tor Exit Node The IP is used as a Tor exit node, allowing users to anonymously
 access the internet through the Tor network. 

 Open Proxy IP hosting proxy services (HTTP, SOCKS, OpenVPN, V2Ray, etc.)
 that are accessible by any internet user without authentication.
 Mutually exclusive with private proxy and commercial VPN. 

 Private Proxy Proxies that require authentication and cannot be attributed to
 other anonymization services. Mutually exclusive with open proxy and
 commercial VPN. 

 Commercial VPN IPs owned by a commercial VPN service provider that allows
 individuals to encrypt their internet traffic and mask their IP
 addresses. Mutually exclusive with open proxy and private
 proxy. 

 Netblock Owner 

 Attributes in this category identify the owner or operator of the IP address netblock. These attributes help distinguish between legitimate cloud and CDN infrastructure and other types of IP addresses. 

 These attributes show associations and cannot be used as a category to block. You
 must select at least one attribute when using Netblock
 Owner . 

 Attribute Description 

 Content Delivery Network (CDN) Rentable CDN IPs that are officially confirmed by CDN providers
 or owned by major CDN providers hosting many domains. Mutually
 exclusive with residential and mobile ISP. 

 AWS Cloud The IP belongs to Amazon Web Services (AWS), a major public cloud
 provider. 

 GCP Cloud The IP belongs to Google Cloud Platform (GCP), a major public
 cloud provider. 

 Azure Cloud The IP belongs to Microsoft Azure, a major public cloud
 provider. 

 OCI Cloud The IP belongs to Oracle Cloud Infrastructure (OCI), a major
 public cloud provider. 

 Public Cloud Rentable public cloud IPs that are officially confirmed by cloud
 providers or owned by known cloud providers providing shared
 computing resources. Mutually exclusive with residential and mobile
 ISP. 

 Residential ISP Residential IP address assigned by an Internet Service Provider
 (ISP) to residential customers. Mutually exclusive with other
 netblock owner attributes. 

 Abuse 

 Attributes in this category identify IP addresses engaged in abusive or malicious activities such as scanning, brute-force attacks, and other reconnaissance activities. 

 Attribute Description 

 Scanning and Brute-force The IP is conducting scanning or brute-force activities with
 solid evidence. This includes port scanning, vulnerability scanning,
 and credential brute-force attacks. 

 Malware & C2 

 Attributes in this category identify IP addresses associated with malware, command-and-control (C2) servers, and malware distribution infrastructure. 

 Attribute Description 

 Malware C2 The IP is hosting command-and-control (C2) services or is bound
 to C2 domains. Malware communicates with these IPs to receive
 commands or exfiltrate data. 

 Malware Download The IP is distributing malware or the content hosted on the IP is
 malware. This includes malware repositories and infected file
 hosting services. 

 In Shellcode The IP appeared in an exploitation payload's shellcode,
 indicating it is used for post-exploitation attacks. These IPs are
 identified from Advanced Threat Prevention threat and device
 telemetry. 

 Malware Communicated A malware sample communicated with the IP during sandbox
 analysis. This indicates the IP is used for malware
 command-and-control or data exfiltration. 

 Hardcoded in Malware The IP is hardcoded in malware samples. Attackers often hardcode
 C2 server IPs in malware to ensure communication even if DNS
 resolution is blocked. 

 High Risk 

 Attributes in this category identify IP addresses associated with high-risk infrastructure and services that pose significant security threats. 

 Attribute Description 

 Bulletproof Hosting The IP or subnet belongs to a bulletproof hosting infrastructure.
 These are hosting services specifically designed to host malicious
 content and resist takedown efforts. 

 Direct-to-IP Detection 

 The Direct-to-IP attribute identifies connections made directly to an IP address without a prior DNS resolution. This attribute detects potential malware command-and-control communications and data exfiltration attempts that bypass DNS-based security controls. 

 The Direct-to-IP category does not contain individual tag attributes. Use it
 only with the match operator; the "does not match" operator is not
 supported for this category. 

 Attribute Description 

 No DNS (Direct-to-IP) The connection is made directly to an IP address without a prior
 DNS lookup. Advanced IP Defense tracks local DNS resolution history
 and identifies any direct-to-IP connections that may indicate
 malware activity or data exfiltration. 

 Direct-to-IP detection uses a zero-trust approach to IP-based traffic. The enforcement point maintains a local DNS cache and compares incoming connections against this cache. If a connection is made to an IP address that was not recently resolved through DNS, it is flagged as a direct-to-IP connection. A grace period of 300 seconds is applied to account for transmission delays and clients using slightly-expired cache entries. 

 Vulnerable Services 

 Attributes in this category identify IP addresses hosting publicly reachable services that are vulnerable to known exploits. 

 Attribute Description 

 Exposed Vulnerable Service A publicly reachable service on an IP host that is vulnerable to
 known CVEs or exploits. These services are potential targets for
 attackers seeking to compromise systems. 

 Using IP Attributes in Policy Rules 

 You can use IP attributes to create granular policy rules that enforce security policies based on the threat profile of IP addresses. When creating policy rules, you can: 

 Select individual attributes to match specific threat classifications 

 Combine multiple attributes using logical operators (AND, OR) to create complex match criteria 

 Use NOT operators to exclude specific attributes from matching 

 Define actions (Block, Allow, Alert) based on attribute matches 

 Set log severity levels to control how matched traffic is logged 

 For example, you can create a policy rule that blocks traffic to IPs classified as both "Malware C2" AND "Direct-to-IP Detection" to prevent malware from establishing command-and-control communications using hardcoded IP addresses. 

 IP Attribute Caching 

 Advanced IP Defense caches IP attributes locally on the enforcement point to reduce cloud lookups and improve performance. Each attribute has a cache TTL (time-to-live) that determines how long the attribute is cached before requiring a new cloud lookup. 

 When the cache expires, the enforcement point queries the Advanced IP Defense cloud service for updated attribute information. On a cache miss, the firewall allows the initial session to pass (fail-open) and asynchronously queries the Advanced IP Defense cloud service. Once the verdict is returned, the local cache is repopulated and the policy is enforced on subsequent sessions. 

 IP Attribute Accuracy and False Positives 

 Advanced IP Defense is designed to minimize false positives for IP attribution. To achieve high accuracy, the service uses multiple detection methods and sources, including OSINT feeds and custom honeypots. 

 Additionally, Advanced IP Defense provides allowlists and exceptions to exclude legitimate traffic from policy enforcement, further reducing false positives and operational overhead. 

 Previous 

 How Advanced IP Defense Works 

 Next 

 Advanced IP Defense Predefined EDLs (PAN-OS 11.1 and PAN-OS 12.1) 

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

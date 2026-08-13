---
url: https://docs.paloaltonetworks.com/vm-series/activation-and-onboarding/software-ngfw/maximum-limits-based-on-memory/maximum-limits-based-on-memory-12-2
fetched_at: 2026-08-13T17:41:01Z
source: palo-alto-main
---

# 12.2 Clear

12.2 

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

 12.2 

 Updated on 

 Fri Jun 19 07:15:14 PDT 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 VM-Series Firewall Docs 

 Activation & Onboarding 

 Getting Started 

 Upgrade 

 Deployment 

 Select a Document 

 Public Cloud 

 Private Cloud 

 Updated on 

 Fri Jun 19 07:15:14 PDT 2026 

 Focus 

 Home 

 VM-Series 

 Software NGFW Credits 

 Maximum Limits Based on Memory 

 12.2 

 Download PDF 

 VM-Series 

 12.2 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 VM-Series Firewall Docs 

 Activation & Onboarding 

 Getting Started 

 Upgrade 

 Deployment 

 Select a Document 

 Public Cloud 

 Private Cloud 

 12.2 

 Sessions 

 Tier 2 14 GB 16 GB 18 GB 

 Max sessions 

 (IPv4 or IPv6) 

 512,000 

 512,000 

 1,200,000 

 Max Default Dataplane vCPUs 

 4 

 12 

 12 

 Tier 3 24 GB 28 GB 32 GB 56 GB 64 GB 

 Max sessions 

 (IPv4 or IPv6) 

 2,500,000 

 2,800,000 

 3,500,000 

 8,500,000 

 8,250,000 

 Max Default Dataplane vCPUs 

 12 

 12 

 12 

 24 

 47 

 Tier 4 121 - 128 GB 

 Max sessions 

 (IPv4 or IPv6) 

 10,000,000 

 Max Default Dataplane vCPUs 

 47 

 Policies 

 Feature Tier 2 Tier 3 Tier 4 

 Security rules 10,000 20,000 

 65,000 

 Security rule schedules 

 256 

 256 

 256 

 NAT rules 

 8,000 15,000 

 16,000 

 Decryption rules 

 1,000 

 2,000 

 5,000 

 App override rules 

 1,000 

 2,000 

 4,000 

 Tunnel content inspection rules 

 500 

 2,000 

 8,500 

 SD-WAN rules 

 300 

 300 

 1,000 

 Policy based forwarding rules 

 500 

 2,000 

 2,000 

 Captive portal rules 

 1,000 

 2,000 

 8,000 

 DoS protection rules 

 1,000 

 1,000 

 2,000 

 Security Zones 

 Feature Tier 2 Tier 3 Tier 4 

 Max security zones 

 200 200 

 17,000 

 Objects (addresses and services) 

 Feature Tier 2 Tier 3 Tier 4 

 Address objects 

 20,000 

 40,000 

 160,000 

 Address groups 

 2,500 

 4,000 

 80,000 

 Members per address group 

 2,500 

 2,500 

 2,500 

 Service objects 

 2,000 

 5,000 

 12,000 

 Service groups 

 250 

 500 

 6,000 

 Members per service group 

 500 

 500 

 2,500 

 FQDN address objects 

 2,000 

 2,000 

 6,144 

 Max DAG IP addresses* 

 (system wide capacity) 

 300,000 

 300,500 

 500,000 

 Tags per IP address 

 32 

 32 

 64 

 * Firewall throughput measured with App-ID and User-ID features enabled utilizing
 AppMix transactions. 

 Security Profiles 

 Feature Tier 2 Tier 3 Tier 4 

 Security Profiles 

 750 

 750 

 750 

 App-ID 

 Feature Tier 2 Tier 3 Tier 4 

 Custom App-ID signatures 

 6,000 

 6,000 

 6,000 

 Shared custom App-IDs 

 512 

 512 

 512 

 Custom App-IDs 

 (virtual system specific) 

 6,416 

 6,416 

 6,416 

 User-ID 

 Feature Tier 2 Tier 3 Tier 4 

 IP-User mappings (management plane) 

 524,288 

 524,288 

 524,288 

 IP-User mappings (data plane) 

 512,000 

 512,000 

 512,000 

 Active and unique groups used in policy (aggregate of LDAP
 groups, XML API Groups, and Dynamic User Group).* 

 10,000 

 10,000 

 10,000 

 Number of User-ID agents 

 100 

 100 

 100 

 Monitored servers for User-ID 

 100 

 100 

 100 

 Terminal server agents 

 2,000 

 2,500 

 2,500 

 Tags per User* 

 (PAN-OS 9.1 and later) 

 32 

 32 

 32 

 *Firewall throughput measured with App-ID and User-ID features enabled utilizing
 AppMix transactions. 

 SSL Decryption 

 Feature Tier 2 Tier 3 Tier 4 

 Max SSL inbound certificates 

 1,000 

 1,000 

 4,000 

 SSL certificate cache 

 (forward proxy) 

 4,000 

 8,000 

 32,000 

 Max concurrent decryption sessions 

 50,000 100,000 

 2,000,000 

 SSL Port Mirror 

 Yes 

 Yes 

 Yes 

 SSL Decryption Broker 

 No 

 Yes 

 Yes 

 HSM Supported 

 Yes 

 Yes 

 Yes 

 URL Filtering 

 Feature Tier 2 Tier 3 Tier 4 

 Total entries for allow list, block list and custom
 categories 

 25,000 

 100,000 

 100,000 

 Max custom categories 

 2,849 

 2,849 

 2,849 

 Max custom categories (virtual system specific) 

 500 

 500 

 500 

 Dataplane cache size for URL filtering 

 90,000 

 250,000 

 250,000 

 Management plane dynamic cache size 

 100,000 

 600,000 

 900,000 

 EDL 

 Feature Tier 2 Tier 3 Tier 4 

 Max number of custom lists 

 30 

 30 

 30 

 Max number of IPs per system 

 50,000 

 50,000 

 150,000 

 Max number of DNS Domains per system 

 2,000,000 2,000,00 

 4,000,000 

 Max number of URL per system 

 100,000 

 100,000 

 250,000 

 Shortest check interval (min) 

 5 

 5 

 5 

 Interfaces 

 Feature Tier 2 Tier 3 Tier 4 

 Mgmt - out-of-band 

 NA 

 NA 

 NA 

 Mgmt - 10/100/1000 high availability 

 NA 

 NA 

 NA 

 Mgmt - 40Gbps high availability 

 NA 

 NA 

 NA 

 Mgmt - 10Gbps high availability 

 NA 

 NA 

 NA 

 Traffic - 10/100/1000 

 NA 

 NA 

 NA 

 Traffic - 100/1000/10000 

 NA 

 NA 

 NA 

 Traffic - 1Gbps SFP 

 NA 

 NA 

 NA 

 Traffic - 10Gbps SFP+ 

 NA 

 NA 

 NA 

 Traffic - 40/100Gbps QSFP+/QSFP28 

 NA 

 NA 

 NA 

 802.1q tags per device 

 4,094 

 4,094 

 4,094 

 802.1q tags per physical interface 

 4,094 

 4,094 

 4,094 

 Max interfaces (logical and physical) 

 4,096 

 4,096 4,096 

 Maximum aggregate interfaces 

 NA 

 NA 

 NA 

 Maximum SD-WAN virtual interfaces 

 1,000 

 1,000 

 1,000 

 Virtual Routers 

 Feature Tier 2 Tier 3 Tier 4 

 Virtual routers 

 20 

 125 

 225 

 Virtual Wires 

 Feature Tier 2 Tier 3 Tier 4 

 Virtual wires 12 

 12 

 12 

 Virtual Systems 

 Feature Tier 2 Tier 3 Tier 4 

 Base virtual systems 

 1 

 1 

 1 

 Max virtual systems 

 Additional licenses are required for virtual system capacities
 above the base virtual system’s capacity 

 NA 

 NA 

 NA 

 Routing 

 Feature Tier 2 Tier 3 Tier 4 

 IPv4 forwarding table size* 

 (Entries shared across virtual routers) 

 32,000 

 100,000 

 228000 

 IPv6 forwarding table size* 

 (Entries shared across virtual routers) 

 32,000 

 100,000 

 228000 

 System total forwarding table size 

 32,000 

 100,000 

 456000 

 Max route maps per virtual router 

 50 

 50 

 50 

 Max routing peers (protocol dependent) 

 1,000 

 1,000 

 1024 

 Static entries-DNS proxy 

 1,024 

 1,024 

 1024 

 Bidirectional Forwarding Detection (BFD) Sessions 

 1,024 

 1,024 

 1024 

 *Firewall throughput measured with App-ID and User-ID features enabled utilizing
 AppMix transactions. 

 L2 Forwarding 

 Feature Tier 2 Tier 3 Tier 4 

 ARP table size per device 

 32,000 

 128,000 

 132,000 

 IPv6 neighbor table size 

 32,000 

 128,000 

 132,000 

 MAC table size per device 

 32,000 

 128,000 

 132,000 

 Max ARP entries per broadcast domain 

 32,000 

 128,000 

 132,000 

 Max MAC entries per broadcast domain 

 32,000 

 128,000 

 132,000 

 NAT 

 Feature Tier 2 Tier 3 Tier 4 

 Total NAT rule capacity 

 8,000 

 8,000 

 16000 

 Max NAT rules (static)* 

 (Configuring static NAT rules to full capacity requires that no
 other NAT rule types are used.) 

 8,000 

 8,000 

 16000 

 Max NAT rules (DIP)* 

 (Configuring DIP NAT rules to full capacity requires that no
 other NAT rule types are used.) 

 8,000 

 8,000 

 16000 

 Max NAT rules (DIPP) 

 2,000 

 2,000 

 4000 

 Max translated IPs (DIP) 

 160,000 

 160,000 

 16000 

 Max translated IPs (DIPP)* 

 (DIPP translated IP capacity is proportional to the DIPP pool
 oversubscription value. The capacity shown here is based on an
 oversubscription value of 1x.) 

 2,000 

 2,000 

 4000 

 Default DIPP pool oversubscription* 

 (Source IP and source port reuse across concurrent sessions) 

 8 8 

 8 

 *Firewall throughput measured with App-ID and User-ID features enabled utilizing
 AppMix transactions. 

 Address Assignment 

 Feature Tier 2 Tier 3 Tier 4 

 DHCP servers 

 20 

 125 

 To be added 

 DHCP relays* 

 (Maximum capacity represents total DHCP servers and DHCP relays
 combined) 

 500 

 500 

 To be added 

 Max number of assigned addresses 64,000 64,000 

 To be added 

 *Firewall throughput measured with App-ID and User-ID features enabled utilizing
 AppMix transactions. 

 High Availability 

 Feature Tier 2 Tier 3 Tier 4 

 Devices supported 

 2 

 2 

 2 

 Max virtual addresses 

 32 

 128 

 To be added 

 QoS 

 Feature Tier 2 Tier 3 Tier 4 

 Number of QoS policies 

 2,000 

 4,000 

 To be added 

 Physical interfaces supporting QoS 

 12 12 

 12 

 Clear text nodes per physical interface 

 63 63 

 63 

 DSCP marking by policy 

 Yes 

 Yes 

 Yes 

 Subinterfaces supported 

 NA 

 NA 

 NA 

 IPSec VPN 

 Feature Tier 2 Tier 3 Tier 4 

 Max IKE Peers 

 1,000 

 2,000 

 To be added 

 Site to site (with proxy id) 

 4,000 

 8,000 

 To be added 

 SD-WAN IPSec tunnels 

 1,000 

 2,000 

 To be added 

 GlobalProtect Client VPN 

 Feature Tier 2 Tier 3 Tier 4 

 Max tunnels (SSL, IPSec, and IKE with XAUTH) 

 6,000 

 12,000 

 To be added 

 GlobalProtect Clientless VPN 

 Feature Tier 2 Tier 3 Tier 4 

 Max SSL tunnels 

 1,200 

 2,500 

 25,000 

 Multicast 

 Feature Tier 2 Tier 3 Tier 4 

 Replication (egress interfaces) 

 100 

 100 

 To be added 

 Routes 

 4,000 

 4,000 

 To be added 

 On This Page 

 Activation and Onboarding 

 Strata Cloud Manager 

 Next-Generation Firewalls 

 Firewalls 

 PAN-OS 

 PAN-OS SD-WAN 

 VM-Series 

 Plugins 

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

 Resources 

 All Release Notes 

 Compatibility Matrix 

 Experts Corner 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

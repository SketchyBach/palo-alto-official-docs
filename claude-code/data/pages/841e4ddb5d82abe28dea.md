---
url: https://docs.paloaltonetworks.com/network-security/ipsec-vpn/administration/ipsec-vpn-basics/internet-key-exchange-ike-for-vpn/ike-gateway
fetched_at: 2026-08-12T14:07:22Z
source: strata-and-sase
---

# IKE
Gateway Clear

IKE
Gateway 

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

 IKE
Gateway 

 Updated on 

 Jun 29, 2026 

 Focus 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

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

 Jun 29, 2026 

 Focus 

 Home 

 Network Security 

 IPSec VPN Basics 

 Internet Key Exchange (IKE) for VPN 

 IKE
Gateway 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 Network Security 

 IKE
Gateway 

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

 Internet Key Exchange (IKE) for VPN 

 Next 

 IKE Phase 1 

 IKE
Gateway 

 Where
 Can I Use This? What
 Do I Need? 

 PAN-OS 

 No license required 

 The Palo Alto Networks firewalls or a firewall and another security device that initiate and
 terminate VPN connections across the two networks are called the IKE Gateways. To set up
 the VPN tunnel and send traffic between the IKE Gateways, each peer must have an IP
 address—static or dynamic—or FQDN. The VPN peers use pre-shared keys or certificates to
 authenticate each other mutually. 

 ( In IKEv1 ) The peers must also negotiate the mode—main or aggressive—for setting up the
 VPN tunnel and the SA lifetime in IKE Phase 1. The main mode protects the identity of the
 peers and is more secure because more packets are exchanged when setting up the tunnel. Main
 mode is the recommended mode for IKE negotiation if both peers support it. Aggressive mode
 uses fewer packets to set up the VPN tunnel and is hence a faster but a less secure option for
 setting up the VPN tunnel. 

 ( In IKEv2 ) IKEv2 negotiation process between the IKE gateways is much more
 efficient and simplified compared to IKEv1 negotiation. IKEv2 performs three types of
 exchanges: initial exchanges, CREATE_CHILD_SA exchange, and INFORMATIONAL exchange. IKEv2 uses
 the following two exchanges during the initial exchange process each with two messages. 

 IKE_SA_INIT exchange—Negotiates IKE SA parameters and exchanges keys. 

 IKE_AUTH exchange—Authenticates the identity of the peer and establishes IPSec SAs. 

 After the four-message initial exchanges, IKEv2 sets up one IKE SA and one pair of
 IPSec SAs. To set up one IKE SA and one pair of IPSec SAs, IKEv1 goes through two phases that
 use a minimum of six messages. 

 To set up one more pair of IPSec SAs within the IKE SA, IKEv2 goes on to perform an
 additional two-message exchange—the CREATE_CHILD_SA exchange. One CREATE_CHILD_SA exchange
 creates one pair of IPSec SAs. IKEv2 also uses the CREATE_CHILD_SA exchange to re-key IKE SAs
 and Child SAs. 

 IKEv2 uses the INFORMATIONAL exchange for errors and notifications. 

 See Set Up an IKE Gateway for
configuration details. 

 Previous 

 Internet Key Exchange (IKE) for VPN 

 Next 

 IKE Phase 1 

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

 VPNs 

 Network Security 

 PAN-OS 

 Next-Generation Firewall 

 IKE 

 Site-to-Site VPN 

 IPsec VPN 

 IPSec 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

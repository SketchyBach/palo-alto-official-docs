---
url: https://docs.paloaltonetworks.com/network-security/ipsec-vpn/administration/ipsec-vpn-basics/internet-key-exchange-ike-for-vpn
fetched_at: 2026-08-12T14:07:21Z
source: strata-and-sase
---

# Internet Key Exchange (IKE) for VPN Clear

Internet Key Exchange (IKE) for VPN 

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

 Internet Key Exchange (IKE) for VPN 

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

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 Network Security 

 Internet Key Exchange (IKE) for VPN 

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

 VPN Deployments 

 Next 

 IKE Gateway 

 Internet Key Exchange (IKE) for VPN 

 Where Can I Use This? What Do I Need? 

 PAN-OS 

 No license required 

 The IKE process allows the VPN peers at both ends of the tunnel to encrypt and decrypt
 packets using mutually agreed-upon keys or certificate and method of encryption. The IKE
 process occurs in two phases: IKE Phase 1 and
 IKE Phase 2 .

 IKE Phase 1—Initially, a VPN peer will exchange the proposals for security services,
 such as, encryption algorithms, authentication algorithm, hash function. Both the
 VPN peers will form a security association which is a collection of parameters that
 the two devices use. When both the VPN peers of the tunnel agree to accept a set of
 security parameters, the IKE phase 1 is completed. 
 There are two modes in IKE
 phase 1, main mode and aggressive mode. 

 IKE Phase 2—Once the IKE phase 1 is completed successfully, IKE phase 2 is
 initiated. The security associations and services between the VPN peers are
 negotiated in IKE phase 2. The VPN peers of the tunnel will negotiate which protocol
 (Authentication Header or Encapsulation Security Protocol) and which algorithm to
 use. 
 IKE Phase 2 operates only in quick mode. 

 Each of these phases uses keys and encryption algorithms that are
 defined using cryptographic profiles— IKE Crypto profile and IPSec Crypto profile—and
 the result of the IKE negotiation is a security association (SA). An SA is a set of
 mutually agreed-upon keys and algorithms that are used by both VPN peers to allow the
 flow of data across the VPN tunnel. The following illustration depicts the key exchange
 process for setting up the VPN tunnel: 

 Previous 

 VPN Deployments 

 Next 

 IKE Gateway 

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

 © 2026 Palo Alto Networks, Inc. All rights reserved.

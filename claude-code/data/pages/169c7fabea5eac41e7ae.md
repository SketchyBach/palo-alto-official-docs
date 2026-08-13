---
url: https://docs.paloaltonetworks.com/next-gen-trust-security/next-gen-trust-security/about-vaas/co-overview-issuing-certs/adding-a-certificate-authority/c-custom-ca-overview/r-sectigo-example/c-sectigo-certificate-terms
fetched_at: 2026-08-13T16:38:53Z
source: palo-alto-main
---

# Sectigo Certificate Term Settings and Issuance Validity Clear

Sectigo Certificate Term Settings and Issuance Validity 

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

 Sectigo Certificate Term Settings and Issuance Validity 

 Updated on 

 Tue Jul 28 08:20:33 PDT 2026 

 Focus 

 Filter

 Expand All 
 | 
 Collapse All 

 Next-Gen Trust Security Docs 

 Getting Started 

 Updated on 

 Tue Jul 28 08:20:33 PDT 2026 

 Focus 

 Home 

 Next‑Gen Trust Security 

 Next-Gen Trust Security 

 Next-Gen Trust Security Overview 

 Overview: Certificate Issuance 

 Adding a Certificate Authority 

 Create a Custom Certificate Authority (CA) 

 Create a Sectigo Certificate Manager (VSatellite) Configuration 

 Sectigo Certificate Term Settings and Issuance Validity 

 Next‑Gen Trust Security 

 Sectigo Certificate Term Settings and Issuance Validity 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Next-Gen Trust Security Docs 

 Getting Started 

 Previous 

 Create a Sectigo Certificate Manager (VSatellite) Configuration 

 Next 

 Working with Custom CA Connectors in the Certificate Authorities Inventory 

 Sectigo Certificate Term Settings and Issuance Validity 

 When creating certificates, Sectigo's certificate profiles use static "terms" instead of an arbitrary number of days to determine certificate validity periods, while Next-Gen Trust Security uses arbitrary numbers. 

 The Sectigo CA Connector accounts for this difference by intelligently matching the number you select to the closest Sectigo term setting. 

 The following table gives an example of how a Next-Gen Trust Security request could match to the Sectigo terms, if these are the terms that apply to the Sectigo account: 

 Next-Gen Trust Security request Sectigo term options Result 

 7 day certificate request Sectigo minimum term length is 30 days Issued certificate will be valid for 30 days. 

 20 day certificate request Sectigo terms allow for 15 day, 45 day, or 90 day terms Issued certificate will be valid for 45 days, since that is the minimum term that covers the requested period. 

 2 year certificate request Sectigo maximum term length is 398 days for your account Issued certificate will be valid for 398 days, since that is the maximum allowed by any available term. This is the only case where the issued certificate will be valid for a shorter term than was requested. 

 When you create a request policy in Next-Gen Trust Security, you specify the maximum validity a user may request, and this is the default validity that is used if the user does not specify a validity in their request. 

 Because of the way Next-Gen Trust Security maps validity to available terms in Sectigo, it is possible for the validity of issued certificates to exceed the maximum validity specified by the request policy. This scenario is possible in situations where the maximum validity specified in the request policy does not exactly match one of the defined Sectigo terms, and only if the Sectigo term is longer than the maximum request policy validity. Consider these two examples: 

 Next-Gen Trust Security request Max validity from request policy Sectigo terms Result 

 150 days 180 days 45 days, 90 days The issued certificate will be valid for 90 days 

 150 days 180 days 100 days, 200 days The issued certificate will be valid for 200 days 

 Previous 

 Create a Sectigo Certificate Manager (VSatellite) Configuration 

 Next 

 Working with Custom CA Connectors in the Certificate Authorities Inventory 

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

 Next-Gen Trust Security 

 Getting Started 

 Certificate Management 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

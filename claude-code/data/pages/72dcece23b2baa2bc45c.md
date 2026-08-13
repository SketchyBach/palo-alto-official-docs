---
url: https://docs.paloaltonetworks.com/next-gen-trust-security/next-gen-trust-security/about-vaas/csm-introduction/csm-setup-overview/csm-certificate-authority
fetched_at: 2026-08-13T16:39:00Z
source: palo-alto-main
---

# Configure a Certificate Authority (Optional) Clear

Configure a Certificate Authority (Optional) 

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

 Configure a Certificate Authority (Optional) 

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

 Introduction to the Code Signing Capability 

 Configuring the Code Signing Capability 

 Configure a Certificate Authority (Optional) 

 Next‑Gen Trust Security 

 Configure a Certificate Authority (Optional) 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Next-Gen Trust Security Docs 

 Getting Started 

 Previous 

 Onboard Users 

 Next 

 Create a Signing Key 

 Configure a Certificate Authority (Optional) 

 If you want Next-Gen Trust Security to issue a code signing certificate along with the key, you will need to select a certificate authority (CA) when creating the Signing Key. Some CAs require no setup, while others require configuration before they can be used: 

 None -- creates only a key pair with no certificate 

 Built-in CA -- requires no configuration and is suitable for internal trust use cases, such as development builds. Certificates issued by the Built-in CA are not implicitly trusted by browsers or operating systems. 

 Microsoft AD CS, DigiCert, and Zero Touch PKI -- require certificate authority connectors to be configured before use 

 Notes : 

 If you plan to obtain a certificate from a public certificate authority, you must select AWS KMS as the key storage type when creating the Signing Key. Public CAs will not sign a CSR for a key that is not stored on a hardware HSM. 

 Certificate authority connectors must be configured in the parent TSG. Once configured, the CA is available for selection when creating a Signing Key in any child TSG. 

 While Next-Gen Trust Security supports additional certificate authorities for issuing TLS certificates, only the CAs listed above are supported for issuing code signing certificates through the code signing capability. 

 For details about setting up certificate authority connectors, see the CA configuration documentation . 

 What's Next 

 After configuring a certificate authority (if needed), continue with Create a Signing Key . 

 Related Links 

 CA configuration 

 Built-in CA 

 Microsoft AD CS 

 DigiCert 

 Zero Touch PKI 

 Previous 

 Onboard Users 

 Next 

 Create a Signing Key 

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

---
url: https://docs.paloaltonetworks.com/next-gen-trust-security/next-gen-trust-security/about-vaas/co-overview-issuing-certs/distributed-issuer-overview/add-configurations
fetched_at: 2026-08-13T16:38:56Z
source: palo-alto-main
---

# Add Configurations Clear

Add Configurations 

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

 Add Configurations 

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

 Distributed Issuer Overview 

 Add Configurations 

 Next‑Gen Trust Security 

 Add Configurations 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Next-Gen Trust Security Docs 

 Getting Started 

 Previous 

 Save Installation Credentials 

 Next 

 Network Clients with JWT 

 Add Configurations 

 Configurations are runtime settings that define how Distributed Issuer operates through a bootstrap performed at startup. They link a sub CA provider, policies, and client configurations that define which clients can interact with Distributed Issuer and how they authenticate. 

 Prerequisites 

 In Next-Gen Trust Security, a Superuser user role. 

 A subordinate CA provider . 

 At least one policy . 

 At least one Built-in Account . 

 Your IdP type (OIDC or JWKS) and its discovery URL or JWKS URI. 

 Note : If using a child Tenant Service Group, you can only create configurations with subordinate CA providers and policies that a parent Tenant Service Group has shared with you. 

 Step 1: Add General Settings 

 Add general configuration properties and optionally, enable logging. 

 Sign in to Next-Gen Trust Security. 

 Click Configuration > Certificate Configuration > Issuer Configurations . 

 On the Issuer Configurations page, click New . 

 Enter a configuration Name . 

 Select a Sub CA Provider . 

 Select one or more Built-in Accounts . A Built-in Account can only connect to one configuration, but a single configuration can have multiple Built-in Accounts. 

 (Optional) Under Advanced Security & Logging Settings , select Log certificate issuance information and Include raw certificate data . 

 (Optional) If you'll install Distributed Issuer using a FIPS image, select Require Issuer instances to be FIPS compliant . 

 Click Continue . 

 Step 2: Configure Client Access 

 The Client Configuration section controls how clients connect to Distributed Issuer. Select one or both network client options, or skip both for local-only access. 

 Network Clients (REST, gRPC, Remote cert-manager) 

 Select this option to allow clients to connect using JSON Web Token (JWT) authentication. See Network Clients with JWT to finish the configuration. 

 Network Clients Authenticated with Instance Metadata 

 Select this option to allow cloud VM instances to authenticate with signed identity documents. See Network Clients with Instance Metadata to finish the configuration. 

 Local-only Access 

 If you select neither network client option, local access via Unix Domain Sockets (UDS) is always available. With this setup, cert-manager must be installed in the same environment. 

 Do the following to finish the configuration. 

 Under Policies , select the Allowed Policies that clients can use. 

 Click Create to save the configuration. 

 What's Next? 

 Once the configuration is complete, it's time to install Distributed Issuer. Installation is CLI-based and requires access to your Kubernetes cluster or Linux host. 

 For more information, see Installation Overview on the NGTS developer documentation site. 

 Previous 

 Save Installation Credentials 

 Next 

 Network Clients with JWT 

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

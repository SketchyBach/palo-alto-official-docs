---
url: https://docs.paloaltonetworks.com/next-gen-trust-security/next-gen-trust-security/about-vaas/about-built-in-accounts/t-built-in-accounts-create-scanafi
fetched_at: 2026-08-13T16:38:36Z
source: palo-alto-main
---

# Create a Scanafi Built-in Account Clear

Create a Scanafi Built-in Account 

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

 Create a Scanafi Built-in Account 

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

 Built-in Accounts Overview 

 Create a Scanafi Built-in Account 

 Next‑Gen Trust Security 

 Create a Scanafi Built-in Account 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Next-Gen Trust Security Docs 

 Getting Started 

 Previous 

 Scopes and Built-in Account Permissions 

 Next 

 Toggling a Built-in Account On or Off 

 Create a Scanafi Built-in Account 

 Scanafi built-in accounts use a private key and Client ID for authentication. 

 For more information about downloading and installing the Scanafi utility, refer to Downloading and Installing Scanafi . 

 Before You Begin 

 Before creating a Scanafi built-in account, you must complete the following tasks: 

 By completing these prerequisites, you ensure that your built-in accounts are configured correctly and ready to handle authentication requests using modern security protocols. 

 To Create a Scanafi Built-in Account 

 Sign in to Next-Gen Trust Security. 

 Click System Settings > Certificate Settings > Built-in Accounts . 

 Click New . 

 Choose the desired use case from the Use case list, and click Continue . The use cases available for you to choose depend on which Next-Gen Trust Security components you have licenses for. 

 Enter a Name for your new built-in account. 

 (Conditional) Enter the number of days for which you want the account to remain valid in the Validity (days) field. You can select any number from 1 to 365 days. This step doesn't apply when creating a Custom API Integration built-in account. 

 Select a Key pair authentication method. 

 Note: 

 Selecting Key pair - Auto-generate a keypair and download the private key requires you to copy the public and private key values used for authentication. 

 Selecting Key pair - Generate your own keypair and upload the public key requires you to provide your own the public key in PEM format for authentication. 

 Select the desired Scope , making sure it matches the permissions and access requirements of your built-in account, and then click Continue . Learn more 

 (Conditional) After selecting a key pair authentication method and scope options, click Create or Continue . 

 (Conditional) If you previously selected Key pair - Auto-generate a keypair and download the private key , copy the public and private key values used for authentication. 

 (Conditional) If you previously selected Key pair - Generate your own keypair and upload the public key enter your public key in PEM format for authentication. 

 After entering all the details, review the information to ensure it's correct and then click Finish to create the new built-in account. 

 Related Links 

 Toggling Built-in Accounts on or Off 

 Editing Built-in Account Settings 

 Deleting Built-in Accounts 

 Overview of Built-in Accounts 

 Downloading and Installing Scanafi 

 API Reference 

 Reference: Service Account API endpoint 

 Reference: creating built-in accounts 

 Previous 

 Scopes and Built-in Account Permissions 

 Next 

 Toggling a Built-in Account On or Off 

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

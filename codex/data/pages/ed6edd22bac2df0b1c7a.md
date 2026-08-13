---
url: https://docs.paloaltonetworks.com/next-gen-trust-security/next-gen-trust-security/about-vaas/notification-center-cco/t-notification-branding
fetched_at: 2026-08-13T16:39:13Z
source: palo-alto-main
---

# Configure Notification Branding Settings Clear

Configure Notification Branding Settings 

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

 Configure Notification Branding Settings 

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

 Notification Rules Overview 

 Configure Notification Branding Settings 

 Next‑Gen Trust Security 

 Configure Notification Branding Settings 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Next-Gen Trust Security Docs 

 Getting Started 

 Previous 

 Advanced Filter Criteria 

 Next 

 Create Notification Templates 

 Configure Notification Branding Settings 

 Use the notification branding page to customize the branding that appears in emails sent by Reports and Notification Rules. Apply your organization's logo, header, footer, and call-to-action (CTA) text consistently across those messages. 

 You can configure any combination of logo, header, footer, and call-to-action. CTA Text requires a CTA Link. If you provide a CTA Link without CTA Text, the link appears as a full URL. 

 To Configure Branding Settings 

 Sign in to Next-Gen Trust Security. 

 Click Configuration > Certificate Notifications > Notification Branding . 

 In the Upload Logo field, enter the URL of the branding image you want to include in notifications. 

 This image isn't stored on CyberArk servers, so ensure the URL is publicly accessible. Images should be at least 75 px tall, with a recommended 2:1 aspect ratio (twice as wide as tall). 

 If you don't specify a value, the CyberArk logo will be used. 

 In Header Text , enter the text you want to appear before the notification content. 

 In Footer Text ,enter the text you want to appear after the notification content. 

 In Footer Call To Action (CTA) Text , enter the display text for a link displayed after the Footer Text. 

 If you specify a CTA Text value, the CTA Link field becomes required. 

 In Footer Call To Action (CTA) Link , enter the URL destination for the link displayed below the footer. 

 If you provide a CTA link without CTA text, the bare URL is shown in the notification. 

 Click Save . 

 To Test Notification Branding 

 Click Send Test Email . 

 A test email is sent to the email address associated with your account. The message is from notification@venafi.cloud . 

 Fields at a Glance 

 Use the table below to review the available Notification Branding fields. 

 Field Description Notes 

 Logo Link URL of the branding image shown at the top of emails. - Must be publicly accessible (not stored on CyberArk servers).- Recommended size: ≥75 px tall, 2:1 aspect ratio.- If not set, the CyberArk logo is used. 

 Header Text Text shown above the notification content. Optional. Keep it short (org name, tagline, etc.). 

 Footer Text Text shown below the notification content. Optional. Often used for disclaimers or copyright. 

 Footer Call To Action (CTA) Text Display text for a clickable link under the footer. Optional. Requires a CTA Link . 

 Footer Call To Action (CTA) Link URL opened when the CTA is clicked. - Required if CTA Text is set.- If provided without CTA Text, the bare URL is displayed. 

 Previous 

 Advanced Filter Criteria 

 Next 

 Create Notification Templates 

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

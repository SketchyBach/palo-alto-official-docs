---
url: https://docs.paloaltonetworks.com/cloud-ngfw-azure/administration/protect-traffic-with-cloud-ngfw-for-azure/cloud-ngfw-for-azure-panorama-integration/configure-advanced-dns-security-in-panorama
fetched_at: 2026-08-13T15:31:08Z
source: palo-alto-main
---

# Configure Advanced DNS Security in Panorama Clear

Configure Advanced DNS Security in Panorama 

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

 Configure Advanced DNS Security in Panorama 

 Updated on 

 Jun 29, 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Cloud NGFW for Azure Docs 

 Getting Started 

 Deployment 

 Administration 

 Reference 

 Release Notes 

 New Features 

 Updated on 

 Jun 29, 2026 

 Focus 

 Home 

 Cloud NGFW for Azure Administration 

 Protect Traffic with Cloud NGFW for Azure 

 Panorama Policy Management 

 Configure Advanced DNS Security in Panorama 

 Download PDF 

 Cloud NGFW for Azure 

 Configure Advanced DNS Security in Panorama 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Cloud NGFW for Azure Docs 

 Getting Started 

 Deployment 

 Administration 

 Reference 

 Release Notes 

 New Features 

 Previous 

 Configure WildFire Protection 

 Next 

 Configure Enterprise DLP for Cloud NGFW on Azure 

 Configure Advanced DNS Security in Panorama 

 Cloud NGFW for Azure leverages Advanced DNS Security to provide real-time, AI-driven
 protection against sophisticated DNS-layer threats. 

 Cloud NGFW for Azure leverages Advanced DNS Security to provide real-time, AI-driven
 protection against sophisticated DNS-layer threats. The Advanced tier uses
 cloud-based deep learning to block zero-day malicious domains. 

 Enable DNS Proxy in the Azure
 Portal . 

 Define Advanced DNS Categories in Panorama. 

 Advanced DNS Security is managed through the Anti-Spyware profile in your
 Panorama-managed device groups. 

 In Panorama , navigate to Objects > Security
 Profiles > Anti-Spyware . 

 Select the Device Group associated with your Cloud
 NGFW for Azure. 

 Click Add (or edit your existing profile) and go to the DNS
 Policies tab. 

 Select required log level for the respective ADNS. 

 Select the required action for the respective ADNS (applicable to
 PAN-OS version 11.2.7 and above only). 

 Click OK . 

 When you select the default options for your Newly Registered
 Domains , the Cloud NGFW automatically utilizes the Advanced DNS
 Security engine. 

 Deploy the Configuration. 

 Go to Policies > Security and ensure the
 Anti-Spyware profile is attached to your outbound security
 rules. 

 Commit the changes to Panorama. 

 Push the configuration to your Cloud NGFW for Azure
 device group. 

 Billing and Credits. 

 Once an Anti-Spyware profile with Advanced DNS categories is
 applied to a live Security Policy: 

 The service is active and billed as an add-on. 

 This appears in your Azure consumption as a credit
 surcharge (approximately 30% of the base firewall credit
 cost ). 

 For more information, see Configuring Anti Spyware profile on
 Panorama . 

 Previous 

 Configure WildFire Protection 

 Next 

 Configure Enterprise DLP for Cloud NGFW on Azure 

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

 Administration 

 Cloud NGFW for Azure 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

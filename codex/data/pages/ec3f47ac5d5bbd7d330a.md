---
url: https://docs.paloaltonetworks.com/dns-security/activation-and-onboarding/activate-advanced-dns-security
fetched_at: 2026-08-13T15:31:49Z
source: palo-alto-main
---

# Activate Advanced DNS Security Clear

Activate Advanced DNS Security 

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

 Activate Advanced DNS Security 

 Updated on 

 Fri Jun 26 16:51:14 PDT 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Advanced DNS Security 

 Activation & Onboarding 

 Getting Started 

 Administration 

 Release Notes 

 Updated on 

 Fri Jun 26 16:51:14 PDT 2026 

 Focus 

 Home 

 Advanced DNS Security Powered by Precision AI® 

 Activate Advanced DNS Security 

 Download PDF 

 Advanced DNS Security Powered by Precision AI® 

 Activate Advanced DNS Security 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Advanced DNS Security 

 Activation & Onboarding 

 Getting Started 

 Administration 

 Release Notes 

 Previous 

 Advanced DNS Security Prerequisites 

 Next 

 Enable DNS Security 

 Activate Advanced DNS Security 

 Activate your DNS Security and Advanced DNS Security licenses. 

 Where Can I Use
 This? What Do I Need? 

 Prisma Access 

 NGFW 

 VM-Series 

 CN-Series 

 A Palo Alto Networks 
 DNS Security subscription; this can include: 

 Advanced DNS Security Resolver License 

 Advanced DNS Security License (for enhanced feature
 support) 

 DNS Security License 

 The Advanced DNS Security and DNS Security licenses also
 require the installation of: 

 Advanced Threat Prevention License 

 Threat Prevention License 

 You must activate your DNS Security or Advanced DNS Security subscription to
 enable your organization to identify and block sophisticated DNS-layer threats, such as
 DNS tunneling, DGA-based malware, and malicious domains. Activation for these integrated
 subscriptions is performed by applying the authorization codes to your NGFW . These procedures assume you already have all the required license auth codes
 necessary for activation. 

 If your subscription was purchased as part of a Prisma Access bundle, the Advanced DNS Security features are automatically included. In these cases, no separate
 activation action is required for the Advanced DNS Security component after you activate
 the primary bundle license, as is typical for Prisma Access 

 You must install the device certificate on your NGFW 
 before you can activate your Advanced DNS Security license. Palo Alto Networks uses the
 device certificate to authentication the NGFW and Prisma Access to
 allow them to connect to the Advanced DNS Security 
 cloud service . Palo Alto Networks requires
 the device certificate to use any Palo Alto Networks cloud service. 

 Palo Alto Networks begins enforcement of device certificate authentication for Advanced DNS Security on February 11, 2026. 

 If you have NGFW with an active Advanced DNS Security license, you must
 install the device certificate on your NGFW by March 13 2026 (30
 days). 

 After this date, your NGFW will no longer be able to connect to the
 Advanced DNS Security cloud service. 

 Standalone NGFW and NGFW (Managed by Strata Cloud Manager) — Install the device certificate on
 every NGFW access the Advanced DNS Security service. 

 NGFW (Managed by Panorama) — Install the device certificate for
 multiple NGFW from your Panorama® management server . 

 Prisma Access (Managed by Panorama or Strata Cloud Manager) —Device certificate installed by default. No
 action required. 

 After you install the device certificate on your NGFW ,
 you can continue to activate the Advanced DNS Security license: 

 NGFW — The base DNS Security and Advanced DNS Security 
 subscriptions are activated similarly on NGFW to other cloud
 service subscriptions. Refer to Activate Subscription Licenses 
 for more information. 

 Prisma Access — Prisma Access typically includes cloud service
 subscription-based features as part of a bundle solution. As a result, these
 subscriptions are automatically enabled when you activate your Prisma Access 
 license. 

 For more information on activating Prisma Access , refer to: Activate Your Prisma Access
 License. 

 Previous 

 Advanced DNS Security Prerequisites 

 Next 

 Enable DNS Security 

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

 Endpoints 

 GlobalProtect 

 Visibility & Monitoring 

 Dashboards 

 Incidents and Alerts 

 Reports 

 Autonomous DEM 

 Best Practices 

 Best Practices Library 

 Advanced DNS Security 

 Activation & Onboarding 

 Cloud-Delivered Security Services 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

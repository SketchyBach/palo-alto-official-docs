---
url: https://docs.paloaltonetworks.com/enterprise-dlp/activation-and-onboarding/activate-endpoint-dlp
fetched_at: 2026-08-13T15:32:06Z
source: palo-alto-main
---

# Activate Endpoint DLP Clear

Activate Endpoint DLP 

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

 Activate Endpoint DLP 

 Updated on 

 Fri Jul 31 14:12:32 PDT 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Enterprise DLP Docs 

 Activation & Onboarding 

 Getting Started 

 Administration 

 Reference 

 Release Notes 

 New Features by OS Version 

 New Features by Month 

 Updated on 

 Fri Jul 31 14:12:32 PDT 2026 

 Focus 

 Home 

 Enterprise DLP 

 Activation & Onboarding 

 Activate Endpoint DLP 

 Download PDF 

 Enterprise DLP 

 Activate Endpoint DLP 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Enterprise DLP Docs 

 Activation & Onboarding 

 Getting Started 

 Administration 

 Reference 

 Release Notes 

 New Features by OS Version 

 New Features by Month 

 Previous 

 Activate Email DLP 

 Next 

 Enable Optical Character Recognition 

 Activate Endpoint DLP 

 Activate Endpoint DLP to stop accidental or malicious data lose over peripheral
 devices. 

 On May 7, 2025 , Palo Alto Networks is introducing new Evidence Storage and Syslog Forwarding service IP
 addresses to improve performance and expand availability for these services
 globally. 

 You must allow these new service IP addresses on your network
 to avoid disruptions for these services. Review the Enterprise DLP 
 Release Notes for more
 information. 

 Where Can I Use This? What Do I Need? 

 NGFW (Managed by Strata Cloud Manager) 

 Prisma Access (Managed by Strata Cloud Manager) 

 Endpoint DLP license 

 Autonomous DEM (6.0.21 or later for End User Coaching) 

 Prisma Agent 

 Prisma Access 5.1 (Preferred or Innovation) or later 

 Activate Endpoint DLP for single tenant or multitenant Customer Support Portal (CSP)
 account to prevent exfiltration of sensitive data to peripheral devices such as USB
 devices, printers, and network shares, or to control access to them. Before you
 active the Endpoint DLP license, you must enable set up the Prisma Agent configuration file to enable the Endpoint DLP functionality and then install the
 Prisma Agent on all endpoints you want to protect. 

 Activating the Endpoint DLP license gives you access to Enterprise Data Loss Prevention (E-DLP) 
 advanced detection methods , data patterns , and data profiles . 

 For production Prisma Agent and Endpoint DLP deployments, Palo Alto Networks requires mobile device management (MDM) deployment to install
 Prisma Agent on endpoints to enable Endpoint DLP. This is required
 because: 

 When transitioning from GlobalProtect to Prisma Agent , the endpoint doesn't support granting required manual extension access
 if you previously installed GlobalProtect using MDM
 deployment. 

 Successfully setting up Prisma Agent for Endpoint DLP requires
 many different settings and configurations. Palo Alto Networks requires MDM
 deployment of Prisma Agent to reduce the chance of
 misconfiguration on multiple endpoints and increase the chance of a
 successful deployment. 

 Endpoint DLP doesn't support GlobalProtect . You must install Prisma Agent to use Endpoint DLP. 

 Single Tenant 

 Multitenant 

 Single Tenant 

 Activate Endpoint DLP to prevent exfiltration of sensitive data over peripheral
 devices for a single tenant Customer Support Portal account. 

 Contact your Palo Alto Networks representative to purchase the Endpoint DLP
 subscription. 

 Click the magic link provided to you by Palo Alto Networks when you purchased
 the Endpoint DLP subscription. 

 Activate Subscription to begin activating Endpoint
 DLP. 

 Enter your Email Address and click
 Next to continue. 

 This email address must match the email that received the magic link to
 activate Endpoint DLP and must have a valid Palo Alto Networks Customer
 Support Portal account. 

 Click Create a New Account if you're a security
 administrator who does not yet have a valid Palo Alto Networks Customer
 Support Portal account for your organization. This is required before you
 can continue activating Endpoint DLP. 

 Verify the tenant details for which you're activating Endpoint DLP. 

 This information is populated by default when the magic link is generated.
 Palo Alto Networks recommends verifying the following tenant details
 before activation to resolve any issues before activation. 

 Customer Support Account —Endpoint DLP must be
 activate on the same Customer Support Portal account as Enterprise DLP . 

 Region —Region is populated by default and is
 based on the region configured for the Customer Support Portal
 tenant. This can’t be changed. 

 Endpoint DLP Licenses —Endpoint DLP license
 must be Fully Assigned and display the total
 number of supported users. 

 Agree to the Terms and Conditions . 

 Activate Now . 

 Set up Prisma Agent and install it on your endpoints. 

 ( Manual Install for Trials and Evaluations ) Palo Alto Networks 
 supports manual Prisma Agent installs only for trials and
 evaluations. Your security administrators might not use an MDM to
 install Prisma Agent or a configuration profile to enable
 Endpoint DLP. In this case, after you install Prisma Agent 
 on the endpoint, Prisma Agent prompts the end user to
 Open System Settings and enable the following
 two extensions: 

 PASrv 

 Enforcer 

 The end user must enable these to extensions on Prisma Agent 
 to use Endpoint DLP when installing Prisma Agent without
 using a configuration profile to manage the Endpoint DLP
 configuration. 

 Ensure your network allows access to
 pool.ntp.org . 

 Prisma Agent requests NTP timestamps from
 pool.ntp.org to ensure endpoints
 are not affected by any system time change by the end user. 

 If Prisma Agent can't request NTP timestamps, it
 experiences communication issues with Enterprise DLP and the
 file explorer on the endpoint device may become unresponsive when
 moving files from one folder to another if the file movement matches
 the data-in-motion Endpoint DLP policy
 rule . 

 ( SSL Decryption ) If you configured SSL decryption for Prisma Access , you must add the following decryption exclusion entry for
 Enterprise DLP . 

 *.dss.paloaltonetworks.com 

 Download the Prisma Agent package. 

 You must first download the Prisma Agent from Strata Cloud Manager so that you can deploy it to your mobile
 users' endpoints using third-party mobile device management (MDM)
 software. 

 Skip this step if you already uploaded the Prisma Agent 
 package to your MDM. 

 Upload the Prisma Agent package to your MDM and install
 Prisma Agent all endpoints you want to protect. 

 You must use one of the supported mobile device management (MDM)
 installation methods if the endpoint currently has GlobalProtect or Cortex XDR installed. Prisma Agent does not support manual installation if
 GlobalProtect or Cortex XDR are
 already installed on the endpoint. 

 Microsoft
 Windows 

 macOS 

 Allow the Prisma Agent processes for your Endpoint Detection and
 Response (EDR) tools. 
 At a minimum, you must allow all DLP 
 (Microsoft Windows) or pangdlp (macOS)
 Endpoint DLP processes. 

 However, Palo Alto Networks recommends allowing all Prisma Agent processes to prevent your EDR tools from
 flagging Endpoint DLP and other Prisma Agent processes as
 malicious. Not allowing these processes might result in unexpected
 behavior and might prevent Endpoint DLP functionality. 

 Set up Endpoint DLP. 

 Edit the Endpoint DLP data filtering settings and
 snippet settings to define the
 operational parameters. 

 Enable Optical Character Recognition 
 on Strata Cloud Manager to scan files with images containing sensitive
 information. 

 Create an Endpoint DLP policy
 rule to control access to peripheral devices and prevent
 exfiltration of sensitive data. 
 The Prisma Agent displays the Endpoint DLP service as
 disabled until you push an Endpoint DLP
 policy rule from Strata Cloud Manager to the Prisma Agent 
 installed on the endpoint. 

 ( Optional ) Save evidence for investigative
 analysis with Enterprise DLP to connect an AWS storage
 bucket, Azure storage bucket, or SFTP server to Enterprise DLP to
 automatically store evidence of inspected traffic. 

 ( Optional ) Add peripheral devices to
 Endpoint DLP. 

 ( Optional ) Create a peripheral group to
 group similar types of peripheral devices together for easier
 application of Endpoint DLP policy rules. 

 ( Optional ) Create a User Coaching Notification
 Template for Endpoint DLP. 

 The End User Coaching Notification Template allows you to configure
 the notification displayed to your users in the Access Experience User
 Interface (UI) when they generate a DLP incident . 

 For the Product Name , select
 Endpoint Data Loss Prevention . Configure
 the Applied Rules and Notification
 Message as needed. 

 Multitenant 

 Activate Endpoint DLP to prevent exfiltration of sensitive data over peripheral
 devices for a multitenant Customer Support Portal (CSP) account. 

 Contact your Palo Alto Networks representative to purchase the Endpoint DLP
 subscription. 

 Click the magic link provided to you by Palo Alto Networks when you purchased
 the Endpoint DLP subscription. 

 Activate Subscription to begin activating Endpoint
 DLP. 

 Enter your Email Address and click
 Next to continue. 

 This email address must match the email that received the magic link to
 activate Endpoint DLP and must have a valid Palo Alto Networks Customer
 Support Portal account. 

 Click Create a New Account if you're a security
 administrator who does not yet have a valid Palo Alto Networks Customer
 Support Portal account for your organization. This is required before you
 can continue activating Endpoint DLP. 

 Verify you're activating Endpoint DLP for the correct Customer
 Support Portal account. 

 In Specify the Tenant , select the child tenant for
 which you want to activate Endpoint DLP. 

 Enterprise DLP must be active on the tenant for which you activating
 Endpoint DLP. 

 Click Done to continue. 

 Verify the tenant details for which you're activating Endpoint DLP. 

 Region —Region is populated by default and is
 based on the child tenant you selected in the previous step. This
 can’t be changed. 

 Endpoint DLP Licenses —Endpoint DLP license
 must be Fully Assigned and display the total
 number of supported users. 

 For the Cloud Identity Engine , select the CIE instance
 associated with your Customer Support Portal account and click
 Done . 

 Agree to the Terms and Conditions . 

 Activate Now . 

 Set up Prisma Agent and install it on your endpoints. 

 ( Manual Install for Trials and Evaluations ) Palo Alto Networks 
 supports manual Prisma Agent installs only for trials and
 evaluations. Your security administrators might not use an MDM to
 install Prisma Agent or a configuration profile to enable
 Endpoint DLP. In this case, after you install Prisma Agent 
 on the endpoint, Prisma Agent prompts the end user to
 Open System Settings and enable the following
 two extensions: 

 PASrv 

 Enforcer 

 The end user must enable these to extensions on Prisma Agent 
 to use Endpoint DLP when installing Prisma Agent without
 using a configuration profile to manage the Endpoint DLP
 configuration. 

 Ensure your network allows access to
 pool.ntp.org . 

 Prisma Agent requests NTP timestamps from
 pool.ntp.org to ensure endpoints
 are not affected by any system time change by the end user. 

 If Prisma Agent can't request NTP timestamps, it
 experiences communication issues with Enterprise DLP and the
 file explorer on the endpoint device may become unresponsive when
 moving files from one folder to another if the file movement matches
 the data-in-motion Endpoint DLP policy
 rule . 

 ( SSL Decryption ) If you configured SSL decryption for Prisma Access , you must add the following decryption exclusion entry for
 Enterprise DLP . 

 *.dss.paloaltonetworks.com 

 Download the Prisma Agent package. 

 You must first download the Prisma Agent from Strata Cloud Manager so that you can deploy it to your mobile
 users' endpoints using third-party mobile device management (MDM)
 software. 

 Skip this step if you already uploaded the Prisma Agent 
 package to your MDM. 

 Upload the Prisma Agent package to your MDM and install
 Prisma Agent all endpoints you want to protect. 

 You must use one of the supported mobile device management (MDM)
 installation methods if the endpoint currently has GlobalProtect or Cortex XDR installed. Prisma Agent does not support manual installation if
 GlobalProtect or Cortex XDR are
 already installed on the endpoint. 

 Microsoft
 Windows 

 macOS 

 Allow the Prisma Agent processes for your Endpoint Detection and
 Response (EDR) tools. 
 At a minimum, you must allow all DLP 
 (Microsoft Windows) or pangdlp (macOS)
 Endpoint DLP processes. 

 However, Palo Alto Networks recommends allowing all Prisma Agent processes to prevent your EDR tools from
 flagging Endpoint DLP and other Prisma Agent processes as
 malicious. Not allowing these processes might result in unexpected
 behavior and might prevent Endpoint DLP functionality. 

 Set up Endpoint DLP. 

 Edit the Endpoint DLP data filtering settings and
 snippet settings to define the
 operational parameters. 

 Enable Optical Character Recognition 
 on Strata Cloud Manager to scan files with images containing sensitive
 information. 

 Create an Endpoint DLP policy
 rule to control access to peripheral devices and prevent
 exfiltration of sensitive data. 
 The Prisma Agent displays the Endpoint DLP service as
 disabled until you push an Endpoint DLP
 policy rule from Strata Cloud Manager to the Prisma Agent 
 installed on the endpoint. 

 ( Optional ) Save evidence for investigative
 analysis with Enterprise DLP to connect an AWS storage
 bucket, Azure storage bucket, or SFTP server to Enterprise DLP to
 automatically store evidence of inspected traffic. 

 ( Optional ) Add peripheral devices to
 Endpoint DLP. 

 ( Optional ) Create a peripheral group to
 group similar types of peripheral devices together for easier
 application of Endpoint DLP policy rules. 

 ( Optional ) Create a User Coaching Notification
 Template for Endpoint DLP. 

 The End User Coaching Notification Template allows you to configure
 the notification displayed to your users in the Access Experience User
 Interface (UI) when they generate a DLP incident . 

 For the Product Name , select
 Endpoint Data Loss Prevention . Configure
 the Applied Rules and Notification
 Message as needed. 

 Previous 

 Activate Email DLP 

 Next 

 Enable Optical Character Recognition 

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

 SaaS Security 

 Endpoints 

 GlobalProtect 

 Visibility & Monitoring 

 Dashboards 

 Incidents and Alerts 

 Reports 

 Autonomous DEM 

 Best Practices 

 Best Practices Library 

 Experts Corner 

 Solutions Docs from Product Experts 

 Activation & Onboarding 

 Cloud-Delivered Security Services 

 Data Filtering 

 Enterprise DLP 

 Task 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

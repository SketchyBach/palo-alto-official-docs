---
url: https://docs.paloaltonetworks.com/enterprise-dlp/activation-and-onboarding/activate-the-enterprise-dlp-license
fetched_at: 2026-08-13T15:32:06Z
source: palo-alto-main
---

# Activate the Enterprise DLP License Clear

Activate the Enterprise DLP License 

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

 Activate the Enterprise DLP License 

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

 Activate the Enterprise DLP License 

 Download PDF 

 Enterprise DLP 

 Activate the Enterprise DLP License 

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

 Activate Next-Generation CASB for Prisma Access and NGFW (CASB-X) 

 Next 

 Install the Enterprise DLP Plugin on Panorama 

 Activate the Enterprise DLP License 

 Activate the Enterprise Data Loss Prevention (E-DLP) license for your NGFW , Prisma Access tenants, and VM-Series, funded with Software NGFW Credits . 

 On May 7, 2025 , Palo Alto Networks is introducing new Evidence Storage and Syslog Forwarding service IP
 addresses to improve performance and expand availability for these services
 globally. 

 You must allow these new service IP addresses on your network
 to avoid disruptions for these services. Review the Enterprise DLP 
 Release Notes for more
 information. 

 Where Can I Use This? What Do I Need? 

 NGFW (Managed by Panorama or Strata Cloud Manager) 

 Prisma Access (Managed by Panorama or Strata Cloud Manager) 

 Enterprise Data Loss Prevention (E-DLP) license 

 Review the Supported
 Platforms for details on the required license
 for each enforcement point. 

 And one of the following licenses: 

 ( Strata Cloud Manager ) Strata Cloud Manager Essentials license 

 ( Panorama ) Support and device management
 license 

 Activate the Enterprise Data Loss Prevention (E-DLP) license using a magic link provided by Palo Alto Networks for a single tenant and multitenant Customer Support Portal
 account. The Enterprise DLP license activation procedure varies depending on
 the enforcement point and type of license you're activating. 

 NGFW —Activate the standalone Enterprise DLP 
 license. After activating the Enterprise DLP license, you need to
 associate the Enterprise DLP service with your NGFW .
 For Panorama -managed deployments, you must also associate Panorama with the same tenant service group (TSG) using Device
 Associations in Strata Cloud Manager before installing the Enterprise DLP plugin. 

 Prisma Access —Enable the Enterprise DLP add-on after
 activating your Prisma Access license. For Panorama -managed
 deployments, you must also associate Panorama with the same TSG
 before installing the Enterprise DLP plugin. 

 VM-Series Firewalls —Create or edit a deployment
 profile. Activating the deployment profile automatically activates the Enterprise DLP license. After activating the Enterprise DLP 
 license, you need to associate the Enterprise DLP service with your VM-Series firewalls. 

 CASB-X and CASB-PA Licenses —The CASB-X and CASB-PA licenses include Enterprise DLP and don't require you to separately activate the Enterprise DLP license. After activating either of these licenses, you
 need to associate the Enterprise DLP service with your NGFW , Prisma Access , and VM-Series 
 firewalls. 

 NGFW 

 Prisma Access 

 VM-Series, funded with NGFW Software
 Credits 

 Activate the Enterprise DLP License for NGFW 

 Activate the Enterprise Data Loss Prevention (E-DLP) license for your NGFW (Managed by Panorama or Strata Cloud Manager) . 

 Contact your Palo Alto Networks representative to purchase the Enterprise DLP subscription. 

 Click the magic link provided to you by Palo Alto Networks when you purchased
 the Enterprise DLP subscription. 

 Activate Subscription to begin activating Enterprise DLP . 

 Enter your Email Address and click
 Next to continue. 

 This email address must match the email that received the magic link to
 activate Enterprise DLP and must have a valid Palo Alto Networks 
 Customer Support Portal account. 

 Click Create a New Account if you're a security
 administrator who does not yet have a valid Palo Alto Networks Customer
 Support Portal account for your organization. This is required before you
 can continue activating Enterprise DLP . 

 Select the Customer Support Account for which
 you're activating Enterprise DLP . 

 Palo Alto Networks automatically populates the list of available Customer
 Support Portal accounts when the Palo Alto Networks representative
 generates the magic link. Palo Alto Networks recommends verifying you're
 activating Enterprise DLP for your Customer Support Portal account
 before you continue. 

 For the Specify the Recipient field, select the
 Tenant for which you want to activate Enterprise DLP . 

 You can select only one tenant for which to activate Enterprise DLP . You
 can’t activate Enterprise DLP for multiple tenants using the same magic
 link. If you have a multitenant tenant service group 
 (TSG), expand the parent tenant to select the child tenant. 

 Verify that the correct Region is selected. 

 Global —Default for all non-FedRAMP Customer Support Accounts
 and can't be modified. 

 All Enterprise DLP tenants are globally available by default.
 However, your Enterprise DLP data and incidents reside in
 geographic locations based on where the enforcement point that
 forwarded the traffic to Enterprise DLP was located. 

 Alternatively on Panorama , you can configure a specific
 Public Cloud Server so
 your Panorama -managed enforcement point forward traffic to
 a region-specific Enterprise DLP tenant. 

 ( FedRAMP only ) United States - Government —Default for
 all FedRAMP Moderate and High Customer Support Accounts and can't be
 modified. 

 For the Data Loss Prevention tenant, select
 None . 

 Selecting None creates a new Enterprise DLP 
 tenant. If you already activated a trial or EVAL license, you must
 create a new production Enterprise DLP . 

 Check Agree to the Terms and Conditions and
 Activate . 

 Log in to 
 Strata Cloud Manager and verify that you can select Configuration Data Loss Prevention . 

 ( Non-TSG Aware CSP Accounts ) Gather the list of the enforcement points
 that already have an active Enterprise DLP license. 

 This is required if you have a non-TSG aware Customer Support Account that
 hasn't been migrated and you already activated and associated the Enterprise DLP license with existing enforcement points to avoid
 activation failure. 

 Skip this step if activating the Enterprise DLP for the first time or
 have a TSG aware Customer Support Portal account. 

 Log in to the Palo Alto Networks 
 Customer Support Portal . 

 Select Product Assets and Add New Filter . 

 Click Select Filter and select
 DLP . 

 Note the list of enforcement points with an active Enterprise DLP license and their serial numbers. 

 The Customer Support Portal displays all enforcement
 points with an active Enterprise DLP license. Use this list of enforcement point serial numbers when selecting NGFW with which to associate the Enterprise DLP 
 license. 

 Associate your Panorama and NGFW with the tenant
 service group (TSG) in which you activated Enterprise DLP . 

 Your Panorama and NGFW must belong to the same TSG.
 This enables Panorama to synchronize Enterprise DLP 
 configuration changes with Strata Cloud Manager and push them to your
 managed NGFW . 

 Use Device Associations in Strata Cloud Manager to add your Panorama and NGFW 
 to the TSG. 

 Associate Enterprise DLP with your NGFW . 

 Select System Settings Device Association . 

 Select the tenant for which you activated Enterprise DLP . 

 Select one or more NGFW and Associate
 Products . 

 TSG Aware Customer Support Account — Strata Cloud Manager displays only the NGFW without an active
 Enterprise DLP license. 

 Non-TSG Aware Customer Support Account —Don't select
 any NGFW with an already active Enterprise DLP license. Compare the list of available
 enforcement points with the list of enforcement points that
 have an active Enterprise DLP license you generated in
 the previous step. 

 Selecting an NGFW with an active Enterprise DLP license blocks activation. Deselect any
 NGFW with an active Enterprise DLP 
 license. 

 In the Products list, select
 Enterprise DLP . 

 Select the NGFW and click
 Save . 

 ( NGFW (Managed by Panorama) only ) Install the Enterprise DLP Plugin on Panorama . 

 If you manage NGFW from Panorama , you must install
 the Enterprise DLP plugin on Panorama to manage your Enterprise DLP configuration, synchronize Enterprise DLP 
 configuration objects with Strata Cloud Manager , and push Enterprise DLP configuration changes to your NGFW . A Panorama 
 with the Enterprise DLP plugin installed is required; Enterprise DLP doesn't support managing your Enterprise DLP configuration directly
 on your NGFW . 

 Install the Enterprise DLP plugin after you associate Enterprise DLP with your Panorama and NGFW . This ensures the plugin correctly maps to your
 TSG and prevents synchronization issues. 

 Enable Enterprise DLP . 

 Some apps, such as SharePoint and OneDrive, use HTTP/2 by default. For NGFW , Prisma Access tenants, and VM-Series 
 firewalls managed by Panorama or by Strata Cloud Manager running
 PAN-OS 10.2.2 and earlier releases, you must create a
 decryption profile and a Security policy rule to strip out the
 application-layer protocol negotiation (ALPN) extension in headers. Complete
 these steps to successfully forward traffic to Enterprise DLP . 

 Activate the Enterprise DLP License for Prisma Access 

 Activate the Enterprise Data Loss Prevention (E-DLP) license for your Prisma Access (Managed by Panorama or Strata Cloud Manager) . 

 Contact your Palo Alto Networks representative to purchase the Prisma Access and Enterprise DLP licenses. 

 Click the magic link provided to you by Palo Alto Networks when you purchased
 the Prisma Access license. 

 Activate the Prisma Access license. 

 Activate the license for
 Prisma Access (Managed by Panorama) . 

 Activate the license for
 Prisma Access (Managed by Strata Cloud Manager) . 

 Enable the Enterprise DLP add-on. 

 Prisma Access (Managed by Panorama) —The Enterprise DLP add-on is enabled
 by default when you activate the Prisma Access license. 

 Prisma Access (Managed by Strata Cloud Manager) — Enable the Enterprise DLP add-on after activating the Prisma Access 
 license. 

 Log in to 
 Strata Cloud Manager and verify that you can select Configuration Data Loss Prevention . 

 Associate your Panorama and Prisma Access tenants with the
 tenant service group (TSG) in which you activated Prisma Access and Enterprise DLP . 

 Your Panorama and Prisma Access tenants must belong to the same
 TSG. This enables Panorama to synchronize Enterprise DLP 
 configuration changes with Strata Cloud Manager and push them to your
 managed Prisma Access tenants. 

 Use Device Associations in Strata Cloud Manager to add your Panorama and Prisma Access 
 tenants to the TSG. 

 ( Prisma Access (Managed by Panorama) only ) Install the Enterprise DLP Plugin on Panorama . 

 If you manage your Prisma Access tenants from Panorama , you
 must install the Enterprise DLP plugin on Panorama to manage
 your Enterprise DLP configuration, synchronize Enterprise DLP 
 configuration objects with Strata Cloud Manager , and push Enterprise DLP configuration changes to your Prisma Access tenants.
 A Panorama with the Enterprise DLP plugin installed is
 required. 

 Install the Enterprise DLP plugin after you associate Enterprise DLP with your Panorama and NGFW . This ensures the plugin correctly maps to your
 TSG and prevents synchronization issues. 

 Enable Enterprise DLP . 

 Some apps, such as SharePoint and OneDrive, use HTTP/2 by default. For NGFW , Prisma Access tenants, and VM-Series 
 firewalls managed by Panorama or by Strata Cloud Manager running
 PAN-OS 10.2.2 and earlier releases, you must create a
 decryption profile and a Security policy rule to strip out the
 application-layer protocol negotiation (ALPN) extension in headers. Complete
 these steps to successfully forward traffic to Enterprise DLP . 

 Activate the Enterprise DLP License for VM-Series, funded with Software NGFW Credits 

 Activate the Enterprise Data Loss Prevention (E-DLP) license for VM-Series, funded with Software NGFW Credits . 

 Create a new deployment profile or edit an existing one. 

 This is required to activate the Enterprise DLP licenses for VM-Series firewalls. 

 New Deployment Profiles — Create a new deployment
 profile and check (enable) DLP in the
 Customize Subscription section. 

 Existing Deployments Profiles — Edit an existing
 deployment profile and check (enable) DLP in
 the Customize Subscription section. 

 Activate the deployment profile. 

 Select the Customer Support Account for which
 you're activating Enterprise DLP . 

 Palo Alto Networks automatically populates the list of available Customer
 Support Portal accounts when you activate a new deployment profile or are
 editing an existing one. Palo Alto Networks recommends verifying you're
 activating Enterprise DLP for your Customer Support Portal account
 before you continue. 

 Select the deployment profile Recipient and click
 Done . 

 The deployment profile must have DLP selected to
 activate Enterprise DLP . 

 Select the Region the deployment profile belongs
 to. 

 Regardless of which deployment profile region you select, the Enterprise DLP tenant belongs to one of the following regions: 

 Global —Default for all non-FedRAMP Customer Support Accounts
 and can't be modified. 

 All Enterprise DLP tenants are globally available by default.
 However, your Enterprise DLP data and incidents reside in
 geographic locations based on where the enforcement point that
 forwarded the traffic to Enterprise DLP was located. 

 Alternatively on Panorama , you can configure a specific
 Public Cloud Server so
 your Panorama -managed enforcement point forward traffic to
 a region-specific Enterprise DLP tenant. 

 ( FedRAMP only ) United States - Government —Default for
 all FedRAMP Moderate and High Customer Support Accounts and can't be
 modified. 

 For the Data Loss Prevention tenant, select
 None . 

 Selecting None creates a new Enterprise DLP 
 tenant. If you have already activated a trial or EVAL license, you must
 create a new production Enterprise DLP . 

 Check Agree to the Terms and Conditions and
 Activate . 

 Log in to 
 Strata Cloud Manager and verify that you can select Configuration Data Loss Prevention . 

 Associate your Panorama and VM-Series firewalls with
 the tenant service group (TSG) in which you activated Enterprise DLP . 

 Your Panorama and VM-Series firewalls must belong to
 the same TSG. This enables Panorama to synchronize Enterprise DLP configuration changes with Strata Cloud Manager and
 push them to your managed VM-Series firewalls. 

 Use Device Associations in Strata Cloud Manager to add your Panorama and VM-Series firewalls to the TSG. 

 ( Non-TSG Aware CSP Accounts ) Gather the list of the enforcement points
 that already have an active Enterprise DLP license. 

 This is required if you have a non-TSG aware Customer Support Account that
 hasn't been migrated and you already activated and associated the Enterprise DLP license with existing enforcement points to avoid
 activation failure. 

 Skip this step if activating the Enterprise DLP for the first time or
 have a TSG aware Customer Support Portal account. 

 Log in to the Palo Alto Networks 
 Customer Support Portal . 

 Select Product Assets and Add New Filter . 

 Click Select Filter and select
 DLP . 

 The Customer Support Portal displays the list of all enforcement
 points with an active Enterprise DLP license and the enforcement
 point Serial Number . 

 Use this list of enforcement point serial numbers when selecting VM-Series firewalls with which to associate the Enterprise DLP license. 

 Associate Enterprise DLP with your VM-Series 
 firewalls. 

 Select System Settings Device Association . 

 Select the tenant for which you activated Enterprise DLP . 

 Select one or more VM-Series firewalls and
 Associate Products . 

 TSG Aware Customer Support Account — Strata Cloud Manager displays only the VM-Series firewalls
 without an active Enterprise DLP license. 

 Non-TSG Aware Customer Support Account —Ensure you
 don't select any VM-Series firewalls with an
 already active Enterprise DLP license by comparing the
 list of available enforcement points and the list of
 enforcement points with an active Enterprise DLP 
 license you generated in the previous step. 

 Selecting a VM-Series firewall with an active
 Enterprise DLP license blocks activation. You must
 deselect any VM-Series firewalls with an
 active Enterprise DLP license. 

 In the Products list, select
 Enterprise DLP . 

 Select the VM-Series firewalls and
 Save . 

 ( Panorama only ) Install the Enterprise DLP Plugin on Panorama . 

 If you're managing your VM-Series firewalls from Panorama , you must install the Enterprise DLP plugin on Panorama to manage your Enterprise DLP configuration,
 synchronize Enterprise DLP configuration objects with Strata Cloud Manager , and to push Enterprise DLP configuration changes
 to your VM-Series firewalls. A Panorama with the Enterprise DLP plugin installed is required; Enterprise DLP does
 not support managing your Enterprise DLP configuration directly on your
 VM-Series firewalls. 

 Install the Enterprise DLP plugin after you associate Enterprise DLP with your Panorama and NGFW . This ensures the plugin correctly maps to your
 TSG and prevents synchronization issues. 

 Enable Enterprise DLP . 

 Some apps, such as SharePoint and OneDrive, use HTTP/2 by default. For NGFW , Prisma Access tenants, and VM-Series 
 firewalls managed by Panorama or by Strata Cloud Manager running
 PAN-OS 10.2.2 and earlier releases, you must create a
 decryption profile and a Security policy rule to strip out the
 application-layer protocol negotiation (ALPN) extension in headers. Complete
 these steps to successfully forward traffic to Enterprise DLP . 

 Previous 

 Activate Next-Generation CASB for Prisma Access and NGFW (CASB-X) 

 Next 

 Install the Enterprise DLP Plugin on Panorama 

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

 © 2026 Palo Alto Networks, Inc. All rights reserved.

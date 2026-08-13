---
url: https://docs.paloaltonetworks.com/globalprotect/administration/globalprotect-user-authentication/set-up-external-authentication/set-up-saml-authentication/customizing-the-saml-cas-acs-landing-page
fetched_at: 2026-08-13T16:32:53Z
source: palo-alto-main
---

# Customize the SAML/CAS ACS Landing Page Clear

Customize the SAML/CAS ACS Landing Page 

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

 Customize the SAML/CAS ACS Landing Page 

 Updated on 

 Wed Jul 08 22:34:43 PDT 2026 

 Focus 

 Download PDF 

 English 

 日本語 (Japanese) 

 Filter

 Expand All 
 | 
 Collapse All 

 GlobalProtect Docs 

 Getting Started 

 Activation & Onboarding 

 Administration 

 User Guide 

 Select a Document 

 6.3 

 6.2 

 6.1 

 6.0 

 Release Notes 

 Select a Document 

 6.3 

 6.2 

 6.1 

 6.0 

 New Features 

 Updated on 

 Wed Jul 08 22:34:43 PDT 2026 

 Focus 

 Home 

 GlobalProtect 

 GlobalProtect Administrator's Guide 

 GlobalProtect User Authentication 

 Set Up External Authentication 

 Set Up SAML Authentication 

 Customize the SAML/CAS ACS Landing Page 

 Download PDF 

 English 

 日本語 (Japanese) 

 GlobalProtect 

 Customize the SAML/CAS ACS Landing Page 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 GlobalProtect Docs 

 Getting Started 

 Activation & Onboarding 

 Administration 

 User Guide 

 Select a Document 

 6.3 

 6.2 

 6.1 

 6.0 

 Release Notes 

 Select a Document 

 6.3 

 6.2 

 6.1 

 6.0 

 New Features 

 Previous 

 Manage Browser Selection for SAML Authentication 

 Next 

 Set Up Kerberos Authentication 

 Customize the SAML/CAS ACS Landing Page 

 This feature describes how the admins can customize the SAML/CAS anding
 page 

 Where Can I Use This? What Do I Need? 

 NGFW (managed by Panorama or Strata Cloud Manager) 

 PAN-OS 10.2.11 or later 

 GlobalProtect app running on Windows, macOS, iOS, Android,
 and Linux endpoints. 

 You can now customize the SAML/CAS ACS landing page displayed on the default browser
 when you are using the SAML/CAS authentication method to authenticate to the
 GlobalProtect app. You can configure to rebrand or debrand the SAML/CAS ACS landing
 page on the default browser by using command-line interface (CLI) commands. By
 default, the feature is not enabled for the app. 

 This feature is not available on Panorama. 

 Before you customize the SAML/CAS ACS landing page, you must: 

 Ensure that the GlobalProtect Portal is
 configured. 

 Ensure that the GlobalProtect Gateway is
 configured. 

 Ensure that the default browser for SAML
 authentication is enabled in the portal configuration through either
 or both of the following methods: 

 Set the Use Default Browser for SAML
 Authentication option to Yes in
 the app settings of the GlobalProtect portal configuration. 

 Enable the Use Default-Browser option in the
 client authentication setting of the portal configuration. 

 To configure the GlobalProtect portal to rebrand or debrand the SAML/CAS ACS
 landing page on the default browser, use the following CLI commands: 

 On the firewall hosting the portal, enter the following CLI command. 

 <username@hostname> set global-protect auth-response-page 

 The screen displays the CLI commands for the SAML/CAS ACS page
 customization feature: 

 Use the following CLI commands to customize the SAML/CAS ACS
 landing page: 

 set global-protect auth-response-page type <default | none | custom> 

 To continue using the default ACS page, leave the type empty or use
 the CLI
 command: 
 set global-protect auth-response-page type <default>

 When you configure the global-protect auth-response-page
 type as <default> and the
 authentication is successful, the default ACS page is displayed with
 Authentication Complete message. If the Authentication
 fails, the screen displays the Authentication Failed 
 message. 

 To remove the default logo, background image, footer logo, and footer
 text, use the CLI
 command: 
 set global-protect auth-response-page type <none>

 To customize the page, use the CLI command:

 set global-protect auth-response-page type <custom>

 Use the following CLI commands to customize the fields of the SAML/CAS ACS
 landing
 page: 
 set global-protect auth-response-page background-image <value> 

 set global-protect auth-response-page main-logo <value> 

 set global-protect auth-response-page auth-message <value> 

 set global-protect auth-response-page footer-logo <value>

 set global-protect auth-response-page footer-text <value>

 You can leave the values empty for all the fields except for the
 type <value> 

 For image <value>, you must enter a valid HTTP or HTTPS URL 

 For text <value>, do not enter any control characters such as \n,
 \r, \t, \0 or characters whose ascii value is < 0x1F 

 Use the following CLI command to view the current authentication response
 page
 settings: 
 set global-protect auth-response-page <show> 

 Character Limits for the Customized Fields 

 The following table lists the maximum character limits for the fields that
 you can customize and the screen displays error messages when you enter a
 value that exceeds the character limit. 

 Field Character Limit Error Messages (When the Character Limit
 Exceeds) 

 Background Image URL 

 2000 

 Should be less than or equal to 2000 characters 

 Main Logo URL 

 2000 

 Should be less than or equal to 2000 characters 

 Footer Logo URL 

 2000 

 Should be less than or equal to 2000 characters 

 Authentication Message 

 500 

 Should be less than or equal to 500 characters 

 Footer Text 

 256 

 Should be less than or equal to 256 characters 

 Image Resolution and Types for the Customized Fields 

 The feature supports all image types such as .png, .jpeg/.jpg, and .svg based
 on the browser compatibility. You must use proper image resolution (width x
 height) depending on the dimensions of the devices. 

 The following table lists the image resolution that you can apply while
 customizing the page: 

 Image Image Resolution 

 Background Image 

 Background image block width is 100% of the
 device/browser window width, and the height is
 calculated by the browser using the image aspect
 ratio. 

 Main Logo 

 Main logo image block width is around 50% of the
 device/browser window width with maximum width of 340
 px, and the height is calculated by the browser using
 the image aspect ratio. 

 Footer Logo 

 Footer logo image block width is fixed to 30 px, and the
 height is calculated by the browser using the image
 aspect ratio. 

 For the footer logo image the aspect ratio for the
 width: height must not be more than three times of the
 width (1:3). If the height ratio increases such as 1:4,
 the footer text may not be properly displayed on the
 screen. 

 Previous 

 Manage Browser Selection for SAML Authentication 

 Next 

 Set Up Kerberos Authentication 

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

 Virtual ION on KVM for NFV 

 Virtual ION on OCI 

 Virtual ION on VMware 

 3rd Party Integrations 

 AWS Cloud-WAN Integration (GRE Connect) 

 AWS Cloud-WAN Integration (Tunnel-less Connect) 

 Checkpoint Integration 

 LiveAction Integration 

 Netskope Integration 

 Symantec Web Security Services Integration 

 Best Practices 

 Best Practices Library 

 Experts Corner 

 Solutions Docs from Product Experts 

 GlobalProtect Administration 

 Network Security 

 10.1 & Later 

 Administration 

 GlobalProtect 

 English 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

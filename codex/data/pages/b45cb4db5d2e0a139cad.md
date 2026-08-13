---
url: https://docs.paloaltonetworks.com/prisma-access-agent/user-guide/configure-windows-hello-for-business-authentication-for-prisma-access-agent
fetched_at: 2026-08-13T17:22:40Z
source: palo-alto-main
---

# Configure Windows Hello for Business Authentication for Prisma Access Agent Clear

Configure Windows Hello for Business Authentication for Prisma Access Agent 

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

 Configure Windows Hello for Business Authentication for Prisma Access Agent 

 Updated on 

 Wed Jul 01 22:45:41 PDT 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma Access Agent Docs 

 Administration 

 User Guide 

 Release Notes 

 New Features 

 Updated on 

 Wed Jul 01 22:45:41 PDT 2026 

 Focus 

 Home 

 Prisma Access Agent 

 Prisma Access Agent User Guide 

 Configure Windows Hello for Business Authentication for Prisma Access Agent 

 Download PDF 

 Prisma Access Agent 

 Configure Windows Hello for Business Authentication for Prisma Access Agent 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma Access Agent Docs 

 Administration 

 User Guide 

 Release Notes 

 New Features 

 Configure Windows Hello for Business Authentication for Prisma Access Agent 

 Configure your environment to use Windows Hello for Business authentication with
 Prisma Access Agent . 

 Where Can I Use This? What Do I Need? 

 Prisma Access (Managed by Strata Cloud Manager) 

 Prisma Access (Managed by Panorama) 

 NGFW (Managed by Panorama) 

 Check the prerequisites for the deployment you're
 using 

 Minimum Prisma Access Agent version: 26.1 

 Windows Hello for Business enabled 

 Microsoft Entra ID-joined Windows 10 version 2024 or later
 devices 

 Contact your Palo Alto Networks account representative to
 activate the Prisma Access Agent feature 

 To enable Windows Hello for Business authentication with Prisma Access Agent , you
 need to properly configure both your Microsoft Entra ID environment and Cloud
 Identity Engine. This procedure guides you through the necessary steps to set up
 this integration. 

 Once configured, Prisma Access Agent will automatically detect the availability of
 Primary Refresh Tokens on your users' devices and leverage Windows Hello for
 Business authentication methods. Users will be able to authenticate using their
 configured personal identification number (PIN) or biometric methods without
 additional web-based authentication steps. 

 Single sign-on with Windows Hello for Business is supported with either the Prisma Access Agent embedded
 browser or the default system browser for SAML
 authentication. You can configure the agent settings to suppress the embedded browser so that it won't appear. 

 Configure Microsft Entra ID and Windows Hello for Business. 

 Connect your Windows systems to Microsoft Entra ID. 

 This enables Entra to manage authentication policy rules for your
 devices. Consult Microsoft's documentation for detailed procedures
 on joining devices to Microsoft
 Entra . 

 Configure Windows Hello for Business
 policy rules in Microsoft Entra ID . 

 Set up policy rules that enforce PIN requirements, biometric
 authentication methods (facial recognition, fingerprint), and other
 security settings according to your organization's requirements. 

 Preconfigure end-user devices with Windows Hello for Business. 

 Ensure your users have registered their biometric data or created
 PINs according to your organization's policy rules. This step is
 crucial for enabling Primary Refresh Token generation on user
 devices. 

 Configure Cloud Identity Engine. 

 Configure Entra ID as an identity
 provider (IdP) in Cloud Identity Engine . Create a Security
 Assertion Markup Language (SAML) 2.0 authentication type for Azure type
 and configure the SAML settings to integrate with your Azure AD
 environment. 

 Set up an authentication
 profile and associate the profile with the Azure
 authentication type you created. 

 Check the user authentication and app configuration for Prisma Access Agent . 

 Set up user authentication for Prisma Access Agent using SAML with Cloud Identity Engine . 

 In the User Authentication section, make sure the configured
 authentication type is SAML . 
 For example, on
 Strata Cloud Manager Managed Prisma Access : 

 In the App Configuration section, make sure the
 Connect method is set to Always
 On . 

 ( Optional ) To prevent the Prisma
 Acesss Agent embedded browser from appearing during single sign-on,
 select Show Advanced Options Authentication and enable Use Single Sign-on
 (Windows) . 

 Go to Configuration Configure NGFW and Prisma Access and make sure the authentication profile mapped in the
 SAML user authentication is mapped to the Azure AD or Entra ID as the
 IdP. 

 If you made any changes, save and push the configuration. 

 Your Entra ID-joined users can now log in to their Windows devices with their
 PIN or biometric method and see that Prisma Access Agent is in the connected
 state. 

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

 Visibility & Monitoring 

 Dashboards 

 Incidents and Alerts 

 Reports 

 Autonomous DEM 

 Best Practices 

 Best Practices Library 

 Experts Corner 

 Solutions Docs from Product Experts 

 Prisma Access Agent 

 Next-Generation Firewall 

 Administration 

 Prisma Access 

 Panorama 

 Strata Cloud Manager 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

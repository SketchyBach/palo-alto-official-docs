---
url: https://docs.paloaltonetworks.com/saas-security/sspm/onboard-saas-apps-supported-by-sspm/onboard-a-webex-app-to-sspm
fetched_at: 2026-08-13T17:34:22Z
source: palo-alto-main
---

# Onboard a Webex App to SSPM Clear

Onboard a Webex App to SSPM 

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

 Onboard a Webex App to SSPM 

 Updated on 

 Fri Jul 10 09:31:52 PDT 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 SaaS Security Docs 

 Activation & Onboarding 

 Getting Started 

 Data Security 

 SaaS Security Inline 

 SSPM 

 Behavior Threats 

 New Features 

 Updated on 

 Fri Jul 10 09:31:52 PDT 2026 

 Focus 

 Home 

 SaaS Security 

 Onboard SaaS Apps Supported by SSPM 

 Onboard a Webex App to SSPM 

 Download PDF 

 SaaS Security 

 Onboard a Webex App to SSPM 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 SaaS Security Docs 

 Activation & Onboarding 

 Getting Started 

 Data Security 

 SaaS Security Inline 

 SSPM 

 Behavior Threats 

 New Features 

 Previous 

 Onboard a Terraform App to SSPM 

 Next 

 Onboard a Weights & Biases App to SSPM 

 Onboard a Webex App to SSPM 

 Connect a Webex instance to SSPM to detect posture risks. 

 Where Can I Use This? What Do I Need? 

 Strata Cloud Manager 

 SaaS Security Posture Management license 

 Or any of the following licenses that include the Data Security license: 

 CASB-X 

 CASB-PA 

 For SSPM to detect posture risks in your Webex instance, you must onboard your Webex
 instance to SSPM. Through the onboarding process, SSPM logs in to Webex using
 administrator account credentials. SSPM uses this account to scan your Webex
 instance for misconfigured settings. If there are misconfigured settings, SSPM
 suggests a remediation action based on best practices. 

 During the onboarding process, you will supply Webex account credentials to SSPM.
 SSPM can access the account directly or through the Okta or Microsoft Azure identity
 providers. Having SSPM access the account through one of these identity providers
 requires multi-factor authentication (MFA), which adds an extra layer of security.
 For direct login, MFA is optional. 

 To onboard your Webex instance, you complete the following actions: 

 Collect Information for Accessing Your Webex Instance 

 Connect SSPM to Your Webex Instance 

 Collect Information for Accessing Your Webex Instance 

 To access your Webex instance, SSPM requires the following information, which you
 will specify during the onboarding process. 

 Item Description 

 User The username or email address of an administrator
 account. The format that you use can depend on whether SSPM will
 log in directly to your account or through an identity
 provider. 
 Required Permissions: The user must
 be a Webex administrator. 

 Password The password for the administrator
 account. 

 If you are logging in through Okta, you must provide SSPM with the following
 additional information: 

 Item Description 

 Okta subdomain The Okta subdomain for your organization. The
 subdomain is included in the login URL that Okta assigned to
 your organization. 

 Okta 2FA secret A key that is used to generate one-time passcodes
 for MFA. 

 If you are using Azure Active Directory (AD) as your identity provider, you must
 provide SSPM with the following additional information: 

 Item Description 

 Azure 2FA secret A key that is used to generate one-time passcodes for
 MFA. 

 If you are logging in to Webex directly instead of using an identity provider,
 you can use Webex's built-in MFA capability to verify your account by using
 one-time passcodes. Although SSPM does not require MFA for direct login to
 Webex, your organization might require MFA. To enable SSPM to generate these
 one-time passcodes, and you must provide the following additional
 information: 

 Item Description 

 Webex 2FA secret A key that is used to generate one-time passcodes for
 MFA. 

 As you complete the following steps, make note of the values of the items
 described in the preceding tables. You will need to enter these values during
 onboarding to access your Webex instance from SSPM. 

 Identify the Webex administrator account that SSPM will use to access your
 Webex instance. 

 Determine whether you want SSPM to log in to the administrator account
 directly by using Webex account credentials, or through an identity provider
 (Okta or Microsoft Azure). 

 For direct login using Webex administrator account
 credentials , decide if you want SSPM to use MFA
 authentication when connecting to your Webex instance. SSPM does not
 require MFA to connect to a Webex instance, but your organization
 might require MFA. To configure MFA, you will generate an MFA secret
 key by using Webex's built-in MFA capability. Do not complete these
 steps if you will be accessing the administrator account through an
 identity provider. 
 If the Webex administrator account is already
 configured for MFA, and if you know the MFA secret key value,
 you don't need to complete the following steps. You need only
 provide the MFA secret key to SSPM during the onboarding
 process. 

 Decide which authenticator app you will use and download it
 to your cellphone. 
 You can use any authenticator app that
 supports time-based one-time passcode (TOTP) generation.
 TOTPs are generated from authenticator apps, such as
 Microsoft Authenticator or Duo Mobile, by using an MFA
 secret key. The key is a shared secret between Webex and
 the authenticator app for generating matching passcodes
 for verification. Like an authenticator app, SSPM uses
 the MFA secret key for passcode generation. 

 Open a web browser and go to the Webex Control Hub sign-in
 page at admin.webex.com . 

 Log in to the Webex administrator account that you will use
 to onboard your Webex instance to SSPM. 
 If MFA is already
 configured for the account, you are prompted to enter
 your one-time passcode. If you know the MFA shared
 secret that generates your one-time passcodes, you do
 not need to complete these steps. Instead, make note of
 the secret key so you can enter it during
 onboarding. 

 If MFA is already configured for the
 account, but you don't know the MFA secret key, do not
 enter your passcode at the prompt. Instead, select
 Reset Authenticator . The
 Webex Control Hub will prompt you to log in again. After
 you log in, the Webex Control Hub will display the MFA
 configuration wizard. 

 The first panel of the MFA configuration wizard prompts you
 to download an authenticator app. Because you have already
 downloaded an authenticator app, go to the
 Next panel of the wizard. 

 The next panel of the MFA configuration wizard displays your
 MFA secret key as a QR code, but do not scan the QR
 code. Instead, click See manual activation
 code to display a text version of the MFA
 secret key. 

 Copy and paste the text version of the MFA secret key into a
 text file. 

 Do not continue to
 the next step unless you have copied the MFA secret key.
 You will provide this key to SSPM during the onboarding
 process. 

 Continue configuring your authentication app by scanning the
 QR code or by manually entering the MFA secret key. 

 ( For Okta log in ) To access the administrator account
 through Okta : 
 Identify your
 Okta subdomain . 

 Generate and
 copy an MFA secret key . 

 ( For Microsoft Azure log in ) To access the administrator
 account through Microsoft Azure : 
 Enable
 third-party software OATH tokens for the administrator
 account . 

 Configure the
 account for MFA and copy the MFA secret key . 

 Connect SSPM to Your Webex Instance 

 By adding a Webex app in SSPM, you enable SSPM to connect to your Webex
 instance. 

 Log in to 
 Strata Cloud Manager . 

 Select Configuration SaaS Security Posture Security Applications Add Application and click the Webex tile. 

 On the Posture Security tab, Add
 New instance. 

 Specify how you want SSPM to connect to your Webex instance. SSPM can
 Log in with Credentials , Log in with
 Okta , or Log in with Azure . 

 When prompted, provide SSPM with the administrator credentials. If
 necessary, specify the information that SSPM needs for MFA. 

 Connect . 

 Previous 

 Onboard a Terraform App to SSPM 

 Next 

 Onboard a Weights & Biases App to SSPM 

 On This Page 

 Activation & Onboarding 

 Strata Cloud Manager 

 Cloud Identity Engine 

 Strata Logging Service 

 Device Associations 

 Identity and Access Management 

 Tenant Management 

 Next-Generation Firewalls 

 AIOps for NGFW 

 Cloud Management for NGFWs 

 Firewalls 

 PAN-OS 

 SASE 

 Prisma Access 

 Strata Multitenant Cloud Manager 

 Prisma Access Monitoring and Visibility 

 Next-Generation CASB 

 Cloud-Delivered Security Services 

 Advanced WildFire 

 Enterprise DLP 

 SaaS Security 

 Visibility & Monitoring 

 Dashboards 

 Incidents and Alerts 

 Reports 

 Autonomous DEM 

 Best Practices 

 Best Practices Library 

 Experts Corner 

 Solutions Docs from Product Experts 

 SaaS Security Posture Management 

 SaaS Security 

 SSPM 

 Cloud-Delivered Security Services 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

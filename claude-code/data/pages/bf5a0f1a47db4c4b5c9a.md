---
url: https://cortex-docs.paloaltonetworks.com/cortex-cloud-runtime-security/saas-security/saas-security/onboard-a-supported-saas-application/onboard-monday.com
fetched_at: 2026-09-16T08:45:20Z
source: cortex-platform
---

# Onboard Monday.com | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex Cloud 

 Cortex CLOUD Runtime Security 

 Saas Security 

 SaaS Security 

 Onboard a Supported SaaS Application 

 Cortex Cloud Runtime 

 Onboard Monday.com 

 Connect a Monday.com instance to detect posture risks and compliance violations. 

 For SaaS Security to detect posture risks in your monday.com instance, you must onboard your monday.com instance to SaaS Security. Through the onboarding process, SaaS Security logs in to monday.com using administrator account credentials. SaaS Security uses this account to scan your monday.com instance for misconfigured settings. If there are misconfigured settings, SaaS Security suggests a remediation action based on best practices. 

 To onboard your monday.com instance, complete the following actions: 

 Collect information for connecting to your monday.com instance 

 Connect SaaS Security to your monday.com instance 

 Step 1: Collect Information for Connecting to Your monday.com Instance 

 To access your monday.com instance, SaaS Security requires connection information. During the onboarding process, you specify the following required and optional information. 

 Item 

 Description 

 Email 

 The login email address of a monday.com administrator. Required Permissions: You must supply SaaS Security with Admin credentials to your monday.com account. 

 Password 

 The password of the monday.com administrator. 

 Account Domain 

 The custom domain for your monday.com account. After you log in to monday.com, this domain is part of your monday.com URL in the format <account_domain>.monday.com. 

 MFA Secret Key 

 (Optional) A key that is used to generate one-time passcodes for multi-factor authentication. 

 As you complete the following steps, make note of the values of the items described in the preceding table. You will need to enter these values during onboarding to access your monday.com instance from SaaS Security. 

 Identify the monday.com administrator whose credentials you will supply to SaaS Security. 

 Required Permissions: You must supply SaaS Security with Admin credentials to your monday.com account. 

 Identify your monday.com account domain. 

 After you log in to monday.com, the account domain is a unique subdomain included in the monday.com URL in the format <account_domain>.monday.com. You can also identify your account domain from your profile: 

 Open a web browser and go to the monday.com login page at auth.monday.com/auth/login_monday . 

 Log in to the administrator account that you identified. 

 Navigate to the Administration page. Locate your account avatar and select <account-avatar> > Administration. 

 On the Administration page, select General > Profile. The Account URL (Web Address) field shows your account domain. 

 (Optional) Generate and copy an MFA secret key. 

 MFA provides an extra layer of security when accessing the monday.com administrator account. To enable this extra layer of security, you must configure the administrator account for MFA that uses time-based one-time passcodes. Like an authenticator app, SaaS Security uses the MFA secret key for passcode generation. 

 Decide which authenticator app you will use and download it to your cellphone. You can use any authenticator app that generates time-based one-time passcodes (TOTP), such as Microsoft Authenticator or Google Authenticator. 

 Open a web browser and go to auth.monday.com/auth/login_monday and log in to the administrator account. 

 Navigate to the Administration page. Locate your account avatar and select <account-avatar> > Administration. 

 On the Administration page, select Security > Login. 

 Locate the Two-Factor Authentication section and click Enable Two-Factor Authentication. 

 When monday.com prompts you to choose your authentication method, select Authentication App and click Continue. 

 A pop-up window displays your MFA secret key as a QR code. Do not scan the QR code. Click Copy code instead to display a text version of the MFA secret key. 

 Copy and paste the text version of the MFA secret key into a text file. 

 Note : Do not continue to the next step unless you have copied the MFA secret key. You will provide this key to SaaS Security during the onboarding process. 

 Continue configuring your authentication app by scanning the QR code or by manually entering the MFA secret key. 

 Step 2: Connect SaaS Security to Your monday.com Instance 

 By adding a monday.com app in Cortex, you enable SaaS Security to connect to your monday.com instance. 

 Log in to Cortex. 

 Select Settings > Data Sources and Integrations > Add New . You can use the Search bar to find the app you want to connect to. 

 Click the monday.com tile. 

 Under Capabilities , enter a name for your application. 

 Select Security Posture under Default Capabilities and click Next. 

 Under Connections , enter the administrator login credentials, your account domain, and, optionally, the MFA secret key. 

 Under Configurations , select a Sync Interval . Choose a meaningful Tag to distinguish between various applications in different environments. 

 Click Next to complete the onboarding validation process. 

 Previous Onboard Microsoft Entra ID 

 Next Onboard MongoDB Atlas 

 Last updated 1 day ago 

 Was this helpful?

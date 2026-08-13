---
url: https://docs.paloaltonetworks.com/globalprotect/administration/globalprotect-user-authentication/set-up-two-factor-authentication/enable-two-factor-authentication-using-smart-cards/enhancements-for-authentication-using-smart-cards-authentication-fallback
fetched_at: 2026-08-13T16:32:55Z
source: palo-alto-main
---

# Support Authentication Profiles With or Without PIV Clear

Support Authentication Profiles With or Without PIV 

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

 Support Authentication Profiles With or Without PIV 

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

 Set Up Two-Factor Authentication 

 Enable Two-Factor Authentication for GlobalProtect Using Smart Cards 

 Support Authentication Profiles With or Without PIV 

 Download PDF 

 English 

 日本語 (Japanese) 

 GlobalProtect 

 Support Authentication Profiles With or Without PIV 

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

 Reduce PIN Prompts for Smart Card Authentication on GLobalProtect 

 Next 

 Enable Two-Factor Authentication Using a Software Token Application 

 Support Authentication Profiles With or Without PIV 

 Enhancements for Authentication Using Smart Cards-Authentication Fallback 

 Where Can I Use This? What Do I Need? 

 NGFW (managed by Panorama) 

 Prisma Access (managed by Panorama or Strata Cloud
 Manager) 

 Windows and macOS endpoints only 

 GlobalProtect Gateway license or Prisma Access license with
 the Mobile User subscription 

 GlobalProtect app version 6.3.0 or later for Windows 

 GlobalProtect app version 6.3.1 or later for macOS 

 Content Version for Smartcard for macOS: 8890-8951 

 If you have configured On-demand mode for the GlobalProtect
 app running on Windows or macOS endpoints with smart card authentication as the
 authentication method, the app now displays the authentication profile options with
 or without the PIV smart card. 

 Enhancements for Authentication Using Smart Cards on Windows Endpoints 

 Where Can I Use This? What Do I Need? 

 GlobalProtect Subscription License 

 GlobalProtect app version 6.3.0 or later 

 GlobalProtect app running on Windows endpoints 

 If you have configured Connect Before Logon -
 On-demand mode for the GlobalProtect app with smart
 card authentication as the authentication method, the app now provides the
 flexibility to the end users to authenticate to the app either using smart card
 or using their username/password. With this feature enabled, the GlobalProtect
 app displays two authentication profiles for the enduser in the
 Portals drop-down on the app homepage; a profile with
 <smartcard> and another profile with
 <no smartcard> . From the two available
 options, the end users can choose their preferred authentication profile. The
 profile with <smartcard> option allows the end
 user to authenticate to the app using the smart card authentication method
 whereas the profile with <no smartcard> option
 allows them to authenticate to the app using their username and password. 

 For example, if end users forget to bring their smart card to work, they can
 choose the authentication profile with <no
 smartcard> from the Portals drop-down
 and can use their username and password to authenticate to the app. If smart
 card is available, they can use the profile with
 <smartcard> and authenticate using smart
 card authentication. 

 This feature will work only when ActivClient software is installed on the
 device, if you have configured Connect Before Logon method for
 the GlobalProtect app. 

 If Always-On 
 connect method is configured for the GlobalProtect app and authentication
 profile keys are predeployed, the default profile option
 <smartcard> will be selected. The end
 user has the option to disconnect the app and change the profile option if
 required. 
 If On-Demand connect method is
 configured for the GlobalProtect app and authentication profile keys are
 predeployed, the end user can choose either
 <smartcard> or <no
 smartcard> option from the app user interface
 ( Portals drop-down). 

 If you have configured Connect Before Logon -
 On-demand mode for the GlobalProtect app with smart
 card authentication as the authentication method, the app now displays the
 authentication profile options with or without the PIV smart card. 

 For the GlobalProtect app to display the authentication profile options with or
 without the PIV smart card, you must: 

 Ensure that Connect Before Logon (CBL) is
 configured with On-demand mode for the GlobalProtect
 app. 

 Select the Allow Authentication with User
 Credentials OR Client Certificate option while configuring the
 GlobalProtect gateway and portal. This option defines whether users can
 authenticate to the portal or gateway using credentials and/or client
 certificates. 

 In the Windows Registry, define the predeployment settings for the app to
 display the authentication profile options with
 <smartcard> and <no
 smartcard> . 

 Launch the Command Prompt and enter regedit 
 to open the Windows Registry. 

 In the Windows Registry, go to:
 HKEY_LOCAL_MACHINE\SOFTWARE\Palo Alto
 Networks\GlobalProtect\Settings\ . 

 Click Edit and then select New String Value . 

 When prompted, specify the Name of the new
 registry value as PIV-profile . 

 Right-click the new registry value and
 Modify it. 

 Set the Value Data to
 yes 

 Click OK . 

 To predeploy the setting from Windows Installer (Msiexec) use the
 following syntax: 

 msiexec.exe / globalprotect64.msi /i PIVPROFILE=yes 

 Customize the Windows Registry Keys for Profile
 Options 

 Starting with GlobalProtect version 6.3.1, you can predeploy the
 customized registry key values for the profile options;
 <PIV> and <NO
 PIV> . 
 The <PIVString> key is available
 in the Windows Registry path:
 HKEY_LOCAL_MACHINE\SOFTWARE\Palo Alto
 Networks\GlobalProtect\Settings 

 The <NoPIVString> key is
 available in the Windows Registry path:
 HKEY_LOCAL_MACHINE\SOFTWARE\Palo Alto
 Networks\GlobalProtect\Settings 

 Enhancements for Authentication Using Smart Cards on macOS Endpoints 

 Where Can I Use This? What Do I Need? 

 GlobalProtect Subscription License 

 GlobalProtect app version 6.3.1 or later 

 Content
 Version for Smartcard for macOS: 8890-8951 

 If you have configured On-demand mode for the
 GlobalProtect app running on macOS endpoints with smart card authentication as
 the authentication method, the app now displays the authentication profile
 options with or without the PIV smart card. 

 If Always-On connect
 method is configured for the GlobalProtect app and authentication profile
 keys are predeployed, the default profile option
 <smartcard> will be selected. The end
 user has the option to disconnect the app and change the profile option if
 required. 
 If On-Demand connect method is
 configured for the GlobalProtect app and authentication profile keys are
 predeployed, the end user can choose either
 <smartcard> or <no
 smartcard> option from the app user interface
 ( Portals drop-down). 

 For the GlobalProtect app to display the authentication profile options with or
 without the Smart Card on macOS endpoints, you must: 

 Ensure that the connect method is configured with
 On-demand mode for the GlobalProtect app. 

 Select the Allow Authentication with User
 Credentials OR Client Certificate option while configuring the
 GlobalProtect gateway and portal. This option defines whether users can
 authenticate to the portal or gateway using credentials and/or client
 certificates. 

 In the macOS GlobalProtect plist file, define the predeployment settings
 for the app to display the authentication profile options with
 <smartcard> and <nO
 smartcard> . 

 Open the GlobalProtect plist file and locate the GlobalProtect
 customization settings. 

 Launch a plist editor, such as Xcode. 

 In the plist editor, open the following plist file:
 /Library/Preferences/
 com.paloaltonetworks.GlobalProtect.settings.plist. 

 Locate the GlobalProtect Settings dictionary:
 /Palo Alto Networks/
 GlobalProtect/Settings . If the Settings
 dictionary does not exist, create it. You can add each key
 to the Settings dictionary as a string. 

 In the Settings dictionary, add the following key-value pair to
 enable the authentication PIV profile with or without PIV
 smartcard: 

 <key>PIV-profile</key> 

 <string>yes</string> 

 To predeploy the customised keys, use: 
 <key>PIVString</key> 

 <key>noPIVString</key> 

 Previous 

 Reduce PIN Prompts for Smart Card Authentication on GLobalProtect 

 Next 

 Enable Two-Factor Authentication Using a Software Token Application 

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

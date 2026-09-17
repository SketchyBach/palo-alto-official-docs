---
url: https://docs.paloaltonetworks.com/globalprotect/10-1/globalprotect-admin/globalprotect-user-authentication/set-up-two-factor-authentication/enable-two-factor-authentication-using-smart-cards/enhancements-for-authentication-using-smart-cards-authentication-fallback
fetched_at: 2026-09-16T12:57:49Z
source: palo-alto-main
---

# Support Authentication Profiles With or Without PIV Clear

Updated on 

 Aug 11, 2026 

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

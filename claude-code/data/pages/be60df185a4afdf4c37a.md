---
url: https://docs.paloaltonetworks.com/globalprotect/release-notes/6-0/changes-to-default-behavior
fetched_at: 2026-09-15T15:14:09Z
source: palo-alto-main
---

# Changes to Default Behavior Clear

Updated on 

 Wed Jun 24 23:47:12 PDT 2026 

 Focus 

 Home 

 GlobalProtect 

 Changes to Default Behavior 

 Download PDF 

 GlobalProtect 

 Changes to Default Behavior 

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

 Enable the GlobalProtect App for macOS to Use Client Certificates for Authentication 

 Previous 

 Uninstall the GlobalProtect App for Linux 

 Previous 

 GlobalProtect for IoT Devices 

 Previous 

 GlobalProtect for IoT Devices 

 Next 

 Associated Software and Content Versions 

 Changes to Default Behavior 

 Changes to default behavior in GlobalProtect app 6.0. 

 The following topics describe changes to default behavior in GlobalProtect app 6.0 versions: 

 Changes to Default Behavior in GlobalProtect App 6.0.13 

 Changes to Default Behavior in GlobalProtect App 6.0.12 

 Changes to Default Behavior in GlobalProtect App 6.0.11 

 Changes to Default Behavior in GlobalProtect App 6.0.10 

 Changes to Default Behavior in GlobalProtect App 6.0.8 

 Changes to Default Behavior in GlobalProtect App 6.0.7 

 Changes to Default Behavior in GlobalProtect App 6.0.6 

 Changes to Default
Behavior in GlobalProtect App 6.0.5 

 Changes to Default Behavior in GlobalProtect App 6.0.4 

 Changes to Default Behavior
in GlobalProtect APP 6.0.3 

 Changes to Default Behavior in GlobalProtect App 6.0.2 

 Changes to Default Behavior in GlobalProtect App 6.0.1 

 Changes to Default Behavior in GlobalProtect App 6.0.0 

 Changes to Default Behavior in GlobalProtect App 6.0.13 

 There are no changes in default behavior in GlobalProtect app version 6.0.13. 

 Changes to Default Behavior in GlobalProtect App 6.0.12 

 There are no changes in default behavior in GlobalProtect app version 6.0.12. 

 Changes to Default Behavior in GlobalProtect App 6.0.11 

 You can now use the new system extension type Non-removable system
 extensions from UI introduced by Jamf Pro for the devices running on
 macOS 15 Sequoia or later versions to prevent the end users from disabling the
 GlobalProtect system extensions on the endpoints. GlobalProtect app
 version 6.0.11 and later supports macOS 15 Sequoia. This functionality is available
 only for the devices running on macOS 15 Sequoia or later versions. 

 You can configure this feature to prevent the end users from disabling GlobalProtect
 system extensions on their endpoints thereby reducing the risks associated with
 disabled system extensions. 

 Previously, end users could disable the GlobalProtect system extension through the
 MDM settings ( General Settings Network Extensions .) However, with this new feature, the Non-removable system
 extensions from UI system extension type in Jamf Pro restricts users
 from disabling the GlobalProtect system extension. 

 To enable this functionality, you must perform the following procedures: 
 Upgrade the GlobalProtect app to version 6.0.11 or later 

 Upgrade the macOS to version 15 Sequoia or later 

 In the mobile device management (MDM), Jamf Pro, set the System
 Extension Type as Non-removable system extensions
 from UI while configuring Configuration
 Profile. 

 If the GlobalProtect system extensions are disabled by the end-user, the following
 GlobalProtect features do not work: 
 Enforcer 

 Split-tunnel by domain 

 Split-tunnel by app 

 Split-DNS 

 Traffic Enforcement 

 Changes to Default Behavior in GlobalProtect App 6.0.10 

 There are no changes in default behavior in GlobalProtect app version 6.0.10. 

 Changes to Default Behavior in GlobalProtect App 6.0.8 

 There are no changes in default behavior in GlobalProtect app version 6.0.8. 

 Changes to Default Behavior in GlobalProtect App 6.0.7 

 There are no changes in default behavior in GlobalProtect app version 6.0.7. 

 Changes to Default Behavior in GlobalProtect App 6.0.6 

 There are no changes in default behavior in GlobalProtect app version 6.0.6. 

 Changes to Default Behavior in GlobalProtect App 6.0.5 

 Beginning with GlobalProtect app 6.0.5, the first time
users launch the GlobalProtect app for Android, they will be prompted
to read and acknowledge a disclosure about the information that
may be collected by the app. 

 Changes to Default Behavior in GlobalProtect App 6.0.4 

 ADEM agent installer has been bundled with GlobalProtect
installer since GlobalProtect version 5.2.6. ADEM installer bundled
with GlobalProtect version 6.0.4 has been updated and contains the
new ADEM Self-Serve feature
due to which there is a notable increase in the size of the GlobalProtect
installer. 

 Changes to Default Behavior in GlobalProtect App 6.0.3 

 There are no changes to default behavior in GlobalProtect
app 6.0.3. 

 Changes to Default Behavior in GlobalProtect App 6.0.2 

 There are no changes to default behavior in GlobalProtect
app 6.0.2. 

 Changes to Default Behavior in GlobalProtect App 6.0.1 

 There are no changes to default behavior in GlobalProtect
app 6.0.1. 

 Changes to Default Behavior in GlobalProtect App 6.0.0 

 ( Windows only ) Starting with GlobalProtect app 6.0, the GlobalProtect
 virtual adapter name on Windows endpoint has been changed from
 PANGP Virtual Ethernet Adapter to
 PANGP Virtual Ethernet Adapter Secure . The
 addition of the keyword secure ensures that Microsoft delivery optimization and peer caching
 can identify that a device is connected to a VPN. This change ensures that
 delivery optimization and peer caching work properly for a large number of
 Windows updates, upgrades, and application downloads. 

 If you are using PAN-OS 10.x.x or 11.0.x and the Use Default Browser
 for SAML Authentication option is selected in any of the portal
 agent configurations, the Use Default Browser option on
 the Client Authentication window will be automatically enabled after you upgrade
 to PAN-OS 11.1.0 or later. Starting from PAN-OS 11.1.0, the default browser
 behavior is controlled by the client authentication setting. For more
 information about this feature and upgrade considerations, see Manage Browser Selection for SAML
 Authentication . 

 Previous 

 Enable the GlobalProtect App for macOS to Use Client Certificates for Authentication 

 Previous 

 Uninstall the GlobalProtect App for Linux 

 Previous 

 GlobalProtect for IoT Devices 

 Previous 

 GlobalProtect for IoT Devices 

 Next 

 Associated Software and Content Versions

---
url: https://docs.paloaltonetworks.com/globalprotect/10-1/globalprotect-admin/globalprotect-portals/configure-intelligent-portal
fetched_at: 2026-09-16T12:57:50Z
source: palo-alto-main
---

# Configure Intelligent Portal Selection Clear

Updated on 

 Tue Aug 11 17:49:01 PDT 2026 

 Focus 

 Home 

 GlobalProtect 

 GlobalProtect Administrator's Guide 

 GlobalProtect Portals 

 Configure Intelligent Portal Selection 

 Download PDF 

 English 

 日本語 (Japanese) 

 GlobalProtect 

 Configure Intelligent Portal Selection 

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

 Define the GlobalProtect Agent Configurations 

 Next 

 Customize the GlobalProtect App 

 Configure Intelligent Portal Selection 

 Learn all about Intelligent Portal. 

 Where Can I Use This? What Do I Need? 

 NGFW (managed by Panorama ) 

 Prisma Access (managed by Panorama) 

 Prisma Access Mobile Users license (for use with Prisma
 Access) 

 GlobalProtect gateway license (for use with PAN-OS) 

 GlobalProtect app 6.3 and later 
 OS Support: Windows and
 macOS 

 Content release version: 8833-8679 and
 later 

 The intelligent portal selection feature enables automatic selection of the
 appropriate portal when a user travels across multiple countries for seamless and
 secure connectivity. After you configure intelligent portal in your environment,
 you're automatically routed to the appropriate Prisma Access portal based on your
 country location. For example, when you travel to China, you are directed to the
 China Prisma Access portal and to the North America portal when you're in the United
 States. This eliminates the need for manual selection of portals and improves the
 end user experience. 

 The intelligent portal feature is supported for the following modes. 
 Always-On and Always-On (Pre-logon) 

 Connect Before Logon if there is no additional portal list for Connect
 Before Logon 
 Intelligent portal is not supported for Connect Before Logon if a portal list
 is defined and for On-Demand mode. 

 Follow the steps below to configure and use the intelligent portal feature in your
 environment. 

 Configure intelligent portal. 

 Current Environment Deployment Steps 

 Fresh install of GlobalProtect 6.3 and later on Windows
 and macOS Deploy GlobalProtect with a command line option to add
 the intelligent portal feature: 
 msiexec.exe /i
 "GlobalProtect64.msi"
 PORTALCOUNTRYMAP=" portal1_address ( country1_code ); portal_2_address ( country2_code " 

 For
 example, the following command deploys GlobalProtect
 with intelligent portal and defines the portals for USA
 and China. You can define multiple portals for a
 country. 

 msiexec.exe /i
 "GlobalProtect64.msi"
 PORTALCOUNTRYMAP="xxx.com(US);yyy.com(CN)" 

 Existing installation of GlobalProtect 6.3 and later for
 Windows If GlobalProtect 6.3 or higher is already installed in
 your environment, you can add the following keys to the
 Windows Registry (path HKEY_LOCAL_MACHINE\SOFTWARE\Palo Alto
 Networks\GlobalProtect\Settings\). 
 (Required) REG ADD "HKLM\Software\Palo Alto
 Networks\GlobalProtect\Settings" /v
 portal-country-map /t REG_SZ /d
 portal_1 ( country1_code ); portal_2 ( country2_code ) 
 The
 portal map must not exceed 255
 characters. 

 (Optional) REG ADD "HKLM\Software\Palo Alto
 Networks\GlobalProtect\Settings" /v
 intelligent-portal /t REG_SZ /d
 yes 
 This entry enables the intelligent
 portal feature the first time the end user logs in
 to the GlobalProtect app. 

 (Optional) REG ADD "HKLM\Software\Palo Alto
 Networks\GlobalProtect\Settings" /v
 intelligent-portal-service /t REG_SZ /d
 "geoip.gpcloudservice.com/getIPLocation" 
 Add
 this entry if you want to host the API service to
 provide user location. 

 Existing installation of GlobalProtect 6.3 and later for
 macOS If GlobalProtect 6.3 or higher is already installed in
 your environment, you can define the following entries in
 the macOS plist. 

 Type sudo vi
 /Library/Preferences/com.paloaltonetworks.GlobalProtect.settings.plist . 

 Navigate to the /Palo Alto
 Networks/GlobalProtect/Settings 
 dictionary. 

 Add the following
 entries. 

 <key>intelligent-portal</key>
<string>yes</string>
<key>portal-country-map</key>
<string> portal1_address ( country1_code ); portal2_address ( country2_code )</string>
<key>intelligent-portal-service</key>
<string>geoip.gpcloudservice.com/getIPLocation</string> 

 Upgrade to GlobalProtect 6.3 and later If you uninstall the previous GlobalProtect release and
 do a fresh install, follow the fresh install procedure
 describes above. 
 If you upgrade GlobalProtect through the
 portal, add the intelligent portal settings to the
 Windows Registry or macOS plist. 

 For additional information on app settings, see Customizable App Settings . 

 Enable the intelligent portal feature on the portal. See step 6 in the Customize the GlobalProtect App . 

 You must enable intelligent portal on the portal even if you defined the
 optional key REG ADD "HKLM\Software\Palo Alto
 Networks\GlobalProtect\Settings" /v intelligent-portal /t REG_SZ /d
 yes in the Windows Registry or macOS plist. 

 The following section describes how intelligent portal works
 after it is configured. 
 When the end user logs in to the GlobalProtect app, GlobalProtect automatically
 selects the portal defined in the portal country map for that location. If there
 are multiple portals defined for a country, GlobalProtect selects the first
 portal for that country. 

 If the user manually selects a different portal for that country from the portal
 map, GlobalProtect directs the user to this portal for subsequent sessions. The
 portal is retained when the app is refreshed or the computer goes to sleep. 

 If the user manually selects a portal that isn't defined in the country map,
 this portal is retained for the session. When the GlobalProtect app is refreshed
 or the computer wakes up from sleep, GlobalProtect automatically directs them to
 the portal defined in the portal country map for that location. If there are
 multiple portals defined for that portal, GlobalProtect selects the first portal
 for that country. 

 Logs for the intelligent portal feature are included in the
 GlobalProtectLogs.tgz file. See the highlighted rows in the
 screenshot below. 

 For information on how to access the log file, see View and Collect GlobalProtect App Logs . 

 Previous 

 Define the GlobalProtect Agent Configurations 

 Next 

 Customize the GlobalProtect App

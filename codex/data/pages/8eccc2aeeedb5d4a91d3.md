---
url: https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/administration/prisma-access-mobile-users/mobile-users-globalprotect/globalprotect-app-upgrades/select-the-active-globalprotect-app-version-for-prisma-access.html
fetched_at: 2026-09-16T11:26:07Z
source: palo-alto-main
---

# Select the Active GlobalProtect App Version for Prisma Access Clear

Updated on 

 Sep 3, 2026 

 Focus 

 Home 

 Prisma Access 

 Prisma Access Administration 

 Prisma Access Mobile Users 

 Mobile Users: GlobalProtect 

 GlobalProtect App Upgrades 

 Select the Active GlobalProtect App Version for Prisma Access 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 Deutsch (German) 

 Prisma Access 

 Select the Active GlobalProtect App Version for Prisma Access 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma Access Docs 

 Release Notes 

 Select a Document 

 6.2 Preferred and Innovation 

 6.1 Preferred and Innovation 

 6.0 Preferred and Innovation 

 5.2 Preferred and Innovation 

 5.1 Preferred and Innovation 

 5.0 Preferred and Innovation 

 4.2 Preferred 

 4.1 Preferred 

 4.0 Preferred 

 3.2 Preferred and Innovation 

 Activation & Onboarding 

 Administration 

 Select a Document 

 4.0 & Later 

 Prisma Access China 

 Integrations 

 Incidents & Alerts 

 New Features 

 Previous 

 GlobalProtect App Upgrades 

 Next 

 Allow Users to Upgrade the GlobalProtect App 

 Select the Active GlobalProtect App Version for Prisma Access 

 How to select the active GlobalProtect app version in
 Prisma Access . 

 Where Can I Use
This? What Do I Need? 

 Prisma Access (Managed by Strata Cloud Manager) 

 Prisma Access (Managed by Panorama) 

 Prisma Access license 

 Prisma Access manages the GlobalProtect app version for Windows and macOS users in
 your organization. While Prisma Access hosts several GlobalProtect app versions,
 only one of the hosted versions is active. When mobile users log in to the Prisma
 Access portal, the active version is the one that is available for mobile users to
 download and install on their Windows and macOS devices. 

 You can select multiple GlobalProtect versions in a multitenant deployment . The
 GlobalProtect app version settings you apply are per tenant and not global; you
 control the app version on a per-tenant basis. 

 Some features, such as IP Optimization, require users to be on
 sufficiently updated versions of GlobalProtect. Continue reading to learn
 how to select the active GlobalProtect app version in Prisma Access . 

 Strata Cloud Manager 

 Panorama 

 Select the Active GlobalProtect App Version for Prisma Access (Managed by Strata Cloud Manager) 

 How to select the active GlobalProtect app version in Prisma Access . 

 You
can replace the current active version with another hosted version
from the Service Setup page by completing the following steps. 

 Select Configuration NGFW and Prisma Access Configuration Scope Prisma Access Mobile Users , and then locate the GlobalProtect
 Connection panel. 

 Select GlobalProtect Setup or Enable GlobalProtect Setup if
GlobalProtect is not already enabled. 

 Select the GlobalProtect App tab,
and then edit the Global App Settings . 

 On the General tab of the Global
Settings page, select the GlobalProtect App
Version you want to allow mobile users to download and
install from the Prisma Access portal. 

 The active version is indicated in the drop-down list. 

 Select the Active GlobalProtect App Version for Prisma Access (Managed by Panorama) 

 How to select the active GlobalProtect app version in Prisma Access . 

 If your currently-active version is end-of-life, Prisma Access notifies you and
 requests that you activate a supported version. 

 You
can replace the current active version with another hosted version
from the Service Setup page by completing the following steps. 

 If
you are using Prisma Access in a FedRAMP environment , you
must use the FIPS-certified version of GlobalProtect, which is version
of 5.1.4. If you change the default
GlobalProtect version from 5.1.4, you cannot select version
5.1.4 from the Panorama UI and must open a Support case with Palo
Alto Networks Technical Support to add it back. 

 Select Panorama Cloud Services Configuration Service Setup . 

 Select Activate new GlobalProtect App version . 

 The active version is indicated in the drop-down list. 

 If
your current GlobalProtect version is end-of-life (EoL), a message
displays in this area on the Service Setup page; if you receive
this message, upgrade your GlobalProtect app version by continuing
to the next step. 

 Select the version to which you want to upgrade and click OK . 

 A window displays to verify your choice. 

 After the
app has been activated, you receive a success message. 

 View the System Status page to verify the Active
GlobalProtect App version . 

 Previous 

 GlobalProtect App Upgrades 

 Next 

 Allow Users to Upgrade the GlobalProtect App

---
url: https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/administration/prisma-access-releases-and-upgrades/cadence-for-software-and-content-updates-for-prisma-access.html
fetched_at: 2026-09-16T11:25:51Z
source: palo-alto-main
---

# Cadence for Software and Content Updates for Prisma Access Clear

Updated on 

 Sep 3, 2026 

 Focus 

 Home 

 Prisma Access 

 Prisma Access Administration 

 Prisma Access Releases and Upgrades 

 Cadence for Software and Content Updates for Prisma Access 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 Deutsch (German) 

 Prisma Access 

 Cadence for Software and Content Updates for Prisma Access 

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

 Prisma Access Upgrade Types 

 Next 

 Prisma Access Dataplane Upgrades 

 Cadence for Software and Content Updates for Prisma Access 

 How often the Prisma Access components are updated, and who updates them
 (you or Palo Alto Networks). 

 Where Can I Use This? What Do I Need? 

 Prisma Access (Managed by Strata Cloud Manager) 

 Prisma Access (Managed by Panorama) 

 Prisma Access license 

 Strata Cloud Manager 

 Panorama 

 Cadence for Software and Content Updates for Prisma Access (Managed by Strata Cloud Manager) 

 Learn more about how Prisma Access updates its infrastructure components. 

 The following table describes how Prisma Access updates its infrastructure components,
 including content and software updates. This table also indicates whether Prisma Access 
 automatically updates the software. If any updates are not automatic, you can learn how
 to apply those infrastructure updates. 

 Component Update Schedule Comments 

 GlobalProtect app 

 Major GlobalProtect App Releases (for example, x .0
 or 4. x )— Prisma Access updates the app with
 the latest major release 7-10 days after the general
 availability of the x .0.1 version of that
 release. 

 For example, given an app release of 4.0, Prisma Access 
 updates the app 7-10 days after the 4.0.1 release. 

 Minor GlobalProtect App Releases (for example,
 4.1. x )— Prisma Access updates the app with
 the latest minor release 7-10 days after the general
 availability of that release. 

 The cloud controls the version of the app that is available for
 upgrade. 

 PAN-OS software upgrades in the Prisma Access 
 infrastructure—scheduled 

 Palo Alto Networks® upgrades the PAN-OS infrastructure when a new
 version of Prisma Access is released. Palo Alto Networks® provide
 you with three weeks’ notice before a scheduled upgrade. 

 Sign up to receive infrastructure upgrades by email or text
 notifications at the Hub . 

 Applications and threat
 updates 

 Daily with a threshold of 24 hours. 

 Palo Alto Networks® releases New App-IDs on the third Tuesday of
 every month. Plan to review and incorporate these new App-IDs within
 the 24 hour threshold. Use the New App-ID filter to minimize this
 possible traffic impact. 

 The New App-ID characteristic lets you see new applications on your
 network and shows you details about newly-categorized application
 activity. What you learn can help you make the right decisions about
 how you to update your security policy to enforce the most
 recently-categorized App-IDs. 

 Antivirus protection 

 Every hour, 10 minutes after the hour 

 Prisma Access is always up-to-date with the latest Antivirus
 release. 

 WildFire 

 Real-time 

 Prisma Access is always up-to-date with the latest WildFire
 release. 

 GlobalProtect Data
 File 

 Every hour 

 Prisma Access is always up-to-date with the latest GlobalProtect data
 file release. 

 Clientless VPN 

 application signatures 

 Every hour 

 Prisma Access is always up-to-date with the latest Clientless VPN
 application signature release. 

 Network Time Protocol (NTP) Dependent on the underlying cloud provider 

 Prisma Access Security Processing nodes synchronize their time
 using the underlying cloud providers' Network Time Protocol (NTP)
 addresses. You cannot configure or change NTP through Strata Cloud Manager . This is a system-level function handled by
 the Prisma Access infrastructure to ensure accurate and
 consistent timekeeping across all nodes. 

 Cadence for Software and Content Updates for Prisma Access (Managed by Panorama) 

 How often the Prisma Access components (for
a Prisma Access (Managed by Panorama) deployment) are updated, and who updates them
(you or Palo Alto Networks). 

 The following table informs you of the software and content updates to get the latest
 applications and threat signatures and leverage the threat prevention capabilities
 provided by Palo Alto Networks. If the Cloud Controlled? column
 has an attribute of No , you perform the required actions to
 update the component. 

 Component Update Schedule Cloud Controlled? (Yes/No) Comments 

 Upgrades to Panorama software for compatibility with
 Prisma Access 

 For major Prisma Access releases, you might need to upgrade your
 Panorama version for the following use cases: 

 Required Upgrade —On occasion, you will be required to
 upgrade the software version on Panorama to maintain
 compatibility with Prisma Access . 

 Maintenance Window —Your organization will need
 to schedule a maintenance window to upgrade the
 Panorama software version. 

 Impact —You cannot use the new plugin version
 until you upgrade your Panorama version. 

 Notification —Palo Alto Networks will provide
 you with a notification 100 days before the
 scheduled major release upgrade. 

 Optional Upgrade —In other cases, you might need to
 upgrade the Panorama software version to use the new
 features that Prisma Access supports in the major
 release. 

 Maintenance Window —Your organization will need
 to schedule a maintenance window to upgrade the
 Panorama software version. 

 Impact —You cannot use the new features that
 Prisma Access supports until you upgrade your
 Panorama. 

 Notification —Palo Alto Networks will notify
 you of any Panorama requirements 21 days before a
 scheduled major release upgrade as defined in Prisma Access Release Types . 

 No See End-of-Support (EoS) Dates for
 Panorama Software Version Compatibility with Prisma Access to
 learn when a Panorama version becomes incompatible with Prisma Access .
 See Prisma Access for the currently supported Panorama versions
 to use with Prisma Access . To upgrade your Panorama to a new version,
 see Install Content and Software Updates
 for Panorama . 

 Cloud Services plugin version 

 Available after the plugin release. 

 No You perform the tasks to upgrade the plugin. See Prisma Access Release Types for details about when Prisma Access updates its
 plugin version. See Upgrade the Cloud Services
 Plugin to upgrade the plugin in the Panorama appliance. 

 GlobalProtect app 

 Major GlobalProtect App Releases (for example, x .0
 or 5. x )— Prisma Access updates the agent on
 the portal with the latest major release 7-10 days after the
 general availability of the x .0.1 version of that
 release. 

 For example, given an agent release of 5.1, Prisma Access 
 updates the agent on the portal 7-10 days after the release
 of 5.1.1. 

 Minor GlobalProtect App Releases (for example,
 5.1. x )— Prisma Access updates the agent on
 the portal with the latest infrastructure maintenance 7-10
 days after the general availability of that release. 

 Yes 

 The cloud controls the versions of the app that are available for
 upgrade; however you can choose between several different hosted
 versions of the app and can control how and when to roll out
 GlobalProtect app updates to the end users. See GlobalProtect App Upgrades for details. 

 If your Prisma Access deployment requires a hotfix of the
 GlobalProtect app, open a Support Case with Palo
 Alto Networks Technical Support for assistance. 

 Applications and threat
 updates 

 Daily with a threshold of 24 hours. 

 Palo Alto Networks releases New App-IDs on the third Tuesday of every
 month. Plan to review and incorporate these new App-IDs within the
 24 hour threshold. 

 The New App-ID characteristic lets you see new applications on your
 network and shows you details about newly-categorized application
 activity. What you learn can help you make the right decisions about
 how you to update your security policy to enforce the most
 recently-categorized App-IDs. 

 Yes 

 Antivirus protection 

 Every hour, 10 minutes after the hour 

 Yes Prisma Access is always up-to-date with the latest
 Antivirus release. 

 WildFire 

 Real-Time 

 Yes Prisma Access retrieves WildFire signatures for
 newly-discovered malware as soon as the WildFire public cloud can
 generate them. 

 GlobalProtect Data
 File 

 Every hour 

 Yes Prisma Access is always up-to-date with the latest
 GlobalProtect data file release. 

 Clientless VPN application
 signatures 

 Every hour 

 Yes Prisma Access is always up-to-date with the latest
 Clientless VPN application signature release. 

 Network Time Protocol (NTP) Dependent on the underlying cloud provider Yes 

 Prisma Access Security Processing nodes synchronize their time
 using the underlying cloud providers' Network Time Protocol (NTP)
 addresses. You cannot configure or change NTP through Strata Cloud Manager . This is a system-level function handled by
 the Prisma Access infrastructure to ensure accurate and
 consistent timekeeping across all nodes. 

 Previous 

 Prisma Access Upgrade Types 

 Next 

 Prisma Access Dataplane Upgrades

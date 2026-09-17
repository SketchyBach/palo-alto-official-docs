---
url: https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/administration/prisma-access-releases-and-upgrades/cadence-for-software-and-content-updates-for-prisma-access/cadence-for-software-and-content-updates-for-prisma-access-cloud-management.html
fetched_at: 2026-09-16T11:25:51Z
source: palo-alto-main
---

# Cadence for Software and Content Updates for Prisma Access (Managed by Strata Cloud Manager) Clear

Updated on 

 Thu Sep 03 12:12:03 PDT 2026 

 Focus 

 Home 

 Prisma Access 

 Prisma Access Administration 

 Prisma Access Releases and Upgrades 

 Cadence for Software and Content Updates for Prisma Access 

 Cadence for Software and Content Updates for Prisma Access (Managed by Strata Cloud Manager) 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 Deutsch (German) 

 Prisma Access 

 Cadence for Software and Content Updates for Prisma Access (Managed by Strata Cloud Manager) 

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

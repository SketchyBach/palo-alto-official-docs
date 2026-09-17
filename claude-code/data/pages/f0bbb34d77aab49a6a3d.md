---
url: https://docs.paloaltonetworks.com/prisma-browser/administration/manage-prisma-browser-policy-profiles/configure-prisma-browser-browser-security/configure-browser-session/flush-browser-data
fetched_at: 2026-09-16T08:21:54Z
source: palo-alto-main
---

# Flush Browser Data Clear

Updated on 

 Thu Sep 10 09:47:19 PDT 2026 

 Focus 

 Home 

 Prisma Browser 

 Manage Prisma Browser Control Sets 

 Configure Prisma Browser Security Controls 

 Configure Browser Session 

 Flush Browser Data 

 Download PDF 

 Prisma Browser 

 Flush Browser Data 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma Browser Docs 

 Activation & Onboarding 

 Getting Started 

 Deployment 

 Administration 

 Integrations 

 User Guide 

 Previous 

 Browser Lock 

 Next 

 Concurrent Number of Devices 

 Flush Browser Data 

 Flush browser data mm 

 Prisma Browser Desktop Prisma Browser Extension Prisma Browser for Mobile 

 Full support No support Partial support 

 Not all attributes are supported 

 This policy creates temporary browser sessions. This means that browser data will be
 cleared upon close, or after a configured time period. 

 The Prisma Browser for Mobile supports flushing data when
 the browser closes. Configuring periodic flushing on the mobile browser will have no
 impact. 

 From Strata Cloud Manager , select Configuration Policy Control Sets Browser Security Browser Session 

 Select Flush Browser Data . 

 Select one of the following options: 

 Enable - the Prisma Browser flush the browser
 data. 

 Select the attributes to clear: 

 Browsing history 

 Download history 

 Cookies and other site data 

 Cached images and files 

 Passwords and Passkeys 

 Autofill 

 Site settings. 

 Host app data 

 Select the trigger for the browser flush action: 

 Browser close - the data will be
 flushed when the browser is closed. 

 Time period - the data will be
 flushed after the configured time elapsed. If this
 option is selected, you can set the flush time from
 1-24 hours. 

 Disable – disable the Browser flush feature. 

 Click Set . 

 i 

 Previous 

 Browser Lock 

 Next 

 Concurrent Number of Devices

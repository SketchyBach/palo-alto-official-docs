---
url: https://docs.paloaltonetworks.com/autonomous-dem/administration/get-started-with-adem/adem-monitoring-and-tests/manage-autonomous-dem/manage-adem-mobile-users
fetched_at: 2026-08-13T15:29:21Z
source: palo-alto-main
---

# Mobile Users Clear

Mobile Users 

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

 Mobile Users 

 Updated on 

 Wed Aug 12 08:13:05 PDT 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Autonomous DEM Docs 

 Activation & Onboarding 

 Administration 

 Select a Document 

 AI-Powered ADEM 

 Autonomous DEM for China 

 User Guide 

 Release Notes 

 New Features 

 Updated on 

 Wed Aug 12 08:13:05 PDT 2026 

 Focus 

 Home 

 Autonomous DEM 

 Get Started with Autonomous DEM 

 Monitor Application Experience with Application Tests 

 Assign Application Tests to Monitor Application Experience 

 Mobile Users 

 Download PDF 

 Autonomous DEM 

 Mobile Users 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Autonomous DEM Docs 

 Activation & Onboarding 

 Administration 

 Select a Document 

 AI-Powered ADEM 

 Autonomous DEM for China 

 User Guide 

 Release Notes 

 New Features 

 Mobile Users 

 Learn how to monitor and manage your registered Autonomous DEM mobile
 users. 

 Use the following steps to begin monitoring
your mobile users’ digital experiences with ADEM: 

 Enable ADEM for your Prisma Access 
 mobile users. 

 ADEM is supported for your Prisma Access mobile users with Windows or
 MacOS endpoints running GlobalProtect version 5.2.11 or later. 

 After you enable ADEM for a user, the ADEM configuration will be pushed to
 the GlobalProtect app the next time the user connects and the app will
 register with the ADEM service. 

 To see all registered ADEM users, from the Prisma Access app on the
 hub: 

 Select System Settings Application Experience Application Experience Agent Management . 

 This tab shows all registered ADEM users and indicates whether the user is
 online (the user device is sending keep-alive messages to the ADEM service)
 or offline (the ADEM service has not received a keep-alive message from the
 user device in the last ten minutes), when the user device was last seen,
 the username, device type, and hostname of the ADEM user, and what ADEM
 agent version they are running. 

 Assign app tests to your registered ADEM users and remote sites. 

 When you create a new app test, you can assign it to ADEM
remote sites or all registered ADEM users (default) or choose specific
users to assign a test to, or you can assign the tests to both remote
sites and users. If you have already created a test to be assigned
to all registered ADEM users, any tests will automatically start running
on an endpoint as soon as it registers with ADEM. Once a test is
started on an endpoint, it will send metrics from the app test to
the ADEM service every five minutes. 

 To temporarily stop an endpoint from running assigned
app tests, select the user for whom you want to suspend app tests
and toggle the Monitoring State . 

 Note that if you disable monitoring, the user is still
counted as a licensed ADEM user. 

 To unregister an endpoint from ADEM, select the row for the endpoint to be
 removed in the table and then click the trash can icon in the
 Action column. 

 Deleting a user frees up an ADEM license. 

 On This Page 

 Activation & Onboarding 

 Strata Cloud Manager 

 Activate a License or Product 

 Cloud Identity Engine 

 Strata Logging Service 

 Device Associations 

 Hub 

 Identity and Access Management 

 Tenant Management 

 SASE 

 Prisma Access 

 Strata Multitenant Cloud Manager 

 AI-Powered ADEM 

 Prisma Access Monitoring and Visibility 

 Prisma SD-WAN 

 ION Devices 

 Next-Generation CASB 

 Visibility & Monitoring 

 Dashboards 

 Incidents and Alerts 

 Reports 

 SASE 

 Administration 

 Autonomous DEM 

 Prisma SASE 

 Strata Cloud Manager 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

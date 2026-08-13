---
url: https://docs.paloaltonetworks.com/fedramp/autonomous-dem/manage-autonomous-dem/manage-adem-mobile-users
fetched_at: 2026-08-13T16:32:37Z
source: palo-alto-main
---

# Manage Autonomous DEM Mobile Users Clear

Manage Autonomous DEM Mobile Users 

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

 Manage Autonomous DEM Mobile Users 

 Updated on 

 Wed Sep 04 15:52:49 PDT 2024 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 FedRAMP Docs 

 Reference 

 Autonomous DEM 

 Updated on 

 Wed Sep 04 15:52:49 PDT 2024 

 Focus 

 Home 

 FedRAMP 

 Manage Autonomous DEM 

 Manage Autonomous DEM Mobile Users 

 Download PDF 

 FedRAMP 

 Manage Autonomous DEM Mobile Users 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 FedRAMP Docs 

 Reference 

 Autonomous DEM 

 Previous 

 Manage Autonomous DEM 

 Next 

 Manage Autonomous DEM Remote Sites 

 Manage Autonomous DEM Mobile Users 

 Learn how to monitor and manage your registered Autonomous
DEM mobile users. 

 Use the following steps to begin monitoring
your mobile users’ digital experiences with ADEM: 

 Enable ADEM for your Prisma Access mobile users. 

 ADEM is supported for your Prisma Access mobile users with
Windows or MacOS endpoints running GlobalProtect version 5.2.11
or later. 

 The steps for enabling ADEM for your users depends
on if you are using Panorama Managed Prisma
Access or Cloud Managed Prisma
Access . After you enable ADEM for a user, the ADEM configuration
will be pushed to the GlobalProtect app the next time the user connects
and the app will register with the ADEM service. 

 To see all registered ADEM users, from the Prisma Access
app on the hub: 

 Select Autonomous DEM Settings Endpoint Agent Management . 

 This
tab shows all registered ADEM users and indicates whether the user
is online (the user device is sending keep-alive messages to the
ADEM service) or offline (the ADEM service has not received a keep-alive
message from the user device in the last ten minutes), when the
user device was last seen, the username, device type, and hostname
of the ADEM user, and what ADEM agent version they are running. 

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

 To unregister an endpoint from ADEM, select the row for
the endpoint to be removed in the table and then click the trash
can icon in the Action column. Unregistering
an endpoint does not free up an ADEM license. 

 Unregistering a user frees up an ADEM license. 

 To set the upgrade preferences for all the users, click Upgrade
Now or Auto Upgrade from the Upgrade
Options menu. 

 Previous 

 Manage Autonomous DEM 

 Next 

 Manage Autonomous DEM Remote Sites 

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

 Prisma Access Monitoring and Visibility 

 Prisma SD-WAN 

 Cloud-Delivered Security Services 

 Advanced WildFire 

 Advanced URL Filtering 

 Advanced Threat Prevention 

 Advanced DNS Security 

 Device Security 

 Enterprise DLP 

 SaaS Security 

 Network Security 

 Shared Policy for NGFWs and Prisma Access 

 Mobile Users 

 Autonomous DEM 

 SASE 

 Prisma SASE 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

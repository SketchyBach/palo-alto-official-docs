---
url: https://docs.paloaltonetworks.com/autonomous-dem/administration/get-started-with-adem/adem-monitoring-and-tests
fetched_at: 2026-08-13T15:29:18Z
source: palo-alto-main
---

# Monitor Application Experience with Application Tests Clear

Monitor Application Experience with Application Tests 

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

 Monitor Application Experience with Application Tests 

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

 Download PDF 

 Autonomous DEM 

 Monitor Application Experience with Application Tests 

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

 Previous 

 ADEM Deployment Best Practices 

 Next 

 Create an Application Test to Monitor Mobile User Experience 

 Monitor Application Experience with Application Tests 

 Create synthetic tests originating from an application to one or more targets.
 You can create only one test per application, but an app test can have multiple
 targets. 

 Where Can I Use This? What Do I Need? 

 Prisma Access (Managed by Strata Cloud Manager) 

 Prisma Access (Managed by Panorama) 

 Prisma Access license 

 ADEM or Strata Cloud Manager Pro 
 license 

 One of the monitoring techniques that ADEM uses is application tests. Application tests allow ADEM to baseline end-to-end user experience
 regardless of whether users access an application. You can create
 application tests that simulate the monitoring done by ADEM . An application can have only one app
 test associated with it, but that app test can monitor multiple
 targets. 

 Web and path tests will be enabled by default for pre-defined tests. 

 Creating Application Tests for Mobile Users and Mobile User
 Groups 

 When creating application tests, you have the option to enable the test
 on an individual Mobile User, a Mobile User group, or both. You can
 enable application tests for user groups that are already part of
 Prisma Access Configuration (for example, GlobalProtect
 configuration or security policies). 

 Keep the following points about Mobile User Group application tests in
 mind: 

 The tests that you enable on a user group will run on all
 devices that belong to every single user in that group. 

 If a user is removed from a user group, the tests will
 automatically stop running on the user's devices. 

 When new users are added to a group, the tests automatically
 begin running on the new users' devices. However, it may
 take up to 6 hours to automatically update users that are
 added/removed from groups. 

 If an application test is modified or created, changes made to
 the user group are automatically reflected. 

 The user groups that belong to Cloud Identity Engine (CIE) and
 Firewalls are displayed here. In case of duplicate user
 group entry, CIE group takes precedence. 

 You can filter the test results by individual Mobile Users or Mobile User
 groups (only groups currently in test configuration). 

 Security Policy Rules for Application Testing 

 In order to run synthetic tests—to SaaS applications or applications in
 your data center through Prisma Access , Secure Fabric, via split
 tunneling—you must have security policy rules that allow the
 synthetic test traffic over ICMP, TCP, HTTPS, and optionally HTTP
 (depending on how you configure your app tests). 

 Previous 

 ADEM Deployment Best Practices 

 Next 

 Create an Application Test to Monitor Mobile User Experience 

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

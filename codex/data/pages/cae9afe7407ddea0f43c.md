---
url: https://docs.paloaltonetworks.com/autonomous-dem/release-notes/ai-powered-adem-release-notes/release-updates-release-notes-doc/known-issues-adem
fetched_at: 2026-08-13T15:26:56Z
source: palo-alto-main
---

# Known Issues— ADEM Agent for Mobile Users  Clear

Known Issues— ADEM Agent for Mobile Users 

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

 Known Issues— ADEM Agent for Mobile Users 

 Updated on 

 Fri Jul 17 06:27:09 PDT 2026 

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

 Fri Jul 17 06:27:09 PDT 2026 

 Focus 

 Home 

 Autonomous DEM 

 AI-Powered Autonomous DEM Release Notes 

 Release Updates 

 Known Issues— ADEM Agent for Mobile Users 

 Download PDF 

 Autonomous DEM 

 Known Issues— ADEM Agent for Mobile Users 

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

 What’s New—Autonomous DEM 

 Next 

 Known Issues— ADEM Agent for Prisma SD-WAN Remote Sites 

 Known Issues— ADEM Agent for Mobile Users 

 Review the open issues in Mobile User Autonomous Digital Experience Management (ADEM)
 agent. 

 Where Can I Use This? What Do I Need? 

 Prisma Access (Managed by Strata Cloud Manager) 

 Prisma Access (Managed by Panorama) 

 Prisma Access license 

 ADEM or Strata Cloud Manager Pro 
 license 

 GlobalProtect or Prisma Access Agent license 

 Here are the issues we’re currently working on. 

 Autonomous DEM Agent 5.10 

 ID Description 

 DEM-12373 On the Access Experience page, agents with
 versions below 5.0 incorrectly show a status of Scheduled 
 instead of Manual Upgrade when Canary Upgrade is configured;
 as agent below 5.0 are not eligible for Canary Upgrade. 
 Work
 Around : Upgrade the ADEM agent to version 5.0 or later
 to be eligible for canary upgrades. For agents running versions
 earlier than 5.0, perform a manual upgrade. 

 DEM-12771 New users registering after the Canary period incorrectly default
 to No Upgrades Planned instead of automatically moving to the
 Scheduled state for global upgrades. 

 Autonomous DEM Agent 5.9 

 ID Description 

 DEM-12332 When you enable the Application Security feature, the
 path visualization sometimes displays incorrect hop data for
 specific time intervals. 

 Autonomous DEM Agent 5.7 

 ID Description 

 DEM-10992 

 ADEM 5.7.x agent is compatible only with GlobalProtect 6.3.3 when
 the direct local network access is blocked in the GlobalProtect
 app. With blocked access to the local network, if you install
 ADEM 5.7.x agent in GlobalProtect 6.3.2 or below, GlobalProtect
 downgrades and breaks the ADEM agent. 

 Workaround : To fix the issue, upgrade GlobalProtect to
 version 6.3.3 and manually reinstall the ADEM 5.7.x agent. Hence
 it is recommended not to install ADEM 5.7.x agent in
 GlobalProtect 6.3.2 and below if you want to collect LAN metrics
 when local network access is blocked. 

 DEM-11093 In the Path visualization widget, the GlobalProtect
 device icon incorrectly shows an empty connected state for
 Proxy-only mode, whereas the expected state is Disconnected. 

 Autonomous DEM Agent 5.6 

 ID Description 

 DEM-10460 Multiple hostnames may be displayed for Windows
 computers. 

 DEM-9586 The device icon under the path to a domain appears
 greyed out in the interface, which may cause confusion when
 attempting to trace network paths. 
 Workaround : Wait 10–15
 minutes after the agent and browser session initialize. Once
 both data streams are consistently running, the RUM and
 Synthetic data joins and the Device icon populates
 automatically. 

 DEM-9703 When viewing Application Performance Metrics, the PAB
 version information is not displayed under Browser Type, making it
 difficult to identify which browser versions are being used. 

 DEM-10079 For GlobalProtect (GP) users, you may observe that
 user devices are not properly displaying all connected devices under
 the User Page. 

 DEM-10108 Proxy-only users on Windows systems are not properly
 updated in the ADEM portal under the Users page. 

 DEM-10242 The RUM extension currently has limited logging
 capabilities. An enhancement to add configurable Log Level settings
 is in development, which will improve troubleshooting capabilities
 in future releases. 

 DEM-10410 You may notice duplicate hostname displays for a
 single Windows endpoint machine, which can lead to confusion when
 identifying specific devices in your environment. 

 Autonomous DEM Agent 5.4 

 ID Description 

 DEM-9183 

 If you had application tests configured before the UI
 change that occurred in December 2024, the Advanced Options Remote Sites Test Options Application Entities field in app test configuration appears to be
 ANY , but in the backend, its value is the
 App-ID of the app test target. 
 Workaround : To actually
 choose ANY , select
 ANY from the dropdown and
 Save the test. 

 Failure to do this could
 result in the app test not working because, on devices running
 ION 6.4.2 or later, the test will run only if you've configured
 an SD-WAN path policy rule for the application test
 target. 

 DEM-9034 In 
 Insights SASE Health , the number of users that appears next to a segment,
 such as LAN, does not match the number of users with degraded
 experience that you see after you select the user count. 

 DEM-8709 If you're collecting both Real User Monitoring (RUM)
 and synthetic test data, you may experience up to a 40-minute delay
 before you see combined results in ADEM 
 dashboards. 

 DEM-8366 

 Under Insights SASE Health Monitored Applications , when Proxy alone is deployed in a particular
 Prisma Access Location, we do not observe that location and its
 details on the Monitored Applications map. 

 DEM-7548 

 The Apple macOS Sequoia 15+ version affects ADEM Agent
 installations as follows: 

 Fresh installations of ADEM Agents with version 5.4 and
 higher will be successfully installed on macOS 15 and
 higher. 

 Fresh installations of ADEM Agents with version 5.4 or lower
 on macOS 15+ will fail. Because current GlobalProtect
 versions bundle ADEM Agents with version 5.4 and lower,
 admins need to install the latest ADEM
 Agent version manually . 

 ADEM Agents already installed on earlier versions of macOS
 will upgrade successfully to the latest version and continue
 to function normally. 

 DEM-4686 

 ADEM may not be able to identify every problem that may impact a
 user's calls. For example, WiFi disconnect will impact a Zoom
 meeting, but will also stop ADEM synthetic tests. As a result,
 the Number of minutes with issues field
 in the Overall Zoom Performance Impact 
 widget and the Impacted Minutes field of
 the Zoom Poor Performance Root Cuases 
 widget may not match. 

 DEM-3992 

 The ADEM dashboard may list one or more user specific attributes
 for multiple clients. For example, the user location or the
 hostname may reflect the same value for multiple users. This
 happens if their Windows GUID is identical. 

 Make sure the Windows GUID is unique for all the machines. Then
 reinstall the agent to get the correct status updated. 

 DEM-3873 

 After the ADEM license expires, the Self-Serve feature will
 continue to work for a grace period of 30 days. At the end of
 the 30-day grace period, the notifications get disabled on both
 Macintosh and Windows. On Macintosh, if you click the
 Application Experience menu bar icon,
 the UI will open and notify you that the notifications are
 disabled. On Windows, the Application
 Experience icon in the task bar gets removed.

 DEM-3798 

 Users receive the Self-Serve notifications regardless of whether
 they are online or offline. If and when a user's device gets
 disconnected from the ADEM portal (the device goes offline),
 users will continue to receive Self-Serve notifications on their
 device during the period that the device is offline. However,
 the notification count will not get updated on the ADEM portal.

 DEM-3139 

 If a user belongs to multiple user groups, then The
 Mobile Users Group filter on the
 Applications page returns
 applications assigned to all groups that the user belongs to,
 not just the selected group in the filter. 

 DEM-3066 

 When ADEM is accessed from the Prisma Access App, only those
 security groups currently used in one or more security policies
 are displayed. On Panorama LDAP, all user groups are
 displayed. 

 DEM-2834 If you make a modification to the application test
 configuration, you may see data gaps of 5 mins interval on the
 application experience trend and performance metrics chart for the
 remote site. 

 DEM-2815 

 The application score that is displayed on the "Global
 Distribution of Application Experience Scores for Remote Sites"
 does not match the score on the Remote Sites page. The first
 score is an average score filtered by location. The second score
 (Remote Sites) is an average of the average score for each
 remote site. 

 DEM-2777 

 Any ADEM license changes for Remote Networks (For example, SPN
 bandwidth allocations) can take between 1 to 4 hours to reflect
 in the UI. 

 DEM-2717 

 When logging into ADEM as a Data Security Manager, the page fails
 to load displaying the following error:“Maximum update depth
 exceeded. This can happen when a component repeatedly calls
 setState inside componentWillUpdate or componentDidUpdate. React
 limits the number of nested updates to prevent infinite
 loops.” 

 DEM-183 

 When you install GlobalProtect app 5.2.6 on macOS devices, the
 pop-up prompt appears, prompting end users for administrative
 privileges to modify system settings. 

 Workaround : Select OK so that the
 pop-up prompt does not appear again. 

 DEM-105 

 Autonomous DEM does not run network performance tests to the
 service connection, and hence the network performance metrics
 are not measured for service connections. The service connection
 is included when tracing the network path from the endpoint to
 the application. 

 NETVIS-3095 In Insights Activity Insights Users Agent Users or Insights Activity Insights Users PAB Users when you Add Filter , the data
 in the Access Agent Users table may not match that which is in the
 Monitored Users widget. For example, if the table shows a user
 device with poor experience, the widget may not reflect that in the
 count of user devices with poor experience. 

 Previous 

 What’s New—Autonomous DEM 

 Next 

 Known Issues— ADEM Agent for Prisma SD-WAN Remote Sites 

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

 Release Notes 

 Autonomous DEM 

 Prisma SASE 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

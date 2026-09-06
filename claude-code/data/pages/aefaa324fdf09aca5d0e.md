---
url: https://cortex-docs.paloaltonetworks.com/xsoar-6-administrator-guide/6.14/customize-cortex-xsoar/customize-and-configure-cortex-xsoar/incidents/incident-lifecycle/receive-notification-on-an-incident-fetch-error
fetched_at: 2026-09-06T10:41:07Z
source: cortex-platform
---

# Receive Notification on an Incident Fetch Error | 6.14 | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSOAR 6 

 Cortex XSOAR 6 Administrator Guides 

 6.14 

 Customize Cortex XSOAR 

 Customize and Configure Cortex XSOAR 

 Incidents 

 Incident Lifecycle 

 Cortex XSOAR 6.14 

 Receive Notification on an Incident Fetch Error 

 Configure Cortex XSOAR 6.14 notifications for incident fetch errors. 

 The administrator and Cortex XSOAR users on the recipient’s list receive a notification when an integration experiences an incident fetch error, which occurs for a state transition from Success to Failure during an incident fetch. 

 Important 

 Because notifications are triggered only by the state transition, you will not receive an alert if: 

 A new integration instance fails its first fetch attempt (since a successful fetch has not yet occurred). 

 You force a fetch failure for testing purposes before a successful fetch has occurred. 

 Cortex XSOAR users can select their notification method, such as email, from their user preferences. Administrators with multiple instances of mail sender can choose to receive one email notification instead of multiple email notifications. 

 Note 

 The connectivity behavior that exists between third-party applications may trigger a fetch failure, which will send a notification to an administrator and users. If the fetch operates correctly just after the notification was sent, the notification may no longer be relevant. 

 Before you begin 

 In the integration instance, ensure that you select the Fetch Incidents checkbox. 

 Select Settings → About → Troubleshooting → Add Server Configuration . 

 Add the following keys and values: 

 Key 

 Value 

 module.health.notification.users 

 List of names in CSV format, for example user1,user2,user3 . 

 message.ignore.failedFetchIncidents 

 false . 

 (Optional) Administrators that have multiple instances of a mail sender configured that want to receive only one email notification should select the Do not use by default option in the integration instances that should not be used to send emails. 

 Previous Fetch Incidents From an Integration Instance 

 Next Incident Context Data 

 Last updated 4 days ago 

 Was this helpful?

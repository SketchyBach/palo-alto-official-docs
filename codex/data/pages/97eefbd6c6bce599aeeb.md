---
url: https://cortex-docs.paloaltonetworks.com/cortex-xdr-5.x/detect-investigate-and-respond-to-threats/monitor-dashboards-and-reports/manage-dashboards-and-reports/configure-the-notification-rule-for-a-failed-report
fetched_at: 2026-09-16T08:42:50Z
source: cortex-platform
---

# Configure the notification rule for a failed report | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XDR 

 Cortex XDR 5.x Documentation 

 Detect, investigate, and respond to threats 

 Monitor dashboards and reports 

 Manage dashboards and reports 

 Cortex XDR 5.x 

 Configure the notification rule for a failed report 

 Get notified when a scheduled report fails. 

 You can receive an email or send a notification to a syslog server if a report fails to run due to a timeout or fails to upload to the GCP bucket. 

 Under Settings → Configurations → General → Notifications , click Add Forwarding Configuration . 

 Enter a name and a description for your rule, and under Log Type , select Management Audit Logs . 

 Use a filter to select the Type as Reporting, Subtype as Run Report, and Result as Fail. 

 Enter a distribution list to receive notifications by email or select a syslog server. 

 Click Next . 

 Review settings and click Create . 

 Previous Import and export dashboards and report templates 

 Next Deleted content 

 Last updated 1 month ago 

 Was this helpful?

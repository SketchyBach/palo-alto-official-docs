---
url: https://docs.prismacloud.io/content-collections/alerts/alert-notifications-state-changes
fetched_at: 2026-09-16T13:35:06Z
source: prisma-cloud
---

# Alert Notifications on State Change | Prisma Cloud arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Enterprise Edition 

 Content Collections 

 Alerts 

 Alert Notifications on State Change 

 Learn whether you can enable alert notifications to an external integration when an alert status is updated. 

 The following table provides an overview of how Prisma Cloud sends alerts for all states. By default, alert notifications are sent for the Open state only. 

 Integrations 

 Alert Status 

 Open 

 Dismissed 

 Snoozed 

 Resolved 

 Amazon SQS 

 Yes 

 Yes 

 Yes 

 Yes 

 Amazon S3 

 Yes 

 Yes 

 Yes 

 Yes 

 Email 

 Yes 

 Yes 

 Yes 

 Yes 

 ServiceNow 

 Yes 

 Yes 

 Yes 

 Yes 

 Slack 

 Yes 

 Yes 

 Yes 

 Yes 

 Splunk 

 Yes 

 Yes 

 Yes 

 Yes 

 Cortex XSOAR 

 Yes 

 No 

 No 

 No 

 Jira 

 Yes 

 No 

 No 

 Yes 

 Microsoft Teams 

 Yes 

 Yes 

 Yes 

 Yes 

 AWS Security Hub 

 Yes 

 Yes 

 Yes 

 Yes 

 Google Cloud SCC 

 Yes 

 Yes 

 Yes 

 Yes 

 PagerDuty 

 Yes 

 Yes 

 Yes 

 Yes 

 Azure Service Bus Queue 

 Yes 

 Yes 

 Yes 

 Yes 

 Webhooks 

 Yes 

 Yes 

 Yes 

 Yes 

 Alert notifications are sent for Resolved issues when you perform the following actions: 

 Policy is disabled—Yes 

 Policy is deleted—Yes 

 Alert rule is disabled—Yes 

 Alert rule is updated and the policy that triggered the alert is removed—Yes 

 Alert rule is deleted—No 

 Resource is updated and the policy violation is addressed when the next scan occurs—Yes 

 Resource is deleted and the next scan discovers that this is no longer an issue—Yes 

 In some cases, when you perform two actions in quick succession and a race condition occurs you may not receive notifications for the state change. For example: 

 When an alert is associated with multiple alert rules, and the alert rules are disabled sequentially, you may not receive resolve notification on all the alert rules. It will be sent out to the last alert rule against which the alert was resolved. 

 When you update an alert rule to remove a policy and also disable or delete the policy, you may not receive the resolve notification. 

 Previous Prisma Cloud Alert Status Reasons 

 Next Create Saved Views 

 Last updated 3 months ago 

 Was this helpful?

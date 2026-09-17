---
url: https://docs.prismacloud.io/content-collections/alerts/prisma-cloud-alert-status-reasons
fetched_at: 2026-09-16T13:35:06Z
source: prisma-cloud
---

# Prisma Cloud Alert Status Reasons | Prisma Cloud arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Enterprise Edition 

 Content Collections 

 Alerts 

 Prisma Cloud Alert Status Reasons 

 Review the different reasons on why an alert is in the Open or Resolved status on Prisma Cloud. 

 When an open alert is resolved, the reason is included to help with audits. The reason is displayed in the response object in the API and on the Prisma Cloud administrative console on Alerts > Overview when you select a resolved alert and review the alert details for the violating resource. 

 Some common reasons listed in the below table are also applicable for when an alert is newly opened or re-opened from the resolved status. 

 Reason 

 Details 

 ACCOUNT_DELETED 

 Account was deleted. When a cloud account that was being monitored on Prisma Cloud is deleted, all alerts are resolved with the resolution reason Account Deleted and the alerts are permanently deleted if the account is not added back within 24 hours. This status is sent with the alert payload to external integrations that you have configured. 

 ACCOUNT_GROUP_UPDATED 

 Account group was updated. 

 ACCOUNT_GROUP_DELETED 

 Account group was deleted. 

 ALERT_RULE_DISABLED 

 Alert rule was disabled. 

 ALERT_RULE_UPDATED 

 Alert rule was updated. The list of policies included in the rule, account groups being scanned, or cloud regions may have been modified. 

 ALERT_RULE_DELETED 

 Alert rule was deleted. 

 ANOMALY_CONFIG_CHANGED 

 Anomaly policy configuration changed. 

 MDC_REOPEN_FOR_ACCIDENTAL_DELETE 

 Alert was reopened during ingestion beacuse a resource was rediscovered. 

 NEW_ALERT 

 A new alert was generated. 

 POLICY_UPDATED 

 Policy was updated. If an alert is resolved, this reason indicates a change in the policy RQL that results in a resource not being in scope for the policy evaluation. If the alert is in open status, this reason indicates that a policy update resulted in a resource being in the scope of the policy evaluation and failed the evaluation. 

 POLICY_DISABLED 

 Policy was disabled. 

 POLICY_DELETED 

 Policy was deleted. 

 REMEDIATED 

 Alert was successfully remediated using the Cloud Service Provider CLI, either manually or by auto-remediation. 

 RESOURCE_DELETED 

 Resource was deleted. 

 RESOURCE_UPDATED 

 Resource was updated (based on the JSON metadata). This status indicates that a change was detected in one of the clauses included in a single or join policy statement within the policy RQL. If the alert is now in the resolved status, this reason indicates that the policy violation is no longer valid due to an update to the underlying resource. If the alert is in the open status, this reason indicates that the policy violation is now valid due to an update to the underlying resource. 

 RESOURCE_POLICY_RESCOPED 

 Alert was resolved because the policy was updated and the violating resource is no longer scanned or within the scope of the modified policy. 

 SNOOZED_AUTO_REOPEN 

 Snooze time expired for the alert and it was automatically reopened. 

 USER_DISMISSED 

 Alert was dismissed or snoozed by a Prisma Cloud administrator or by a user with the role of System Admin, Account Group Admin, or Account and Cloud Provisioning Admin. 

 USER_REOPENED 

 A dismissed or snoozed alert was reopened by a Prisma Cloud administrator or by a user with the role of System Admin, Account Group Admin, or Account and Cloud Provisioning Admin. 

 Previous Suppress Alerts for Prisma Cloud Anomaly Policies 

 Next Alert Notifications on State Change 

 Last updated 3 months ago 

 Was this helpful?

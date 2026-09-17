---
url: https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/post-deployment-steps/set-up-your-environment/data-and-log-forwarding/forward-logs-and-data-from-cortex-cloud-to-external-services/configure-notification-forwarding
fetched_at: 2026-09-16T08:46:53Z
source: cortex-platform
---

# Configure notification forwarding | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex Cloud 

 Cortex CLOUD Posture Management 

 onboard and configure 

 Post-deployment steps 

 Set up your environment 

 Data and log forwarding 

 Forward logs and data from Cortex Cloud to external services 

 Cortex Cloud Posture 

 Configure notification forwarding 

 Configure where Cortex Cloud forwards notifications. 

 After you integrate with an external service such as Slack, a syslog server, Amazon S3, Amazon SQS, Webhook, or Splunk, create a forwarding configuration that specifies the data or log type you want to forward. You can configure notifications for issues, cases, and logs. To send reports to email or Slack, see Run or schedule reports. 

 Prerequisite 

 Before you can select an external service for notification forwarding, you must integrate the external service with Cortex Cloud. For more information, see Configure external applications for forwarding . No prior configuration is required to send data to an email distribution list. 

 How to configure notifications 

 Select Settings → Configurations → General → Notifications → Add Forwarding Configuration . 

 Enter a name for the configuration. 

 Select the data or log type you want to forward: 

 Issues: Send notifications for specific issue types. 

 Note 

 Forwarding destinations : Only issues and cases can be forwarded to Slack, Splunk, Amazon SQS, Amazon S3, or Webhook. 

 Notification forwarding by domain : To configure notification forwarding for issues by domain, select Issues and filter the Issues table by Issue Domain . 

 Alert vs. issue format : By default, new configurations use the issue format, but you can select the alert format if needed, when forwarding to email, Slack, or a syslog server. You cannot forward issues in the alert format to Splunk, Amazon SQS, Amazon S3, or Webhook. 

 Existing legacy configurations are not automatically updated and continue to send notifications in the alert format. To use the issue format, edit the existing configuration. 

 Agent Audit Logs: Send notifications for audit logs reported by your Cortex XDR agents. 

 Management Audit Logs: Send notifications for audit logs about events related to your Cortex Cloud tenant. 

 Cases —Send notifications for specific cases. 

 Note 

 Not all data and log types can be sent to all external services. For more information, see Forward logs and data from Cortex Cloud to external services . 

 (Optional) Enter a description of the forwarding configuration. 

 Click Next , and under Scope , filter which issues, cases, or logs you want included in a notification. 

 For example, for a filter set to Severity = Medium, Category = Configuration , Cortex Cloud sends the issues or events matching this filter as a notification. 

 Click Next . 

 Select email or the external service you want to forward to. 

 Email (Issues, cases, logs) 

 Enable the email option and click Email to expand the form. 

 Enter the email address for your Distribution List . 

 For issue forwarding, you can define the Grouping Timeframe , which is the time frame, in minutes, to specify how often Cortex Cloud sends notifications. Every 20 issues aggregated within this time frame are sent together in one notification, sorted according to severity. To send a notification when one issue is generated, set the time frame to 0 . The grouping time frame for case and management audit log is 10 minutes and cannot be modified. 

 (Optional) Define your email configuration: 

 In the Distribution List , add the email addresses to which you want to send email notifications. 

 Choose whether you want Cortex Cloud to provide an auto-generated subject. 

 Choose the format you want to send the email. If you choose Alert , you can choose the Standard or Legacy format. For more information about the legacy format, see Log format for IOC and BIOC issues . 

 Choose whether you want Cortex Cloud to provide an auto-generated subject or enter your own subject. 

 By default, data is sent in the issue format. You can also choose Alert format, Standard or Legacy . For more information about the legacy format, see Log format for IOC and BIOC issues . 

 The Grouping Timeframe defines the time frame, in minutes, of how often Cortex Cloud sends notifications. Every 20 issues or 20 events aggregated within this time frame are sent together in one notification, sorted according to severity. To send a notification when one issue or event is generated, set the time frame to 0 . 

 Syslog server (Issues, logs) 

 Enable the Syslog option and click Syslog to expand the form. 

 Select a syslog receiver. Cortex Cloud displays the list of receivers integrated with your Cortex Cloud tenant. 

 Choose the format you want to send the syslog. If you choose Alert , you can choose the Standard or Legacy format. For more information about the legacy format, see Log format for IOC and BIOC issues . 

 Slack (Issues, cases) 

 Enable the Slack option and click Slack to expand the form. 

 Enter the Slack channel name and select from the list of available channels. Slack channels are managed independently of Cortex Cloud in your Slack workspace. After integrating your Slack account with your Cortex Cloud tenant, Cortex Cloud displays a list of specific Slack channels associated with the integrated Slack workspace. 

 Choose the format you want to send the syslog. If you choose Alert , you can choose the Standard or Legacy format. For more information about the legacy format, see Log format for IOC and BIOC issues . 

 Amazon S3, Amazon SQS, Splunk, or Webhook (Issues, cases) 

 Enable the Amazon S3, Amazon SQS, Splunk, or Webhook option and click to expand the form. 

 Select the instance name. 

 Click Next . 

 Review the forwarding configuration and click Create . 

 Previous Integrate Slack for outbound notifications 

 Next Set up email notifications for tenant updates 

 Last updated 1 month ago 

 Was this helpful?

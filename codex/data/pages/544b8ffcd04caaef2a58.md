---
url: https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cases-and-issues/investigation-and-response/investigate-issues/issue-syncing
fetched_at: 2026-09-16T08:47:14Z
source: cortex-platform
---

# Issue syncing | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex Cloud 

 Cortex CLOUD Posture Management 

 Cases and issues 

 Investigation and response 

 Investigate issues 

 Cortex Cloud Posture 

 Issue syncing 

 Configure and monitor synchronization of issues with external systems. 

 You can set up integrations that mirror Cortex issues with external applications, such as Atlassian Jira or ServiceNow. When mirroring issues, also referred to as issue syncing, you can make changes in an external application that will be reflected in the platform, and vice versa. 

 If an issue is mirrored with an external application, you have the following options: 

 Link the ticket to the issue: If an issue is linked to a ticket, the ticket number is displayed in the Overview section of the issue card. You see details about the status of the ticket by clicking on the ticket number. 

 Sync changes between the issue and the ticket: If an issue is synced to a ticket, changes are synchronized in an outbound, inbound, or bi-directional flow. 

 Note 

 Multiple tickets can be linked to an issue with outbound syncing. Issues with inbound syncing can be linked to a single ticket only. 

 Set up an external integration to sync with issues 

 Before you can sync issues with external applications, you must set up and configure your integration instance. Complete the following steps: 

 1 

 Install the content pack. 

 Install the relevant content pack, for example Atlassian Jira or ServiceNow: 

 To install from the Data Sources & Integrations page: Navigate to Settings → Data Sources & Integrations , click + Add New , and search for the relevant content pack. 

 To install from Marketplace : Navigate to Settings → Configurations → Marketplace . and browse for the relevant content pack. 

 2 

 Connect an integration instance. 

 Navigate to Settings → Data Sources & Integrations . 

 Search for the relevant data source (for example Atlassian Jira ) select it, and click Add Instance . 

 Enter instance details in the required fields and click Connect . 

 Manually create a synced ticket 

 Prerequisite 

 You must set up the following before you can sync issues: 

 An external integration. For more information, see Set up an external integration to sync with issues . 

 A sync profile. For more information, see Create a sync profile . 

 You can manually sync existing issues with external applications. 

 From the Issues page, right-click an issue and select Run Automation → Select Automation . 

 Under Quick Actions , select the action you want to configure, such as Create Jira Ticket or Create ServiceNow Ticket . 

 Define the required ticket parameters. 

 Note 

 Using issue fields as variables is not currently supported. 

 Under Using , select the name of the instance to execute the command. 

 Warning 

 If you leave this field blank, all configured instances will be used. 

 Under Sync Configuration , the following options are displayed, depending on your selection: 

 Link to issue: select this option if you want the issue to be linked to the created ticket. You must check this option if you want to sync the issue with the ticket. 

 Sync Direction: select the syncing configuration: 

 Inbound: Sync changes from the external ticket with the Cortex issue. 

 Outbound: Sync changes from the Cortex issue with the external ticket. 

 Bi-directional: Sync changes in both directions. 

 None: Do not sync changes between the Cortex issue with the external ticket. If you select this option, the tickets are still linked, but changes are not synced. You can update this option at any time to start syncing. 

 Define the inbound and/or outbound sync profiles. 

 Depending on the selected option, select sync profiles that define field mapping between the issue and the external ticket. You can use the default sync profiles or you can create custom profiles. For more information about sync profiles, see Create a sync profile . 

 Note 

 You can only define a single inbound profile. If you change the inbound sync profile the current profile is overwritten. 

 You can define multiple outbound profiles; one issue can update multiple tickets. 

 Click OK . 

 After ticket creation, the ticket number is shown in the Issue card. Click on the ticket number to see details about the created ticket and syncing configuration. In addition, the execution is recorded in the War Room tab. If there is a error in the requested action, you can see details in the audit. 

 View or edit the syncing configuration. For more information, see View, update, or resolve a ticket below. 

 Example 

 The following example shows an automation run on an issue to create a ServiceNow ticket that is synced in an outbound flow with the ticket. 

 Outbound_SNOW_sync_example.png 

 Create an automation rule for syncing issues with external tickets 

 Prerequisite 

 You must set up an integration before you can sync issues. 

 You can set up automation rules that create external tickets when certain issues occur and define the syncing configuration for transferring data between the issues and tickets. 

 Go to Investigation & Response → Automation → Automation Rules . 

 Click Add Automation Rule . 

 Enter a name and description for the rule. 

 Select whether to enable the rule after creation. 

 Under Rule Conditions, define the WHEN, and IF conditions. For more information about rule conditions, see Create an automation rule . 

 Under THEN select the desired automation, such as Create Jira Ticket and complete the following fields: 

 Define the required ticket parameters. 

 Note 

 Using issue fields as variables is not currently supported. 

 Under Using , select the name of the instance to execute the command. 

 Warning 

 If you leave this field blank, all configured instances will be used. 

 Under Sync Configuration , the following options are displayed, depending on your selection: 

 Link to issue: select this option if you want the issue to be linked to the created ticket. You must check this option if you want to sync the issue with the ticket. 

 Sync Direction: select the syncing configuration: 

 Inbound: Sync changes from the external ticket with the Cortex issue. 

 Outbound: Sync changes from the Cortex issue with the external ticket. 

 Bi-directional: Sync changes in both directions. 

 None: Do not sync changes between the Cortex issue with the external ticket. If you select this option, the tickets are still linked, but changes are not synced. You can update this option at any time to start syncing. 

 Define the inbound and/or outbound sync profiles. 

 Depending on the selected option, select sync profiles that define field mapping between the issue and the external ticket. You can use the default sync profiles or you can create custom profiles. For more information about sync profiles, see Create a sync profile . 

 Note 

 You can only define a single inbound profile. If you change the inbound sync profile the current profile is overwritten. 

 You can define multiple outbound profiles; one issue can update multiple tickets. 

 Click OK . 

 If a ticket is created, the ticket number is shown in the Issue card. You can click on the ticket number to see details about the created ticket and syncing configuration. In addition, the execution is recorded in the War Room tab. If there is a error in the requested action, you can see details in the audit. 

 Click Create . 

 The rule is added to the Automation Rules page. If required, drag to reorder the rules. 

 Example 

 The following example shows an automation rule that creates a Jira ticket with bi-directional syncing when a Critical Posture issue is triggered. 

 issue_sync_automation_rule.png 

 View, update, or resolve a ticket 

 Once you have set up ticket syncing, you can view, update and resolve the issue and external ticket as required The changes are reflected according to the defined syncing configuration. 

 To open the ticket details, in the Overview section of the issue card, click on the external ticket number. 

 A panel opens with details of the external ticket. You can see the external ticket number, the sync configuration, and details of the ticket. 

 Open the linked ticket by clicking on the external ticket number in the panel. 

 Update the fields as required. 

 The updates are logged in the ticket history. 

 Note 

 The inbound syncing flow runs every two minutes, and the outbound syncing flow runs every five minutes. 

 In a bi-directional set-up, if the same field is updated in both tickets, the most recently updated value is used. 

 In the external ticket, the logged history shows updates to the ticket. The user name that is logged with the history reflects the user token of the user who configured the data source. 

 Resolve the ticket. 

 Note 

 After an issue is resolved, ticket syncing remains active for up-to seven days. Therefore, you still update, change, or reopen the issue or external ticket and the tickets will continue to sync. 

 Edit or disable ticket syncing 

 You can change the syncing configuration between a ticket and an issue from the issue card. 

 In the Overview section of the issue card, click on the external ticket number. 

 A panel opens with details of the ticket. 

 Click on the settings icon. 

 Under Sync Configuration , change the syncing configuration as required. 

 Note 

 If you change the selected inbound sync profile, the original sync profile is immediately overwritten. 

 To disable ticket syncing, take one of the following actions: 

 To pause ticket syncing, set the Sync Direction value to None . 

 This temporarily stops the tickets from syncing, but the tickets are still linked. You can update the syncing configuration at any time to resume ticket syncing. 

 To unlink the tickets, uncheck Link to issue . 

 This action is not reversable. 

 Click Save . 

 Limitations of issue mirroring 

 Consider the following limitations of issue mirroring: 

 Issue syncing requires the latest version of Atlassian Jira (V3) and ServiceNow (V2). 

 Issue syncing is currently supported in Atlassian Jira (V3) and ServiceNow (V2) only. 

 You can sync up to 50K objects. 

 You can create a maximum of 200 sync profiles. 

 Up to 100 inbound syncs are supported across all synced tickets over a two-minute period. Any additional changes beyond this limit will not be synced. 

 If a connector instance is deleted or disabled, tickets are no longer synced and external ticket information is not available. 

 Custom statuses are not supported. 

 Currently, a specific set of fields is supported. 

 Previous Query case and issue data 

 Next Review findings 

 Last updated 1 month ago 

 Was this helpful?

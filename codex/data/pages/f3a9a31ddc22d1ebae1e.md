---
url: https://cortex-docs.paloaltonetworks.com/cortex-xpanse/incidents-and-alerts/incidents/incident-status
fetched_at: 2026-09-06T10:52:32Z
source: cortex-platform
---

# Incident Status | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex Xpanse 

 Xpanse Expander Documentation 

 Incidents and alerts 

 Incidents 

 Incident Status 

 Learn about each incident status. 

 The table below describes the incident statuses. Some of these statuses are assigned automatically by Xpanse and some are assigned manually by a user. You can manually change the status of any incident to any status. 

 Incidents typically move through a New → Under Investigation → Resolved workflow. However, after an incident has been resolved, Xpanse will reopen it with the status New if scans detect the asset on the internet again and a corresponding alert is generated. 

 Incident Status 

 Description 

 Set by System or User or Both 

 New 

 Incidents have the status New in the following circumstances: 

 Xpanse has created a brand new incident. 

 Xpanse has reopened a previously resolved incident because the asset was observed on the public internet again and Xpanse opened an alert for it. 

 A user has set the incident status to New . 

 Both. The system sets the status to New for a new or reopened incident. A user can change the status to New anytime. 

 Under Investigation 

 Indicates that one or more alerts for the incident are In Progress or New . 

 User only 

 Resolved 

 When all the related alerts for an incident are resolved, the incident is marked Resolved . 

 Both. The system changes the status to Resolved when all the alerts have been resolved. A user can change the status to Resolved anytime. 

 Add Custom Alert and Incident Statuses and Resolution Reasons 

 Warning 

 Before you add a custom status, please review the built-in options. For more information see Alert Status and Incident Status . 

 We recommend using the built-in statuses and resolution reasons where possible. Custom statuses and resolution reasons might not be supported by all content, and status syncing can take time. 

 In addition, custom statuses affect ability of Cortex Xpanse to learn, correctly identify, and score future incidents. 

 You can create custom alert and incident statuses and custom resolution reasons that are tailored to your workflow. Custom statuses and resolution reasons apply to both incident and alert statuses, and can also be used in playbooks. 

 Custom resolution types are always nonterminal (or reopenable ). That means an incident that is resolved with a custom resolution will be reopened with the status New if scans detect the asset again an an alert is generated. An alert that is resolved with a custom resolution will be reopened with the status Reopened . 

 Adding custom incident statuses and resolution reasons requires a View/Edi t RBAC permission for Incident Properties (under Object Setup ). 

 Go to Settings → Configurations → Object Setup → Incidents . 

 The existing statuses and resolution types are listed. 

 In the** Add another status** field, type a new status and click Save . 

 Click **Edit **to rearrange the order of the statuses. This order is presented when you set a status or select a resolution type. 

 Previous Export an incident as a PDF 

 Next Incident Starring 

 Last updated 1 month ago 

 Was this helpful?

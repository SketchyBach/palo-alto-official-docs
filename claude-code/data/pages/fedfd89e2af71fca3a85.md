---
url: https://cortex-docs.paloaltonetworks.com/cortex-xdr-5.x/detect-investigate-and-respond-to-threats/investigate-and-respond-to-cases/investigate-issues/issue-investigation-actions/update-issue-fields
fetched_at: 2026-09-16T08:42:52Z
source: cortex-platform
---

# Update issue fields | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XDR 

 Cortex XDR 5.x Documentation 

 Detect, investigate, and respond to threats 

 Investigate and respond to cases 

 Investigate issues 

 Issue investigation actions 

 Update issue fields 

 Update fields associated with an issue. 

 You can update issue fields by running the setIssue and setIssueStatus commands in the CLI, in a script, or a playbook task. 

 setIssue : Sets values for specific issue fields. The supported fields are presented in the list of arguments. 

 Examples of the setIssue command in the CLI 

 The following examples show how to run the setIssue command in the CLI. You can run CLI commands in the War Room . When you start typing the CLI provides the available options and if you select an enum field, the CLI provides the available values. 

 To change the issue severity to high , run 

 Ask Copy 

 !setIssue severity=high 

 To change the issue severity to high and star the issue, run 

 Ask Copy 

 !setIssue severity=high starred=true 

 setIssueStatus : Sets the status or resolution value for an issue. This command supports the status argument, which presents a list of status and resolution type values. The selected status is set in the custom_status field. 

 If you specify a resolution status, the issue is closed and the resolution_status and closeReason fields are updated to the same value as the custom_status field. If you specify a New, Reopened, or Under Investigation status, the issue remains open and the resolution_status and closeReason fields are empty. 

 Tip 

 You can create custom issue statuses and resolution reasons, and use the setIssueStatus command to set these custom statuses for issues. 

 For example, when a user starts investigating an issue, the issue status is automatically changed from New to Under Investigation . In some cases, it is useful to create an interim status, such as Triage . After you create the custom status, the new status will be available for selection. To create a custom status, follow the instructions in Create custom case statuses and resolution reasons. 

 Examples of using the setIssueStatus command in the CLI 

 The following examples show how to run the setIssueStatus command in the CLI. You can run CLI commands in the War Room . When you start typing, the CLI provides the available options and if you select an enum field, the CLI provides the available values. 

 To change the issue status to Resolved - Known Issue , run 

 Ask Copy 

 !setIssueStatus status="Resolved - Known Issue" 

 To change the issue status to custom status Triage , run 

 Ask Copy 

 !setIssueStatus status=Triage 

 Note 

 You must create a custom status before you can select it. 

 Example of using the setIssueStatus command in a playbook 

 The following example shows how the setIssueStatus command can be used in a playbook task. In this example, the task sets a custom issue status (Triage). The custom issue status was created before setting up the playbook. 

 setAlertStatus_playbook_example.png 

 Previous Query case and issue data 

 Next Close an issue 

 Last updated 1 month ago 

 Was this helpful?

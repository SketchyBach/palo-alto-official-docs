---
url: https://cortex-docs.paloaltonetworks.com/cortex-agentix/detect-investigate-and-respond-to-threats/investigation-and-response/analyze-and-resolve-cases/resolve-the-case/resolution-center
fetched_at: 2026-09-16T08:51:15Z
source: cortex-platform
---

# Resolution Center | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex AgentiX 

 Cortex AgentiX Documentation 

 Detect, Investigate, and Respond to Threats 

 Investigation and Response 

 Analyze and resolve cases 

 Resolve the case 

 Cortex AgentiX 

 Resolution Center 

 Use Resolution Center to plan and execute case remediation in Cortex AgentiX. 

 The Resolution Center is the primary workspace for managing and resolving cases. With a focused, action-oriented flow, you can focus on resolving the entire case rather than investigating isolated issues. By removing fragmented navigation, this workspace allows you to work without context switching, enabling you to open and run playbooks within the case context and quickly review the status of all tasks for all issues in the case. 

 The Resolution Center guides you toward resolution by answering the question, What should I do next? You can track your progress using four specialized tabs: 

 Pending 

 Your to-do list for case actions. This tab displays any tasks waiting for execution or tasks that require your input. 

 Task details: View the task summary, assignee, and SLA. If SLAs are configured, tasks are sorted by deadline; otherwise, they appear in the order they were created. 

 Play book execution: Each task shows its source (Issue ID and Automation Name). You can click the Issue ID to open the issue card or click the playbook to open the workplan. 

 If a playbook is already in progress but requires user input, the label shows the status of the playbook. Click the label to open the Workplan and directly execute the playbook task. 

 Agent actions in error: Review agent actions that require manual intervention, such as sensitive actions that require approval, or actions that require user input. Click the related issue or the agent name to open the issue Resolution tab showing the entire agent conversation. 

 Note 

 Tasks that are already In Progress but require your input will appear in both the Pending and In Progress tabs. 

 Recommended 

 Lists suggested playbooks and response actions to help remediate issues linked to the case. 

 Task details: View details of recommended tasks, including the name of the source that triggered the recommendation. 

 Consolidated tasks: If the same action is recommended for multiple issues, it is only listed once. Review the labels on a task to see the issues for which the task is relevant. 

 Playbook execution: Click a playbook to preview and execute it in the Work Plan . If the playbook applies to multiple issues, you can choose which issues to run it against. 

 Recommended response actions: Click a recommended action to open a dialog with detailed steps for executing the action. 

 In Progress 

 Track automations that are currently running and remediation workflows in real time. 

 Real-time tracking: View all active playbooks, including those in the run queue. 

 Status details: Each record includes the playbook name, related issue, and current status (Error, Waiting, or Running). 

 Navigation: Click a playbook to open the Work Plan or click an Issue ID to view the associated issue card. 

 Agent actions running on an issue: Click the related issue or the agent name to open the issue Resolution tab showing the entire agent conversation. 

 Done 

 Review an audit trail of resolution steps. 

 You can review a list of completed playbooks, automations, and actions that ran on the issues in the case. Records includes the playbook name, the related issue, the completion time, and the final status. 

 Previous Resolve the case 

 Next Collaborative notes and comments 

 Last updated 1 month ago 

 Was this helpful?

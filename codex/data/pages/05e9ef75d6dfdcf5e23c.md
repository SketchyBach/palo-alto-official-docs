---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsoar-8-on-prem/8.13/investigate-and-respond-to-threats/incidents-and-indicators-investigation/investigate-an-incident/use-the-work-plan-in-an-investigation
fetched_at: 2026-09-06T10:28:29Z
source: cortex-platform
---

# Use the Work Plan in an investigation | 8.13 | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSOAR 8 

 Cortex XSOAR 8 On-prem Documentation 

 8.13 

 Investigate and Respond to Threats 

 Incidents and indicators investigation 

 Investigate an incident 

 Cortex XSOAR 8.13 On-prem 

 Use the Work Plan in an investigation 

 Use the Work Plan in Cortex XSOAR 8.13 On-prem investigations. 

 The Work Plan is a visual representation of the running playbook assigned to the incident. Playbooks enable you to automate many security processes, such as managing your investigations and handling tickets. Work Plans enable you to monitor and manage a playbook workflow, and add new tasks to tailor the playbook to a specific investigation. 

 In an investigation, when you open the Work Plan tab you can see the playbook, the playbook name, and navigation tools. 

 By default, the Follow checkbox is checked, which allows you to see the playbook executing in real-time. The playbook moves when a task is completed. 

 In the Work Plan you can do the following: 

 Action 

 Description 

 Change the default playbook 

 On the left-hand side of the window, select the playbook you want to run. 

 When changing the playbook, all completed tasks are removed and the new playbook will run. If you select playbooks several times you can view the history of which playbooks ran. 

 Rerun the playbook 

 When changing the playbook, select the current playbook to run again. 

 View inputs and outputs 

 View the inputs and outputs of each task that has run. You can't view inputs and outputs of any task that hasn't run. 

 Manage tasks 

 View, create, and edit a playbook task. For each task, you can do the following: 

 Designate tasks as complete either manually or by running a script. 

 Assign an owner 

 Set a due date 

 Add comments and completed notes, as required. 

 You can manage these tasks in the CLI by using the /task command. For more information about tasks, see Incident Tasks . 

 Export to a PNG 

 Export the Work plan to a PNG format for easy analysis. 

 The color coding and symbols in the Work Plan help you to easily troubleshoot errors or respond to manual steps. The following table displays the playbook tasks and icons in the Work Plan. 

 Important 

 A playbook will not continue its execution path if a prior task has failed; you must resolve the failed task before subsequent tasks can run. 

 Playbook tasks and icons in the Work Plan 

 Task 

 Description 

 Standard manual task 

 An arrow with a light blue square background indicates a standard manual task. The following are kinds of standard tasks. 

 Manual Standard task (no lightning bolt logo): 

 These tasks are used where usually it's not possible to automate them. You can add comments, assign them to an owner, and set a due date. The analyst who is responsible for the investigation needs to complete the task before the Work Plan can continue. A user icon ( ) indicates the task requires manual inputs. 

 Automated Standard task (with lightning bolt script logo): 

 A single command or script that is set to automatically run when the Work Plan execution reaches this step. Some scripts need arguments in order to run - make sure to set them up properly. If left empty, the analyst who is responsible for the investigation will need to complete them so the script will run and the Work Plan can continue. 

 Automated Standard task (with Builtin logo): 

 A single system command or script that is set to automatically run when the Work Plan reaches this step. Some scripts need arguments in order to run - make sure to set them up properly. If left empty, the analyst who is responsible for the investigation will need to complete them so the script will run and the Work Plan can continue. 

 Automated Standard task (with Multi Command logo): 

 A generic single command or script that can be used with multiple integrations is set to automatically run when the Work Plan reaches this step. Some scripts need arguments in order to run - make sure to set them up properly. If left empty, the analyst who is responsible for the investigation will need to complete them so the script will run and the Work Plan can continue. 

 Conditional task 

 A diamond icon in a purple square background indicates a conditional task used as decision trees in your Work Plan. The following are kinds of conditional tasks. 

 Manual conditional task. A user icon ( ) indicates the task requires manual inputs. 

 Automated conditional task (with the lightning bolt script logo). 

 Automated conditional task that uses a system script (with the Builtin logo). 

 Data collection task / Communication task 

 The speech bubble in a turquoise background indicates a data collection task. This task prompts the receivers to respond to a multi-question form and submit replies, even if they are not Cortex users. A user icon ( ) indicates the task requires manual inputs. 

 Sub-playbook task 

 The workflow icon in a blue background indicates that the task is a playbook nested within the parent playbook. You can view the playbook by opening the task and selecting Open sub-playbook . 

 Task containing an error 

 Scripts or sub-playbooks that have errors are designated by a red triangle. You need to open the script or sub-playbook to review the errors. 

 Task containing a deprecated script or needs to be updated 

 Scripts or sub-playbooks that have updates or are deprecated are designated by a yellow triangle. You need to update the scripts, integration commands, or sub-playbook tasks to their most current version. 

 Set to skip 

 When a task is set to skip, the skip icon will be orange. 

 Breakpoint 

 When the Work Plan reaches a breakpoint, the task has an orange line at the top to indicate the breakpoint. 

 Overridden inputs or outputs 

 When a task is set to have overridden inputs or outputs, the word Input or Output appears in orange. 

 Pending/in queue task 

 When the Work Plan starts to run, all tasks that are about to be performed are gray. 

 Running/ in progress task 

 A spinning circle inside the gray square indicates a running/in progress task. 

 Completed task 

 The green square indicates a completed task. 

 Waiting task 

 The orange square indicates that the task is pending action. 

 If you hover over the icon on the top left corner, details about the reason the task is in waiting mode appear. 

 The user icon ( ) indicates the task requires you to open it and manually mark it as complete. 

 A speech bubble icon ( ) indicates the task is waiting for a questionnaire to be completed. 

 Failed task 

 The red warning icon indicates that the task failed to complete as expected and requires manual inspection and troubleshooting. Contact your Cortex XSOAR administrator. 

 If you hover on the icon on the top left corner, details about the specific problem appear. 

 If a red warning icon is paired with the clock icon ( ), the task’s SLA is overdue. 

 Skipped task 

 The task will look faded to indicate it was not executed. This can happen if this task was set to be skipped when an error occurs, or if it is in a branch that was not executed if a condition wasn’t met. 

 Add ad-hoc tasks to a Work Plan as part of your investigation 

 As part of your incident investigation, within the Work Plan you can create tasks for a specific iteration of a playbook. The task type can be an automation or another playbook. For example, within a manual task, you might need to enrich some data and run an investigation playbook. 

 When you create a task, add a name, automation, and description. The name and description should be meaningful so that the task corresponds to the data that you are collecting. 

 In the Work Plan, go to the task where you want to add and click the + sign at the bottom right-hand corner of the task. 

 The ad-hoc task is added after the task on which you clicked. 

 Select the task type. 

 Standard: Runs a single automation. 

 Playbook: Runs a playbook to enhance the investigation. 

 The playbook functions as any playbook would and requires you to define the inputs and outputs, as well as any other details. 

 Click Save . 

 To run the Work Plan again, click the Run again icon. 

 For a phishing investigation, after the initial playbook run parses the email and extracts email addresses, as part of the manual investigation, you could use the Email Address Enrichment - Generic v2.1 playbook as an ad-hoc playbook task to get more information about these email addresses. 

 Previous Evidence Handling 

 Next Investigate an incident using the canvas 

 Last updated 3 hours ago 

 Was this helpful?

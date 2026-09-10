---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsiam/configure-cortex-xsiam/automations/playbooks/build-your-playbook/test-your-playbook
fetched_at: 2026-09-06T09:29:00Z
source: cortex-platform
---

# Test your playbook | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSIAM 

 Cortex XSIAM Documentation 

 Configure Cortex XSIAM 

 Automations 

 Playbooks 

 Build your playbook 

 Cortex XSIAM 

 Test your playbook 

 Test Cortex XSIAM playbooks using breakpoints, skips, and input or output overrides. 

 The debugger provides a test environment for troubleshooting playbooks. Change data and playbook logic, then view results in real time. You can inspect context data and extracted indicators at every step. 

 To open a detached system playbook, a system playbook copy, or a custom playbook, select it and click Edit . 

 To open an attached playbook, select it and click View . While editing a playbook, select Open sub-playbook in the task pane. 

 When a playbook includes identical sub-playbooks, debugger settings apply to each copy. This includes breakpoints, skips, and input or output overrides. 

 Settings within a loop apply every time that loop runs. 

 Choose test data 

 The debugger uses test data to execute the playbook and show expected results. 

 The debugger does not support parentIncidentFields . 

 New Mock Issue : By default, the debugger uses an empty mock issue. Use it to test simple functionality, such as input parsing. 

 Existing Issue : Select an existing issue, such as a phishing issue ingested through a mail listener. The debugger does not change the original issue or its context data. 

 To select an issue, open the Debugger Panel . Then select an issue in Test data . The list includes the last 50 issues, plus issues you own, joined, or participated in. 

 Using an existing issue does not affect the original issue or context data. 

 Set a breakpoint 

 At a breakpoint, override inputs or outputs to test execution changes. Conditional breakpoints pause only when their condition is met. 

 For example, pause a phishing playbook when it identifies a VIP target. If no VIP exists, execution continues. If a VIP exists, verify that the relevant task identified that member. 

 Breakpoints do not apply to manual tasks. Manual tasks always pause a run unless skipped. When execution reaches a breakpoint, no new tasks begin. Parallel tasks already running continue. 

 You can set breakpoints in parent playbooks and sub-playbooks. 

 To set a breakpoint, go to a task and click on the breakpoint button. When a breakpoint is set, the breakpoint button changes to orange. 

 After a breakpoint is reached, click the task to override inputs and outputs if needed. 

 When you are finished with the task, run the debugger, and in the task, select an option for the playbook to continue. 

 For an automated task, you have the options Run automation now or Complete Manually. If you choose Complete Manually, click on Mark Completed for the playbook to continue. 

 For a task that is a sub-playbook, click Run playbook now for the playbook to continue. 

 For a conditional task, choose which branch the playbook should follow and click Mark Completed for the playbook to continue. The default branch is else. 

 When the playbook reaches a breakpoint, the task has an orange line at the top to indicate the breakpoint. 

 Breakpoint alerts are also displayed at the top of the playbook, enabling you to navigate between multiple breakpoints that have been reached in the playbook or sub-playbooks. 

 Start and stop the debugger 

 The debugger runs with the logged-in user's permissions. Potentially harmful commands appear in the audit trail under that user's name. 

 Breakpoints, skips, and overrides apply only to your session. They never change the playbook permanently. Existing test issues remain unchanged, including their context data. 

 Tasks still execute normally. For example, adding an item to a list adds it to the real list. Users with the required permissions can access that item. 

 Breakpoints pause execution before a task. While paused, the Debugger Panel shows the current context data, indicators, and task information. 

 Click Run to start the debugger. Click Stop to stop it and reset context data: 

 For an existing issue, context resets to the original issue data. 

 For a mock issue, context is cleared. 

 Your breakpoints, skips, and overrides remain available. 

 Override inputs and outputs 

 Override task inputs or outputs temporarily and view results in real time. Overrides apply only to your debugger view. 

 To retain a change permanently, cancel the override and edit the task. You can edit tasks in the debugger or through standard playbook editing. 

 You can add overrides before or during a run. During a run, an override applies only if execution has not reached that task. Permanent input edits apply on the next run. 

 You cannot use filters or transformers in overrides. 

 To override an input or output, open the task and hover over any existing input or output. Click Override Input. 

 Enter a new input or output that will be used only in the debugger. For output overrides, you can enter a value, an array of values, or JSON. For input overrides, you can only enter plain text. 

 Click OK to save your changes. 

 The playbook task card displays a label indicating that the task input or output has been overridden. 

 Skip tasks 

 Skip tasks during testing to prevent unintended actions. For example, skip a task that closes a firewall port, deletes an email, or notifies a manager. 

 You can also skip tasks for integrations that are not configured. If the playbook needs task output, skip the task and override its output. When skipping a conditional task, select the branch to run after the task. 

 Skip a task when you need to: 

 Identify whether a task causes an issue. 

 Avoid tasks unrelated to troubleshooting. 

 Prevent harmful actions, such as blocking a user. 

 Test playbooks before configuring integrations. 

 How to skip a task 

 Click the ‘skip’ button for the task. 

 When a task is set to skip, the ‘skip’ button will be orange. 

 If the output is required for the playbook to proceed, click the task and override inputs and outputs. 

 View context data, indicators, and task information 

 While the debugger runs, select any completed task. The Debugger Panel shows its context data, extracted indicators, and task results. 

 You can see the results of that task in the debugger panel. 

 Previous Update issue fields with playbook tasks 

 Next Troubleshoot playbook performance 

 Last updated 1 month ago 

 Was this helpful?

---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsoar-8-on-prem/8.12/configure-cortex-xsoar/playbooks/develop-your-playbook/task-3.-add-tasks/create-a-section-header
fetched_at: 2026-09-06T10:30:36Z
source: cortex-platform
---

# Create a section header | 8.12 | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSOAR 8 

 Cortex XSOAR 8 On-prem Documentation 

 8.12 

 Configure Cortex XSOAR 

 Playbooks 

 Develop your playbook 

 Task 3. Add tasks 

 Cortex XSOAR 8.12 On-prem 

 Create a section header 

 In Cortex XSOAR 8.12 On-prem, create section headers in playbooks. 

 Section headers are used to manage the flow of your playbook and help you organize your tasks efficiently. You create a section header to group a number of related tasks. 

 Section headers can also be used for time tracking between phases in a playbook. When you start time tracking, apply the Start action for the section header. Because you are using this to time track a particular phase of an investigation, add a stop timer section header when the phase completes. The time tracking data can be used to display in dashboards and report time trends. 

 In a playbook, click + to create a task. 

 Select the Section Header option. 

 Enter a meaningful name in the Task Name field for the section header. 

 Configure the relevant fields. 

 Tab 

 Fields in the tab 

 Details 

 Tag the result with : Add a tag to the task result. You can use the tag to filter entries in the War Room. 

 Sub Section : If selected, this section becomes a subsection of the parent section above it, and it collapses when its parent section collapses. 

 Task description (Markdown supported) : Provide a description of what this task does. In the Playbooks page, click on the section header to display the description. 

 Timers 

 For a time tracking header, select the action to take when the timer is triggered (start, stop, or pause). 

 Timer.start : The trigger for starting to send a message or survey to recipients. You can change this trigger or add a trigger for Timer.stop or Timer.pause . Select the trigger timer field from the drop down. 

 Add Trigger : You can add other trigger timer fields from the drop down. 

 Click Save . 

 Collapse and expand playbook sections 

 You can easily navigate playbooks and focus on the parts you need to work on by collapsing and expanding playbook sections. Collapsing sections provides a condensed view of the playbook flow, reducing visual clutter and enabling quick access to specific sections. Expanding sections allows you to view or edit specific parts of a playbook while keeping the rest of the playbook compact and maintaining focus on the relevant playbook details. You can also hover over a Section Header to highlight all tasks under the section and easily identify the section scope. 

 To collapse and expand a section, in the Playbooks page, after selecting a playbook from the library or creating a new playbook and adding tasks, click on a section header. 

 When you collapse a section, you can see the number of tasks included under the section. For example: 

 playbook-collapsed-num-tasks.png 

 Click to collapse or expand the entire playbook. 

 Previous Set playbook inputs and outputs 

 Next Create a standard task 

 Last updated 3 hours ago 

 Was this helpful?

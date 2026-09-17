---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsoar-8-on-prem/8.5/configure-cortex-xsoar/playbooks/develop-your-playbook/task-3.-add-tasks
fetched_at: 2026-09-16T09:15:02Z
source: cortex-platform
---

# Task 3. Add tasks | 8.5 (EoL) | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSOAR 8 

 Cortex XSOAR 8 On-prem Documentation 

 8.5 (EoL) 

 Configure Cortex XSOAR 

 Playbooks 

 Develop your playbook 

 Cortex XSOAR 8.5 On-prem EoL 

 Task 3. Add tasks 

 Documentation for Cortex XSOAR On-prem 8.5 (EoL). 

 Playbook tasks are the building blocks of playbooks. Tasks enable you to run scripts and sub-playbooks, communicate with end users, set conditions, and store relevant data. 

 Cortex XSOAR supports different task types for different actions to be taken in a playbook, and each task can receive and generate data in the form of inputs and outputs. For example, for enrichment, you might want to run an enrichment sub-playbook or a command that returns additional information for an indicator. 

 Tasks can be reused across playbooks, and you can copy, cut, paste, and delete tasks within or between playbooks using keyboard shortcuts. To see a list of keyboard shortcuts, see Keyboard shortcuts . 

 The Task Library contains scripts, tasks, and playbooks. You can create new tasks from scripts, repurpose existing tasks, and use existing playbooks as sub-playbooks. 

 You can add a brief description for each task, explaining what the task does. Descriptions are added in the Task Description task field. 

 Note 

 To open multiple playbooks at the same time, edit the first playbook and then click the New icon next to the playbook name to create a new tab. You can either create a new playbook or add an existing one. 

 Once you add tasks to your playbook, connect the tasks in their logical order by dragging and dropping a wire from one task to another. 

 Task type 

 Description 

 Section 

 Use a section header task to group related tasks to organize and manage the flow of your playbook. 

 Section headers can also be used for time tracking between phases in a playbook. This data can be used to display in dashboards and report time trends. 

 For example, in a phishing playbook you would have a section for the investigative phase of the playbook such as indicator enrichment, and a section for communication tasks with the user who reported the phishing. 

 For more information, see Create a section header . 

 Standard 

 Standard tasks can be manual tasks such as manual verification to prompt an analyst to verify the severity or classification of an incident before proceeding with automated actions. They can also be automated tasks such as parsing a file or enriching indicators. 

 Automated tasks are based on scripts that exist in the system. These scripts can be created by you or come out-of-the-box as part of a content pack. For example, the !ad-get-user command retrieves detailed information about a user account using the Active Directory Query V2 integration. 

 You can also automatically remediate an incident by interacting with a third-party integration, open tickets in a ticketing system such as Jira, or detonate a file using a sandbox. 

 For more information, see Create a standard task . 

 Conditional 

 Use conditional tasks to validate conditions based on values or parameters and take appropriate direction in the playbook workflow, like a decision tree in a flow chart. 

 For example, a conditional task may ask whether indicators are found. If yes, you can have a task to enrich them, and if not you can proceed to determine that the incident is not malicious. Alternatively, you can use conditional tasks to check if a certain integration is available and enabled in your system. If yes, you can use that integration to perform an action, and if not, you can continue on a different branch in the decision tree. 

 Conditional tasks can also be used to communicate with users through a single question survey, the answer to which determines how a playbook will proceed. 

 For more information, see Create a conditional task . 

 Data Collection 

 Use a data collection task to interact with users through a survey, for example to collect responses or escalate an incident. 

 All responses are collected and recorded in the incident context data, from a single user or multiple users. You can use the survey questions and answers as input for subsequent playbook tasks. 

 You can collect responses in custom fields, for example, a grid field. 

 For more information, see Create a communication task . 

 Previous Task 2. Configure playbook settings 

 Next Set playbook inputs and outputs 

 Last updated 14 days ago 

 Was this helpful?

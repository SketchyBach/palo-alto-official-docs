---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsiam/configure-cortex-xsiam/automations/playbooks/build-your-playbook/add-objects-from-the-task-library/add-manual-tasks-and-blank-tasks/create-a-standard-task
fetched_at: 2026-08-13T15:06:45Z
source: cortex-platform
---

# Create a standard task | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

Create a standard task | Cortex Documentation Portal 

 ⌘ Ctrl k 

 Blog Support 
 More 

 Home 

 Products 

 Guides 

 Release Notes 

 API 

 Reference 

 AI Assistant 

 Good afternoon 
 I'm here to help you with the docs. 

 What is this page about? What should I read next? Can you give an example? 

 ⌘ Ctrl i 

 AI Based on your context 
 Send 

 Learn about Cortex XSIAM 

 Navigate the Cortex XSIAM docs 

 Get started with Cortex XSIAM 

 Agentic AI in Cortex XSIAM 

 Cortex XSIAM product licenses 

 In-product support ticket creation 

 Supported web browsers 

 Use the interface 

 Manage API keys 

 Onboard Cortex XSIAM 

 How to onboard Cortex XSIAM 

 Plan and prepare 

 Deployment steps 

 Post-deployment 

 Configure Cortex XSIAM 

 Learn how to configure Cortex XSIAM 

 Data management 

 Cortex XSIAM Data Sources and Connectors 

 Marketplace 

 Configure the Cortex Agentic Assistant 

 Cortex MCP server 

 Automations 

 Automation in Cortex XSIAM 

 Quick Actions 

 Automation Exclusion Center 

 Playbooks 

 Playbooks overview 

 Access to playbooks 

 Playbook development checkli 

 Plan your playbook 

 Manage playbooks 

 Build your playbook 

 Choose from existing playbooks or create your own 

 Configure playbook settings 

 Add objects from the Task Library 

 Add commands and scripts 

 Add sub-playbooks 

 Add AI Prompt tasks 

 Add manual tasks and blank tasks 

 Create a standard task 

 Create a conditional task 

 Create a communication task 

 Create a section header 

 Configure script error handling in a playbook 

 Customize your playbook 

 Test your playbook 

 Manage playbook content 

 Accelerate playbook development using the Automation Engineer agent (preview) 

 Best practices for playbooks 

 Autonomous playbooks 

 AI Prompts 

 Agentic Response (Preview) 

 Create an automation rule 

 Scripts 

 Context data 

 Lists 

 Jobs 

 Engines 

 Remote repository management 

 Customize cases and issues 

 XQL query management 

 Multi-Tenant 

 Managed Services configuration in Cortex 

 Protect your endpoints 

 Endpoint security 

 Endpoint DLP 

 Detect, Investigate, and respond to threats 

 Monitor dashboards and reports 

 Investigation and response 

 Agentic Assistant chat 

 Asset management 

 Threat management 

 Attack surface management 

 Vulnerability management 

 Exposure management 

 Cortex Advanced Email Security 

 Identity Threat Detection and Response (ITDR) 

 Cloud Security 

 Monitor and track compliance adherence 

 Cloud security rules and policies 

 Cortex Cloud Data Classification 

 Cortex Data Security 

 Cloud Identity Security 

 Network exposure detection 

 Cortex Cloud SaaS Security 

 Cortex Cloud AI Security 

 Serverless function posture security 

 Cortex Cloud Application Security 

 Cloud workload policies and rules 

 Base image rules 

 Web and API Security (WAAS) 

 Serverless function runtime security 

 Reference and developer docs 

 Cortex XSIAM XQL 

 Graph Search 

 Cortex CLI 

 Role-Based Access Control 

 API documentation 

 Reference 

 Migrating to a new Broker VM image 

 Learn more about migrating to the latest broker VM image 

 Standalone Broker VM 

 Broker VM high availability cluster node 

 On this page 

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

 Add objects from the Task Library 

 Add manual tasks and blank tasks 

 Create a standard task 

 Standard tasks can be manual tasks such as manual verification to prompt an analyst to verify the severity or classification of an issue before proceeding with automated actions. They can also be automated tasks such as parsing a file or enriching indicators. 

 From the Task Library pane, click the task you want, for example Blank Task. 

 In the Task Details pane, select the Standard icon for Task Type. 

 Enter a meaningful name in the Task Name field for the task that corresponds to the data you are collecting. 

 Select the options you want to configure for the Standard task. 

 Standard tasks include the following field and tabs. 

 Field / tab 

 Settings 

 Choose script field 

 From a drop down list, select a script for the playbook to run. In the following tabs you can set: 

 Inputs: Each script has its own set of input arguments (or none). You can set each argument to a specific value (by typing directly on the line under the argument name) or you can click the curly brackets to define a source field to populate the argument. 

 Note 

 When a script or integration command requires a credential, such as a username/password or API key, you can typically select a stored secret by clicking Switch to credentials . If your user role has the Credentials permission set to None , this option is hidden and you will see the message Credentials are locked by admin . In this state, you cannot view, select, or reference any stored credentials within the task configuration. For more information, see Credentials permissions . 

 Outputs: Each script has its own set of output arguments (or none). 

 Mapping: 

 Map the output from a playbook task directly to an issue field. 

 The value for an output key populates the specified field per issue. This is a good alternative to using a task with the setIssue command. 

 The output value is dynamic and is derived from the context at the time that the task is processed. As a result, parallel tasks that are based on the same output may return inconsistent results. 

 In the Mapping tab, click Add custom output mapping. 

 Under Outputs, select the output parameter whose output you want to map. Click the curly brackets to see a list of the output parameters available from the script. 

 Under Field to fill, select the field that you want to populate with the output. 

 Click Save. 

 Advanced: Includes the following fields. 

 Using: Choose which integration instance will execute the command, or leave empty to use all integration instances. 

 Extend context: Append the extracted results of the action to the context. For example, "newContextKey1=path1::newContextKey2=path2" returns "[path1:'aaa',path2: 'bbb', newContexKey1: 'aaa',newContextKey2:'bbb']" 

 Ignore outputs: If set to true, will not store outputs into the context (besides the extended outputs). 

 Execution timeout (seconds): Sets the command execution timeout in seconds. 

 Indicator Extraction mode: Choose when to extract indicators: 

 None: Do not perform indicator extraction 

 Inline: Before other playbook tasks 

 Out of band: While other tasks are running 

 Mark results as note 

 Mark results as evidence 

 Run without a worker 

 Skip this branch if this script/playbook is unavailable 

 Quiet Mode: When in quiet mode, tasks do not display inputs and outputs or extract indicators. Errors and warnings are still documented. You can turn quiet mode on or off at the task or playbook level. 

 Details: Includes the following fields. 

 Tag the result with: Add a tag to the task result. You can use the tag to filter entries in the War Room. 

 Task description (Markdown supported): Describe what this task does. You can enter objects from the context data in the description. For example, in a communication task, you can use the recipient’s email address. The value for the object is based on what appears in the context every time the task runs. 

 Timers: Includes the following fields. 

 Timer.start: The trigger for starting to send a message or survey to recipients. You can change this trigger or add a trigger for Timer.stop or Timer.pause. Select the trigger timer field from the drop-down. 

 Add Trigger: You can add other trigger timer fields from the drop-down. 

 On Error: Includes the following fields. 

 Number of retries: How many times the task should retry running if there is an error. Default is 0. 

 Retry interval (seconds): How long to wait between retries. Default is 30 seconds. 

 The maximum retry interval is 800 seconds (13.3 minutes). If you enter a value greater than 800 seconds, the retry interval will be limited to 800 seconds. 

 Error handling: How the task should behave if there is an error. Options are: 

 Stop 

 Continue 

 Continue on error path(s) 

 This option configures the task to handle potential errors that may occur when executing the current task's script. 

 Manual task settings tab 

 Default assignee: Assign an owner to this task. 

 Only the assignee can complete the task: Stop the playbook from proceeding until the task assignee completes the task. By default, in addition to the task assignee, the default administrator can also complete the blocked task. You can also block tasks until a user with an external email address completes the task. 

 Task SLA: Set the SLA in granularity of weeks, days, hours, and minutes. 

 Set task Reminder at: Set a reminder for the task in the granularity of weeks, days, hours, and minutes. 

 Advanced tab 

 Register as case timeline record : If enabled, the results of the task execution appear as a record in the case timeline. If enabled, you must enter a Record name. You have the option of adding an Effective time , Description , Tags , and marking the record as evidence and adding an evidence comment.
 NOTE : Only enter an Effective time if you want the same exact time recorded every time the playbook task executes. 

 Quiet Mode: Determines whether this task uses the playbook default setting for quiet mode. When in quiet mode, tasks do not display inputs and outputs or extract indicators. Errors and warnings are still documented. You can turn quiet mode on or off at the task or playbook level. 

 Details tab 

 Tag the result with: Add a tag to the task result. You can use the tag to filter entries in the War Room. 

 Task description (Markdown supported): Provide a description of what this task does. You can enter objects from the context data in the description. For example, in a communication task, you can use the recipient’s email address. The value for the object is based on what appears in the context every time the task runs. 

 Timers tab 

 Timer.start: The trigger for starting to send a message or survey to recipients. You can change this trigger or add a trigger for Timer.stop or Timer.pause. Select the trigger timer field from the drop down. 

 Add Trigger: You can add other trigger timer fields from the drop down. 

 Click Save. 

 The task is added in the playbook editor. 

 If you selected a system script in the settings, the task logo indicates Builtin. 

 Connect the tasks you've added in their logical order by dragging and dropping a wire from one task to another. 

 Save the playbook. 

 Previous Add manual tasks and blank tasks Next Create a conditional task 

 Last updated 18 days ago 

 Was this helpful? 

 ‍ 

 Trust Center 

 ‍ 

 Privacy 

 ‍ 

 Terms of Use 

 ‍ 

 Legal 

 © 2026 Palo Alto Networks, Inc. All rights reserved. 

 Was this helpful?

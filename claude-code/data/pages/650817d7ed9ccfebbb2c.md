---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsiam/configure-cortex-xsiam/automations/playbooks/build-your-playbook/add-objects-from-the-task-library/create-a-section-header
fetched_at: 2026-08-13T15:06:54Z
source: cortex-platform
---

# Create a section header | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

Create a section header | Cortex Documentation Portal 

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

 Create a section header 

 Section headers are used to manage the flow of your playbook and help you organize your tasks efficiently. You create a section header to group a number of related tasks. 

 From the Task Library pane, click Header or Blank Task . 

 In the Task Details pane, for Task Type, select the Section Header icon. 

 Enter a meaningful name in the Task Name field for the section header. 

 In the Details tab, configure the following. 

 Tag the result with : Add a tag to the task result. You can use the tag to filter entries in the War Room. 

 Sub Section : If selected, this section becomes a subsection of the parent section above it, and it collapses when its parent section collapses. 

 Response action : Select this checkbox to mark the section as containing impactful remediation or response steps. These actions are surfaced in the Resolution tab of an issue and the Possible Response section in the playbook's high-level visual structure. Use this for autonomous playbooks to highlight key results for analysts. 

 Requires manual intervention : Select this checkbox to pause the playbook at this section. The playbook will remain in a pending state until an analyst provides manual approval or performs the required action in the Pending tab of the Resolution Center. Use this to ensure relevant autonomous actions only proceed with human oversight. 

 Display label : Enter a short, human-readable name for the action. This label is displayed in the UI (such as the Resolution tab or Case screen) to help analysts identify the task's intent during an investigation. This enables autonomous playbooks to provide a clear summary of automated findings. 

 Task description (Markdown supported) : Provide a description of what this task does. In the Playbooks page, click on the section header to display the description. 

 In the Timers tab, for a time tracking header, select the action to take when the timer is triggered (start, stop, or pause). 

 Timer.start : The trigger for starting to send a message or survey to recipients. You can change this trigger or add a trigger for Timer.stop or Timer.pause. Select the trigger timer field from the drop down. 

 Add Trigger : You can add other trigger timer fields from the drop down. 

 Click Save . 

 Previous Create a communication task Next Configure script error handling in a playbook 

 Last updated 17 days ago 

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

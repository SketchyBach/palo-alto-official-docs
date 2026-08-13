---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsiam/configure-cortex-xsiam/automations/autonomous-playbooks/manage-autonomous-automation-rules
fetched_at: 2026-08-13T15:07:32Z
source: cortex-platform
---

# Manage autonomous automation rules | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

Manage autonomous automation rules | Cortex Documentation Portal 

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

 Autonomous playbooks 

 Enable autonomous playbooks 

 Manage autonomous playbooks 

 Manage autonomous automation rules 

 Work Plan for autonomous playbooks 

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

 Autonomous playbooks 

 Manage autonomous automation rules 

 When the Autonomous Playbooks feature is enabled, the relevant autonomous automation rules are automatically added to Cortex XSIAM and can be viewed at Investigation & Response → Automation → Automation Rules . 

 Autonomous automation rules are grouped together and are displayed as a collapsed block that you can expand. By default, the autonomous automation rules are placed at the end of the list of automation rules, but you can adjust the position of the block. For all automation rules, autonomous and regular, rules are evaluated in order, and only the first rule that matches the trigger conditions is executed. 

 You cannot edit, duplicate, or delete autonomous automation rules and you cannot delete or change the playbook assigned to the rule. 

 If you need to temporarily stop a specific autonomous playbook from triggering automatically, you can disable its rule. On the automation rules screen, right-click the specific rule within the autonomous block and select Disable . You can also add your own automation rules that apply the same condition but run a different playbook or Quick Action. If your custom automation rule is higher in the list than the autonomous automation rule, your rule is executed when the condition is met and the autonomous automation rule with the same condition is ignored. 

 As new autonomous automation rules for Cortex Analytics are released, they automatically appear in the Automation Rules pages. By default, they are enabled. 

 Autonomous automation rules only work with autonomous playbooks. You cannot trigger an autonomous playbook with a custom automation rule. 

 Previous Manage autonomous playbooks Next Work Plan for autonomous playbooks 

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

---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsiam/configure-cortex-xsiam/automations/automation-exclusion-center
fetched_at: 2026-08-13T15:06:13Z
source: cortex-platform
---

# Automation Exclusion Center | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

Automation Exclusion Center | Cortex Documentation Portal 

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

 Manage automation exclusion policies 

 Playbooks 

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

 Automation Exclusion Center 

 Automation exclusion policies prevent commands and scripts from performing remediation on critical assets. 

 Automation exclusion policies enable you to protect critical assets from automated remediation without having to detach and customize playbooks, scripts, and integrations. 

 Automation exclusion policies prevent commands and scripts from performing automated remediation actions on critical assets, such as users, IP addresses, and domains. For example, a playbook task might block multiple domains, but mission-critical domains in the policy list would not be blocked. 

 Automation exclusion policies apply any time a relevant command or script runs, whether in a playbook task, a Quick Action, as an action executed by an AI agent, or in the CLI. If you configure a policy to allow overrides, users can manually run the command in the War Room, using the override-policy parameter. Any command triggered with the override-policy parameter appears in the Management Audit Logs. If you attempt to use the override-policy parameter and the policy does not allow overrides, an error entry appears in the War Room. 

 When an automation exclusion policy prevents a command or script from a remediation action, the exclusion appears in the issue War Room. 

 When a playbook task contains a command or script that is included in an automation exclusion policy, a Policy tab appears in the task details pane, showing the relevant policy. 

 To enable an automation exclusion policy, add critical assets to a list. Each policy uses one or more lists to exclude assets from remediation. By default, all policies are enabled, but lists are empty until assets are added to the list. 

 Note 

 By default, all users have read and edit permissions to lists. When creating a list of critical assets, we recommend limiting the read and edit permissions to specific roles. 

 User Hard Remediation and User Soft Remediation policies can also use asset groups, enabling automatic updates of critical assets without requiring you to edit a list. These remediation policies can contain lists, asset groups, or a combination of lists and asset groups. 

 Policies can be enabled or disabled, and lists can be edited, but you cannot add or remove policies. 

 Each policy can include one or more scripts or commands. Commands and scripts only appear if the content is installed. The policy affects only these scripts and commands. Scripts and commands cannot be added, edited, or removed from the policy. 

 By default, only admin users have access to the Automation Exclusion Center page. You can also provide other roles with View or View/Edit access to the Automation Exclusion Center. When creating or editing a role, the permission can be found under Investigation & Response → Automations . 

 Policies can be sorted, filtered, and searched using the category, status, policy, exclude, and description columns. 

 To configure a policy, see Manage automation exclusion policies . 

 Previous Quick Actions Next Manage automation exclusion policies 

 Last updated 20 days ago 

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

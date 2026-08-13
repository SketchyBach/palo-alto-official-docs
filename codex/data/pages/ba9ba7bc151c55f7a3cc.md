---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsiam/configure-cortex-xsiam/configure-the-cortex-agentic-assistant-1/agents-hub/manage-agents
fetched_at: 2026-08-13T15:06:01Z
source: cortex-platform
---

# Manage agents | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

Manage agents | Cortex Documentation Portal 

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

 Agentic Assistant components and concepts 

 Agentic Assistant Hub 

 Manage actions 

 Register actions 

 Manage agents 

 Build agents 

 Manage knowledge sources (preview) 

 Expand agent capabilities with MCP integrations 

 Agentic Assistant role-based access control 

 Cortex MCP server 

 Automations 

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

 Configure the Cortex Agentic Assistant 

 Agentic Assistant Hub 

 Manage agents 

 Agents create and execute step-by-step plans dynamically, choosing relevant actions based on a user's request. Each agent has a model, a user context, a conversation context, and a set of actions that it can perform. Users engage with agents through conversations in the chat interface. 

 Agents can only use actions that have been assigned to them, and execution is limited by the user's permissions. 

 Permissions for the Agentic Assistant and the Agentic Assistant Hub can be found under CORTEX AGENTIC ASSISTANT in the role permissions when creating or edit a role. For more information, see Agentic Assistant role-based access control 

 There are two types of agents in the Cortex Agentic Assistant: 

 Custom agents : Each user can create one or more agents that have the same or fewer permissions as the user, ensuring agents operate with the least necessary privileges required. These permissions automatically update if the user’s roles or permissions change. When users create custom agents, they can create a private agent only they can access, or a public agent all users can access. 

 System agents : System agents come out-of-the-box and are not linked to a specific user; instead, they possess their own defined roles and permissions. A system agent may include actions that the user does not have permission to execute. All users have access to all system agents, but plan execution is limited by the permissions of the individual user. 

 System agents can include actions that require additional content packs to be installed and configured. To view all actions assigned to a system agent, including actions not available due to missing content, click on the system agent in the Agentic Assistant Hub . There may be actions assigned to a system agent that are not relevant to your organization. For example, the Case Investigation agent includes the action ServiceNow - Create Ticket , but you would only install and configure the relevant content pack if you wanted to create tickets in ServiceNow. 

 System agents include system actions that may be marked as sensitive and require manual approval to execute. You can change this setting for specific system actions from the the Actions tab of the Agentic Assistant Hub , by clicking in the action card and selecting Mark as sensitive or Mark as non-sensitive . 

 Agent management 

 You can edit, delete, disable, or enable custom agents by clicking the more options icon for the agent. 

 You can edit, enable, or disable system agents by clicking the more options for the agent. The edit option for system agents is limited to adding specific instructions for the agent such as tone, style, format, and priorities. 

 You can click on an Agent to view all actions assigned to the agent. There are three possible statuses for actions assigned to an agent: 

 Enabled (green circle with a check mark): The action is enabled and available for the agent to use. 

 Disabled (grey circle with an x): The action has been disabled and is not available for the agent to use. 

 Unavailable content (grey circle with a horizontal line): The content the action is based on is not available. To use the action, the content item must be installed and configured. 

 In some cases, an agent may include actions with content items that are not relevant for all licenses. If that occurs, the grey circle appears, but you are not able to install the related content. 

 Search, filter, and sort existing agents 

 You can use the dropdown filter to search all agents, custom agents, enabled agents, or disabled agents. 

 You can sort agents by most used, creation time, or update time. 

 Previous Register actions Next Build agents 

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

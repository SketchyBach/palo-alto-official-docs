---
url: https://cortex-docs.paloaltonetworks.com/cortex-xdr-5.x/reference-and-developer-docs/role-based-access-control/cortex-agentic-assistant-permissions/cortex-agentic-assistant-agents
fetched_at: 2026-09-16T08:43:48Z
source: cortex-platform
---

# Cortex Agentic Assistant Agents | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XDR 

 Cortex XDR 5.x Documentation 

 Reference and developer docs 

 Role-Based Access Control 

 Cortex Agentic Assistant permissions 

 Cortex XDR 5.x 

 Cortex Agentic Assistant Agents 

 Configure Cortex Agentic Assistant Agents permissions. 

 Cortex Agentic Assistant Agents 

 Controls whether a user can access and interact with the Cortex Agentic Assistant, including managing actions and agents. This is the base permission required for any assistant interaction. 

 Permission 

 Description 

 Roles Example 

 None 

 The assistant panel is disabled. Users cannot use natural language queries or access the Agentic Assistant Hub. 

 View/Edit 

 Users can open the Cortex Agentic Assistant panel, access the Agentic Assistant Hub, view chat history, and view agent details and action details in the Hub. In addition, you can select the following: 

 Interact with Agents 

 Manage Actions 

 Manage Agents 

 Agents Admin 

 SOC Tier-1 Analyst: Needs to use the assistant for quick lookups, IP/hash enrichment, and guided investigation. No need to manage agents or actions. 

 SOC Tier-2 and 3 Analysts: full assistant interaction for complex investigations. No need to manage agents or actions. 

 Threat Hunter: Full assistant interaction for threat hunting. Can view agents and actions, but does not need to modify them 

 Security Engineer: Builds custom agents and actions for the organization. Does not need Agents Admin as they manage their own agents. 

 Cortex Agentic Assistant Agents sub-permissions 

 Sub-permissions 

 Description 

 Roles Example 

 Interact with Agents 

 Interact with Agents: Users can trigger Agents in the Cortex Agentic Assistant. Users can access their own agents, public agents, and system agents. For more information, see Agentic Assistant Hub . 

 Checked: The user can take actions, such as sending messages and queries to the assistant, starting new conversations with agents, and executing insight actions (Add as IOC, etc). 

 Unchecked: The user can view the assistant panel, home screen, Agentic Assistant Hub (read-only, based on the parent View/Edit level), chat history, and previous conversations. The user can also view insights cards for IPs, hashes, and domains. 

 All roles should require full assistant interaction. 

 Manage Actions 

 Controls the ability to manage agent actions - the discrete operations that agents can perform. Actions are the building blocks that agents use to execute tasks. For more information, see Manage actions . 

 Checked: Users can manage actions, register scripts as agent actions, and configure action parameters and descriptions. 

 Unchecked: The user can view the Actions tab in the Agentic Assistant Hub (read-only, browse available actions and their configurations. They can also view action details, parameters, and descriptions. 

 Security Engineer 

 Manage Agents 

 Controls the ability to create and manage AI agents. Users with this permission can create custom agents, edit their own agents, and configure agent properties. For more information, see Manage agents . 

 Checked: Users can manage agents, configure agent instructions, and assign/remove actions from agents. 

 Unchecked: Users can view the Agents tab in the Agentic Assistant Hub, browse available agents, and their configurations. They can also view agent details, descriptions, and assigned actions. 

 Security Engineer 

 Agents Admin 

 The highest-level agent management permission. When checked, it overrides the ownership restrictions of the Manage Agents checkbox, allowing the user to edit and manage ALL agents in the organization, including system agents and agents created by other users. For more information, see Agentic Assistant Hub. 

 Checked: Users can edit/delete any agent, including system agents, configure custom instructions for system agents, and manage organization-wide agent settings. The user can override all agent ownership restrictions. 

 Unchecked: The user cannot edit system agents, cannot edit agents created by other users, and cannot manage organization-wide agent configurations. 

 Note 

 If Manage Agents is checked, the user can only edit their own agents. 

 Required and recommended permissions 

 Consider adding the following permissions: 

 Permission 

 Permission Level 

 Reason 

 Cases & Issues 

 View or View/Edit 

 View: Required. Agent conversations reference cases and issues. 

 View/Edit: Strongly recommended. Agents can modify case status and assign analysts. 

 Threat Intelligence (under Threat Management) 

 View or View/Edit 

 View: Required. Agents perform Indicator lookups and enrichment. 

 View/Edit: Strongly recommended for Indicator actions. Agents can create/modify Indicators. 

 Query Center 

 View or View/Edit 

 View: Required. Agents generate and execute XQL queries. 

 View/Edit: Strongly recommended. Agents execute queries on behalf of users. 

 Scripts & Playbooks 

 View or View/Edit 

 View: Required. Register scripts as agent actions. Agents can suggest and reference playbooks. 

 View/Edit: Strongly recommended. Create scripts to register as actions; needed for full action builder workflow 

 Dashboards 

 Enabled 

 Strongly recommended to view the Command Center dashboard with agent integration. 

 Forensics 

 View 

 Recommended. Agents can reference forensic data in investigations. 

 Host Insights 

 View 

 Recommended. Agents can reference host/endpoint data. 

 Marketplace 

 View/Edit 

 Recommended to install content packs with agent definitions and actions. 

 Integrations 

 View/Edit 

 Recommended to configure integrations that agents use as data sources. 

 Previous AI Prompts 

 Next Agents and endpoint protection 

 Last updated 20 days ago 

 Was this helpful?

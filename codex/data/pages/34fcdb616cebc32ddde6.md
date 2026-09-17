---
url: https://cortex-docs.paloaltonetworks.com/cortex-cloud-runtime-security/cases-and-issues/investigation-and-response/automation/playbooks
fetched_at: 2026-09-16T08:44:41Z
source: cortex-platform
---

# Playbooks | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex Cloud 

 Cortex CLOUD Runtime Security 

 Cases and issues 

 Investigation and response 

 Automation 

 Cortex Cloud Runtime 

 Playbooks 

 Build and manage playbooks for automated workflows. 

 Playbooks are a series of tasks that run in a predefined flow to save time and improve the efficiency and results of the investigation and response process. They enable you to automate many security processes, including handling investigations and managing tickets. For example, a playbook task can parse the information in an issue, whether it is an email or a PDF attachment. Playbooks also standardize workflows, ensuring consistent and efficient incident response and management. 

 Prerequisite 

 To work with playbooks, an administrator must configure their user role with specific RBAC permissions. 

 Permissions must be enabled in the following order: 

 Scripts : This component (under Investigation & Response → Automations ) must be set to Enabled first. It is the foundational permission for all automation; if Scripts are not enabled, you cannot configure Playbooks or Cases and Issues . Role-level permissions determine your ability to create new scripts or edit those marked as Public . 

 Playbooks : This component (under Investigation & Response → Automations ) must be set to Enabled . Role-level permissions determine your ability to create new playbooks or edit those marked as Public . Specific access to individual custom playbooks and scripts is managed at the object level. For detailed information on the access model, see Access to playbooks . 

 Cases and Issues : Once Scripts and Playbooks are enabled, you can set Cases and Issues (under Cases & Issues ) to View or View/Edit . This is required to view the results of playbooks executed within a case. 

 Credentials : While not required to open the Playbook Editor, a minimum of View permissions for Credentials is required to select or reference stored secrets within playbook tasks. If your role has the Credentials permission set to None , you will be unable to select credentials from dropdown menus. Furthermore, any task that attempts to retrieve a credential to authenticate an integration command will fail during execution because the system cannot fetch the secret under your role's restricted context. 

 Restricting playbook access : To completely restrict playbook access, first set the Cases and Issues RBAC permission to None and then set the Playbooks permission to Disabled . 

 Automation Engineer agent for playbook development (preview) 

 Use the AI-powered Automation Engineer agent to simplify playbook creation and management through an intuitive, interactive experience. It enables you to generate, modify, and query playbooks with the Cortex Agentic Assistant natural language chat prompt. For example, within the chat, you can ask the agent to "Add a step to block the domain in Okta" or ask it to explain how a specific conditional branch operates. 

 For more details about using the Automation Engineer agent, see Accelerate playbook development using the Automation Engineer agent (preview) . 

 Previous Manage automation exclusion policies 

 Next Playbooks overview 

 Last updated 1 month ago 

 Was this helpful?

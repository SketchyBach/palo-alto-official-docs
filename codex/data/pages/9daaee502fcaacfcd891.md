---
url: https://cortex-docs.paloaltonetworks.com/cortex-cloud-runtime-security/cases-and-issues/investigation-and-response/investigate-issues
fetched_at: 2026-09-06T09:55:11Z
source: cortex-platform
---

# Investigate issues | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex Cloud 

 Cortex CLOUD Runtime Security 

 Cases and issues 

 Investigation and response 

 Cortex Cloud Runtime 

 Investigate issues 

 Cortex Cloud generates issues to bring your attention to security risks in your framework. 

 Prerequisite 

 To work with issues, an administrator must configure your user role with specific RBAC permissions. Permissions must be enabled in the following order: 

 Playbooks : This component (under Investigation & Response → Automations ) must be set to Enabled first. Role-level permissions determine your ability to create new playbooks or edit those marked as Public . Specific access to individual custom playbooks and scripts is managed at the object level. For detailed information on the access model, see Access to playbooks . 

 Cases and Issues : Once Playbooks are enabled, you can set Cases and Issues (under Cases & Issues ) to View or View/Edit . 

 Issues help you to monitor and control the security of your system framework by notifying you about risks to security in your framework. Cortex Cloud generates issues from the following: 

 Rules that you set up, such as vulnerability rules. 

 Findings 

 Findings themselves are not issues, but findings that match a specific logic can generate issues. 

 Integrations 

 Integrations enable you to ingest events, such as phishing emails, SIEM events, from third-party security and management vendors. You might need to configure the integrations to determine how events are classified as events. For example, for email integrations, you might want to classify items based on the subject field, but for SIEM events, you want to classify by event type. 

 Previous Investigation and response 

 Next Overview of the Issues page 

 Last updated 1 month ago 

 Was this helpful?

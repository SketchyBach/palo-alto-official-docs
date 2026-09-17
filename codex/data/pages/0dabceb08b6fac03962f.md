---
url: https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cases-and-issues/investigation-and-response/automation/integrations/manage-credentials
fetched_at: 2026-09-16T08:47:24Z
source: cortex-platform
---

# Manage credentials | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex Cloud 

 Cortex CLOUD Posture Management 

 Cases and issues 

 Investigation and response 

 Automation 

 Integrations 

 Cortex Cloud Posture 

 Manage credentials 

 Manage credentials used by integrations. 

 Credentials simplify and compartmentalize administrative tasks, and enable you to save login information without exposing usernames, passwords, certificates, and SSH keys. You can reuse credentials across multiple systems, for example, when using the same administrator password across multiple endpoints. 

 Prerequisite 

 To view the Credentials page and manage its content, your user role must have the following minimum permissions: 

 Integrations : View 

 Data Sources : View 

 External Issue Mapping : View 

 Without these permissions, the Credentials page is hidden. Furthermore, if the Credentials permission itself is set to None , the page is hidden even if the above prerequisites are met. 

 After you set up a credential, you can configure integration instances to use it instead of entering the name and password manually. 

 Add credentials to an integration instance 

 Create the credential. 

 Select Settings → Configurations → Integrations → Credentials → New Credential . 

 Add the following parameters: 

 Parameters 

 Description 

 Credential Name 

 The name of the credential. You select this name when adding the credential to the integration instance. 

 Username 

 The username for the credential. 

 Workgroup 

 The workgroup to associate this credential with. Relevant for third-party services, such as Active Directory, CyberArk, and HashiCorps. 

 Password 

 The password for the credential. For example, add the API Key when defining the API credential. 

 Certificate 

 Certificate or SSH to use for the credential. 

 Save the credential. 

 Add the credential to the integration instance. 

 Go to Settings → Data Sources & Integrations and select the integration. 

 Click Add Instance . 

 Locate the relevant section and click Switch to credentials . 

 If there is more than one credential, select the relevant credential. 

 Note 

 If your user role has the Credentials permission set to None , the Switch to credentials option is hidden. Instead, the message Credentials are locked by admin is displayed, and you cannot reference stored secrets. This restriction applies to both data sources and unified connectors. 

 Test and Save & Exit the integration instance. 

 Previous Troubleshoot integations 

 Next Engines 

 Last updated 14 days ago 

 Was this helpful?

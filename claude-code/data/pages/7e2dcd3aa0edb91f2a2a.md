---
url: https://cortex-docs.paloaltonetworks.com/cortex-cloud-runtime-security/cases-and-issues/investigation-and-response/automation/manage-automation-exclusion-policies
fetched_at: 2026-09-06T09:55:38Z
source: cortex-platform
---

# Manage automation exclusion policies | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex Cloud 

 Cortex CLOUD Runtime Security 

 Cases and issues 

 Investigation and response 

 Automation 

 Manage automation exclusion policies 

 Create and manage policies that exclude automated actions. 

 Automation exclusion policies prevent commands and scripts from performing automated remediation actions on critical assets, such as users, IP addresses, and domains. For example, a playbook task might block multiple domains, but mission-critical domains in the policy list would not be blocked. 

 Admin users and all roles with read/write permissions to the Automation Exclusion Center can edit, disable, and enable policies. 

 Go to Settings → Configurations → Automation → Automation Exclusion Center . 

 Right-click on a policy and choose Edit . 

 From the Edit Policy page, you can do the following: 

 Enable or disable the policy. Policies are enabled by default. 

 Enable or disable policy overrides. If you enable policy overrides, users can manually run the commands and scripts on the excluded critical assets, using the override-policy parameter. Use of the override-policy parameter is included in the Management Audit Logs. 

 Select one or more lists of excluded assets. 

 Clicking the list icon opens a new browser tab for the Lists page, where you can create and edit lists. 

 For the IAM User Hard Remediation and User Soft Remediation policies, we recommend including username, email, and ID for each user you want to exclude. Example: username1, user@example.com, userID112 . 

 Each list can be filtered by conditions, such as Equals , Ends with , and Doesn't include . For example, you can exclude all email addresses with your company's domain using the Ends with filter. 

 For IAM User Hard Remediation and User Soft Remediation policies, you can also select asset groups. These policies can include only lists, only asset groups, or a combination of asset groups and lists. 

 Under THEN skip execution of the following commands and scripts , click to view the scripts and commands affected by the policy. Commands only appear if they are part of an active integration instance. You cannot edit the list of scripts and commands. 

 Save your changes. 

 You can also right click on a policy from the main Automation Exclusion Center page to disable or enable the policy. 

 If you click on a list name in the Exclude column, that list opens in the Lists page. 

 Previous Automation Exclusion Center 

 Next Playbooks 

 Last updated 1 month ago 

 Was this helpful?

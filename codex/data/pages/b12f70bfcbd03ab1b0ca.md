---
url: https://cortex-docs.paloaltonetworks.com/cortex-agentix/configure-cortex-agentix/automations/playbooks/build-your-playbook/manage-playbook-content
fetched_at: 2026-09-16T08:51:03Z
source: cortex-platform
---

# Manage playbook content | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex AgentiX 

 Cortex AgentiX Documentation 

 Configure Cortex AgentiX 

 Automations 

 Playbooks 

 Build your playbook 

 Cortex AgentiX 

 Manage playbook content 

 Manage playbook content, versions, and dependencies in Cortex AgentiX. 

 Manage playbook content with a remote repository 

 In Cortex AgentiX, you can develop and test your playbook content on development machines before using it in a production environment using the remote repository feature. 

 For more information about content management in Cortex AgentiX, see Cortex AgentiX development tenant. 

 Save versions of your playbook in Cortex AgentiX 

 You can save versions of a playbook as you are developing it. When you save a version of a playbook, add a meaningful comment so that you will be able to recognize the changes you made in that version at a later time. The version is saved with the name of the playbook, your commit message, an indication of what the change was (modify, insert), the date the playbook was saved, and the name of the author who last saved it. If necessary, you can access the playbook’s version history and revert your playbook to a previous version. 

 In a playbook, after making changes, click the list next to Save Playbook and then click Save version for current Playbook. 

 Enter a description of the change that was made to the current version. 

 Click Update Playbook. 

 To access a version of a playbook: 

 Click the icon next to New Playbook. The tooltip displays Version history for all Playbooks. 

 Search for the required playbook. The description that was entered when the version was saved should help you locate the version you now require. 

 Click Restore to restore the required version of the playbook. 

 Playbook editing conflict management 

 If multiple users simultaneously attempt to edit the same playbook, they could overwrite each other's changes in the playbook editor. To prevent users from accidentally losing their work, the playbook editor only allows the first user to edit and save. Subsequent users are automatically placed in View Mode Only, and a banner in the playbook editor clearly shows who is currently editing the playbook. The subsequent users can still view, debug, run, duplicate, and download the playbook. 

 Opening a playbook does not immediately lock it. A playbook is considered to be in edit mode only when a user makes a modification that causes the Save button to become available. 

 The playbook is automatically unlocked when the user currently editing the playbook saves the playbook, closes the editor, logs out, or when their session expires. In addition, users with playbook View/Edit and Unlock permission can click Unlock in the banner on the Playbooks page or directly in the playbook editor to force-unlock the playbook. 

 Manually unlocking a playbook may cause version conflicts. This turns off concurrent editing protection, and if the original user is still editing, their changes might be lost or overwritten. 

 The playbook Unlock permission is located under Settings → Configurations → Access Management → Roles. Edit a role and go to Investigation & Response → Automations → Playbooks. Ensure you have View/Edit permissions selected. 

 Previous Troubleshoot playbook performance 

 Next Accelerate playbook development using the Automation Engineer agent (preview) 

 Last updated 1 month ago 

 Was this helpful?

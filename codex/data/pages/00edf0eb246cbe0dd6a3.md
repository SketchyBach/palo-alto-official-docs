---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsoar-8-on-prem/8.13/multi-tenant/child-tenant-management/content-management-in-multi-tenant/sync-content-to-child-tenants
fetched_at: 2026-09-06T10:29:08Z
source: cortex-platform
---

# Sync content to child tenants | 8.13 | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSOAR 8 

 Cortex XSOAR 8 On-prem Documentation 

 8.13 

 Multi-Tenant 

 Child tenant management 

 Content management in multi-tenant 

 Cortex XSOAR 8.13 On-prem 

 Sync content to child tenants 

 Sync content to child tenants in Cortex XSOAR 8.13 On-prem. 

 The content that you sync from the main tenant to the child tenants might add, override, or remove content from the child tenants. New content items, that do not currently exist on the child tenants, are added. When you sync content to child tenants, there can potentially be content items added. 

 Note 

 There may be instances where a child tenant is disconnected for whatever reason when content is supposedly synced. The Cortex XSOAR on-prem main tenant displays the exact reason why the child tenant is disconnected and is unable to receive any updates. We recommend to review the Tenant Management page on the main tenant to resolve the issue. 

 Option 

 Description 

 Add 

 New content items that do not currently exist on the child tenants will be added. 

 Override 

 For content items that are being pushed in the sync operation and that already exist on the child tenants, the sync operation overrides the existing content on the child tenants 

 Remove 

 For content items that were removed from the main tenant and which already exist on the child tenants, the sync operation removes the existing content from the child tenants. 

 You should review each content item and its dependencies before syncing the content. You have the option to remove items before executing the sync operation for a single tenant. 

 Before you begin 

 Ensure that your user roles have view or view/edit permission to sync to child tenants. For more information, see Role-based permissions . 

 Add propagation labels to child tenants. 

 Add propagation labels to content. 

 From the Tenant Management , from the Main Tenant, you can click the link of the child tenant to access the child tenant. 

 How to sync content 

 In the Main Tenant, go to Settings & Info → Settings → Tenant Management . 

 Select the tenant you want to sync. 

 If you select one tenant, you can review which content sync. If you select two or more tenants, you can't review the content before syncing. 

 Select one of the following options to sync content. 

 To review the content before syncing to a child tenant, select a child tenant, and click Sync . 

 Review all content affected by the sync operation in the ADD , OVERRIDE , and REMOVE tabs. 

 If there are playbooks listed in the OVERRIDE tab, select or clear the checkbox to Override playbook inputs in the child tenant. 

 If the Run on field has changed in the script, select or clear the Overwrite script run-on to override this field in the child tenant. 

 To sync content to child tenants without manual review, select two or more child tenants and then click Sync . 

 This option automatically updates new, and existing content to the child tenant, and removes outdated content. If there are playbooks and scripts, select or clear the checkbox to Override playbook inputs and script run-on-settings in the child tenant. 

 Click Sync . 

 Note 

 If you sync a content item from the main tenant to a child tenant, and a content item with that same name already exists on the child tenant, the content on the child tenant is overwritten. This applies to integrations, fields, incident types, and Threat Intel report types. 

 Previous Add propagation labels to a child tenant 

 Next Manage content using a remote repository 

 Last updated 3 hours ago 

 Was this helpful?

---
url: https://cortex-docs.paloaltonetworks.com/cortex-agentix/configure-cortex-agentix/remote-repository-management/set-up-a-remote-repository/set-up-a-built-in-remote-repository
fetched_at: 2026-09-16T08:50:43Z
source: cortex-platform
---

# Set up a built-in remote repository | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex AgentiX 

 Cortex AgentiX Documentation 

 Configure Cortex AgentiX 

 Remote repository management 

 Set up a remote repository 

 Set up a built-in remote repository 

 Set up the built-in remote repository to synchronize Cortex AgentiX content between tenants. 

 The following are typical scenarios for setting up a built-in remote repository for the production and one or more development tenants. 

 Once enabled, development tenants have a red banner on the top left showing DEV . 

 Set up a built-in repository for new Cortex AgentiX development tenants 

 In this scenario, the production tenant is first activated as a standalone (by default), and the built-in remote repository is then enabled in the production tenant (as a pull tenant). Once enabled, the first development tenant becomes the push tenant and any additional tenants become pull tenants. 

 Perform the following procedures in the order listed below. 

 Task 1. Enable the built-in repository in the production tenant. 

 In the production tenant, go to Settings → Configurations → General → Remote Repository Settings and toggle the Content repository slider to enable the remote repository. 

 When set to On , the sync direction is Pull . 

 In the Repository type field, select Built-in , and save the settings. 

 Task 2. Activate a new development tenant in Cortex Gateway for a built-in repository. 

 In Cortex Gateway , locate the Cortex AgentiX production tenant where you enabled the built-in repository in task 1. 

 Hover over the Cortex AgentiX tenant and click Activate Dev Tenant . 

 Define the following fields: 

 Name 

 Details 

 DEV TENANT NAME 

 Give the Cortex AgentiX dev tenant an easily recognizable name. Choose a name that is 59 or fewer characters and is unique across your company account. 

 REGION 

 Select the region in which you want to set up the Cortex AgentiX dev tenant. 

 DEV TENANT SUBDOMAIN 

 Give your Cortex AgentiX dev instance an easy to recognize name that is used to access the tenant directly using the full URL ( https:// <subdomain> agentix. <region> .paloaltonetworks.com ). 

 Select ENABLE CONTENT REPOSITORY . 

 Accept the terms and conditions and activate the tenant. 

 Repeat this task to activate any additional development tenants in Cortex Gateway. They will automatically be set to pull. 

 Set up a built-in repository for existing Cortex AgentiX tenants 

 In this scenario, the production and development tenants were managed in parallel with different sets of content. Since they were already activated in Cortex Gateway, their remote repository settings can only be changed within the tenants. 

 The first tenant that is enabled pushes its content to the remote repository first. For example, these instructions describe enabling the production tenant first, so the remote repository will initially contain production tenant content. You can enable a development tenant first if you want the remote repository to initially contain the content from the development tenant. 

 Perform the following procedures in the order listed below. 

 Task 1. Enable the built-in repository in the production tenant. 

 In the production tenant, go to Settings → Configurations → General → Remote Repository Settings and toggle the Content repository slider to enable the remote repository. 

 When set to On , the sync direction is Pull . 

 In the Repository type field, select Built-in , and save the settings. 

 Task 2. Enable the built-in remote repository in the development tenants. 

 Once enabled, the first development tenant automatically becomes the push tenant. For more details about push and pull tenants, see Cortex development tenant . 

 In the development tenant, go to Settings → Configurations → General → Remote Repository Settings and toggle the Content repository slider to enable the remote repository. 

 When set to On , the sync direction for the first development tenant is Push . The sync direction for any additional development tenants is Pull . 

 In the Repository type field, select Built-in , and save the settings. 

 Select which content to keep and which to overwrite. If there are any discrepancies between the development tenant and remote repository (which in this example initially contains the production tenant content after it is enabled), the Specified repository is not empty window opens. Options are: 

 Existing content on your tenant : Keeps the existing content on your tenant and replaces the content on the specified repository. Cortex AgentiX checks if any other tenants are using the remote repository. If yes, this option is disabled. In this example, the remote repository was already enabled in the production tenant, so the remote repository holds production content. If you want to keep the content on the development tenant: 

 Disable the remote repository in any additional enabled tenants. In this case, for the first development tenant, only the production tenant must be disabled. 

 Select Existing content on your tenant for this tenant. 

 Complete synchronization. 

 Re-enable the remote repository in any additional tenants and select Existing content on the specified repository in each additional tenant. 

 Existing content on the specified repository : Deletes the existing content on your tenant and replaces it with content from the specified repository. 

 Click Continue . 

 Previous Set up a remote repository 

 Next Set up a Private Remote Repository 

 Last updated 21 days ago 

 Was this helpful?

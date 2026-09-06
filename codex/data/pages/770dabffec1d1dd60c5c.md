---
url: https://cortex-docs.paloaltonetworks.com/cortex-xdr-5.x/protect-your-endpoints/install-and-manage-endpoints/manage-endpoint-protection/manage-endpoint-tags/create-an-endpoint-tag
fetched_at: 2026-09-06T09:42:38Z
source: cortex-platform
---

# Create an endpoint tag | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XDR 

 Cortex XDR 5.x Documentation 

 Protect your endpoints 

 Install and manage endpoints 

 Manage endpoint protection 

 Manage endpoint tags 

 Cortex XDR 5.x 

 Create an endpoint tag 

 An endpoint tag can be created during installation of the Cortex XDR agent. 

 An endpoint tag can be created after installation either from the Cortex XDR agent or from the Cortex XDR management console. 

 Add an endpoint tag as an installation parameter of the Cortex XDR agent's installer 

 Installer parameter: run msiexec /i ... ENDPOINT_TAGS="Name1,Name2,Name3" . 

 Cytool argument: cytool endpoint_tags add "tag1 [,tag2,...,tagN]" . 

 Note: 

 Tag names are case sensitive. 

 In Windows and Mac, a tag name can contain spaces. 

 Linux does not support tag names with spaces as command line arguments to the shell installer. Instead, tags can be set in the /etc/panw/cortex.conf configuration file, which supports all Linux installers. 

 Add an endpoint tag after installation 

 From the machine where the Cortex XDR agent is installed: 

 1 

 Navigate to the Cytool folder location and open the CLI as an administrator. 

 2 

 Cytool argument: cytool endpoint_tags add "tag1 [,tag2, ...,tagN]" . 

 Note: 

 Tag names are case sensitive and can contain spaces. 

 From the Cortex XDR management console (Server) 

 1 

 Navigate to Inventory → Endpoints → All Endpoints . 

 2 

 Select one or more endpoints, right-click, and select Endpoint Control → Assign Endpoint Tags . 

 3 

 Select Add tag... and choose one or more tags from the list of existing tags or begin to type a new tag name to Create tag . 

 Note: 

 Tag names are case sensitive and can contain spaces. 

 4 

 (This step requires administrator permissions) To assign the tag to users or user groups, select Add selected tags to Users or Groups , and select the relevant Users and/or User Groups . 

 Note: 

 When SBAC is enabled, assigning tags may impact user permissions. 

 5 

 Click Save . 

 Previous Manage endpoint tags 

 Next Remove an endpoint tag 

 Last updated 1 month ago 

 Was this helpful?

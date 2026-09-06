---
url: https://cortex-docs.paloaltonetworks.com/cortex-agentix/configure-cortex-agentix/users-and-roles-management/roles-management/role-permissions-by-component/marketplace-permissions
fetched_at: 2026-09-06T10:17:31Z
source: cortex-platform
---

# Marketplace permissions | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex AgentiX 

 Cortex AgentiX Documentation 

 Configure Cortex AgentiX 

 Users and roles management 

 Roles management 

 Role permissions by component 

 Cortex AgentiX 

 Marketplace permissions 

 Configure Cortex AgentiX Marketplace permissions for browsing, installing, updating, and managing automation content packs. 

 Configure access to manage content packs in Marketplace. 

 Marketplace is the central hub for discovering, installing, and managing content packs in Cortex AgentiX. Content packs include integrations, playbooks, scripts, dashboards, and other automation content that extend capabilities. Installing a content pack is typically the first step; further configuration of the included integrations or credentials must be completed in the Configurations section. 

 Caution 

 Granting View/Edit access to the Marketplace allows users to install new content packs. As content packs often contain Python scripts and automated playbooks, this permission effectively allows users to introduce new executable code into the tenant. This should be restricted to Security Engineers and Administrators. 

 Permissions 

 Description 

 Roles Example 

 None 

 No access to the Marketplace, and users cannot view content packs. 

 View 

 Read-only access to browse, search, and view pack details and version history. 

 SOC Tier 1, 2, and 3 Analysts, and Threat Hunters: Browse available content and reference content packs during investigations. 

 View/Edit 

 Full access to install, uninstall, upload, and upgrade content packs. Users can also contribute content from other pages (e.g., scripts/playbooks). 

 Security Engineer: Full content management, including custom contributions. 

 Required and recommended permissions 

 Consider adding the following permissions: 

 Permission 

 Permission Level 

 Reason 

 Integrations 

 View 

 Strongly recommended to view and configure installed integration instances. 

 Playbooks 

 Enabled 

 Recommended to view installed playbooks. 

 Scripts 

 Enabled 

 Recommended to view installed scripts. 

 Credentials 

 View 

 Strongly recommended to configure integration credentials. 

 Previous Threat Intelligence permissions 

 Next Exceptions Configuration permissions 

 Last updated 10 days ago 

 Was this helpful?

---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsiam/reference-and-developer-docs/role-based-access-control/configuration-permissions/object-setup-permissions/layout-permissions
fetched_at: 2026-09-06T09:37:38Z
source: cortex-platform
---

# Layout permissions | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSIAM 

 Cortex XSIAM Documentation 

 Reference and developer docs 

 Role-Based Access Control 

 Configuration permissions 

 Object Setup permissions 

 Cortex XSIAM 

 Layout permissions 

 Control access to case and issue layouts, including their layout rules in Cortex XSIAM. 

 Controls access within Object Setup ( Settings → Configurations → Object Setup ) to the following: 

 Case layouts ( Cases → Layouts ): Visual layout definitions that determine how case data is presented when viewing a case. Layouts define which fields are shown, their arrangement in sections/tabs: 

 Case layout rules ( Cases → Layout Rules ): Rules that determine which layout is applied to a given case based on conditions (e.g., case type, source, severity). 

 Issue layouts ( Issues → Layouts ): Visual layout definitions that determine how alert data is presented when viewing an issue. Layouts define which fields are shown, their arrangement in sections/tabs, and widget configurations. 

 Issue layout rules ( Issues → Layout Rules ): Rules that determine which layout is applied to a given issue based on conditions (e.g., issue type, source, severity). 

 Permission 

 Description 

 Roles Example 

 None 

 Users have no access to layout configurations or rules. They can see data rendered in assigned layouts, but cannot modify the definitions 

 SOC Tier-1 Analyst: Layout configuration is an administrative function. 

 Threat Hunter: Layout configuration is outside the threat hunting scope. 

 View 

 Read-only access to all layout definitions and rules. The user can browse the layouts table (cases and issues) and browse layout rules and conditions. 

 SOC Tier-2 and 3 Analysts: May need to understand the layout structure for reporting purposes and to know what data is available in different views. 

 View/Edit 

 Full read/write access to create, edit, copy, and delete custom layouts and layout rules. 

 Security Engineer: Designs and implements custom layouts for alerts and incidents; builds the visual experience. 

 Required and recommended permissions 

 Consider adding the following permissions: 

 Permission 

 Permission level 

 Reasons 

 Cases & Issues 

 View 

 Required to edit layout rules and need to see case/issue data when creating/editing a layout rule. 

 Fields and Types 

 View 

 Required to see available fields when building layouts; essential for layout design. 

 Case Properties 

 View 

 Strongly recommended to understand the case structure (statuses, domains) for layout design. 

 Marketplace 

 View/Edit 

 Recommended to install content packs that include layout definitions. 

 Audit 

 View 

 Recommended to track layout changes. 

 Previous Fields and Types permissions 

 Next Sync Profile permissions 

 Last updated 10 days ago 

 Was this helpful?

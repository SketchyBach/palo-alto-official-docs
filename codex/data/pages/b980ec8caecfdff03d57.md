---
url: https://cortex-docs.paloaltonetworks.com/cortex-agentix/configure-cortex-agentix/users-and-roles-management/roles-management/role-permissions-by-component/configuration-permissions/fields-and-types-permissions
fetched_at: 2026-09-16T08:50:49Z
source: cortex-platform
---

# Fields and Types permissions | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

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

 Configuration permissions 

 Cortex AgentiX 

 Fields and Types permissions 

 Control access to Cortex AgentiX custom fields and indicator types. 

 Controls access to custom fields and indicator types within Object Setup Settings → Configurations → Object Setup : 

 Case fields ( Cases → Fields ): Custom fields that extend the case data schema, appearing in case views, queries, and layouts. 

 Issue fields ( Issues → Fields ): Custom fields for the issue data schema, often used for automation rules and filtering. 

 Indicator fields and types: Definitions for custom indicator fields and new indicator types (e.g., Cloud Resource ID), including extraction regex patterns. 

 Permission 

 Description 

 Roles Example 

 None 

 No access to define fields or types. Users can still view and use existing fields in case/issue views, but cannot modify their definitions 

 SOC Tier 1 Analyst: Schema changes are outside Tier-1 scope; they use existing fields but don't need to see field configuration. 

 View 

 Read-only access to all field definitions and indicator types. Allows exporting definitions to CSV. 

 SOC Tier 2 and 3 Analysts: Need to understand field definitions for advanced queries, custom field usage, and investigation workflows. 

 Threat Hunter: Needs to understand field definitions for hunting queries (XQL) and custom field usage. 

 View/Edit 

 Full read/write access. Users can create, modify, or delete custom fields and indicator types, and write extraction regex. 

 Required and recommended permissions 

 As schema changes impact how data is displayed and analyzed, consider the following dependencies: 

 Permission 

 Permission Level 

 Reasons 

 Cases & Issues 

 View 

 Required to see how fields are used in actual cases/issues. 

 Layouts 

 View 

 Strongly recommended. See how fields are rendered in layouts; needed to design layouts that use custom fields. 

 Case Properties 

 View 

 Strongly recommended. Understand incident structure (statuses, domains) alongside field definitions 

 Threat Intel 

 View 

 Recommended. Understand indicator types and fields in the context of threat intelligence. 

 Audit 

 View 

 Recommended to track field creation/modification history. 

 Marketplace 

 View 

 Recommended to install content packs that include field definitions and indicator types. 

 Previous Exclusion list permissions 

 Next Layout permissions 

 Last updated 20 days ago 

 Was this helpful?

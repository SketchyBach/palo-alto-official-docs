---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsoar-8-on-prem/8.14/multi-tenant/child-tenant-management/content-management-in-multi-tenant/add-propagation-labels-to-content
fetched_at: 2026-09-16T08:53:18Z
source: cortex-platform
---

# Add propagation labels to content |  8.14 | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSOAR 8 

 Cortex XSOAR 8 On-prem Documentation 

 8.14 

 Multi-Tenant 

 Child tenant management 

 Content management in multi-tenant 

 Cortex XSOAR 8.14 On-prem 

 Add propagation labels to content 

 Add content propagation labels in Cortex XSOAR 8.14 On-prem. 

 You can add propagation labels when creating a new content item or when editing an existing item. 

 The default propagation label for all content items is all . 

 Tip 

 We recommend that you first apply propagation labels to your child tenants and then add the corresponding labels to the content items that you want to sync to the tenants. 

 The following content items support propagation labels: 

 Playbooks 

 Scripts 

 Integrations and integration instances 

 Indicator fields, types, and layouts 

 Incident fields, types, and layouts 

 Threat Intel Report types, fields, and layouts 

 Classifiers and mappers 

 Evidence fields 

 Pre-process rules 

 Lists 

 Widgets 

 Dashboards 

 Note 

 When installing a content pack from the Marketplace, the default propagation label is set to all . If you want to change the propagation label, after installation, go to the INSTALLED CONTENT PACKS tab on the Marketplace page and click the propagation button for the content pack. If a content item is part of a content pack and is not specifically labeled, it inherits the content pack’s propagation labels. If labels are specified, it propagates according to those labels. 

 For a non-content item such as an integration instance, if you want to propagate the instance, you need to apply propagation labels both to the integration and to the integration instance. If a tenant does not have the integration installed, the instance will not be propagated even if the propagation label exists both on the main tenant and child tenant. 

 If you want to create new propagation labels or add existing ones, ensure that you have the required permissions. For more information, see Role-based permissions . 

 Go to the content item that you want to add a propagation label to. 

 In the Propagation Labels field, add the relevant labels by either selecting an existing label or typing a new label. After typing a new label and pressing Enter , the label is available immediately for use. If you instead keep the default all label, the content syncs to all child tenants. For example, when editing or creating a playbook, in the PLAYBOOK SETTINGS section, in the Propagation Labels field, add the label as required. 

 Previous Content management in multi-tenant 

 Next Add propagation labels to a child tenant 

 Was this helpful?

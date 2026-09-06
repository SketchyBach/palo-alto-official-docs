---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsoar-8-on-prem/8.13/configure-cortex-xsoar/remote-repository-management/push-content-from-a-development-tenant
fetched_at: 2026-09-06T10:27:23Z
source: cortex-platform
---

# Push content from a development tenant | 8.13 | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSOAR 8 

 Cortex XSOAR 8 On-prem Documentation 

 8.13 

 Configure Cortex XSOAR 

 Remote Repository Management 

 Cortex XSOAR 8.13 On-prem 

 Push content from a development tenant 

 Push content from development in Cortex XSOAR 8.13 On-prem. 

 Once you develop your content, for it to be available as part of a content update for the production tenant, you must push the changes from the development tenant. 

 Considerations for pushing content 

 You should not manually export content from the development tenant to import to the production tenant. Use only the procedures outlined in the documentation to ensure that your content is properly updated in the production tenant. 

 On each page you can decide whether to include or exclude items, which prevents them from being pushed to production, on a temporary or permanent basis. You can only exclude individual content items, not content packs. 

 Content that can be pushed 

 The following types of content can be synchronized between development and production tenants: 

 Note 

 In the production tenant, it is not possible to edit these content items. 

 Scripts 

 Playbooks 

 Integrations: Integration instances are not pushed to the production tenant. Only customized integration YML files are pushed to the production tenant. 

 Classifiers and mappers 

 Content packs: When pushing a content pack to the production tenant, we recommend pushing all of the content for the content pack to work properly. 

 Incidents: Including incident types, fields, and layouts 

 Indicators: Including indicator types, fields, and layouts 

 Evidence fields 

 Pre-processing rules: If you reorder your pre-processing rules you must push all of the pre-processing changes to the production tenant. 

 Lists 

 Reports: When pushing a report to the production tenant, the time range set in the report on the development tenant does not sync with the production tenant. 

 Dashboards 

 Widgets 

 How to push content from a development tenant 

 In the development tenant, go to Settings & Info → Settings . 

 Under the Local Changes section, go to the relevant page according to the items you want to push: 

 Items 

 Content that is not related specifically to a content pack. For example, customized scripts or playbooks. When creating custom content, the content is automatically added here. If you have already pushed a content pack and later edit one of its content items, the edited items appear in the Content Pack Items page, not the Content Packs page. 

 Content Packs 

 All of the content that is specific to the content packs you installed from Marketplace. 

 Content Pack Items 

 If you do not want to install the whole content pack, you can install specific items in the content pack. 

 Select the items you want to push to production, and click Push . 

 If the items have dependencies, review the contents and click Push 

 Sometimes you may not want to push all content, content pack dependencies, etc. For example, when a user makes a change in a playbook that includes a script dependency to which another user is adding a feature, and the change does not require the new feature (version) of the script, you can push the playbook without the new script. 

 In the dialog box, add an optional message and click Push . 

 On the production tenant, Install content on the production tenant . 

 Previous Set up a private remote repository 

 Next Install content on a production tenant 

 Last updated 1 month ago 

 Was this helpful?

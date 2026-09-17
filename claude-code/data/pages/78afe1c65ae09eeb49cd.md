---
url: https://cortex-docs.paloaltonetworks.com/xsoar-6-administrator-guide/6.14/onboard-cortex-xsoar/marketplace/content-pack-contributions
fetched_at: 2026-09-16T08:56:11Z
source: cortex-platform
---

# Content Pack Contributions | 6.14 | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSOAR 6 

 Cortex XSOAR 6 Administrator Guides 

 6.14 

 Onboard Cortex XSOAR 

 Marketplace 

 Cortex XSOAR 6.14 

 Content Pack Contributions 

 Create and submit content packs to the Cortex XSOAR 6.14 Marketplace. 

 Contributions are content packs that you create for the Cortex XSOAR marketplace, which are submitted to Cortex XSOAR for review and approval. After approval, these content packs are uploaded to the Marketplace , and are shared and installed like any other content pack. When creating new content such as playbooks, automations, incident types, and integrations, or when updating content, you can: 

 Create and submit content directly from Cortex XSOAR. For example, from a Playbook, click Contribute . You then have the option to submit the contribution for review or download the contribution and upload it, for example, to GitHub. 

 Submit a content pack of one or more items through the Cortex XSOAR Marketplace UI. When you create or edit content in Cortex XSOAR, that content is added to the Add Content section in the CONTRIBUTIONS tab in the Marketplace. You can add content from this list to a content pack. From the CONTRIBUTIONS tab in the Cortex XSOAR Marketplace, you can create, edit, submit, and delete content that you have submitted through the Marketplace. 

 Create a GitHub pull request on the public XSOAR Content Repository. 

 Users with the Contribute to Marketplace permission can contribute content packs to the Marketplace. 

 When adding content to the content pack, Cortex XSOAR scans the content and automatically adds dependencies, which ensures that the content pack installs and runs correctly on all environments. 

 Although Cortex XSOAR scans and tests the content to ensure it works correctly, you need to review the content to ensure that all dependencies are incorporated and work as they should in the event that not all dependencies are added automatically. For example, when adding a phishing playbook, the incident type and layout should be automatically added. This enables you to add a phishing dashboard. 

 Validation 

 Content validation enables users to improve the quality of the content they develop in Cortex XSOAR by running an automation script to check for errors before submission. 

 Configuration 

 By default, content validation passes your content item(s) as inputs to the ValidateContent script included in the Base pack. The ValidateContent script uses the demisto-sdk utility to run validate and lint on the content item(s) and returns the results. You can also create your own validation script and set the automation as the default by adding a server configuration. To add a server configuration, go to Settings → About → Troubleshooting → Add Server Configuration . 

 Key 

 Description 

 content.item.validate.script 

 Sets the automation used for Content Validation. 

 Value: name of the automation 

 content.item.validate.script.use_system_proxy 

 Sets whether the default automation uses the system proxy. Default is no. 

 content.item.validate.script.trust_any_certificate 

 Sets whether the default automation trusts any certificate. Default is no. 

 Automatic 

 When contributing content, either from the Contributions page, the Contribution Pack Editor page or directly from a content item's drop-down menu, the content goes through content validation before submission. After clicking Contribute , you have the option to Save and submit your contribution or Save and download your contribution . In both cases, your contribution goes through validation before you submit or download the content. 

 review-contribution-marketplace.png 

 If the content pack passes validation, the process continues. If you are downloading the content, a download will start automatically. If you are submitting the content, the content will submit automatically. If the content pack does not pass validation, the validation issues are listed, and you have the option to export a raw JSON file with the error details. You can then make changes to your content items and resubmit for validation. 

 You also have the option to skip the validation step or to contribute a content pack that does not pass validation. For example, there might be an issue you are aware of that cannot yet be resolved. For a large content pack, where you have already validated the individual content items, you might want to skip the final validation as it can be a lengthy process for a large content pack. 

 validation-results-marketplace.png 

 You can also manually trigger content validation. The Validate button appears in the Contribution page, the Contribution Pack Editor page, as well as in both the Automation and Integration Editors. With manual validation, you can check your content during the development process and make changes. 

 Review Process 

 The review process consists of the Cortex XSOAR team checking that your contribution meets code, documentation, naming, and other standards. You receive a form to complete asking for more information, such as certification, contact details, etc. The Cortex XSOAR team will be in touch with you during the review process. 

 During the review process, you may be asked to make changes in the code, or provide more data, metadata, dependencies, documentation, support and certification model, etc. You can anonymize your name if required. 

 When your contribution is approved, it is uploaded to the Marketplace where other Cortex XSOAR users can view, download, and rate it. We encourage you to learn more about the contribution process . 

 Previous Marketplace Troubleshooting 

 Next Create a Content Pack 

 Last updated 14 days ago 

 Was this helpful?

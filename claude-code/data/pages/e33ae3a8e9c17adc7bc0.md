---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsiam/cloud-security/base-images-rule/create-a-base-images-rule
fetched_at: 2026-09-06T09:36:19Z
source: cortex-platform
---

# Create a base image rule | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSIAM 

 Cortex XSIAM Documentation 

 Cloud Security 

 Base image rules 

 Create a base image rule 

 Create and manage Cortex XSIAM base image rules for scanned registry images, including filters, previews, and rule updates. 

 Before creating a rule, ensure: 

 container registries are onboarded and actively scanned in your environment. 

 you have View/Edit permission for Compute Policies or the Instance Administrator role to create or manage a Base Images Rule . 

 You can create a Base Images rule from either Rules & Policies or a Registry Image Asset Card . 

 How to create a base images rule from Rules & Policies : 

 Navigate to Posture Management → Rules & Policies → Rules → Base Images . 

 Select + Create Rule . 

 Enter a Name and optional Description for the rule. 

 Define the filter conditions, such as: 

 Registry URL (for example, https://docker.io ) 

 Repository name. 

 (Optional) Refine the filter conditions by adding additional conditions, such as: 

 Image Name 

 Image Tag (for example, latest ). 

 You can use supported operators such as Equals , Not Equals , Contains , Not Contains , starts with, and ends with to specify the conditions. 

 Select Run Preview to view matching images. 

 Select Create to add the rule. 

 The rule is automatically applied to all existing and future images that match the defined criteria. After you create or modify a Base Images rule, it can take up to 6 hours for the system to apply the changes and update the relationships across your assets. 

 Create a base image rule from a registry image asset card 

 Navigate to Inventory → Assets → All Assets → Compute → Container Images . 

 Filter Asset Type = Registry Image . 

 Select a registry image row to open the details pane 

 Select the More options ( ⋮ ) menu. 

 Choose Add base image rule . The Base Image Rules page opens with conditions pre-populated based on the selected image. 

 Modify the conditions if required. 

 Select Run Preview to view matching images. 

 Select Create to add the rule. 

 The rule is automatically applied to all existing and future images that match the defined criteria. After you create or modify a Base Images rule, it can take up to 6 hours for the system to apply the changes and update the relationships across your assets. 

 Manage a Base Images rule 

 To manage a Rule, follow these steps: 

 Navigate to Inventory → Assets → All Assets → Compute → Container Images . 

 Find the Base Images from the list of rules, or use the filter to search. 

 Select the rule row to open the details pane 

 Select the More options ( ⋮ ) menu. 

 Actions 

 Instructions 

 Edit 

 Modify the existing Base Images rule. 

 Save as new 

 Create a new rule using the existing Base Images rule as a template. 

 Delete 

 Remove the Base Images rule. 

 Previous Base image rules 

 Next Find the base image for an asset 

 Last updated 13 days ago 

 Was this helpful?

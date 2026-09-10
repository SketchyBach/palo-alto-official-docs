---
url: https://cortex-docs.paloaltonetworks.com/cortex-cloud-runtime-security/endpoint-security/install-and-manage-endpoints/manage-endpoint-protection/manage-endpoint-prevention-profiles
fetched_at: 2026-09-06T09:54:05Z
source: cortex-platform
---

# Manage endpoint prevention profiles | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex Cloud 

 Cortex CLOUD Runtime Security 

 Endpoint security 

 Install and manage endpoints 

 Manage endpoint protection 

 Cortex Cloud Runtime 

 Manage endpoint prevention profiles 

 Manage endpoint prevention profiles by viewing their policy usage, editing their settings, or creating policy rules. 

 Go to Inventory → Endpoints → Policy Management → Prevention → Profiles . 

 Check profile usage 

 Check which policy rules use a profile before you modify or delete it. 

 Right-click the profile, then select View Policy Rules . 

 Cortex Cloud opens a filtered Prevention Policy Rules tab. It shows only rules using that profile. 

 Manage a profile 

 Edit 

 Right-click the profile, then select Edit . 

 Make your changes, then click Save . 

 Export 

 Right-click the profile, then select Export Profile . 

 Click Export to download the profile. 

 Duplicate 

 Right-click the profile, then select Save as New . 

 Edit the name, description, and any settings. 

 Click Create . 

 Create a policy rule with the new profile. 

 Delete 

 You can delete a profile only when its Usage Count is 0 . 

 Delete or detach every policy rule that uses the profile. 

 Locate the profile and confirm its Usage Count is 0 . 

 Right-click the profile, then select Delete . 

 Click Yes to confirm. 

 Create a policy rule from a profile 

 1 

 Right-click the profile, then select Create a new policy rule using this profile . 

 Cortex Cloud sets the platform from the profile configuration. It also assigns the profile by type. 

 2 

 Enter a Policy Name . Optionally, add a description. 

 3 

 Assign additional profiles, then click Next . The endpoint list opens. 

 4 

 Select target endpoints. Alternatively, use filters to define the policy criteria. Click Next . 

 5 

 Review the policy rule summary, then click Done . 

 Previous Set an alias for an endpoint 

 Next Create a new prevention policy rule for serverless function 

 Last updated 1 month ago 

 Was this helpful?

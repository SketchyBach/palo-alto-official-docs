---
url: https://docs.prismacloud.io/content-collections/runtime-security/configure/tags
fetched_at: 2026-09-16T13:35:19Z
source: prisma-cloud
---

# Tags | Prisma Cloud arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Enterprise Edition 

 Content Collections 

 Runtime Security 

 Configure 

 Tags 

 Tags are predefined labels that can help you manage the vulnerabilities in your environment. They are centrally defined and can be set to vulnerabilities and as policy exceptions. 

 Tags are used as: 

 Vulnerability labels. They provide a convenient way to categorize the vulnerabilities in your environment. 

 Policy exceptions. They can be a part of your rules to have a specific effect on tagged vulnerabilities. 

 Tags are useful when you have large container deployments with multiple teams working in the same environment. For example, you might have different teams handling different types of vulnerabilities. Then you can set tags to define responsibilities over vulnerabilities. Other uses would be to set the status of fixing the vulnerability or to mark vulnerabilities to ignore when there are known problems that can’t be fixed in the near future. 

 For tags that are not used as policy exceptions, all user roles that can view the scan results and have the Collections and Tags permission, are allowed to assign these tags on CVEs. Assigning tags that are used as policy exceptions is allowed only for Admin, Operator, and Vulnerability Manager user roles. Custom roles aren’t allowed to set these tags, regardless of their other permissions. 

 Tag Definition 

 You can define as many tags as you like. 

 To define a new tag, navigate to Manage > Collections and Tags > Tags . 

 Prisma Cloud ships with a predefined set of tags: Ignored, In progress, For review, and DevOps notes. The predefined tags are editable, and you can use them according to your needs. 

 Click Add Tag . 

 In the Create new tag dialog, enter a name and description. 

 Pick a color for easy visibility and differentiation. 

 Click Save . 

 Tag assignment 

 You can assign tags to vulnerabilities, and specify their scope based on CVE ID, packages and resources. Alternatively, you can manually tag vulnerabilities from scan reports . 

 Note that a tag assignment is uniquely identified by a tag, CVE ID, package scope, and resource type, therefore, you can not create multiple tag assignments for the same tag, CVE ID, package scope, and resource type. To extend the scope of a tag applied to a CVE, edit its existing tag assignment to apply to more packages or resources. 

 For example, assign the tag Ignored to CVE-2020-1971 , package openssl , and all ubuntu images as follows: 

 You can also adjust the scope of a tag assigned either from the tags management page or from scan reports. Click the Edit button to start editing the tag assignment. For example, extend the scope of the tag Ignored for CVE-2020-1971 to all packages affected by this CVE by changing the Package scope : 

 As another example, after the In progress tag was assigned to CVE-2019-14697 for specific alpine images from the scan reports, you can extend its scope so it will apply to all alpine images and their descendant images: 

 To easily navigate in multiple tag assignments, use the table filters on the Tag assignment table. Filter by CVE ID, tag, package scope, and resource type to quickly find all places a tag applies to. 

 To assign a tag to a vulnerability, navigate to Manage > Collections and Tags > Tags . 

 Click Assign Tag . 

 In Tag , select the tag to assign. 

 In CVE , select the CVE ID to assign the tag for. 

 In Package scope , select the package to which the tag should apply. You can select All packages to apply the tag to all the packages affected by the CVE. 

 In Resource type , select the type of resources to assign the tag for. You can select All resources to apply the tag to all the resources across your environment. 

 VMware Tanzu droplets and running applications are being referenced as Images . 

 Once a resource type is selected, specify the resources to which the tag should apply under Images , Hosts , Functions , or Code repositories . Wildcards are supported. 

 (Optional) For images, turn on the Tag descendant images toggle to let Prisma Cloud automatically tag this CVE in all images where the base image is one of the images specified in the Images field. 

 For Prisma Cloud to be able to tag descendant images, first identify the base images in your environment under Defend > Vulnerabilities > Images > Base images . 

 (Optional) In Comment , specify a comment for this tag assignment. 

 Click Save . 

 Previous Collections 

 Next WildFire Settings 

 Last updated 1 month ago 

 Was this helpful?

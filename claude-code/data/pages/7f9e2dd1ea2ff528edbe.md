---
url: https://docs.prismacloud.io/content-collections/connect/connect-cloud-accounts/onboard-aws/update-onboarded-aws-accnt-to-org
fetched_at: 2026-09-16T13:34:55Z
source: prisma-cloud
---

# Update an Onboarded AWS Account to AWS Organization | Prisma Cloud arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Enterprise Edition 

 Content Collections 

 Connect 

 Connect Cloud Accounts 

 Onboard AWS 

 Update an Onboarded AWS Account to AWS Organization 

 If you had previously onboarded an individual AWS account as type Account and now you want to onboard the same account as type Organization , you can do so without losing any changes to the onboarded account and assigned account groups. 

 On Settings > Providers > Cloud Accounts , identify the account which you want to update from Account to Organization type. 

 Select Connect Provider > Cloud Account . 

 Select AWS 

 Select Organization . 

 Enter an Account Name . 

 You can enter the same Account Name as the one you had entered while onboarding as account or enter a different name. 

 Select the Security Capabilities and Permissions that you want to enable. 

 Click Next . 

 While configuring the account, if you want to retain the existing role name and external ID for a member account when you move that account from standalone to under an organization, select the Preserve Role ARN and External ID of already onboarded accounts that belong to this Org checkbox under Advanced Settings . 

 In the future, if you want to update the member CFT for which the role name and external ID was retained when it is moved from standalone to under an organization, you have to download CFT using download CFT API and update the corresponding stack in your AWS console. 

 The role name and download CFT for these members is not available in the UI. 

 You need to save these values or you can contact Prima Cloud customer support. 

 You will not be able to change these member role names unless you deselect the Preserve Role ARN and External ID of already onboarded accounts that belong to this Org checkbox. 

 Download IAM Role CFT and complete the required Steps . 

 Select All member accounts. 

 Make sure you assign the same Account Group that you had assigned when you had onboarded as an account. 

 Click Next . 

 Review Status of your AWS organization. 

 Click Save . 

 After successfully onboarding the account, you will see it onboarded as an Organization on the Cloud Accounts page. 

 Previous Update an Onboarded AWS Account 

 Next AWS APIs Ingested by Prisma Cloud 

 Last updated 3 months ago 

 Was this helpful?

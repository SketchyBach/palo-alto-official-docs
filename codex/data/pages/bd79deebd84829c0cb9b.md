---
url: https://docs.prismacloud.io/content-collections/governance/create-an-iam-policy
fetched_at: 2026-09-16T13:35:01Z
source: prisma-cloud
---

# Create an IAM Policy | Prisma Cloud arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Enterprise Edition 

 Content Collections 

 Governance 

 Create an IAM Policy 

 Prisma Cloud provides the ability to create custom IAM policies to fulfill your organization’s IAM requirements. You can build a new IAM policy based on the config from iam RQL query and monitor the identities across your cloud environment. 

 Select Governance . 

 Select Add Policy > IAM . 

 Enter your policy details— Policy Name and Severity . 

 (Optional) Add a Description and Labels . 

 Check Use Group/Cloud Service Account as violating resource if you wish to view alert results on AWS role, Azure service principal or GCP account group. 

 Select Next and build your RQL query. 

 The default option of New Search enables you to build a new RQL query from scratch while Saved Search enables you to use a RQL query that you previously saved. For example: 

 config from iam where source.cloud.service.name = 'iam' and source.cloud.resource.type = 'user' and source.cloud.resource.name = 'my-user' 

 Returns the net effective permissions of a user in your cloud account named my-user . 

 config from iam where grantedby.cloud.entity.type = 'group' AND source.cloud.resource.type = 'user' 

 Lists all effective permissions that have been granted to a user by any AWS IAM group. 

 A green check mark displays if you entered a valid query. 

 Select the search button. 

 Save the policy. 

 After you successfully create your new policy, it displays on the Policies page. 

 Use the Filter to search for custom or default (out-of-the-box) policies. 

 Previous Prisma Cloud Threat Detection 

 Next Create a Network Exposure Policy 

 Last updated 1 month ago 

 Was this helpful?

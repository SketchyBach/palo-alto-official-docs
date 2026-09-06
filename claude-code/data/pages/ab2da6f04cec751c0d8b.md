---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsoar-8-saas/multi-tenant/onboard-cortex-xsoar-multi-tenant/step-2.-create-a-child-tenant
fetched_at: 2026-09-06T10:23:23Z
source: cortex-platform
---

# Step 2. Create a child tenant | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSOAR 8 

 Cortex XSOAR 8 SaaS Documentation 

 Multi-Tenant 

 Onboard Cortex XSOAR multi-tenant 

 Cortex XSOAR 8 (SaaS) 

 Step 2. Create a child tenant 

 Create and activate Cortex XSOAR 8 SaaS child tenants in Cortex Gateway for a multi-tenant deployment. 

 After you have set up the main tenant, you can set up child tenants in Cortex Gateway. You can create as many child tenants as you require, subject to your license. 

 The Main Account (main tenant) is labeled in the Cortex Gateway, but child tenants are not labeled. 

 Cortex enables parent-child pairing between tenants located in different geographical regions. To enable this capability, contact your support team. 

 To create a child tenant, ensure that you have Account Admin permissions. 

 In Cortex Gateway, you can view all the available tenants. If you want to create more child tenants than your license permits, contact Customer Support. 

 In Cortex Gateway, hover over the main tenant you activated previously, on the right-hand side, click the ellipsis, and then click Add Child Tenant . 

 mt-activation.png 

 Add the following details. 

 Parameter 

 Description 

 Child Tenant Name 

 Give the Cortex XSOAR tenant an easily recognizable name. 

 Choose a name that is 59 or fewer characters and is unique across your company account. 

 Region 

 View the region for the child tenant. This can't be changed. 

 Child Tenant Subdomain 

 Give your Cortex XSOAR instance an easy-to-recognize name that is used to access the tenant directly using the full URL. 

 https://<subdomain>.crtx.< region >.paloaltonetworks.com 

 Note 

 This is a public FQDN, so be careful with sensitive information such as the company name. 

 After activating a child tenant, you can't change the child tenant Subdomain. 

 Incident Retention Licenses 

 If you have incident retention licenses available, assign one or more incident retention licenses to the child tenant. For more information, see Step 3. Allocate incident retention licenses . 

 Click the box to verify you understand that licenses cannot be removed or reallocated without contacting Customer Support. 

 Activate the child tenant and confirm approval. 

 Activation can take up to an hour. You should receive notification by email that the child tenant has completed the activation process. 

 (Optional) Add another child tenant by repeating step 2 or access your newly created tenant. 

 In the Cortex Gateway, under your main tenant, you can see the total number of tenants you are licensed for and how many you have created. 

 If you reach your limit for child tenants, depending on your license, you may be able to create more tenants. You may be charged for additional tenants. Contact Customer Support if you are approaching your authorized limit. 

 Previous Step 1. Activate Cortex XSOAR (Main Tenant) 

 Next Step 3. Allocate incident retention licenses 

 Last updated 5 days ago 

 Was this helpful?

---
url: https://docs.paloaltonetworks.com/cloud-ngfw-aws/reference/credit-distribution/cloud-ngfw-procurement-and-management-with-legacy-cloud-ngfw-credits
fetched_at: 2026-08-13T15:34:29Z
source: palo-alto-main
---

# Cloud NGFW Procurement and Management with legacy Cloud NGFW Credits Clear

Cloud NGFW Procurement and Management with legacy Cloud NGFW Credits 

 Home 

 EN

 Location 

 Documentation Home 

 Palo Alto Networks 

 Support 

 Live Community 

 Knowledge Base 

 >

 Strata Copilot

 Cloud NGFW Procurement and Management with legacy Cloud NGFW Credits 

 Updated on 

 Thu Aug 06 08:11:58 PDT 2026 

 Focus 

 Download PDF 

 English 

 日本語 (Japanese) 

 Français (French) 

 Deutsch (German) 

 Filter

 Expand All 
 | 
 Collapse All 

 Cloud NGFW for AWS Docs 

 Getting Started 

 Deployment 

 Administration 

 Reference 

 Release Notes 

 New Features 

 Updated on 

 Thu Aug 06 08:11:58 PDT 2026 

 Focus 

 Home 

 Cloud NGFW for AWS 

 Software NGFW Credit Distribution and Management 

 Cloud NGFW Procurement and Management with legacy Cloud NGFW Credits 

 Download PDF 

 English 

 日本語 (Japanese) 

 Français (French) 

 Deutsch (German) 

 Cloud NGFW for AWS 

 Cloud NGFW Procurement and Management with legacy Cloud NGFW Credits 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Cloud NGFW for AWS Docs 

 Getting Started 

 Deployment 

 Administration 

 Reference 

 Release Notes 

 New Features 

 Previous 

 Cloud NGFW Procurement and Management with Software NGFW Credits 

 Next 

 Edit Deployment Profiles in Credit Management System (CMS) 

 Cloud NGFW Procurement and Management with legacy Cloud NGFW Credits 

 Interchange and allocate credits among your Cloud NGFW resources regardless of the
 Cloud deployment method. 

 Activate (legacy) Cloud NGFW Credits 

 Once you book the order for credits, they become active immediately, and an email
 is sent to enable you to start using your credits; for example, if you purchased
 credits for a one year term on September 6, 2026, the credits are active from
 that day forward, while the term lasts, in the case of this example, until
 September 5, 2027. The person listed as the administrative contact in the quote
 receives the activation email. The email provides details about the
 subscription, the credit pool ID, the subscription start and end date, the
 number of credits purchased, and the description of the default credit pool. You
 can use these details to activate credits in your Customer Support Portal (CSP) account. 

 Palo Alto Networks recommends retaining this email to
 access information related to your account. 

 You will select one of your CSP accounts for the credit pool during activation.
 Once your credit pool is active, you can manage and allocate the credits to your
 Cloud NGFW tenants using the Credit Management Application described below. 

 In the email, click Activate . 

 After clicking Activate , you’re redirected to the
 CSP. Select the CSP account in which you want to activate the credits. 

 Select Start Activation to start using your credits
 by depositing them into the CSP and allocating the credits. 

 Select the Palo Alto Networks Customer Support portal account (you can
 search by account number or name) where you want to deposit the credits and
 click Deposit Credits : 

 You can view your deposited credits in the customer support portal
 (CSP): 

 In the CSP, within the left navigation panel go to
 Product , select Software/Cloud
 NGFW Credits . 

 If there is an active contract, the credit pool is visible on this
 page. 

 Use the Account Selector field to ensure
 that you're viewing the correct account. Select Go to
 Details for a specific pool to see more granular
 information, such as the deployment profiles (also known as parent
 deployment profiles) associated with that pool. 

 Click Go to Cloud NGFW Credits to access the Cloud
 NGFW Credit Management application in the Palo Alto Networks hub . 

 Associate Software NGFW Credits with Cloud NGFW tenant 

 Do the following: 

 Step 1: Create a Parent Deployment Profile in
 Customer Support Portal 

 Step 2: Create a Child Parent
 Deployment Profile in Credit Management Application 

 The Cloud NGFW Credit Management Application 
 provides a single location where you can manage your purchased credit pools,
 create deployment profiles and associate them with your Cloud NGFW
 tenants. 

 In the hub, click Cloud NGFW Credit Management 
 to display the app: 

 The Cloud NGFW Credit Management application displays the
 credit pools associated with the CSP account: 

 Each credit pool, displayed as an individual tile, provides two
 options: 
 Check Details . Use this option to
 display information about the credit pool. If a deployment
 profile already exists, it appears in the
 Deployment Profile table: 

 Create Deployment Profile . Use this
 option to create a deployment profile to consume activated
 credits from the pool. 

 Before you create a
 deployment profile, estimate the number of firewalls that will
 use the configuration. You don't have to deploy all the
 firewalls at once. 

 Click Create Deployment Profile . In the
 Create Deployment Profile screen, specify the
 following information: 

 In the Name field, use the drop-down
 menu to select the Credit Pool ID from
 the list of available options. Enter the corresponding name for
 the credit pool ID. 

 Select the Cloud Type (either Amazon Web
 Services or Microsoft Azure). 

 Use the drop-down menu to select the Cloud NGFW
 Serial Number . 

 If you don't see a Cloud NGFW
 Serial number in the drop down, it's because of the
 following reasons: 
 Your firewall in the Cloud Service Provider’s portal
 isn't registered to the Palo Alto Networks CSP where
 your credit is deposited. In this case, go to the
 Cloud Service Provider’s portal and register the
 firewall to the CSP account. 

 Your firewall is registered in a different CSP
 account that you're not part of. In this case, add
 yourself as an admin to the CSP account and visit
 the deployment profile screen again. It should
 display the serial number. 

 Specify the Number of Credits you want
 to allocate from the credit pool; the number of available
 credits from the credit pool appears. 

 Optionally include a description. 

 Click Save . 

 After you have successfully created the deployment profile, the
 CNGFW Credits page displays the newly
 created profile along with the number of allocated credits: 

 Previous 

 Cloud NGFW Procurement and Management with Software NGFW Credits 

 Next 

 Edit Deployment Profiles in Credit Management System (CMS) 

 On This Page 

 Activation & Onboarding 

 Strata Cloud Manager 

 Activate a License or Product 

 Cloud Identity Engine 

 Strata Logging Service 

 Device Associations 

 Hub 

 Identity and Access Management 

 Tenant Management 

 Next-Generation Firewalls 

 AIOps for NGFW 

 Cloud Management for NGFWs 

 Cloud NGFW for AWS 

 Cloud NGFW for Azure 

 Firewalls 

 PAN-OS 

 PAN-OS SD-WAN 

 Service Provider 

 Cloud-Delivered Security Services 

 Advanced WildFire 

 Advanced URL Filtering 

 Advanced Threat Prevention 

 Advanced DNS Security 

 Device Security 

 Enterprise DLP 

 SaaS Security 

 Network Security 

 Shared Policy for NGFWs and Prisma Access 

 Best Practices 

 Best Practices Library 

 Experts Corner 

 Solutions Docs from Product Experts 

 Cloud NGFW for AWS 

 AWS 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

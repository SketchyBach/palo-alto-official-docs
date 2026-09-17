---
url: https://docs.prismacloud.io/content-collections/data-security-posture-management/prisma-cloud-dspm-deployment/deploy-prisma-cloud-dspm-on-microsoft-365/onboarding-microsoft-365
fetched_at: 2026-09-16T13:35:51Z
source: prisma-cloud
---

# Onboarding Microsoft 365 | Prisma Cloud arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Enterprise Edition 

 Content Collections 

 Data Security Posture Management 

 Prisma Cloud DSPM Deployment 

 Deploy Prisma Cloud DSPM on Microsoft 365 

 Onboarding Microsoft 365 

 Architecture 

 The image below depicts the deployment architecture. 

 Roles and Permissions 

 Below is a list of the roles Prisma Cloud DSPM uses to access your environment and the permissions they have. Permissions are used to access different types of data, or perform actions such as creating/deleting virtual machines (VMs), exporting snapshots, etc. 

 IMPORTANT 

 If your Microsoft 365 account has any firewall or network restrictions in place, it is imperative to grant access to the following Prisma Cloud DSPM IP addresses: 

 EU: 

 52.48.123.3 

 99.80.210.235 

 34.247.249.123 

 USA: 

 54.225.205.121 

 18.214.146.232 

 3.93.120.3 

 Environment 

 Permissions 

 Description 

 Prisma Cloud DSPM (External) 

 User.Read.All (Graph) 

 Identify guest users (future risks) 

 Prisma Cloud DSPM (External) 

 Group.Read.All (Graph) 

 Identify the groups containing guest users (future risks) 

 Prisma Cloud DSPM (External) 

 Directory.Read.All (Graph) 

 Retrieve domain information 

 Prisma Cloud DSPM (External) 

 Application.Read.All (Graph) 

 Identify application permissions (future risks) 

 Prisma Cloud DSPM (External) 

 Sites.Read.All (Graph) 

 Discover all sites 

 Prisma Cloud DSPM (External) 

 Sites.Read.All (SharePoint API) 

 Get site configurations 

 Prisma Cloud DSPM (External) 

 Sites.Manage.All (SharePoint API) 

 Get site’s external sharing configuration to identify publicly exposed files 

 Prisma Cloud DSPM (External) 

 Files.Read.All (Graph) 

 Read metadata on files including MIP labels 

 Prisma Cloud DSPM (External) 

 SharePointTenantSettings.Read.All (Graph) 

 Read org-level config for External Sharing 

 Prisma Cloud DSPM (External) 

 InformationProtectionPolicy.Read.All (Graph) 

 Read MIP labels policies 

 Customer (Internal) 

 Files.Read.All (Graph) 

 Classification 

 Customer (Internal) 

 Sites.Read.All (Graph) 

 Classification 

 Customer (Internal) 

 Content.SuperUser (RMS) 

 Read RMS encrypted files (future) 

 Prerequisites 

 Prisma Cloud DSPM Orchestrator must be deployed in the same Azure tenant where the Microsoft 365 domain is hosted. 

 The user running the script must have the Application.ReadWrite.All permission. 

 Onboarding Steps 

 Sign in to your Prisma Cloud DSPM account. 

 From the left menu, select Settings. 

 Under Integrations, go to the Microsoft 365 option, and click Configure. 

 Click Add New. 

 In the Microsoft 365 Connect New Subscription window, do the following: 

 Enter the required details. 

 Select the orchestrator and the region 

 Choose the environment type) 

 Grant approval for the enterprise application. Ensure that you are signed in to the tenant associated with the Microsoft 365 instance you wish to onboard. This tenant should also correspond to the one in which the Orchestrator was deployed. 

 The Approval screen opens in a new tab. Follow the provided steps until you reach the Success screen. 

 In Prisma Cloud DSPM, choose the Enable option (step 3). 

 Copy the provided PowerShell script and execute it in the Azure PowerShell console . 

 Wait until the script successfully completes, and return to Prisma Cloud DSPM. 

 Previous Deploy Prisma Cloud DSPM on Microsoft 365 

 Next Offboarding a DSPM Project 

 Last updated 1 month ago 

 Was this helpful?

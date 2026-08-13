---
url: https://docs.paloaltonetworks.com/prisma-access-browser/integrations/cloud-storage-integrations/cloud-provider-microsoft-onedrive
fetched_at: 2026-08-13T17:23:42Z
source: palo-alto-main
---

# Cloud Provider - Microsoft OneDrive Clear

Cloud Provider - Microsoft OneDrive 

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

 Cloud Provider - Microsoft OneDrive 

 Updated on 

 Tue Jul 28 09:39:05 PDT 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma Browser Docs 

 Activation & Onboarding 

 Getting Started 

 Deployment 

 Administration 

 Integrations 

 User Guide 

 Updated on 

 Tue Jul 28 09:39:05 PDT 2026 

 Focus 

 Home 

 Prisma Browser 

 Cloud Storage Integrations 

 Cloud Provider - Microsoft OneDrive 

 Download PDF 

 Prisma Browser 

 Cloud Provider - Microsoft OneDrive 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma Browser Docs 

 Activation & Onboarding 

 Getting Started 

 Deployment 

 Administration 

 Integrations 

 User Guide 

 Cloud Provider - Microsoft OneDrive 

 This document contains the directions for integrating Microsoft OneDrive as the cloud
 provider 

 Microsoft OneDrive Prerequisites 

 These are the prerequisites for configuring Microsoft OneDrive as your cloud
 provider: 

 Global Administrator access in Azure Active Directory (AD) 

 End users require a valid Microsoft 365 license: 
 Microsoft 365 Business Basic /Standard / Premium 

 Microsoft 365 Apps for Business 

 Microsoft 365 E3 / E5 

 Configure Microsoft OneDrive as the Cloud Provider 

 Register a new app in Azure. 

 Sign in to the Azure Portal . 

 Go to Azure Active Directory → App registrations → + New
 registration . 

 Enter a descriptive name (for example, Prisma Browser Cloud
 Storage for M365 ) 

 Choose Single tenant 
 (Accounts in this organizational directory
 only) . 

 Under Redirect URI , select Single-page application
 (SPA) and use this URI:
 https://gdhaibkimkeghllnpodfpoamchapggea.chromiumapp.org/ 

 Click Register . 

 Add Permissions to the New App. 

 Open the new app → App permissions → + Add a
 permission . 

 Choose Microsoft Graph . 

 Add the following Application permissions: 

 Application.Read.All 

 DelegatedPermissionGrant.Read.All 

 Click +Add a permission → Microsoft Graph → Delegated
 permissions . 

 Add the following permission: 

 Files.ReadWrite.All 

 Click Grant admin consent for <your tenant name> Click
 Yes in the consent confirmation pop-up. 

 User.Read
 permission (delegated) is added by default by the
 application. DO NOT REMOVE THIS PERMISSION. 

 WHY ARE THESE PERMISSIONS NEEDED? 

 Prisma Browser requires specific permissions. These are the
 minimum necessary to ensure proper connection and to manage file
 downloads to your organization's cloud storage. This
 least-privilege approach minimizes security risks by only
 requesting access essential for its operation. 

 Permission Type Permission Name Reason 

 Delegated User.Read Confirms that the user connected to the browser is
 the same user that is connected to Microsoft. 

 Delegated Files.ReadWrite.All Saving files to the user's OneDrive on their
 behalf. 

 Application Application.Read.All
 DelegatedPermissionGrant.Read.All Verifies the integration configured by the Microsoft
 admin. 

 Admins always consent to application
 permissions. In contrast, end users consent to delegated permissions.
 Granting admin consent for delegated permissions is required. It
 prevents users from mistakenly denying permissions, which would block
 them from downloading and saving files to OneDrive when a Security
 policy is triggered. 

 Verifying the onboarding status of the
 integration is critical. Improper configuration will prevent Prisma Browser from saving files to OneDrive. This will block end
 users from downloading and saving files when their download action
 matches a policy rule. 

 Generate Client Secret. 

 Go to Certificates & Secrets → New client secret . 

 In the Add a client secret tab, do the following: 

 Enter a description for the secret, for example -
 Microsoft secret 01. (this field is optional. 

 In the Expires field, select 730 days (24
 months) . 

 Click Add . 

 Copy the value of the new client secret. You will need it for the
 next step when you connect the cloud storage to the Prisma Browser . We recommend that you save it in a safe place. 

 Connect to the Prisma Browser . 

 Go to the Prisma Browser admin console and select
 Integrations . 

 Select Cloud Storage . 

 Click on either +add provider or Connect your first
 provider . 

 Select the provider - Microsoft . 

 Insert a descriptive Storage name for the connection, for
 example - Microsoft Cloud Storage . 

 Paste the Client secret that you generated in the previous
 step. 

 Enter the Application (client) ID and the Directory (tenant) ID
 from the Application Overview in the Azure Portal. 

 Click Test provider connection to verify the connection with
 Azure. 

 Once the test is successful, click Add Provider . 

 Create the Save to Cloud Rule 

 Open the Access & Data Control rules and create a new
 rule. 

 At the Data Control step, select File Download .

 Select Save to organization storage and choose the provider
 that you configured in the previous step. 

 Add any additional details, and click Set . 

 Known Limitations and Requirements 

 To successfully use Save to Cloud, users must meet the following conditions: 
 Microsoft 365 Licensing: The policy must apply only to users who
 hold a valid Microsoft 365 license that includes access to OneDrive and
 the Office suite. 

 Email Consistency: The email address used to sign into the
 browser must match the Microsoft account associated with the user’s
 OneDrive. This prevents accidental data leakage or cross-account DLP
 violations. 

 Microsoft Sign-In Required: Users must be signed into their
 Microsoft account. If not already authenticated, they will be prompted
 to log in, with the browser providing a username hint to streamline the
 process. 

 HTML sites will be compressed using zip format and saved
 in a folder. The Prisma Browser does not support unzipping files. As a result,
 this is not recommended. 

 On This Page 

 Activation & Onboarding 

 Strata Cloud Manager 

 Cloud Identity Engine 

 Strata Logging Service 

 Device Associations 

 Hub 

 Identity and Access Management 

 Tenant Management 

 SASE 

 Prisma Access 

 Strata Multitenant Cloud Manager 

 AI-Powered ADEM 

 Prisma Access Monitoring and Visibility 

 Prisma SD-WAN 

 ION Devices 

 Next-Generation CASB 

 Prisma Browser 

 Prisma Access 

 Strata Cloud Manager 

 Integrations 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

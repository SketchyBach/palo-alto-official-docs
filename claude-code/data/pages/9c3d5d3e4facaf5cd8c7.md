---
url: https://docs.paloaltonetworks.com/prisma-access-browser/integrations/integrate-prisma-access-browser-with-microsoft-information-protection
fetched_at: 2026-09-16T07:45:50Z
source: strata-and-sase
---

# Integrate Prisma Access Browser with Microsoft Information Protection Clear

Updated on 

 Aug 19, 2026 

 Focus 

 Home 

 Prisma Browser 

 Integrate Prisma Access Browser with Microsoft Information Protection 

 Download PDF 

 Prisma Browser 

 Integrate Prisma Access Browser with Microsoft Information Protection 

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

 Integrate Prisma Access Browser with Microsoft Information Protection 

 Integrate Prisma Access Browser with Microsoft Information Protection to enable Prisma Access Browser to read the labels when downloading and uploading files and enforce an
 appropriate policy. 

 Where Can I Use This? What Do I Need? 

 Strata Cloud Manager 

 Standalone Prisma Access Browser 

 Prisma Access with Prisma Access Browser bundle license or
 Prisma Access Browser standalone license 

 Role: Prisma Access Browser
 Roles 

 Microsoft Information Protection 

 The Microsoft Information Protection (also known as Microsoft Purview) is an external
 system that classifies and labels files. By integrating with Microsoft Information
 Protection, you enable the Prisma Access Browser to read the labels when downloading
 and uploading files and enforce an appropriate policy. 

 Find your tenant ID. 

 Sign in to the Azure portal . 

 Make sure you're signed in to the correct tenant. If you're not in the
 correct tenant, switch directories . 

 Under Azure services, select Microsoft Entra ID .
 If you don't see Microsoft Entra ID, use the search function to find
 it. 

 Locate the Tenant ID in the
 Overview page. 

 Obtain your client ID. 

 Sign in to the Azure portal . 

 Make sure you're signed in to the correct tenant. If you're not in the
 correct tenant, switch directories . 

 Under Azure services, select Microsoft Entra ID .
 If you don't see Microsoft Entra ID, use the search function to find
 it. 

 Under Manage , select App registrations New registration . 

 Enter a display Name for your application. Your
 users will see the display name when they interact with the app. 

 You can change the display name at any time or use it for multiple
 app registrations. It doesn't affect the automatically generated
 Application (client) ID, which uniquely identifies your app. 

 Specify which users can use the application. 

 For Redirect URI , select Single Page
 Application (SPA) and provide the following URI: https://gdhaibkimkeghllnpodfpoamchapggea.chromiumapp.org . 

 Click Register . 

 When registration finishes, you can find the Application
 (client) ID in the app registration's Overview
 page. 

 Configure the required permissions for the app. 

 After the registration, under Manage , select
 Authentication . Under Implicit
 grant , select both Access tokens 
 and ID tokens . 

 Under API permissions , select Add a
 permission . Select APIs my organization
 uses , and search for Microsoft Information Protection
 Sync Service. Select Delegated permissions and
 add the UnifiedPolicy.User.Read permission . 

 Under API permissions , select Add a
 permission . Select Microsoft
 APIs , and select Microsoft Graph .
 Choose Delegated permissions and add the email
 and openid permissions. 

 Under API permissions , select Grant
 admin consent for <Organization Name> . 

 Under Token configuration , select Add
 optional claim . Select ID , and
 add email . 

 Enable the integration in Strata Cloud Manager . 

 Go to Manage Configuration Prisma Access Browser Administration Integrations Services . 

 Scroll to Microsoft Information Protection
 Integration and expand it. 

 Click Enabled , then enter the Tenant
 ID and Client ID . 

 Click Save .

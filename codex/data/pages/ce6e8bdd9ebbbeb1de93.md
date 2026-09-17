---
url: https://docs.paloaltonetworks.com/prisma-browser/deployment/deploy-prisma-browser/deploy-prisma-browser-using-intune
fetched_at: 2026-09-16T08:22:04Z
source: palo-alto-main
---

# Deploy Prisma Browser Using Intune Clear

Updated on 

 Sep 3, 2026 

 Focus 

 Home 

 Prisma Browser 

 Deploy the Prisma Browser via MDM 

 Deploy Prisma Browser Using Intune 

 Download PDF 

 Prisma Browser 

 Deploy Prisma Browser Using Intune 

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

 Deploy Prisma Browser Using Intune 

 Learn how to deploy Prisma Access Secure Enterprise Browser ( Prisma Browser ) using
 Intune. 

 Microsoft Intune is a cloud-based endpoint management solution. It manages user
 access to organizational resources and simplifies app and device management
 across your many devices, including mobile devices, desktop computers, and
 virtual endpoints. 

 Open the Microsoft Intune Admin Center . 

 Select Apps All apps . 

 Click + Add . 

 In the Select app type window, select Line-of-business
 app . 

 Click Select . 

 In the App information step, click Select app package
 file . 

 In the App package file window, browse to the MSI installation file, named
 PrismaAccessBrowserSetup.msi . 

 Click Ok . 

 Enter all the needed properties. 

 Enter a name for the app. This will be visible
 in the Intune list and in the Company Portal. 

 Provide a brief description of the app and its benefits
 for users. This description will be available in the Company
 Portal, where you can use rich text formatting to enhance
 it. 

 Enter the name of the app’s publisher , which
 appears in the Company Portal. 

 App install context – Select the Device. 

 Show this as a featured app in the Company
 Portal – we recommend that you select Yes so that it
 will be easier for your users to find. 

 Select the appropriate Logo for the application.

 Click Next . 

 Select the Assignments for this app. 

 For Available for enrolled devices, select Add group, and select the
 required Entra groups assigned to the application. 

 If you select Add all users, then the Entra assignment will include
 all Entra users in your organization. 

 Click Next . 

 Review all the settings and click Create to create the new app, or
 Previous to make changes. 

 Creating the app might take a few additional minutes. The application will be
 available for use after this step. 

 Set Prisma Browser Mobile as the Default Browser for Intune-managed Apps 

 If you are using Intune to manage your deployment, you can set Prisma Browser Mobile as the default browser. Intune empowers you to set a
 default browser for organization-managed apps. This can be applied globally
 through App Protection Policies, or selectively for specific, critical
 applications. This is particularly relevant for mobile devices (iOS and
 Android), as they are often employee-owned. However, enforcing a company browser
 as the default for all apps might raise employee concerns. 

 This requires an Intune Plan 1 license. 

 Browse to the Intune Admin Portal → App Protection Policies → Select the
 policy you want to modify or create. 

 At the Data Protection step, select "Restrict web
 content transfer with other apps", and enter Unmanaged browser 

 ( Optional ) For iOS devices: In the Unmanaged browser
 protocol field, enter prisma . 
 This requires Prisma Browser iOS version 1.4046 or later. 

 ( Optional ) For Android devices: 

 In the Unmanaged Browser ID field, enter
 com.talonsec.talon . 

 In the Unmanaged Browser Name field, enter
 PA Browser . 

 More information on Intune's App
 Protection Policies .

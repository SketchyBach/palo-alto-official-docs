---
url: https://docs.paloaltonetworks.com/saas-security/sspm/onboard-saas-apps-supported-by-sspm/onboard-an-arcgis-app-to-sspm
fetched_at: 2026-08-13T17:34:25Z
source: palo-alto-main
---

# Onboard an ArcGIS App to SSPM Clear

Onboard an ArcGIS App to SSPM 

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

 Onboard an ArcGIS App to SSPM 

 Updated on 

 Fri Jul 10 09:31:52 PDT 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 SaaS Security Docs 

 Activation & Onboarding 

 Getting Started 

 Data Security 

 SaaS Security Inline 

 SSPM 

 Behavior Threats 

 New Features 

 Updated on 

 Fri Jul 10 09:31:52 PDT 2026 

 Focus 

 Home 

 SaaS Security 

 Onboard SaaS Apps Supported by SSPM 

 Onboard an ArcGIS App to SSPM 

 Download PDF 

 SaaS Security 

 Onboard an ArcGIS App to SSPM 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 SaaS Security Docs 

 Activation & Onboarding 

 Getting Started 

 Data Security 

 SaaS Security Inline 

 SSPM 

 Behavior Threats 

 New Features 

 Previous 

 Onboard an Aptible App to SSPM 

 Next 

 Onboard an Articulate Global App to SSPM 

 Onboard an ArcGIS App to SSPM 

 Connect an ArcGIS instance to SSPM to detect posture risks. 

 Where Can I Use This? What Do I Need? 

 Strata Cloud Manager 

 SaaS Security Posture Management license 

 Or any of the following licenses that include the Data Security license: 

 CASB-X 

 CASB-PA 

 For SSPM to detect posture risks in your ArcGIS instance, you must onboard your
 ArcGIS instance to SSPM. Through the onboarding process, SSPM connects to an ArcGIS
 API and, through the API, scans your ArcGIS instance for misconfigured settings. If
 there are misconfigured settings, SSPM suggests a remediation action based on best
 practices. 

 SSPM gets access to your ArcGIS instance through OAuth 2.0 authorization. To enable
 OAuth 2.0 authorization, you first create an OAuth 2.0 integration application in
 ArcGIS before onboarding your ArcGIS instance in SSPM. During the onboarding
 process, you are prompted to log in to ArcGIS and to grant SSPM the access it
 requires. 

 To onboard your ArcGIS instance, you complete the following actions: 

 Collect Information for Accessing Your ArcGIS Instance 

 Connect SSPM to Your ArcGIS Instance 

 Collect Information for Accessing Your ArcGIS Instance 

 To access your ArcGIS instance, SSPM requires the
 following application credentials. You will create the OAuth 2.0 integration
 application and provide its credentials to SSPM during the onboarding process.

 Item Description 

 Client ID SSPM will access an ArcGIS API through an OAuth 2.0
 application that you create. ArcGIS generates the Client ID to
 uniquely identify this application. 

 Client Secret SSPM will access the ArcGIS API through an OAuth 2.0
 application that you create. ArcGIS generates the Client Secret,
 which SSPM uses to authenticate to this application. 

 As you complete the following steps, make note of the values of the items
 described in the preceding table. You will need to enter these values during
 onboarding to enable SSPM to access your ArcGIS instance. 

 From SSPM, get a redirect URI. You will specify this redirect URI in the
 OAuth 2.0 application that you will create in ArcGIS. To get this
 information, you will begin the onboarding process in SSPM, but you will not
 complete the process. 

 Log in to 
 Strata Cloud Manager . 

 Select Configuration SaaS Security Posture Security Applications Add Application and click the ArcGIS tile. 

 Under posture security instances, Add
 Instance or, if there is already an instance
 configured, Add New instance. 

 Log in with Credentials . 
 A connection page
 for onboarding an ArcGIS instance is displayed. The Redirect URL
 field displays the redirect URL value. 

 Copy the URL and paste it into a text file. 

 Do not continue to the next step
 unless you have copied the redirect URL. You will need to
 specify this URL later when you are configuring your OAuth 2.0
 integration application. 

 Because you will not be completing the onboarding process until
 after you have gathered the necessary configuration information,
 return to the Apps Onboarding page. 

 Identify the administrator account that you will use to create your OAuth
 2.0 application. 

 Required Permissions: The OAuth 2.0 application must be created
 by an ArcGIS administrator. 

 Create your OAuth 2.0 application. 

 Open a web browser and go to the ArcGIS Developer page at developers.arcgis.com . 

 Log in to the administrator account that you identified
 earlier. 

 From the ArcGIS Developer dashboard, navigate to the
 OAuth 2.0 tab to create a New
 Application . 

 In the Create new application dialog, specify a name for the
 application and Create application . 
 ArcGIS
 displays a configuration page for your new OAuth 2.0
 application. This page contains the application credentials
 (Client ID and Client Secret) for your application. 

 Copy the Client ID and Client Secret and paste them into a text
 file. 

 Do not continue to the next
 step unless you have copied the Client ID and Client Secret. You
 must provide this information to SSPM during the onboarding
 process. 

 Add the redirect URI that you obtained from SSPM to your Oauth 2.0
 application. 

 From the OAuth 2.0 tab of the ArcGIS Developer dashboard, select
 your OAuth 2.0 application and click View Full
 Credentials . 

 Locate the Redirect URLs tile and click + Add URI
 . 

 In the Add Allowed URI dialog, specify the URI that you copied from
 SSPM and Add URI . 

 Connect SSPM to Your ArcGIS Instance 

 By adding an ArcGIS app in SSPM, you enable SSPM to
 connect to your ArcGIS instance. 

 Log in to 
 Strata Cloud Manager . 

 Select Configuration SaaS Security Posture Security Applications Add Application and click the ArcGIS tile. 

 Under posture security instances, Add Instance or,
 if there is already an instance configured, Add New 
 instance. 

 Log in with Credentials . 

 Enter the application credentials (Client ID and Client Secret) and
 Connect . 

 SSPM redirects you to the ArcGIS login page. 

 Log in to the ArcGIS administrator account. 

 ArcGIS displays a consent form that details the access permissions that
 SSPM requires. 

 Review the consent form and allow the requested permissions. 

 Previous 

 Onboard an Aptible App to SSPM 

 Next 

 Onboard an Articulate Global App to SSPM 

 On This Page 

 Activation & Onboarding 

 Strata Cloud Manager 

 Cloud Identity Engine 

 Strata Logging Service 

 Device Associations 

 Identity and Access Management 

 Tenant Management 

 Next-Generation Firewalls 

 AIOps for NGFW 

 Cloud Management for NGFWs 

 Firewalls 

 PAN-OS 

 SASE 

 Prisma Access 

 Strata Multitenant Cloud Manager 

 Prisma Access Monitoring and Visibility 

 Next-Generation CASB 

 Cloud-Delivered Security Services 

 Advanced WildFire 

 Enterprise DLP 

 SaaS Security 

 Visibility & Monitoring 

 Dashboards 

 Incidents and Alerts 

 Reports 

 Autonomous DEM 

 Best Practices 

 Best Practices Library 

 Experts Corner 

 Solutions Docs from Product Experts 

 SaaS Security Posture Management 

 SaaS Security 

 SSPM 

 Cloud-Delivered Security Services 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

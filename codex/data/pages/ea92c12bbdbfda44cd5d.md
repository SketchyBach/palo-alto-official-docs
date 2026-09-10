---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsoar-8-on-prem/8.6/onboard-cortex-xsoar/onboard-and-configure-cortex-xsoar/step-1.-install-cortex-xsoar
fetched_at: 2026-09-06T11:23:21Z
source: cortex-platform
---

# Step 1. Install Cortex XSOAR | 8.6 (EoL) | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSOAR 8 

 Cortex XSOAR 8 On-prem Documentation 

 8.6 (EoL) 

 Onboard Cortex XSOAR 

 Onboard and configure Cortex XSOAR 

 Cortex XSOAR 8.6 On-prem EoL 

 Step 1. Install Cortex XSOAR 

 Install Cortex XSOAR On-prem 8.6 (EoL), including requirements and licensing. 

 To install a Cortex XSOAR 8 tenant, you need to log into Cortex Gateway, which is a portal for downloading the relevant image file and license. If you have multiple or development tenants, you must repeat this task for each tenant. 

 Before you begin 

 A Customer Support Portal (CSP) account. 

 You need to set up your CSP account. For more information, see How to Create Your CSP User Account . 

 When you create a CSP account you can set up two-factor authentication (2FA) to log into the CSP, by using an Email, Okta Verfiy, or Google Authenticator (non-FedRAMP accounts). For more information, see How to Enable a Third Party IdP . 

 You have one of the following roles assigned: 

 Role 

 Details 

 CSP role 

 The Super User role is assigned to your CSP account. The user who creates the CSP account is granted the Super User role. 

 Cortex role 

 You must have the Account Admin role. 

 If you are the first user to access Cortex Gateway with the CSP Super User role, you are automatically granted Account Admin permissions for the Cortex Gateway. You can also add Account Admin users in Cortex Gateway if required. 

 Review the System Requirements for installation. 

 Have a basic understanding of how to deploy OVA or VHD file formats. 

 Add DNS records that point the following host names to the cluster IP address. 

 FQDN 

 Details 

 Cluster FQDN 

 The Cortex XSOAR DNS name for accessing the UI. For example, xsoar.mycompany.com . 

 API-FQDN 

 The Cortex XSOAR DNS name that is mapped to the API IP address. For example, api-xsoar.mycompany.com . 

 ext-FQDN 

 : The Cortex XSOAR DNS name that is mapped to the external IP address. For example, ext-xsoar.mycompany.com . 

 Install Cortex XSOAR 

 From the Cortex Gateway, in the Available for Activation section, use the serial number to locate the tenant to download. 

 Click Download On Prem . 

 If you want to use a production and a development tenant with a private remote repository, select Dev . 

 If you don't select it now, you can install a development tenant later. 

 Download one of the following image files. 

 OVA : Supported by VMWare. 

 VHD : Supported by Microsoft Hyper-V. 

 You can deploy a single node (standalone) or a cluster (three nodes). 

 Depending on the image file, do one of the following: 

 Install Cortex XSOAR from an OVA image 

 Install Cortex XSOAR from a VHD image 

 After installation, add the Cortex XSOAR license. 

 When you download the image file, you have two license files for each environment. Each must be uploaded separately to the respective tenant. 

 Go to Settings & Info → Cortex XSOAR License . 

 In the Upload License section, drag and drop your license file. 

 The license file is in JSON format. 

 For more information, see Add the Cortex XSOAR license . 

 Optionally perform post-installation maintenance, including scaling up hardware resources and using your own X.509 certificate for a secure HTTP connection. 

 If you want to install a development machine, install the image files on the development virtual machine. 

 For more information, see Cortex XSOAR Installation . 

 Previous Onboarding checklist 

 Next Step 2. Set up an engine 

 Last updated 4 days ago 

 Was this helpful?

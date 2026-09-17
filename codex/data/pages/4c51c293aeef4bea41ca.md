---
url: https://docs.prismacloud.io/content-collections/connect/connect-cloud-accounts/onboard-your-azure-account/authorize-prisma-cloud
fetched_at: 2026-09-16T13:34:57Z
source: prisma-cloud
---

# Authorize Prisma Cloud to access Azure APIs | Prisma Cloud arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Enterprise Edition 

 Content Collections 

 Connect 

 Connect Cloud Accounts 

 Onboard Azure 

 Authorize Prisma Cloud to access Azure APIs 

 Connecting Prisma Cloud to your Azure cloud account enables you to analyze and monitor traffic logs, and detect potential malicious network activity or compliance issues. During the built-in onboarding process you have the option of using one of the following three methods to authorize Prisma Cloud to access Azure APIs: 

 Onboard using Automated Terraform Script (Recommended) This workflow automates the process of setting up the Prisma Cloud application on Microsoft Entra ID (previously known as Azure Active Directory) and enables read-only or read-write access to your Azure subscription. 

 Azure China workflows do not support the use of Terraform templates. 

 Onboard using JSON and Custom Roles Using a manually created Custom Role you also have the option to enforce least access privilege to restrict access. To achieve this you will need to manually set up the Prisma Cloud application on Microsoft Entra ID and Create a Custom Role to authorize access to Azure APIs. 

 Onboard Manually If your organization restricts the use of Terraform scripts, you can choose to manually create the required Azure resources for Prisma Cloud to call the Azure APIs. 

 Onboard using Automated Terraform Script 

 Follow the steps below to use the Automated Terraform script method to create the Azure Tenant resources for Prisma Cloud onboarding. 

 Before you begin, ensure your system has Terraform installed and that it is also authenticated to Azure via the CLI. 

 Download the Terraform script using Prisma Cloud Azure Onboarding User Interface or Azure Template Generation API. 

 We recommend that you create a directory to store the Terraform template you download. This allows you to better manage the templates when you add new Azure resources to Prisma Cloud or update existing roles. Give this directory a unique name for example, onboard-tenant-<tenant-name> . 

 Run the command terraform init > terraform apply and click Confirm . 

 This generates outputs with the following values: 

 Input these Terraform Output Key values in the associated UI fields as indicated: 

 Application (Client) ID: b_application_id 

 Application Client Secret: c_application_key 

 Enterprise Application Object ID: e_service_principal_object_id 

 Use the Azure portal to Grant admin consent for API permissions. This authorizes Prisma Cloud to access Azure resources. This is required to ingest Azure resources associated with subscriptions and management groups, only during the initial onboarding of your Azure accounts. 

 On your Azure portal, clink on the e_consent_link to be redirected to the API permissions section. 

 Click on Grant admin consent and select Yes . A success message appears indicating Grant Consent successful . 

 Verify that the status column has green check marks. 

 Automated Terraform Script for Subscription Workflow 

 Follow the steps below to use the Automated Terraform script method to create the Azure Subscription resources for Prisma Cloud onboarding. 

 Before you begin, ensure your system has Terraform installed and that it is also authenticated to Azure via the CLI. 

 Download the Terraform script using Prisma Cloud Azure Onboarding User Interface or Azure Template Generation API. 

 We recommend that you create a directory to store the Terraform template you download. This allows you to better manage the templates when you add new Azure resources to Prisma Cloud or update existing roles. Give this directory a unique name that indicates its purpose, for example, onboard-subscription-<subscription-name> . 

 Run the command terraform init > terraform apply and click Confirm . 

 This generates outputs with the following values as shown below: 

 Input the following Terraform Output Key values in the associated UI fields as indicated: 

 Application (Client) ID: c_application_id 

 Application Client Secret: d_application_key 

 Enterprise Application Object ID: e__enterprise_application_object_id 

 Terraform for Microsoft Entra ID Workflow 

 Follow the steps listed under the Tenant flow above. For step 2, remember to name the directory you use to store your Terraform template something intuitive such as, onboard-active-directory-<tenant-name> . 

 Onboard using JSON and Custom Roles 

 In addition to the automated Terraform authorization method, you also have the option to create a custom role so that you can enforce the principal of least access privileges to limit user access to the bare minimum. To create a custom role on Azure, you must have a Microsoft Entra ID Premium 1 or Premium 2 license plan. 

 Create a custom role using Azure CLI. You can create custom roles using Azure PowerShell, Azure CLI, or the REST API. The following instructions use the Azure CLI command (run on PowerShell or on the DOS command prompt) to create the custom role. 

 Install the Azure CLI and log in to Azure. 

 In your Prisma Cloud console, in the Configure Account step, click Download Terraform Script to download the JSON files which contain the permissions. These permissions vary depending on whether your account is Commercial, Government, or in China. 

 Microsoft recommends using a wildcard to configure NSG flow log permissions (Microsoft.Network/networkWatchers/queryFlowLogStatus/*), listed in the JSON files. Refer to Microsoft documentation for more details. 

 Depending on whether you are creating a custom role for the Tenant or Subscription workflow, complete the following steps: 

 Tenant Workflow: Edit the saved custom role JSON file in a text editor and update the value for AssignableScopes with the value below and save your changes: 

 Subscription Workflow: Edit the saved custom role JSON file in a text editor and update the value for AssignableScopes with the value below and save your changes: 

 Log in to the Azure portal from the same local system where the JSON file was saved and complete the following steps: 

 Open a PowerShell window or a DOS Command Prompt Window. 

 Go to the directory where you stored the JSON file. 

 Enter the following Azure CLI command (replacing the JSON filename to match the name of your custom role JSON file): 

 Commercial 

 Government 

 China 

 The command generates the sample output below indicating successful creation of a custom role: 

 Assign the Custom Role 

 Complete the following steps to assign the custom role to an app registration , add role assignments and configure it to access the flow logs: 

 Log in to the Microsoft Azure Portal. 

 Follow the navigation path for your selected workflow: 

 Tenant scope: Navigate to All Services > Management Groups . Click on Tenant Root Group . 

 Subscription scope: Navigate to All services > Subscriptions 

 Select Access control (IAM) > Add role assignment . 

 Verify that you can see the newly created custom role in the Roles drop-down. 

 Assign the custom role to the Prisma Cloud app registration. Enable the permission to query flow log status and save your changes. 

 Onboard Manually 

 If your organization restricts the use of Terraform templates, you also have the option to manually onboard your Microsoft Entra ID, Government or Azure China account resources to Prisma Cloud by creating an app registration (service principal) on Azure. Here is a preview of the required steps based on your chosen onboarding flow: 

 Azure Tenant 

 Create a custom role at the tenant level. 

 Assign IAM roles at the tenant root level. 

 Assign GraphAPI permissions at the tenant level. 

 Grant admin consent for Microsoft Entra ID Graph APIs. 

 Azure Subscription 

 Create a custom role at the Subscription level. 

 Assign IAM roles at the subscription level. 

 Microsoft Entra ID 

 Assign GraphAPI permissions at the tenant level. 

 Grant admin consent for Microsoft Entra ID Graph APIs. 

 Prerequisites 

 A Prisma Cloud tenant with permissions to onboard a cloud account. 

 Access the Azure portal with permissions to register an application and create and assign roles. 

 Steps 

 Elevate access for a Global Administrator on the Azure portal. This allows Prisma Cloud to access Azure subscriptions or management groups. This is required for ingesting resources associated with subscriptions and management groups only during the initial onboarding of your Azure accounts. You have the option to disable this after onboarding is complete. 

 Follow the steps below to Register a new application . 

 Log in to Azure portal . 

 Select Microsoft Entra ID[App registrations > + New registration] . 

 Enter the application name. 

 Select the supported account types. 

 Choose from single tenant, multitenant, multitenant and personal Microsoft accounts, or personal Microsoft accounts only. 

 tt:[Optional]—Enter the Redirect URI. 

 The authentication response of the app will be returned to this URI. 

 Click Register . 

 Copy Application (client) ID and Entra (tenant) ID to a secure location on your computer. You will later enter these details into the Prisma Cloud UI. 

 Create the client secret. 

 The client secret is a secret string that the application uses to prove its identity when requesting a token. 

 Select Certificates & secrets[+ New client secret . 

 Enter a client Description , select Expires to configure how long the client secret lasts, and Add . 

 Copy Value to a secure location. Make sure that you copy Value and not Secret ID . 

 Get the Object ID. 

 Select Microsoft Entra ID[Enterprise applications] , and search for the app you previously created in the search box. 

 Copy Object ID to a secure location on your computer. Make sure that you get the Object ID for the Prisma Cloud application from Enterprise Applications > All applications on the Azure portal—not from App Registrations . 

 Add roles to the root group. 

 The following roles should be added to the root group: 

 Reader : Required to ingest configuration and activity logs. 

 Reader and Data Access : Required to fetch flow logs and storage account attributes to detect vulnerabilities. 

 Network Contributor : Required to access and read flow logs settings for all network security groups (NSGs) and auto-remediation of network-related incidents. 

 Storage Account Contributor : Optional but required if you want to enable auto-remediation of policy violations. 

 Key Vault Crypto Service Encryption User : Required for Agent-based Workload Protection. 

 Create Custom Roles for Agentless Scanning, and Serverless Scanning (These functions are not supported for Azure China.) 

 Verify that all the roles have been added. 

 Select Role assignments . 

 Enter the name of your app in the search form and confirm that the roles that have been added. 

 Assign the created roles. Skip this step if your following the Microsoft Entra ID onboarding flow. 

 Complete the steps below to add role assignments. 

 For Tenant workflow: Select Management groups > Tenant Root Group > Access control (IAM) > Role assignments > + Add > Add role assignment . 

 For Subscription workflow: Select All Services > Subscriptions > Access Control (IAM) > Role assignments > + Add > Add role assignment . 

 Enter the name of the role, for example, Reader, in the search box. Click on the role name in the results, and select Next . 

 Assign members to the role, navigate to Select members > Assign access . Under Assign Access to , select Assign the role to a User, group, or service principal . 

 Click + Select members and then enter the name of the app you previously created, in the search box to assign the role to your app. 

 Click Select and then Next . 

 Select Review + Assign to complete adding the role assignment. 

 Confirm that all the newly created roles were added. 

 Add the Microsoft Graph APIs. 

 Navigate to the app you previously registered. Select Microsoft Entra ID > App registrations*, and select your app. 

 Navigate to Microsoft Graph. Select API permissions > Add a permission > Microsoft Graph > Application permissions . 

 Add the permissions. Enter the permission name in Select permissions , and select the name from Permission . Add the following permissions: 

 User.Read.All 

 Policy.Read.All 

 Group.Read.All 

 GroupMember.Read.All 

 Reports.Read.All 

 Directory.Read.All 

 Domain.Read.All 

 Application.Read.All 

 RoleManagement.Read.All 

 EntitlementManagement.Read.All 

 AuditLog.Read.All 

 If you have enabled additional functions like Agentless Scanning or Workload Protection additional permissions will be required. Review the Roles and Permissions list for the required permissions. 

 Grant admin consent for Default Directory. 

 Select Yes under Grant admin consent for Default Directory . 

 Verify that the permissions are granted. 

 Confirm that you can see green check marks under the Status column. 

 Previous Connect a Microsoft Entra ID Tenant 

 Next Update Azure Application Permissions 

 Last updated 1 month ago 

 Was this helpful?

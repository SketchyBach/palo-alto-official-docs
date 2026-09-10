---
url: https://cortex-docs.paloaltonetworks.com/cortex-xdr-5.x/configure-cortex-xdr/cortex-xdr-data-sources/cloud-service-provider-csp-onboarding/microsoft-azure-cloud-onboarding/prerequisites-for-onboarding-azure
fetched_at: 2026-09-06T09:40:53Z
source: cortex-platform
---

# Prerequisites for onboarding Azure | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XDR 

 Cortex XDR 5.x Documentation 

 Configure Cortex XDR 

 Cortex XDR Data Sources and Connectors 

 Cloud service provider (CSP) onboarding 

 Microsoft Azure cloud onboarding 

 Prerequisites for onboarding Azure 

 Before you begin onboarding Microsoft Azure, you must review the following prerequisites. 

 Permissions 

 Before you begin to onboard Microsoft Azure to Cortex Cloud, ensure that you have the necessary permissions: 

 In Cortex Cloud, you must have a Cortex Cloud role with Data Sources - View & Edit permissions (to add/configure cloud accounts in Cortex Cloud). This role is included in the following built-in roles: Instance Administrator, Security Admin, and IT Admin. 

 In Microsoft Azure, you must have an admin user with the required permissions . 

 Additional prerequisites 

 Before you begin onboarding Microsoft Azure, ensure that: 

 You have a Microsoft Azure subscription. 

 You obtain the tenant ID and subscription ID. You can view these in the Microsoft Azure Portal in Management groups. 

 Custom (user-defined) audit log collection 

 If you are configuring custom (user-defined) audit log collection using an existing Event Hub, ensure that: 

 You have the Event Hub name, Event Hub namespace, and Event Hub resource group name. 

 The namespace and Event Hub belong to the specific Azure subscription being onboarded. Cross-subscription or centralized logging is not currently supported. 

 Required Azure permissions for Cortex Cloud onboarding 

 This section lists all Azure permissions required for Cortex Cloud onboarding using custom roles (least-privilege). It covers both the Terraform (TF) and ARM (onboard.sh) provisioning methods. The specific permissions required depend on your target scope (subscription, management group, or tenant) and whether audit log collection is enabled. 

 Global permission prerequisites for creating service principal 

 When onboarding an Azure tenant to Cortex Cloud, the onboarding wizard automatically checks for the Cortex service principal when you enter your Azure tenant ID. If the service principal is missing, the wizard provides a command to register it manually, establishing Cortex Cloud's primary runtime identity within your Azure tenant so you can proceed with onboarding. The user who runs the command to create the service principal must have the Application Administrator built-in Entra ID role. 

 Overview of required Azure permissions by onboarding scope 

 Find your target scope below to see the required roles you need to assign or create. 

 Onboarding scope 

 Base permissions required 

 Additional permissions required if audit log collection is enabled 

 Subscription 

 Create the Basic Subscription custom role (using the permissions listed below) and assign it at the target subscription. 

 Create the Audit Log Collection custom role (using the permissions listed below) and assign it at the target subscription. 

 Management group 

 Assign the Basic Subscription role. Create a custom Basic Management Group role (using the permissions listed below) and assign it at the target management group. 

 Assign the built-in Privileged Role Administrator Entra ID role and the Application Administrator Entra ID role. 

 Create the Audit Log Collection custom role (using the permissions listed below) and assign it at the target management group. 

 Tenant 

 Assign the Basic Subscription role. Create a custom Basic Management Group role (using the permissions listed below) and assign it at the root management group. 

 Assign the built-in Privileged Role Administrator Entra ID role and the Application Administrator Entra ID role. 

 Create the Audit Log Collection custom role (using the permissions listed below) and assign it at the target management group. 

 Assign the built-in Security Admin Entra ID role (required for updating/destroying diagnostic settings). 

 Basic Subscription custom role permissions 

 These permissions must be included in a custom Azure role assigned at the subscription level. 

 Basic Management Group custom role permissions 

 These permissions must be included in a custom Azure role assigned at the management group level. Assign this role in addition to the basic subscription layer. 

 Audit Log Collection custom role permissions 

 These permissions must be included in a custom Azure role assigned at the target scope. Assign this role in addition to the previous roles according to the scope being onboarded. 

 Audit log collection in a tenant scope: Entra ID role requirement 

 This section applies when audit log collection is enabled and the onboarding is done at the tenant scope. 

 The microsoft.aadiam/diagnosticSettings permissions family at the tenant level is required for provisioning relevant resources required for audit log collection. The onboarding user must have the Security Administrator Entra ID role (or Global Administrator) in order to create, update, and delete the Azure diagnostic settings. 

 For more information, see Microsoft documentation . 

 Previous Onboard Microsoft Azure 

 Next How to onboard Microsoft Azure 

 Last updated 1 month ago 

 Was this helpful?

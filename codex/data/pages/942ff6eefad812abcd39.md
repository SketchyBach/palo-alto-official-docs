---
url: https://cortex-docs.paloaltonetworks.com/microsoft-azure-manual-onboarding/azure-manual-onboarding-guide/azure-manual-onboarding-management-group-or-tenant-scope/prerequisites
fetched_at: 2026-09-06T11:16:42Z
source: cortex-platform
---

# Prerequisites | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Manual Cloud Onboarding 

 Microsoft Azure Manual Onboarding 

 Azure Manual Onboarding Guide 

 Azure Manual Onboarding: Management group or tenant scope 

 Prerequisites 

 Note: Custom roles containing DataActions cannot be assigned directly at the management group scope. However, Microsoft allows these roles to include a management group in their AssignableScopes , provided they are assigned at the subscription scope. This guide strictly follows this supported pattern. 

 Ensure az cli is installed and authenticated. 

 Ensure you have the necessary permissions: 

 In Cortex, you must have a Cortex role with Data Sources - View & Edit permissions (to add/configure cloud accounts in Cortex). This role is included in the following built-in roles: Instance Administrator, Security Admin, and IT Admin. 

 In Microsoft Azure, to create the service principal and assign the required Application.Read.All Microsoft Graph permission to Cortex, the onboarding user must have the Application Administrator built-in Entra ID role. 

 Create the Cortex service principal. 

 Decide on your resource naming convention. Throughout this manual onboarding process, you will need to choose your own names for the resource group, custom roles, Event Hub namespace, storage account, UAMI. Use the Configuration values reference to keep track of the names as you will need to refer to them throughout the process. 

 Gather and record the following required Azure deployment variables. You will need to substitute these values throughout the configuration steps. 

 Variable 

 Description 

 <TENANT_ID> 

 Your Microsoft Entra ID tenant ID. 

 <MG_ID> 

 For MG onboarding: the child management group's name (not its displayName ). Run az account management-group list -o table to find it.
For tenant root management group onboarding: the tenant ID (same value as <TENANT_ID> ). The tenant ID is also the root MG name. 

 <HOST_SUBSCRIPTION_ID> 

 A stable, long-lived subscription under the target management group to host the audit logs infrastructure (Event Hub, UAMI, and Storage Account). Required only if audit log collection is enabled. 

 P.1 Create the Cortex service principal 

 The Cortex service principal is Cortex's primary runtime identity in your tenant. It is the identity that all subsequent custom role assignments bind to and Cortex uses it to read your Azure resources and perform actions for the capabilities you enable. When you enter your Azure tenant ID in the onboarding wizard, Cortex checks whether this service principal already exists in your tenant. If it does, no action is needed. If it is not found, you must create it: 

 Open Azure Cloud Shell in the tenant you are onboarding, or open a local terminal with the Azure CLI installed, and log in to the target tenant before executing the command below. 

 Run the following command: 

 Ask Copy 

 az ad sp create --id < AZURE_TENANT_I D > 

 Where <AZURE_TENANT_ID> is the tenant ID of your Azure tenant. 

 Previous Azure Manual Onboarding: Management group or tenant scope 

 Next Phase 1: Create Azure cloud instance in Cortex 

 Last updated 8 days ago 

 Was this helpful?

---
url: https://cortex-docs.paloaltonetworks.com/microsoft-azure-manual-onboarding/azure-manual-onboarding-guide/azure-manual-onboarding-subscription-scope/phase-1-create-azure-cloud-instance-in-cortex
fetched_at: 2026-09-16T09:12:20Z
source: cortex-platform
---

# Phase 1: Create Azure cloud instance in Cortex | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Manual Cloud Onboarding 

 Microsoft Azure Manual Onboarding 

 Azure Manual Onboarding Guide 

 Azure Manual Onboarding: Subscription Scope 

 Phase 1: Create Azure cloud instance in Cortex 

 Phase 1: Create Azure cloud instance in Cortex 

 1.1 Start the Azure onboarding wizard 

 1.1.2 Access the Azure onboarding wizard in Cortex Cloud: 

 In Cortex Cloud, select Settings → Data Sources & Integrations. 

 On the Data Sources & Integrations page, click + Add New. 

 On the Add Data Sources or Integrations page, search for Microsoft Azure, then hover over it and click Add. 

 1.1.3 Select the scope 

 Select the scope for this cloud instance: 

 Tenant: (Default) A specific instance of Azure Active Directory, which can contain several subscriptions. 

 Management Group: A collection of Microsoft Azure subscriptions. 

 Subscription: A collection of Microsoft Azure resources associated with a specific Microsoft Azure tenant. 

 1.1.4 Choose the scan mode 

 Specify the scanning infrastructure for your cloud instance by selecting one of the following scan modes: 

 Cloud Scan: (Recommended) Security scanning is performed in the Cortex Cloud cloud environment. 

 Scan with Outpost: Security scanning is performed on infrastructure deployed to a cloud account owned by you. If you select this option, choose the outpost account to use for this instance. 

 Note: Scanning with an outpost may require additional Azure permissions and may incur additional CSP costs. 

 1.1.5 Verify the Cortex service principal 

 The Cortex service principal is Cortex's primary runtime identity in your tenant. It is the identity that all subsequent custom role assignments bind to and Cortex uses it to read your Azure resources and perform actions for the capabilities you enable. When you enter your Azure tenant ID in the onboarding wizard, Cortex checks whether this service principal already exists in your tenant. You should have already created the Cortex service principal in Step P.2. 

 Select your Azure tenant ID from the list of approved tenants. A green checkmark next to a tenant ID indicates that Cortex is already registered as an approved application on that tenant and the approval has been verified. 

 Note: Cortex performs a live verification of each tenant's approval status against Azure each time the list is displayed. If a previously approved tenant no longer shows a green checkmark, the Cortex service principal may have been removed from the Azure tenant. Run the Azure CLI command again to re-create the service principal, then click Validate. 

 1.1.6 Configure advanced settings 

 Click Show advanced settings to define the following advanced settings: 

 Instance Name: Enter a unique instance name or leave it empty to be automatically populated. The automatic naming convention is Azure-<tenantID> . Cortex does not prevent you from reusing instance names, but it is best practice to use a unique name for every cloud instance. 

 Deployment Method: Select whether you want to onboard with a Cortex-generated Terraform authentication template or to perform a manual deployment. 

 Terraform: (Recommended). Proceed to How to onboard Microsoft Azure. 

 Manual: Select this option to manually configure service accounts and permissions, so your cloud setup stays aligned with internal governance requirements. 

 Scope Modifications: Use these settings to fine-tune your Microsoft Azure scope. You can modify the scope by including or excluding specific regions. Additionally, if you selected a tenant or management group as the scope, you can modify the scope by including or excluding specific subscriptions. For more details, see Apply region or account filters. 

 Additional Security Capabilities: Choose which security capabilities you want to benefit from. Some security capabilities are enabled by default and can be modified. Adding security capability typically requires additional cloud provider permissions. For detailed information on the permissions required, see Cloud service provider permissions. 

 Data security posture management: An agentless data security scanner that discovers, classifies, protects, and governs sensitive data. 

 Registry scanning: A container registry scanner that scans registry images for vulnerabilities, malware, and secrets. For more details, see Configure registry scanning for cloud accounts. 

 Serverless functions scanning: Implement serverless scanning to detect and remediate vulnerabilities within serverless functions during the development lifecycle. Seamless integration into CI/CD pipelines enables automated security scans for a continuously secure pre-production environment. 

 Automation: Use automation to pre-configure a list of integrations and associated commands to automate security issue responses. Commands can be utilized individually or as part of custom playbooks for issue remediation. 

 Log Level: (Optional - for Automation only) Configure the automation integration logging level. Possible values are: 

 Off (Default) 

 Debug 

 Verbose 

 Agentless disk scanning: (Recommended) Implement agentless disk scanning to remotely detect and remediate vulnerabilities during the development lifecycle. 

 Cloud Tags: Define tags and tag values to be added to any new resource created by Cortex Cloud in Microsoft Azure. Note: The managed_by = paloaltonetworks tag is automatically added to all resources. This tag is mandatory. You cannot edit or remove this tag. 

 Log Collection Configuration: To maximize security coverage, include the collection of audit logs using Event Hub. 

 1.2 Download the customized identifiers file 

 The Identifiers JSON file is a customized configuration document generated based on the specific security capabilities selected during the initial onboarding wizard. It acts as a workbook to track service accounts and organization-specific metadata across the different phases of deployment. 

 The file is divided into two primary sections, each serving a distinct purpose in your manual onboarding process: 

 The "identifiers" section: This section is pre-populated by the Azure onboarding wizard. It contains the following specific details generated for your environment. You will reference these in Phases 2-4. 

 Variable 

 Description 

 <CORTEX_OBJECT_ID> 

 Cortex service principal object ID in your tenant 

 <AUDIENCE> 

 OIDC audience for the federated credential. Always api://AzureADTokenExchange for commercial Azure. (Audit logs only) 

 <COLLECTOR_SA_UNIQUE_ID> 

 Unique ID of the Cortex Collector's Google service account. Used as the federated-credential subject (Audit Logs only). 

 <COLLECTOR_ALLOWED_IPS> 

 Comma-separated list of Cortex Collector egress IPs. Allow-listed on the storage account and Event Hub network rules (Audit Logs only). 

 The "manual_details" section: These fields are initially empty. During the manual setup in Phase 2, you will retrieve specific values from your Azure environment, such as your role names and Event Hub details, and input them directly into this section of the file. 

 In the Azure onboarding wizard, in the Manual Connection Setup step, click Identifiers to download your customized identifiers file. At this point in the deployment process, you move over to the Microsoft Azure environment to create the required resources, as described in phases 2-4. As you create the custom resources, you can keep track of their values in the Configuration values reference. You will need to enter these details in Azure Global Identifiers and Managed Identity sections in the Azure onboarding wizard when you have completed phase 4. 

 Previous Prerequisites 

 Next Phase 2: Platform Identity and Base Role 

 Last updated 19 days ago 

 Was this helpful?

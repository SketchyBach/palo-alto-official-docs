---
url: https://cortex-docs.paloaltonetworks.com/cortex-xdr-5.x/configure-cortex-xdr/cortex-xdr-data-sources/cloud-service-provider-csp-onboarding/google-cloud-platform-cloud-onboarding/how-to-onboard-google-cloud-platform
fetched_at: 2026-09-06T09:40:58Z
source: cortex-platform
---

# How to onboard Google Cloud Platform | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XDR 

 Cortex XDR 5.x Documentation 

 Configure Cortex XDR 

 Cortex XDR Data Sources and Connectors 

 Cloud service provider (CSP) onboarding 

 Google Cloud Platform cloud onboarding 

 How to onboard Google Cloud Platform 

 Follow the GCP onboarding wizard, and Cortex Cloud creates a custom authentication template to be applied in GCP. 

 After completing the prerequisites, follow these instructions to onboard your Google Cloud Platform (GCP) environment to Cortex Cloud. 

 Access the GCP onboarding wizard in Cortex Cloud: 

 In Cortex Cloud, select Settings → Data Sources & Integrations. 

 On the Data Sources & Integrations page, click + Add New. 

 On the Add Data Sources or Integrations page, search for Google Cloud Platform (GCP), then hover over it and click Add. 

 Select the GCP environment 

 In the GCP onboarding wizard, select the type of GCP environment: 

 Government: GCP GovCloud environments for compatibility with FedRAMP-certified tenants. 

 Commercial: (Default) Standard cloud deployment typically used for private and public sector organizations that do not require isolated government-specific infrastructure. 

 Select the scope 

 Select the scope for this cloud instance: 

 Organization: (Default) A collection of GCP projects that are managed centrally. 

 Folder: A GCP folder can contain projects, folders, or a combination of both projects and folders. 

 Project: A specific GCP project. 

 Choose the scan mode 

 Specify the scanning infrastructure for your cloud instance by selecting one of the following scan modes: 

 Cloud Scan: (Recommended) Security scanning is performed in the Cortex Cloud cloud environment. 

 Scan with Outpost: Security scanning is performed on infrastructure deployed to a cloud account owned by you. If you select this option, choose the outpost account to use for this instance. 

 Note 

 Scanning with an outpost may require additional GCP permissions and may incur additional CSP costs. 

 Configure advanced settings (optional) 

 Click Show advanced settings to define the following advanced settings: 

 Instance Name: Enter a unique instance name or leave it empty to be automatically populated. The automatic naming convention is GCP- or `GCP-`<organizationID> . Cortex Cloud does not prevent you from reusing instance names, but it is best practice to use a unique name for every cloud instance. 

 Deployment Method: Select whether you want to onboard with a Cortex-generated IaC template or to perform a manual deployment: 

 Infrastructure as Code: (Recommended) Automatically provisions all required cloud resources and permissions using an IaC template. 

 Manual: Select this option if your organization requires manual provisioning to meet internal security and compliance policies. If you choose to onboard manually, follow the manual onboarding instructions . 

 Scope Modifications: Use these settings to fine-tune your GCP scope. You can modify the scope by including or excluding specific regions. Additionally, if you selected an organization or folder as the scope, you can modify the scope by including or excluding specific folders or projects. For more details, see Apply region or account filters . 

 Additional Security Capabilities: Choose which security capabilities you want to benefit from. Some security capabilities are enabled by default and can be modified. Adding security capability typically requires additional cloud provider permissions. For detailed information on the permissions required, see Cloud service provider permissions . 

 Data security posture management: An agentless data security scanner that discovers, classifies, protects, and governs sensitive data. 

 Registry scanning: A container registry scanner that scans registry images for vulnerabilities, malware, and secrets. For more details, see Configure registry scanning for cloud accounts . 

 Serverless functions scanning: Implement serverless scanning to detect and remediate vulnerabilities within serverless functions during the development lifecycle. Seamless integration into CI/CD pipelines enables automated security scans for a continuously secure pre-production environment. 

 Automation: Use automation to pre-configure a list of integrations and associated commands to automate security issue responses. Commands can be utilized individually or as part of custom playbooks for issue remediation. 

 Log Level: (Optional - for Automation only) Configure the automation integration logging level. Possible values are: 

 Off (Default) 

 Debug 

 Verbose 

 Agentless disk scanning: (Recommended) Implement agentless disk scanning to remotely detect and remediate vulnerabilities during the development lifecycle. 

 Cloud Tags: Define tags and tag values to be added to any new resource created by Cortex Cloud in GCP. Note: The managed_by = paloaltonetworks tag is automatically added to all resources. This tag is mandatory. You cannot edit or remove this tag. 

 Log Collection Configuration: To maximize security coverage, include the collection of audit logs (GCP Pub/Sub). This may require additional cloud service provider permissions. For detailed information on the permissions required, see Cloud service provider permissions . 

 Connect to GCP Workspace: Gain a comprehensive view of your Google Workspace identities and security. This provides you with detailed information on your users, groups, and organizational units, and collects security event logs to help you detect threats, improve your security posture, and meet compliance requirements. 

 Note 

 If you want to connect to your GCP Workspace, you must first complete onboarding with the option disabled. Once the GCP cloud instance is created, perform the steps detailed in Connect Google Workspace with your GCP cloud instance . 

 Upload unknown files to WildFire: Use this option to upload unknown files scanned during registry image scans to WildFire for detonation analysis. This option expands malware detection by allowing WildFire to analyze new samples found in your registry images. When a detonation result returns a malicious verdict, the system re-evaluates the relevant registry image and creates a malware finding. 

 Notes 

 The file types sent for WildFire analysis depend on the platform type. WildFire accepts files up to 300 MB in size. 

 This setting applies only to registry image scans and is enabled by default for new GCP instances. For existing instances, this setting is disabled by default to preserve the current behavior. You can enable it at any time by editing the instance configuration. 

 Your cloud provider may charge standard outbound data transfer (egress) fees when scanning with an Outpost . 

 Save the configuration and download the template 

 Click Save. Cortex Cloud generates a Terraform authentication template based on the settings you configured in the GCP onboarding wizard. Cortex Cloud creates an instance in the pending state. For details on pending instances, see Pending cloud instances . 

 Click Download Terraform to download the template file and then click Close. 

 The Terraform authentication template is reusable and can be applied as many times as you want to create new instances with the settings you defined in the GCP onboarding wizard. The Terraform authentication template is valid for seven days from when it was created. 

 Next step: Deploy the Terraform authentication template in GCP. 

 Previous Prerequisites for onboarding GCP 

 Next Deploy the Terraform authentication template in GCP 

 Last updated 7 days ago 

 Was this helpful?

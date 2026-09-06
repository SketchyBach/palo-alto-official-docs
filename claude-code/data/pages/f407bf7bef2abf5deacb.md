---
url: https://cortex-docs.paloaltonetworks.com/cortex-xdr-5.x/configure-cortex-xdr/cortex-xdr-data-sources/cloud-service-provider-csp-onboarding/google-cloud-platform-cloud-onboarding/prerequisites-for-onboarding-gcp
fetched_at: 2026-09-06T09:40:58Z
source: cortex-platform
---

# Prerequisites for onboarding GCP | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

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

 Prerequisites for onboarding GCP 

 Before you begin onboarding GCP, you must review the following prerequisites. 

 Permissions 

 Before you begin to onboard GCP to Cortex Cloud, ensure that you have the necessary permissions: 

 In Cortex Cloud, you must have a Cortex Cloud role with Data Sources - View & Edit permissions (to add/configure cloud accounts in Cortex Cloud). This role is included in the following built-in roles: Instance Administrator, Security Admin, and IT Admin. 

 In GCP, you must have access to Google Cloud console and an admin user with the required GCP permissions . 

 Required APIs 

 Ensure you have enabled the following APIs in the GCP project you are onboarding: 

 Cloud Resource Manager API 

 Identity and Access Management (IAM) API 

 Cloud Pub/Sub API (if audit logs are enabled) 

 If you plan on enabling Automation as an additional security capability, enable the following APIs: 

 Kubernetes Engine API 

 Compute Engine API 

 Service Usage API 

 Cloud Storage API 

 Required admin GCP permissions for Cortex Cloud onboarding 

 Use the following template to create a dedicated role with the permissions required for onboarding GCP to Cortex Cloud: 

 Previous Onboard Google Cloud Platform 

 Next How to onboard Google Cloud Platform 

 Last updated 1 month ago 

 Was this helpful?

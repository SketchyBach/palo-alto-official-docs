---
url: https://cortex-docs.paloaltonetworks.com/google-cloud-platform-manual-onboarding/gcp-manual-onboarding/gcp-manual-onboarding-guide-project-scope/phase-3-scanner-service-account
fetched_at: 2026-09-06T11:16:34Z
source: cortex-platform
---

# Phase 3: Scanner Service Account | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Manual Cloud Onboarding 

 Google Cloud Platform Manual Onboarding 

 GCP Manual Onboarding 

 GCP Manual Onboarding Guide - Project Scope 

 Phase 3: Scanner Service Account 

 This phase is only required if you enabled one or more of the following capabilities in the GCP onboarding wizard in Cortex: 

 Registry Scanning 

 Data Security Posture Management (DSPM) 

 Serverless Scanning 

 Note: If these features were selected, any step marked as "Required" in the phase 3 substeps must be completed to ensure the corresponding scanner functions correctly. If none of these capabilities were enabled, you may skip to phase 4. 

 3.1 Create the Scanner Service Account (Required) 

 Module: OUTPOST_SCANNER 

 Ask Copy 

 gcloud iam service-accounts create < SCANNER_SA_NAM E > \ 
 --display-name= " Cortex Platform Outpost Scanner Service Account " 

 Where <SCANNER_SA_NAME> is your chosen service account ID (e.g., cortex-scanner). 

 3.2 Grant the Viewer role to the Scanner Service Account (Required) 

 Module: OUTPOST_SCANNER 

 Ask Copy 

 gcloud projects add-iam-policy-binding < PROJECT_I D > \ 
 --member= " serviceAccount:<SCANNER_SA_NAME>@<PROJECT_ID>.iam.gserviceaccount.com " \ 
 --role= " roles/viewer " 

 Where: 

 <SCANNER_SA_NAME> is your chosen service account ID (e.g., cortex-scanner) 

 <PROJECT_ID> is the ID of the GCP project you are onboarding to Cortex 

 3.3 DSPM: Scanner Service Account (Optional) 

 Module: DSPM 

 Execute the steps in this section if you enabled Data Security Posture Management (DSPM) in the GCP onboarding wizard in Cortex. 

 3.3.1 Create the DSPM Outpost role 

 Where: 

 <DSPM_OUTPOST_ROLE_ID> is your chosen name for the role (e.g. CortexDspmOutpost) 

 <PROJECT_ID> is the ID of the GCP project you are onboarding to Cortex 

 3.3.2 Grant the DSPM Outpost role to the Outpost Service Account 

 Where: 

 <PROJECT_ID> is the ID of the GCP project you are onboarding to Cortex 

 <OUTPOST_SERVICE_ACCOUNT_EMAIL> is the value listed in the identifiers JSON file 

 <DSPM_OUTPOST_ROLE_ID> is your chosen name for the role (e.g. CortexDspmOutpost) 

 3.3.3 Create the DSPM Scanner Connector role 

 Where: 

 <DSPM_SCANNER_CONNECTOR_ROLE_ID> is your chosen name for the role (e.g. CortexDspmScanner) 

 <PROJECT_ID> is the ID of the GCP project you are onboarding to Cortex 

 3.3.4 Grant the DSPM Scanner Connector role to the Scanner Service Account 

 Where: 

 <PROJECT_ID> is the ID of the GCP project you are onboarding to Cortex 

 <SCANNER_SA_NAME> is your chosen service account ID (e.g., cortex-scanner) 

 <DSPM_SCANNER_CONNECTOR_ROLE_ID> is your chosen name for the role (e.g. CortexDspmScanner) 

 3.3.5 Grant the Storage Object Viewer role to the Scanner Service Account 

 Where: 

 <PROJECT_ID> is the ID of the GCP project you are onboarding to Cortex 

 <SCANNER_SA_NAME> is your chosen service account ID (e.g., cortex-scanner) 

 3.3.6 Grant the Service Account Token Creator role to the DSPM Scanner Service Account 

 Allow the DSPM Scanner Service Account (provided by Cortex) to impersonate the Scanner Service Account: 

 Where: 

 <SCANNER_SA_NAME> is your chosen service account ID (e.g., cortex-scanner) 

 <PROJECT_ID> is the ID of the GCP project you are onboarding to Cortex 

 <DSPM_SCANNER_SERVICE_ACCOUNT_EMAIL> is the value listed in the identifiers JSON file 

 3.4 Registry Scanning (Optional) 

 Module: REGISTRY 

 Execute the steps in this section if you enabled Registry Scanning in the GCP onboarding wizard in Cortex. 

 3.4.1 Create the Registry Scanner role 

 Where: 

 <REGISTRY_SCANNER_ROLE_ID> is your chosen name for the role (e.g. CortexRegistryScanner) 

 <PROJECT_ID> is the ID of the GCP project you are onboarding to Cortex 

 3.4.2 Grant the Registry Scanner role to the Scanner Service Account 

 Where: 

 <PROJECT_ID> is the ID of the GCP project you are onboarding to Cortex 

 <SCANNER_SA_NAME> is your chosen service account ID (e.g., cortex-scanner) 

 <REGISTRY_SCANNER_ROLE_ID> is your chosen name for the role (e.g. CortexRegistryScanner) 

 3.4.3 Grant the Service Account Token Creator role to the Registry Scanner Service Account 

 Where: 

 <SCANNER_SA_NAME> is your chosen service account ID (e.g., cortex-scanner) 

 <PROJECT_ID> is the ID of the GCP project you are onboarding to Cortex 

 <REGISTRY_SCANNER_SERVICE_ACCOUNT_EMAIL> is the value listed in the identifiers JSON file 

 3.5 Serverless Scanning (Optional) 

 Module: SERVERLESS 

 Execute the steps in this section if you enabled Serverless Scanning in the GCP onboarding wizard in Cortex. 

 3.5.1 Create the Serverless Scanner role 

 Where: 

 <SERVERLESS_SCANNER_ROLE_ID> is your chosen name for the role (e.g. CortexServerlessScanner) 

 <PROJECT_ID> is the ID of the GCP project you are onboarding to Cortex 

 3.5.2 Grant the Serverless Scanner role to the Scanner Service Account 

 Where: 

 <PROJECT_ID> is the ID of the GCP project you are onboarding to Cortex 

 <SCANNER_SA_NAME> is your chosen service account ID (e.g., cortex-scanner) 

 <SERVERLESS_SCANNER_ROLE_ID> is your chosen name for the role (e.g. CortexServerlessScanner) 

 3.5.3 Grant the Service Account Token Creator role to the Serverless Scanner Service Account 

 Where: 

 <SCANNER_SA_NAME> is your chosen service account ID (e.g., cortex-scanner) 

 <PROJECT_ID> is the ID of the GCP project you are onboarding to Cortex 

 <SERVERLESS_SCANNER_SERVICE_ACCOUNT_EMAIL> is the value listed in the identifiers JSON file 

 Previous Phase 2: Platform service accounts 

 Next Phase 4: Audit Logs 

 Last updated 8 days ago 

 Was this helpful?

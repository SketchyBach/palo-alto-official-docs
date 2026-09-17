---
url: https://docs.prismacloud.io/content-collections/connect/connect-cloud-accounts/onboard-gcp/create-custom-role-on-gcp
fetched_at: 2026-09-16T13:35:00Z
source: prisma-cloud
---

# Create a Service Account With a Custom Role | Prisma Cloud arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Enterprise Edition 

 Content Collections 

 Connect 

 Connect Cloud Accounts 

 Onboard GCP 

 Create a Service Account With a Custom Role 

 If you prefer to create a service account with more granular permissions to onboard your GCP Organization or onboard your GCP Project , instead of using the Terraform template which grants the Viewer (primitive) role for read-only access to resources in your GCP account, follow the steps listed below. 

 If you enable granular permissions, you must update the custom role and add additional permissions that maybe required to ingest data from any new service that is added on Prisma Cloud. 

 To enable dataflow log compression using the Dataflow service, you must enable additional permissions. See Flow Logs Compression on GCP for details on ingesting network log data. 

 Create a YAML file with the custom permissions. 

 Create a YAML file and add the granular permissions for the custom role. 

 Use this YAML format as an example. You must add the permissions for onboarding your GCP organization or project, from the link above, to this file: 

 Ask Copy 

 title: prisma-custom-role 
 description: prisma-custom-role 
 stage: beta 
 includedPermissions: 
 - compute.networks.list 
 - compute.backendServices.list 

 Create the custom role. 

 When creating a service account, you must select a GCP project because GCP does not allow the service account to belong directly under the GCP Organization. 

 Select the GCP project in which you want to create the custom role. 

 Upload the YAML file to the Cloud Shell. 

 Run the gcloud command userinput:[gcloud iam roles create <prisma customrole name> --project <project-ID> --file <YAML file name>] 

 Create a Service Account and attach the custom role to it. 

 Select IAM > Admin > Service Accounts in the Google Cloud Console. 

 Create Service Account and add the role you created earlier to it. 

 Create a key and download the private key. 

 Continue to onboard your GCP project and use the private key for the service account to complete onboarding. 

 For onboarding tt:[GCP Organization only], create the custom role in the GCP Organization level. 

 Select your GCP organization. 

 Verify that the YAML file you created earlier includes the additional permissions for GCP organization. 

 Run the gcloud command gcloud iam roles create <prisma customrole name> --organization <org ID> --file <YAML File name> . 

 For onboarding tt:[GCP Organization only], set up your Service Account to monitor all the GCP folders and projects within the GCP Organization. 

 You must associate the Service account you created in the project to the GCP Organization-level and add the custom role you created in the previous step. Additionally, you must add the predefined role for Organization Viewer to the service account. All these tasks together enable the service account to monitor all the GCP projects that are within the GCP organizational hierarchy. 

 Copy the service account member address. 

 Select the project that you used to create the service account, and select IAM > Admin > IAM to copy the service account member address. 

 Select your Organization, select IAM > Admin > IAM to Add members to the service account. 

 Paste the service account member address you copied as New members and Select a role . 

 Select the custom role you created above and + ADD ANOTHER ROLE . 

 Select Resource > Manager > Organization Role Viewer , Folder Viewer role, and Save . 

 The Organization Viewer role enables permissions to view the Organization name without granting access to all resources in the Organization. The Folder Viewer roles is also required to onboard your GCP folders. 

 For tt:[GCP Organization only], continue to Onboard Your GCP Organization and use the private key associated with your service account to complete onboarding. 

 Previous Update an Onboarded GCP Account 

 Next GCP APIs Ingested by Prisma Cloud 

 Last updated 1 month ago 

 Was this helpful?

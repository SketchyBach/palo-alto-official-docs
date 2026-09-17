---
url: https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/administration/ztna-connector-in-prisma-access/onboard-a-cloud-instance-or-vm-for-the-ztna-connector/google-cloud-platform-deployments-supported-by-ztna-connector/onboard-a-ztna-connector-using-google-cloud-platform.html
fetched_at: 2026-09-16T11:25:59Z
source: palo-alto-main
---

# Onboard a ZTNA Connector in Google Cloud Platform Clear

Updated on 

 Thu Sep 03 12:12:03 PDT 2026 

 Focus 

 Home 

 Prisma Access 

 Prisma Access Administration 

 Prisma Access ZTNA Connector 

 Onboard the ZTNA Connector VM in Your Data Center 

 Google Cloud Platform Deployments Supported by ZTNA Connector 

 Onboard a ZTNA Connector in Google Cloud Platform 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 Deutsch (German) 

 Prisma Access 

 Onboard a ZTNA Connector in Google Cloud Platform 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma Access Docs 

 Release Notes 

 Select a Document 

 6.2 Preferred and Innovation 

 6.1 Preferred and Innovation 

 6.0 Preferred and Innovation 

 5.2 Preferred and Innovation 

 5.1 Preferred and Innovation 

 5.0 Preferred and Innovation 

 4.2 Preferred 

 4.1 Preferred 

 4.0 Preferred 

 3.2 Preferred and Innovation 

 Activation & Onboarding 

 Administration 

 Select a Document 

 4.0 & Later 

 Prisma Access China 

 Integrations 

 Incidents & Alerts 

 New Features 

 Previous 

 Google Cloud Platform Deployments Supported by ZTNA Connector 

 Next 

 Amazon Web Services Deployments Supported by ZTNA Connector 

 Onboard a ZTNA Connector in Google Cloud Platform 

 ZTNA Connector deployment in Google Cloud Platform. 

 Review the requirements and guidelines 
 and the FQDNs and ports you need to
 configure to use Prisma Access ZTNA Connector in the Google Cloud
 Platform (GCP). 

 Retrieve and copy the Connector key and secret values on the Prisma SASE Portal:
 Configuration ZTNA Connector Connectors , find the Connector object you created in Prisma Access to
 associate with this VM, and select Copy Token ; then, copy
 the Key and Secret values. 

 After you’ve met all the prerequisites, follow these steps to onboard a Prisma Access 
 ZTNA Connector in GCP. 

 Go to GCP Marketplace and search for
 Prisma Access ZTNA Connector . 

 Choose the software plan that best suits your requirement. 

 Prisma Access 

 Prisma Access 

 Deploy ZTNA Connector 1-Arm in GCP 

 Follow these steps to deploy ZTNA Connector 1-Arm in GCP: 

 LAUNCH to configure ZTNA Connector 1-Arm. 

 On New Prisma Access ZTNA Connector 1-Arm
 deployment , Download the terraform. 

 Choose your option based on your requirement. In the downloaded folder, go
 to envs > commercial and change your directory to this
 environment. 

 The details related to the package and the
 commands are available in README.md file. 

 Modify your deployment variables in the file terraform.tfvars and
 run the following commands. 

 username@M-####### gcp % find 1-arm
1-arm
1-arm/outputs.tf
1-arm/main.tf
1-arm/marketplace_test.tfvars
1-arm/README.md
1-arm/variables.tf
1-arm/envs
1-arm/envs/commercial
1-arm/envs/commercial/outputs.tf
1-arm/envs/commercial/main.tf
1-arm/envs/commercial/terraform.tfvars
1-arm/envs/commercial/README.md
1-arm/envs/commercial/variables.tf
username@M-####### gcp % 

 terraform init - initializes the terraform 

 terraform plan - output of this command will show the GCP
 resources that will be created 

 terraform apply - deploys them into your GCP account 

 Deploy ZTNA Connector 2-Arm in GCP 

 Follow these steps to deploy ZTNA Connector in GCP: 

 LAUNCH to configure. 

 On New Prisma Access ZTNA Connector 2-Arm
 deployment , Download the terraform. 

 Choose your option based on your requirement. In the downloaded folder, go
 to envs > commercial and change your directory to this
 environment. 

 The details related to the package and the
 commands are available in README.md file. 

 Modify your deployment variables in the file terraform.tfvars and
 run the following commands. 

 username@M-####### gcp % find 1-arm
1-arm
1-arm/outputs.tf
1-arm/main.tf
1-arm/marketplace_test.tfvars
1-arm/README.md
1-arm/variables.tf
1-arm/envs
1-arm/envs/commercial
1-arm/envs/commercial/outputs.tf
1-arm/envs/commercial/main.tf
1-arm/envs/commercial/terraform.tfvars
1-arm/envs/commercial/README.md
1-arm/envs/commercial/variables.tf
username@M-####### gcp % 

 terraform init - initializes the terraform 

 terraform plan - output of this command will show the GCP
 resources that will be created 

 terraform apply - deploys them into your GCP account 

 Previous 

 Google Cloud Platform Deployments Supported by ZTNA Connector 

 Next 

 Amazon Web Services Deployments Supported by ZTNA Connector

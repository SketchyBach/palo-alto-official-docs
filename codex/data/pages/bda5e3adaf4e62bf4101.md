---
url: https://docs.paloaltonetworks.com/ai-runtime-security/activation-and-onboarding/onboard-and-activate-cloud-account-in-scm/gcp-onboarding-prereq-and-steps/onboard-gcp-cloud-account-in-scm
fetched_at: 2026-08-13T14:02:37Z
source: ai-security
---

# Onboard GCP Cloud Account in Strata Cloud Manager Clear

Onboard GCP Cloud Account in Strata Cloud Manager 

 Home 

 EN

 Location 

 Documentation Home 

 Palo Alto Networks 

 Support 

 Live Community 

 Knowledge Base 

 >

 Strata Copilot

 Onboard GCP Cloud Account in Strata Cloud Manager 

 Updated on 

 Tue Aug 11 09:28:58 PDT 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma AIRS Docs 

 Activation & Onboarding 

 Administration 

 AI Model Security 

 AI Red Teaming 

 Release Notes 

 New Features 

 Updated on 

 Tue Aug 11 09:28:58 PDT 2026 

 Focus 

 Home 

 Prisma AIRS 

 Activation & Onboarding 

 Onboard and Activate a Cloud Account in Strata Cloud Manager 

 Onboard Cloud Account in GCP 

 Onboard GCP Cloud Account in Strata Cloud Manager 

 Download PDF 

 Prisma AIRS 

 Onboard GCP Cloud Account in Strata Cloud Manager 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma AIRS Docs 

 Activation & Onboarding 

 Administration 

 AI Model Security 

 AI Red Teaming 

 Release Notes 

 New Features 

 Previous 

 GCP Cloud Account Onboarding Prerequisites 

 Next 

 Onboard Cloud Account in Azure 

 Onboard GCP Cloud Account in Strata Cloud Manager 

 Onboard your GCP cloud account in Strata Cloud Manager . 

 Where Can I Use This? What Do I Need? 

 Creating a GCP Service Account for Strata Cloud
 Manager Integration 

 GCP Cloud Account Onboarding Prerequisites 

 Palo Alto Networks is migrating Discovery services to a new
 infrastructure from the SCM environment to the Multi-Cloud Security Fabric (MSF)
 platform. This change affects existing customers who have onboarded cloud accounts
 and requires action. See the section Migrate from Discovery Services . 

 Onboard GCP cloud account in Strata Cloud Manager . Create and download an onboarding
 Terraform template. When you apply this template in your cloud environment, it
 generates a service account with sufficient permissions. These permissions enable
 discovery within your cloud environment, allowing Prisma AIRS 
 AI Runtime firewall or VM-Series firewall to access the network flow
 logs, asset inventory details, and other essential cloud resources. 

 Log in to Strata Cloud Manager . 

 Navigate to AI Security → AI
 Runtime → AI Runtime Firewall . (If you are
 onboarding for the first time, click Get Started . 

 If you have previously onboarded a cloud account; from the top right corner,
 click the Cloud Account Manager (cloud) icon. 

 Select Cloud Service Provider as GCP and select
 Next . 

 Enter basic information: 

 A unique Name to identify your onboarded cloud account (Limit the
 name to 32 characters). 

 The GCP Project ID . 

 Input (Storage) Bucket Name you created in the Create a Cloud Storage Bucket prerequisite step. 
 Select Next . 

 In Application Definition , configure how your assets will be grouped for
 discovery. 

 Enhanced application definition options provide granular boundary
 criteria using workload-specific methods such as tags, subnets, and
 namespaces that align with your application deployment patterns and business
 logic. 

 Your selected application boundaries determine which
 applications appear in the deployment workflow .
 For all workload types, Prisma AIRS AI Runtime firewall maps
 applications to their VPCs, and the firewall protects traffic at
 the VPC level. The namespace shows applications from
 Pods/Cluster workloads, while VPC/VNETs display applications
 from virtual machine workloads. 

 For container workloads, regardless of the application
 definition method you select (namespace, cluster, or tag),
 please annotate all pods if you want to add protection with the
 Palo Alto Networks-specific label
 "paloaltonetworks.com/firewall": "pan-fw". This annotation is
 needed to secure the pods, in addition to defining the
 application boundaries. 

 When using tag-based
 application boundaries, if your cloud provider allows tags with
 only keys (no values), you should use the application name as
 the tag key. 

 Table: Workload-specific selection guide 

 Workloads Application Definition Method Choose When 

 Container Workloads 

 (Default boundary: namespace) 

 Namespace 

 Cluster Name 

 Tag 

 Applications are separated by Kubernetes
 namespaces for logical isolation. 

 Applications span multiple namespaces but remain
 within a single cluster. 

 Applications require custom grouping based on
 business logic, regardless of infrastructure. 

 Virtual Machines 

 (Default boundary: VPC/VNET) 

 Subnet Name 

 VPC/VNET 

 Tag 

 VMs are organized by network segments that align
 with application boundaries. 

 You prefer a broader network perimeter-based
 application grouping (default). 

 Uses key-value pairs for business-context-driven
 application organization. 

 Serverless Compute 

 (Default boundary VPC/VNET) 

 Subnet Name 

 VPC/VNET 

 Tag 

 Functions are deployed in specific subnet
 boundaries within the application domain. 

 You want to group all functions within the same
 network level using VPC/VNET boundaries. 

 Uses key-value pairs for flexible business
 requirement-based grouping. 

 select Next . 

 Input Service Account Name (Enter only lowercase letters and numbers; the
 name must be between 3 and 24 characters). 

 Download Terraform . 

 Use one service account per project. 

 Execute Terraform . Unzip the downloaded Terraform zip file and follow
 the `README.md` file for instructions on deploying Prisma AIRS AI Runtime firewall Terraform in your cloud
 environment. 

 cd <unzipped-folder>/gcp //Change directory to the Terraform plan

#Deploy the Terraform
terraform init
terraform plan
terraform apply 

 Provide the required IAM Permissions to the user executing the
 Terraform template. 

 Once the `terraform apply` command completes, the following output is
 displayed: 

 Apply complete! Resources: 19 added, 0 changed, 0 destroyed.

Outputs:

service_account_email = "panw-discovery-****@PROJECT_ID.iam.gserviceaccount.com" 

 After executing Terraform, deploy services to your
 GKE cluster. For detailed instructions, see Deploy an application to a GKE
 cluster . 

 Select Done . 
 It may take about 10 seconds before you can click on the “Done” button. This
 brief pause ensures all background processes complete successfully. This
 validates the successful creation of a service account in GCP. 

 After successfully connecting to the cloud service provider
 with the specified service account, the Prisma AIRS AI Runtime firewall gathers cloud VM and Kubernetes workload IP-tags
 from the Edge Service and tag collector, respectively. This discovery
 process can take up to 15 minutes before assets appear on the Strata Cloud Manager command center dashboard. 

 You can now view and manage the onboarded cloud
 accounts in Strata Cloud Manager . 

 To discover your protected and unprotected cloud assets, see the page on discovering your cloud
 resources . 
 Next, protect the network traffic flow by deploying Prisma AIRS AI Runtime: Network in
 GCP or VM-Series firewall. 

 Migrate from Discovery Services 

 When migrating consider the following: 

 GCP accounts will be fully disabled following the infrastructure migration
 from Fawkes to MSF due to the new Service Connector on MSF infrastructure.
 Existing GCP accounts cannot be re-enabled — you must onboard a new GCP
 account using the steps below. 

 CIPT continues to function on the old disabled GCP account during and after
 migration. To restore full CIPT functionality on the new
 infrastructure: 

 Onboard a new GCP account following the steps provided on the Migrate from Discovery Services
 page . 

 Configure Cloud IP Tag service on the new GCP account. 

 Verify CIPT is operating correctly on the new account. 

 Delete the old (disabled) GCP account. 

 Previous 

 GCP Cloud Account Onboarding Prerequisites 

 Next 

 Onboard Cloud Account in Azure 

 On This Page 

 Activation & Onboarding 

 Strata Cloud Manager 

 Activate a License or Product 

 Cloud Identity Engine 

 Strata Logging Service 

 Device Associations 

 Hub 

 Identity and Access Management 

 Tenant Management 

 Next-Generation Firewalls 

 CN-Series 

 Firewalls 

 VM-Series 

 Cloud-Delivered Security Services 

 Advanced URL Filtering 

 Advanced Threat Prevention 

 Advanced DNS Security 

 Enterprise DLP 

 Network Security 

 Visibility & Monitoring 

 Dashboards 

 Incidents and Alerts 

 Reports 

 Autonomous DEM 

 Activation & Onboarding 

 Google Cloud Platform 

 Prisma AIRS 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

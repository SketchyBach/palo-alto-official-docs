---
url: https://docs.paloaltonetworks.com/enterprise-dlp/administration/monitor-enterprise-dlp/save-evidence-for-investigative-analysis-with-enterprise-data-loss-prevention/set-up-cloud-storage-on-microsoft-azure-to-save-evidence
fetched_at: 2026-08-13T15:32:22Z
source: palo-alto-main
---

# Set Up Cloud Storage on Microsoft Azure to Save Evidence Clear

Set Up Cloud Storage on Microsoft Azure to Save Evidence 

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

 Set Up Cloud Storage on Microsoft Azure to Save Evidence 

 Updated on 

 Fri Jul 10 12:56:22 PDT 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Enterprise DLP Docs 

 Activation & Onboarding 

 Getting Started 

 Administration 

 Reference 

 Release Notes 

 New Features by OS Version 

 New Features by Month 

 Updated on 

 Fri Jul 10 12:56:22 PDT 2026 

 Focus 

 Home 

 Enterprise DLP 

 Administration 

 Monitor Enterprise DLP 

 Save Evidence for Investigative Analysis with Enterprise DLP 

 Set Up Cloud Storage on Microsoft Azure to Save Evidence 

 Download PDF 

 Enterprise DLP 

 Set Up Cloud Storage on Microsoft Azure to Save Evidence 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Enterprise DLP Docs 

 Activation & Onboarding 

 Getting Started 

 Administration 

 Reference 

 Release Notes 

 New Features by OS Version 

 New Features by Month 

 Previous 

 Set Up Cloud Storage on AWS to Save Evidence 

 Next 

 Download Files for Evidence Analysis 

 Set Up Cloud Storage on Microsoft Azure to Save Evidence 

 Configure cloud storage on Microsoft Azure to save evidence for investigative
 analysis with Enterprise Data Loss Prevention (E-DLP) . 

 On May 7, 2025 , Palo Alto Networks is introducing new Evidence Storage and Syslog Forwarding service IP
 addresses to improve performance and expand availability for these services
 globally. 

 You must allow these new service IP addresses on your network
 to avoid disruptions for these services. Review the Enterprise DLP 
 Release Notes for more
 information. 

 Where Can I Use This? What Do I Need? 

 NGFW (Managed by Panorama or Strata Cloud Manager) 

 Prisma Access (Managed by Panorama or Strata Cloud Manager) 

 Prisma Browser 

 Enterprise Data Loss Prevention (E-DLP) license 

 Review the Supported
 Platforms for details on the required license
 for each enforcement point. 

 Or any of the following licenses that include the Enterprise DLP license 

 Prisma Access CASB license 

 Next-Generation
CASB for Prisma Access and NGFW (CASB-X) license 

 Data Security license 

 Microsoft Azure users can configure a blob storage bucket to automatically upload all
 files that match an Enterprise Data Loss Prevention (E-DLP) data profile. 

 To store files scanned by Enterprise DLP , you must create a storage account and
 Identity and Access Management (IAM) role that allows Enterprise DLP access to
 automatically store files. Files uploaded to your storage account are automatically
 named using a unique Report ID for each file. The Report ID is used to search and
 download specific files for more in-depth investigation. 

 Enterprise DLP automatically sends email alerts to the data security
 administrator who originally connected Enterprise DLP to the storage bucket and
 to the data security admin who last modified the storage bucket settings in case of
 connection issues. Enterprise DLP sends the email alert every 48 hours until
 you restore the connection between Enterprise DLP and the storage bucket. 

 Files not scanned while Enterprise DLP is disconnected from your storage
 bucket can't be stored and are lost. This means that all impacted files are not
 available for download. However, your data security administrator can still view
 all snippet data associated with the DLP incident . 

 Enterprise DLP automatically resumes forwarding files to your storage bucket
 after you restore the connection. 

 Review the setup prerequisites for Enterprise DLP and enable the required ports, fully qualified domain names
 (FQDN), and IP addresses on your network. 

 Log in to the Microsoft Azure portal as an administrator. 
 Administrator-level privileges are required to add the Enterprise DLP 
 evidence storage application using Cloud Shell and to configure access to the
 storage account for file uploads. 

 ( Optional ) From the portal menu, select Storage
 groups and click Create to create a new storage group . 

 You can also search for storage groups . 

 The storage group is required to associate the storage account you create
 next for storing matched files. 

 Skip this step if you have an existing resource group that you want to
 associate with the storage account. 

 From the portal menu, select Storage accounts and click
 Create to create a new storage account . 

 You can also search for storage accounts . 

 Obtain the App-ID, Tenant ID, and blob service endpoint URL. 
 You need this information to add the Palo Alto Networks Enterprise DLP 
 application to your Microsoft Azure tenant and to configure connectivity to Enterprise DLP . 

 Palo Alto Networks Enterprise DLP App ID - 65def4b7-bae6-4bff-ab73-63fe8c9a3c8d 

 Obtain your Tenant ID. 

 From the portal menu, select Azure Active
 Directory . 

 You can also search for azure active
 directory . 

 In the Basic Information section, copy the Tenant
 ID . 

 Obtain the blob service endpoint URL. 

 From the portal menu, select Storage
 accounts and select the storage account you want
 to use to save files for evidence analysis. 

 Select Settings Endpoints and copy the Blob
 service endpoint URL. 

 Add the Palo Alto Networks Enterprise DLP application. 

 Open Cloud Shell . 
 Click the Cloud Shell icon in the top-right corner of the Microsoft
 Azure portal. 

 Add the Palo Alto Networks Enterprise DLP application. 

 Connect-AzureAD -TenantID
 <Your_Tenant_ID> 

 New-AzureADServicePrincipal -AppId
 65def4b7-bae6-4bff-ab73-63fe8c9a3c8d 

 It might take a few minutes for Microsoft Azure to add a new
 application to your Azure tenant. 

 Close the Cloud Shell. 

 Search for and select Enterprise
 applications . 

 For the Application type, choose All
 applications . 

 Search for the Palo Alto Networks Enterprise DLP application name to verify you successfully added the
 application. 

 Configure permissions for the Palo Alto Networks Enterprise DLP 
 application. 

 Select the Palo Alto Networks Enterprise DLP application name. 

 Select Security Permissions and click Grant Admin consent . 

 Select the administrator email in the Microsoft login prompt. 

 Accept the permissions request to allow Enterprise DLP to view your Azure storage accounts. 

 It might take a few minutes for the permissions to be granted to Enterprise DLP . 

 You still need to grant Enterprise DLP permission to write to a
 specific storage account. 

 Verify that the Azure Storage and
 Microsoft Graph API names are displayed
 in the Admin consent section. 

 From the portal menu, select Storage accounts 
 and select the storage account you want to use to save files for
 evidence analysis. 

 Select Access Control (IAM) Add Add Role Assignment Storage Blob Data Owner and click Next . 

 Select to assign access to User, group, or service
 principal and click Select
 members . 

 Search for and select the Palo Alto Networks Enterprise DLP application. 

 Click Review + assign to allow Enterprise DLP to write to the storage account. 

 It can take up to 10 minutes for the write permissions to be granted
 to Enterprise DLP . 

 Configure the evidence storage connection on Strata Cloud Manager . 

 Log in to 
 Strata Cloud Manager . 

 Access to evidence storage settings and files on Strata Cloud Manager is allowed only for an account administrator or app
 administrator role with Enterprise DLP read and
 write privileges. 

 Select Configuration Data Loss Prevention Settings Sensitive Data and navigate to Evidence
 Storage . 

 Select the enforcement points for which you want to enable Evidence
 Storage for. 

 You can enable evidence storage for Prisma Browser , Prisma Access , and Endpoint
 DLP. 

 Select Configure Regional Bucket Azure 

 Select the Region(s) from which you want to
 forward evidence files to the storage bucket. 

 You can associate storage accounts in different Azure regions with
 your DLP regions. When DLP incidents are generated in the regions you
 select here, Enterprise DLP forwards the incident evidence to
 the storage bucket. 

 Review the Instructions - Azure and click
 Next . 

 In Input Bucket Details , enter the Microsoft
 Azure Tenant ID. 

 Enter the Storage Endpoint. 

 This is the blob service endpoint URL that you obtained for the
 storage account. 

 Click Connect to connect Enterprise DLP 
 to your storage bucket. 

 Review the Connection Status to verify Enterprise DLP successfully connected to your storage bucket. 

 As part of the setup process, Enterprise DLP uploads a
 Palo_Alto_Networks_DLP_Connection_Test.txt 
 file to your storage bucket to test and verify connectivity. 

 Save the storage bucket settings if Enterprise DLP successfully connected. 

 Select Previous and edit the bucket connection
 settings if Enterprise DLP can't connect to your storage
 bucket. 

 ( Email DLP only ) Select Configuration SaaS Security Settings Email DLP Settings and enable Evidence Storage for Email DLP. 

 Enterprise DLP won't forward evidence files for Email DLP traffic
 matches unless you enable this setting. 

 Enable Sensitive Files for your enforcement
 points. 

 You can enable evidence storage of sensitive files for Prisma Access , NGFW , and Endpoint DLP. Enable 
 evidence storage when prompted to confirm. 

 Download Files for Evidence Analysis . 

 Previous 

 Set Up Cloud Storage on AWS to Save Evidence 

 Next 

 Download Files for Evidence Analysis 

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

 AIOps for NGFW 

 Cloud Management for NGFWs 

 Cloud NGFW for AWS 

 Cloud NGFW for Azure 

 CN-Series 

 Firewalls 

 PAN-OS 

 PAN-OS SD-WAN 

 Service Provider 

 VM-Series 

 SASE 

 Prisma Access 

 Strata Multitenant Cloud Manager 

 AI-Powered ADEM 

 Prisma Access Monitoring and Visibility 

 Prisma SD-WAN 

 ION Devices 

 Next-Generation CASB 

 Cloud-Delivered Security Services 

 Advanced WildFire 

 Advanced URL Filtering 

 Advanced Threat Prevention 

 Advanced DNS Security 

 Device Security 

 SaaS Security 

 Endpoints 

 GlobalProtect 

 Visibility & Monitoring 

 Dashboards 

 Incidents and Alerts 

 Reports 

 Autonomous DEM 

 Best Practices 

 Best Practices Library 

 Experts Corner 

 Solutions Docs from Product Experts 

 Administration 

 Cloud-Delivered Security Services 

 Data Filtering 

 Enterprise DLP 

 Task 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

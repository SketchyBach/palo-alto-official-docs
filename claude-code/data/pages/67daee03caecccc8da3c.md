---
url: https://docs.paloaltonetworks.com/content/techdocs/en_US/enterprise-dlp/administration/monitor-enterprise-dlp/save-evidence-for-investigative-analysis-with-enterprise-data-loss-prevention/set-up-cloud-storage-on-aws-to-save-evidence/set-up-cloud-storage-on-aws-using-aws-kms-for-cloud-management.html
fetched_at: 2026-09-16T13:01:44Z
source: palo-alto-main
---

# Set up Evidence Storage on Strata Cloud Manager Using AWS KMS Clear

Updated on 

 Thu Sep 10 12:41:05 PDT 2026 

 Focus 

 Home 

 Enterprise DLP 

 Administration 

 Monitor Enterprise DLP 

 Save Evidence for Investigative Analysis with Enterprise DLP 

 Set Up Cloud Storage on AWS to Save Evidence 

 Set up Evidence Storage on Strata Cloud Manager Using AWS KMS 

 Download PDF 

 Enterprise DLP 

 Set up Evidence Storage on Strata Cloud Manager Using AWS KMS 

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

 Set up Evidence Storage on Strata Cloud Manager Using AWS KMS 

 Create an S3 storage bucket on AWS using the AWS Key Management Service (KMS) to
 store files that match your Enterprise Data Loss Prevention (E-DLP) data profiles on Strata Cloud Manager . 

 Review the setup prerequisites for Enterprise DLP and enable the required ports, fully qualified domain names
 (FQDN), and IP addresses on your network. 

 Create an S3 storage bucket with AWS KMS encryption to store files scanned by
 Enterprise DLP . 

 Log in to the Amazon AWS console . 

 Select Services Storage S3 Buckets and click Create bucket . 

 Enter a descriptive Bucket name . 

 Select the AWS Region for the S3 storage
 bucket. 

 In the Default encryption section, select
 AWS Key Management Service (SSE-KMS) as the
 Encryption key type . 

 To specify the AWS KMS key , choose
 Choose from your AWS KMS keys or
 Enter AWS key ARN . 

 You can click Create a KMS Key if one doesn't
 already exist. Refer to AWS Documentation for
 details on creating a new KMS key. 

 Click Create bucket . 

 Obtain the ARN for the S3 storage bucket. 

 After creating the S3 storage bucket, you're redirected back to the
 Buckets page. Search for and click the
 storage bucket you created. 

 Click Properties . The storage bucket ARN is
 displayed in the Bucket overview . 

 Obtain the trust relationship and access policy JSONs from Strata Cloud Manager . 

 You need these JSONs to create the IAM role that allows Enterprise DLP 
 to write to your S3 storage bucket. 

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

 Select Configure Regional Bucket AWS . 

 Enable KMS Enabled to use an S3 storage bucket
 with AWS KMS encryption. 

 In Instructions - AWS , copy the trust
 relationship JSON and the access policy JSON. 

 The first JSON is the trust relationship and the second is the access
 policy. You use these JSONs in the next step to create the IAM role
 for the S3 storage bucket. 

 Leave this browser tab open. You return here after creating the IAM
 role to complete the evidence storage configuration. 

 Create the IAM role for the S3 storage bucket. 

 This role allows Enterprise DLP to write evidence files to your S3
 storage bucket. 

 Log in to the Amazon AWS console . 

 Select Services Security, Identity, and Compliance IAM Access management Roles and click Create role . 

 For the Trusted entity type , select
 Custom trust policy . 

 Paste the trust relationship JSON you copied from Strata Cloud Manager into the Custom trust policy 
 editor. 

 Click Next . 

 In Add permissions , select Create policy JSON . 

 A new browser window opens for the policy editor. 

 Paste the access policy JSON you copied from Strata Cloud Manager 
 into the Policy editor . 

 Replace all instances of
 bucket_name_to_be_replaced in the JSON
 with the S3 storage bucket ARN you obtained earlier. 

 Add the AWS KMS key ARN. 

 The AWS KMS ARN you add here must be the same AWS KMS Key ARN you
 provided when you created the S3 storage bucket. 

 Click Next . 

 Enter a Policy name and click
 Create policy . 

 Return to the browser window where you're creating the IAM role. 

 Search for and select the access policy you created. 

 Click Next . 

 Enter a descriptive Role name for the IAM
 role. 

 Review the IAM role trust relationship and access policy. 

 Click Create role . 

 Configure the evidence storage connection on Strata Cloud Manager . 

 Return to the Strata Cloud Manager browser tab you left open and complete
 the evidence storage configuration wizard. 

 Select the Region(s) from which you want to
 forward evidence files to the storage bucket. 

 You can associate S3 buckets in different AWS regions with your DLP
 regions. When DLP incidents are generated in the regions you select
 here, Enterprise DLP forwards the incident evidence to the
 storage bucket. 

 Review the Instructions - AWS and click
 Next . 

 In Input Bucket Details , enter the
 S3 Bucket Name of the bucket you
 created. 

 The name you enter here must match the name of the S3 storage bucket
 on AWS. 

 Enter the Role ARN for the IAM role you
 created. 

 The IAM Role ARN is displayed in the
 Summary of the IAM role
 Permissions on the Amazon AWS
 console. 

 Select the AWS Region where the bucket is
 located. 

 This region corresponds to where you deployed your AWS storage
 bucket, not the DLP region where incidents are generated. 

 Click Connect to connect Enterprise DLP 
 to your S3 storage bucket. 

 Review the Connection Status to verify Enterprise DLP successfully connected to your S3 storage
 bucket. 

 As part of the setup process, Enterprise DLP uploads a
 Palo_Alto_Networks_DLP_Connection_Test.txt 
 file to your S3 storage bucket to test and verify connectivity. 

 Save the storage bucket settings if Enterprise DLP successfully connected. 

 Select Previous and edit the bucket connection
 settings if Enterprise DLP can't connect to your S3 storage
 bucket. 

 ( Email DLP only ) Select Configuration SaaS Security Settings Email DLP Settings and enable Evidence Storage for Email DLP. 

 Enterprise DLP won't forward evidence files for Email DLP traffic
 matches unless you enable this setting. 

 Enable Sensitive Files for your enforcement
 points. 

 You can enable evidence storage of sensitive files for Prisma Access , NGFW , and Endpoint DLP. Enable 
 evidence storage when prompted to confirm. 

 Download Files for Evidence Analysis .

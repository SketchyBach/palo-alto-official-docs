---
url: https://cortex-docs.paloaltonetworks.com/cortex-analytics-content-releases/cortex-analytics-content-release-notes/2026-07-29
fetched_at: 2026-09-16T09:02:23Z
source: cortex-platform
---

# 2026.07.29 | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Release Notes 

 Content Releases 

 Cortex Analytics Content Releases 

 Cortex Analytics Content Release Notes 

 2026.07.29 

 Release date: 09-August-2026 

 Summary 

 Added 

 3 Detectors: 1 High, 1 Low, 1 Informational 

 3 Variations: 1 High, 1 Low, 1 Informational 

 Removed 

 1 Detector: 1 Informational 

 1 Variation: 1 Low 

 Modified Logic 

 493 Detectors: 5 High, 10 Medium, 67 Low, 411 Informational 

 55 Variations: 1 High, 2 Medium, 17 Low, 35 Informational 

 Modified Metadata 

 6 Detectors: 1 Low, 5 Informational 

 2 Variations: 2 Low 

 Added 

 [High] EC2 backdoor created with newly added external SSH or RDP access 

 [High] EC2 backdoor created with a newly added external SSH or RDP access by a rarely used identity 

 [Low] AWS Security Group remote access allowed from an unknown external IP address 

 [Informational] Cloud infrastructure discovery across multiple regions 

 [Low] Cloud infrastructure discovery across multiple AWS services and regions 

 [Informational] Cloud infrastructure discovery across multiple AWS services within a single region 

 Removed 

 [Informational] Uncommon net localgroup execution 

 [Low] Uncommon net localgroup execution by an untrusted CGO 

 Modified Logic 

 [Informational] Cloud instance creation attempt 

 [High] EC2 instance creation with admin profile, public IP address and external security group - Added 

 [Medium] EC2 instance creation with admin profile and public IP address - Added 

 [High] Cloud penetration testing tool activity 

 [High] Multiple risk indicators for a cloud identity 

 [High] Suspicious AI model usage from a Tor exit node 

 [High] Suspicious API call from a Tor exit node 

 [High] Suspicious objects encryption in an AWS bucket 

 [Medium] A Kubernetes API operation was successfully invoked by an anonymous user 

 [Medium] A Kubernetes dashboard service account was used outside the cluster 

 [Medium] A cloud storage object was copied to a foreign cloud account 

 [Informational] A user accessed multiple unusual resources via SSO 

 [Medium] A user accessed multiple resources via SSO using an anonymized proxy - Modified Metadata 

 [Low] Multiple Resource Access from a New IP via SSO - Modified Metadata 

 [Low] Suspicious user access to multiple resources via SSO - Modified Metadata 

 [Medium] Azure AD PIM alert disabled 

 [Medium] Cloud snapshot of a database or storage instance was publicly shared 

 [Medium] Command execution via AWS SSM 

 [Medium] Kubernetes vulnerability scanning tool usage 

 [Medium] Logging was impaired via external encryption key 

 [Medium] Potential Phishing has been detected 

 [Medium] Suspicious heavy allocation of compute resources - possible mining activity 

 [Low] A Backup vault policy was modified 

 [Low] A Command Line Interface (CLI) command was executed from a GCP serverless compute service 

 [Low] A Command Line Interface (CLI) command was executed from an AWS serverless compute service 

 [Low] A cloud function was created with an unusual runtime 

 [Low] AI model discovery 

 [Low] AWS Bedrock model invocation logging deletion 

 [Low] AWS Guard-Duty detector deletion 

 [Low] AWS IAM Role Created with Cross-Account Access 

 [Low] AWS IAM Role's Trusted Policy Modification Allows Cross-Account Access 

 [Low] AWS Lambda Cross-Account sensitive permissions configured 

 [Low] AWS S3 bucket was exposed to public access 

 [Low] AWS data asset shared public 

 [Low] An Azure Firewall policy deletion 

 [Low] An RDS snapshot was exported to an unknown S3 bucket 

 [Low] An S3 replication policy to an unknown bucket was created 

 [Low] An identity successfully extracted multiple secrets within the organization 

 [Informational] An uncommon file added to startup-related Registry keys 

 [Low] An uncommon LOLBIN added to startup-related Registry keys - Modified Metadata 

 [Low] An uncommon file added to startup-related Registry keys by a remote actor - Modified Metadata 

 [Low] An uncommon file added to startup-related Registry keys by an unsigned and unpopular CGO process - Modified Metadata 

 [Low] An uncommon script added to startup-related Registry keys - Modified Metadata 

 [Low] Azure AD PIM role settings change 

 [Low] Azure Event Hub Deletion 

 [Informational] Azure Monitor alert rule deleted 

 [Informational -> Low] Azure Monitor alert rule deleted by compute workload - Modified Metadata 

 [Informational -> Low] Unusual Azure Monitor alert rule deletion - Modified Metadata 

 [Low] Azure Network Watcher Deletion 

 [Informational] Azure VM extension abuse attempt 

 [Informational -> Low] Unusual azure VM extension abuse - Modified Metadata 

 [Low] Azure account deletion by a non-standard account 

 [Low] Azure domain federation settings modification attempt 

 [Informational] Azure route table creation or modification 

 [Informational -> Low] Unusual Azure route table creation or modification - Modified Metadata 

 [Informational] Azure virtual machine commands execution 

 [Informational -> Low] Unusual Azure VM remote command execution - Modified Metadata 

 [Informational] Azure managed Run Command (runCommands/write) execution - Removed 

 [Low] Bedrock model shared with a foreign account 

 [Low] Billing admin role was removed 

 [Informational] Common third-party software name masquerading 

 [Low] Common third-party software name masquerading which was downloaded from an unexpected source - Modified Metadata 

 [Low] Conditional Access policy removed 

 [Low] Data exfiltration from cloud database 

 [Low] Disable encryption operations 

 [Low] Email attachment with Right-to-Left Override Unicode character 

 [Low] Email was received from an unknown sender using a disposable domain 

 [Low] Email with file-sharing link containing auto-download parameter 

 [Low] First Azure AD PowerShell operation for a user 

 [Informational] First-seen email from mailbox owner to external recipient's address in the last 30 days 

 [Low] First-time email to the disposable domain - Modified Metadata 

 [Informational] First-time outbound email from mailbox owner to multiple external recipients without any internal recipients in the last 30 days - Modified Logic 

 [Low] GCP IAM deny policy creation 

 [Low] GCP data asset shared public 

 [Low] GCP sensitive role granted to group 

 [Informational] Globally uncommon high entropy process was executed 

 [Low] Globally uncommon high entropy process was executed by an untrusted CGO - Temporarily Removed 

 [Low] HTTP with suspicious characteristics 

 [Low] Kubernetes pod creation from unknown container image registry 

 [Low] Large Upload (Generic) 

 [Low] MFA was disabled for an Azure identity 

 [Low] ML artifacts destruction 

 [Low] Microsoft 365 storage services exfiltration activity 

 [Low] Multiple Azure AD admin role removals 

 [Low] New cloud identity created with administrative policy 

 [Low] Possible multistage attack in Microsoft Teams 

 [Low] Possible phishing attack via Microsoft Teams 

 [Low] Potential denial of wallet abusing AI services 

 [Low] Potential kubelet impersonation attempt 

 [Low] PowerShell runs suspicious base64-encoded commands 

 [Low] Privileged role used by Azure application 

 [Low] Recurring access to rare domain 

 [Low] Recurring rare domain access to dynamic DNS domain 

 [Low] Remote usage of an AWS service token 

 [Low] Remote usage of an Azure Managed Identity token 

 [Low] Sending unusual file(s) to an external address 

 [Low] Suspicious AI Dataset Download 

 [Low] Suspicious AI Dataset Label Modification 

 [Low] Suspicious EBS snapshots deletion 

 [Informational] Suspicious SSO access from ASN 

 [Low] Suspicious SSO access from ASN via a suspicious IP - Modified Metadata 

 [Informational] Google Workspace - Suspicious SSO access from ASN - Modified Logic 

 [Low] Suspicious access to Kubernetes API with kubelet credentials 

 [Low] Suspicious activity indicating a potential abuse of a cloud-native email service 

 [Low] Suspicious cloud user data modification attempt followed by VM restart 

 [Low] Suspicious identity downloaded multiple objects from a bucket 

 [Low] Suspicious usage of EC2 token 

 [Medium -> Low] Training simulation email detected 

 [Informational -> Low] Uncommon Azure Cosmos DB master key read by identity 

 [Informational] Uncommon user management via net.exe 

 [Low] Uncommon user management via net.exe by an untrusted CGO - Temporarily Removed 

 [Low] Unsigned process creates a scheduled task via file access 

 [Low] Unusual AI Knowledge Base Modification 

 [Low] Unusual AI RAG Knowledge Base Modification 

 [Low] Unusual AI dataset modification 

 [Low] Unusual cross projects activity 

 [Informational] Windows CGO, actor and action processes with anomalous characteristics 

 [Low] Windows CGO, actor and action processes with anomalous characteristics by an untrusted CGO - Temporarily Removed 

 [Informational] A Cloud DB instance was exported to an unknown destination 

 [Informational] A GCP Cloud SQL DB instance was exported from a production account 

 [Informational] A Kubernetes ConfigMap was created or deleted 

 [Informational] A Kubernetes Cronjob was created 

 [Informational] A Kubernetes DaemonSet was created 

 [Informational] A Kubernetes Pod was created with a sidecar container 

 [Informational] A Kubernetes Pod was deleted 

 [Informational] A Kubernetes ReplicaSet was created 

 [Informational] A Kubernetes StatefulSet was created 

 [Informational] A Kubernetes cluster role binding was created or deleted 

 [Informational] A Kubernetes cluster role was created 

 [Informational] A Kubernetes cluster was created or deleted 

 [Informational] A Kubernetes deployment was created 

 [Informational] A Kubernetes ephemeral container was created 

 [Informational] A Kubernetes namespace was created or deleted 

 [Informational] A Kubernetes node service account activity from external IP 

 [Informational] A Kubernetes role binding was created or deleted 

 [Informational] A Kubernetes secret was created or deleted 

 [Informational] A Kubernetes service account executed an unusual API call 

 [Informational] A Kubernetes service account has enumerated its permissions 

 [Informational] A Kubernetes service account was created or deleted 

 [Informational] A Kubernetes service was created or deleted 

 [Informational] A New Server was Added to an Azure Active Directory Hybrid Health ADFS Environment 

 [Informational] A Service Principal was created in Azure 

 [Informational] A Service Principal was removed from Azure 

 [Informational] A cloud identity created or modified a security group 

 [Informational] A cloud identity executed an API call from an unusual country 

 [Informational] A cloud identity had escalated its permissions 

 [Informational] A cloud identity invoked IAM related persistence operations 

 [Informational] A cloud identity started a Cloud Shell session 

 [Informational] A cloud instance was stopped 

 [Informational] A cloud snapshot of AWS database or storage was modified or shared 

 [Informational] A cloud storage configuration was modified 

 [Informational] A compute-attached identity executed API calls outside the instance's region 

 [Informational] A container registry was created or deleted 

 [Informational] A new Azure email domain verification was requested 

 [Informational] A non-browser process accessed a website UI 

 [Informational] A user logged in to the AWS console for the first time 

 [Informational] AI safeguards deletion attempt 

 [Informational] AI safeguards were modified 

 [Informational] AWS Backup recovery point deletion 

 [Informational] AWS Backup vault was deleted 

 [Informational] AWS Bedrock AI infrastructure enumeration activity 

 [Informational] AWS CloudTrail has been stopped 

 [Informational] AWS CloudTrail modification 

 [Informational] AWS CloudWatch log group deletion 

 [Informational] AWS CloudWatch log stream deletion 

 [Informational] AWS Config Recorder stopped 

 [Informational] AWS EBS enumeration activity 

 [Informational] AWS EBS snapshot deletion 

 [Informational] AWS EC2 infrastructure enumeration activity 

 [Informational] AWS EC2 instance exported into S3 

 [Informational] AWS Flow Logs deletion 

 [Informational] AWS IAM resource group deletion 

 [Informational] AWS Lambda infrastructure enumeration activity 

 [Informational] AWS Password Policy Discovery 

 [Informational] AWS RDS cluster deletion 

 [Informational] AWS S3 Buckets enumeration activity 

 [Informational] AWS S3 bucket data retention policy change through S3 Lifecycle rule 

 [Informational] AWS SES account sending settings modified 

 [Informational] AWS SSM association created with inventory collection document 

 [Informational] AWS SSM parameters discovery 

 [Informational] AWS SSM parameters retrieval 

 [Informational] AWS SSM send command attempt 

 [Informational] AWS STS temporary credentials were generated 

 [Informational] AWS Secrets Manager discovery 

 [Informational] AWS Security Service Enumeration 

 [Informational] AWS SecurityHub findings were modified 

 [Informational] AWS Storage Gateway enumeration 

 [Informational] AWS Storage Gateway file share enumeration 

 [Informational] AWS Systems Manager hosts enumeration 

 [Informational] AWS Transfer Family server created 

 [Informational] AWS config resource deletion 

 [Informational] AWS console login without MFA 

 [Informational] AWS network ACL rule creation 

 [Informational] AWS network ACL rule deletion 

 [Informational] AWS principals discovery 

 [Informational] AWS resource discovery 

 [Informational] AWS root account activity 

 [Informational] AWS support case creation 

 [Informational] AWS user creation 

 [Informational] AWS web ACL deletion 

 [Informational] Abnormal Allocation of compute resources in multiple regions 

 [Informational] Abnormal Recurring Communications to a Rare Domain 

 [Informational] Allocation of multiple cloud compute resources 

 [Informational] An AWS EC2 instance containing sensitive data was exported 

 [Informational] An AWS EC2 instance was exported from a production account 

 [Informational] An AWS EC2 instance was exported into an unknown S3 bucket 

 [Informational] An AWS EFS File-share mount was deleted 

 [Informational] An AWS EFS file-share was deleted 

 [Informational] An AWS EKS cluster was created or deleted 

 [Informational] An AWS GuardDuty IP set was created 

 [Informational] An AWS Lambda Function was created 

 [Informational] An AWS Lambda function was modified 

 [Informational] An AWS RDS Global Cluster Deletion 

 [Informational] An AWS RDS instance was created from a snapshot 

 [Informational] An AWS Route 53 domain was transferred to another AWS account 

 [Informational] An AWS S3 bucket configuration was modified 

 [Informational] An AWS SAML provider was modified 

 [Informational] An AWS SES identity was deleted 

 [Informational] An AWS database service master user password was changed 

 [Informational] An Azure DNS Zone was modified 

 [Informational] An Azure Firewall rule collection group was modified or deleted 

 [Informational] An Azure Firewall was modified 

 [Informational] An Azure Key Vault key was modified 

 [Informational] An Azure Key Vault was modified 

 [Informational] An Azure Kubernetes Cluster was created or deleted 

 [Informational] An Azure Kubernetes Role or Cluster-Role was modified 

 [Informational] An Azure Kubernetes Role-Binding or Cluster-Role-Binding was modified or deleted 

 [Informational] An Azure Kubernetes Service Account was modified or deleted 

 [Informational] An Azure Network Security Group was modified 

 [Informational] An Azure Point-to-Site VPN was modified 

 [Informational] An Azure SQL database was exported from a production subscription 

 [Informational] An Azure Suppression Rule was created 

 [Informational] An Azure VM snapshot SAS URL was generated 

 [Informational] An Azure VM snapshot SAS URL was generated for export from a production subscription 

 [Informational] An Azure VPN Connection was modified 

 [Informational] An Azure application reached a throttling API rate 

 [Informational] An Azure firewall rule group was modified 

 [Informational] An Azure identity performed multiple actions that were denied 

 [Informational] An Azure virtual network Device was modified 

 [Informational] An Azure virtual network was modified 

 [Informational] An EBS snapshot block was downloaded 

 [Informational] An Email address was added to AWS SES 

 [Informational] An IAM group was created 

 [Informational] An RDS snapshot containing sensitive data was exported 

 [Informational] An RDS snapshot was exported from a production account 

 [Informational] An RDS snapshot was exported to an unknown bucket 

 [Informational] An identity accessed Azure Kubernetes Secrets 

 [Informational] An identity accessed a backup cloud storage 

 [Informational] An identity accessed a cloud storage for the first time 

 [Informational] An identity attached an administrative policy to an IAM user or role 

 [Informational] An identity created or updated password for an IAM user 

 [Informational] An identity disabled bucket logging 

 [Informational] An identity initiated a download of multiple cloud objects 

 [Informational] An identity performed a suspicious download of multiple cloud storage objects 

 [Informational] An identity started an AWS SSM session 

 [Informational] An identity was granted permissions to manage user access to Azure resources 

 [Informational] An operation was performed by an identity from a domain that was not seen in the organization 

 [Informational] An unknown account was invited to the AWS organization 

 [Informational] An unusual cloud identity was granted permissions to a BigQuery resource 

 [Informational] An unusual read activity of cloud object 

 [Informational] Attempted Azure application access from unknown tenant 

 [Informational] Aurora DB cluster stopped 

 [Informational] Authentication method added to an Azure account 

 [Informational] Authentication method was added to Azure account 

 [Informational] Azure AD PIM elevation request 

 [Informational] Azure AD account unlock/password reset attempt 

 [Informational] Azure Automation Account Creation 

 [Informational] Azure Automation Runbook Creation/Modification 

 [Informational] Azure Automation Runbook Deletion 

 [Informational] Azure Automation Webhook creation 

 [Informational] Azure Blob Container Access Level Modification 

 [Informational] Azure Event Hub Authorization rule creation/modification 

 [Informational] Azure Key Vault Secrets were modified 

 [Informational] Azure Key Vault modification 

 [Informational] Azure Kubernetes events were deleted 

 [Informational] Azure Resource Group Deletion 

 [Informational] Azure Service principal/Application creation 

 [Informational] Azure Storage Account key generated 

 [Informational] Azure Temporary Access Pass (TAP) registered to an account 

 [Informational] Azure account creation by a non-standard account 

 [Informational] Azure application URI modification 

 [Informational] Azure application consent 

 [Informational] Azure application credentials added 

 [Informational] Azure application removed 

 [Informational] Azure conditional access policy creation or modification 

 [Informational] Azure device code authentication flow used 

 [Informational] Azure diagnostic configuration deletion 

 [Informational] Azure enumeration activity using Microsoft Graph API 

 [Informational] Azure group creation/deletion 

 [Informational] Azure mailbox rule creation 

 [Informational] Azure permission delegation granted 

 [Informational] Azure service principal assigned app role 

 [Informational] Azure storage account blob anonymous access is enabled 

 [Informational] Azure storage account cross-tenant object replication was enabled 

 [Informational] Azure storage account was publicly shared 

 [Informational] Azure user creation/deletion 

 [Informational] Azure user password reset 

 [Informational] BigQuery table or query results exfiltrated to a foreign project 

 [Informational] BitLocker key retrieval 

 [Informational] Bucket's block public access setting turned off 

 [Informational] Bucket's object ownership controls were modified 

 [Informational] Cloud AI agent was modified 

 [Informational] Cloud Organizational policy was created or modified 

 [Informational] Cloud Watch alarm deletion 

 [Informational] Cloud access key creation 

 [Informational] Cloud activity from a high-risk IP address 

 [Informational] Cloud compute instance user data script modification 

 [Informational] Cloud compute serial console access 

 [Informational] Cloud compute volume creation attempt 

 [Informational] Cloud email infrastructure enumeration activity 

 [Informational] Cloud email sending was enabled 

 [Informational] Cloud email service activity 

 [Informational] Cloud identity reached a throttling API rate 

 [Informational] Cloud impersonation attempt by unusual identity type 

 [Informational] Cloud infrastructure enumeration activity 

 [Informational] Cloud instance deletion attempt 

 [Informational] Cloud resource logging was disabled 

 [Informational] Cloud snapshot created or modified 

 [Informational] Cloud storage automatic backup disabled 

 [Informational] Cloud storage delete protection disabled 

 [Informational] Cloud user performed multiple actions that were denied 

 [Informational] CloudTrail logging deletion 

 [Informational] Compute activity in dormant cloud region 

 [Informational] Credentials were added to Azure application 

 [Informational] Data encryption was disabled 

 [Informational] Deletion of multiple cloud resources 

 [Informational] Denied API call by a Kubernetes service account 

 [Informational] Device Registration Policy modification 

 [Informational] Disable AWS audit logs through Event Selectors 

 [Informational] Display text URL differs from actual URL 

 [Informational] EBS snapshots were created from an EC2 instance 

 [Informational] EBS volume attachment attempt 

 [Informational] EBS volume detachment attempt 

 [Informational] EC2 instance Amazon machine image was created 

 [Informational] Email attachment with a potentially malicious file extension 

 [Informational] Attachment(s) with a potentially malicious file extension unusual for the organization - Modified Metadata 

 [Informational] Attachment(s) with a potentially malicious file extension unusual for the recipient - Modified Metadata 

 [Informational] Email attachment with multiple extensions 

 [Informational] Email attachment(s) with potentially malicious MIME type 

 [Informational] Attachment(s) with a potentially malicious MIME type that is unusual for the recipient - Modified Metadata 

 [Informational] Attachment(s) with potentially malicious MIME type unusual for the organization - Modified Metadata 

 [Informational] Email containing a link with an IP address convention was detected 

 [Informational] Email containing a redirected link 

 [Informational] Email containing a redirected link with multiple redirections - Modified Metadata 

 [Informational] Email contains URL delivering high-risk file type 

 [Informational] Email marked as spam and bulk based on Spam Confidence Level and Bulk Complaint Level values 

 [Informational] Email with high Spam Confidence Level and Bulk Complaint Level values - Modified Metadata 

 [Informational] Email with high Spam Confidence Level or Bulk Complaint Level values - Modified Metadata 

 [Informational] Email with medium Spam Confidence Level and Bulk Complaint Level values - Modified Metadata 

 [Informational] Email with medium Spam Confidence Level or Bulk Complaint Level values - Modified Metadata 

 [Informational] Email mimics replies or forwards without an actual ongoing conversation 

 [Informational] Email sent using an automated system or script detected 

 [Informational] Email was received from an unknown address using a public provider domain 

 [Informational] Email with URL shortener detected 

 [Informational] External email display name impersonation of internal personnel 

 [Informational] External email with a single internal recipient hidden in BCC 

 [Informational] External user invitation to Azure tenant 

 [Informational] First-time attachment exchange 

 [Informational] First-time directory sync of an on-premises domain user to an existing cloud account 

 [Informational] Foreign account was granted permissions to S3 bucket via resource-based policy 

 [Informational] GCP Firewall Rule Modification 

 [Informational] GCP Firewall Rule creation 

 [Informational] GCP IAM Role Deletion 

 [Informational] GCP IAM Service Account Key Deletion 

 [Informational] GCP Logging Bucket Deletion 

 [Informational] GCP Pub/Sub Subscription Deletion 

 [Informational] GCP Pub/Sub Topic Deletion 

 [Informational] GCP Service Account Deletion 

 [Informational] GCP Service Account Disable 

 [Informational] GCP Service Account creation 

 [Informational] GCP Service Account key creation 

 [Informational] GCP Storage Bucket Configuration Modification 

 [Informational] GCP Storage Bucket Permissions Modification 

 [Informational] GCP Storage Bucket deletion 

 [Informational] GCP VPC Firewall Rule Deletion 

 [Informational] GCP Virtual Private Cloud (VPC) Network Deletion 

 [Informational] GCP Virtual Private Network Route Creation 

 [Informational] GCP Virtual Private Network Route Deletion 

 [Informational] GCP administrative role granted to a cloud identity 

 [Informational] GCP logging sink deletion 

 [Informational] GCP logging sink modification 

 [Informational] GCP sensitive Cloud Run role granted 

 [Informational] GCP sensitive Deployment Manager role granted 

 [Informational] GCP sensitive Functions role granted 

 [Informational] GCP sensitive IAM role granted 

 [Informational] GCP sensitive Secret Manager role granted 

 [Informational] GCP sensitive compute role granted 

 [Informational] GCP sensitive storage role granted 

 [Informational] GCP service account impersonation attempt 

 [Informational] GCP set IAM policy activity 

 [Informational] Granting Access to an Account 

 [Informational] IAM Enumeration sequence 

 [Informational] IAM User added to an IAM group 

 [Informational] IAM inline policy was added to group 

 [Informational] IAM inline policy was added to role 

 [Informational] IAM inline policy was added to user 

 [Informational] IAM instance profile associations were described 

 [Informational] IAM instance profile was associated with EC2 instance 

 [Informational] IAM instance profile was created 

 [Informational] IAM instance profile was replaced for EC2 instance 

 [Informational] IAM policy default version was changed 

 [Informational] IAM policy version was created 

 [Informational] IAM policy was attached to group 

 [Informational] IAM policy was attached to role 

 [Informational] IAM role trust policy modification 

 [Informational] IAM role was created 

 [Informational] IAM role-attached managed policies were listed 

 [Informational] Identity assigned an Azure AD Administrator Role 

 [Informational] Impossible travel by a cloud identity 

 [Informational] Initial person-to-person email contact 

 [Informational] Kubernetes Pod Created With Sensitive Volume 

 [Informational] Kubernetes Pod Created with host Inter Process Communications (IPC) namespace 

 [Informational] Kubernetes Pod created with host process ID (PID) namespace 

 [Informational] Kubernetes Privileged Pod Creation 

 [Informational] Kubernetes admission controller activity 

 [Informational] Kubernetes cluster events deletion 

 [Informational] Kubernetes enumeration activity 

 [Informational] Kubernetes network policy modification 

 [Informational] Kubernetes pod creation with host network 

 [Informational] Kubernetes secrets enumeration for the first time 

 [Informational] Kubernetes service account activity outside the cluster 

 [Informational] Log enumeration via cloud native logging service 

 [Informational] MFA device was removed/deactivated from an IAM user 

 [Informational] Mailbox enumeration activity by Azure application 

 [Informational] Microsoft OneDrive enumeration activity 

 [Informational] Microsoft OneNote enumeration activity 

 [Informational] Microsoft SharePoint enumeration activity 

 [Informational] Microsoft Teams enumeration activity 

 [Informational] Modification or Deletion of an Azure Application Gateway Detected 

 [Informational] Moniker link detected in URL(s) 

 [Informational] Multi region enumeration activity 

 [Informational] Multiple cloud snapshots export 

 [Informational] Multiple failed AWS assume role attempts 

 [Informational] Multiple failed logins from a single IP 

 [Informational] Near-empty email from an external sender 

 [Informational] Network sniffing detected in Cloud environment 

 [Informational] Numerous emails sent by a single sender to multiple internal recipients 

 [Informational] Object versioning was disabled 

 [Informational] OneDrive file download 

 [Informational] OneDrive file upload 

 [Informational] OneDrive folder creation 

 [Informational] Outbound email contains file-sharing service link sent to external recipient 

 [Informational] Outbound email includes an external BCC recipient observed for the first time 

 [Informational] Outbound email to an address hosted by a public email service provider 

 [Informational] Owner added to Azure application 

 [Informational] Owner was added to Azure application 

 [Informational] PIM privilege member removal 

 [Informational] Potential creation of persistent cloud credentials 

 [Informational] Potential spoofing of internal domain spotted 

 [Informational] Quarantined email released to recipients 

 [Informational] Rarely seen sender address in the organization 

 [Informational] Rarely seen sender domain in the organization 

 [Informational] Remote usage of AWS Lambda's role 

 [Informational] Remote usage of VM Service Account token 

 [Informational] Remote usage of an App engine Service Account token 

 [Informational] Remote usage of an Azure Service Principal token 

 [Informational] Removal of an Azure Owner from an Application or Service Principal 

 [Informational] Retrieval of cloud compute EC2 instance user data 

 [Informational] S3 configuration deletion 

 [Informational] SES Production Access Requested 

 [Informational] SSO with abnormal operating system 

 [Informational] Security tools detection attempt 

 [Informational] Serial console access was enabled in AWS account 

 [Informational] Short-lived Azure AD user account 

 [Informational] Soft delete of cloud storage configuration was disabled 

 [Informational] Storage enumeration activity 

 [Informational] Successful unusual guest user invitation 

 [Informational] Sudden spike in outbound email volume 

 [Informational] Suspicious AWS SSM parameters retrieval activity 

 [Informational] Suspicious DKIM Result 

 [Informational] DKIM results lacking sender correlation - Modified Metadata 

 [Informational] Known domain DKIM deviation - Modified Metadata 

 [Informational] Known domain suspicious DKIM result - Modified Metadata 

 [Informational] Lack DKIM signature from typically signing domains - Modified Metadata 

 [Informational] Suspicious DMARC result 

 [Informational] DMARC deviation from historically compliant domain - Modified Metadata 

 [Informational] DMARC failure bypassed domain policy - Modified Metadata 

 [Informational] Suspicious MFA request reported by user in Entra ID 

 [Informational] Suspicious ML Model Download 

 [Informational] Suspicious SPF Result 

 [Informational] Internal domain SPF deviation - Modified Metadata 

 [Informational] Known domain SPF deviation - Modified Metadata 

 [Informational] Suspicious Unicode character detected in email 

 [Informational] Suspicious access to cloud credential files 

 [Informational] Suspicious activity on logging bucket 

 [Informational] Suspicious brand affiliation detected 

 [Informational] Suspicious cloud compute instance SSH keys modification attempt 

 [Informational] Suspicious process loads a known PowerShell module 

 [Informational] Suspicious secrets dump activity 

 [Informational] Suspicious sender exhibiting automated sending patterns 

 [Informational] Suspicious sending domain with sender address randomization 

 [Informational] System profiling WMI query execution 

 [Informational] Tampering with Internet Explorer Protected Mode configuration 

 [Informational] Uncommon URL domain(s) in your organization detected in email 

 [Informational] Uncommon increase in Azure Microsoft Graph API request sizes 

 [Informational] Uncommon sensitive filesystem registry hive access 

 [Informational] Unrecognized internal address (AAD mismatch) 

 [Informational] Unusual AI model invocation 

 [Informational] Unusual AWS Bedrock model access request 

 [Informational] Unusual AWS CLI/SDK activity 

 [Informational] Unusual AWS S3 objects deletion 

 [Informational] Unusual AWS SageMaker notebook access 

 [Informational] Unusual AWS systems manager activity 

 [Informational] Unusual Conditional Access operation for an identity 

 [Informational] Unusual IAM enumeration activity by a non-user Identity 

 [Informational] Unusual Identity and Access Management (IAM) activity 

 [Informational] Unusual Kubernetes secret access 

 [Informational] Unusual URL(s) sent by a brand were observed in the email 

 [Informational] Unusual access to Microsoft 365 storage services 

 [Informational] Unusual attachment volume in outbound emails 

 [Informational] Unusual certificate management activity 

 [Informational] Unusual cloud Instance Metadata Service (IMDS) access 

 [Informational] Unusual cloud identity impersonation 

 [Informational] Unusual display name in From header 

 [Informational] Unusual exec into a Kubernetes Pod 

 [Informational] Unusual file-sharing links for mailbox owner 

 [Informational] Unusual hostname for the sending mail server in the email headers 

 [Informational] Unusual key management activity 

 [Informational] Unusual multi-region AWS Resource Explorer searches 

 [Informational] Unusual resource access by Azure application 

 [Informational] Unusual resource modification by newly seen IAM user 

 [Informational] Unusual secret management activity 

 [Informational] Unusual sender IP subnet 

 [Informational] Unusual sender IP subnet associated with infrastructure or tunneling services - Modified Metadata 

 [Informational] Unusual sender IP subnet associated with internal sender - Modified Metadata 

 [Informational] Unusual user-agent for a cloud identity 

 [Informational] Unverified domain added to Azure AD 

 [Informational] Usage of homograph characters detected in an email 

 [Informational] Usage of homograph characters detected in an email attachment(s) name 

 [Informational] Usage of homograph characters detected in an email's from header 

 [Informational] User installed an application in Microsoft Teams via Graph API 

 [Informational] User sent messages in Microsoft Teams to multiple conversations via Graph API 

 [Informational] Well-known brand in sender headers with header inconsistencies 

 [Informational] Windows CGO, actor process and action module with anomalous characteristics 

 [Informational] X-Forefront-Antispam-Report has flagged this email as a potential threat 

 [Informational] Email contains an attachment flagged by X-Forefront-Antispam-Report as malware due to its file type - Modified Metadata 

 [Informational] Email flagged by X-Forefront-Antispam-Report as a highly confident phishing attempt - Modified Metadata 

 [Informational] Email flagged by X-Forefront-Antispam-Report as impersonating internal communication - Modified Metadata 

 [Informational] Email identified by X-Forefront-Antispam-Report as a phishing attempt - Modified Metadata 

 [Informational] X-Forefront-Antispam-Report flagged this email as spam - Modified Metadata 

 [Informational] X-Forefront-Antispam-Report has flagged an internal email as spam - Modified Metadata 

 [Informational] X-Forefront-Antispam-Report has flagged this email as a bulk email - Modified Metadata 

 [Informational] X-Forefront-Antispam-Report has flagged this email as attempting to forge the sender's identity - Modified Metadata 

 [Informational] X-Forefront-Antispam-Report has flagged this email as impersonating a specific user within the organization - Modified Metadata 

 [Informational] X-Forefront-Antispam-Report has flagged this email as impersonating a well-known brand - Modified Metadata 

 [Informational] X-Forefront-Antispam-Report has flagged this email as impersonating the organization's domain - Modified Metadata 

 [Informational] X-Forefront-Antispam-Report has flagged this email as using advanced impersonation techniques - Modified Metadata 

 [Informational] X-Forefront-Antispam-Report has strongly flagged this email as spam - Modified Metadata 

 Modified Metadata 

 [Medium -> Low] Microsoft Office Process Spawning a Suspicious One-Liner 

 [Informational] Uncommon signed process execution by scheduled task 

 [Low] Rare signed process execution by scheduled task - Modified Metadata 

 [Low] Uncommon signed process execution by scheduled task on a sensitive server - Modified Metadata 

 [Low -> Informational] Built-in SoundRecorder tool capturing audio 

 [Informational] Port Sweep 

 [Informational] Punycode characters detected in URL(s) 

 [Informational] Suspicious theme and sentiment in email 

 Previous 2026.08.05 

 Next 2026.07.22 

 Was this helpful?

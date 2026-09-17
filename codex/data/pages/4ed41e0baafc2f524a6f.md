---
url: https://docs.prismacloud.io/release-notes/prisma-cloud-release-information/features-introduced-in-2024/features-introduced-in-march-2024
fetched_at: 2026-09-16T13:36:00Z
source: prisma-cloud
---

# Features Introduced in March 2024 | Prisma Cloud arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Enterprise Edition 

 Release Notes 

 Prisma Cloud Release Information 

 Features Introduced in 2024 

 Features Introduced in March 2024 

 Learn what’s new on Prisma® Cloud in March 2024. 

 Announcement 

 New Features 

 API Ingestions 

 New Policies 

 Policy Updates 

 New Compliance Benchmarks and Updates 

 REST API Updates 

 Deprecation Notice 

 Announcement 

 Feature 

 Description 

 Prisma Cloud Darwin Release 

 The Prisma Cloud Darwin Release is now available for Prisma Cloud environments on all stacks. With the Code to Cloud™ intelligence capabilities in this release, your security and development teams can work together to reduce application risks and prevent breaches. 

 With this change, your tenant will be updated with the new intuitive user interface and rich set of security capabilities . Refer to the Enterprise Edition—Darwin documentation. 

 Contact your Prisma Cloud Customer Success team for more details. 

 New Features 

 Feature 

 Description 

 Blobstore Scanning Defender Upgrade for Tanzu Customers 

 Secure the Runtime 

 Enhanced the existing blobstore scanning feature for Tanzu customers. As a part of this enhancement, existing blobstore scanning defenders will now appear disconnected and new defender instances will be automatically created to replace them. The disconnected blobstore will disappear after 24 hours as part of the retention process. This upgrade excludes Linux and Windows defenders (Full coverage defenders). If you have have configured blobstore scanning and assigned it to a specific blobstore defender after the release of 32.04, you are required to manually edit the configurations and change it to a newly created blobstore defender scanner. This release also supports a new tile - jammy for TAS. 

 Added Account ID Information to Defenders Dashboard 

 Secure the Runtime 

 The Account ID information is displayed on the Defenders dashboard under Manage > Defenders . It is also included in the downloadable .csv file. 

 Enhanced Vulnerability Assessment Process 

 Secure the Runtime 

 Prisma Cloud now has an enhanced vulnerability assessment process for applications installed through the OS. If Prisma Cloud cannot detect any vulnerabilities in the vendor feed, it automatically searches for third-party security data to ensure comprehensive security coverage. For a comprehensive list of the detected vulnerabilities, navigate to Monitor > Vulnerabilities > Vulnerability Explorer . 

 Exclude Go CVEs for Windows from the CVEs of UNIX-based Systems 

 Secure the Runtime 

 Prisma Cloud now excludes vulnerabilities found in Go packages that are specific to Windows from UNIX-based operating systems in Vulnerability Explorer . For a comprehensive list of the detected vulnerabilities, navigate to Monitor > Vulnerabilities > Vulnerability Explorer . 

 Cloud Discovery and Exposure Management Enhancements in Prisma Cloud 

 Secure the Infrastructure 

 24.3.2 

 Prisma Cloud includes the following enhancements for Cloud Discovery and Exposure Management (CDEM): 

 Enhanced Subscription Process : Ensure precise scanning of internet-exposed resources by verifying or manually entering your DUNS number and associated Domains while subscribing to CDEM . 

 Asset Snoozing Options : Choose to temporarily or permanently snooze your unmanaged (internet-exposed) assets while inspecting your assets in the Discovery and Exposure Management Dashboard widgets. Snoozing assets provide the flexibility to view your Active assets separately from the Snoozed assets on Inventory > Unmanaged Assets . 

 Download Unmanaged Assets : Download the comprehensive list of Unmanaged Assets filtered by Asset type in .csv format from Inventory > Unmanaged Assets , expanding from previous limitations to current page details. 

 Flow Log Visualization : Explore the new Network Flow Log tab in the side panel while inspecting internet-exposed assets. Visualize traffic flow between internet-exposed (unmanaged) and secure (managed) assets to make informed decisions and take appropriate actions to secure the internet-exposed asset. 

 Onboard Google Workspace 

 Secure the Infrastructure 

 24.3.2 

 Prisma Cloud now supports onboarding of your Google Workspace domains to Prisma Cloud to get security and visibility into your Workspace accounts. After successful onboarding, you can configure alert rules on Workspace related to multi-factor authentication policies and identify Workspace users that have MFA enabled or disabled. 

 Save Widget Configurations as Saved Views 

 Secure the Infrastructure 

 24.3.2 

 Prisma Cloud > Dashboards now offers the option to save your widget configurations as Saved Views . The following caveats apply: 

 Views are no longer limited to a maximum of 20. 

 Saved Views are enabled by default for the persona (Cloud/Runtime/Application Security) you created them in. If you switch to another persona, the view is disabled but you have the option to re-enable it. 

 Create Saved Views to store select widget configurations for a customizable view of your security posture. 

 Alert Notification Delay Support for Push Integration Method 

 Secure the Infrastructure 

 24.3.2 

 The Alert Notification Delay capability is now supported for all external integrations that use the Push integration method. 

 Update Advanced Settings Option in AWS Cloud Account Onboarding 

 Secure the Infrastructure 

 24.3.2 

 While onboarding your AWS Account or Organization to Prisma Cloud, a new Use Tenant Specific External ID (optional) capability is now available under Advanced Settings during account configuration. When you select the Use Tenant Specific External ID checkbox, Prisma Cloud provides a unique auto-generated external ID at the tenant level for that particular AWS account or organization once you Download the CFT . You can use this optional capability both while onboarding a new as well as editing or updating an existing AWS account or organization. 

 Update Policy Subtype Column Included in Downloaded .csv 

 Secure the Infrastructure 

 24.3.2 

 On the Governance page if you filter by Policy Subtype , the column is now also displayed in the resulting .csv file when you select Download policies data > Download detailed view . Previously, the Policy Subtype column was displayed in the downloaded csv only on selecting Download policies data > Download current view . 

 Prisma Cloud Code Security Scanner Extension Available for VS Code 

 Secure the Source 

 24.3.2 

 The Prisma Cloud Code Security scanner extension is now supported in Visual Studio Code , offering convenient access to robust security scanning features directly within your coding environment, that allows you to detect and address security issues, including IaC misconfigurations, SCA vulnerabilities, secrets exposure, and license compliance. You can download the extension from the Visual Studio Code Marketplace or through the IDE extensions feature. 

 API Ingestions 

 Service 

 API Details 

 Amazon SageMaker 

 24.3.2 

 aws-sagemaker-processing-job 

 Additional permissions required: 

 sagemaker:ListProcessingJobs 

 sagemaker:DescribeProcessingJob 

 The Security Audit role includes the permissions. 

 Amazon SageMaker 

 24.3.2 

 aws-sagemaker-code-repository 

 Additional permissions required: 

 sagemaker:ListCodeRepositories 

 sagemaker:DescribeCodeRepository 

 The Security Audit role includes the permissions. 

 AWS Account Management 

 24.3.2 

 aws-account-contact-information 

 Additional permission required: 

 account:GetContactInformation 

 The Security Audit role includes the permission. 

 AWS Backup 

 24.3.2 

 aws-backup-protected-resources 

 Additional permission required: 

 backup:ListProtectedResources 

 You must manually add the above permission to the CFT template to enable it. 

 Amazon EC2 

 24.3.2 

 aws-ec2-vpc-endpoint-connection-notification 

 Additional permission required: 

 ec2:DescribeVpcEndpointConnectionNotifications 

 The Security Audit role includes the permission. 

 AWS Glue 

 24.3.2 

 aws-glue-job 

 Additional permission required: 

 glue:GetJobs 

 The Security Audit role includes the permission. 

 AWS Glue 

 24.3.2 

 aws-glue-schema 

 Additional permissions required: 

 glue:ListSchemas 

 glue:GetSchema 

 You must manually add the above permissions to the CFT template to enable them. 

 AWS Security Hub 

 24.3.2 

 aws-securityhub-hub 

 Additional permission required: 

 securityhub:DescribeHub 

 The Security Audit role includes the permission. 

 Update AWS Trusted Advisor 

 24.3.2 

 aws-trusted-advisor-check-result 

 The API now includes the metadata field which was previously excluded. 

 AWS WAF 

 24.3.2 

 aws-waf-classic-global-ip-set 

 Additional permissions required: 

 waf:ListIPSets 

 waf:GetIPSet 

 The Security Audit role includes the permissions. 

 AWS WAF 

 24.3.2 

 aws-waf-classic-regional-ip-set 

 Additional permissions required: 

 waf-regional:ListIPSets 

 waf-regional:GetIPSet 

 The Security Audit role includes the permissions. 

 AWS WAF 

 24.3.2 

 aws-waf-v2-regional-ip-set 

 Additional permissions required: 

 wafv2:ListIPSets 

 wafv2:GetIPSet 

 The Security Audit role includes the wafv2:ListIPSets permission. 

 AWS WAF 

 24.3.2 

 aws-waf-v2-global-ip-set 

 Additional permissions required: 

 wafv2:ListIPSets 

 wafv2:GetIPSet 

 The Security Audit role includes the wafv2:ListIPSets permission. 

 Azure Logic Apps 

 24.3.2 

 azure-logic-app-workflow-versions 

 Additional permissions required: 

 Microsoft.Logic/workflows/read 

 Microsoft.Logic/workflows/versions/read 

 The Reader role includes the permissions. 

 Azure Database for MariaDB Server 

 24.3.2 

 azure-database-maria-db-server-firewall-rules 

 Additional permissions required: 

 Microsoft.DBforMariaDB/servers/read 

 Microsoft.DBforMariaDB/servers/firewallRules/read 

 The Reader role includes the permissions. 

 Azure Defender for Cloud 

 24.3.2 

 azure-defender-for-cloud-jit-network-access-policies 

 Additional permission required: 

 Microsoft.Security/locations/jitNetworkAccessPolicies/read 

 The Reader role includes the permission. 

 Azure Cognitive Services 

 24.3.2 

 azure-cognitive-search-service 

 Additional permission required: 

 Microsoft.Search/searchServices/read 

 The Reader role includes the permission. 

 Azure Recovery Services 

 24.3.2 

 azure-recovery-service-vault-backup-policies 

 Additional permissions required: 

 Microsoft.RecoveryServices/Vaults/read 

 Microsoft.RecoveryServices/vaults/backupPolicies/read 

 The Reader role includes the permissions. 

 Update Azure Compute 

 24.3.2 

 azure-vm-list 

 The API is updated to include the properties.osProfile.linuxConfiguration.patchSettings.patchMode field in the JSON resource configuration. As part of this change, the properties.osProfile.linuxConfiguration.patchSettings.patchMode key is now available in RQL auto-completion. 

 Update Google Vertex AI 

 24.3.2 

 gcloud-vertex-ai-notebook-instance 

 Prisma Cloud has updated the gcloud-vertex-ai-notebook-instance API to exclude the gcs_backup_sync_last_updated field from the resource configuration because it changes frequently causing too many resource snapshots. 

 Update Google Vertex AI 

 24.3.2 

 Prisma Cloud no longer requires access to the notebooks.locations.list permission to scan and monitor gcloud-vertex-ai-notebook-environment and gcloud-vertex-ai-notebook-instance APIs. 

 New Policies 

 Policies 

 Description 

 AWS RDS database instance not configured with encryption in transit 

 24.3.2 

 Identifies AWS RDS database instances that are not configured with encryption in transit. This covers MySQL, SQL Server, PostgreSQL, MariaDB, and DB2 RDS instances. Enabling encryption is crucial to protect data as it moves through the network and enhances the security between clients and storage servers. Without encryption, sensitive data transmitted between your application and the database is vulnerable to interception by malicious actors. This could lead to unauthorized access, data breaches, and potential compromises of confidential information. It is recommended that data be encrypted while in transit to ensure its security and reduce the risk of unauthorized access or data breaches. 

 Policy Severity— Low 

 Policy Type— Config 

 AWS Cognito service role does not have identity pool verification 

 24.3.2 

 Identifies the AWS Cognito service role that does not have identity pool verification. AWS Cognito is an identity and access management service for web and mobile apps. AWS Cognito service roles define permissions for AWS services accessing resources. The 'aud' claim in a cognito service role is an identity pool token that specifies the intended audience for the token. If the aud claim is not enforced in the cognito service role trust policy, it could potentially allow tokens issued for one audience to be used to access resources intended for a different audience. This oversight increases the risk of unauthorized access, compromising access controls and elevating the potential for data breaches within the AWS environment. It is recommended to implement proper validation of the 'aud' claim by adding the 'aud' in the Cognito service role trust policy. 

 Policy Severity— Low 

 Policy Type— Config 

 AWS Cognito service role with wide privileges does not validate authentication 

 24.3.2 

 Identifies the AWS Cognito service role that has wide privileges and does not validate user authentication. AWS Cognito is an identity and access management service for web and mobile apps. AWS Cognito service roles define permissions for AWS services accessing resources. The 'amr' field in the service role represents how the user was authenticated. if the user was authenticated using any of the supported providers, the 'amr' will contain 'authenticated' and the name of the provider. Not validating the 'amr' field can allow an unauthenticated user (guest access) with a valid token signed by the identity-pool to assume the Cognito role. If this Cognito role has a ' ' wildcard in the action and resource, it could lead to lateral movement or unauthorized access. Ensuring limiting privileges according to business requirements can help in restricting unauthorized access and misuse of resources. It is recommended to limit the Cognito service role used for guest access to not have a ' ' wildcard in the action or resource. 

 Policy Severity— Low 

 Policy Type— Config 

 AWS Redshift cluster with a commonly used master username and public access setting enabled 

 24.3.2 

 Identifies AWS Redshift clusters configured with commonly used master usernames like 'awsuser', 'administrator', or 'admin', and the public access setting is enabled. AWS Redshift, a managed data warehousing service typically stores sensitive and critical data. Allowing public access increases the risk of unauthorized access, data breaches, and potential malicious activities. Using standard usernames increases the risk of password brute-force attacks by potential intruders. As a recommended security measure, it is advised not to use commonly used usernames and to disable public access for the Redshift cluster. 

 Policy Severity— Informational 

 Policy Type— Config 

 AWS Redshift cluster is configured with public accessibility 

 24.3.2 

 Identifies AWS Redshift clusters with the publicly accessible setting set to true. When Amazon Redshift clusters are made public, the likelihood of malicious activity increases, such as unauthorized access or Distributed Denial of Service (DDoS) attacks. As a security best practice, the public accessibility parameter of the Redshift cluster should be turned off. 

 Policy Severity— Low 

 Policy Type— Config 

 AWS CloudTrail S3 bucket encrypted with Customer Managed Key (CMK) that is scheduled for deletion 

 24.3.2 

 Identifies AWS CloudTrail S3 buckets encrypted with Customer Managed Key (CMK) that is scheduled for deletion. CloudTrail logs contain account activity related to actions across your AWS infrastructure. These log files stored in Amazon S3 are encrypted by AWS KMS keys. Deleting keys in AWS KMS that are used by CloudTrail is a common defense evasion technique and could be a potential ransomware attacker activity. After a key is deleted, you can no longer decrypt the data that was encrypted under that key, which helps the attacker to hide their malicious activities. It is recommended to regularly monitor the key used for encryption to prevent accidental deletion. 

 Policy Severity— High 

 Policy Type— Config 

 AWS SNS Topic not encrypted by Customer Managed Key (CMK) 

 24.3.2 

 Identifies AWS SNS Topics that are not encrypted by Customer Managed Key (CMK). AWS SNS Topics are used to send notifications to subscribers and might contain sensitive information. SNS Topics are encrypted by default by a AWS managed key but users can specify CMK to get enhanced security, control over the encryption key and also comply with any regulatory requirements. As a security best practice use of CMK to encrypt your SNS Topics is advisable as it gives you full control over the encrypted data. 

 Policy Severity— Low 

 Policy Type— Config 

 AWS Default VPC is being used 

 24.3.2 

 Identifies AWS Default VPCs that are being used. AWS creates a default VPC automatically upon the creation of your AWS account with a default security group and network access control list (NACL). Using AWS default VPC can lead to limited customization and security concerns due to shared resources and potential misconfigurations, hindering scalability and optimal resource management. As a best practice, using a custom VPC with specific security and network configuration provides greater flexibility and control over your architecture. 

 Policy Severity— Informational 

 Policy Type— Config 

 AWS EKS cluster does not have secrets encryption enabled 

 24.3.2 

 Identifies AWS EKS clusters that do not have secrets encryption enabled. AWS EKS cluster secrets are, by default, stored unencrypted in the API server’s underlying data store (etcd). Anyone with direct access to etcd or with API access can retrieve or modify the secrets. Using secrets encryption for your Amazon EKS cluster allows you to protect sensitive information such as passwords and API keys using Kubernetes-native APIs. It is recommended to enable secret encryption to ensure its security and reduce the risk of unauthorized access or data breaches. 

 Policy Severity— Low 

 Policy Type— Config 

 AWS Elastic Load Balancer v2 (ELBv2) with cross-zone load balancing disabled 

 24.3.2 

 Identifies load balancers that do not have cross-zone load balancing enabled. Cross-zone load balancing is a feature that evenly distributes incoming traffic across healthy targets in all availability zones that have been configured. This can help to ensure that your application is able to manage additional traffic and limit the danger of any single availability zone getting overwhelmed and perhaps affecting load balancer performance. So, it is recommended to enable cross-zone load balancing. 

 Policy Severity— Informational 

 Policy Type— Config 

 AWS MSK cluster encryption in transit is not enabled 

 24.3.2 

 Identifies AWS MSK clusters with encryption in transit in a disabled state. Without in-transit encryption, data can be intercepted when moving between brokers. So it is recommended to enable in-transit encryption between brokers within a cluster to ensure that data exchanged between brokers within the cluster is encrypted, thereby protecting sensitive data from eavesdropping and unauthorized access. 

 Policy Severity— Low 

 Policy Type— Config 

 AWS RDS Postgres Cluster does not have Query Logging enabled 

 24.3.2 

 Identifies RDS Postgres clusters with query logging disabled. In AWS RDS PostgreSQL, by default, the logging level captures login failures, fatal server errors, deadlocks, and query failures. To log data changes, we recommend enabling cluster logging for monitoring and troubleshooting. To obtain adequate logs, an RDS cluster should have log_statement and log_min_duration_statement parameters configured. It is a best practice to enable additional RDS cluster logging, which will help in data change monitoring and troubleshooting. 

 Policy Severity— Informational 

 Policy Type— Config 

 GCP Composer environment web server network access control allows access from all IP addresses 

 24.3.2 

 Identifies GCP Composer environments with web server network access control that allows access from all IP addresses. Web server network access controls which IP addresses will have access to the Airflow web server. By default, this feature allows all connections from the public internet. Allowing all traffic to the composer environment may allow a bad actor to brute force their way into the system and potentially get access to the entire network. As a best practice, restrict traffic solely from known static IP addresses. Limit the access list to include known hosts, services, or specific employees only. 

 Policy Severity— Low 

 Policy Type— Config 

 GCP Cloud Run service is using default service account with editor role 

 24.3.2 

 Identifies GCP Cloud Run services that are utilizing the default service account with the editor role. In Google Cloud Platform (GCP), the Compute Engine Default service account is automatically created upon enabling the Compute Engine API. This service account is granted the IAM basic Editor role by default, unless explicitly disabled. To adhere to the principle of least privilege and mitigate potential privilege escalation risks, it is recommended not to assign the default service account, particularly when granting the editor role. This ensures that instances are provisioned with minimal access rights, promoting a better security posture. 

 Policy Severity— Medium 

 Policy Type— Config 

 GCP GKE cluster node boot disk not encrypted with CMEK 

 24.3.2 

 Identifies GCP GKE clusters that do not have their node boot disk encrypted with CMEK. The GKE node boot disk is the persistent disk that houses the Kubernetes node file system. By default, this disk is encrypted by a GCP managed key but users can specify customer managed encryption key to get enhanced security, control over the encryption key, and also comply with any regulatory requirements. As a security best practice use of CMEK to encrypt the boot disk of GKE cluster nodes is advisable. 

 Policy Severity— Low 

 Policy Type— Config 

 GCP SQL Instance with public IP address does not have authorized network configured 

 24.3.2 

 Identifies GCP Cloud SQL instances with public IP addresses that do not have authorized network configured. Clients can connect to the SQL instance securely by using the Cloud SQL Proxy or adding the client’s public address as an authorized network. If the client application is connecting directly to a Cloud SQL instance on its public IP address, client’s external IP address needs to be added as an Authorized network to allow the connection. It is recommended to add authorized networks to reduce the access vector. 

 Policy Severity— Medium 

 Policy Type— Config 

 GCP Dataproc Cluster not configured with Customer-Managed Encryption Key (CMEK) 

 24.3.2 

 Identifies Dataproc Clusters that are not configured with CMEK. Dataproc cluster and job data are stored on persistent disks associated with the Compute Engine VMs in the cluster as well as in a Cloud Storage staging bucket. As a security best practice use of CMEK to encrypt this data on persistent disk and bucket is advisable and provides more control to the user. 

 Policy Severity— Low 

 Policy Type— Config 

 GCP PostgreSQL instance database flag cloudsql.enable_pgaudit is not set to on 

 24.3.2 

 Identifies PostgreSQL database instances in which database flag cloudsql.enable_pgaudit is not set to on. Enabling the flag cloudsql.enable_pgaudit enables the logging by pgAudit extension for the database (if installed). The pgAudit extension for PostgreSQL databases provides detailed session and object logging to comply with government, financial, & ISO standards and provides auditing capabilities to mitigate threats by monitoring security events on the instance. Any changes to the database logging configuration should be made in accordance with the organization’s logging policy. 

 Policy Severity— Informational 

 Policy Type— Config 

 GCP PostgreSQL instance database flag log_min_error_statement is not set 

 24.3.2 

 Identifies PostgreSQL database instances in which database flag log_min_error_statement is not set. The log_min_error_statement flag defines the minimum message severity level that are considered as an error statement. Messages for error statements are logged with the SQL statement. Valid values include DEBUG5, DEBUG4, DEBUG3, DEBUG2, DEBUG1, INFO, NOTICE, WARNING, ERROR, LOG, FATAL, and PANIC. Each severity level includes the subsequent levels. log_min_error_statement flag value changes should only be made in accordance with the organization’s logging policy. Proper auditing can help in troubleshooting operational problems and also permits forensic analysis. 

 Policy Severity— Informational 

 Policy Type— Config 

 GCP Vertex AI Workbench user-managed notebook is using a default service account with the editor role 

 24.3.2 

 Identifies GCP Vertex AI Workbench user-managed notebooks that are using the default service account with the editor role. When you create a new Vertex AI Workbench user-managed notebook, the compute engine default service account is associated with the notebook by default if any other service account is not configured. The compute engine default service account is automatically created when the Compute Engine API is enabled and is granted the IAM basic Editor role if you have not disabled this behavior explicitly. These permissions can be exploited to get admin access to the GCP project. To be compliant with the principle of least privileges and prevent potential privilege escalation, it is recommended that Vertex AI Workbench user-managed notebooks are not assigned the 'Compute Engine default service account' especially when the editor role is granted to the service account. 

 Policy Severity— Medium 

 Policy Type— Config 

 New CI/CD Configuration Build Policies 

 24.3.2 

 The following default CI/CD policies are added within the Build subtype of Configuration policies under Governance for enhanced continuous integration and deployment pipeline security: 

 Azure Policies 

 Repository in Azure Repos does not dismiss pull request approvals on the default branch when new commits are pushed 

 NPM project contains unused dependencies in an Azure Repos repository 

 NPM package downloaded from git without commit hash reference in an Azure Repos repository 

 GitHub Policies 

 NPM project contains unused dependencies in a GitHub repository 

 NPM package downloaded from git without commit hash reference in a GitHub repository 

 GitLab Policies 

 NPM project contains unused dependencies in a GitLab repository 

 NPM package downloaded from git without commit hash reference in a GitLab repository 

 Policy Updates 

 Policy Updates 

 Description 

 Policy Updates—RQL 

 Update Azure Microsoft Defender for Cloud set to Off for DNS 

 24.3.2 

 Changes— The Policy description and RQL have been updated to check either of the config i.e, Azure Microsoft Defender for servers plan 2 (which includes DNS) has not been enabled or Azure Microsoft Classic Defender for Cloud which has defender setting for DNS set to Off. 

 Severity— Informational 

 Policy Type— Config 

 Current Policy Description— Identifies Azure Microsoft Defender for Cloud which has defender setting for DNS set to Off. Enabling Azure Defender provides advanced security capabilities like providing threat intelligence, anomaly detection, and behavior analytics in the Azure Microsoft Defender for Cloud. Defender for DNS monitors the queries and detects suspicious activities without the need for any additional agents on your resources. It is highly recommended to enable Azure Defender for DNS. 

 Updated Policy Description— Identifies Azure Microsoft Defender for Cloud which has a defender setting for DNS set to Off. Enabling Azure Defender for the cloud provides advanced security capabilities like threat intelligence, anomaly detection, and behavior analytics. Defender for DNS monitors the queries and detects suspicious activities without the need for any additional agents on your resources. It is highly recommended to enable Azure Defender for DNS. 

 Current RQL— 

 Updated RQL— 

 Impact— Low. New Alerts might be generated in case the Azure Microsoft Defender for servers plan 2 is not enabled or Azure Microsoft Defender for Cloud which has defender setting for DNS set to Off. Existing alerts might get resolved in case Azure Microsoft Classic Defender for servers plan 2 is enabled. 

 Update AWS SQS queue access policy is overly permissive 

 24.3.2 

 Changes— The policy RQL has been updated to consider Action: SQS* as the IAM action and prefix are case-insensitive. 

 Severity— Informational 

 Policy Type— Config 

 Current RQL— 

 Updated RQL— 

 Impact— Low. New Alerts might be generated in case the IAM action starts with SQS* 

 Update GCP Storage buckets are publicly accessible to all users 

 24.3.2 

 Changes— Policy RQL has been updated to account for bucket level prevent public access feature. The recommendation is also updated as per the updated GCP UI. 

 Severity— High 

 Policy Type— Config 

 Current RQL— 

 Updated RQL— 

 Impact— Low. Existing alerts on buckets with the prevent public access feature enabled at the bucket level will be resolved. Alerts will be generated against the policy violations. 

 New Compliance Benchmarks and Updates 

 Compliance Benchmark 

 Description 

 Support for Telecommunications Security Act (TSA) 

 24.3.2 

 Prisma Cloud now supports the Telecommunications Security Act - TSA compliance standard. This framework encompasses measures to ensure the security and integrity of telecommunications networks and data. It includes provisions for network security, data protection, encryption, access controls, and various other categories. 

 You can view this built-in standard and the associated policies from Compliance > Standards . You can also generate reports for immediate viewing or download, and schedule recurring reports to track this compliance standard over time. 

 Support for HITrust CSF 11.2.0 

 24.3.2 

 Prisma Cloud now supports the HITrust CSF 11.2.0 compliance standard. This compliance standard includes all the requirements and controls provided by HITrust CSF and Prisma Cloud policies mapped. 

 You can view this built-in standard and the associated policies from Compliance > Standards . You can also generate reports for immediate viewing or download, and schedule recurring reports to track this compliance standard over time. 

 Policy mappings update for NIST 800-53 Revision 5 

 24.3.2 

 The compliance requirements in NIST 800-53 Revision 5 compliance standard are updated with new mappings. 

 Impact- As new mappings are introduced, compliance scoring might vary. 

 REST API Updates 

 Change 

 Description 

 Report Vulnerabilities Using Package URL (purl) Format 

 Secure the Runtime 

 The following API responses include a new purl parameter: 

 Get Image Scan Results 

 Get Registry Scan Results 

 Get All CI Image Scan Results 

 Get Host Scan Results 

 Get VM Image Scan Results 

 Get All CI Image Scan Results 

 The purl field identifies the absolute path for the packages. 

 API to Send Console Logs to Remote Syslog 

 Secure the Runtime 

 The Add Logging Settings API includes a new cert parameter under Syslog to configure a TLS certificate. 

 Asset Explorer APIs 

 Secure the Infrastructure 

 24.3.2 

 The Get Asset - POST /uai/v1/asset endpoint now includes an array of IP addresses in the response. 

 AWS Cloud Account APIs 

 Secure the Infrastructure 

 24.3.2 

 The following parameters are added to Add Cloud Account (AWS) , Update Cloud Account (AWS) , and Get Cloud Account Status (AWS) : 

 customMemberRoleNameEnabled 

 skipOverrideMemberRoleName 

 unifiedCftDisabled 

 memberRoleName 

 useTenantExternalId 

 CDEM APIs 

 Secure the Infrastructure 

 24.3.2 

 The following CDEM endpoints are available to snooze, unsnooze, download your unmanaged assets, and get the traffic flow logs: 

 Snooze Unmanaged Assets - POST /asm/api/v1/asset/snooze 

 Unsnooze Unmanaged Assets - POST /asm/api/v1/asset/reopen 

 Download Unmanaged Assets - POST /asm/api/v1/asset/download 

 Get Flow Logs of Unmanaged Assets - GET /asm/api/v1/asset/{assetId}/flowlog-relationships 

 GCP Cloud Account APIs 

 Secure the Infrastructure 

 24.3.2 

 The following endpoints now support Google Workspace account type to onboard and update the onboarded Google Workspace account to Prisma Cloud: 

 Add Cloud Account (GCP) 

 Update Cloud Account (GCP) 

 Get Cloud Account Status (GCP) 

 IAM APIs 

 Secure the Infrastructure 

 24.3.2 

 A new Get Permissions V4 - POST /iam/api/v4/search/permission endpoint is now available to get the permissions grouped by certain fields. 

 Widgets APIs 

 Secure the Infrastructure 

 24.3.2 

 The following Widget API endpoints are now accessible to roles with the Alerts_READ permission: 

 /api/v1/metrics/alert-count-by-resolution-reason 

 /api/v1/metrics/alert-mean-resolution-time 

 Deprecation Notice 

 Change 

 Description 

 Redundant V1 Errors Endpoints in Application Security 

 24.3.2 

 The following v1 errors endpoints in Application Security for which v2 endpoints were released previously are now deprecated: 

 List All Errors in File Path 

 Lists Files with Errors 

 You must use the following APIs released previously that provide the same functionality: 

 Get Code Issues from Periodic Scans 

 Get Code Issues from Pull Requests Scans and CICD Runs 

 Previous Features Introduced in April 2024 

 Next Features Introduced in February 2024 

 Last updated 2 months ago 

 Was this helpful?

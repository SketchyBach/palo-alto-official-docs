---
url: https://docs.prismacloud.io/release-notes/prisma-cloud-release-information/classic-releases/prisma-cloud-cspm-release-information/features-introduced-in-september-2023
fetched_at: 2026-09-16T13:36:04Z
source: prisma-cloud
---

# Features Introduced in September 2023 | Prisma Cloud arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Enterprise Edition 

 Release Notes 

 Prisma Cloud Release Information 

 Classic Releases 

 Prisma Cloud Platform Release Information 

 Features Introduced in September 2023 

 Learn what’s new on Prisma® Cloud in September 2023. 

 New Features Introduced in 23.9.2 

 New Features Introduced in 23.9.1 

 New Features Introduced in 23.9.2 

 New Features 

 API Ingestions 

 New Policies 

 Policy Updates 

 IAM Policy Updates 

 Changes in Existing Behavior 

 REST API Updates 

 New Features 

 FEATURE 

 DESCRIPTION 

 Credit Consumption Visualization 

 On Aug 1, 2023, Prisma Cloud Enterprise Edition introduced reductions to the credit required for several modules. When this change was rolled out, the data pertaining to historical credit usage (prior to Aug 1st, 2023) was normalized to the new model and the visualization was updated on the licensing page of the Prisma Cloud console. As a result , you could not see a decrease in credit consumption for resources that are no longer billed. 

 Now, in the 23.9.2 release, we no longer normalize credit data consumed prior to Aug 1st, 2023. This update enables you to accurately track your credit consumption trend using historical data before Aug 1, 2023 and the new usage after Aug 1, 2023. 

 API Ingestions 

 SERVICE 

 API DETAILS 

 AWS Backup 

 aws-backup-backup-plan 

 Additional permissions required: 

 backup:ListBackupPlans 

 backup:GetBackupPlan 

 backup:ListTags 

 You must manually add or update the CFT template to enable the permissions. 

 AWS Glue 

 aws-glue-crawler 

 Additional permissions required: 

 glue:GetCrawler 

 glue:ListCrawlers 

 The Security Audit role only includes glue:GetCrawler . 

 You must manually add or update the CFT template to enable glue:ListCrawlers permission. 

 AWS Trusted Advisor 

 aws-trusted-advisor-check-result 

 Additional permissions required: 

 support:DescribeTrustedAdvisorChecks 

 support:DescribeTrustedAdvisorCheckResult 

 The Security Audit role includes the permissions. 

 Update Azure Container Registry 

 azure-container-registry 

 The resource JSON for this API has been updated to include the properties.policies.exportPolicy.status field. The field identifies the export policy for a container registry. 

 Update Azure SQL Database 

 azure-sql-managed-instance 

 The resource JSON for this API has been updated to include the properties.azureADOnlyAuthentication field. The field identifies if Azure Active Directory only authentication is enabled. 

 Update Azure Storage 

 azure-storage-account-list 

 Prisma Cloud now supports soft delete setting for azure-storage-account-list . The resource JSON for this API has been updated to include the following fields. 

 shareDeleteRetentionPolicy.file 

 shareDeleteRetentionPolicy.file.days 

 shareDeleteRetentionPolicy.file.enabled 

 Update Azure Security Center 

 azure-security-center-settings 

 The resource JSON for this API has been updated to include pricings[\].properties.subPlan field. The field enables a set of security features for a given resource. 

 Google Cloud DNS 

 gcloud-dns-response-policy-rule 

 Additional permissions required: 

 dns.responsePolicies.list 

 dns.responsePolicyRules.list 

 The Viewer role includes the permissions. 

 Google Cloud Filestore 

 gcloud-filestore-instance-snapshot 

 Additional permissions required: 

 file.instances.list 

 file.snapshots.list 

 The Viewer role includes the permissions. 

 Google Cloud Filestore 

 gcloud-filestore-instance-backup 

 Additional permission required: 

 file.backups.list 

 The Viewer role includes the permission. 

 Google Cloud Run 

 gcloud-cloud-run-job 

 Additional permissions required: 

 run.jobs.list 

 run.services.list 

 run.jobs.getIamPolicy 

 The Viewer role includes the permissions. 

 New Policies 

 NEW POLICIES 

 DESCRIPTION 

 Azure Policies 

 Prisma Cloud has included the following new policies: 

 Azure Cache for Redis not configured with data in transit encryption 

 Azure Database for MariaDB not configured with private endpoint 

 Azure Database for MySQL server not configured with private endpoint 

 Azure PostgreSQL servers not configured with private endpoint 

 Azure SQL Database server not configured with private endpoint 

 Policy Severity— Medium 

 Policy Type— Config 

 GCP backend bucket having dangling GCP Storage bucket 

 Identifies the GCP backend buckets having dangling GCP Storage bucket. 

 A GCP backend bucket is usually used by GCP Load Balancers for serving static content. Such setups can also have DNS pointing to the load balancer’s IP for easy human access. A GCP backend bucket pointing to a GCP storage bucket that doesn’t exist in the same project is a potential risk of bucket takeover as well as at risk of subdomain takeover. An attacker can exploit such a setup by creating a GCP Storage bucket with the same name in their own GCP project, thus receiving all requests redirected to this backend bucket from the load balancer to an attacker-controlled GCP Storage bucket. This attacker-controlled bucket can be used to serve malicious content to perform phishing attacks, spread malware, or engage in other illegal activities. 

 As a best practice, it is recommended to review and protect GCP storage buckets bound to a GCP backend bucket from accidental deletion. Delete the GCP backend bucket if it points to a non-existent GCP storage bucket. 

 Policy Severity— Medium 

 Policy Type— Config 

 Policy Updates 

 POLICY UPDATES 

 DESCRIPTION 

 Policy Updates—RQL 

 AWS S3 bucket accessible to unmonitored cloud accounts 

 Changes— The policy RQL has been updated to exclude reporting for the awslogsdelivery account which is used by CloudFront to save logs to the S3 bucket. 

 Severity— Low 

 Policy Type— Config 

 Current RQL— 

 Updated RQL— 

 Impact— Low. Existing alerts will be resolved. 

 GCP VPC Network subnets have Private Google access disabled 

 Changes— The policy RQL has been updated to exclude proxy-only subnet as private google access cannot be configured on proxy-only subnets. 

 Severity— Low 

 Policy Type— Config 

 Current RQL— 

 Updated RQL— 

 Impact— Low. Any alert triggered for Proxy-only subnet will be resolved. 

 Policy Updates—Metadata 

 Azure App Services Remote debugging is enabled 

 Changes— The policy now supports remediation. You can resolve the alerts by running the remediation. 

 Severity— Medium 

 Policy Type— Config 

 Impact— No impact since support for remediation is introduced. 

 Azure Cosmos DB key based authentication is enabled 

 Changes— The policy now supports remediation. You can resolve the alerts by running the remediation. 

 Severity— Low 

 Policy Type— Config 

 Impact— No impact since support for remediation is introduced. 

 Policy Deletions 

 Azure Policies 

 The following Azure policies were enabled by default and have been deleted from Prisma Cloud. However, these policies are added again in the disabled state by default with a new policy name. See New Policies for more details. 

 Azure Cache for Redis not configured with data in-transit encryption 

 Azure Database for MariaDB not configured private endpoint 

 Azure Database for MySQL server not configured private endpoint 

 Azure PostgreSQL servers not configured private endpoint 

 Azure SQL Database server not configured private endpoint 

 Severity— Medium 

 Policy Type— Config 

 Impact— Low. Previously generated alerts will be resolved as Policy_Deleted . 

 Attack Path Policies 

 The following policies have been deleted from Prisma Cloud: 

 Potentially unauthorized port scanning activity detected on a publicly exposed AWS EC2 instance 

 Potentially unauthorized port scanning activity detected on a publicly exposed and vulnerable Azure Virtual Machine 

 Potentially unauthorized port scanning activity detected on a publicly exposed and vulnerable GCP VM instance 

 Policy Type— Attack Path 

 Impact— High. Previously generated alerts will be resolved as Policy_Deleted . 

 IAM Policy Updates 

 The following IAM out-of-the-box (OOTB) policies have been updated in Prisma Cloud: 

 POLICY NAME 

 DESCRIPTION 

 RQL 

 CLOUD TYPE 

 SEVERITY 

 EC2 with IAM role attached has iam:PassRole and ec2:Run Instances permissions 

 This IAM policy enforces controlled access by permitting only the specified actions (iam:PassRole, ec2:RunInstances) within AWS, specifically for 'instance' resources. By limiting the scope of permissions to this focused context, potential risks and unauthorized activity are mitigated. 

 AWS 

 Low 

 AWS role having iam:PassRole and lambda:InvokeFunction permissions attached to EC2 instance 

 This IAM policy is meticulously designed to address potential vulnerabilities arising from an AWS EC2 instance with specific permissions. The 'iam:PassRole' action, coupled with 'lambda:CreateFunction' and 'lambda:InvokeFunction', holds the potential for adversaries to exploit and escalate privileges. By strategically controlling access to these actions within the 'ec2' service, this policy effectively mitigates the risk of unauthorized creation and manipulation of Lambda functions, safeguarding against potential escalation of privileges and maintaining the integrity of your system. 

 AWS 

 Low 

 AWS IAM policy allows access and decrypt Secrets Manager Secrets permissions 

 This IAM policy tackles potential vulnerabilities linked to an AWS EC2 instance equipped with an IAM role that confers access to the 'secretsmanager:GetSecretValue' and 'kms:Decrypt' actions. By closely managing permissions within the 'ec2' service, this policy guards against unauthorized retrieval of sensitive secrets from Secrets Manager and unauthorized decryption of encrypted data through AWS Key Management Service (KMS). This strategic control ensures the safeguarding of system confidentiality and integrity, mitigating risks associated with potential unauthorized access or compromise. 

 AWS 

 Low 

 AWS EC2 with IAM role with destruction permissions for Amazon RDS databases 

 This IAM policy addresses the potential risks associated with an AWS EC2 instance having an IAM role enabling the execution of SQL statements directly on Amazon RDS databases. By meticulously controlling access to the 'rds-data:ExecuteStatement' and 'rds-data:BatchExecuteStatement' actions within the 'ec2' service, this policy mitigates the possibility of data breaches, unauthorized modifications, and access to sensitive information stored in the databases, ensuring a robust security posture for your cloud environment. 

 AWS 

 Low 

 AWS EC2 machine with write access permission to resource-based policies 

 This IAM policy identifies ec2 instance with permissions contol resource based policies for different AWS services. They enable setting policies and permissions for repositories, applications, backup vaults, file systems, data stores, and more. While these permissions offer operational flexibility, it is crucial to use them responsibly. Mishandling these permissions may result in unauthorized access, misconfigurations, or data exposure. It is recommended to assign and manage these permissions to trusted individuals to maintain security posture for AWS resources. 

 AWS 

 Medium 

 AWS EC2 IAM role with Elastic IP Hijacking permissions 

 This precision-crafted IAM policy provides vigilant control over essential actions within AWS, specifically targeting 'instance' resources. By meticulously governing access to actions like 'ec2:DisassociateAddress' and 'ec2:EnableAddressTransfer', this policy serves as a bulwark against unauthorized endeavors to transfer Elastic IPs to unauthorized accounts, bolstering the security of your cloud environment. 

 AWS 

 Medium 

 AWS EC2 with IAM role attached has credentials exposure permissions 

 This meticulously tailored IAM policy enforces precise control over vital actions within AWS, specifically honing in on EC2 'instance' resources. By meticulously governing access to a comprehensive range of actions, this policy provides a robust defense mechanism against unauthorized activities, thereby enhancing the overall security posture of your AWS environment 

 AWS 

 Low 

 AWS EC2 with IAM role with alter critical configuration for s3 permissions 

 This IAM policy instates precise oversight over essential operations within AWS, with a specific focus on 'instance' resources. By thoughtfully managing the capability to influence s3 bucket attributes, such as configuring retention, lifecycle, policy, and versioning settings, this policy plays a crucial role in averting potential hazards. It ensures that unauthorized modifications, which could lead to public exposure or data loss, are effectively mitigated, contributing to the overall resilience of your cloud environment. 

 AWS 

 Low 

 AWS Lambda with IAM role attached has credentials exposure permissions 

 This IAM policy serves as an impenetrable shield for your AWS Lambda resources. It empowers your Lambda functions to wield powerful capabilities, seamlessly orchestrating tasks such as secure communication, user authentication, and data protection. This policy acts as a sentinel, guarding against potential attempts to acquire sensitive login tokens, thus ensuring the sanctity of your critical services. With its astute vigilance, your Lambda environment remains impervious to unauthorized access and unwarranted data exposure, bolstering the robustness and integrity of your cloud ecosystem 

 AWS 

 Medium 

 Azure VM instance with risky Storage account permissions 

 This IAM policy bolsters protection for Azure VM instances by meticulously controlling access to critical actions related to storage accounts, including management of keys, regeneration, and deletion. By imposing stringent access controls within the 'Microsoft.Compute' service, potential risks associated with risky storage account permissions are effectively mitigated. 

 Azure 

 Low 

 GCP VM instance with permissions to disrupt logging 

 This IAM policy exerts meticulous control over crucial actions associated with Google Cloud’s 'compute' service, focusing on 'Instances' resources. By thoughtfully overseeing capabilities such as managing logging metrics, buckets, logs, and sinks, this policy effectively bolsters the integrity of your cloud environment. By mitigating the potential for unauthorized alterations, this policy thwarts attempts to evade proper event logging during lateral movement, reinforcing the overall security of your GCP infrastructure 

 GCP 

 Medium 

 GCP Cloud Function with permissions to disrupt logging 

 This IAM policy maintains vigilant control over pivotal operations within Google Cloud’s 'cloudfunctions' service, with a specific focus on ensuring the integrity of event logging. By thoughtfully governing the management of logging metrics, buckets, logs, and sinks within the 'logging' service, this policy serves as a robust safeguard against unauthorized alterations. This fortified control mitigates the potential for unauthorized manipulations, thereby thwarting any attempts to evade proper event logging during lateral movement. The policy contributes to a resilient and secure GCP environment. 

 GCP 

 Medium 

 GCP VM instance with permissions over Deployments Manager 

 This IAM policy empowers stringent oversight over pivotal functions within Google Cloud’s 'compute' service, exclusively targeting 'Instances' resources. It effectively governs the critical actions involved in managing deployments through Deployment Manager, ensuring a robust defense against unauthorized alterations. By orchestrating deploymentmanager.deployments.create and deploymentmanager.deployments.update capabilities, this policy enforces meticulous control over resource creation and updates, guarding against potential internet exposure, privilege escalation, or lateral movements. This heightened control fortifies the security of your GCP VM instances with heightened vigilance over Deployment Manager functionalities. 

 GCP 

 Medium 

 GCP Cloud Function with permissions over Deployments Manager 

 This IAM policy for GCP’s 'cloudfunctions' service orchestrates vigilant control over the potent capabilities tied to Deployment Manager. With a keen focus on deploying and updating resources, this policy reinforces a robust defense against unauthorized resource creation and modifications. By weaving together the intricacies of deploymentmanager.deployments.create and deploymentmanager.deployments.update actions, this policy establishes a formidable barrier against potential security risks. Through these measures, the policy ensures heightened protection for your GCP Cloud Function, guarding against the perils of internet exposure, privilege escalation, and lateral movements. This strategic fortification bolsters your cloud infrastructure’s resilience and security 

 GCP 

 Medium 

 Changes in Existing Behavior 

 No changes in existing behavior for 23.9.2. 

 REST API Updates 

 No REST API Updates for 23.9.2. 

 New Features Introduced in 23.9.1 

 New Features 

 API Ingestions 

 New Policies 

 Policy Updates 

 IAM Policy Updates 

 Changes in Existing Behavior 

 REST API Updates 

 New Features 

 No new features in 23.9.1. 

 API Ingestions 

 SERVICE 

 API DETAILS 

 AWS Application Auto Scaling 

 aws-application-autoscaling-scaling-policy 

 Additional permission required: 

 application-autoscaling:DescribeScalingPolicies 

 The Security Audit role includes the permission. 

 AWS DataSync 

 aws-datasync-task 

 Additional permissions required: 

 datasync:ListTasks 

 datasync:DescribeTask 

 datasync:ListTagsForResource 

 The Security Audit role includes the permissions. 

 Amazon EFS 

 aws-efs-access-point 

 Additional permission required: 

 elasticfilesystem:DescribeAccessPoints 

 You must manually add or update the CFT template to enable the above permission. 

 Amazon Inspector 

 aws-inspector-v2-account-status 

 Additional permission required: 

 inspector2:BatchGetAccountStatus 

 The Security Audit role includes the permission. 

 Amazon Route53 

 aws-route53-health-check 

 Additional permissions required: 

 route53:ListHealthChecks 

 route53:GetHealthCheck 

 route53:ListTagsForResource 

 The Security Audit role includes the permissions. 

 AWS Systems Manager 

 aws-ssm-custom-inventory-entry 

 Additional permissions required: 

 ssm:GetInventory 

 ssm:GetInventorySchema 

 ssm:ListInventoryEntries 

 The Security Audit role only includes ssm:ListInventoryEntries . 

 You must manually add or update the CFT template to enable the following permissions: 

 ssm:GetInventory 

 ssm:GetInventorySchema 

 Google Binary Authorization 

 gcloud-binary-authorization-attestor 

 Additional permissions required: 

 binaryauthorization.attestors.list 

 binaryauthorization.attestors.getIamPolicy 

 The Viewer role includes the permissions. 

 Google Cloud Build 

 gcloud-cloud-build-github-enterprise-config-v1 

 Additional permission required: 

 cloudbuild.integrations.list 

 The Viewer role includes the permission. 

 Google Cloud Build 

 gcloud-cloud-build-private-worker-pool 

 Additional permission required: 

 cloudbuild.workerpools.list 

 The Viewer role includes the permission. 

 Google Stackdriver Monitoring 

 gcloud-monitoring-uptime-check-config 

 Additional permission required: 

 monitoring.uptimeCheckConfigs.list 

 The Viewer role includes the permission. 

 OCI IAM 

 oci-iam-compartment 

 Additional permission required: 

 COMPARTMENT_INSPECT 

 You must download and execute the Terraform template from the console to enable the permission. 

 OCI Integration 

 oci-integration-instance 

 Additional permissions required: 

 INTEGRATION_INSTANCE_INSPECT 

 INTEGRATION_INSTANCE_READ 

 You must download and execute the Terraform template from the console to enable the permissions. 

 New Policies 

 NEW POLICIES 

 DESCRIPTION 

 AWS Transit Gateway auto accept vpc attachment is enabled 

 Identifies if Transit Gateways are automatically accepting shared VPC attachments. When this feature is enabled, the Transit Gateway automatically accepts any VPC attachment requests from other AWS accounts without requiring explicit authorization or verification. This can be a security risk, as it may allow unauthorized VPC attachments to connect to the Transit Gateway. As per the best practices for authorization and authentication, it is recommended to turn off the AutoAcceptSharedAttachments feature. 

 Policy Severity— Low 

 Policy Type— Config 

 AWS CodeBuild project environment privileged mode is enabled 

 Identifies the CodeBuild projects where the privileged mode is enabled. Privileged mode grants unrestricted access to all devices and runs the Docker daemon inside the container. It is recommended to enable this mode only for building Docker images. It recommended disabling the privileged mode to prevent unintended access to Docker APIs and container hardware, reducing the risk of potential tampering or critical resource deletion. 

 Policy Severity— Medium 

 Policy Type— Config 

 AWS ECS services have automatic public IP address assignment enabled 

 Identifies whether Amazon ECS services are configured to assign public IP addresses automatically. Assigning public IP addresses to ECS services may expose them to the internet. If the services are not adequately secured or have vulnerabilities, they could be susceptible to unauthorized access, DDoS attacks, or other malicious activities. It is recommended that the Amazon ECS environment not have an associated public IP address except for limited edge cases. 

 Policy Severity— Low 

 Policy Type— Config 

 Azure Log analytics linked storage account is not configured with CMK encryption 

 Identifies Azure Log analytics linked Storage accounts which are not encrypted with CMK. By default Azure Storage account is encrypted using Microsoft Managed Keys. It is recommended to use Customer Managed Keys to encrypt data in Azure Storage accounts linked Log analytics for better control on the data. 

 Policy Severity— Low 

 Policy Type— Config 

 Azure Synapse Workspace vulnerability assessment is disabled 

 Identifies Azure Synpase workspace which has Vulnerability Assessment setting disabled. Vulnerability Assessment service scans Azure Synapse workspaces for known security vulnerabilities and highlight deviations from best practices, such as misconfigurations, excessive permissions, and unprotected sensitive data. It is recommended to enable Vulnerability assessment. 

 Policy Severity— Medium 

 Policy Type— Config 

 GCP Cloud Function has risky basic role assigned 

 Identifies GCP Cloud Functions configured with the risky basic role. Basic roles are highly permissive roles that existed prior to the introduction of IAM and grant wide access over project to the grantee. To reduce the blast radius and defend against privilege escalations if the Cloud Function is compromised, it is recommended to follow the principle of least privilege and avoid use of basic roles. 

 Policy Severity— Medium 

 Policy Type— Config 

 GCP VM instance has risky basic role assigned 

 Identifies GCP VM instances configured with the risky basic role. Basic roles are highly permissive roles that existed prior to the introduction of IAM and grant wide access over project to the grantee. To reduce the blast radius and defend against privilege escalations if the VM is compromised, it is recommended to follow the principle of least privilege and avoid use of basic roles. 

 Policy Severity— Medium 

 Policy Type— Config 

 Policy Updates 

 POLICY UPDATES 

 DESCRIPTION 

 Policy Updates—RQL 

 AWS Elastic Load Balancer v2 (ELBv2) with listener TLS/SSL is not configured 

 Changes— The policy RQL has been updated to not trigger an alert when the HTTP listener requests are redirected to HTTPS URL. 

 Severity— Low 

 Policy Type— Config 

 Current RQL— 

 Updated RQL— 

 Impact— Low. Existing alerts where the Listener requests are redirected to HTTPS URL are resolved. 

 GCP VM instance configured with default service account 

 Changes— The policy RQL has been updated to check for Default Service Accounts with editor role. 

 Severity— Informational 

 Policy Type— Config 

 Current RQL— 

 Updated RQL— 

 Impact— Low. Existing alerts where they do not have editor role attached to default service account are resolved. 

 Policy Updates—Metadata 

 AWS EC2 instance not configured with Instance Metadata Service v2 (IMDSv2) 

 Changes— The policy now supports remediation. You can resolve the alerts by running the remediation. 

 Severity— High 

 Policy Type— Config 

 Impact— No impact since support for remediation is introduced. 

 IAM Policy Updates 

 Prisma Cloud has updated the following Azure IAM out-of-the-box (OOTB) policies: 

 POLICY NAME 

 DESCRIPTION 

 CURRENT RQL 

 UPDATED RQL 

 Azure VM instance associated managed identities with Key Vault management access (data access is not included) 

 With access to 'Microsoft.KeyVault' service, an adversary can elevate the access of the VM instance, expanding the surface of the attack and granting access to cloud resources with sensitive information 

 Azure Managed Identity (user assigned or system assigned) with broad Key Vault management access 

 Managed identities provide an automatic way for applications to connect to resources that support Azure Active Directory (Azure AD) authentication. Providing Key Vault management access lets non-human identities manage key vaults. The least privilege model should be enforced and unused sensitive permissions should be revoked. 

 Azure Service Principals with broad Key Vault management access 

 Service Principles provide an automatic way for applications to connect to resources that support Azure Active Directory (Azure AD) authentication. Providing Key Vault management access lets non-human identities manage key vaults. The least privilege model should be enforced and unused sensitive permissions should be revoked 

 Azure AD users with broad Key Vault management access 

 Providing Key Vault access lets users manage key vaults. The least privilege model should be enforced and unused sensitive permissions should be revoked 

 Changes in Existing Behavior 

 FEATURE 

 DESCRIPTION 

 Pending Resolution State for Alerts 

 A new alert state Pending Resolution is available for filtering alerts. If you configured an alert rule with Auto Remediation enabled and it includes config policies that are remediable, the alerts is marked with pending_resolution which is an interim state. As soon as the CLI is executed and the resource misconfguration is addressed, the alert transitions from the Pending Resolution state to the Resolved state. 

 API change— The https://pan.dev/prisma-cloud/api/cspm/get-alert-filter-and-options/ includes the new state in the response. 

 If you have not explicitly included the alert.status value in the API request, the response will include alerts with all states ("dismissed", "snoozed", "pending_resolution", "open", "resolved"). 

 REST API Updates 

 CHANGE 

 DESCRIPTION 

 New Search APIs 

 The following new endpoints are available as part of the Search APIs: 

 POST /search/api/v1/config 

 POST /search/api/v1/config/async 

 POST /search/api/v1/config/download 

 POST /search/api/v1/config/:id 

 Previous Features Introduced in October 2023 

 Next Features Introduced in August 2023 

 Last updated 2 months ago 

 Was this helpful?

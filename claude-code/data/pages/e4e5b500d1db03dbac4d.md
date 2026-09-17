---
url: https://docs.prismacloud.io/release-notes/prisma-cloud-release-information/features-introduced-in-2026/features-introduced-in-august-2026
fetched_at: 2026-09-16T13:35:54Z
source: prisma-cloud
---

# Features Introduced in August 2026 | Prisma Cloud arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Enterprise Edition 

 Release Notes 

 Prisma Cloud Release Information 

 Features Introduced in 2026 

 Features Introduced in August 2026 

 Learn what’s new in the Prisma® Cloud August 2026 release. This release includes updates for Prisma Cloud Enterprise Edition version 26.8.1 and Runtime updates for version 34.05. 

 Enhancements 

 Changes in Existing Behavior 

 API Ingestions 

 Policy Updates 

 Policy Updates - Metadata 

 Enhancements 

 Enhancement 

 Details 

 Support for Rocky Linux 10.x (Red Quartz) 
 Secure the Runtime 

 Prisma Cloud now supports Rocky Linux 10.x (Red Quartz) for vulnerability and compliance scanning and for runtime protection. 

 Rocky Linux — source-package and epoch support 
 Secure the Runtime 

 During scanning, Rocky Linux binary packages are now linked to their source package (for example, expat-devel and expat-libs linked to expat ). This ensures that CVE matches against the Rocky Linux errata feed are no longer missed. Version comparison also honors the RPM epoch, which eliminates a class of false positives on Rocky Linux images. 

 Support for RKE2 v1.35 
 Secure the Runtime 

 Defenders now deploy successfully on RKE2 v1.35 clusters. Previously, defenders failed to connect to Console because CRI-client initialization could not determine the container runtime version on newer RKE2 releases. 

 Host defender support on RHEL 10 with nftables 
 Secure the Runtime 

 Host defenders deployed on RHEL 10 with the -n (nftables) install flag no longer log spurious iptables: executable file not found in $PATH errors while evaluating the Linux CIS firewall configuration. 

 Generic distro-based CVE exclusion via custom feed entries 
 Secure the Runtime 

 Custom CVE exclusions now support any OS distribution — Windows, Ubuntu, Red Hat, Alpine, and others — extending the existing PAN-OS / GKE mechanism. Administrators can upload custom excludedCve entries per target distribution through the portal to suppress specific CVEs from vulnerability results. 

 False-positive suppression for CVEs on OpenShift nodes 
 Secure the Runtime 

 OpenShift node scans now filter out CVEs that Red Hat has marked as "not affected" for the OpenShift version in the VEX feed. This eliminates false positives such as CVE-2025-30204 on OpenShift 4.14 RHCOS nodes. 

 Environment variables printed on defender startup 
 Secure the Runtime 

 On startup, the defender now logs all of its environment variables, making support cases involving env-var configuration significantly faster to triage. 

 Defender image — Red Hat Ecosystem Catalog certification 
 Secure the Runtime 

 The defender image now includes the required labels ( name , vendor , version , release , summary , description , maintainer ) and a /licenses folder with license files (MIT, Apache, and others), enabling certification in the Red Hat Ecosystem Catalog. 

 Agentless OCI — compartment ID support 
 Secure the Runtime 

 The Agentless scanner for Oracle Cloud Infrastructure now supports specifying a compartment ID, which allows customers to scope agentless scans to a specific OCI compartment. 

 Agentless AWS — expanded fallback instance types 
 Secure the Runtime 

 The Agentless scanner now uses additional fallback instance types beyond m5.2xlarge , m4.2xlarge , m3.2xlarge , t2.2xlarge , and m6i.2xlarge . This allows agentless scans to succeed in AWS regions where the current defaults are unavailable (for example, af-south-1 , me-central-1 , il-central-1 , ap-southeast-4 , eu-central-2 , and others). 

 Registry scan — image deduplication by digest 
 Secure the Runtime 

 Registry scans configured with a Cap now deduplicate images by digest before enforcing the Cap, so the same image referenced by multiple tags is no longer scanned repeatedly or double-counted against the Cap. 

 Vulnerability / Compliance Explorer — daily refresh at very large scale 
 Secure the Runtime 

 The daily compliance-stats aggregation in db.AggregatedComplianceData is restructured so it no longer accumulates a $push array that exceeds MongoDB's hard-coded 100 MiB internal limit. This unblocks daily refresh of the Vulnerability and Compliance Explorer for very large tenants (~4M+ container compliance hits). A workaround is also available: set the new MONGO_DB_CUSTOM_CONFIG_PATH environment variable to mount a custom mongodb configuration that raises internalQueryMaxPushBytes from 100 MiB to 500 MiB. 

 LDAP users in multiple groups — access to all assigned collections 
 Secure the Runtime 

 On on-prem consoles using LDAP, when a user belongs to multiple LDAP groups mapped to custom roles, the user is now granted access to every collection associated with those groups instead of only the first collection. 

 Changes in Existing Behavior 

 Feature 

 Description 

 Removal of environment-variable printing from defender failure log 
 Secure the Runtime 

 The defender no longer prints its environment variables to the log on failure. This complements the new startup-time env-var dump (see Enhancements) and prevents environment state from appearing in failure logs. 

 API Ingestions 

 Service 

 API Details 

 Amazon Bedrock 

 aws-bedrock-prompt 

Additional permissions required:
- bedrock:ListPrompts 
- bedrock:GetPrompt 
- bedrock:ListTagsForResource 

The Security Audit role does not include bedrock:GetPrompt . A custom role is required.

 Note : This API is disabled by default and available upon request. 

 Amazon Bedrock 

 aws-bedrock-flow 

Additional permissions required:
- bedrock:ListFlows 
- bedrock:GetFlow 
- bedrock:ListTagsForResource 

The Security Audit role does not include bedrock:GetFlow . A custom role is required.

 Note : This API is disabled by default and available upon request. 

 Amazon Bedrock 

 aws-bedrock-flow-alias 

Additional permissions required:
- bedrock:ListFlows 
- bedrock:ListFlowAliases 
- bedrock:GetFlowAlias 
- bedrock:ListTagsForResource 

The Security Audit role includes the permissions.

 Note : This API is disabled by default and available upon request. 

 Amazon Bedrock 

 aws-bedrock-guardrail 

Additional permissions required:
- bedrock:ListGuardrails 
- bedrock:GetGuardrail 
- bedrock:ListTagsForResource 

The Security Audit role does not include the permissions. A custom role is required.

 Note : This API is disabled by default and available upon request. 

 Amazon Bedrock AgentCore 

 aws-bedrock-agentcore-browser-session 

Additional permissions required:
- bedrock-agentcore:ListBrowsers 
- bedrock-agentcore:ListBrowserSessions 
- bedrock-agentcore:GetBrowserSession 

The Security Audit role includes bedrock-agentcore:ListBrowsers . A custom role is required for bedrock-agentcore:ListBrowserSessions and bedrock-agentcore:GetBrowserSession .

 Note : This API is disabled by default and available upon request. 

 Amazon Bedrock AgentCore 

 aws-bedrock-agentcore-code-interpreter-session 

Additional permissions required:
- bedrock-agentcore:ListCodeInterpreters 
- bedrock-agentcore:ListCodeInterpreterSessions 
- bedrock-agentcore:GetCodeInterpreterSession 

The Security Audit role includes bedrock-agentcore:ListCodeInterpreters . A custom role is required for bedrock-agentcore:ListCodeInterpreterSessions and bedrock-agentcore:GetCodeInterpreterSession .

 Note : This API is disabled by default and available upon request. 

 Amazon AppFlow 

 aws-appflow-connector 

Additional permissions required:
- appflow:DescribeConnectors 

The Security Audit role does not include the permissions. A custom role is required.

 Note : This API is disabled by default and available upon request. 

 Amazon CloudFront 

 aws-cloudfront-vpc-origin 

Additional permissions required:
- cloudfront:ListVpcOrigins 

The Security Audit role includes the permissions.

 Note : This API is disabled by default and available upon request. 

 Amazon Connect 

 aws-connect-contact-flow 

Additional permissions required:
- connect:ListInstances 
- connect:ListContactFlows 
- connect:DescribeContactFlow 

The Security Audit role does not include the permissions. A custom role is required.

 Note : This API is disabled by default and available upon request. 

 Amazon Connect 

 aws-connect-security-profile-application 

Additional permissions required:
- connect:ListInstances 
- connect:ListSecurityProfiles 
- connect:ListSecurityProfileApplications 

The Security Audit role does not include the permissions. A custom role is required.

 Note : This API is disabled by default and available upon request. 

 Amazon Connect 

 aws-qconnect-assistant 

Additional permissions required:
- wisdom:ListAssistants 
- wisdom:GetAssistant 
- wisdom:ListTagsForResource 

The Security Audit role does not include the permissions. A custom role is required.

 Note : This API is disabled by default and available upon request. 

 AWS Database Migration Service 

 aws-dms-data-migration 

Additional permissions required:
- dms:DescribeDataMigrations 

The Security Audit role includes the permissions.

 Note : This API is disabled by default and available upon request. 

 Amazon EC2 Image Builder 

 aws-imagebuilder-lifecycle-policy 

Additional permissions required:
- imagebuilder:ListLifecyclePolicies 
- imagebuilder:GetLifecyclePolicy 

The Security Audit role does not include the permissions. A custom role is required.

 Note : This API is disabled by default and available upon request. 

 Amazon Elastic Load Balancing 
 Update 

 aws-elbv2-describe-load-balancers 

The API now ingests additional listener-level attributes, including routing, mTLS/TLS header routing, CORS, and security-header response attributes.

Additional permissions required:
- elasticloadbalancing:DescribeListenerAttributes 

The Security Audit role includes the permissions.

 Note : This API is disabled by default and available upon request. 

 AWS Glue 

 aws-glue-table 

Additional permissions required:
- glue:GetDatabases 
- glue:GetTables 
- glue:GetTable 

The Security Audit role does not include the permissions. A custom role is required.

 Note : This API is disabled by default and available upon request. 

 AWS Lambda 

 aws-lambda-get-function-recursion-config 

Additional permissions required:
- lambda:ListFunctions 
- lambda:GetFunction 
- lambda:GetFunctionRecursionConfig 

The Security Audit role does not include the permissions. A custom role is required.

 Note : This API is disabled by default and available upon request. 

 Amazon Route53 Resolver 

 aws-route53resolver-dnssec-config 

Additional permissions required:
- route53resolver:ListResolverDnssecConfigs 
- route53resolver:GetResolverDnssecConfig 

The Security Audit role does not include the permissions. A custom role is required.

 Note : This API is disabled by default and available upon request. 

 Amazon S3 
 Update 

 aws-s3api-get-bucket-acl 

The API now ingests the additional attribute bucketKeyEnabled . 

 Amazon SageMaker 

 aws-sagemaker-mlflow-tracking-server 

Additional permissions required:
- sagemaker:ListMlflowTrackingServers 
- sagemaker:DescribeMlflowTrackingServer 
- sagemaker:ListTags 

The Security Audit role includes the permissions.

 Note : This API is disabled by default and available upon request. 

 AWS Systems Manager 

 aws-ssm-command-invocation 

Additional permissions required:
- ssm:ListCommandInvocations 

The Security Audit role does not include the permissions. A custom role is required.

 Note : This API is disabled by default and available upon request. 

 AWS Systems Manager 

 aws-ssm-ops-item-related-item 

Additional permissions required:
- ssm:DescribeOpsItems 
- ssm:ListOpsItemRelatedItems 

The Security Audit role does not include the permissions. A custom role is required.

 Note : This API is disabled by default and available upon request. 

 AWS Systems Manager 

 aws-ssm-ops-metadata 

Additional permissions required:
- ssm:ListOpsMetadata 
- ssm:GetOpsMetadata 
- ssm:ListTagsForResource 

The Security Audit role includes ssm:ListOpsMetadata and ssm:GetOpsMetadata . A custom role is required for ssm:ListTagsForResource .

 Note : This API is disabled by default and available upon request. 

 AWS Systems Manager 

 aws-ssm-quicksetup-configuration 

Additional permissions required:
- ssm-quicksetup:ListConfigurations 

The Security Audit role does not include the permissions. A custom role is required.

 Note : This API is disabled by default and available upon request. 

 Amazon Textract 

 aws-textract-adapter 

Additional permissions required:
- textract:ListAdapters 
- textract:GetAdapter 

The Security Audit role does not include the permissions. A custom role is required.

 Note : This API is disabled by default and available upon request. 

 Google BigQuery 

 gcloud-bigquery-model 

Additional permissions required:
- bigquery.datasets.get 
- bigquery.models.list 

The Viewer role includes the permissions. 

 Google Cloud Conversational Insights 

 gcloud-conversational-insights-conversation-analysis 

Additional permissions required:
- contactcenterinsights.conversations.list 
- contactcenterinsights.analyses.list 

The Viewer role includes the permissions. 

 Google Cloud Customer Engagement Suite 

 gcloud-ces-app 

Additional permissions required:
- ces.locations.list 
- ces.apps.list 
- ces.apps.get 
- ces.tools.list 
- ces.toolsets.list 

The Viewer role includes the permissions. 

 Google Cloud Customer Engagement Suite 

 gcloud-ces-app-conversation 

Additional permissions required:
- ces.locations.list 
- ces.apps.list 
- ces.conversations.list 
- ces.conversations.get 

The Viewer role includes the permissions. 

 Amazon S3 
 Update 

 aws-s3api-get-bucket-acl 

 Update: Added the bucketKeyEnabled attribute to the existing API ingestion 

 AWS CodeConnections 

 aws-codeconnections-connection 

Additional permissions required:

- codeconnections:ListConnections 
- codeconnections:GetConnection 

The Security Audit role does not include the permissions. A custom role is required.

 Note: This API is disabled by default and available upon request. 

 AWS CodeConnections 

 aws-codeconnections-host 

Additional permissions required:

- codeconnections:ListHosts 
- codeconnections:GetHost 

The Security Audit role does not include the permissions. A custom role is required.

 Note: This API is disabled by default and available upon request. 

 Policy Updates 

 Policy Name 

 Details 

 GCP Vertex AI Workbench User-Managed Notebook Policies 

 Changes: The following policies are deprecated because GCP deprecated Vertex AI Workbench user-managed notebooks, with support ending January 30, 2025 and final migration of existing resources on March 30, 2026.

- GCP Vertex AI Workbench user-managed notebook's JupyterLab interface access mode is set to single user
- GCP Vertex AI Workbench user-managed notebook is using default service account with the editor role
- GCP Vertex AI Workbench user-managed notebook has vTPM disabled
- GCP Vertex AI Workbench user-managed notebook auto-upgrade is disabled
- GCP Vertex AI Workbench user-managed notebook has Integrity monitoring disabled

 Impact: Alerts related to these policies resolve when the policies are deleted. 

 Policy Updates - Metadata 

 Policy Name 

 Details 

 AWS Application Load Balancer (ALB) is not using the latest predefined security policy 

 Severity: Low

 Changes: The RQL is updated to include ELBSecurityPolicy-TLS13-1-2-Res-FIPS-PQ-2025-09 as an accepted secure policy, replacing the previously listed ELBSecurityPolicy-TLS13-1-2-FIPS-PQ-2025-09 .

 Current RQL: 
 <br>config from cloud.resource where cloud.type = 'aws' AND api.name = 'aws-elbv2-describe-load-balancers' AND json.rule = type equals application and listeners[?any(protocol equals HTTPS and sslPolicy exists and sslPolicy is not member of ('ELBSecurityPolicy-TLS13-1-2-Res-2021-06','ELBSecurityPolicy-TLS13-1-2-Res-PQ-2025-09','ELBSecurityPolicy-TLS13-1-2-FIPS-PQ-2025-09'))] exists<br> 

 Updated RQL: 
 <br>config from cloud.resource where cloud.type = 'aws' AND api.name = 'aws-elbv2-describe-load-balancers' AND json.rule = type equals application and listeners[?any(protocol equals HTTPS and sslPolicy exists and sslPolicy is not member of ('ELBSecurityPolicy-TLS13-1-2-Res-2021-06', 'ELBSecurityPolicy-TLS13-1-2-Res-PQ-2025-09','ELBSecurityPolicy-TLS13-1-2-Res-FIPS-PQ-2025-09'))] exists<br> 

 Impact: Low. This update may re-open existing resolved alerts on AWS ALB resources not using the latest AWS recommended security policy. 

 Previous Features Introduced in 2026 

 Next Features Introduced in June 2026 

 Last updated 1 month ago 

 Was this helpful?

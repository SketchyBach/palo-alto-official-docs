---
url: https://cortex-docs.paloaltonetworks.com/cortex-xdr-5.x/configure-cortex-xdr/cortex-xdr-data-sources/cloud-service-provider-csp-onboarding/alibaba-cloud-cloud-onboarding/alibaba-security-capabilities-and-deployment-planning
fetched_at: 2026-09-06T09:41:02Z
source: cortex-platform
---

# Alibaba security capabilities and deployment planning | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XDR 

 Cortex XDR 5.x Documentation 

 Configure Cortex XDR 

 Cortex XDR Data Sources and Connectors 

 Cloud service provider (CSP) onboarding 

 Alibaba Cloud cloud onboarding 

 Alibaba security capabilities and deployment planning 

 Configure cloud service provider onboarding for Cortex XDR. 

 Security capabilities and deployment planning 

 Plan your deployment by reviewing the security capabilities available for Alibaba Cloud. The onboarding process deploys the capabilities using a single Terraform connector template. Alibaba Cloud onboarding currently supports two capabilities: Discovery and Permissions. No additional capabilities (such as agentless disk scanning, data security, audit logs, registry scanning, serverless scanning, or automation) are currently supported. 

 Core capabilities (Discovery and Permissions) 

 The Discovery and Permissions capabilities are mandatory and are deployed automatically when you onboard an Alibaba Cloud account to Cortex Cloud. Discovery inventories cloud resources across supported services, while Permissions analyzes IAM configurations and monitors access policies. 

 Module 

 Identity created 

 Resources created 

 Purpose 

 Regional scope 

 Discovery 

 CortexPlatformRole (RAM role) 

 RAM Role, Custom Policy, Policy Attachment, OIDC Provider 

 Read-only discovery and inventory of Alibaba Cloud resources across ECS, OSS, VPC, RDS, SLB, CEN, ActionTrail, and NAS. 

 All supported internal regions. 

 Permissions 

 CortexPlatformRole (RAM role) 

 RAM Role, Custom Policy, Policy Attachment, OIDC Provider 

 IAM permission analysis and monitoring across RAM users, roles, groups, and policies. 

 Global (RAM is a global service). 

 Read-only permissions by service 

 The Terraform template provisions a custom RAM policy with 46 read-only permissions grouped by Alibaba Cloud service: 

 Service 

 Permissions 

 ECS 

 DescribeInstances, DescribeDisks, DescribeInstanceRamRole, DescribeSecurityGroups, DescribeSecurityGroupAttribute 

 OSS 

 ListBuckets, GetBucketInfo, GetBucketLogging, GetBucketVersioning 

 RAM 

 ListUsers, ListRoles, ListGroups, ListPolicies, GetPolicy, GetPolicyVersion, ListPoliciesForUser, ListPoliciesForRole, ListPoliciesForGroup, GetLoginProfile, GetUserMFAInfo, ListAccessKeys, GetPasswordPolicy 

 RDS 

 DescribeDBInstances, DescribeDBInstanceIPArrayList, DescribeDBInstanceSSL, DescribeDBInstanceEncryptionKey, DescribeDBInstanceTDE, DescribeDBInstanceAttribute 

 VPC 

 DescribeVpcs, DescribeFlowLogs, DescribeVpnConnections, DescribeVpnConnection, DescribeSslVpnServers 

 SLB 

 DescribeLoadBalancers, DescribeLoadBalancerAttribute, DescribeVServerGroups, DescribeMasterSlaveServerGroups, DescribeCACertificates, ListTLSCipherPolicies, DescribeLoadBalancerHTTPSListenerAttribute 

 ActionTrail 

 DescribeTrails, GetTrailStatus 

 CEN 

 DescribeCens, DescribeCenInterRegionBandwidthLimits 

 NAS 

 DescribeFileSystems 

 Previous Alibaba Cloud cloud onboarding 

 Next Alibaba Cloud resource inventory 

 Last updated 5 days ago 

 Was this helpful?

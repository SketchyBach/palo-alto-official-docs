---
url: https://cortex-docs.paloaltonetworks.com/xsoar-migration-guide/cortex-xsoar-8-saas-migration/migration-prerequisites-for-cortex-xsoar-8-saas
fetched_at: 2026-09-06T10:39:19Z
source: cortex-platform
---

# Migration Prerequisites for Cortex XSOAR 8 SaaS | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSOAR 8 

 Cortex XSOAR Migration Guide 

 Cortex XSOAR 8 SaaS Migration 

 Migration Prerequisites for Cortex XSOAR 8 SaaS 

 Before you start the migration, review the users' process and other requirements. 

 Before starting migration, review the following prerequisites for the relevant migration process. 

 Self-service migration 

 Review the feature changes in Cortex XSOAR 8, including users and roles. For more information, see Cortex XSOAR 8 Feature Changes . 

 Plan your migration. Coordinate and obtain approval for the migration dates through your internal change management process. 

 Migration using the migration wizard 

 Platform 

 Feature 

 Description 

 Cortex XSOAR 8 

 General 

 Review the feature changes in Cortex XSOAR 8. For more information, see Cortex XSOAR 8 Feature Changes . 

 Users and roles 

 Review the users and roles feature in Cortex XSOAR 8. A unique email address is required for users to access the Cortex XSOAR 8 tenant. Verify that all local users who need to be migrated, including the default admin, have a unique email address in Cortex XSOAR 6. For more information, see Set up Users and Roles . 

 Important 

 You must provide a valid email address so that users can receive their activation notification and reset their password. 

 Cortex XSOAR 6 

 Version 

 Upgrade your Cortex XSOAR 6 instance to Cortex XSOAR 6.13 and above. 

 Incidents and indicators 

 If migrating incidents and indicators, ensure you have sufficient memory on Cortex XSOAR 6. 

 Important 

 When migrating from Cortex XSOAR 6 On-prem, you need more than 50% free RAM on Cortex XSOAR 6 due to how the migration flow is handled. If current use on your Cortex XSOAR 6 environment exceeds 50%, add more RAM to your Cortex XSOAR 6 server. 

 Diagnostic issues 

 In Cortex XSOAR 6, fix any system diagnostic issues, which enables a faster initial data sync, a shorter downtime at the switchover date, and a better performance on Cortex XSOAR 8. For more information about how to fix system diagnostic issues, see Fix System Diagnostics Issues . 

 Bolt/Elasticsearch specifications 

 In Cortex XSOAR 6, ensure that you comply with the following recommended specifications: 

 Bolt deployments: See System Requirements . 

 Elasticsearch deployments: See Elasticsearch System Requirements . 

 Private remote repository 

 If using a private remote repository, verify that the remote repository branch is not protected before starting the migration process. You can set it to protected after the switchover (migration is complete). 

 Deprecated content 

 Update any deprecated content in Cortex XSOAR 6 to supported content. For example, on Cortex XSOAR 6, if you have configured the Demisto REST API integration, replace it with the Core Rest API. When you start the migration process, the initial data sync includes the updated supported content to Cortex XSOAR 8. If you do not update before the initial data sync, the content is not migrated and you must configure it in Cortex XSOAR 8. 

 N/a 

 Migration dates 

 Coordinate and obtain approval for the migration dates through your internal change management process. A brief period of downtime may be required when the migration is completed. 

 Tip 

 We also recommend reviewing the following information: 

 Familiarize yourself with the Cortex Gateway. The Cortex Gateway is a central portal for managing your Cortex products. Although most settings can also be configured in the Cortex XSOAR 8 tenant, there are additional options in the Cortex Gateway. You can manage users through the Customer Support Portal (CSP) or SSO. User management in the CSP applies to all Cortex products. For more information, see Set up Users and Roles . 

 Cortex XSOAR 8 Release Notes to understand the latest features and improvements. 

 Update your firewall's allow list for Cortex XSOAR 8. For more information, see Cortex XSOAR 8 IP addresses . 

 Previous Migration FAQs - XSOAR 6 On-Prem to XSOAR 8 SaaS 

 Next Migrate from Cortex XSOAR 6 to Cortex XSOAR 8 SaaS (Self-Service) 

 Last updated 1 month ago 

 Was this helpful?

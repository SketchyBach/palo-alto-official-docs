---
url: https://docs.prismacloud.io/content-collections/data-security-posture-management/how-to-articles/explore-data-asset-access-information
fetched_at: 2026-09-16T13:35:51Z
source: prisma-cloud
---

# Explore Data Asset Access Information | Prisma Cloud arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Enterprise Edition 

 Content Collections 

 Data Security Posture Management 

 How-To Articles 

 Explore Data Asset Access Information 

 This article describes how to do the following: 

 Obtain a comprehensive visibility into cloud IAM principals with access to specific assets. 

 Filter access information based on permission types, originating projects, and other crucial criteria such as risk indicators. 

 Prerequisites 

 This information is calculated by Prisma Cloud CIEM (Cloud Identity and Entitlement Management). In order for access information to be visible in the Prisma Cloud console, the tenant needs to be subscribed both to DSPM and CIEM. 

 Access information 

 Access information is available for the following services: 

 AWS 

 S3 

 RDS 

 EFS 

 Aurora 

 OpenSearch 

 DynamoDB 

 Azure 

 Storage account 

 NetApp File share 

 SQL Server 

 Azure SQL 

 CosmosDB 

 GCP 

 GCS 

 BigTable 

 CloudSQL 

 BigQuery 

 The access information shows all users and roles who have access to the data asset scope, including access levels (e.g. Read, Write, List and Manage) and public access 

 This feature is enabled by default, no action is required to enable access information on data assets. 

 View asset access details 

 Navigate to the asset whose access details you wish to view. 

 In Prisma Cloud DSPM, click Inventory. 

 In Inventory, click the name of the specific asset you want to view.

 Click the Access tab to view the DAG (data access governance) for the asset.

 Use the Access mapping graph or Access list to identify and monitor all the roles and users with access permissions to the asset. 

 Access mapping graph 

 The access mapping graph opens by default when you click the Access tab. 

 Use the mapping graph to instantly view a snapshot of each users’ relationship to the asset. 

 View the permissions associated to each identity. 

 Mouse hover over the bucket, project, user groups, and roles to view more details about users' access details. 

 Access list 

 In the Access tab click the toggle at the top right to view the access information in list form. (To return to the mapping graph, click the mapping icon.) 

 Previous Create and edit custom risk rules 

 Next Monitor and Identify AWS Activities 

 Last updated 1 month ago 

 Was this helpful?

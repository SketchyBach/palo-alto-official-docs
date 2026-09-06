---
url: https://cortex-docs.paloaltonetworks.com/cortex-cloud-runtime-security/cortex-cloud-data-sources-and-connectors/vendor-specific-data-sources/databricks/databricks
fetched_at: 2026-09-06T09:59:52Z
source: cortex-platform
---

# How to onboard Databricks | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex Cloud 

 Cortex CLOUD Runtime Security 

 Cortex Cloud Data Sources and Connectors 

 Vendor-specific data sources and connectors 

 Databricks 

 Cortex Cloud Runtime 

 How to onboard Databricks 

 Collect Databricks data in Cortex Cloud. 

 You can add the Databricks platform as a third-party data source in Cortex Cloud Data Security. 

 Prerequisites 

 In order to use Databricks, you must be registered. 

 Make sure you have the following account permissions to onboard: 

 Account Admin : For information about this role, see Set up users, groups, and roles . 

 Metastore Admin : Databricks admin that can only be assigned by an Account Admin . Databricks recommends assigning this role to a group rather than an individual user in order to facilitate management and ensure continuity in case an individual leaves the organization. 

 Make sure you have the following ID numbers at hand: 

 Account ID: Refers to the unique identifier of the user account. 

 How to find the Account ID 

 Log in to the account console. 

 In the account console, your user name should appear in the upper right corner of the page. 

 Click the icon of your user name. 

 Your account ID appears in the list. 

 Application ID: Refers to the unique identifier for a service principal in Databricks. 

 How to find the Application ID 

 Log in to the account console. 

 Click User Management and navigate to the Service Principals tab. 

 Click the name of the service principal for which you need the Application ID. The service principal must also be the account admin. 

 On the service principal settings page, navigate to the Configuration tab. 

 The Application ID appears in the list. 

 Add the Databricks data source 

 To add the Databricks platform as a data source, you need to add configuration details, establish a connection, and then verify the connection. 

 Add configuration details 

 Navigate to Settings → Data Sources & Integrations. 

 On the Data Sources & Integrations page, click + Add New. 

 On the Add Data Sources or Integrations page, search for Databricks, then hover over it and click Add. 

 On the Databricks integration instance settings page, for the Configuration step do the following: 

 Enter the display name for your Databricks integration instance. 

 Enter your Databricks Account ID. 

 Enter your Application ID. 

 Select a cloud platform. 

 (Optional) Turn on the toggle for My Databricks account protected by network policies and select a region. 

 If you turn on this feature, both the cloud and region will be used for scanning, possibly incurring cost and requiring adherence to certain compliance policies. 

 Click Next. 

 Click Next. 

 Establish a connection 

 For the Establish Connection step, you are now instructed to open your Databricks console in a new browser tab. 

 On the Establish Connection tab, click the arrow to open the Generated script code block. Do one or both of the following: 

 Click the cloud icon to download the .sh script file. 

 Click the copy icon to copy the script to your clipboard. 

 Run the script in your Databricks CLI. 

 Click Verify Connection. 

 Verify the connection 

 For the Verify Connection step, if the connection is verified, a confirmation message is displayed. 

 Click Close. 

 Databricks now appears in the list of data sources on the Data Sources & Integrations page. 

 Verify the Cortex Gateway connection 

 At the end of the onboarding process, a pending request for Databricks approval is automatically created and displayed on the Cortex Gateway screen. In order to complete the onboarding process, approve the pending request. If you do not have permissions, contact your Cortex Cloud administrator. 

 For more information, see Egress configurations . 

 Previous Databricks 

 Next Databricks 

 Last updated 1 month ago 

 Was this helpful?

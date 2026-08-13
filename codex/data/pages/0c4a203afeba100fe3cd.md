---
url: https://docs.paloaltonetworks.com/prisma-access-agent/administration/troubleshoot-prisma-access-agents/prisma-access-agent-and-agent-manager-logs/audit-prisma-access-agent-configuration-activities
fetched_at: 2026-08-13T17:22:28Z
source: palo-alto-main
---

# Audit Prisma Access Agent Configuration Activities Clear

Audit Prisma Access Agent Configuration Activities 

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

 Audit Prisma Access Agent Configuration Activities 

 Updated on 

 Wed Jul 29 16:23:07 PDT 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma Access Agent Docs 

 Administration 

 User Guide 

 Release Notes 

 New Features 

 Updated on 

 Wed Jul 29 16:23:07 PDT 2026 

 Focus 

 Home 

 Prisma Access Agent 

 Prisma Access Agent Administration 

 Troubleshoot Prisma Access Agents 

 Audit Prisma Access Agent Logs and Management Logs 

 Audit Prisma Access Agent Configuration Activities 

 Download PDF 

 Prisma Access Agent 

 Audit Prisma Access Agent Configuration Activities 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma Access Agent Docs 

 Administration 

 User Guide 

 Release Notes 

 New Features 

 Previous 

 Management Log Event Details 

 Next 

 Prisma Access Agent Overview 

 Audit Prisma Access Agent Configuration Activities 

 Where Can I Use This? What Do I Need? 

 Prisma Access (Managed by Strata Cloud Manager) 

 Prisma Access (Managed by Panorama) 

 NGFW (Managed by Panorama) 

 Check the prerequisites for the deployment you're
 using 

 Contact your Palo Alto Networks account representative to
 activate the Prisma Access Agent feature 

 You can audit any Prisma Access Agent configuration change in the log viewer or
 Strata Logging Service . 

 For example, you can audit the configuration logs to see the configuration activities
 that were performed in Prisma Access and who initiated the actions. You can also
 view event details to identify the Prisma Access configuration before and
 immediately after a configuration change. 

 All data is collected and sent to Strata Logging Service , which is viewable in
 Strata Logging Service or the Prisma Access log viewer. 

 To learn how to use the log viewer, you can explore logs in detail. 

 Open the log viewer or Strata Logging Service . 
 In the log viewer, the following events will be logged under Log Viewer Common Configuration . 

 In Strata Logging Service , select Explore Common Configuration . 

 If no data is displayed, increase the different time range to show more
 entries. 

 To narrow the scope of the logs in the table, you can create queries based on
 the column headings in the log viewer, and save the queries as filters for use
 later. 

 Enter a log query in the search field. Click to
 display a list of fields and select an item from the list or start
 entering the name of a field and select from the list of matching
 items. 

 You can create queries base on the configuration schema . 

 Select an operator, such as = ,
 != , < > , or
 LIKE and a value for the field. You can build
 on the query by adding AND or OR operators. For example, to show logs
 that have configuration changes, you can create a query such as: 

 Event Name = edit AND Event Result = Succeeded 

 You can use the LIKE operator to filter on
 values that match a pattern you provide. For example, to show all
 event ID values that start with gateway , you
 can
 specify: 
 Event ID Value LIKE 'gateway%' 

 Select a different time range if needed. 

 Click the right arrow to begin the query. 

 To save the query for future use, click the filter save icon. Then,
 enter a descriptive Name for the query and
 Save the filter for future use. 

 ( Optional ) Export the log query results
 to a .csv file and download the file to your
 computer for further analysis with a spreadsheet app. 

 To view the details in a log, click the icon 

 next to a log in the table to open the LOG
 DETAILS window. 

 To show all the details in the log, select Log
 Details . 

 Previous 

 Management Log Event Details 

 Next 

 Prisma Access Agent Overview 

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

 Enterprise DLP 

 SaaS Security 

 Network Security 

 Visibility & Monitoring 

 Dashboards 

 Incidents and Alerts 

 Reports 

 Autonomous DEM 

 Best Practices 

 Best Practices Library 

 Experts Corner 

 Solutions Docs from Product Experts 

 Prisma Access Agent 

 Next-Generation Firewall 

 Administration 

 Prisma Access 

 Panorama 

 Strata Cloud Manager 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

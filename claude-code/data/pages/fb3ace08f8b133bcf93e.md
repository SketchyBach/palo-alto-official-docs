---
url: https://docs.paloaltonetworks.com/content/techdocs/en_US/advanced-url-filtering/administration/monitoring/monitoring-web-activity/view-user-activity-report.html
fetched_at: 2026-09-16T12:58:21Z
source: palo-alto-main
---

# View the User Activity Report Clear

Updated on 

 Thu Jul 30 19:58:44 PDT 2026 

 Focus 

 Home 

 Advanced URL Filtering 

 Monitoring 

 Monitoring Web Activity 

 View the User Activity Report 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 Advanced URL Filtering 

 View the User Activity Report 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Advanced URL Filtering 

 Administration 

 Previous 

 Monitoring Web Activity 

 Next 

 Generate, Schedule, and Share URL Filtering Reports 

 View the User Activity Report 

 Learn how to quickly generate and view user activity
reports for users and groups in your organization. 

 Where can I use
this? What do I need? 

 Prisma Access (Managed by Strata Cloud Manager) 

 Prisma Access (Managed by Panorama) 

 NGFW (Managed by Strata Cloud Manager) 

 NGFW (Managed by PAN-OS or Panorama) 

 Advanced URL
 Filtering license (or a legacy URL filtering
 license) 

 Notes: 

 Legacy URL filtering licenses are discontinued,
 but active legacy licenses are still
 supported. 

 Prisma Access licenses include Advanced URL Filtering capabilities. 

 User Activity reports provide insights into the activities of users you search or filter by.
 These insights include: 

 Unique threats detected 

 Web browsing overview (URLs visited and their associated risk levels) 

 Most visited websites 

 Sites blocked by Security policy rules 

 Application usage summaries 

 You can share these Activity reports with others in your organization and schedule
 them for regular delivery. 

 For more information about additional report types you can generate and how to
 generate them for NGFW (Managed by PAN-OS or Panorama) , see Report Types . For Strata Cloud Manager ,
 see Generate, Schedule, and Share URL Filtering Reports . 

 Strata Cloud Manager 

 PAN-OS & Panorama 

 View the User Activity Report ( Strata Cloud Manager ) 

 The following procedure describes how to create a User Activity report. Access to
 user activity data requires an active Cloud Identity Engine tenant. 

 Activate the Cloud Identity
 Engine . 

 Set up the Cloud Identity
 Engine . 

 The Cloud Identity Engine gives apps read-only access to your Active
 Directory information and enables you to easily share reports with people in
 your organization. 

 Configure a User Activity report. 

 To view user activity, select Insights Activity Insights Users . 

 In the Search bar, enter a username or user. You can also filter the
 data by User Name . 

 Unique threats, a web browsing summary, and more appear for the
 requested user. 

 ( Optional ) Filter by Time Range ,
 Scope Selection , or other options. 

 Download the report. 
 For more information, see Download, Share, and Schedule User
 Activity Reports . 

 View the User Activity Report ( PAN-OS & Panorama ) 

 Configure a User Activity Report. 

 Select Monitor PDF Reports User Activity Report . 

 Add a report and enter a Name for
it. 

 Select the report Type : 

 Select User to generate
a report for one person. 

 Select Group for a group of users. 

 You
must enable User-ID to be able
to select user or group names. If User-ID is not configured, you
can select the type User and enter the IP
address of the user’s computer. 

 Enter the Username/IP Address for
a user report or enter the group name for a user group report. 

 Select the time period. You can select an existing
time period, or select Custom . 

 Select the Include Detailed Browsing check
box, so browsing information is included in the report. 

 Run the report. 

 Click Run Now . 

 When the firewall finishes generating report, click
one of the links to download it: 

 Click Download User Activity Report to
download a PDF version of the report. 

 Click Download URL Logs to download
a CSV file of the corresponding log entries. 

 After downloading the report, click Cancel . 

 If you want to save the user activity report settings
to run the same report again later, click OK ;
otherwise click Cancel . 

 View the user activity report by opening the file that
you downloaded. The PDF version of the report shows the user or
group on which you based the report, the report time frame, and
a table of contents: 

 Click an item in the table of contents to view the report
details. For example, click Traffic Summary by URL Category to view
statistics for the selected user or group. 

 Previous 

 Monitoring Web Activity 

 Next 

 Generate, Schedule, and Share URL Filtering Reports

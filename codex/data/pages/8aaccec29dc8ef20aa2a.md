---
url: https://docs.paloaltonetworks.com/content/techdocs/en_US/enterprise-dlp/administration/monitor-enterprise-dlp/enterprise-dlp-incident-management/view-dlp-log-details/view-enterprise-dlp-log-details-on-strata-cloud-manager.html
fetched_at: 2026-09-16T13:01:44Z
source: palo-alto-main
---

# View Enterprise DLP Incident Details on Strata Cloud Manager Clear

Updated on 

 Thu Sep 10 12:41:05 PDT 2026 

 Focus 

 Home 

 Enterprise DLP 

 Administration 

 Monitor Enterprise DLP 

 Enterprise DLP Incident Management 

 View an Enterprise DLP Incident 

 View Enterprise DLP Incident Details on Strata Cloud Manager 

 Download PDF 

 Enterprise DLP 

 View Enterprise DLP Incident Details on Strata Cloud Manager 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Enterprise DLP Docs 

 Activation & Onboarding 

 Getting Started 

 Administration 

 Reference 

 Release Notes 

 New Features by OS Version 

 New Features by Month 

 View Enterprise DLP Incident Details on Strata Cloud Manager 

 View the incident details for traffic that matches your Enterprise Data Loss Prevention (E-DLP) data
 profiles on Strata Cloud Manager . 

 Log in to 
 Strata Cloud Manager . 

 ( Optional ) Configure syslog forwarding for Enterprise DLP incidents. 

 Select Configuration Data Loss Prevention DLP Incidents . 

 Filter and group the Incidents list to narrow down the
 DLP incidents you want to investigate. 

 Scan Date — Enterprise DLP supports
 filtering DLP incidents generated in the Past 60
 Minutes , Past 3 Hours ,
 Past 24 Hours , Past 7
 Days , Past 30 Days , or
 Past 90 Days . 

 Add Filters —Add additional filters to narrow
 down the scope of DLP incidents. 

 Palo Alto Networks recommends using the Data
 Profile filter. This filter displays all DLP
 incidents triggered by a specific data profile . 

 For the Regions filter, Enterprise DLP generates incidents in the Region 
 where the Public Cloud Server is located. 

 For Prisma Access (Managed by Strata Cloud Manager) and NGFW (Managed by Strata Cloud Manager) , Enterprise DLP automatically resolves to the closest Public
 Cloud Server to where the inspected traffic originated. 

 When Palo Alto Networks introduces a new Public Cloud Server,
 Enterprise DLP automatically resolve to it if it’s
 closer to where the inspected traffic originated. 

 This might mean that new DLP incidents generated after the
 release of a new Public Cloud Server are generated in a
 different Region . 

 Group By —Group the DLP incidents based on the
 Incident Assignee ,
 Source ,
 Destination ,
 Asset , or Product 
 (enforcement channel). 

 Review the Incidents list and click the
 Incident ID to view the DLP incident
 details. 

 You can also select and assign one or more incidents to a specific data
 security administrator to investigate and resolve as part of y our Enterprise DLP 
 incident case management process from this list.

 Review the Incident Details to review specific incident details. 

 Make note of the Report ID for the DLP incident if you
 have not already done so. Use the Report ID to view additional Traffic log
 details regarding the DLP incident. 

 General Info 

 The General Info panel displays high-level
 information about the DLP incident. 

 Incident Creation Time —Date and time a user generated
 the DLP incident. Format is DD Month YYYY H:MM
 <AM or PM> <Timezone> . 

 Severity —The incident severity configured in the DLP rule 
 ( Strata Cloud Manager ) or the data filtering
 profile ( Panorama ). 

 Incident ID —Unique ID for the DLP incident. 

 Channel —The enforcement point that forwarded traffic
 to Enterprise DLP through which the incident
 occurred. 

 Data Profile — Data
 profile that traffic matched against that
 generated the incident. 

 For Data Security (SaaS API) incidents triggered by
 a data asset policy
 rule that doesn't use Enterprise DLP match
 criteria, this field displays No Data
 Profile . 

 Report ID —Unique ID used to view additional Traffic
 log details regarding the DLP incident. 

 For Data Security (SaaS API) incidents triggered by
 a data asset policy
 rule that doesn't use Enterprise DLP match
 criteria, this field is not available. 

 Action —The action Enterprise DLP took on the
 traffic that matched your DLP
 rule . 

 Data Asset 

 File —Name of the file containing sensitive data that
 generated the incident. For non-file inspection, the
 filename is http-post-put . 

 Data Risk —The data risk
 score associated with the incident. The data risk
 score provides quantifiable metrics to measure the overall
 data risk for your organization. 

 Size —Size of the file or non-file traffic that
 generated the DLP incident. 

 Scan Date —Date and time Enterprise DLP inspected
 the matched traffic and generated the DLP incident. 

 Direction —Indicates whether the matched traffic was a
 Download or an
 Upload when the incident
 occurred. 

 Download —If you have Evidence
 Storage configured, you can Download the
 file that generated the DLP incident for further
 investigation. 

 User 

 User data requires integration with Cloud Identity Engine
 (CIE) to display. The User data displayed correspond to
 Palo Alto Networks
 Attributes that correlate to specific directory provider
 fields in CIE. 

 User Name —Name of the user as configured in CIE that
 generated the DLP incident. 

 Corresponding Palo Alto Networks Attribute is
 Name . 

 User ID —ID of the user who generated the DLP
 incident. 

 The User ID field does not require CIE integration. However,
 the corresponding Palo Alto Networks Attribute is
 User Principal Name . 

 User Email —Email of the user who generated the DLP
 incident. 

 Corresponding Palo Alto Networks Attribute is
 Mail . 

 Organization —Organization the user who generated the
 DLP incident is associated with. 

 Corresponding Palo Alto Networks Attribute is
 Department . 

 Location —Location of the user who generated the DLP
 incident. 

 Corresponding Palo Alto Networks Attribute is
 Location . 

 Manager —Manager of the user who generated the DLP
 incident. 

 Corresponding Palo Alto Networks Attribute is
 Manager . 

 Exception Rule 

 Name of the granular data profile DLP exception
 rule that generated the DLP incident. 

 Displays Not Applicable if the DLP
 incident was not generated because it matched an exceptionr
 rule. 

 Session 

 Prisma Access Device SN —Serial number of the Prisma Access tenant that blocked traffic or generated
 an alert. 

 Source IP —Upload or download IP address of the app or
 user source. 

 Destination IP —Target upload or download IP address of
 the app or user. 

 Application —App-ID for the target app. 

 URL —Fully Qualified Domain Name (FQDN) of the target
 app or user. 

 Response Management 

 The Response Management section allows your data security
 administrator to allow or deny an exemption request submitted by an
 end user through End User Coaching . 

 Case Management 

 Manually manage your DLP incidents to
 efficiently handle data security incident resolution across your
 security channels. 

 Audit History 

 The Audit History shows you the full Incident Case Management history for the specific DLP incident. It
 outlines every step of the case management process and the specific
 action taken by each user from when the incident case was assigned
 to when it was closed. 

 Review the Matches within Data Profiles to review snippets of matching traffic
 and the data patterns that matched the traffic to better understand what
 sensitive data Enterprise DLP detected. 

 Toggle the Triggered Incidents to display only the
 data patterns that contain matched criteria. 

 Enterprise DLP generates an audit log when a user
 accesses a DLP incident and reviews the associated snippet. 

 Enterprise DLP displays the proximity keyword and the
 corresponding snippet of sensitive data that generated the DLP
 incident. 

 Proximity keywords for predefined data patterns 
 are case insensitive and display exactly as detected in the snippet.
 Proximity keywords for custom data
 patterns and data dictionaries 
 are case sensitive. 

 For custom regex data patterns, Enterprise DLP displays only the
 first proximity keyword for sensitive data with a High
 Confidence match. 

 ( Nested and Granular Data Profiles ) Enterprise DLP 
 displays Triggered by each data profile
 containing match criteria in the data profile that inspected traffic
 matched against. 

 When viewing a data pattern, Enterprise DLP displays the total
 number of Occurrences as well as the
 number of Unique Occurrences for all
 High, Medium, and Low Confidence detections. 

 ( File Property data pattern ) File size of the file that
 generated the DLP incident. 

 ( EDM data sets ) Enterprise DLP displays the column
 header of the EDM data set 
 that matches the detected sensitive data. Enterprise DLP 
 displays multiple column headers when sensitive data is detected in
 multiple different columns. 

 Click Report False Positive if Enterprise DLP incorrectly detected and took action on the file
 or network traffic that it should not have. This is referred to as a
 false positive detection .
 Report a false positive detection to Palo Alto Networks to improve
 Enterprise DLP detection accuracy for yourself and other
 Enterprise DLP users. 

 General Example 

 EDM Data Set Example 

 Review the file log to learn about the traffic data for the DLP incident. 

 Select Incidents & Alerts Log Viewer . 

 From the Firewall drop-down, select File . 

 Filter to view the file log for the DLP incident using the Report
 ID. 

 Report ID = <report-id> 

 Review the file log to learn more about the traffic data for the DLP
 incident. 

 Manage your Enterprise DLP incidents.

---
url: https://cortex-docs.paloaltonetworks.com/cortex-xdr-5.x/configure-cortex-xdr/customize-cases-and-issues/create-slas-for-issue-resolution/create-case-timers-and-slas
fetched_at: 2026-09-16T08:42:48Z
source: cortex-platform
---

# Create additional case timers and SLAs | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XDR 

 Cortex XDR 5.x Documentation 

 Configure Cortex XDR 

 Customize cases and issues 

 Create SLAs for case and issue resolution 

 Cortex XDR 5.x 

 Create additional case timers and SLAs 

 Create case timers and service level agreements. 

 To help you to monitor and assess your key performance indicators (KPIs), you can create SLAs at the case level. Case SLAs provide the ability to track KPIs, obtain real-time insights into operational performance, and ensure alignment with established objectives. 

 Tip 

 You don't need to build a resolution SLAs and timers from scratch. The following built-in fields are available in the Cases table: 

 Resolution Timer: Works automatically out-of-the-box to measure elapsed case duration. 

 Resolution SLA: Pre-positioned in the system, but requires you to configure your specific time goals to begin tracking compliance. 

 For more information, see Create SLAs for case and issue resolution . 

 In addition to the default Resolution Timer and Resolution SLA fields, you can create additional timer and SLA fields to measure separate milestones, such as initial response times, or to enforce unique targets for specific customer tiers. 

 All active case SLAs are displayed in the case header. 

 Case SLAs are based on case timer fields. When a case matches the defined criteria, the timer starts running. If the timer field is linked to an SLA, the progress of the case is tracked in relation to the SLA. Note that the timer field counts forward, and the SLA field counts backwards. 

 Prerequisite 

 Before you can create a case SLA, you must first create a timer field. A timer field can be associated with a single case SLA. 

 Create a case timer 

 Take the following steps to create a case timer field: 

 Go to Settings → Configurations → Object Setup → Case and open the Fields tab. 

 Click New Field . 

 Under Field Type , select Timer . 

 Type a field name. 

 Under Tooltip , enter a description to pop-up when you hover over the field. 

 Under Case Filter , click Set Filter and define the subset of cases for which the timer will be activated. For example, you can define timers for specific domains or case source types. 

 Note 

 If you edit this filter after creation, the timer and associated SLA will be removed from any case that no longer qualifies, even if the timer is already running. 

 Under Conditions , add filters that define when the timer will start and end. To add a pause condition to the timer, click Pause and define the pause criteria. 

 Under When case is reopened , select the action that you want Cortex XSIAM to take. 

 Click Save . 

 The following timer measures the amount of time a security case is waiting in New status before an analyst starts investigating. 

 Field 

 Value 

 Field Type 

 Timer 

 Field Name 

 Security case response 

 Tooltip 

 Measure time from case opening to analyst response. 

 Cases Filter 

 Case Domain = Security 

 Start when 

 Status = New 

 End when 

 Status = Under Investigation 

 When case is reopened 

 Reset timer 

 Create a case SLA field 

 Take the following steps to create a case SLA. You can set up multiple goals for an SLA. 

 Go to Settings → Configurations → Object Setup → Cases and open the Fields tab. 

 Click New Field . 

 Under Field Type , select SLA . 

 Type a name to identify the SLA. 

 Under Tooltip , enter a description to pop-up when you hover over the field. 

 Under Timer , select the timer field with which to associate the SLA. 

 Under Goals , click Add SLA Goal . 

 The default goal applies to all cases that meet the filter criteria specified in the timer field. You can set up addition goals that apply to subsets of the defined cases. 

 In the SLA goal, type a goal name and set filter criteria. 

 In the Days , Hours , or Minutes fields, define the time conditions for to the SLA goal. 

 Arrange the SLA goals by dragging them in order of goal priority. 

 Click Save . 

 The following SLA field sets goals for analyst response times for security cases with Critical and High severity. This SLA is based on the timer field created in the previous example. Because the timer field is set up with the filter Case Domain = Security , this SLA will apply to security cases only. 

 The first SLA goal applies to security cases with a severity level of Critical . The SLA specifies that an analyst must respond to critical severity cases within one hour. 

 The second SLA goal applies to security cases with a severity level of High . The SLA specifies that an analyst must respond to high severity cases within two hours. 

 Field 

 Value 

 Field Type 

 SLA 

 Field Name 

 Security case response SLA 

 Tooltip 

 Measure time from case opening to analyst response. 

 Timer 

 Security case response 

 Goals 

 Name: Critical severity cases 

 Minutes: 60 

 Filter: severity = Critical 

 Name: High severity cases 

 Minutes: 120 

 Filter: severity = High 

 Display case timer and SLA fields in the Cases page 

 After creating new timer and SLA fields, you can add them to the Cases table layout and view them in the Cases detailed view: 

 In the Cases table view, add the timer and SLA fields to the Layout tab in the Table Setting Menu . 

 In the Cases detailed view, use the Sort By field to filter the cases list by the SLA field. Details of the SLA are shown in the list. 

 Example of SLA and timer fields 

 This example is based on the fields created in the previous procedures: 

 The Security case response timer field displays the number of minutes since case creation. When the case status moves from New to Under Investigation , the timer stops. 

 The Security case response SLA field starts counting backwards to show the remaining time to meet the SLA. If the field is shown in red with a minus time, the SLA is breached. 

 For case 001, the critical severity case has been in New status for 5 minutes. An analyst must respond within the remaining 55 minutes. 

 For case 002, the high severity case has been in New status for 20 minutes. An analyst must respond within the remaining 1 hour and 40 minutes. 

 For case 003, an analyst did not respond within 60 minutes and therefore the SLA was breached. The Security case response SLA field displays a minus value and a red icon. 

 Case ID 

 Severity 

 Security case response 

 Security case response SLA 

 001 

 Critical 

 5m 

 55m 25s 

 002 

 High 

 20m 

 1h 40m 30s 

 003 

 Critical 

 65m 

 - 5m 23s 

 Additional considerations 

 Consider the following information when working with timer and SLA fields: 

 When a case is resolved, the timer calculation stops. 

 Updating timer logic affects open and new cases. Therefore, the timer and associated SLA will be removed from any case that no longer qualifies, even if the timer is already running. 

 If you delete a timer field, the SLA associated to the timer is also deleted. 

 Previous Create SLAs for case and issue resolution 

 Next Update case timer and SLA fields 

 Last updated 15 days ago 

 Was this helpful?

---
url: https://cortex-docs.paloaltonetworks.com/xsoar-6-administrator-guide/6.14/investigate-and-respond-to-threats/day-to-day-tasks-in-cortex-xsoar/indicator-management/configure-the-indicator-timeline
fetched_at: 2026-09-16T08:57:08Z
source: cortex-platform
---

# Configure the Indicator Timeline | 6.14 | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSOAR 6 

 Cortex XSOAR 6 Administrator Guides 

 6.14 

 Investigate and Respond to Threats 

 Day to Day Tasks in Cortex XSOAR 

 Indicator Management 

 Cortex XSOAR 6.14 

 Configure the Indicator Timeline 

 Configure the Cortex XSOAR 6.14 indicator timeline and improve timeline performance. 

 A large number of indicators can affect performance of the indicator timeline. The indicator timeline displays a list of dates and events that affect the timeline, such as change of verdict, traffic light protocol, etc. There are several advanced server configurations you can implement to manage the indicator timeline performance. 

 Go to Settings → ABOUT → Troubleshooting . 

 In the Server Configuration section, click Add Server Configuration . 

 Key 

 Value 

 Description 

 indicator.timeline.enabled 

 true or false 

 Enables the indicator timeline in all flows. The default is true . 

 indicator.timeline.enabled.type.< indicatorType > 

 true or false 

 Enables the indicator timeline for a specific indicator type. This configuration overrides the indicator.timeline.enabled configuration. 

 For example: indicator.timeline.enabled.type.ip 

 indicator.timeline.auto.extract.enabled 

 true or false 

 Enables the indicator timeline in the indicator extraction flow. The default is true . 

 indicator.timeline.max.size 

 Number 

 The maximum number of indicator comments (timeline and regular). The default is 100. 

 indicator.timeline.worker.enabled 

 true or false 

 Enables you to add timeline comments through content integrations. 

 Previous Indicator Query 

 Next Exclusion List 

 Last updated 13 days ago 

 Was this helpful?

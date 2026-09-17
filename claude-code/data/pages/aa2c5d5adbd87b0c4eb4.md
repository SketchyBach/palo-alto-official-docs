---
url: https://docs.paloaltonetworks.com/content/techdocs/en_US/enterprise-dlp/administration/monitor-enterprise-dlp/email-dlp-queue-monitoring/view-email-dlp-queue-historical-dashboard.html
fetched_at: 2026-09-16T13:01:44Z
source: palo-alto-main
---

# Queue Historical Clear

Updated on 

 Thu Sep 10 12:41:05 PDT 2026 

 Focus 

 Home 

 Enterprise DLP 

 Administration 

 Monitor Enterprise DLP 

 Email DLP Queue Monitoring 

 Queue Historical 

 Download PDF 

 Enterprise DLP 

 Queue Historical 

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

 Queue Historical 

 View the Queue Historical dashboard to analyze Email DLP queue depth trends and
 per-stage dwell times across selectable time windows from real time to 30 days. 

 Log in to 
 Strata Cloud Manager . 

 Select Configuration SaaS Security Data Security Dashboard and choose Email DLP . 

 Select Queue Historical . 

 Choose a time window to set the scope of the Queue Historical
 Dashboard and Dwell Time by Stage . 

 Real Time —Live queue depth sampled at short intervals. 

 Last 15 min , Last 30 min , Last 1 hour , Last 3
 hours —Recent operational windows for active
 troubleshooting. 

 Last 12 hours , Last 24 hours , Last 2
 days —Day-scale operational windows for post-incident review. 

 Last 7 days , Last 30 days —Trend windows for identifying
 recurring patterns or capacity growth. 

 Review the Queue Historical Dashboard to identify when
 queue depth increased and which stages were affected. 

 The chart plots time on the x-axis and message count on the y-axis. The
 Delivery Pending stage is displayed as a stacked step line that separates
 Deferred and Delayed sub-components so you can distinguish messages actively
 awaiting retry from those that have already generated delay notifications.
 Scan Pending is plotted as a separate step line. 

 Use the Avg / P95 toggle in the
 upper-right corner of the chart to switch between average queue depth and
 95th-percentile depth for the selected time window. 

 Review the Dwell Time by Stage metrics for the selected
 time window to understand how long messages spent in each pipeline stage. 

 The Dwell Time by Stage section shows a widget for each pipeline stage:
 Scan Pending Queue , Delivery
 Pending Queue , Delivery Pending -
 Deferred , and Delivery Pending -
 Delayed . Each card shows average dwell time (seconds) and
 P95 dwell time for the selected window. 

 Average dwell time reflects typical processing speed per stage. P95 dwell
 time surfaces the slowest 5 percent of messages and is a stronger indicator
 of user-visible delay than the average.

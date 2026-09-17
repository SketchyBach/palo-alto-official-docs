---
url: https://docs.paloaltonetworks.com/prisma/prisma-sd-wan/prisma-sd-wan-admin/get-started-with-prisma-sd-wan/prisma-sd-wan-predictive-analytics-dashboard
fetched_at: 2026-09-16T11:41:10Z
source: palo-alto-main
---

# Prisma SD-WAN Predictive Analytics Dashboard Clear

Updated on 

 Mon Aug 24 08:54:44 PDT 2026 

 Focus 

 Home 

 Prisma SD-WAN 

 Prisma SD-WAN Administrator’s Guide 

 Get Started with Prisma SD-WAN 

 Prisma SD-WAN Predictive Analytics Dashboard 

 Download PDF 

 Prisma SD-WAN 

 Prisma SD-WAN Predictive Analytics Dashboard 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma SD-WAN Docs 

 Activation & Onboarding 

 Administration 

 CloudBlades 

 Select a Document 

 CloudBlade Integrations 

 CloudBlades Integration with Prisma Access 

 Deployment 

 Incidents & Alerts 

 Reference 

 Release Notes 

 Select a Document 

 ION 6.8 

 ION 6.6 

 ION 6.5 

 ION 6.4 

 ION 6.3 

 ION 6.1 

 ION 5.6 

 Prisma SD-WAN Controller 

 Prisma SD-WAN On-Premises Controller 

 Prisma SD-WAN CloudBlades 

 Prisma Access CloudBlade Cloud Managed 

 Prisma Access CloudBlade Panorama Managed 

 New Features 

 Previous 

 Site Summary Dashboard 

 Next 

 Prisma SD-WAN Link Quality Dashboard 

 Prisma SD-WAN Predictive Analytics Dashboard 

 Use the Prisma SD-WAN Predictive Analytics Dashboard to monitor site, application, and link health using AI/ML-driven health scores, and to predict future bandwidth capacity needs. 

 Where Can I Use This? What Do I Need? 

 Prisma SD-WAN (Managed by Strata Cloud Manager ) 

 Prisma SD-WAN 

 WAN Clarity Reports 

 Prisma® SD-WAN Predictive Analytics provides deep observability into the
 health of sites and applications and proactive monitoring to identify critical issues
 and troubleshoot them faster, thus enhancing service levels. 

 Select Insights Prisma SD-WAN Dashboard Predictive Analytics to view the Predictive Analytics dashboard. Observability
 identifies critical Sites , Links ,
 and Applications and categorizes them as
 Good , Fair , and
 Poor at the tenant level, based on AI/ML health
 scores. 

 Prediction includes predicting capacity utilization at the
 site level based on the previous three to six months of information. 

 The default time range to view the metrics is three hours; however, you can
 adjust it to shorter or longer periods depending on the desired scope of
 information. 

 View the top 10 sites whose bandwidth utilization increased in the
 previous 28 days. The dashboard shows a 7-day prediction when 28-day prediction data
 is unavailable and forecasts future branch capacity utilization. 

 For time ranges longer than seven days, a Network DVR license is required.
 For more information, contact your Palo Alto Networks Account Team. 

 Observability and Prediction are available to you with an active WAN Clarity.
 Predictive Analytics in the preview mode is available only to select customers
 (migrated to the new data lake infrastructure) and will be made available to other
 customers in the future. For more information, contact the Palo Alto Networks
 Accounts Team. 

 Sites 

 The active branch sites are categorized as Good ,
 Fair , and Poor , and inactive sites
 are classified as N/A . 

 The Sites widget displays sites with poor performance
 across your tenant. A site is categorized as poor when more than 10% of
 its health score samples fall below 30. For example, during a 3-hour period, the system
 collects 36 samples (5-minute intervals equal 12 samples per hour, or 36
 samples in 3 hours). If at least 3 samples score below 30,
 the system counts the site as poor. The poor site count reflects the number of
 unique sites with poor performance during any interval in the selected duration. 

 Rating Score Range Comments 

 Good >=70 90% or more samples score 70 or higher during the selected duration. 

 Fair 30-69 Samples score between 30 and 69. 

 Poor <30 10% or more samples score below 30 during the selected duration. 

 Click Monitor Sites to view Sites . 

 Alternatively, select Monitor Sites > List View to view branch sites. The widget displays the number of sites that were
 active during the selected time range. The average score for a poor site represents the average of
 all poor samples from sites categorized as poor. 

 Site Health Distribution—The distribution of Good ,
 Fair , and Poor sites graph
 for a given tenant. 

 Site Health Distribution Over Time—The Time series graph of Site Health
 Distribution Over Time for a given tenant. 

 The time-series graph is computed and refreshed based on the selected
 duration. For example, supported durations are one hour, three hours, 24
 hours, seven days, 30 days, and 90 days and the interval is one minute, five
 minutes, one hour, and one day, respectively. 

 Applications 

 The Applications widget displays health scores
 for underperforming applications, lists applications with poor health for your tenant,
 and plots the average health score over the last
 3 hours in 5-minute intervals. 

 Click Monitor Applications to view the Applications detail widget.
 This widget shows the list of Applications, Health Score numbers, and other details
 related to that particular application. 

 Links 

 The Links widget displays the number of poor-performing links
 for your tenant based on health scores during the selected time period. 

 Click Monitor Links to view the Link Quality
 screen. The links list view captures: 

 Link Performance—The distribution of Good ,
 Fair , and Poor links graph
 for a given tenant. 

 Link Performance Distribution Over Time—The Time series graph of Link
 Performance Distribution Over Time for a given tenant. 

 The time-series graph is computed and refreshed based on the selected
 duration. For example, supported durations are one hour, three hours, 24
 hours, seven days, 30 days, and 90 days and the interval is one minute, five
 minutes, one hour, and one day, respectively. 

 Network Insights 

 The system generates insights using machine learning
 algorithms. 

 These insights identify conditions such as: 

 Excessive Packet Loss Detected 

 Excessive Latency Detected 

 Bandwidth Upgrade Recommended 

 Configured vs Consumed Bandwidth Mismatch Detected 

 Low Circuit Throughput Detected 

 Top Sites with BW Utilization Growth in Past 30 days 

 The Top Sites with BW Utilization Growth in Past 30 days 
 widget displays the top 10 Sites that have only increased their utilization in the
 last 30 days. Ingress and Egress Trend depicts information for the previous 30
 days. 

 Site Capacity Prediction and Anomaly 

 The Site Capacity Prediction and
 Anomaly widget displays the number of sites that will reach high
 capacity utilization threshold within the next 28 days. If 28 days prediction is
 unavailable, it will show the seven days prediction for the branch site capacity
 utilization, the bandwidth anomaly for the specified time range filter, and the
 bandwidth forecast for the next seven days. 

 Click the branch to view the sites that are attaining high capacity bandwidth
 utilization. 

 Click the number under the Branch column to view the Site List View screen. The table
 lists sites approaching capacity. For the
 anomalous occurrence branch, you can drill down into the site list to view bandwidth anomaly occurrences for each site. 
 Select Approaching Capacity, Anomaly, or All to filter the displayed site results. 

 Previous 

 Site Summary Dashboard 

 Next 

 Prisma SD-WAN Link Quality Dashboard

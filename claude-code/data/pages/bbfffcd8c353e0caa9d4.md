---
url: https://cortex-docs.paloaltonetworks.com/cortex-xdr-5.x/detect-investigate-and-respond-to-threats/monitor-dashboards-and-reports/dashboard-reference/system-dashboards/data-ingestion
fetched_at: 2026-09-06T09:43:10Z
source: cortex-platform
---

# Data Ingestion | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XDR 

 Cortex XDR 5.x Documentation 

 Detect, investigate, and respond to threats 

 Monitor dashboards and reports 

 Dashboard reference 

 System dashboards 

 Cortex XDR 5.x 

 Data Ingestion 

 Use Cortex XDR Data Ingestion to monitor data collection health, volume, and coverage. 

 The Data Ingestion dashboard provides interactive, high-level overviews of your data ingestion health, rates, and storage consumption across different ingestion tiers. You can use this dashboard to monitor the status of your data sources and ensure that logs are being ingested as expected. 

 What the Data Ingestion dashboard measures 

 The Data Ingestion dashboard, including the Ingestion Rate widget, reports the volume of data ingested from third-party and external data sources, such as: 

 Next-generation firewalls and other network devices 

 Cloud providers and SaaS applications 

 Syslog and other collectors 

 Custom integrations and API-based ingestion 

 Data collected by the Cortex XDR agent is not included in these figures. 

 Note 
Endpoint data collected by the Cortex XDR agent is excluded from the Data Ingestion dashboard by design. If your tenant collects data exclusively through Cortex XDR agents, the Ingestion Rate widget displays 0 even though endpoint data is being ingested normally. This does not indicate data loss or an ingestion failure. 

 Key Features 

 Unified monitoring: Displays a unified view of your ingestion health across different storage tiers, such as Analytics and Cortex Data Lake. 

 Consumption tracking: Monitors daily data consumption to help you manage license quotas and plan capacity. 

 Drill-down capabilities: Allows you to click on widgets to see a full breakdown of ingested data by source or investigate specific ingestion alerts. 

 Data Ingestion widgets 

 The dashboard includes several widgets to help you visualize your data pipeline: 

 Ingestion Rate: Displays the rate at which logs are ingested by each data source. 

 Analytics Daily Consumption: Shows the amount of data consuming your primary Analytics (GB) license quota. 

 Data Lake Daily Consumption: Shows data ingested into the low-cost Cortex Data Lake tier for long-term storage and compliance. 

 Daily Quota Consumption: Tracks the current data usage against your organization's daily allowance. 

 Top Data Sources: A breakdown of the top contributors to your daily billable ingestion volume. 

 Non-billable data ingestion 

 ​To provide comprehensive security visibility without increasing ingestion costs, specific log types are moved to a non-billable status. While these logs continue to be ingested and analyzed, they do not consume your licensed daily ingestion quota and are excluded from the billable totals on this dashboard. 

 The following data types are non-billable: 

 ​Enhanced Application Logs (EAL): Specialized telemetry from Palo Alto Networks firewalls. EAL data volume is excluded from your daily license consumption totals. To ensure consistency, the EAL category is removed from the NGFW Ingestion Rate graph to align with its non-billable status. 

 ​Cortex Audit Logs (PANW/Cortex Audit): Logs documenting administrative and investigative actions within the Cortex platform. These logs are excluded from the billable daily ingestion quota calculation and are not displayed in the Data Ingestion dashboard widgets to ensure that system auditing does not impact your organization's data allowance. 

 Important design considerations 

 ​When using the Data Ingestion dashboard, keep the following design exclusions in mind: 

 ​Cortex XDR agent data exclusion: By design, data collected from Cortex XDR agents is excluded from the Data Ingestion dashboard and the Ingestion Rate widget . This dashboard focuses on external data sources and integrations rather than endpoint agent telemetry. Data ingested from Cortex XDR agents is licensed under a different model, such as Analytics Enterprise. 

 ​Data source categorization: Data sources are grouped by vendor and product to allow for granular monitoring. 

 ​Ingestion tiers: The dashboard distinguishes between the Analytics and Data Lake tiers. Only data ingested into the Analytics tier counts toward your primary daily quota. 

 ​Stale data: While the system can collect data offline (such as using the Broker VM), the ingestion dashboard focuses on real-time pipeline health. Large uploads of stale data from prolonged disconnections are typically handled to avoid triggering daily ingestion limit alerts. 

 Verifying Cortex XDR agent data ingestion 

 Cortex XDR agent data is always ingested into, and queryable from, the xdr_data dataset. To confirm that endpoint data is arriving, run the following XQL query: 

 If the query returns rows, agent data is being ingested as expected, regardless of what the Ingestion Rate widget shows. 

 Troubleshooting: Ingestion Rate shows 0 

 If the Ingestion Rate widget shows 0, use this checklist to verify your environment: 

 Identify your data sources : If the tenant is connected only to Cortex XDR agents and has no third-party data sources, an Ingestion Rate of 0 is expected. 

 Confirm endpoint data is arriving : Query xdr_data as shown above. If rows are returned, ingestion is healthy. 

 Check third-party sources : If you have external data sources configured and the widget still shows 0, verify those integrations under Settings > Data Sources & Integrations . 

 Note 

 If you need Cortex XDR agent volume to be reflected in the ingestion dashboard, contact your account team to submit a feature request. 

 Monitoring and Troubleshooting 

 You can use the dashboard in conjunction with the Data Ingestion Health page to investigate disruptions. When a significant deviation from normal ingestion patterns is detected, the system triggers health alerts . 

 From the dashboard, you can: 

 Identify sources with zero or unexpected ingestion rates. 

 Right-click an alert or widget to Investigate in XQL . 

 View related metrics in the metrics_view preset to troubleshoot pipeline issues. 

 Previous Cloud Security Operations 

 Next Asset management 

 Last updated 6 days ago 

 Was this helpful?

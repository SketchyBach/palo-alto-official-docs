---
url: https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cases-and-issues/case-concepts/issues-findings-and-events
fetched_at: 2026-09-06T10:04:38Z
source: cortex-platform
---

# Issues, findings, and events | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex Cloud 

 Cortex CLOUD Posture Management 

 Cases and issues 

 Case concepts 

 Cortex Cloud Posture 

 Issues, findings, and events 

 Understand the relationship between issues, findings, and events. 

 Understand how issues, findings, and events are related to cases. 

 Issues 

 Issues identify the problems that you need to solve in your environment. Cortex Cloud creates issues when problems occur in your environment that cross defined thresholds, or surpass your organization's accepted level of risk and threat tolerance. 

 Each issue comprises a defined framework of: 

 What happened: A description of the problem 

 How is your environment impacted: Affected assets or the impact of this issue in your environment 

 Contributing evidence: Data that supports our analysis and observations 

 Recommended actions: Automations, playbooks, and manual suggestions 

 Issues are created from findings or from events that occur in your environment. When an issue is created, Cortex Cloud assesses the content of the issue and assigns it to a new or existing case. In addition, according to the content of the issue, it is assigned to a domain that reflects the operational use case of the issue, such as Security or Health . Using case grouping logic, Cortex Cloud then determines whether to link the issue to a case. 

 When you open a case, you can see all issues that are linked to the case. Review the Grouping graph to see why the issues were grouped together in the case. For more information about how issues are grouped in cases, see Case grouping . 

 In addition, Cortex Cloud offers the flexibility to: 

 Manually link and unlink issues from cases. Issues can also be linked to multiple cases. For more information, see Link or unlink issues from a case . 

 Create issues from custom rules that you define. For example, correlation rules, malware rules, and vulnerability rules. 

 Findings 

 Findings are non-actionable, informational objects that provide context about the current state of the assets in your environment. 

 To gather findings, Cortex Cloud periodically scans the assets in your environment and collects raw data about vulnerabilities, compliance, exposures, malware, secrets, and other posture-related information about the asset. This raw data is processed, saved to datasets, and recorded as findings. 

 Each time the assets are scanned, the findings are updated to reflect the current state of the assets. Therefore, the finding for an asset will change over time. 

 Each finding is categorized according to its context, for example Configuration, Vulnerability, Compliance, or Identity, and is related directly to the scanned asset. When you investigate an asset through the Asset Inventory , you can see any findings that were collected for the asset. 

 Findings themselves are not issues, however findings that match a specific logic can generate issues. You can also set up your own rules to trigger issues when certain types of findings are recorded. For example, you can set up Compliance rules that will create issues if specific compliance fails are identified in compliance findings. 

 To view findings: 

 View all findings. From the the Issues page click Findings . 

 See findings for a specific asset. From the Asset Inventory, select a specific asset to open the asset card. If findings are available for the asset you can click to open the finding card. 

 Search the Findings data set to see the findings collected over time for an asset. 

 Events 

 Events are logged activities that occur in your environment. 

 Cortex Cloud collects event logs that audit the activities that occur in your environment. The logs are ingested from various sources, such as Palo Alto Networks Next-Generation Firewall (NGFW), Prisma Access, third-party sources, and EDRs. These logs provide a complete picture of the events that occur in the environment and the activities surrounding the events. 

 When certain malicious objects (such as malware) are discovered in the event logs, an issue is created. During case investigation, you can query your event logs to see information about the actors and processes that triggered the issue. 

 Previous Case concepts 

 Next Case grouping 

 Last updated 1 month ago 

 Was this helpful?

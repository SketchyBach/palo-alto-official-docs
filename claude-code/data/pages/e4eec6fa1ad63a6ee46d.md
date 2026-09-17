---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsiam/reference-and-developer-docs/role-based-access-control/jupyter-and-observability-apps-permissions
fetched_at: 2026-09-16T08:37:40Z
source: cortex-platform
---

# Jupyter and Observability apps permissions | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSIAM 

 Cortex XSIAM Documentation 

 Reference and developer docs 

 Role-Based Access Control 

 Cortex XSIAM 

 Jupyter and Observability apps permissions 

 Configure permissions to use Jupyter and Observability applications. 

 The following permissions enable users to use Jupyter and Observability applications. 

 Caution 

 Usage and management: The permissions allow users to use and access existing application instances. If a user needs to manage, install, configure, or delete application instances, they must be granted the separate Apps permission under the Configurations menu. For more information, see Apps - Instance permissions . 

 Jupyter Notebook permissions 

 An interactive notebook environment for creating and running Python-based analyses and automations. Jupyter Notebooks let you explore security data, build custom analytics, and prototype detections. 

 Caution 

 Jupyter Data Access (SBAC): Granting access to Jupyter does not bypass dataset restrictions. Users must have the appropriate Scope-Based Access Control (SBAC) dataset permissions to query specific data via the Cortex SDK within their notebooks. 

 For more information, see Notebooks . 

 Component 

 Description 

 Roles Example 

 None 

 No access to Jupyter Notebooks. 

 SOC Analyst Tier-1: Focus on issue triage. 

 SOC Analyst Tier-2: Standard investigation tools are sufficient. Consider View/Edit if the team performs advanced analysis. 

 View/Edit 

 Full access to Jupyter Notebooks, including installing, creating, editing, saving, and exporting notebooks. You can also execute Python code and access datasets. 

 SOC Analyst Tier-3: Advanced investigations often require custom analysis, data exploration, and ad-hoc queries. 

 Threat Hunter: Critical - Notebooks are essential for hypothesis-driven hunting, custom analytics, and data exploration. 

 Security Engineer: Develops custom detection logic, automation scripts, and analysis tools. 

 Jupyter Notebook - required and recommended permissions 

 Consider adding the following permissions: 

 Permission 

 Permission Level 

 Reason 

 Query Center 

 View or View/Edit 

 View: Required to run XQL queries from notebooks via Cortex SDK. 

 View/Edit: Strongly recommended to save and manage queries created in notebooks. 

 Dataset Permissions 

 N/a 

 Various. Control which datasets are queryable from notebooks. 

 Query Library 

 Enabled 

 Strongly recommended to access and save queries. 

 Cases & Issues 

 View or View/Edit 

 View: Strongly recommended to view cases and issues data for correlation in notebooks. 

 View/Edit: Recommended to create/update cases from notebook analysis. 

 Threat Intel 

 View 

 Strongly recommended to enrich data with threat intelligence in notebooks. 

 Playbooks 

 Enabled with checkboxes selected 

 Enabled with Playbooks and Create Playbooks selected. Recommended to reference and develop playbooks from notebooks. 

 Scripts 

 Enabled with checkboxes selected 

 Enabled with Scripts and Create Scripts selected. Recommended to reference and develop scripts alongside notebooks. 

 Detection Rules 

 View/Edit 

 Recommended to view and create detection rules for analysis. 

 Forensics 

 View/Edit 

 Recommended to access the forensics data for analysis and initiate forensic action. 

 Action Center 

 View/Edit 

 Recommended to view and execute response actions. 

 Observability 

 Observability provides infrastructure and application monitoring capabilities within Cortex XSIAM, leveraging Prometheus-based metrics collection, alerting, and visualization through Grafana integration. 

 Note 

 Observability is a Beta feature and is still subject to changes. To enable the feature in your tenant, contact your Customer Support Team. 

 Component 

 Description 

 Roles Example 

 None 

 No access to Observability. 

 SOC Analyst Tier-1, 2, and 3, and Threat Hunters who do not need tool development. 

 View/Edit 

 Full access to Observability, including access to the Observability interface, View Prometheus UI, and Alert Manager. 

 Security Engineers: Require full access for tool development and configuration. 

 Observability - required and recommended permissions 

 Consider adding the following permissions: 

 Permission 

 Permission Level 

 Reason 

 Broker VM 

 View or View/Edit 

 Strongly recommended to view Broker VMs hosting Observability collectors and configure Observability collectors on Broker VMs. 

 Alert Notifications 

 View/Edit 

 Recommended to configure alert notifications from Observability alerts. 

 Data Sources 

 View/Edit 

 Recommended to manage data sources that feed into Observability. 

 Cases & Issues 

 View/Edit 

 Recommended to correlate Observability alerts with security cases and create cases from Observability findings. 

 Audit 

 View 

 Recommended to review audit logs for Observability configuration changes. 

 Previous Automation Exclusion Center permissions 

 Next Threat Management permissions 

 Last updated 20 days ago 

 Was this helpful?

---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsiam/protect-your-endpoints/endpoint-security/install-and-manage-endpoints/harden-endpoint-security/vulnerability-assessment
fetched_at: 2026-08-13T15:13:17Z
source: cortex-platform
---

# Vulnerability Assessment | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

Vulnerability Assessment | Cortex Documentation Portal 

 ⌘ Ctrl k 

 Blog Support 
 More 

 Home 

 Products 

 Guides 

 Release Notes 

 API 

 Reference 

 AI Assistant 

 Good afternoon 
 I'm here to help you with the docs. 

 What is this page about? What should I read next? Can you give an example? 

 ⌘ Ctrl i 

 AI Based on your context 
 Send 

 Learn about Cortex XSIAM 

 Navigate the Cortex XSIAM docs 

 Get started with Cortex XSIAM 

 Agentic AI in Cortex XSIAM 

 Cortex XSIAM product licenses 

 In-product support ticket creation 

 Supported web browsers 

 Use the interface 

 Manage API keys 

 Onboard Cortex XSIAM 

 How to onboard Cortex XSIAM 

 Plan and prepare 

 Deployment steps 

 Post-deployment 

 Configure Cortex XSIAM 

 Learn how to configure Cortex XSIAM 

 Data management 

 Cortex XSIAM Data Sources and Connectors 

 Marketplace 

 Configure the Cortex Agentic Assistant 

 Cortex MCP server 

 Automations 

 Engines 

 Remote repository management 

 Customize cases and issues 

 XQL query management 

 Multi-Tenant 

 Managed Services configuration in Cortex 

 Protect your endpoints 

 Endpoint security 

 Endpoint protection 

 Install and manage endpoints 

 Set up endpoint protection 

 Define endpoint groups 

 Configure global agent settings 

 Apply profiles to endpoints 

 Create an agent installation package 

 Harden endpoint security 

 Device control 

 Host firewall 

 Disk encryption 

 Host Inventory 

 Vulnerability Assessment 

 Set a Cortex XDR agent Critical Environment version 

 Manage endpoint protection 

 Endpoint DLP 

 Detect, Investigate, and respond to threats 

 Monitor dashboards and reports 

 Investigation and response 

 Agentic Assistant chat 

 Asset management 

 Threat management 

 Attack surface management 

 Vulnerability management 

 Exposure management 

 Cortex Advanced Email Security 

 Identity Threat Detection and Response (ITDR) 

 Cloud Security 

 Monitor and track compliance adherence 

 Cloud security rules and policies 

 Cortex Cloud Data Classification 

 Cortex Data Security 

 Cloud Identity Security 

 Network exposure detection 

 Cortex Cloud SaaS Security 

 Cortex Cloud AI Security 

 Serverless function posture security 

 Cortex Cloud Application Security 

 Cloud workload policies and rules 

 Base image rules 

 Web and API Security (WAAS) 

 Serverless function runtime security 

 Reference and developer docs 

 Cortex XSIAM XQL 

 Graph Search 

 Cortex CLI 

 Role-Based Access Control 

 API documentation 

 Reference 

 Migrating to a new Broker VM image 

 Learn more about migrating to the latest broker VM image 

 Standalone Broker VM 

 Broker VM high availability cluster node 

 On this page 

 For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSIAM 

 Cortex XSIAM Documentation 

 Protect your endpoints 

 Endpoint security 

 Install and manage endpoints 

 Harden endpoint security 

 Vulnerability Assessment 

 Cortex XSIAM vulnerability assessment enables you to identify and quantify the security vulnerabilities on an endpoint. After evaluating the risks to which each endpoint is exposed and the vulnerability status of an installed application in your network, you can mitigate and patch these vulnerabilities on all the endpoints in your organization. 

 The Vulnerability Assessment feature is included with the Host Insights license. If you have Cortex Cloud Posture Security, Cortex Cloud Runtime Security, Exposure Management, or Attack Surface Management add-ons, use the Vulnerability Management feature. 

 You can access the vulnerability assessment feature by navigating to Inventory → Endpoints → Host Insights → Vulnerability Assessment. Cortex XSIAM uses an advanced algorithm to collect extensive details on common vulnerabilities and exposures from comprehensive databases and to produce an in-depth analysis of endpoint vulnerabilities. Cortex XSIAM retrieves the latest information from the NIST public database to calculate the severity score. 

 Vulnerability Assessment 

 Vulnerability Assessment uses an advanced algorithm to collect extensive details on CVEs from comprehensive databases and to produce an in-depth analysis of the endpoint vulnerabilities. 

 Prerequisite 

 The following are prerequisites for Cortex XSIAM to perform an Enhanced Vulnerability Assessment of your endpoints. 

 Requirement 

 Description 

 Supported Platforms 

 Windows 

 Cortex XDR agent 8.3 or a later release. 

 Cortex XDR collects all the information about the operating system and the installed applications, and calculates CVE. 

 CVEs that apply to applications that are installed by one user aren't detected when another user without the application installed is logged in during the scan. 

 MacOS 

 Cortex XDR agent 8.3 or a later release. 

 Cortex XDR collects all the information about the operating system and the installed applications, and calculates CVE. 

 Setup and Permissions 

 Ensure Host Inventory Data Collection is enabled for your Cortex XDR agent. 

 Certificates for Windows and macOS 

 When Advanced Vulnerability and Assessment is enabled, these certificates are a prerequisite for Windows and macOS. 

 Download the certificates from here . 

 Import the Digicert Trusted Root G4 certificate into the Trusted Root Certification Authorities store in the local machine. 

 In some environments, if the scan does not initialize, the DigiCert Trusted G4 Code Signing RSA4096 SHA384 2021 CA1 certificate, may also be required. 

 Import the signed certificate into the Intermediate Certification Authorities store in the local machine. 

 Limitations 

 Some CVEs may be outdated if the Cortex XDR agent wasn't updated recently. 

 Application versions which have reached end-of-life (EOL) may have their version listed as 0. This doesn't affect the detection of the CVEs. 

 Some applications are listed twice. One of the instances may display invalid version , however, this doesn't affect the functionality. 

 The scanning process may impact performance on the Cortex XDR agent during scanning. The scan may take up to two minutes. 

 After enabling the feature for the first time, it may take up to a week to get the updated data into the platform. Re-collecting the data from all endpoints in your network could take up to 6 hours. After that, Cortex XSIAM initiates periodic recalculations to rescan the endpoints and retrieve the updated data. If at any point you want to force data recalculation, click Recalculate. The recalculation performed by any user on a tenant updates the list displayed to every user on the same tenant. 

 CVE Analysis 

 View CVE details : Left-click the CVE to view in-depth details about it on a panel that appears on the right. Use the in-panel links as needed. 

 View a complete list of all endpoints in your network that are impacted by a CVE : Right-click the CVE and then select View affected endpoints. 

 Learn more about the applications in your network that are impacted by a CVE : Right-click the CVE and then select View applications. 

 Exclude irrelevant CVEs from your endpoints and applications analysis : Right-click the CVE and then select Exclude. You can add a comment if needed, as well as Report CVE as incorrect for further analysis and investigation by Palo Alto Networks. The CVE is grayed out and labeled Excluded and no longer appears on the Endpoints and Applications views in Vulnerability Assessment, or in the Host Insights widgets. To restore the CVE, you can right-click the CVE and Undo exclusion at any time. 

 The CVE will be removed/reinstated to all views, filters, and widgets after the next vulnerability recalculation. 

 You can perform the following actions from Cortex XDR as you analyze the existing vulnerabilities: 

 Value 

 Description 

 Affected endpoints 

 The number of endpoints that are currently affected by this CVE. For excluded CVEs, the affected endpoints are N/A. 

 Applications 

 The names of the applications affected by this CVE. 

 CVE 

 The name of the CVE. 

 You can click each individual CVE to view in-depth details about it on a panel that appears on the right. 

 Description 

 The general NIST description of the CVE. 

 Excluded 

 Indicates whether this CVE is excluded from all endpoint and application views and filters, and from all Host Insights widgets. 

 Platforms 

 The name and version of the operating system affected by this CVE. 

 Severity 

 The severity level (Critical, High, Medium, or Low) of the CVE as ranked in the NIST database. 

 Severity score 

 The CVE severity score is based on the NIST Common Vulnerability Scoring System (CVSS). Click the score to see the full CVSS description. 

 For each vulnerability, Cortex XSIAM displays the following default and optional values. 

 If you have the Identity Threat Module enabled, you can also view the CVE analysis in the Host Risk View. To do so, from Inventory → Assets → Asset Scores, select the Hosts tab, right-click on any endpoint, and select Open Host Risk View. 

 To evaluate the extent and severity of each CVE across your endpoints, you can drill down into each CVE in Cortex XDR and view all the endpoints and applications in your environment that are impacted by the CVE. Cortex XDR retrieves the latest information from the NIST public database. From Inventory → Endpoints → Host Inventory → Vulnerability Assessment, select CVEs on the upper-right bar. This information is also available in the va_cves dataset, which you can use to build queries in XQL Search. 

 Endpoint Analysis 

 View endpoint details : Left-click the endpoint to view in-depth details about it on a panel that appears on the right. Use the in-panel links as needed. 

 View a complete list of all applications installed on an endpoint : Right-click the endpoint and then select View installed applications. This list includes the application name and version of applications on the endpoint. If an installed application has known vulnerabilities, Cortex XSIAM also displays the list of CVEs and the highest Severity. 

 (Windows only) Isolate an endpoint from your network : Right-click the endpoint and then select Isolate the endpoint before or during your remediation to allow the Cortex XDR agent to communicate only with Cortex XSIAM. 

 (Windows only) View a complete list of all KBs installed on an endpoint : Right-click the endpoint and then select View installed KBs. This list includes all the Microsoft Windows patches that were installed on the endpoint and a link to the Microsoft official Knowledge Base (KB) support article. This information is also available in the host_inventory_kbs preset, which you can use to build queries in XQL Search. 

 Retrieve an updated list of applications installed on an endpoint : Right-click the endpoint and then select Rescan endpoint 

 You can perform the following actions from Cortex XSIAM as you investigate and remediate your endpoints: 

 Value 

 Description 

 CVEs 

 A list of all CVEs that exist on applications that are installed on the endpoint. 

 Endpoint ID 

 Unique ID assigned by Cortex XSIAM that identifies the endpoint. 

 Endpoint name 

 Hostname of the endpoint. 

 You can click each individual endpoint to view in-depth details about it on a panel that appears on the right. 

 Last Reported Timestamp 

 The date and time of the last time the Cortex XDR agent started the process of reporting its application inventory to Cortex XSIAM. 

 MAC address 

 The MAC address associated with the endpoint. 

 IP address 

 The IP address associated with the endpoint. 

 Platform 

 The name of the platform running on the endpoint. 

 Severity 

 The severity level (Critical, High, Medium, or Low) of the CVE as ranked in the NIST database. 

 Severity score 

 The CVE severity score based on the NIST Common Vulnerability Scoring System (CVSS). Click the score to see the full CVSS description. 

 For each vulnerability, Cortex XSIAM displays the following default and optional values. 

 To help you assess the vulnerability status of an endpoint, Cortex XSIAM provides a full list of all installed applications and existing CVEs per endpoint and also assigns each endpoint a vulnerability severity score that reflects the highest NIST vulnerability score detected on the endpoint. This information helps you to determine the best course of action for remediating each endpoint. From Inventory → Endpoints → Host Inventory → Vulnerability Assessment, select Endpoints on the upper-right bar. This information is also available in the va_endpoints dataset. In addition, the host_inventory_endpoints preset lists all endpoints, CVE data, and additional metadata regarding the endpoint information. You can use this dataset and preset to build queries in XQL Search. 

 Application Analysis 

 To view the details of all the endpoints in your network on which an application is installed, right-click the application and select View endpoints. 

 To view in-depth details about the application, left-click the application name. 

 From Inventory → Endpoints → Host Inventory, select Applications. 

 Starting with macOS 10.15, Mac built-in system applications are not reported by the Cortex XDR agent and are not part of the Cortex XDR Application Inventory. 

 You can assess the vulnerability status of applications in your network using the Host inventory. Cortex XDR compiles an application inventory of all the applications installed in your network by collecting from each Cortex XDR agent the list of installed applications. For each application on the list, you can see the existing CVEs and the vulnerability severity score that reflects the highest NIST vulnerability score detected for the application. Any new application installed on the endpoint will appear in Cortex XSIAM within 24 hours. Alternatively, you can re-scan the endpoint to retrieve the most up-to-date list. 

 Previous Host Inventory Next Set a Cortex XDR agent Critical Environment version 

 Last updated 16 days ago 

 Was this helpful? 

 ‍ 

 Trust Center 

 ‍ 

 Privacy 

 ‍ 

 Terms of Use 

 ‍ 

 Legal 

 © 2026 Palo Alto Networks, Inc. All rights reserved. 

 Was this helpful?

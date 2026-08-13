---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsiam/configure-cortex-xsiam/cortex-xsiam-data-sources/administration-and-troubleshooting/integrations/integration-use-cases
fetched_at: 2026-08-13T15:05:07Z
source: cortex-platform
---

# Integration use cases | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

Integration use cases | Cortex Documentation Portal 

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

 What are Cortex XSIAM data sources and connectors? 

 Complete data source and connector catalog 

 Vendor-specific data sources and connectors 

 Connectors 

 Standard data sources 

 Cloud service provider (CSP) onboarding 

 Generic on-premise data collectors 

 Palo Alto Networks integrations 

 Cloud Posture and Runtime Security data sources 

 External alerts using External Issue Mapping 

 Administration and troubleshooting 

 Manage instances 

 Integrations 

 Integration use cases 

 Add an integration instance 

 Configure integration permissions 

 Fetch issues from an integration instance 

 Manage credentials 

 Troubleshoot Integrations 

 Forward Requests to Long-Running Integrations 

 Verify collector connectivity 

 Overview of data ingestion metrics 

 About health issues 

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

 Configure Cortex XSIAM 

 Cortex XSIAM Data Sources and Connectors 

 Administration and troubleshooting 

 Integrations 

 Integration use cases 

 The following categories are common use cases for Cortex XSIAM integrations. While this list is not meant to be exhaustive, it's a starting point to understand what use cases are supported by Cortex XSIAM and third-party integrations. 

 Analytics and SIEM 

 Top use cases: 

 Fetch issues with relevant filters. 

 Create, close, and delete issues/events/cases. 

 Update issues - update status, assignees, severity, SLA, and more. 

 Get events related to an issue/case for enrichment/investigation purposes. 

 Query SIEM (consider aggregating logs). 

 These integrations usually include the Fetch Issues or Fetch Alerts option for an integration instance configuration. The integration may also include integration commands enabling you to list or retrieve issues or related information. 

 Analytics & SIEM integration Example: ArcSight ESM 

 Authentication and Identity Management 

 Top use cases: 

 Use credentials from the authentication vault to configure instances in Cortex XSIAM. (Save credentials in: Settings → Configurations → Integrations → Credentials .) Integrations that use credentials from the vault should have the Switch to credentials option. 

 Lock/Delete Account – Use an integration to lock/unlock a third-party account. 

 Reset Account - Perform a reset password command for a third-party account. 

 Lock an external credentials vault - in case of an emergency (if the vault has been compromised), allow the option to lock/unlock the entire vault via an integration. 

 Step-Up authentication - Enforce Multi-Factor Authentication for an account. 

 Create, update, and delete users. 

 Manage user groups. 

 Block users, force a change of passwords. 

 Manage access to resources and applications. 

 Create, update, and delete roles. 

 Authentication integration example: CyberArk AIM v2 (Partner Contribution) 

 Case Management 

 Top use cases: 

 Create, get, edit, close a ticket or issue, and add and view comments. 

 Assign a ticket/issue to a specified user. 

 List all tickets, and filter by name, date, and assignee. 

 Get details about a managed object, update, create, or delete. 

 Add and manage users. 

 Case Management/Ticketing integration example: ServiceNow V2 

 Data Management and Threat Intelligence 

 Top use cases: 

 Enrich information about different IOC types: Upload object for scan and get the scan results. (If there’s an option to upload private/public, the default should be set to private.) Search for former scan results about an object to get information about a sample without uploading it yourself. Enrich information and scoring for the object. 

 Add indicators to the system and search for existing indicators. 

 Add indicators to the exclusion list. 

 Calculate DBot Score for indicators. 

 Enrich asset – get vulnerability information for an asset (or a group of assets) in the organization. 

 Generate/trigger a scan on specified assets. 

 Get a scan report including vulnerability information for a specified scan and export it. 

 Get details for a specified vulnerability. 

 Scan assets for a specific vulnerability. 

 Data Enrichment & Threat Intelligence integration example: Unit 42 Intelligence. 

 Email 

 Top use cases: 

 Get message – download the email itself, retrieve metadata, and body. 

 Download attachments for a given message. 

 Manage senders – block/allow specified mail senders. 

 Manage URLs – block/allow the sending of specified URLs. 

 Encode/decode URLs in messages 

 Release a held message when a gateway has placed a suspicious message on hold. 

 Email Gateway integration example: MimeCast v2 

 Endpoint 

 Top use cases: 

 Fetch issues and events 

 Get event details (from a specified alert) 

 Quarantine a file 

 Isolate and contain endpoints 

 Update indicators (for example, network and hashes) by policy (can be block, monitor) – deny list 

 Add indicators to the exclusion list 

 Search for indicators in the system (see indicators and related issues/events) 

 Download a file based on the hash and the path 

 Trigger scans on specified hosts 

 Update .DAT files for signatures and compare existing .DAT files to the newest one on the Cortex XSIAM tenant 

 Get information for a specified host (OS, users, addresses, hostname) 

 Get policy information and assign policies to endpoints 

 Endpoint integration example: Tanium V2 

 Forensics and Malware Analysis 

 Top use cases: 

 Submit a file and get a report (detonation) 

 Submit a URL and get a report (detonation) 

 Search for past analysis (input being a hash/URL) 

 Retrieve a PCAP file 

 Retrieve screenshots taken during analysis 

 Forensic and Malware Analysis example: Cuckoo Sandbox 

 Network Security 

 Top use cases: 

 Create block/accept policies (source, destination, port), for IP addresses and domains 

 Add addresses and ports (services) to predefined groups, create groups, and more 

 Support custom URL categories 

 Fetch network logs for a specific address for a configurable time frame 

 URL filtering categorization change request 

 Built-in blocked rule command for fast blocking 

 If there is a Management Firewall, allow the option to manage policy rules through it 

 Get/fetch issues 

 Get PCAP file, packet 

 Get network logs filtered by time range, IP addresses, ports, and more 

 Create/manage/delete policies and rules 

 Update signatures from an online source/upload + get the last signature update information 

 Install policy (if existing) 

 Network Security Firewall integration examples: Tufin (Partner Contribution), Protectwise 

 Vulnerability Management 

 Top use cases: 

 Enrich asset – get vulnerability information for an asset (or a group of assets) in the organization. 

 Generate/trigger a scan on specified assets 

 Get a scan report including vulnerability information for a specified scan and export it 

 Get details for a specified vulnerability 

 Scan assets for a specific vulnerability 

 Vulnerability Management integration example: Tenable.sc 

 Previous Integrations Next Add an integration instance 

 Last updated 22 days ago 

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

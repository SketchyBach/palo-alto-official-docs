---
url: https://cortex-docs.paloaltonetworks.com/xsoar-6-administrator-guide/6.13/onboard-cortex-xsoar/marketplace/use-cases
fetched_at: 2026-09-06T10:44:20Z
source: cortex-platform
---

# Use Cases | 6.13 | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSOAR 6 

 Cortex XSOAR 6 Administrator Guides 

 6.13 

 Onboard Cortex XSOAR 

 Marketplace 

 Cortex XSOAR 6.13 

 Use Cases 

 Explore Marketplace use cases in Cortex XSOAR 6.13. 

 This section includes common Use Cases for the different categories of Cortex XSOAR integrations. While this list is not meant to be exhaustive, it's a good starting point for you to understand what use cases could be supported by your integration. 

 Analytics and SIEM 

 Top Use Cases: 

 Fetch Incidents with relevant filters 

 Create, close and delete incidents/events/cases 

 Update Incidents - Update status, assignees, Severity, SLA, etc. 

 Get events related to an incident/case for enrichment/investigation purposes 

 Query SIEM (consider aggregating logs) 

 Note 

 This will normally include the Fetch Incidents possibility for the instance. It can also include list-incidents or get-incident as integration commands, or important information for an Event/Incident. 

 Analytics & SIEM Integration Example: ArcSight ESM 

 Authentication 

 Top Use Cases: 

 Use credentials from the authentication vault in order to configure instances in Cortex XSOAR. (Save credentials in: Settings → Integrations → Credentials .) The integration should include the isFetchCredentials parameter, and other integrations that will use credentials from the vault, should have the Switch to credentials option. 

 Lock/Delete Account – Use an integration to lock/unlock a third party account. 

 Reset Account - Perform a reset password command for a third party account 

 Lock an external credentials vault - in case of emergency (if the vault has been compromised), allow the option to lock/unlock the entire vault via an integration. 

 Step-Up authentication - Enforce Multi Factor Authentication for an account. 

 Authentication Integration Example: CyberArk AIM 

 Case Management 

 Top Use Cases: 

 Create, get, edit, close a ticket/issue, add + view comments 

 Assign a ticket/issue to a specified user 

 List all tickets, filter by name, date, assignee 

 Get details about a managed object, update, create, delete 

 Add and manage users 

 Case Management/Ticketing Integration Example: ServiceNow 

 Data Enrichment & Threat Intelligence 

 Top Use Cases: 

 Enriching information about different IOC types: Upload object for scan and get the scan results. (If there’s a possibility to upload private/public, the default should be set to private.) Search for former scan results about an object. (This way you can get information about a sample without uploading it yourself.) Enrich information and scoring for the object. 

 Add/Search for indicators in the system 

 Add indicators to the exclusion list 

 Calculate DBot Score for indicators 

 Data Enrichment & Threat Intelligence Integration Example: VirusTotal 

 Email Gateway 

 Top Use Cases: 

 Get message – Download the email itself, retrieve metadata, body 

 Download attachments for a given message 

 Manage senders – Block/ Allow specified mail senders 

 Manage URLs – Block/ Allow the sending of specified URLs 

 Encode/ Decode URLs in messages 

 Release a held message (The gateway can place suspicious messages on hold, and sometimes they would need to be released to the receiver.) 

 Email Gateway Integration Example: MimeCast 

 Endpoint 

 Top Use Cases: 

 Fetch Incidents & Events 

 Get event details (from specified incident) 

 Quarantine File 

 Isolate and contain endpoints 

 Update Indicators (Network, hashes, etc.) by policy (can be block, monitor) – deny list 

 Add indicators to the exclusion list 

 Search for indicators in the system (Seen indicators and related incidents/events) 

 Download file (based on hash, path) 

 Trigger scans on specified hosts 

 Update .DAT files for signatures and compare existing .DAT file to the newest one on the server 

 Get information for a specified host (OS, users, addresses, hostname) 

 Get policy information and assign policies to endpoints 

 Endpoint Integration Examples: Cortex XDR, Tanium and Carbon Black Protection 

 Forensics and Malware Analysis 

 Top Use Cases: 

 Submit a file and get a report (detonation) 

 Submit a URL and get a report (detonation) 

 Search for past analysis (input being a hash/URL) 

 Retrieve a PCAP file 

 Retrieve screenshots taken during analysis 

 Sandbox Integration Example: Cuckoo Sandbox 

 IAM (Identity and Access Management) 

 Top use cases: 

 Create, update, and delete users. 

 Manage user groups. 

 Block users, force change of passwords. 

 Manage access to resources and applications. 

 Create, update, and delete roles. 

 Network Security (Firewall) 

 Top Use Cases: 

 Create block/accept policies (Source, Destination, Port), for IP addresses and domains 

 Add addresses and ports (services) to predefined groups, create groups, etc. 

 Support custom URL categories 

 Fetch network logs for a specific address for a configurable time frame 

 URL filtering categorization change request 

 Built-in blocked rule command for fast-blocking 

 If there is a Management FW, allow the option to manage policy rules through it 

 Network Security Firewall Integration Example: Palo Alto Networks PAN-OS 

 Network Security (IDS/IPS) 

 Top Use Cases: 

 Get/Fetch alerts 

 Get PCAP file, packet 

 Get network logs filtered by time range, IP addresses, ports, etc. 

 Create/manage/delete policies and rules 

 Update signatures from an online source / upload + Get last signature update information 

 Install policy (if existing) 

 Network Security (IPS/IDS) Integration Example: Protectwise 

 Vulnerability Management 

 Top Use Cases: 

 Enrich asset – get vulnerability information for an asset (or a group of assets) in the organization 

 Generate/Trigger a scan on specified assets 

 Get a scan report including vulnerability information for a specified scan and export it 

 Get details for a specified vulnerability 

 Scan assets for a specific vulnerability 

 Vulnerability Management Integration Example: Tenable.io 

 Previous Convert Existing Content to Content Pack Format 

 Next Content Pack Installation 

 Last updated 1 month ago 

 Was this helpful?

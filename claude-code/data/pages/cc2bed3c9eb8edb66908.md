---
url: https://docs.paloaltonetworks.com/ngfw/administration/firewall-administration/launch-the-web-interface/use-global-find-to-search-the-firewall-or-panorama-management-server/use-global-find-pan-os-12-1-2-and-later
fetched_at: 2026-09-16T07:25:43Z
source: palo-alto-main
---

# PAN-OS 12.1.2 and later Clear

Updated on 

 Mon Aug 31 04:46:16 PDT 2026 

 Focus 

 Home 

 Next-Generation Firewall 

 Firewall Administration 

 Launch the Web Interface 

 Use Global Find to Search the Firewall or Panorama Management Server 

 PAN-OS 12.1.2 and later 

 Download PDF 

 Next-Generation Firewall 

 PAN-OS 12.1.2 and later 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Next-Generation Firewall Docs 

 Getting Started 

 Administration 

 Networking 

 Quick Start 

 Reference 

 Incidents & Alerts 

 Release Notes 

 Select a Document 

 PAN-OS 12.2 

 PAN-OS 12.1 

 PAN-OS 11.2 

 PAN-OS 11.1 

 PAN-OS 11.0 (EoL) 

 PAN-OS 10.2 

 PAN-OS 10.1 (EoL) 

 PAN-OS 10.0 (EoL) 

 PAN-OS 9.1 (EoL) 

 PAN-OS 9.0 (EoL) 

 PAN-OS 8.1 (EoL) 

 Help 

 Select a Document 

 PAN-OS 12.2 

 PAN-OS 12.1 

 PAN-OS 11.2 

 PAN-OS 11.1 

 PAN-OS 10.2 

 PAN-OS 10.1 

 New Features 

 Previous 

 PAN-OS 11.1 and earlier 

 Next 

 Manage Locks for Restricting Configuration Changes 

 PAN-OS 12.1.2 and later 

 Launch Global Find by clicking the Search icon located
 on the upper right of the web interface. 

 To access the Global Find from within a configuration area, click the drop-down
 next to an item and select Global Find : 

 For example, click Global Find on a zone named
 LAN to search the candidate configuration for each location where
 the zone is referenced. 

 The Optimized Search Results dialog provides
 the following options: 

 Search UUIDs : Use this option to perform targeted search
 exclusively for UUIDs. 

 Include Template References : Use this option to
 perform targeted search exclusively for template references.

 Optimized Search : Use this option to prioritize search
 results based on admin usage patterns. The system returns the
 most relevant results in batches. This substantially reduces
 overall search times. 

 Search tips: 

 If you initiate a search on a firewall that has multiple virtual
 systems enabled or if custom administrative role types are
 defined, Global Find will only return results for areas of the
 firewall in which the administrator has permissions. The same
 applies to Panorama device groups. 

 Spaces in search terms are handled as AND operations. For example, if
 you search on corp policy , the search results
 include instances where corp and policy exist in the
 configuration. 

 To find an exact phrase, enclose the phrase in quotation marks. 

 Enter no more than five keywords or use an exact phrase match with
 quotation marks. 

 To rerun a previous search, click Search (located on the upper right
 of the web interface) to see a list of the last 20 searches. Click
 an item in the list to rerun that search. Search history is unique
 to each administrator account. 

 To search for a UUID, you must copy and paste the UUID. 

 Previous 

 PAN-OS 11.1 and earlier 

 Next 

 Manage Locks for Restricting Configuration Changes

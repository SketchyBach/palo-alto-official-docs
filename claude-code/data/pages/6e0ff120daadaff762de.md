---
url: https://docs.paloaltonetworks.com/iot/new-features/by-date/device-security/august-2026
fetched_at: 2026-09-16T09:59:20Z
source: palo-alto-main
---

# New Features - Device Security - August 2026 Clear Clear Clear Clear Clear Clear Clear Clear Clear Clear Clear Clear Clear Clear Clear

Focus 

 Home 

 Device Security 

 New Features - Device Security - August 2026 

 Download PDF 

 Application Metadata Collection for Device Security 

 Release Date: August 2026 
 | 
 Last Updated: August 2026 

 You can now apply a metadata profile to each zone on your NGFW to filter the log fields forwarded to Device Security . When you specify a metadata profile, PAN-OS only forwards log data based on the cloud services enabled on your NGFW . This helps bandwidth-constrained sites, such as remote facilities or OT environments, as they only forward log data required by the cloud services instead of excess logs. 

 Metadata profiles map log fields to the cloud services that need them. You assign a profile to a zone with a single setting, which replaces the multi-step Log Forwarding Profile configuration previously attached to each firewall policy. 

 This gives you a simpler way to send the right metadata to Device Security and reduces the volume of data your firewalls push to the cloud at sites where bandwidth is limited. Existing log forwarding configurations continue to work after upgrade, so you can adopt metadata profiles on a zone-by-zone basis. 

 Device Security

 July 2026

 PAN-OS

 Core

 July 2026

 Strata Cloud Manager

 Management

 August 2026

 Device Security API Improvements for Subnet and Site Management 

 Release Date: August 2026 
 | 
 Last Updated: September 2026 

 You can retrieve your Device Security subnet and site structure in fewer API calls, using new query options that eliminate the need for recursive lookups and local data filtering in your automation scripts. Additional enhancements make the API more predictable and reduce the manual overhead required to build integrations with the Device Security API at scale. 

 Subnet queries support filtering by name, site, or description, and a parameter can retrieve your full subnet hierarchy in a single call instead of making one request per network block. The device inventory response includes the site name for each device, eliminating the secondary lookup required to identify site context. You can also read and write site parent-child relationships through the Device Security API, enabling you to manage your organizational structure programmatically. 

 Subnet responses always include all documented fields even when empty, so you don't need defensive attribute checks. A filter that returns no results responds with an empty list rather than an ambiguous error, and creating a site no longer requires a manually supplied identifier because the API assigns one automatically, consistent with how the web interface creates sites. 

 Device Security

 August 2026

 Expanded Support for Networks Download File in Device Security 

 Release Date: August 2026 
 | 
 Last Updated: September 2026 

 You can export a complete record of your network inventory from the Device Security Networks page , including all available columns and an option to include child networks, so you don't need to run multiple filtered exports and merge the results to reconstruct your full network hierarchy. 

 The CSV download includes every column available on the Networks page, regardless of which columns you have visible in your current table view. A new option to include child networks lets you pull descendant networks at every nesting level in a single export. A Parent Network column is present in every download, giving you the information needed to identify each record's position in the hierarchy and reconstruct the full tree from the flat file. 

 Column headers in the exported file match the labels shown in the Networks page table, so you can orient yourself without mapping field names in the file to what you see in the product. Whether you are importing data into a CMDB, auditing your network topology, or sharing a snapshot with your team, the exported file provides a self-contained representation of your network inventory. 

 Device Security

 August 2026

 Flexible MAC Address Search in Device Security 

 Release Date: August 2026 
 | 
 Last Updated: September 2026 

 When using the Device Security Query Builder , you can now search for devices by MAC address in any common format, eliminating the manual conversion required when MAC addresses from different tools use different delimiters. The Query Builder normalizes input automatically so you get accurate results regardless of how the address was formatted. 

 MAC addresses appear in different formats depending on the source. The formats range from hyphen-delimited addresses (XX-XX-XX-XX-XX-XX) and dot notation (XXXX.XXXX.XXXX) to undelimited strings (XXXXXXXXXXXX). Query Builder can accept all common delimiter styles and is case-insensitive. You can paste a MAC address from any tool into the Query Builder and find the matching device directly. 

 Flexible MAC address search applies to the Query Builder Library, global search, and the Assets Inventory search. Partial MAC search is also supported across all input formats. Existing searches in colon-delimited format continue to work without any changes. 

 Device Security

 August 2026

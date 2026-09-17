---
url: https://docs.paloaltonetworks.com/ngfw/help/12-2/objects/objects-mobile-networks-equipments
fetched_at: 2026-09-16T07:32:05Z
source: palo-alto-main
---

# Objects > Mobile Networks > Equipments Clear

Updated on 

 Wed Aug 19 00:09:31 PDT 2026 

 Focus 

 Home 

 Next-Generation Firewall 

 PAN-OS Web Interface Help 

 Objects 

 Objects > Mobile Networks > Equipments 

 Download PDF 

 Next-Generation Firewall 

 Objects > Mobile Networks > Equipments 

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

 Objects > Mobile Networks > Subscriber Groups 

 Next 

 Objects > Mobile Networks > Equipment Groups 

 Objects > Mobile Networks > Equipments 

 Use Equipment objects to identify and manage mobile equipment in enterprise mobile
 networks. 

 Equipment objects utilize the International Mobile Equipment Identity (IMEI) to manage
 and secure mobile devices in enterprise mobile networks. These objects allow
 administrators to reference specific hardware identifiers in security policy rules
 without needing to manually look up and enter 15-digit IMEI numbers for every rule. 

 Prerequisite: Enable GTP Security to make equipment object configuration
 options available on the firewall. 

 Field Description 

 Name Enter a name for the equipment object (up to 63 characters). The name
 is case-sensitive, must be unique, and can contain only letters,
 numbers, spaces, hyphens, and underscores. 

 Shared Select this option if you want the equipment object to be available
 to every virtual system (vsys) on a multi-vsys firewall or every device
 group on Panorama. 

 Description Enter an optional description for the object (up to 1,023
 characters). 

 Type Specify the identifier type and the entry: 
 IMEI —Enter a 15 or 16-digit identifier. 

 IMEI Range —Enter a range of IMEI values. Ranges are
 supported from the 4th digit through the 15th digit. 

 IMEI Prefix —Enter a variable length prefix starting from
 the 4th digit (e.g., 300*). 

 Previous 

 Objects > Mobile Networks > Subscriber Groups 

 Next 

 Objects > Mobile Networks > Equipment Groups

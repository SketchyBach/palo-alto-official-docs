---
url: https://docs.paloaltonetworks.com/ngfw/help/12-2/objects/objects-mobile-networks-equipments
fetched_at: 2026-08-13T16:52:36Z
source: palo-alto-main
---

# Objects > Mobile Networks > Equipments Clear

Objects > Mobile Networks > Equipments 

 Home 

 EN

 Location 

 Documentation Home 

 Palo Alto Networks 

 Support 

 Live Community 

 Knowledge Base 

 >

 Strata Copilot

 Objects > Mobile Networks > Equipments 

 Updated on 

 Mon Aug 03 19:43:33 PDT 2026 

 Focus 

 Download PDF 

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

 Updated on 

 Mon Aug 03 19:43:33 PDT 2026 

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

 On This Page 

 Activation & Onboarding 

 Strata Cloud Manager 

 Activate a License or Product 

 Cloud Identity Engine 

 Strata Logging Service 

 Device Associations 

 Hub 

 Identity and Access Management 

 Tenant Management 

 Next-Generation Firewalls 

 AIOps for NGFW 

 Cloud Management for NGFWs 

 Cloud NGFW for AWS 

 Cloud NGFW for Azure 

 CN-Series 

 Firewalls 

 PAN-OS 

 PAN-OS SD-WAN 

 Service Provider 

 VM-Series 

 SASE 

 Prisma Access 

 Strata Multitenant Cloud Manager 

 AI-Powered ADEM 

 Prisma Access Monitoring and Visibility 

 Prisma SD-WAN 

 ION Devices 

 Next-Generation CASB 

 Cloud-Delivered Security Services 

 Advanced WildFire 

 Advanced URL Filtering 

 Advanced Threat Prevention 

 Advanced DNS Security 

 Device Security 

 Enterprise DLP 

 SaaS Security 

 Network Security 

 Shared Policy for NGFWs and Prisma Access 

 Visibility & Monitoring 

 Dashboards 

 Incidents and Alerts 

 Reports 

 Autonomous DEM 

 Best Practices 

 Best Practices Library 

 Experts Corner 

 Solutions Docs from Product Experts 

 Mobile Network Infrastructure 

 12.2 

 PAN-OS 

 Help 

 Objects 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

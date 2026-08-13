---
url: https://docs.paloaltonetworks.com/panorama/administration/administer-panorama/manage-storage-quotas-and-expiration-periods-for-logs-and-reports/configure-storage-quotas-and-expiration-periods-for-logs-and-reports
fetched_at: 2026-08-13T17:17:28Z
source: palo-alto-main
---

# Configure Storage Quotas and Expiration Periods for Logs
and Reports Clear

Configure Storage Quotas and Expiration Periods for Logs
and Reports 

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

 Configure Storage Quotas and Expiration Periods for Logs
and Reports 

 Updated on 

 Jul 30, 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Panorama Docs 

 Getting Started 

 Administration 

 New Features 

 Updated on 

 Jul 30, 2026 

 Focus 

 Home 

 Panorama 

 Administer Panorama 

 Manage
Storage Quotas and Expiration Periods for Logs and Reports 

 Configure Storage Quotas and Expiration Periods for Logs
and Reports 

 Download PDF 

 Panorama 

 Configure Storage Quotas and Expiration Periods for Logs
and Reports 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Panorama Docs 

 Getting Started 

 Administration 

 New Features 

 Previous 

 Log and Report Expiration Periods 

 Next 

 Configure the Run Time for Panorama Reports 

 Configure Storage Quotas and Expiration Periods for Logs
and Reports 

 Configure the storage quotas and expiration periods for: 

 App Stats logs that Panorama receives from firewalls. 

 System and Config logs that Panorama and Log Collectors generate locally. 

 The
Panorama management server stores these logs locally. 

 If you reduce a storage quota such that
the current logs exceed it, after you commit the change, Panorama
removes the oldest logs to fit the quota. 

 Select Panorama Setup Management and
edit the Logging and Reporting Settings. 

 In the Log Storage settings,
enter the storage Quota (%) for each log
type. 

 When you change a percentage value, the page refreshes
to display the corresponding absolute value (Quota GB/MB column)
based on the total allotted storage on Panorama. 

 Enter the Max Days (expiration
period) for each log type (range is 1 to 2,000). 

 By default, the fields are blank, which means the logs
never expire. 

 Restore Defaults if
you want to reset the quotas and expiration periods to the factory defaults. 

 Configure the expiration period for reports that Panorama
generates. 

 Select Log Export and Reporting and
enter the Report Expiration Period in days
(range is 1 to 2,000). 

 By default, the field is blank, which means reports never expire. 

 Click OK to save your changes. 

 Configure the storage quotas and expiration periods for
logs of all types (except App Stats logs) that M-700, M-600, M-500,
M-300, M-200 appliances, or Panorama virtual appliance in Panorama
mode receives from firewalls. 

 The local or Dedicated Log Collectors store these logs. 

 You
configure these storage quotas at the Collector Group level, not
for individual Log Collectors. 

 Select Panorama Collector Groups and edit the
Collector Group. 

 In the General settings, click
the Log Storage value. 

 A value doesn’t display unless you assigned Log Collectors
to the Collector Group. If the field displays 0MB after you assign
Log Collectors, verify that you enable the disk pairs when you Configure
a Managed Collector and that you committed the changes ( Panorama Managed Collectors Disks ). 

 Enter the storage Quota(%) for
each log type. 

 When you change a percentage value, the page refreshes
to display the corresponding absolute value (Quota GB/MB column)
based on the total storage allotted to the Collector Group. 

 Enter the Max Days (expiration
period) for each log type (range is 1 to 2,000). 

 By default, the fields are blank, which means the logs
never expire. 

 Restore Defaults if
you want to reset the quotas and expiration periods to the factory defaults. 

 Click OK to save your changes. 

 Commit the changes to Panorama and push the changes to
the Collector Group. 

 Select Commit Commit and Push and Edit
Selections in the Push Scope. 

 Select Collector Groups , select
the Collector Group you modified, and click OK . 

 Commit and Push your changes. 

 Verify that Panorama applied the storage quota changes. 

 Select Panorama Setup Management and,
in the Logging and Reporting Settings, verify that the Log Storage values
are correct for the logs that the Panorama management server stores. 

 Select Panorama Collector Groups , select the
Collector Group you modified, and verify that the Log
Storage values in the General tab
are correct for the logs that the Log Collectors store. 

 You can also verify the Collector Group
storage quotas by logging in to a Log Collector CLI and entering
the operational command show log-diskquota-pct . 

 Previous 

 Log and Report Expiration Periods 

 Next 

 Configure the Run Time for Panorama Reports 

 On This Page 

 Activation and Onboarding 

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

 Panorama 

 Service Provider 

 VM-Series 

 Plugins 

 SASE 

 Prisma Access 

 Prisma SASE Multitenant Platform 

 AI-Powered ADEM 

 Prisma Access Monitoring & Visibility 

 Prisma SD-WAN 

 ION Devices 

 Next-Generation CASB 

 Cloud-Delivered Security Services 

 Advanced WildFire 

 Advanced URL Filtering 

 Advanced Threat Prevention 

 Advanced DNS Security 

 AI Access Security 

 Device Security 

 Enterprise DLP 

 SaaS Security 

 Network Security 

 Shared Policy for NGFWs and Prisma Access 

 IPSec VPN 

 Security Policy 

 Quantum Security 

 Endpoints 

 GlobalProtect 

 Remote Browser Isolation 

 Prisma Access Agent 

 Visibility & Monitoring 

 Dashboards 

 Incidents and Alerts 

 Reports 

 Autonomous DEM 

 FedRAMP 

 Prisma SASE for FedRAMP 

 Autonomous DEM for FedRAMP 

 Prisma SD-WAN Experts Corner 

 Network Policy 

 QoS Whitepaper 

 Security Architecture Whitepaper 

 External Antennas for ION-C Series 

 Dynamic Path Selection 

 Best Practices 

 Best Practices Library 

 Experts Corner 

 Solutions Docs from Product Experts 

 Resources 

 All Products A - Z 

 All Release Notes 

 Compatibility Matrix 

 Experts Corner 

 Network Security Platform 

 Security Policy 

 Decryption 

 Device-ID 

 IPSec VPN 

 Quality of Service 

 Quantum Security 

 11.1 & Later 

 Next-Generation Firewall 

 Administration 

 Panorama 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

---
url: https://docs.paloaltonetworks.com/advanced-wildfire/wildfire-appliance/use-the-wildfire-appliance-cli/wildfire-appliance-operational-mode-command-reference/show-system-raid
fetched_at: 2026-08-13T15:21:51Z
source: palo-alto-main
---

# show system raid Clear

show system raid 

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

 show system raid 

 Updated on 

 Mon Mar 02 18:41:58 PST 2026 

 Focus 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 Filter

 Expand All 
 | 
 Collapse All 

 Advanced WildFire 

 Administration 

 Appliance 

 Updated on 

 Mon Mar 02 18:41:58 PST 2026 

 Focus 

 Home 

 Advanced WildFire Powered by Precision AI™ 

 Use the WildFire Appliance CLI 

 WildFire Appliance Operational Mode Command Reference 

 show system raid 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 Advanced WildFire Powered by Precision AI™ 

 show system raid 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Advanced WildFire 

 Administration 

 Appliance 

 Previous 

 show high-availability transitions 

 Next 

 submit wildfire local-verdict-change 

 show system raid 

 Description 

 Show the RAID configuration
of the WildFire appliance. The WF-500 appliance ships with four
drives in the first four drive bays (A1, A2, B1, B2). Drives A1
and A2 are a RAID 1 pair and drives B1 and B2 are a second RAID
1 pair. 

 Hierarchy Location 

 show system 

 Syntax 

 raid { 
 detail; 
{ 

 Options 

 No additional options. 

 Sample Output 

 The following shows the
RAID configuration on a functioning WF-500 appliance. 

 admin@WF-500> show system raid detail 
Disk Pair A Available 
 Status clean 
 Disk id A1 Present 
 model : ST91000640NS 
 size : 953869 MB 
 partition_1 : active sync 
 partition_2 : active sync 
 Disk id A2 Present 
 model : ST91000640NS 
 size : 953869 MB 
 partition_1 : active sync 
 partition_2 : active sync 
Disk Pair B Available 
 Status clean 
 Disk id B1 Present 
 model : ST91000640NS 
 size : 953869 MB 
 partition_1 : active sync 
 partition_2 : active sync 
 Disk id B2 Present 
 model : ST91000640NS 
 size : 953869 MB 
 partition_1 : active sync 
 partition_2 : active sync 

 Required Privilege Level 

 superuser, superreader 

 Previous 

 show high-availability transitions 

 Next 

 submit wildfire local-verdict-change 

 On This Page 

 Activation & Onboarding 

 Strata Cloud Manager 

 Activate a License or Product 

 Strata Logging Service 

 Device Associations 

 Hub 

 Identity and Access Management 

 Tenant Management 

 Next-Generation Firewalls 

 AIOps for NGFW 

 Cloud Management for NGFWs 

 Firewalls 

 PAN-OS 

 Panorama 

 VM-Series 

 SASE 

 Prisma Access 

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

 Security Policy 

 Visibility & Monitoring 

 Dashboards 

 Incidents and Alerts 

 Reports 

 CLI 

 10.1 

 11.0 

 Network Security 

 PAN-OS 

 10.2 

 WF-500-B Appliance 

 Advanced Wildfire 

 WF-500 Appliance 

 Appliance 

 9.1 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

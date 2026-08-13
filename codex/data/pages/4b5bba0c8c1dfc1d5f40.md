---
url: https://docs.paloaltonetworks.com/advanced-wildfire/wildfire-appliance/use-the-wildfire-appliance-cli/wildfire-appliance-operational-mode-command-reference/request-wildfire-sample-redistribution
fetched_at: 2026-08-13T15:21:37Z
source: palo-alto-main
---

# request wildfire sample redistribution Clear

request wildfire sample redistribution 

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

 request wildfire sample redistribution 

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

 request wildfire sample redistribution 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 Advanced WildFire Powered by Precision AI™ 

 request wildfire sample redistribution 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Advanced WildFire 

 Administration 

 Appliance 

 Previous 

 request system raid 

 Next 

 request system wildfire-vm-image 

 request wildfire sample redistribution 

 Description 

 Redistribute samples
from the local WildFire appliance cluster node to another cluster
node while optionally retaining samples on the local node. 

 Hierarchy Location 

 request system 

 Syntax 

 request { 
wildfire { 
sample { 
redistribution { 
  keep-local-copy {no | yes}; 
  serial-number <value>; 
} 
} 
} 
} 

 Options 

 * keep-local-copy —Keep
or do not keep a copy of the redistributed samples on the local
WildFire appliance node. 

 * serial-number —Serial
number of the node to which you redistribute samples. 

 Sample Output 

 Storage Nodes displays
the other node to which the local node redistributes samples. If
the local node is not redistributing samples, only one storage node
location displays. If the local node is redistributing samples, Storage
Nodes shows two storage node locations. The highlighted
output shows the two storage nodes that store samples (the local
node and the node to which the local node redistributes samples)
and verifies that sample redistribution is occurring. 

 admin@WF-500> show wildfire global sample-analysis 
Last Created 100 Malicious Samples 
+----------------------------------------------------------------------+ 
| SHA256 | Finish Date | Create Date | Malicious | 
+----------------------------------------------------------------------+ 
| <HASH VALUE> | 2017-03-24 17:27:40 | 2017-03-24 15:41:47 | Yes | 
| <HASH VALUE> | 2017-03-24 17:26:46 | 2017-03-24 15:41:45 | Yes | 
| <HASH VALUE> | 2017-03-24 17:26:54 | 2017-03-24 15:41:45 | Yes | 
| <HASH VALUE> | 2017-03-24 17:25:12 | 2017-03-24 15:41:44 | Yes | 
| <HASH VALUE> | 2017-03-24 17:24:28 | 2017-03-24 15:41:44 | Yes | 
| <HASH VALUE> | 2017-03-24 17:23:58 | 2017-03-24 15:41:44 | Yes | 
| <HASH VALUE> | 2017-03-24 17:26:52 | 2017-03-24 14:55:23 | Yes | 
| <HASH VALUE> | 2017-03-24 17:23:32 | 2017-03-24 14:55:23 | Yes | 
| <HASH VALUE> | 2017-03-24 17:24:58 | 2017-03-24 14:55:23 | Yes | 
| <HASH VALUE> | 2017-03-24 17:22:02 | 2017-03-24 14:55:23 | Yes | 
+----------------------------------------------------------------------+ 

+--------------------------------------------------------------------+ 
| Storage Nodes | Analysis Nodes | Status | File Type | 
+--------------------------------------------------------------------+ 
| 0907:ld2_2,065:ld2_2 | qa116 | Notify Finish | Java JAR | 
| 0097:ld2_2,004:ld2_2 | qa117 | Notify Finish | Java Class | 
| 0524:ld2_2,006:ld2_2 | qa117 | Notify Finish | Java Class | 
| 0656:ld2_2,524:ld2_2 | qa117 | Notify Finish | Java Class | 
| 0024:ld2_2,056:ld2_2 | qa117 | Notify Finish | DLL | 
| 0324:ld2_2,006:ld2_2 | qa117 | Notify Finish | Java JAR | 
| 0682:ld2_2,006:ld2_2 | qa116 | Notify Finish | Java JAR | 
| 0092:ld2_2,016:ld2_2 | qa116 | Notify Finish | DLL | 
| 0682:ld2_2,002:ld2_2 | qa116 | Notify Finish | DLL | 
| 0056:ld2_2,824:ld2_2 | qa117 | Notify Finish | DLL | 
+--------------------------------------------------------------------* 
lines 1-10 

 Required Privilege Level 

 superuser, deviceadmin 

 Previous 

 request system raid 

 Next 

 request system wildfire-vm-image 

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

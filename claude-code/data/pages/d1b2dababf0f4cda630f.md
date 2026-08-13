---
url: https://docs.paloaltonetworks.com/advanced-wildfire/wildfire-appliance/use-the-wildfire-appliance-cli/wildfire-appliance-operational-mode-command-reference/show-cluster-data-migration-status
fetched_at: 2026-08-13T15:21:44Z
source: palo-alto-main
---

# show cluster data migration status Clear

show cluster data migration status 

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

 show cluster data migration status 

 Updated on 

 Mar 2, 2026 

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

 Mar 2, 2026 

 Focus 

 Home 

 Advanced WildFire Powered by Precision AI™ 

 Use the WildFire Appliance CLI 

 WildFire Appliance Operational Mode Command Reference 

 show cluster data migration status 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 Advanced WildFire Powered by Precision AI™ 

 show cluster data migration status 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Advanced WildFire 

 Administration 

 Appliance 

 Previous 

 show cluster controller 

 Next 

 show cluster membership 

 show cluster data migration status 

 Description 

 Use this command
from a WildFire appliance cluster controller node to display the
current data migration status. The command displays when data migration
was initiated and it’s progress. When data migration finishes the
command displays the completion time stamp. If the data migration fails,
the status will display 0% completed . 

 Hierarchy Location 

 show cluster 

 Syntax 

 data-migration-status; 

 Options 

 No additional options. 

 Sample Output 

 adminWF-500(active-controller)>
 show
 cluster data-migration-status 
 100% completed on Mon Sep 9 21:44:48 PDT 2019 

 Required Privilege Level 

 superuser, deviceadmin 

 Previous 

 show cluster controller 

 Next 

 show cluster membership 

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

---
url: https://docs.paloaltonetworks.com/fedramp/autonomous-dem/first-look-at-adem-in-pa/experience-score
fetched_at: 2026-08-13T16:32:33Z
source: palo-alto-main
---

# Experience Score Clear

Experience Score 

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

 Experience Score 

 Updated on 

 Wed Sep 04 15:52:49 PDT 2024 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 FedRAMP Docs 

 Reference 

 Autonomous DEM 

 Updated on 

 Wed Sep 04 15:52:49 PDT 2024 

 Focus 

 Home 

 FedRAMP 

 First Look at Autonomous DEM Dashboards 

 Experience Score 

 Download PDF 

 FedRAMP 

 Experience Score 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 FedRAMP Docs 

 Reference 

 Autonomous DEM 

 Previous 

 First Look at Autonomous DEM Dashboards 

 Next 

 Time Range Filter 

 Experience Score 

 Learn about the Autonomous DEM experience score. 

 Where Can I Use This? What Do I Need? 

 Prisma Access (Managed by Strata Cloud Manager) 

 Prisma Access (Managed by Panorama) 

 Strata Cloud Manager 

 Prisma Access license 

 Autonomous DEM license 

 The Experience Score is the weighted average
of end-to-end application performance metrics for all monitored
applications across all users or remote sites. A fair or poor experience
score lets you know right away that there are performance issues
impacting a large number of your users or remote sites. However,
because the experience score is weighted, it may not uncover performance
issues in monitored apps or locations that have a smaller number
of users. 

 The experience score will also give you an indication of the
overall digital experience for the user. For each application that
is monitored per mobile user, ADEM calculates a score based on the
5 critical metrics - application availability, DNS resolution time,
TCP connect time, SSL connect time, and the HTTP latency. If the
application fails the availability test (application is unavailable),
then the experience score is 0. If the application is reachable,
only then the remaining four metrics will be calculated. Each of
the above metrics (other than application reachability) have a different
weightage and baselined lower and upper thresholds, and their combined weightage
equals 100. The sum of these individual metric scores determines
the application experience score for a user. An average of all the
test sample results for each application determines the experience
score of a user. 

 Experience scores are color coded in widgets as follows: 

 Good (green) - experience score >=70 

 Fair (orange) - experience score is 69-30 

 Poor (red) - experience score is <30 

 For information on how experience score is calculated for remote
sites, refer to Calculating Experience Score for Remote Sites . 

 Previous 

 First Look at Autonomous DEM Dashboards 

 Next 

 Time Range Filter 

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

 SASE 

 Prisma Access 

 Strata Multitenant Cloud Manager 

 Prisma Access Monitoring and Visibility 

 Prisma SD-WAN 

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

 Remote Networks 

 Mobile Users 

 Autonomous DEM 

 SASE 

 Prisma SASE 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

---
url: https://docs.paloaltonetworks.com/advanced-wildfire/wildfire-appliance/monitor-wildfire-appliance-activity/use-the-wildfire-appliance-to-monitor-samples/view-wildfire-sample-analysis-processing-details
fetched_at: 2026-08-13T15:19:53Z
source: palo-alto-main
---

# View WildFire Sample Analysis Processing Details Clear

View WildFire Sample Analysis Processing Details 

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

 View WildFire Sample Analysis Processing Details 

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

 Monitor WildFire Appliance Activity 

 Use the WildFire Appliance to Monitor Sample Analysis Status 

 View WildFire Sample Analysis Processing Details 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 Advanced WildFire Powered by Precision AI™ 

 View WildFire Sample Analysis Processing Details 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Advanced WildFire 

 Administration 

 Appliance 

 Previous 

 View WildFire Analysis Environment Utilization 

 Next 

 Use the WildFire CLI to Monitor the WildFire Appliance 

 View WildFire Sample Analysis Processing Details 

 Where Can I Use
This? What Do I Need? 

 WildFire Appliance 

 WildFire License 

 The WildFire appliance retains records of analysis
activity within an event log. You can view details about which connected
services or appliances in your network analyzed a particular sample,
as well as how many samples were analyzed in a given time-frame.
You can use this information to monitor activity and develop policies and
countermeasures against malicious activity. Unusually heavy activity
can indicate suspicious activity. Also consider using a threat intelligence
tool such as AutoFocus to investigate and determine the nature of
a threat. 

 View the number of samples processed locally within
a specified timespan or based on a maximum number of samples. 

 show wildfire local sample-processed {time [last-12-hrs| last-15-minutes | last-1-hr | last-24-hrs | last-30-days | last-7-days| last-calender-day | last-calender-month] \ count <number_of_samples>} . 

 Latest samples information:
+------------------------------------------------------------------+---------------------+-----------+------------+-----------+------------+-------------------+
| SHA256 | Create Time | File Name | File Type | File Size | Malicious | Status |
+------------------------------------------------------------------+---------------------+-----------+------------+-----------+------------+-------------------+
| ce752b7b76ac2012bdff2b76b6c6af18e132ae8113172028b9e02c6647ee19bb | 2018-12-09 16:55:53 | | Email Link | 31,522 | | download complete |
| 349e57e51e7407abcd6eccda81c8015298ff5d5ba4cedf09c7353c133ceaa74b | 2018-12-09 16:53:40 | | Email Link | 39,679 | | download complete |
+------------------------------------------------------------------+---------------------+-----------+------------+-----------+------------+-------------------+ 

 Identify the device(s) that submitted a specified sample
for WildFire analysis. 

 show wildfire global sample-device-lookup sha256equal <SHA_256> . 

Sample 1024609813c57fe174722c53b3167dc3cf5583d5c7abaf4a95f561c686a2116e last seen on following devices:
+------------------------------------------------------------------+-----------+-----------+---------------------+
| SHA256 | Device ID | Device IP | Submitted Time |
+------------------------------------------------------------------+-----------+-----------+---------------------+
| 1024609813c57fe174722c53b3167dc3cf5583d5c7abaf4a95f561c686a2116e | Manual | Manual | 2019-08-05 19:24:39 |
+------------------------------------------------------------------+-----------+-----------+---------------------+

 Previous 

 View WildFire Analysis Environment Utilization 

 Next 

 Use the WildFire CLI to Monitor the WildFire Appliance 

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

 11.0 

 Network Security 

 PAN-OS 

 Advanced Wildfire 

 Appliance 

 9.1 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

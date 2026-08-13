---
url: https://docs.paloaltonetworks.com/advanced-wildfire/wildfire-appliance/use-the-wildfire-appliance-cli/wildfire-appliance-operational-mode-command-reference/show-wildfire-local
fetched_at: 2026-08-13T15:21:56Z
source: palo-alto-main
---

# show wildfire local Clear

show wildfire local 

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

 show wildfire local 

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

 show wildfire local 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 Advanced WildFire Powered by Precision AI™ 

 show wildfire local 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Advanced WildFire 

 Administration 

 Appliance 

 Previous 

 show wildfire global 

 Next 

 test wildfire registration 

 show wildfire local 

 Description 

 Shows various information
about local devices and samples, activity, recent samples that the
appliance analyzed, and basic WildFire statistics. 

 Hierarchy Location 

 show wildfire local 

 Syntax 

 latest { 
 analysis { 
 filter malicious|benign; 
 sort-by SHA256|Submit Time|Start Time|Finish Time|Malicious|Status; 
 sort-direction asc|desc; 
 limit 1-20000; 
 days 1-7; 
 } 
 OR... 
samples { 
 filter malicious|benign; 
 sort-by SHA256|Create Time|File Name|File Type|File Size|Malicious|Status; 
 sort-direction asc|desc; 
 limit 1-20000; 
 days 1-7; 
 } 
sample-processed { 
 count 1-1000;
 time {last-1-hr|last-12-hrs|last-15-minutes|last-24-hrs|last-30-days|last-7-days|last-calender-day|last-calender-month; 
} 
sample-status { 
 sha256 { 
 equal <value>; 
} 
} 
statistics days <1-31> | hours <0-24> | minutes <0-60>; 
} 

 Options 

 > latest —
Show latest 30 activities, which include the last 30 analysis activities,
the last 30 files that were analyzed, network session information
on files that were analyzed and files that were uploaded to the
public cloud server. 

 > sample-processed —
Shows the number of samples processed locally within a specified
timespan or maximum number of samples. 

 > sample-status —
Show wildfire sample status. Enter the SHA256 value of the file
to view the current analysis status. 

 > statistics —
Display basic wildfire statistics. 

 Sample Output 

 The following shows the
output for this command. 

 admin@WF-500> show
wildfire latest analysis 
Latest analysis information: 
+-------------+---------------------+---------------------+---------------------+ 
| SHA256 | Submit Time | Start Time | Finish Time | 
+-------------+---------------------+---------------------+---------------------+ 
| <HASH VALUE>| 2017-03-01 14:28:26 | 2017-03-01 14:28:26 | 2017-03-01 14:34:24 | 
| <HASH VALUE>| 2017-03-01 14:28:25 | 2017-03-01 14:28:25 | 2017-03-01 14:28:41 | 
| <HASH VALUE>| 2017-03-01 14:28:25 | 2017-03-01 14:28:25 | 2017-03-01 14:28:26 | 
+-------------+---------------------+---------------------+---------------------+ 
+------------+-----------------------------------------------------------+-----------+ 
| Malicious | VM Image | Status | 
+------------+-----------------------------------------------------------+-----------+ 
| Yes | Windows 7 x64 SP1, Adobe Reader 11, Flash 11, Office 2010 | completed | 
| No | Java/Jar Static Analyzer | completed | 
| Suspicious | Java/Jar Static Analyzer | completed | 
+------------+-----------------------------------------------------------+-----------+ 

admin@WF-500> show wildfire local latest samples 

Latest samples information: 
+--------------+---------------------+----------------+---------------+ 
| SHA256 | Create Time | File Name | File Type | 
+--------------+---------------------+----------------+---------------+ 
| <HASH VALUE> | 2017-03-01 14:28:25 | | JAVA Class | 
| <HASH VALUE> | 2017-03-01 14:28:25 | | JAVA Class | 
| <HASH VALUE> | 2017-03-01 14:28:25 | | PE | 
+--------------+---------------------+----------------+---------------+ 
+--------------+-----------+-------------------+ 
| File Size | Malicious | Status | 
+--------------+-----------+-------------------+ 
| 20,407 | No | analysis complete | 
| 1,584 | Yes | analysis complete | 
| 259,024 | No | analysis complete | 
+--------------+-----------+-------------------+ 

admin@WF-500> show wildfire local sample-processed count
2 

Time Window: last-15-minutes
Display Count: 2:
+------------------------------------------------------------------+---------------------+-----------+------------+-----------+------------+-------------------+
| SHA256 | Create Time | File Name | File Type | File Size | Malicious | Status |
+------------------------------------------------------------------+---------------------+-----------+------------+-----------+------------+-------------------+
| ce752b7b76ac2012bdff2b76b6c6af18e132ae8113172028b9e02c6647ee19bb | 2018-12-09 16:55:53 | | Email Link | 31,522 | | download complete |
| 349e57e51e7407abcd6eccda81c8015298ff5d5ba4cedf09c7353c133ceaa74b | 2018-12-09 16:53:40 | | Email Link | 39,679 | | download complete |
+------------------------------------------------------------------+---------------------+-----------+------------+-----------+------------+-------------------+

admin@WF-500> show wildfire local sample-status sha256
equal 0f2114010d00d7fa453177de93abca9643f4660457536114898c56149f819a9b 

Sample information: 
+---------------------+-----------+-----------------------------------+ 
| Create Time | File Name | File Type | 
+---------------------+-----------+-----------------------------------+ 
| 2017-03-01 22:28:24 | rmr.doc | Microsoft Word 97 - 2003 Document | 
+---------------------+-----------+-----------------------------------+ 
+-----------+-----------+-------------------+ 
| File Size | Malicious | Status | 
+-----------+-----------+-------------------+ 
| 133120 | Yes | analysis complete | 
+-----------+-----------+-------------------+ 
Analysis information: 
+---------------------+---------------------+---------------------+------------+ 
| Submit Time | Start Time | Finish Time | Malicious | 
+---------------------+---------------------+---------------------+------------+ 
| 2017-03-01 22:28:24 | 2017-03-01 22:28:24 | 2017-03-01 22:28:24 | Suspicious | 
| 2017-03-01 22:28:24 | 2017-03-01 22:28:24 | 2017-03-01 22:34:07 | Yes | 
+---------------------+---------------------+---------------------+------------+ 
+-----------------------------------------------------------+-----------+ 
| VM Image | Status | 
+-----------------------------------------------------------+-----------+ 
| DOC/CDF Static Analyzer | completed | 
| Windows 7 x64 SP1, Adobe Reader 11, Flash 11, Office 2010 | completed | 
+-----------------------------------------------------------+-----------+ 

admin@WF-500> show wildfire local statistics 

Current Time: 2017-03-01 17:44:31 
Received After: 2017-02-28 17:44:31 
Received Before: 2017-03-01 17:44:31 

------------------------------------------------------------------------------------- 
| Wildfire Stats | 
+-----------------------------------------------------------------------------------+ 
|+----------------------------------------------------------------------------------+| 
|| Executable || 
|+---------------------------------------------------------------------------------+| 
|| FileType | Submitted | Analyzed | Pending | Malware | Grayware | Benign | Error || 
|+---------------------------------------------------------------------------------+| 
|| exe | 2 | 2 | 0 | 0 | 0 | 2 | 0 || 
|+---------------------------------------------------------------------------------+| 
|| dll | 0 | 0 | 0 | 0 | 0 | 0 | 0 || 
|+---------------------------------------------------------------------------------+| 

Environment Analysis Summary for Executable: 
VM Utilization : 0/10 
Files Analyzed : 2 

+-----------------------------------------------------------------------------------+ 
|| Non-Executable || 
|+---------------------------------------------------------------------------------+| 
|| FileType | Submitted | Analyzed | Pending | Malware | Grayware | Benign | Error || 
|+---------------------------------------------------------------------------------+| 
|| pdf | 0 | 0 | 0 | 0 | 0 | 0 | 0 || 
|+---------------------------------------------------------------------------------+| 
|| jar | 0 | 0 | 0 | 0 | 0 | 0 | 0 || 
|+---------------------------------------------------------------------------------+| 
|| doc | 1 | 1 | 0 | 1 | 0 | 0 | 0 || 
|+---------------------------------------------------------------------------------+| 
|| ppt | 0 | 0 | 0 | 0 | 0 | 0 | 0 || 
|+---------------------------------------------------------------------------------+| 
|| xls | 0 | 0 | 0 | 0 | 0 | 0 | 0 || 
|+---------------------------------------------------------------------------------+| 
|| docx | 0 | 0 | 0 | 0 | 0 | 0 | 0 || 
|+---------------------------------------------------------------------------------+| 
|| pptx | 0 | 0 | 0 | 0 | 0 | 0 | 0 || 
|+---------------------------------------------------------------------------------+| 
|| xlsx | 0 | 0 | 0 | 0 | 0 | 0 | 0 || 
|+---------------------------------------------------------------------------------+| 
|| rtf | 0 | 0 | 0 | 0 | 0 | 0 | 0 || 
|+---------------------------------------------------------------------------------+| 
|| class | 2 | 2 | 0 | 1 | 0 | 1 | 0 || 
|+---------------------------------------------------------------------------------+| 
|| swf | 1 | 1 | 0 | 0 | 0 | 1 | 0 || 
|+---------------------------------------------------------------------------------+| 

Environment Analysis Summary for Non-Executable: 
VM Utilization : 0/16 
Files Analyzed : 4 

+-----------------------------------------------------------------------------------+ 
|| Links || 
|+---------------------------------------------------------------------------------+| 
|| FileType | Submitted | Analyzed | Pending | Malware | Grayware | Benign | Error || 
|+---------------------------------------------------------------------------------+| 
|| elink | 1 | 1 | 0 | 1 | 0 | 0 | 0 || 
|+---------------------------------------------------------------------------------+| 

Environment Analysis Summary for Links: 
Files Analyzed : 1 

---------------------------------------------------------- 
| General Stats | 
+--------------------------------------------------------+ 

Total Disk Usage: 67/1283(GB) (5%) 

||+--------------------------+-----------+-+-----------+|| 
||| Sample Queue ||| 
||+-----------------+-------------------+--------------+|| 
||| SUBMITTED | ANALYZED | PENDING ||| 
||+--------------------------+-----------+-+-----------+|| 
||| 7 | 7 | 0 ||| 
||+--------------------------+-----------+-+----------+||| 

|+---------------------------+--------------------------+| 
||| Verdicts ||| 
||+--------------------------+-------------------------+|| 
||| Malware | Grayware | Benign | Error ||| 
||+-----------------------------+----------------------+|| 
||| 3 | 0 | 4 | 0 ||| 
||+--------------------------+-----------+-+----------+||| 

|+---------------------------+--------------------------+| 
||| Session and Upload Count ||| 
||+--------------------------+-------------------------+|| 
||| Sessions | Uploads ||| 
||+--------------------------+-------------------------+|| 
||| 7 | 5 ||| 
||+--------------------------+-------------------------+|| 

 Required Privilege Level 

 superuser, superreader 

 Previous 

 show wildfire global 

 Next 

 test wildfire registration 

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

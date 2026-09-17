---
url: https://docs.paloaltonetworks.com/prisma-sd-wan/ion-cli-reference/use-cli-commands/dump-commands/dump-user-summary
fetched_at: 2026-09-16T07:48:38Z
source: strata-and-sase
---

# dump user-id summary Clear

Updated on 

 Tue Jun 02 09:34:24 PDT 2026 

 Focus 

 Home 

 Prisma SD-WAN 

 Use CLI Commands 

 Dump Commands 

 dump user-id summary 

 Download PDF 

 Prisma SD-WAN 

 dump user-id summary 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma SD-WAN Docs 

 Activation & Onboarding 

 Administration 

 CloudBlades 

 Select a Document 

 CloudBlade Integrations 

 CloudBlades Integration with Prisma Access 

 Deployment 

 Incidents & Alerts 

 Reference 

 Release Notes 

 Select a Document 

 ION 6.8 

 ION 6.6 

 ION 6.5 

 ION 6.4 

 ION 6.3 

 ION 6.1 

 ION 5.6 

 Prisma SD-WAN Controller 

 Prisma SD-WAN On-Premises Controller 

 Prisma SD-WAN CloudBlades 

 Prisma Access CloudBlade Cloud Managed 

 Prisma Access CloudBlade Panorama Managed 

 New Features 

 Previous 

 dump user-id status 

 Next 

 dump user-id useridx 

 dump user-id summary 

 Use the dump user-id summary command to display the number of
 users, groups, IP address to user mapping, and user-group mapping learnt from the
 controller. 

 Command 

 dump user-id summmary 

 Options 

 None 

 Command Notes 

 Role Super, Read Only, Monitor 

 Related Commands — 

 Introduced in Release 6.2.1 

 Example 

 dump user-id summary
Number of IP User Mappings: 4
IP Address: 10.1.1.2
UserIndex: 15862297924230219
UserName: user/madhu
Expire Time: 2022-09-23 07:39:16 +0000 UTC
User Groups:
 GroupIndex : 158622979242302240 GroupName : engineering
 GroupIndex : 158622979242302242 GroupName : employees

IP Address: 10.1.1.5
UserIndex: 15862297924230222
UserName: user/bob
Expire Time: 2022-09-23 07:39:16 +0000 UTC
User Groups:
 GroupIndex : 158622979242302242 GroupName : employees

IP Address: 10.1.1.3
UserIndex: 15862297924230220
UserName: user/ravi
Expire Time: 2022-09-23 07:39:16 +0000 UTC
User Groups:
 GroupIndex : 158622979242302240 GroupName : engineering
 GroupIndex : 158622979242302241 GroupName : sales

IP Address: 10.1.1.4
UserIndex: 15862297924230221
UserName: user/alice
Expire Time: 2022-09-23 07:39:16 +0000 UTC
User Groups:
 GroupIndex : 158622979242302242 GroupName : employees 

 Previous 

 dump user-id status 

 Next 

 dump user-id useridx

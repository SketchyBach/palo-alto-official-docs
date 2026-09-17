---
url: https://docs.paloaltonetworks.com/prisma-sd-wan/ion-cli-reference/use-cli-commands/dump-commands/dump-time-status
fetched_at: 2026-09-16T07:48:37Z
source: strata-and-sase
---

# dump time status Clear

Updated on 

 Tue Jun 02 09:34:24 PDT 2026 

 Focus 

 Home 

 Prisma SD-WAN 

 Use CLI Commands 

 Dump Commands 

 dump time status 

 Download PDF 

 Prisma SD-WAN 

 dump time status 

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

 dump time log 

 Next 

 dump troubleshoot message 

 dump time status 

 Use the dump time status command
to display the latest information from time sources.Information
displayed includes: 

 Current time—Displays system time
on the device. 

 Current drift—Displays system time adjustment specified by
the importance of being ahead or behind, according to time sync
information. 

 Server—Displays either a configured NTP server or the controller
time source (CTS). 

 Polled—Displays the time when sent the last request to a
time server. 

 Error—Displays the latest error obtained on contacting the
server. 

 Selected—Displays the last time this server was the first
to answer when selected it. 

 Delta—Displays the difference in time of the system and the
time server along with the margin of error. 

 Address—Displays the address of the selected server. 

 Stratum—Displays the stratum of the time server. 

 Action—Displays the action taken; drift means slow or speeds
up the system clock, a jump means change immediately. 

 Command 

 dump time status

 Options 

 None 

 Command Notes 

 Role Super, Read Only, Monitor 

 Related Commands 

 dump time config 

 Introduced in Release 4.7.1 

 Example 

 dump time status
 Current Time 2018-03-05 17:31:12.726938694 +0000 UTC
 Current Drift -15.682
 Server Event
 time.nist.gov polled 13m4s ago
 selected 13m4s ago
 delta -15.680±10.454
 address 132.163.97.1
 stratum 1
 action drift -15.680
 CTS polled 1.939s ago
 selected 1.939s ago
 delta -15.683±1.154
 action drift -15.683 

 Previous 

 dump time log 

 Next 

 dump troubleshoot message

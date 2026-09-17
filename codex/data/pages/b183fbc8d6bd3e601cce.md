---
url: https://docs.paloaltonetworks.com/prisma-sd-wan/ion-cli-reference/use-cli-commands/inspect-commands/inspect-ipfix-interface-info
fetched_at: 2026-09-16T07:48:41Z
source: strata-and-sase
---

# inspect ipfix interface-info Clear

Updated on 

 Tue Jun 02 09:34:24 PDT 2026 

 Focus 

 Home 

 Prisma SD-WAN 

 Use CLI Commands 

 Inspect Commands 

 inspect ipfix interface-info 

 Download PDF 

 Prisma SD-WAN 

 inspect ipfix interface-info 

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

 inspect ipfix wan-path-info 

 Next 

 inspect ip-rules 

 inspect ipfix interface-info 

 Use the inspect ipfix interface-info command
to present mapping information for all interfaces and view the collector
context attached to an interface. 

 Command 

 inspect ipfix interface-info 

 Options 

 None 

 Command Notes 

 Role Super, Read Only 

 Related Commands — 

 Introduced in Release 5.5.1 

 Example 

 Interface ID Interface Name Device SNMP Index IPFIX Context ID (Type) IPFIX Context Name
 -------------------- ------------------------- ---------------- ---------- ------------------------ --------------------------------
 15759796305670035 23.123 eth2.123 21
 15670679352910161 9 eth9 11
 15670679351650126 3 eth3 5
 15734532300070135 BVI-1 vi2 19 16097351040390067 (F) Filter-115670679353260189 2 eth2 415670679352040140 1 eth1 3 16097350669480033 (C) CC-1 16097370807850021 (F) FILTER CONTEXT OVERRIDE
 15670679352470147 6 eth6 8
 15761299727860133 89.1113 eth8.1113 20
 15670679353020168 4 eth4 6 16097617291090212 (C)15670679351940133 8 eth8 10
 15670679353080175 5 eth5 7
 15670679352830154 controller 1 eth0 2
 15670679353130182 7 eth7 9
 INTERFACES Flow Field Option : false
 SNMP agent is running 

 Previous 

 inspect ipfix wan-path-info 

 Next 

 inspect ip-rules

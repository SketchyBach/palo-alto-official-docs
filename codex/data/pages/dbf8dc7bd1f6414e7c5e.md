---
url: https://docs.paloaltonetworks.com/prisma-sd-wan/ion-cli-reference/use-cli-commands/inspect-commands/inspect-app-l4-prefix-lookup
fetched_at: 2026-09-16T07:48:39Z
source: strata-and-sase
---

# inspect app-l4-prefix lookup Clear

Updated on 

 Tue Jun 02 09:34:24 PDT 2026 

 Focus 

 Home 

 Prisma SD-WAN 

 Use CLI Commands 

 Inspect Commands 

 inspect app-l4-prefix lookup 

 Download PDF 

 Prisma SD-WAN 

 inspect app-l4-prefix lookup 

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

 inspect app-flow-table 

 Next 

 inspect app-map 

 inspect app-l4-prefix lookup 

 Use the inspect app-l4-prefix lookup command
to identify lookup on a given destination address in TCPPROXY L4-Prefix-Lookup
table and also configures at the device level. 

 Command 

 inspect app-l4-prefix lookup dstv4=192.168.20.100 dstport=805 protocol= [ protocol=tcp|udp|ip ] 

 Options 

 tcp Enter tcp to look up a given destination address
in TCP L4-Prefix-Lookup table. 

 udp Enter udp to look up a given destination address
in UDP L4-Prefix-Lookup table. 

 ip Enter ip to look up a given destination address
in non-TCP-UDP L4-Prefix-Lookup table. 

 Command Notes 

 Role Super, Read Only 

 Related Commands — 

 Introduced in Release 5.4.1 

 Example 

 inspect app-l4-prefix lookup dstv4=192.168.20.100 dstport=907protocol=udp
 {
 "App Found": "ring-central3",
 "App ID": 3888,
 "dscp": 0,
 "App Name": "ring-central3",
 "Order Number": 32768
 }

 inspect app-l4-prefix lookup dstv4=192.168.20.100 dstport=907protocol=tcp
 {
 "App Found": "disk",
 "App ID": 65,
 "dscp": 0,
 "App Name": "disk",
 "Order Number": 32768
 }

 inspect app-l4-prefix lookup dstv4=192.168.20.100 dstport=907protocol=tcp
 {
 "App NOT Found": []
 } 

 Previous 

 inspect app-flow-table 

 Next 

 inspect app-map

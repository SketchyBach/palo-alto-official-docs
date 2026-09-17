---
url: https://docs.paloaltonetworks.com/prisma-sd-wan/ion-cli-reference/use-cli-commands/clear-commands/clear-connection
fetched_at: 2026-09-16T07:48:16Z
source: strata-and-sase
---

# clear connection Clear

Updated on 

 Tue Jun 02 09:34:24 PDT 2026 

 Focus 

 Home 

 Prisma SD-WAN 

 Use CLI Commands 

 Clear Commands 

 clear connection 

 Download PDF 

 Prisma SD-WAN 

 clear connection 

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

 clear app-probe prefix 

 Next 

 clear device account-login 

 clear connection 

 Use the clear connection command
to clear the established connections that match user-specified options. 

 Command 

 clear connection (all | srcv4=src-ipv4 | destv4=dst-ipv4 | ) | | srcport=src-port |dstport=dst-port | proto= ( udp | tcp | icmp | other ) 

 Options 

 srcv4 Enter the source IP address to clear the established connections
that match the specified source IP address. 

 dstv4 Enter the destination IP address to clear the established
connections that match the specified destination IP address. 

 srcport Enter the source port to clear the established connections
that match the specified source port. 

 dstport Enter the destination port to clear the established connections
that match the specified destination port. 

 prot Tab to select UDP, TCP, or ICMP. Or, enter
a protocol number ranging from 0 - 255. 

 Command Notes 

 Role Super 

 Related Commands — 

 Introduced in Release 5.0.1 

 Example 

 clear connection proto=udp
 This will be Service impacting for the matching connections areyou sure? [Y|N]:Y
 PROTO TIME OUT SRC DST SPORT DPORT t-src t-dst tsport tdport
 udp 29 10.24.18.209 8.8.8.8 38382 53 10.24.18.209 8.8.8.8 38382 53
 udp 29 10.24.18.202 8.8.8.8 37516 53 10.24.18.202 8.8.8.8 37516 53 

 Previous 

 clear app-probe prefix 

 Next 

 clear device account-login

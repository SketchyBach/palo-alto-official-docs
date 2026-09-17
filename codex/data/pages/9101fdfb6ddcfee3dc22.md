---
url: https://docs.paloaltonetworks.com/prisma-sd-wan/ion-cli-reference/use-cli-commands/inspect-commands/inspect-servicelink-connection
fetched_at: 2026-09-16T07:48:44Z
source: strata-and-sase
---

# inspect servicelink conn Clear

Updated on 

 Tue Jun 02 09:34:24 PDT 2026 

 Focus 

 Home 

 Prisma SD-WAN 

 Use CLI Commands 

 Inspect Commands 

 inspect servicelink conn 

 Download PDF 

 Prisma SD-WAN 

 inspect servicelink conn 

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

 inspect servicelink conn 

 Use the inspect servicelink conn command to inspect the active VPN
 connections. Information includes the authentication selected, Internet Key Exchange
 (IKE) protocol details, and Dead Peer Detection (DPD) details. 

 Command 

 inspect servicelink conn ( all | sldev= | slname= ) 

 Options 

 all Enter all to view all the active VPN connections for
 a device. 

 sldev Enter the VPN ID to view the parameters for a
 specific active VPN. 

 slname Enter the VPN interface name to view the parameters
 for a specific active VPN. 

 Command Notes 

 Role Super, Read Only 

 Related Commands — 

 Introduced in Release 6.5.1 

 Example 

 inspect servicelink conn all
sl2: IKEv2, reauthentication every 86400s, rekeying every 86400s, dpd delay 1s
 local: 10.65.27.23
 remote: 10.65.27.43
 local pre-shared key authentication:
 id: 10.65.27.23
 remote pre-shared key authentication:
 id: %any
 sl2childsa: TUNNEL, rekeying every 27900s, dpd action is start
 local: 0.0.0.0/0
 remote: 0.0.0.0/0
sl1: IKEv2, no reauthentication, rekeying every 86400s, dpd delay 1s
 local: 10.65.27.23
 remote: 10.65.27.44
 local pre-shared key authentication:
 id: 10.65.27.23
 remote pre-shared key authentication:
 id: %any
 sl1childsa: TUNNEL, rekeying every 27900s, dpd action is start
 local: 0.0.0.0/0
 remote: 0.0.0.0/0

 inspect servicelink conn sldev=sl1
sl1: IKEv2, no reauthentication, rekeying every 86400s, dpd delay 1s
 local: 10.65.27.23
 remote: 10.65.27.44
 local pre-shared key authentication:
 id: 10.65.27.23
 remote pre-shared key authentication:
 id: %any
 sl1childsa: TUNNEL, rekeying every 27900s, dpd action is start
 local: 0.0.0.0/0
 remote: 0.0.0.0/0 

 inspect servicelink conn slname=ToSV2
sl1: IKEv2, no reauthentication, rekeying every 86400s, dpd delay 1s
 local: 10.65.27.23
 remote: 10.65.27.44
 local pre-shared key authentication:
 id: 10.65.27.23
 remote pre-shared key authentication:
 id: %any
 sl1childsa: TUNNEL, rekeying every 27900s, dpd action is start
 local: 0.0.0.0/0
 remote: 0.0.0.0/0

---
url: https://docs.paloaltonetworks.com/prisma-sd-wan/ion-cli-reference/use-cli-commands/dump-commands/dump-lldp
fetched_at: 2026-09-16T07:48:25Z
source: strata-and-sase
---

# dump lldp Clear

Updated on 

 Jun 2, 2026 

 Focus 

 Home 

 Prisma SD-WAN 

 Use CLI Commands 

 Dump Commands 

 dump lldp 

 Download PDF 

 Prisma SD-WAN 

 dump lldp 

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

 dump ipfix config templates 

 Next 

 dump lldp config 

 dump lldp 

 Use the dump lldp command to
display the link layer discovery protocol (LLDP) and cisco discovery protocol
(CDP) messages received on physical ports. 

 Messages replace
with the new messages received on the same interface from the same
source, and they get deleted when their time to live expires. The
command output displays the interface the message was received on
the protocol type and the decoded value list. 

 There are two
entries for each interface for a bypass pair interface. These are
bridge interfaces such as a private WAN bypass pair for LAN 1 and
WAN 1 connected to a switch, and the router displays an LLDP entry
for both the controller and router when viewing output for LAN1. 

 Command 

 dump lldp [ all | interface
 interface name ]

 Options 

 all Enter all to display status for all interfaces. 

 interface Enter the interface name to display
configuration for a specific interface. 

 Command Notes 

 Role Super, Read Only, Monitor 

 Related Commands — 

 Introduced in Release 5.0.3 

 Example 

 dump lldp all
 interface : controller
 protocol : LLDP
 chassis capabilities : wlan_ap
 chassis mac : d8:cb:8a:66:6e:d7
 chassis port_descr : enp3s0
 chassis system_descr : Ubuntu 18.04 LTS Linux 4.15.0-20-generic #21-Ubuntu SMP Tue Apr 24 06:16:15 UTC 2018 x86_64
 chassis system_name : len
 port auto_negotiation : yes
 port link_aggregation : disabled
 port mac : d8:cb:8a:66:6e:d7
 port mode : 1000baseT/Full
 port modes_advertised : 1000baseT/Full, 1000baseT/Half,FdxAPause, FdxPause, 100baseTX/Full, 100baseTX/Half, 10baseT/Full, 10baseT/Half, otherinterface : controller
 protocol : CDP
 chassis capabilities : host
 chassis id : michael-bionic-vm
 chassis ios_version : Ubuntu 18.04.1 LTS Linux 4.15.0-29-generic #31-Ubuntu SMP Tue Jul 17 15:39:52 UTC 2018 x86_64
 chassis name : michael-bionic-vm
 chassis platform : Ubuntu 18.04.1 LTS Linux x86_64
 port address : 192.168.100.117
 port duplex : full
 port id : ens33
 port mtu : 1500 

 Previous 

 dump ipfix config templates 

 Next 

 dump lldp config

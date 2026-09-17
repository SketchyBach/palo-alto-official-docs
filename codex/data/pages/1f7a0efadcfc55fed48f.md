---
url: https://docs.paloaltonetworks.com/prisma-sd-wan/ion-cli-reference/use-cli-commands/inspect-commands/inspect-system-ipv6-neighbor
fetched_at: 2026-09-16T07:48:44Z
source: strata-and-sase
---

# inspect system ipv6-neighbor Clear

Updated on 

 Tue Jun 02 09:34:24 PDT 2026 

 Focus 

 Home 

 Prisma SD-WAN 

 Use CLI Commands 

 Inspect Commands 

 inspect system ipv6-neighbor 

 Download PDF 

 Prisma SD-WAN 

 inspect system ipv6-neighbor 

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

 inspect system arp 

 Next 

 inspect system vrf 

 inspect system ipv6-neighbor 

 Use the inspect system ipv6-neighbor command
to inspect all the IPv6 system neighbors. 

 Command 

 inspect system ipv6-neighbor ( all | interface
 interface-name )

 Options 

 all Enter all to inspect all system IPv6 neighbors
for a device. 

 interface Enter interface name to list the names of system
IPv6 neighbors for a device. 

 Command Notes 

 Role Super, Read Only 

 Related Commands — 

 Introduced in Release 6.0.1 

 Example 

 inspect system ipv6-neighbor all
 fe80::250:56ff:fe95:edf dev eth1 lladdr 00:50:56:95:0e:df STALE
 fe80::250:56ff:feab:42c4 dev eth2 lladdr 00:50:56:ab:42:c4 router STALE
 fe80::fcde:feff:fe28:5143 dev eth1 lladdr 00:50:56:95:0e:df router STALE
 fe80::250:56ff:fe95:db52 dev eth1 lladdr 00:50:56:95:db:52 STALE
 fe80::8c61:66ff:fe7a:f943 dev v-ppp1-p lladdr 9e:5a:9a:4d:30:9a PERMANENT
 fe80::700a:a5ff:fe6d:5d55 dev v-eth1-p lladdr ce:92:5f:14:e9:d9 PERMANENT
 2008::33 dev eth1 INCOMPLETE
 fe80::250:56ff:feab:90e5 dev eth2 lladdr 00:50:56:ab:90:e5 router STALE
 2008::55 dev eth1 INCOMPLETE
 fe80::250:56ff:fe88:e61d dev eth1 lladdr 00:50:56:88:e6:1d router STALE 

 Previous 

 inspect system arp 

 Next 

 inspect system vrf

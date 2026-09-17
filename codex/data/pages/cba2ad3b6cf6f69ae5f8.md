---
url: https://docs.paloaltonetworks.com/prisma-sd-wan/ion-cli-reference/use-cli-commands/dump-commands/dump-routing-peer-routes
fetched_at: 2026-09-16T07:48:33Z
source: strata-and-sase
---

# dump routing peer routes Clear

Updated on 

 Tue Jun 02 09:34:24 PDT 2026 

 Focus 

 Home 

 Prisma SD-WAN 

 Use CLI Commands 

 Dump Commands 

 dump routing peer routes 

 Download PDF 

 Prisma SD-WAN 

 dump routing peer routes 

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

 dump routing peer received-routes 

 Next 

 dump routing peer route-via 

 dump routing peer routes 

 Use the dump routing peer routes command
to display the installed routes learned from BGP peers. 

 Command 

 dump routing peer routes ( all | peer-ip = Peer IP | vrf-name= vrf name | address-family= (ipv4 or ipv6) ) 

 Options 

 all Enter all to display learned routes from all
BGP peers. 

 vrf-name Enter a VRF name to display the configuration for a
 specific BGP peer. Release 6.3.1 

 address-family Enter an address family to display the learned routes
 of IPv4 or IPv6 for a specific BGP peer. Release
 6.3.1 

 peer-ip Enter an IP address to display routes learned from a specific BGP peer with both IPv4 and IPv6
 address. . 

 Command Notes 

 Role Super, Read Only, Monitor 

 Related Commands — 

 Introduced in Release 5.0.1 

 Example 

 dump routing peer routes peer-ip 10.24.24.34
 BGP table version is 0, local router ID is 172.16.1.86
 Status codes: s suppressed, d damped, h history, * valid, > best,i - internal,r RIB-failure, S Stale, R Removed
 Origin codes: i - IGP, e - EGP, ? - incomplete
 Network Next Hop Metric Loc Prf Weight Path
 0.0.0.0 10.24.24.34 0 2000 65000 1111i
 10.24.24.0/29 10.24.24.34 0 2000 65000 1111
 1101?
 .
 .
 .
 192.168.168.4/30 10.24.24.34 0 2000 65000 ?

 Total number of prefixes 37 

 dump routing peer routes vrf-name=IOT-Voice 

BGP table version is 10, local router ID is 7.7.8.8, vrf id 27
Default local pref 100, local AS 1200
Status codes: s suppressed, d damped, h history, * valid, > best, = multipath,
 i internal, r RIB-failure, S Stale, R Removed
Nexthop codes: @NNN nexthop's vrf id, < announce-nh-self
Origin codes: i - IGP, e - EGP, ? - incomplete
RPKI validation codes: V valid, I invalid, N Not found

 Network Next Hop Metric LocPrf Weight Path
*> 99.9.9.0/24 7.7.8.254(vyos) 0 0 1300 i

Displayed 1 routes and 2 total paths

dump routing peer routes peer-ip 10.2.68.2 address-family=ipv6

BGP table version is 192, local router ID is 4.4.4.4, vrf id 0
Default local pref 100, local AS 2001
Status codes: s suppressed, d damped, h history, * valid, > best, = multipath,
 i internal, r RIB-failure, S Stale, R Removed
Nexthop codes: @NNN nexthop's vrf id, < announce-nh-self
Origin codes: i - IGP, e - EGP, ? - incomplete
RPKI validation codes: V valid, I invalid, N Not found
 Network Next Hop Metric LocPrf Weight Path
* 2001:10:2:68::/64
 fe80::250:56ff:fe95:2a6f(BR2L3SW)
 0 0 2002 ?
* 2001:10:2:69::/64
 fe80::250:56ff:fe95:2a6f(BR2L3SW)
 0 0 2002 ?
*> 2001:10:2:70::/64
 fe80::250:56ff:fe95:2a6f(BR2L3SW)
 0 0 2002 ?
*> 2001:10:2:72::/64
 fe80::250:56ff:fe95:2a6f(BR2L3SW)
 0 0 2002 ?
*> 3aaa:3aaa:3aaa:3aaa::/65
 fe80::250:56ff:fe95:2a6f(BR2L3SW)
 0 0 2002 ?
Displayed 5 routes and 50 total paths

 Previous 

 dump routing peer received-routes 

 Next 

 dump routing peer route-via

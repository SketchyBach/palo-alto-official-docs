---
url: https://docs.paloaltonetworks.com/prisma-sd-wan/ion-cli-reference/use-cli-commands/dump-commands/dump-routing-running-config
fetched_at: 2026-09-16T07:48:33Z
source: strata-and-sase
---

# dump routing running-config Clear

Updated on 

 Tue Jun 02 09:34:24 PDT 2026 

 Focus 

 Home 

 Prisma SD-WAN 

 Use CLI Commands 

 Dump Commands 

 dump routing running-config 

 Download PDF 

 Prisma SD-WAN 

 dump routing running-config 

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

 dump routing routemap 

 Next 

 dump routing summary 

 dump routing running-config 

 Use the dump routing running-config command
to display the current routing configuration for a device. 

 Command 

 dump routing running-config

 Options 

 None 

 Command Notes 

 Role Super, Read Only, Monitor 

 Related Commands — 

 Introduced in Release 5.0.1 

 Example 

 dump routing running-config
 Building configuration...
 Current configuration:
 !
 log syslog notifications
 log facility syslog
 bgp multiple-instance
 !
 debug zebra rib
 debug bgp
 !
 password default
 !
 interface br0
 ipv6 nd suppress-ra
 !
 ...
 router bgp 7000
 bgp router-id 172.20.75.146
 neighbor 172.120.16.8 remote-as 1234
 neighbor 172.120.16.8 description "core peer 15296501950110247"
 neighbor 172.120.16.8 advertisement-interval 1
 neighbor 172.120.16.8 timers 30 90 |
 neighbor 172.120.16.8 timers connect 120
 neighbor 172.120.16.8 soft-reconfiguration inbound
 neighbor 172.120.16.8 route-map auto-core-15296501950110247-routemap-in in
 neighbor 172.120.16.8 route-map auto-core-15296501950110247-routemap-out out
 !
 ip prefix-list PLC seq 2 permit 10.10.10.0/24 ge 28 le 30
 ip prefix-list 172.120.16.8 seq 5 permit 172.120.16.8/32
 !
 ip as-path access-list auto-core-15296501950110247-as-path-outpermit .*
 !
 route-map auto-core-15296501950110247-route-map-in permit 10
 set local-preference 100
 !
 route-map auto-core-15296501950110247-route-map-out permit 99
 match as-path auto-core-15296501950110247-as-path-out
 match ip address prefix-list auto-prefix-adv-and-distribute set
 as-path prepend 7000,7000,7000,7000
 !
 route-map peer-172.120.16.8-show permit 10
 match ip next-hop prefix-list 172.120.16.8
 !
 ip forwarding!line vty
 !
 end 

 Previous 

 dump routing routemap 

 Next 

 dump routing summary

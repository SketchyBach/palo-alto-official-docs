---
url: https://docs.paloaltonetworks.com/prisma-sd-wan/ion-cli-reference/use-cli-commands/inspect-commands/inspect-connection
fetched_at: 2026-09-16T07:48:40Z
source: strata-and-sase
---

# inspect connection Clear

Updated on 

 Jun 2, 2026 

 Focus 

 Home 

 Prisma SD-WAN 

 Use CLI Commands 

 Inspect Commands 

 inspect connection 

 Download PDF 

 Prisma SD-WAN 

 inspect connection 

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

 inspect cgnxinfra role 

 Next 

 inspect dhcplease 

 inspect connection 

 Use the inspect connection command
to inspect the established connections and to debug connections
that match user-specified options. It displays the protocol, time
after which connection times out, source IP, destination IP, source
port, and destination port. 

 Command 

 inspect connection (all | srcv4=src-ipv4 | destv4=dst-ipv4 | srcv6=src-ipv6 | destv6=dst-ipv6 | srcport=src-port | dstport=dst-port | proto= ( udp | tcp | icmp | other )) 

 Options 

 srcv4 Enter the source IPv4 address. 

 dstv4 Enter the destination IPv4 address. 

 srcv6 Enter the source IPv6 address. 

 dstv6 Enter the destination IPv6 address. 

 srcport Enter the source port. 

 dstport Enter the destination port. 

 proto Tab to select UDP, TCP, or ICMP. Or, enter
a protocol number ranging from 0 - 255. 

 Command Notes 

 Role Super, Read Only 

 Related Commands — 

 Introduced in Release 5.0.1 

 Example 

 inspect connection proto=udp
 PROTO TIMEOUT SRC DST SPORT DPORT t-src t-dst tsport tdport
 udp 6 127.0.0.1 127.0.0.1 51884 53 127.0.0.1 127.0. 0.1 51884 53
 udp 12 0.0.0.0 255.255.255.255 68 67 0.0.0.0 255.255.255.255 68 67
 udp 29 10.24.18.20 210.24.18.101 51409 3784 10.24.18.20 210.24.18.101 51409 3784

 inspect connection all

 PROTO TIMEOUT SRC DST SPORT DPORT t-src t-dst t-sport t-dport

 tcp 3524 fd13::2 2001:800::2 52754 9999 2001:800::1 2001:800::2 52754 9999

 udp 29 100.64.0.36 100.64.0.37 52634 3784 100.64.0.36 100.64.0.37 52634 3784

 udp 29 100.64.0.38 100.64.0.39 62944 3784 100.64.0.38 100.64.0.39 62944 3784 

 Previous 

 inspect cgnxinfra role 

 Next 

 inspect dhcplease

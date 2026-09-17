---
url: https://docs.paloaltonetworks.com/prisma-sd-wan/ion-cli-reference/use-cli-commands/debug-commands/trace-route
fetched_at: 2026-09-16T07:48:21Z
source: strata-and-sase
---

# traceroute Clear

Updated on 

 Tue Jun 02 09:34:24 PDT 2026 

 Focus 

 Home 

 Prisma SD-WAN 

 Use CLI Commands 

 Debug Commands 

 traceroute 

 Download PDF 

 Prisma SD-WAN 

 traceroute 

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

 tcpping 

 Next 

 traceroute6 

 traceroute 

 Use the traceroute command to
print the route taken by packets to a destination and to identify the
route or measure packet transit delays across a network. 

 Command 

 traceroute interface dst-ipv4 (args=" ") 

 Options 

 dst-ipv4 Enter the interface to listen on. 

 interface Enter the interface name or ID. 

 args= "-F" Use when probe packets should not be fragmented. 

 args= "-l" Displays the time-to-live (TTL) value of the returned
packet. 

 args="-l" Use ICMP ECHO instead of UDP datagrams. 

 args="-m number" Enter the maximum number of hops (max TTL value)
that trace route probe. 

 args= "-n" Print hop addresses numerically rather than symbolically. 

 args="-p string" This is the base UDP port number used in probes (default
value is 33434). 

 args="-q number" Enter the number of probe packets per TTL.
The default value is 3. 

 args= "-t number" Enter a value for Type of Service (TOS) in
probe packets. The default value is 0. 

 args="-w number" Enter a time (in seconds) to wait for a response to
a probe. The default value is 3 seconds. 

 Command Notes 

 Role Super, Read Only 

 Related Commands — 

 Introduced in Release 4.4.1 

 Example 

 traceroute 1 8.8.8.8 args="-n"
 traceroute to 8.8.8.8 (8.8.8.8), 30 hops max, 46 byte packets 1
 200.30.0.2 92.231 ms 92.298 ms 92.241 ms 2 10.0.0.1 92.336 ms
 92.327 ms 92.388 ms 3 66.128.148.171 93.410 ms 93.279 ms * 4
 206.72.210.41 102.026 ms 102.013 ms 103.401 ms 5 108.170.247.225
 101.901 ms * 108.170.247.161 101.729 ms 6 108.177.3.235 102.291 ms
 72.14.232.197 102.165 ms 108.170.238.7 102.435 ms 7 8.8.8.8
 101.937 ms 101.563 ms 102.023 ms 

 Previous 

 tcpping 

 Next 

 traceroute6

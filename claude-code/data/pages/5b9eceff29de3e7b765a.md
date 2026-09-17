---
url: https://docs.paloaltonetworks.com/prisma-sd-wan/ion-cli-reference/use-cli-commands/debug-commands/ssh-interface
fetched_at: 2026-09-16T07:48:21Z
source: strata-and-sase
---

# ssh interface Clear

Updated on 

 Tue Jun 02 09:34:24 PDT 2026 

 Focus 

 Home 

 Prisma SD-WAN 

 Use CLI Commands 

 Debug Commands 

 ssh interface 

 Download PDF 

 Prisma SD-WAN 

 ssh interface 

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

 ssh6 interface 

 Next 

 tcpdump 

 ssh interface 

 Use the ssh interface command
to invoke the secure shell (SSH) or client from the device for debugging
and troubleshooting purposes. 

 Command 

 ssh <interface> <user>@<hostname> [port | identity] 

 Options 

 port Enter a port number for SSH connection. 

 identity Provides a file identity in the form of a private
key for RSA or DSA authentication. For example, 

 ABC.pem 

 Command Notes 

 Role Super, Read Only 

 Related Commands — 

 Introduced in Release 4.7.1 

 Example 

 ssh controller1 elem-admin@172.20.75.146
 Warning: Permanently added '172.20.75.146' (ECDSA) to the list ofknown hosts.
 Password: # #

 dump software status
 CurrentVersion : 4.7.1-b6
 APICompleteSha :
 e54a0cedb4e999f6453d98110cf8a3baac9affc68fcbe91157344d83d4b815c2APIMajorShacf7cc4a0e0f6a70d8fd940f7c18e6f4e4f34c8adced0d4bf7a7b0692c76629a0#
 #exit
 Connection to 172.20.75.146 closed. 

 Previous 

 ssh6 interface 

 Next 

 tcpdump

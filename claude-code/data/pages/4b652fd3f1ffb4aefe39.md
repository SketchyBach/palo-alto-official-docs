---
url: https://docs.paloaltonetworks.com/prisma-sd-wan/ion-cli-reference/get-started-with-the-ion-cli/grep-support-for-the-ion-cli-commands
fetched_at: 2026-09-16T07:48:15Z
source: strata-and-sase
---

# Grep Support for the ION Device CLI Commands Clear

Updated on 

 Tue Jun 02 09:34:24 PDT 2026 

 Focus 

 Home 

 Prisma SD-WAN 

 Get Started with the ION Device CLI 

 Grep Support for the ION Device CLI Commands 

 Download PDF 

 Prisma SD-WAN 

 Grep Support for the ION Device CLI Commands 

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

 Command Syntax 

 Next 

 Access the ION Device CLI Commands 

 Grep Support for the ION Device CLI Commands 

 Grep support for Prisma SD-WAN ION CLI commands. 

 Grep is a command-line utility that searches
for text that matches a specified regular expression or a pattern and
use CLI commands to filter the command output. 

 Option Description 

 -i Ignores case, i.e., the search is irrespective
of uppercase or lowercase. 

 -v Inverts match, i.e., returns results that do
not have the specified search string. 

 -w Matches words or regular expressions, i.e.
returns only those lines which contain matches that form whole words. 

 -F Interprets patterns as a list of fixed strings
instead of regular expressions. 

 An example of grep command usage is shown as
follows: 

 Output without grep 

 #dump interface status
interface=controller1 

 Interface : controller 1
 Device : eth0
 ID : 15257577339130077
 MAC Address : 00:50:56:a7:7a:e9
 State : up
 Last Change : 2018-08-22 11:06:21.450667117 +0000 UTC
 Duplex : full
 Speed : 1000Mbps
 Address : 172.20.74.134/22
 Route : 0.0.0.0/0 via 172.20.75.254 metric 0
DNS Server : 172.18.18.160
DNS Server : 172.30.30.250
DNS Search : google.com

 Output with grep 

 #dump interface status interface=controller1
| grep Add 

 MAC Address : 00:50:56:a7:7a:e9
Address : 172.20.74.134/22 

 Previous 

 Command Syntax 

 Next 

 Access the ION Device CLI Commands

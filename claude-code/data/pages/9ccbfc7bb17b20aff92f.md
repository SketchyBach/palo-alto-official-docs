---
url: https://docs.paloaltonetworks.com/prisma-sd-wan/ion-cli-reference/use-cli-commands/inspect-commands/inspect-ipfix-app-table
fetched_at: 2026-09-16T07:48:41Z
source: strata-and-sase
---

# inspect ipfix app-table Clear

Updated on 

 Tue Jun 02 09:34:24 PDT 2026 

 Focus 

 Home 

 Prisma SD-WAN 

 Use CLI Commands 

 Inspect Commands 

 inspect ipfix app-table 

 Download PDF 

 Prisma SD-WAN 

 inspect ipfix app-table 

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

 inspect ipfix collector-stats 

 Next 

 inspect ipfix wan-path-info 

 inspect ipfix app-table 

 Use the inspect ipfix app-table command
to present mapping information exported in the IPFIX option records.
The standard applicationId (IANA 95) information element provides
the AppId value as a part of the flow data record. Collectors need
to associate the exported application identifiers with the application
names. 

 Command 

 inspect ipfix app-table 

 Options 

 None 

 Command Notes 

 Role Super, Read Only 

 Related Commands — 

 Introduced in Release 5.5.1 

 Example 

 inspect ipfix app-table | grep netbios
 Application Name IPFIX..App Id (Hex)
 --------------------- ----------------------- ------------------
 netbios 6..14585908745650047 0x060033d1ce8582bf7f 

 Previous 

 inspect ipfix collector-stats 

 Next 

 inspect ipfix wan-path-info

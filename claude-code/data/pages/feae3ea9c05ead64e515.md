---
url: https://docs.paloaltonetworks.com/prisma-sd-wan/ion-cli-reference/use-cli-commands/dump-commands/dump-performance-policy-config-policy-sets
fetched_at: 2026-09-16T07:48:30Z
source: strata-and-sase
---

# dump performance-policy config policy-sets Clear

Updated on 

 Tue Jun 02 09:34:24 PDT 2026 

 Focus 

 Home 

 Prisma SD-WAN 

 Use CLI Commands 

 Dump Commands 

 dump performance-policy config policy-sets 

 Download PDF 

 Prisma SD-WAN 

 dump performance-policy config policy-sets 

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

 dump performance-policy config policy-rules 

 Next 

 dump performance-policy config policy-set-stacks 

 dump performance-policy config policy-sets 

 Use the dump performance-policy config policy-sets command to display
 the current details of a device interface. 

 Information displayed includes the name of the policy set and the policy set
 ID. 

 Command 

 dump performance-policy config policy-sets <all | policy-set>

 Options 

 name Enter the name of the policy set. 

 Command Notes 

 Role Super, Read Only, Monitor 

 Related Commands NA 

 Introduced in Release 6.3.1 

 Example 

 dump performance-policy config policy-sets all
Performance Policy Set : FirstPolicy (1690738857525016028)
Link Health Policy rule Order : 1696588934366004628 : Rule_1

Performance Policy Set : Default-PerfMgmtPolicySet (1690621745198024028)
Link Health Policy rule Order : 1690621746053024428 : Default-PerfMgmtRule-Visibility
 1690621746045024328 : Default-PerfMgmtRule-Media-Apps
 1690621745787024228 : Default-PerfMgmtRule-All-Apps

 dump performance-policy config policy-sets policy-set=1690621745198024028
Performance Policy Set : Default-PerfMgmtPolicySet (1690621745198024028)
Link Health Policy rule Order : 1690621746053024428 : Default-PerfMgmtRule-Visibility
 1690621746045024328 : Default-PerfMgmtRule-Media-Apps
 1690621745787024228 : Default-PerfMgmtRule-All-Apps

 Previous 

 dump performance-policy config policy-rules 

 Next 

 dump performance-policy config policy-set-stacks

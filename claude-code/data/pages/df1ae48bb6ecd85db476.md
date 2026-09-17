---
url: https://docs.paloaltonetworks.com/prisma-sd-wan/ion-cli-reference/use-cli-commands/dump-commands/dump-security-policy-config-policy-set
fetched_at: 2026-09-16T07:48:35Z
source: strata-and-sase
---

# dump security-policy config policy-set Clear

Updated on 

 Tue Jun 02 09:34:24 PDT 2026 

 Focus 

 Home 

 Prisma SD-WAN 

 Use CLI Commands 

 Dump Commands 

 dump security-policy config policy-set 

 Download PDF 

 Prisma SD-WAN 

 dump security-policy config policy-set 

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

 dump security-policy config policy-rules 

 Next 

 dump security-policy config policy-set-stack 

 dump security-policy config policy-set 

 Use the dump security-policy config policy-set command
to display the security policy sets configuration for a device. 

 Information
displayed includes the policy set ids along with the order of security
policy rules. 

 Command 

 dump security-policy config policy-set all 

 Options 

 None 

 Command Notes 

 Role Super, Read Only, Monitor 

 Related Commands 

 dump security-policy config policy-rules 

 Introduced in Release 4.5.1 

 Example 

 dump security-policy config policy-set all
 Security Policy Set ID : 16245957623450255
 Security Policy Set Name: Set2-Port-Range
 Policy Rule Order: 
 16246315738930189: Rule1-Set2-20 
 16246317241460212: Rule2-Set2-21 
 16246318197250246: Rule3-Set2-22
 Security Policy Set ID : 16245009722000198
 Security Policy Set Name: Set3-Specific
 Policy Rule Order: 
 16245010650670003: Rule1-Set3-20 
 16245011984140128: Rule2-Set3-21 
 16245012757060237: Rule3-Set3-22
 Security Policy Set ID : 16245013500920058
 Security Policy Set Name: Set4-Generic
 Policy Rule Order: 
 16245013906270078: Rule1-Set4
 Security Policy Set ID : 16228336609730048
 Security Policy Set Name: default
 Policy Rule Order: 
 16228336610060052: self-zone 
 16228336610050051: intra-zone 
 16228336609900050: default 

 dump security-policy config policy-set policy-set-name=branch-zfbw-set2

 Security Policy Set ID : 1676108499873022196
 Security Policy Set Name : branch-zfbw-set2
 Policy Rule Order:
 1676108536798018796 : branch-zbfw-rule2
 1676114407512016596 : branch-zbfw-rule3

 Previous 

 dump security-policy config policy-rules 

 Next 

 dump security-policy config policy-set-stack

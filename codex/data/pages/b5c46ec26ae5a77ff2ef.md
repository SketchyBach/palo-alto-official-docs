---
url: https://docs.paloaltonetworks.com/prisma-sd-wan/administration/prisma-sd-wan-stacked-policies/add-a-path-policy-rule/l3-failure-path
fetched_at: 2026-09-16T07:47:55Z
source: strata-and-sase
---

# L3 Failure Paths Clear

Updated on 

 Mon Aug 24 08:54:44 PDT 2026 

 Focus 

 Home 

 Prisma SD-WAN 

 Prisma SD-WAN Administrator’s Guide 

 Prisma SD-WAN Stacked Policies 

 Add a Path Policy Rule 

 L3 Failure Paths 

 Download PDF 

 Prisma SD-WAN 

 L3 Failure Paths 

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

 Configure User-ID based Policy Rules 

 Next 

 Minimize Metered LTE Usage 

 L3 Failure Paths 

 Let us learn about the Layer 3 failure on all other paths and understand that there is no
 way to reach the WAN side destination optimally or sub-optimally. 

 Where Can I Use This? What Do I Need? 

 Prisma SD-WAN (Managed by Strata Cloud Manager ) 

 Prisma SD-WAN 

 Layer Failure 3 paths can be private wan or internet paths, VPN, or standard
 VPNs. The L3 failure path will only be used when there is a Layer 3 failure on all other
 active and backup paths and there is no way to reach the WAN side destination optimally
 or sub-optimally. Typical usecase for L3 Failure path would be a Metered 4G/5G
 connection. To keep bandwidth consumption low on the cellular circuit you can configure
 it as a L3 failure path. 

 A path that is configured in the Layer 3 failure
paths list is considered only in the following conditions: 

 Condition 1 

 All active and backup paths
are up and available, but Layer 3 is unreachable. 

 Layer 3 failure paths are configured and up. 

 At least one Layer 3 failure path is Layer 3 reachable. 

 Condition 2 

 All active and backup paths are
down or routes on both paths do not exist. For example, direct on
public-1 and public-1 do not exist. 

 Layer 3 failure paths are configured and are up. 

 Condition 3 

 Network asymmetry. 

 Previous 

 Configure User-ID based Policy Rules 

 Next 

 Minimize Metered LTE Usage

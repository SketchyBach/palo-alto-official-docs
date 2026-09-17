---
url: https://docs.paloaltonetworks.com/prisma-sd-wan/administration/performance-policy-with-forward-error-correction-fec/performance-policy-use-cases
fetched_at: 2026-09-16T07:47:33Z
source: strata-and-sase
---

# Performance Policy Use Cases Clear

Updated on 

 Mon Aug 24 08:54:44 PDT 2026 

 Focus 

 Home 

 Prisma SD-WAN 

 Prisma SD-WAN Administrator’s Guide 

 Prisma SD-WAN Performance Policy 

 Performance Policy Use Cases 

 Download PDF 

 Prisma SD-WAN 

 Performance Policy Use Cases 

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

 Best Practices and Recommendations 

 Next 

 Use Case 1 - Protect a Business Critical SaaS Application 

 Performance Policy Use Cases 

 Introduction to Performance Policy use cases to review sample policy rules for
 several common use cases along with general guidelines for implementation. 

 Where Can I Use This? What Do I Need? 

 Prisma SD-WAN (Managed by Strata Cloud Manager ) 

 Prisma SD-WAN 

 Physical and virtual ION devices running software version 6.3.1
 and higher 

 Performance Policy provides a flexible framework for the assurance of Application and
 Network SLAs. In this section, we will review common use cases, how to configure the
 policy intent, and how to monitor for effectiveness. 
 Use Case 1 - Protect a Business Critical SaaS Application : The business uses
 SuperSaaSApp as a critical application, requiring low latency and SLA
 compliance. Direct internet paths (Verizon and Comcast) are prioritized, with
 metered 5G as a fallback. A performance policy monitors path quality (latency,
 jitter, packet loss) and dynamically routes traffic to compliant paths, raising
 alerts for noncompliance. Monitoring tools like Flow Browser revealed
 Verizon's excessive packet loss, triggering incidents for degraded application
 and circuit performance. This policy ensures optimal app performance, efficient
 traffic management, and timely issue resolution. 

 Use Case 2 - Protect a Business Critical Enterprise Application : The business uses WebPoS 
 for Point of Sale, hosted in corporate data centers, where packet loss
 significantly affects performance. A performance policy prioritizes the Prisma
 SD-WAN VPN on the primary internet, with metered 5G as a Layer 3 failure path.
 The policy uses Link Quality Monitoring (LQM) to adaptively apply Forward Error
 Correction (FEC) for packet loss, ensuring optimal performance. Monitoring tools
 revealed consistent packet loss on the active path, mitigated by FEC to maintain
 0% packet loss for WebPoS sessions. This policy ensures reliable order
 processing and is easily monitored through Application Details, Link Quality
 Metrics, and the Flow Browser. 

 Use Case 3 - Protect Physical Security on LEO Satellite and 5G : The business relies on secure, high-bandwidth
 connectivity for remote locations with strict physical security requirements,
 including video and audio surveillance. Traffic is configured to use Prisma
 SD-WAN VPNs over LEO Satellite Internet and non-metered Public 5G as active
 paths, with Internet ADSL as a Layer 3 failure path. The performance policy
 leverages Link Quality Monitoring (LQM) to actively manage packet duplication
 during packet loss or path degradation, ensuring reliable operations. This setup
 ensures delivery of critical traffic, with issues monitored through App Site
 Details, Link Quality Metrics, and the Flow Browser. 

 Use Case 4 - Protect An Enterprise Voice Application : The business relies on a VoIP system for
 contact centers, with an SLA requiring a minimum MOS score of 3.6 and packet
 loss below 1%. Media traffic (RTP-Audio, RTP-Base, and SIP) uses primary
 internet and MPLS as active paths, with Metered 5G as a last-resort fallback. A
 performance policy ensures traffic is routed through SLA compliant paths, with
 packet duplication applied during packet loss or path degradation. This policy
 guarantees critical voice traffic delivery and is monitored via App Site
 Details, Link Quality Metrics, and the Flow Browser. 

 Previous 

 Best Practices and Recommendations 

 Next 

 Use Case 1 - Protect a Business Critical SaaS Application

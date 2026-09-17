---
url: https://docs.paloaltonetworks.com/prisma/prisma-sd-wan/prisma-sd-wan-admin/get-started-with-prisma-sd-wan/prisma-sd-wan-link-quality
fetched_at: 2026-09-16T11:47:21Z
source: palo-alto-main
---

# Prisma SD-WAN Link Quality Dashboard Clear

Updated on 

 Mon Aug 24 08:54:44 PDT 2026 

 Focus 

 Home 

 Prisma SD-WAN 

 Prisma SD-WAN Administrator’s Guide 

 Get Started with Prisma SD-WAN 

 Prisma SD-WAN Link Quality Dashboard 

 Download PDF 

 Prisma SD-WAN 

 Prisma SD-WAN Link Quality Dashboard 

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

 Prisma SD-WAN Predictive Analytics Dashboard 

 Next 

 Prisma SD-WAN Command Center Dashboard 

 Prisma SD-WAN Link Quality Dashboard 

 Monitor WAN path health with the Prisma SD-WAN Link Quality Dashboard, which displays MOS, packet loss, jitter, and latency across all branch and data center sites. 

 Where Can I Use
 This? What Do I Need? 

 Prisma SD-WAN (Managed by Strata Cloud Manager ) 

 Prisma SD-WAN 

 With Prisma® SD-WAN, you meet application Service Level Agreements (SLAs) by configuring Path ,
 QoS , and Security policies. In
 your Prisma SD-WAN path policy, you define rules that express your business intent for which
 paths are allowed per application. ION devices evaluate each application session
 against your defined path policy and select the WAN path that meets the
 application-specific SLA. One key mechanism for determining whether a path will
 meet an application’s SLA is monitoring Link Quality . 

 The Dashboard 
 > 
 Overall Link Quality on the web interface provides the aggregate
 link quality metrics of all branch and data center sites at a glance. It includes
 information on the MOS, packet loss, jitter, and latency of the links. View data in the
 last available 5 minutes' time frames and the last available 1 hour of any metric. 

 Prisma SD-WAN determines link quality by actively probing the
 Secure Fabric VPN paths over public and private transports
 and the private WAN underlay paths. The probes provide a constant measurement of network
 performance metrics, such as jitter, latency, and packet loss. These metrics, along with
 application-specific performance metrics and Layer 1 – Layer 7 reachability inform
 traffic forwarding decisions for new and existing application flows. 

 By default, Link Quality metrics influence path selection for all
 real-time voice and video applications. If a link is acceptable, the
 real-time application stays on the initially selected path. However, when the link becomes
 degraded or inadequate, the ION device seamlessly moves all existing and
 subsequent real-time application flows to a suitable alternate path, if one is available and allowed by
 policy. 

 Choose link quality metrics and filter the information by
 Interval, Start Time, and Direction. You can change the
 metric to any other link quality metric to view the corresponding graphs. The bar graphs display the distribution range up to the 90th percentile of the available data. 

 The Link Quality Metrics dashboard shows a snapshot of the current state
 of your monitored links. You view Link Performance,
 Link Packet Loss, Link Jitter, and Link Latency. By default, the dashboard displays links for all
 your sites for the most recent time period (last available 5 minutes or last
 available hour). You can use filters to change the scope of
 displayed information and analyze specific data in greater
 detail on the Link Quality Details tab. 

 Click View Details to view the links table in detail.
 The table displays all secure fabric links between sites, along with
 Circuit and WAN information. You can view link quality metrics and link type
 for each link. Sort the table by any link quality
 metric to display the worst values at the top. Expand a site to view
 link quality metrics for ingress and egress flows. You can view the link
 quality chart per site and path. Your selected site and active path become the preselected
 filter criteria for the Activity chart. 

 Related CLIs 

 inspect lqm stats 

 Previous 

 Prisma SD-WAN Predictive Analytics Dashboard 

 Next 

 Prisma SD-WAN Command Center Dashboard

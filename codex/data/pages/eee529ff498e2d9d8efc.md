---
url: https://docs.paloaltonetworks.com/content/techdocs/en_US/enterprise-dlp/getting-started/whats-supported-with-enterprise-data-loss-prevention/support-for-nonfile-based-traffic.html
fetched_at: 2026-09-16T09:59:18Z
source: palo-alto-main
---

# Non-File Based Traffic Clear

Updated on 

 Fri Sep 04 15:49:18 PDT 2026 

 Focus 

 Home 

 Enterprise DLP 

 What's Supported with Enterprise DLP? 

 Non-File Based Traffic 

 Download PDF 

 Enterprise DLP 

 Non-File Based Traffic 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Enterprise DLP Docs 

 Activation & Onboarding 

 Getting Started 

 Administration 

 Reference 

 Release Notes 

 New Features by OS Version 

 New Features by Month 

 Previous 

 Supported Languages 

 Next 

 Failover and Resiliency 

 Non-File Based Traffic 

 Non-file based traffic types that Enterprise Data Loss Prevention (E-DLP) can inspect, including
 clipboard paste, form submissions, and chat messages. 

 Inspection of non-file based traffic is supported on Panorama running PAN-OS
 10.2.1 and later releases and Enterprise DLP plugin 3.0.1 and later
 releases. 

 To upgrade to PAN-OS 10.2.1, you must install Application and Threats content release
 version 8552-7333 or later version on Panorama and managed
 firewalls using Enterprise DLP . This is required to support non-file based
 traffic inspection. 

 Enterprise Data Loss Prevention (E-DLP) supports inspection of non-file based traffic for sensitive
 data. A data filtering profile configured for non-file based traffic detection allows
 you to configure URL and application exclusion lists to exempt specific URLs and
 applications from Enterprise DLP inspection. 

 On the Panorama® management server , each data profile you create can be configured to
 inspect for either file-based traffic or for non-file based traffic, or for both. On Strata Cloud Manager , you need to enable non-file based DLP inspection . After you enable this setting on
 Strata Cloud Manager you can modify a DLP rule to inspect for either
 file-based traffic or for non-file based traffic, or for both. 

 Enterprise DLP pre-filtering for non-file traffic automatically
 identifies and excludes URLs that can't contain user-entered data before they reach
 inspection. Pre-filtering currently applies to supported non-GenAI and GenAI apps with the web-browsing 
 App-ID . When you enable non-file based inspection, Enterprise DLP 
 forwards every PUT and POST web request for inspection. This includes background
 telemetry, analytics calls, and other operational traffic that typically carries
 operational metadata rather than sensitive data. These requests can generate false
 positive incidents by triggering sensitive data pattern matches on system noise rather
 than actual data leakage. Pre-filtering resolves this by recognizing known telemetry,
 analytics, and background operational request patterns and dropping them before
 inspection begins. Enterprise DLP also adapts dynamically to exclude new telemetry
 patterns as they emerge, keeping your exclusion coverage current without manual updates.
 For traffic unique to your environment, you can define additional URLs or applications
 to exclude through non-file Application List and URL Category List Exclusions in the
 DLP rule . Pre-filtering is a service-side
 capability that doesn't require upgrades to Strata Cloud Manager , Prisma Access , or
 your NGFW . 

 If you enable non-file based inspection, you can
 then also enable WebSocket inspection . WebSocket inspection
 is a special type of non-file based inspection, which examines WebSocket persistent
 streams in real time to identify sensitive patterns within the open connection. 

 Previous 

 Supported Languages 

 Next 

 Failover and Resiliency

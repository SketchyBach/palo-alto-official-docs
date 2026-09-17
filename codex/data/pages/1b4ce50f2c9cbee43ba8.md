---
url: https://docs.paloaltonetworks.com/content/techdocs/en_US/enterprise-dlp/activation-and-onboarding/setup-prerequisites-for-enterprise-dlp/setup-prerequisites-for-enterprise-dlp-evidence-storage-syslog-icap-forwarding.html
fetched_at: 2026-09-16T09:59:19Z
source: palo-alto-main
---

# Setup Prerequisites for Enterprise DLP Evidence Storage, Syslog Forwarding, and ICAP
        Forwarding Clear

Updated on 

 Tue Sep 01 12:56:17 PDT 2026 

 Focus 

 Home 

 Enterprise DLP 

 Activation & Onboarding 

 Setup Prerequisites for Enterprise DLP 

 Setup Prerequisites for Enterprise DLP Evidence Storage, Syslog Forwarding, and ICAP
 Forwarding 

 Download PDF 

 Enterprise DLP 

 Setup Prerequisites for Enterprise DLP Evidence Storage, Syslog Forwarding, and ICAP
 Forwarding 

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

 Setup Prerequisites for Enterprise DLP Evidence Storage, Syslog Forwarding, and ICAP
 Forwarding 

 Allow access to the IP addresses required for Enterprise Data Loss Prevention (E-DLP) Evidence
 Storage, Syslog Forwarding, and ICAP Forwarding services. 

 Enterprise Data Loss Prevention (E-DLP) requires you to allow the same region-specific IP addresses on
 your network for Evidence Storage, Syslog Forwarding, and ICAP Forwarding. If you have
 already allowed these IP addresses for one service, you don't need to allow them again
 for the others. 

 Evidence Storage —Allow the IP addresses for the region or zone where Enterprise DLP scans traffic to— automatically store inspected files. To
 download stored files from your evidence storage bucket, you may also need to
 allow specific user IP addresses. If your organization uses a virtual private
 network (VPN), you must allow the subnets that can download files from your
 evidence storage bucket. 

 Syslog Forwarding —Allow the IP addresses to forward 
 Enterprise Data Loss Prevention (E-DLP) incident syslogs to your third-party security
 information and event management (SIEM), Security Orchestration, Automation and
 Response (SOAR), or other automated ticketing systems. This enables your SOC
 analysts and incident admins to triage, review, and resolve data security risks
 in your organization. 

 ICAP Forwarding —Allow the IP addresses to integrate your existing
 on-premises third-party DLP solutions with Enterprise DLP using Internet
 Content Adaptation Protocol (ICAP). You can configure Enterprise DLP to
 forward inspected files to your on-premises ICAP server for further inspection
 while still leveraging the advanced inline ML-based detections that Enterprise DLP offers. 

 You must allow the Default IP addresses to successfully
 connect to Enterprise DLP services. The region-specific IP addresses you need to
 allow depend on the region or zone where Enterprise DLP scans traffic. 

 Country IP Addresses 

 Region IP Address 

 Date Introduced 

 Australia 

 13.54.198.248 

 April 30, 2022 

 52.63.9.154 

 34.87.236.168 

 May 7, 2025 

 Brazil 

 56.124.6.83 

 56.125.134.63 

 November 10, 2025 

 Canada 

 15.222.125.234 

 April 30, 2022 

 99.79.19.33 

 34.118.182.133 

 May 7, 2025 

 France 

 15.237.145.165 

 April 30, 2022 

 13.36.207.215 

 34.155.50.15 

 May 7, 2025 

 Germany 

 3.123.172.116 

 April 30, 2022 

 52.59.186.42 

 35.198.73.41 

 May 7, 2025 

 India 

 15.207.246.3 

 April 30, 2022 

 3.108.103.214 

 34.47.134.16 

 May 7, 2025 

 Japan 

 3.115.43.201 

 April 30, 2022 

 35.72.148.77 

 35.74.96.38 

 52.68.52.77 

 34.84.142.203 

 May 7, 2025 

 Singapore 

 13.228.151.58 

 April 30, 2022 

 52.74.82.77 

 34.142.217.106 

 May 7, 2025 

 Switzerland 

 34.65.89.231 

 June 13, 2025 

 United Kingdom 

 13.43.141.10 

 April 30, 2022 

 18.169.44.228 

 35.177.5.4 

 52.56.54.90 

 ( London, England )
 35.197.230.50 

 May 7, 2025 

 ( Default ) United States of America 

 3.230.176.219 

 April 30, 2022 

 3.226.106.173 

 18.190.146.204 

 3.16.224.253 

 34.223.123.78 

 35.164.119.230 

 52.27.148.95 

 54.189.225.136 

 34.135.174.89 

 May 7, 2025 

 34.173.206.52 

 34.172.74.250 

 34.48.104.244 

 35.197.73.227 

 34.94.161.165 

 34.66.246.164 

 35.225.238.124 

 35.223.231.169 

 34.58.60.130 

 35.238.28.62 

 34.67.76.48 

 104.154.217.19 

 35.202.179.253 

 34.123.101.142 

 ( Evidence Storage only ) FedRAMP IP Addresses 

 Supported for AWS storage buckets only. Not
 supported for Azure or SFTP storage buckets. 

 Country 

 IP Address 

 FedRAMP Impact Level 

 Date Introduced 

 United States 

 3.31.2.86 

 3.31.9.107 

 15.205.197.250 

 Moderate 

 April 30, 2022

---
url: https://cortex-docs.paloaltonetworks.com/analytics-alerts/alerts-by-name/user-installed-an-application-in-microsoft-teams-via-graph-api
fetched_at: 2026-09-16T09:08:55Z
source: cortex-platform
---

# User installed an application in Microsoft Teams via Graph API | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 Analytics Alerts 

 Alerts by name 

 User installed an application in Microsoft Teams via Graph API 

 Synopsis 

 Field 

 Value 

 Activation Period 

 14 Days 

 Training Period 

 30 Days 

 Test Period 

 N/A (single event) 

 Deduplication Period 

 1 Day 

 Required Data 

 Microsoft Graph Logs 

 Detection Modules 

 Identity Threat Module, SaaS Threat Detection 

 Detector Tags 

 Microsoft Teams 

 ATT&CK Tactic 

 Persistence (TA0003) 

 ATT&CK Technique 

 Cloud Application Integration (T1671) 

 Severity 

 Informational 

 Description 

 A user who rarely uses the Graph API to install Microsoft Teams applications has installed one using it. 

 Attacker's Goals 

 Attackers may leverage Teams applications to maintain persistent access to compromised Teams accounts. 

 Investigative actions 

 Verify the user's role and typical usage of Microsoft Graph API. 

 Check if the user's account has recently logged in from unusual locations or devices. 

 Review recent email and chat activity to identify any phishing or suspicious messages sent. 

 Examine the Graph API call logs to see what actions were performed and their timestamps. 

 Correlate with endpoint logs to detect any malware or suspicious processes running on the user's device. 

 Check for signs of account compromise, such as password changes or MFA bypass attempts. 

 Follow further actions done by the account. 

 Variations 
 User installed an application in Microsoft Teams via Graph API from a first seen ASN 

 Synopsis 

 Field 

 Value 

 ATT&CK Tactic 

 Persistence (TA0003) 

 ATT&CK Technique 

 Cloud Application Integration (T1671) 

 Severity 

 Low 

 Description 

 A user who rarely uses the Graph API to install Microsoft Teams applications has installed one using it. 

 Attacker's Goals 

 Attackers may leverage Teams applications to maintain persistent access to compromised Teams accounts. 

 Investigative actions 

 Verify the user's role and typical usage of Microsoft Graph API. 

 Check if the user's account has recently logged in from unusual locations or devices. 

 Review recent email and chat activity to identify any phishing or suspicious messages sent. 

 Examine the Graph API call logs to see what actions were performed and their timestamps. 

 Correlate with endpoint logs to detect any malware or suspicious processes running on the user's device. 

 Check for signs of account compromise, such as password changes or MFA bypass attempts. 

 Follow further actions done by the account. 

 Previous User exported multiple messages in Microsoft Teams via Graph API 

 Next User mail items accessed from multiple IPs in the same subnet 

 Was this helpful?

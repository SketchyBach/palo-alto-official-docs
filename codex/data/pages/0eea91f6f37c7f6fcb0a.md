---
url: https://docs.paloaltonetworks.com/ngfw/administration/app-id/security-policy-rule-optimization/high-availability-for-application-usage-statistics
fetched_at: 2026-09-16T07:25:33Z
source: palo-alto-main
---

# High Availability for Application Usage Statistics Clear

Updated on 

 Mon Aug 31 04:46:16 PDT 2026 

 Focus 

 Home 

 Next-Generation Firewall 

 App-ID 

 Security Policy Rule Optimization 

 High Availability for Application Usage Statistics 

 Download PDF 

 Next-Generation Firewall 

 High Availability for Application Usage Statistics 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Next-Generation Firewall Docs 

 Getting Started 

 Administration 

 Networking 

 Quick Start 

 Reference 

 Incidents & Alerts 

 Release Notes 

 Select a Document 

 PAN-OS 12.2 

 PAN-OS 12.1 

 PAN-OS 11.2 

 PAN-OS 11.1 

 PAN-OS 11.0 (EoL) 

 PAN-OS 10.2 

 PAN-OS 10.1 (EoL) 

 PAN-OS 10.0 (EoL) 

 PAN-OS 9.1 (EoL) 

 PAN-OS 9.0 (EoL) 

 PAN-OS 8.1 (EoL) 

 Help 

 Select a Document 

 PAN-OS 12.2 

 PAN-OS 12.1 

 PAN-OS 11.2 

 PAN-OS 11.1 

 PAN-OS 10.2 

 PAN-OS 10.1 

 New Features 

 Previous 

 Identify Security Policy Rules with Unused Applications 

 Next 

 How to Disable Policy Optimizer 

 High Availability for Application Usage Statistics 

 How active/passive and active/active high-availability
configurations affect where you can view application usage statistics. 

 Where Can I Use This? What Do I Need? 

 Prisma Access 

 Next-Generation Firewall 

 This is a core Network Security feature for NGFWs and Prisma Access;
 no prerequisites needed. 

 When you configure two firewalls as a
High Availability (HA) pair, the application usage statistics are
local to the firewall that generates the Traffic logs for the application.
Where you can view application usage statistics also depends in
part on the HA configuration: 

 Active/Passive —The active device generates the
application usage statistics. If a passive device has seen no user
traffic, then only the active device displays the application usage
statistics. If a passive device has seen traffic, then the passive
device only displays the application usage statistics from the traffic
that it has seen. 

 On a failover, the application usage statistics
are based only on the Traffic logs generated on the newly active
device (the device that was passive before the failover). 

 Active/Active —The device that owns a session generates
the Traffic logs for that session, so the application usage statistics
for a session are only available on the device that owns the session.
If one active device owns a session, the other active device does
not display that session’s application usage statistics. 

 Previous 

 Identify Security Policy Rules with Unused Applications 

 Next 

 How to Disable Policy Optimizer

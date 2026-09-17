---
url: https://docs.paloaltonetworks.com/ngfw/help/12-2/modify-the-captive-portal-session-timeout
fetched_at: 2026-09-16T08:20:51Z
source: palo-alto-main
---

# Modify the Authentication Portal Session Timeout Clear

Updated on 

 Wed Aug 19 00:09:31 PDT 2026 

 Focus 

 Home 

 Next-Generation Firewall 

 PAN-OS Web Interface Help 

 Modify the Authentication Portal Session Timeout 

 Download PDF 

 Next-Generation Firewall 

 Modify the Authentication Portal Session Timeout 

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

 Modify the Authentication Portal Session Timeout 

 The Authentication Portal session timeout
must be the same as or greater than the PAN-OS web server timeout.
For details, see Connection
Timeouts for Authentication Servers . 

 The more
you raise the PAN-OS web server and Authentication Portal session
timeouts, the slower Authentication Portal will respond to users. 

 Select Device Setup Session and
edit the Session Timeouts. 

 Enter a new Authentication Portal value
in seconds (default is 30; range is 1 to 1,599,999) and click OK . 

 Commit your changes.

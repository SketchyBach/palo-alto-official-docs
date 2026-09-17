---
url: https://docs.paloaltonetworks.com/ngfw/networking/fail-open/configure-fail-open/configure-fail-open-cli
fetched_at: 2026-09-16T07:32:53Z
source: palo-alto-main
---

# CLI Clear

Updated on 

 Thu Aug 13 13:39:29 PDT 2026 

 Focus 

 Home 

 Next-Generation Firewall 

 Fail Open 

 Configure Fail Open 

 CLI 

 Download PDF 

 Next-Generation Firewall 

 CLI 

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

 CLI 

 Configure the fail open ports on your firewall to provide a pass-through connection
 in the event of a power or operating system failure. 

 Issue the following command: 

 set network interface fail-open yes 

 Commit your change using the commit command. 

 You can view the fail open status by inputting the following command: 

 show interface <port> | match "Fail Open" 

 Replace <port> with the name of the fail open port
 (eg. ethernet1/3). 

 Verify that the result says Fail Open : Enabled .

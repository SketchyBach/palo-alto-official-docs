---
url: https://cortex-docs.paloaltonetworks.com/cortex-xdr-5.x/protect-your-endpoints/install-and-manage-endpoints/harden-endpoint-security/host-firewall
fetched_at: 2026-09-06T09:42:33Z
source: cortex-platform
---

# Host firewall | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XDR 

 Cortex XDR 5.x Documentation 

 Protect your endpoints 

 Install and manage endpoints 

 Harden endpoint security 

 Cortex XDR 5.x 

 Host firewall 

 Configure host firewall policies to control endpoint network traffic. 

 The Cortex XDR host firewall enables you to control communications on your endpoints. To use the host firewall, you set rules that allow or block the traffic on the devices and apply them to your endpoints using host firewall policy rules. Additionally, you can configure different sets of rules based on the current location of your endpoints - within or outside your organization network. The Cortex XDR host firewall rules leverage the operating system firewall APIs and enforce these rules on your endpoints, but not your Windows or Mac firewall settings. 

 The following apply Cortex XDR host firewall policy rules on your endpoints: 

 Platform 

 Requirements and Limitations 

 Windows 

 By default, Cortex firewall is disabled and Windows firewall has control. Enforcing Cortex firewall rules will take control away from Windows Firewall, and Windows firewall rules will no longer apply. 

 It is recommended to disable the windows firewall on endpoints running Windows 7 SP1 before applying the Cortex XDR host firewall profile. 

 Mac 

 After you disable or remove the Cortex XDR host-firewall policy on the endpoint, the system firewall on the endpoint is disabled. 

 You cannot configure the following Mac host firewall settings with the Cortex XDR host firewall. 

 Automatically allow built-in software to receive incoming connections. 

 Automatically allow downloaded signed software to receive incoming connections. 

 Linux 

 Not supported. 

 Previous Device control 

 Next Host firewall for Windows 

 Last updated 5 days ago 

 Was this helpful?

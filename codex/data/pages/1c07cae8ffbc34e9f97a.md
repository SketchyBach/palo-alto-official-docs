---
url: https://cortex-docs.paloaltonetworks.com/xsoar-6-administrator-guide/6.13/onboard-cortex-xsoar/engines/remove-an-engine
fetched_at: 2026-09-06T10:44:36Z
source: cortex-platform
---

# Remove an Engine | 6.13 | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSOAR 6 

 Cortex XSOAR 6 Administrator Guides 

 6.13 

 Onboard Cortex XSOAR 

 Engines 

 Cortex XSOAR 6.13 

 Remove an Engine 

 Remove an engine in Cortex XSOAR 6.13. 

 You can remove a Cortex XSOAR engine when it is no longer needed. 

 Run one of the following commands according to your operating system: 

 Installation 

 Command 

 RPM 

 Get the full package: **`rpm -qa 

 DEB 

 Get the full package: dpkg-query -W -f='${Package}' d1_* 

 Remove the package: dpkg --purge <package name> 

 SH 

 Remove an Engine: sudo`` `` <engine-file-path> -- -purge 

 For Windows machines, delete the engine file that was created. 

 Previous Notify Users When an Engine Disconnects 

 Next Troubleshoot Cortex XSOAR Engines 

 Last updated 3 days ago 

 Was this helpful?

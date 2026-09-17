---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsoar-8-saas/configure-cortex-xsoar/engines/remove-an-engine
fetched_at: 2026-09-16T08:52:17Z
source: cortex-platform
---

# Remove an engine | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSOAR 8 

 Cortex XSOAR 8 SaaS Documentation 

 Configure Cortex XSOAR 

 Engines 

 Cortex XSOAR 8 (SaaS) 

 Remove an engine 

 Remove a Cortex XSOAR 8 SaaS engine using the operating system command. 

 You can remove a engine when it is no longer needed. 

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

 Previous Upgrade an engine 

 Next Configure engines 

 Last updated 14 days ago 

 Was this helpful?

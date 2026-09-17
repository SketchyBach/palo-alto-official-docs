---
url: https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/administration/secure-agentless-access/configure-split-tunneling-for-secure-agentless-access-traffic/configure-split-tunneling-for-secure-agentless-access-traffic-scm.html
fetched_at: 2026-09-16T11:37:00Z
source: palo-alto-main
---

# Configure Split Tunneling for Secure Agentless Access Traffic (Strata Cloud Manager) Clear

Updated on 

 Thu Sep 03 12:12:03 PDT 2026 

 Focus 

 Home 

 Prisma Access 

 Prisma Access Administration 

 Secure Agentless Access 

 Configure Split Tunneling for Secure Agentless Access Traffic 

 Configure Split Tunneling for Secure Agentless Access Traffic (Strata Cloud Manager) 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 Deutsch (German) 

 Prisma Access 

 Configure Split Tunneling for Secure Agentless Access Traffic (Strata Cloud Manager) 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma Access Docs 

 Release Notes 

 Select a Document 

 6.2 Preferred and Innovation 

 6.1 Preferred and Innovation 

 6.0 Preferred and Innovation 

 5.2 Preferred and Innovation 

 5.1 Preferred and Innovation 

 5.0 Preferred and Innovation 

 4.2 Preferred 

 4.1 Preferred 

 4.0 Preferred 

 3.2 Preferred and Innovation 

 Activation & Onboarding 

 Administration 

 Select a Document 

 4.0 & Later 

 Prisma Access China 

 Integrations 

 Incidents & Alerts 

 New Features 

 Configure Split Tunneling for Secure Agentless Access Traffic ( Strata Cloud Manager ) 

 For managed devices, you can configure split tunneling for Secure Agentless Access traffic
 on Strata Cloud Manager to help improve SAA performance. 

 In use cases where SAA is being accessed from managed devices
 that have GlobalProtect installed, configure split tunneling for the SAA domain to help improve performance. 

 From Strata Cloud Manager , go to Configuration NGFW and Prisma Access Configuration Scope Prisma Access Mobile Users Container GlobalProtect Setup GlobalProtect App . 

 In the Tunnel Settings section, select Default . 

 Configure split tunnel settings to exclude traffic based on the destination
 domain. 

 In the Exclude Traffic section, click Add
 Domain . 

 Enter the Domain you're using for SAA . This can be the default SAA domain ( *.panwpra.com or *.panwsaa.com ) or
 your custom SAA domain. 

 Save your domain. 

 Save your tunnel settings and Push
 Config .

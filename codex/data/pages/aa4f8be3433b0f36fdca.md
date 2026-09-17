---
url: https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/administration/prisma-access-advanced-deployments/prisma-access-remote-network-advanced-deployments/prisma-access-internal-gateway/prisma-access-internal-gateway-panorama.html
fetched_at: 2026-09-16T11:36:49Z
source: palo-alto-main
---

# Prisma Access Internal Gateway (Panorama) Clear

Updated on 

 Sep 3, 2026 

 Focus 

 Home 

 Prisma Access 

 Prisma Access Administration 

 Prisma Access Advanced Deployments 

 Prisma Access Remote Network Advanced Deployments 

 Prisma Access Internal Gateway 

 Prisma Access Internal Gateway (Panorama) 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 Deutsch (German) 

 Prisma Access 

 Prisma Access Internal Gateway (Panorama) 

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

 Prisma Access Internal Gateway ( Panorama ) 

 Set up the Prisma Access internal gateway in Panorama. 

 In Panorama , set up GlobalProtect , add app settings , and onboard remote networks . 
 Notice that there are no internal host detection and internal gateway
 configurations at present. 

 Go to Panorama Cloud Services Configuration Remote Networks Settings . 

 Enable Internal Gateway and save the changes. 
 ( Optional ) Enable Prisma Access Internal Host
 Detection for IPv4 if you don't want to use your own DNS server.
 You can enable the internal host detection only after you
 select Enable Internal Gateway . 

 Prisma Access supports internal host detection
 only for the Always On 
 connect method . 

 When you enable the
 internal gateway, the remote network instances act as internal gateways.
 When you enable the internal host detection, Prisma Access creates
 PTR records on the remote network DNS proxy servers for the internal host
 detection process. 

 When you enable the internal gateway, Prisma Access creates an internal gateway configuration in a remote
 network template. 

 Go to Templates Network GlobalProtect Gateways and select Remote_Network_Template . 
 You will find the GlobalProtect_Internal_Gateway 
 template created for the internal gateway. 

 Create an authentication profile for this remote network template similar to
 the authentication profile in the mobile user template. 

 Select the remote network template,
 GlobalProtect_Internal_Gateway template,
 hyperlink. 

 Go to Authentication Client Authentication . 

 Edit the authentication profile details of the
 DEFAULT client authentication. 

 Create an
 authentication profile same as the one in the mobile user template. You
 can find the authentication profile used in the mobile user template
 under Template Device Authentication Profile . Ensure to select
 Mobile_User_Template . 

 You can also view the authentication profile
 for the remote network template by selecting Templates Device Authentication Profile . Select
 Remote_Network_Template . 

 Create a device certificate for the remote network template similar to the
 device certificate in the mobile user template. 

 Select the remote network template,
 GlobalProtect_Internal_Gateway ,
 hyperlink. 

 Go to Agent Client Settings . 

 Select the DEFAULT configuration, and go to
 Authentication Override settings. 

 Edit the Certificate to Encrypt/Decrypt Cookie 
 settings, and create a new device certificate. 

 Create a device
 certificate same as the one in the mobile user template. You can find
 the device certificate used in the mobile user template under Template Device Certificate Management Certificates Device Certificates . Ensure to select
 Mobile_User_Template . The
 DEFAULT configuration references the
 Authentication Cookie CA certificate. Follow
 the same hierarchy as the one in
 Mobile_User_Template for successful
 authentication. 

 You can also view the device certificate for
 the remote network template by selecting Template Device Certificate Management Certificates Device Certificates . Select
 Remote_Network_Template . 

 Push the changes to mobile users and remote networks at
 the same time.

---
url: https://docs.paloaltonetworks.com/prisma-sd-wan/administration/prisma-sd-wan-sites-and-devices/set-up-sites/configure-site-prefixes
fetched_at: 2026-09-16T07:47:52Z
source: strata-and-sase
---

# Configure a Site Prefix Clear

Updated on 

 Mon Aug 24 08:54:44 PDT 2026 

 Focus 

 Home 

 Prisma SD-WAN 

 Prisma SD-WAN Administrator’s Guide 

 Prisma SD-WAN Sites and Devices 

 Set Up Sites 

 Configure a Site Prefix 

 Download PDF 

 Prisma SD-WAN 

 Configure a Site Prefix 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma SD-WAN Docs 

 Activation & Onboarding 

 Administration 

 CloudBlades 

 Select a Document 

 CloudBlade Integrations 

 CloudBlades Integration with Prisma Access 

 Deployment 

 Incidents & Alerts 

 Reference 

 Release Notes 

 Select a Document 

 ION 6.8 

 ION 6.6 

 ION 6.5 

 ION 6.4 

 ION 6.3 

 ION 6.1 

 ION 5.6 

 Prisma SD-WAN Controller 

 Prisma SD-WAN On-Premises Controller 

 Prisma SD-WAN CloudBlades 

 Prisma Access CloudBlade Cloud Managed 

 Prisma Access CloudBlade Panorama Managed 

 New Features 

 Previous 

 Configure Secure SD-WAN Fabric Tunnels between Branch Sites 

 Next 

 Configure Ciphers 

 Configure a Site Prefix 

 You can configure site prefixes for branch sites, but the preferred method for
 advertising branch reachability is through the use of global scope interfaces and static
 routes. 

 Where Can I Use
 This? What Do I
 Need? 

 Prisma SD-WAN (Managed by Strata Cloud Manager ) 

 Prisma SD-WAN 

 Prisma SD-WAN uses site prefixes to advertise reachability from sites into the SD-WAN fabric.
 Site prefixes allow Prisma SD-WAN data center sites to easily advertise routes and
 reachability to branch sites. This can also be accomplished using globally scoped
 static routes in the data center ION devices, but for simplicity, configuring at the
 site level may be preferred. 

 You can configure site prefixes for branch sites, but
 the preferred method for advertising branch reachability is through the use of
 global scope interfaces and static routes. 

 Configure site prefixes to route traffic for a data center site. 

 Select Configuration Prisma SD-WAN Data Centers <Name of the site> . 

 In the Routing section, under IP
 Prefixes , click Manage IP Prefixes . 

 On the IP Prefixes screen, click Edit Add IP Prefix . You can add IPv4 and IPv6 addresses for prefixes and click
 Save . 

 Enter an IP Prefix and click Save . 

 (Optional) Click View Advertised IP Prefixes to
 view the list of Global IP prefixes and VRF Prefixes
 attached to the site . 

 Related CLIs 

 dump site config 

 Previous 

 Configure Secure SD-WAN Fabric Tunnels between Branch Sites 

 Next 

 Configure Ciphers

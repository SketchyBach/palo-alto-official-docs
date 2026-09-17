---
url: https://docs.paloaltonetworks.com/prisma-sd-wan/administration/prisma-sd-wan-sites-and-devices/set-up-devices/assign-a-device-to-a-shell
fetched_at: 2026-09-16T07:47:49Z
source: strata-and-sase
---

# Assign a Device to a Shell Clear

Updated on 

 Mon Aug 24 08:54:44 PDT 2026 

 Focus 

 Home 

 Prisma SD-WAN 

 Prisma SD-WAN Administrator’s Guide 

 Prisma SD-WAN Sites and Devices 

 Set Up Devices 

 Assign a Device to a Shell 

 Download PDF 

 Prisma SD-WAN 

 Assign a Device to a Shell 

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

 Switch From Non-FIPS to FIPS Mode 

 Next 

 Configure Device Access One-Time Password 

 Assign a Device to a Shell 

 Learn how to associate a device to a shell. 

 Where Can I Use This? What Do I Need? 

 Prisma SD-WAN (Managed by Strata Cloud Manager ) 

 Prisma SD-WAN 

 The ION device shell allows you to create elements, visualize the network, and do simple
 configurations. You can now pre-stage device configurations before the ION device
 becomes available to accelerate deployment. This new approach is referred to as the
 ‘Device Shell’. If there are device-related attributes in the template, then when
 deploying using the site template, enter the device serial number to which site it
 should be attached. If you don't have a physical device serial number or if the device
 isn’t available at the time of deployment, a virtual configuration–element shell–is
 created associating a device to the site. 

 When deploying a site using a site template, if you input the device serial number, and
 if the device is available, unclaimed, and online during the site deployment, it will be
 provisioned as part of the deployment process. However, if the physical device's serial
 number is unavailable or the device is inaccessible during deployment, a virtual
 configuration, Device Shell, is generated to preconfigure the device within the site.
 When the device is available, you can attach the physical device to this device shell to
 finalize the deployment of the site. 

 When a device is allocated to the tenant and is online, it can be assigned to the device
 shell at the site. At this point, the configuration from the device shell is transferred
 to the actual device, and the device shell is deleted. Refer Associate a Device with the Shell to know more. 

 Previous 

 Switch From Non-FIPS to FIPS Mode 

 Next 

 Configure Device Access One-Time Password

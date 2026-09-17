---
url: https://docs.paloaltonetworks.com/prisma/prisma-access/prisma-access-panorama-release-notes/prisma-access-about/upgrade-cloud-services-plugin
fetched_at: 2026-09-16T11:41:11Z
source: palo-alto-main
---

# Upgrade the Cloud Services Plugin Clear

Updated on 

 Fri May 29 15:04:04 PDT 2026 

 Focus 

 Home 

 Prisma 

 Prisma Access 

 Prisma Access Release Notes (Panorama Managed) 

 Prisma Access (Panorama Managed) Release Information 

 Upgrade the Cloud Services Plugin 

 Download PDF 

 Upgrade the Cloud Services Plugin 

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

 Previous 

 Changes to Default Behavior 

 Next 

 Prisma Access Known Issues 

 Upgrade the Cloud Services Plugin 

 After reviewing the Prisma Access Known Issues , use the following
procedure to upgrade the Cloud Services plugin. 

 If
this is the first time you are installing the plugin, refer to License and Install the Prisma
Access Components for instructions. 

 Prisma Access
uses the Cloud Services plugin in Panorama to activate its functionality. 

 For
a list of the Panorama software versions that are supported with
Prisma Access, see Minimum Required Panorama Software
Versions in the Palo Alto Networks Compatibility
Matrix . 

 Before you upgrade the plugin, remove any non-Prisma
Access templates from Prisma Access template stacks to avoid commit
validation errors after upgrade and make sure that the Panorama
that manages Prisma Access is running a supported PAN-OS version. 

 Use
one of the following tasks to download and install the Cloud Services
plugin. 

 HA Deployments Only —If you have two
Panorama appliances configured in High Availability (HA) mode ,
install the plugin on the Primary HA pair first, then the Secondary. 

 Determine the upgrade path for the plugin to which you want to upgrade. 

 For some upgrade paths, you need to upgrade your plugin sequentially. For
 example, to upgrade from a 2.2 Preferred plugin to a 3.2 or 3.2.1 plugin,
 you must first perform interim upgrades to 3.0 and 3.1 before upgrading to
 3.2 or 3.2.1. 

 Download and install the Cloud Services plugin versions
you require. 

 To download and install the Cloud Services plugin
by downloading it from the Customer Support Portal, complete the
following steps. 

 Log in to the Customer Support Portal and select Software
Updates , 

 Find the Cloud Services plugin in the Panorama Integration
Plug In section and download it. 

 Do not rename the
plugin file or you will not be able to install it on Panorama. 

 Log in to the Panorama Web Interface of the Panorama you
licensed for use with the Prisma Access, select Panorama Plugins Upload and Browse for
the plugin File that you downloaded from the
CSP. 

 Install the plugin. 

 To download and install the new version of the Cloud Services
plugin directly from Panorama, complete the following steps: 

 Select Panorama Plugins and
click Check Now to display the latest Cloud
Services plugin updates. 

 Download the plugin version you want
to install. 

 After downloading the plugin, Install it. 

 Commit Commit
and Push your changes. 

 Previous 

 Changes to Default Behavior 

 Next 

 Prisma Access Known Issues

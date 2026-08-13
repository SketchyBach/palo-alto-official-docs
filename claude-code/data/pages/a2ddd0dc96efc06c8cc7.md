---
url: https://docs.paloaltonetworks.com/ngfw/help/10-2/panorama-web-interface/panorama-device-deployment/manage-software-and-content-updates
fetched_at: 2026-08-13T16:44:33Z
source: palo-alto-main
---

# Manage Software and Content Updates Clear

Manage Software and Content Updates 

 Home 

 EN

 Location 

 Documentation Home 

 Palo Alto Networks 

 Support 

 Live Community 

 Knowledge Base 

 >

 Strata Copilot

 Manage Software and Content Updates 

 Updated on 

 Thu Jun 25 17:37:48 PDT 2026 

 Focus 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 한국어 (Korean) 

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

 Updated on 

 Thu Jun 25 17:37:48 PDT 2026 

 Focus 

 Home 

 Next-Generation Firewall 

 Panorama Web Interface 

 Panorama > Device Deployment 

 Manage Software and Content Updates 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 한국어 (Korean) 

 Next-Generation Firewall 

 Manage Software and Content Updates 

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

 Previous 

 Panorama > Device Deployment 

 Next 

 Display Software and Content Update Information 

 Manage Software and Content Updates 

 Panorama > Device Deployment
> Software 

 Panorama provides the following options for deploying software
and content updates to firewalls and Log Collectors. 

 To reduce traffic on the management (MGT)
interface, you can configure Panorama to use a separate interface
for deploying updates (see Panorama
> Setup > Interfaces ). 

 Panorama Device Deployment Options 

 Description 

 Download 

 To deploy a software or content update when
Panorama is connected to the Internet, Download the
update. When the download finishes, the Available column displays
Downloaded. You can then: 

 Install the
PAN-OS/Panorama software update or content update. 

 Activate the
GlobalProtect™ app or SSL VPN Client software update. 

 Upgrade 

 If a BrightCloud URL Filtering content update
is available, click Upgrade . After a successful
upgrade, you can Install the
update on firewalls. 

 Install 

 After you Download or Upload a
PAN-OS software, Panorama software, or content update, click Install in
the Action column and select: 

 Devices —Select
the firewalls or Log Collectors on which to install the update. If
the list is long, use the Filters. Select Group HA Peers to
group firewalls that are high availability (HA) peers. This enables
you to easily identify firewalls that have an HA configuration.
To display only specific firewalls or Log Collectors, select them
and then Filter Selected . 

 Upload only to device ( software
only )—Select to load the software without automatically installing
it. You must manually install the software. 

 Reboot device after install ( software
only )—Select to specify that the installation process automatically
reboots the firewalls or Log Collectors. The installation cannot
finish until a reboot occurs. 

 Disable new apps in content update ( Applications
and Threats only )—Select to disable applications in the update
that are new relative to the last installed update. This protects
against the latest threats while giving you the flexibility to enable
applications after preparing any policy updates. Then, to enable
applications, log in to the firewall, select Device Dynamic Updates , click Apps in
the Features column to display the new applications, and click Enable/Disable for
each application you want to enable. 

 You
can also select Panorama Managed
Devices to install Firewall
Software and Content Updates or Panorama Managed Collectors to install Software
Updates for Dedicated Log Collectors . 

 Activate 

 After you Download or Upload a
GlobalProtect app software update, click Activate in
the Action column and select the options as follows: 

 Devices —Select
the firewalls on which to activate the update. If the list is long,
use the Filters. Select Group HA Peers to group firewalls
that are high availability (HA) peers. This enables you to easily
identify firewalls that have an HA configuration. To display only
specific firewalls, select them and then Filter Selected . 

 Upload only to device —Select if you
don’t want PAN-OS to automatically activate the uploaded image.
You must log in to the firewall and activate it. 

 Revert 

 Software Patches only 

 PAN-OS 10.2.8 and later releases 

 Uninstall the PAN-OS software patch currently installed on managed
 firewalls and Log Collectors. 

 Release Notes 

 PAN-OS 10.2.7 and earlier releases 

 Click Release Notes to
access the release notes for the desired software release and review
the release changes, fixes, known issues, compatibility issues,
and changes in default behavior. 

 Documentation 

 PAN-OS 10.2.8 and later releases 

 Click Release Notes to access the release notes for the desired
 software release and review the release changes, fixes, known issues, compatibility issues,
 and changes in default behavior. 

 ( Software Patches only ) Click More Info to view additional
 details about the PAN-OS software patch impact and restart requirements. 

 Deletes software or content updates when
no longer needed or when you want to free up space for more downloads
or uploads. 

 Check Now 

 Check Now to Display
Software and Content Update Information . 

 Upload 

 To deploy a software or content update when
Panorama is not connected to the Internet, download the update to
your computer from the Software Updates or Dynamic Updates site,
select the Panorama Device
Deployment page that corresponds to the
update type, click Upload , select the update Type ( content
updates only ), select the uploaded file, and click OK .
The steps to then install or activate the update depend on the type: 

 PAN-OS or Panorama software —When the upload is complete,
the Downloaded column displays check mark and you can the Action
column displays Install . 

 GlobalProtect Client or SSL VPN Client software —Activate
from file. 

 Dynamic updates —Install from file. 

 Preferred Releases 
 ( PAN-OS 10.2.10 and later 10.2
 releases ) 
 Select the Preferred Releases checkbox to view the
 list of preferred releases. Preferred releases offer the latest and advanced features. Ensure
 that you use preferred releases for stability and optimal performance. 
 By default, both
 preferred and base releases are selected. 

 If Panorama does not have access
 to the external network, use a browser to visit the Software Update site to view the preferred releases. 

 Base Releases 
 ( PAN-OS 10.2.10 and later 10.2
 releases ) 

 Select the Base Releases checkbox to view the list of
 base releases. A base release is the earliest version of a specific release. 

 By default, both preferred and base releases are selected. 

 If Panorama does not have access to the external network, use a browser to visit
 the Software Update site to view the base releases. 

 Include Patch 

 PAN-OS 10.2.8 and later releases 

 Check (enable) to include PAN-OS software patches in the list of PAN-OS
 software versions. 

 Install from File 

 After you upload a content update, click Install
from File , select the content Type ,
select the filename of the update, and select the firewalls or Log Collectors. 

 Activate from File 

 After you upload a GlobalProtect app software
update, click Activate from File , select
the filename of the update, and select the firewalls. 

 Schedules 

 Select to Schedule
Dynamic Content Updates . 

 Previous 

 Panorama > Device Deployment 

 Next 

 Display Software and Content Update Information 

 On This Page 

 Activation & Onboarding 

 Strata Cloud Manager 

 Activate a License or Product 

 Cloud Identity Engine 

 Strata Logging Service 

 Device Associations 

 Hub 

 Identity and Access Management 

 Tenant Management 

 Next-Generation Firewalls 

 AIOps for NGFW 

 Cloud Management for NGFWs 

 Cloud NGFW for AWS 

 Cloud NGFW for Azure 

 CN-Series 

 Firewalls 

 PAN-OS 

 PAN-OS SD-WAN 

 Service Provider 

 VM-Series 

 SASE 

 Prisma Access 

 Strata Multitenant Cloud Manager 

 AI-Powered ADEM 

 Prisma Access Monitoring and Visibility 

 Prisma SD-WAN 

 ION Devices 

 Next-Generation CASB 

 Cloud-Delivered Security Services 

 Advanced WildFire 

 Advanced URL Filtering 

 Advanced Threat Prevention 

 Advanced DNS Security 

 Device Security 

 Enterprise DLP 

 SaaS Security 

 Network Security 

 Shared Policy for NGFWs and Prisma Access 

 Visibility & Monitoring 

 Dashboards 

 Incidents and Alerts 

 Reports 

 Autonomous DEM 

 Best Practices 

 Best Practices Library 

 Experts Corner 

 Solutions Docs from Product Experts 

 PAN-OS 

 10.2 

 Next-Generation Firewall 

 Help 

 Web Interface 

 Panorama 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

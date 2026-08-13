---
url: https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-admin/certifications/enable-fips-and-common-criteria-support/change-the-operational-mode-to-fips-cc-mode
fetched_at: 2026-08-13T17:08:47Z
source: palo-alto-main
---

# Change the Operational Mode to FIPS-CC Mode Clear

Change the Operational Mode to FIPS-CC Mode 

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

 Change the Operational Mode to FIPS-CC Mode 

 Updated on 

 Aug 3, 2026 

 Focus 

 Download PDF 

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

 Aug 3, 2026 

 Focus 

 Home 

 Next-Generation Firewall 

 Certifications 

 Change the Operational Mode to FIPS-CC Mode 

 Download PDF 

 Next-Generation Firewall 

 Change the Operational Mode to FIPS-CC Mode 

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

 Access the Maintenance Recovery Tool (MRT) 

 Next 

 FIPS-CC Security Functions 

 Change the Operational Mode to FIPS-CC Mode 

 Switch the firewall or appliance to FIPS-CC mode in order to comply with the Common
 Criteria and the Federal Information Processing Standards. 

 Where Can I Use This? What Do I Need? 

 NGFW (Managed by PAN-OS or Panorama) 

 No prerequisites needed 

 The following procedure describes how to change
the operational mode of a Palo Alto Networks product from normal
mode to FIPS-CC mode. 

 When the appliance
is in FIPS-CC mode, you will not be able to configure any settings
via the console, including the management interface settings. Before enabling
FIPS-CC mode, make sure that your network is set up to allow access
to the management interface via SSH or the web interface. The management
interface will default to a static address of 192.168.1.1 if using
a PA-Series firewall or to an address retrieved via DHCP if it is
a VM-Series firewall. The WildFire, virtual Panorama, and M-series
Panorama appliances will default to a static address of 192.168.1.1. 

 Once FIPS-CC mode is enabled, all configurations
and settings are erased. If an administrator has configurations
or settings they would like to reuse after FIPS-CC mode is enabled,
the administrator can save and export the configuration before changing
to FIPS-CC mode. The configuration can then be imported once the
operational mode change is complete. The imported configuration
must be edited per the FIPS-CC Security Functions or
else the import process will fail. 

 Keys, passwords,
and other critical security parameters cannot be shared across modes. 

 If
you change the operational mode of a firewall or Dedicated Log Collector managed
by a Panorama management server to FIPS-CC mode, you must also change
the operational mode of Panorama to FIPS-CC mode. This is required
to secure password hashes for local admin passwords pushed from
Panorama. 

 ( Existing HA Configuration only ) Disable
the high availability (HA) configuration. 
 This is required to successfully change the operational mode
to FIPS-CC mode for firewalls already in an HA configuration. 

 Log in to the firewall web interface of the primary
HA peer. 

 Select Device High Availability General and
edit the HA Pair Settings Setup. 

 Uncheck (disable) Enable HA and
click OK . 

 Commit . 

 ( Public Cloud VM-Series firewalls or Public Cloud
Panorama Virtual Appliances only ) Create an SSH key and log
in to the firewall or Panorama. 

 On some public cloud platforms, such as Microsoft Azure,
you must have an SSH key to prevent an authentication failure after
changing to FIPS-CC mode. Verify that you have deployed the firewall
to authenticate using the SSH key. Although on Azure you can deploy
the VM-Series firewall or Panorama and log in using a username and
password, you will be unable to authenticate using the username
and password after changing the operational mode to FIPS-CC. After
resetting to FIPS-CC mode, you must use the SSH key to log in and
can then configure a username and password that you can use for
subsequently logging in to the firewall web interface. 

 Connect to the firewall or appliance and Access the Maintenance Recovery Tool (MRT) . 

 Select Set FIPS-CC Mode from the
menu. 

 Select Enable FIPS-CC Mode . The
mode change operation begins a full factory reset and a status indicator
shows the progress. After the mode change is complete, the status
shows Success . 

 All configurations and settings
are erased and cannot be retrieved once the mode change is complete. 

 When prompted, select Reboot . 

 If you change the operational mode
on a VM-Series firewall deployed in the public cloud and you lose
your SSH connection to the MRT before you are able to Reboot ,
you must wait 10-15 minutes for the mode change to complete, log
back into the MRT, and then reboot the firewall to complete the
operation. After resetting to FIPS-CC mode, on some virtual form
factors (Panorama or VM-Series) you can only log in using the SSH
key, and if you have not set up authentication using an SSH key,
you can no longer log in to the firewall on reboot. 

 After
you switch to FIPS-CC mode, you see the following status: FIPS-CC mode enabled successfully . 

 In
addition, the following changes are in effect: 

 FIPS-CC
displays at all times in the status bar at the bottom of the web
interface. 

 The default administrator login credentials change to admin/paloalto. 

 See FIPS-CC Security Functions for
details on the security functions that are enforced in FIPS-CC mode. 

 ( Existing HA only ) Re-enable HA. 

 This step is required for firewalls that were configured
in HA before changing to FIPS-CC mode. 

 See High Availability for
more information on setting up HA for the first time. 

 Log in to the firewall web interface of the primary
HA peer. 

 Select Device High Availability General and
edit the HA Pair Settings Setup. 

 Check (enable) Enable HA and
click OK . 

 Commit . 

 Enable encryption for the HA1 control link . 

 This is required for all firewalls in FIPS-CC mode in an
HA configuration. 

 To successfully leverage HA for firewalls
in FIPS-CC mode, you must set automatic rekeying parameters and
must set the data parameter to a value no greater than 1000 MB.
You cannot let the key default and must set a time interval (you
cannot leave it disabled). 

 Previous 

 Access the Maintenance Recovery Tool (MRT) 

 Next 

 FIPS-CC Security Functions 

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

 Network Security 

 PAN-OS 

 Next-Generation Firewall 

 Administration 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

---
url: https://docs.paloaltonetworks.com/iot/integration/asset-management/integrate-iot-security-with-nuvolo/set-up-iot-security-and-xsoar-for-nuvolo-integration
fetched_at: 2026-08-13T16:36:55Z
source: palo-alto-main
---

# Set up Device Security and XSOAR for Nuvolo Integration Clear

Set up Device Security and XSOAR for Nuvolo Integration 

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

 Set up Device Security and XSOAR for Nuvolo Integration 

 Updated on 

 Thu May 14 09:23:33 PDT 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Device Security Docs 

 Activation & Onboarding 

 Getting Started 

 Administration 

 Enterprise Administration 

 Integrations 

 Release Notes 

 Best Practice 

 New Features 

 Updated on 

 Thu May 14 09:23:33 PDT 2026 

 Focus 

 Home 

 Device Security 

 Device Security Integration Guide 

 Asset Management 

 Integrate Device Security with Nuvolo 

 Set up Device Security and XSOAR for Nuvolo Integration 

 Download PDF 

 Device Security 

 Set up Device Security and XSOAR for Nuvolo Integration 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Device Security Docs 

 Activation & Onboarding 

 Getting Started 

 Administration 

 Enterprise Administration 

 Integrations 

 Release Notes 

 Best Practice 

 New Features 

 Previous 

 Set up Nuvolo for Integration 

 Next 

 Send Security Alerts to Nuvolo 

 Set up Device Security and XSOAR for Nuvolo Integration 

 Set up Device Security and Cortex XSOAR to integrate with
Nuvolo. 

 Where Can I Use This? What Do I Need? 

 Device Security (Managed by Strata Cloud Manager) 

 (Legacy) IoT Security (Standalone portal) 

 One of the following subscriptions: 

 Device Security subscription for an advanced
 Device Security product (Enterprise Plus,
 Industrial OT, or Medical)

 Device Security X subscription

 One of the following Cortex XSOAR setups:

 A free, cohosted, limited-featured
 Cortex XSOAR instance

 A full-featured Cortex XSOAR server

 To set up Device Security to integrate through
 Cortex XSOAR with Nuvolo, you need the following: 

 The
username and password of a user account that allows XSOAR to send
device data and security events through the Nuvolo API to the Clinical
Devices table you created 

 The source_key for the data source, which acts as a second
factor of authentication for the Nuvolo API 

 The URL of your Nuvolo instance 

 Log in to Device Security and then access
Nuvolo settings in Cortex XSOAR . 

 Log in to Device Security and then click Integrations . 

 Because Device Security uses XSOAR to integrate with Nuvolo, you must configure settings for
 the Nuvolo instance in the Cortex XSOAR interface. To access XSOAR,
 click Launch Cortex XSOAR . 

 Click Settings in the left navigation
menu, search for nuvolo to locate it among
other instances. 

 Configure the Nuvolo integration instance. 

 Click the integration instance settings icon ( 

 ) for PANW IoT
3rd Party Nuvolo Integration Instance to open the settings panel. 

 Enter the following and leave other settings at their default
values: 

 Do not change the default integration instance
name (PANW IoT 3rd Party Nuvolo Integration Instance). XSOAR jobs
for Nuvolo use playbooks that refer to this integration instance
name specifically. 

 Nuvolo Server URL :
Enter the URL of the Nuvolo instance. 

 You must include
a slash ( / ) at the end of the Nuvolo server URL; for example: https://ven01234.service-now.com/ 

 Source
key : Enter the source key you saved when configuring
Nuvolo. 

 Username : Enter the username
of the user account you created on Nuvolo. 

 Password :
Enter the password associated with the user account. 

 Use
single engine : Choose No engine . 

 When finished, click Run test or Test . 

 If
the test is successful, a Success message appears. If not, check
that the settings were entered correctly and then test the configuration
again. 

 After the test succeeds, click Save & exit to
save your changes and close the settings panel. 

 To enable the PANW IoT 3rd Party Nuvolo Integration Instance,
click Enable . 

 XSOAR begins an automated process that sends Nuvolo incrementally
updated data from Device Security about changes to device attributes
occurring within the last 15 minutes. 

 Return to Device Security and check the status
of the Nuvolo integration. 

 XSOAR automatically runs a preconfigured job for Nuvolo
integration and reports the integration instance to Device Security ,
which displays it on the Integrations page. The integration instance
can be in one of the following four states as shown in the Status
column on the Integrations page: 

 Disabled means
that either the integration was configured but intentionally disabled
or it was never configured and a job that references it is enabled
and running. 

 Error means that the integration was
configured and enabled but is not functioning properly, possibly
due to a configuration error or network condition. 

 Inactive means that the integration
was configured and enabled but no job has run for at least the past
60 minutes. 

 Active means that the integration
was configured and enabled and is functioning properly. 

 When
you see that its status has changed from Disabled to Active ,
the setup of the integration instance is complete. 

 The
status in Device Security doesn’t change immediately after you enable
the instance in XSOAR. Device Security updates the status when it receives
a report back from XSOAR after it successfully runs the next incremental
device export job to Nuvolo. 

 Export the IoT medical device inventory from Device Security 
to Nuvolo. 

 Although regular, automated incremental updates are now
in progress, Nuvolo doesn’t yet have a complete medical IoT device
inventory from Device Security . This requires a bulk data export from
 Device Security to Nuvolo that you initiate from the XSOAR interface.
The process is somewhat time consuming; for example, exporting an
inventory of 30,000-40,000 medical IoT devices can take up to 36
hours. 

 To start a bulk export of the entire medical IoT device inventory, click Launch
 Cortex XSOAR to return to the XSOAR
 interface. Click Jobs , select the preconfigured job
 PANW IoT Bulk Export to Nuvolo , and then click
 Run now . 

 During
the bulk export and after the job completes, the automated incremental
update will continue running every 15 minutes. 

 Import IoT medical device data from Nuvolo into Device Security . 

 Consider importing medical IoT device data from Nuvolo
regularly. How often you run this job largely depends on how often
there are changes to the medical IoT devices on your network. You
might start by running this once a month and then either increase
or decrease the frequency as necessary. 

 Before importing any
device data from Nuvolo, Cortex XSOAR gets a list of MAC addresses
for all the medical IoT devices in the Device Security inventory—and
IP addresses for any medical IoT devices with a static IP address
whose MAC address is unknown to Device Security . Then, when XSOAR requests
device data from Nuvolo, it only requests data for the devices identified in
the list. 

 To start a bulk import of device data from Nuvolo for the medical IoT devices in the Device Security inventory, click Launch Cortex XSOAR to return to the XSOAR interface. Click
 Jobs , select the preconfigured job
 Nuvolo Bulk Importing Device to PANW IoT Cloud ,
 and then click Run now . 

 During
the bulk import and after the job completes, the automated incremental
update will continue running every 15 minutes. 

 Previous 

 Set up Nuvolo for Integration 

 Next 

 Send Security Alerts to Nuvolo 

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

 Firewalls 

 PAN-OS 

 PAN-OS SD-WAN 

 Service Provider 

 VM-Series 

 SASE 

 Prisma Access 

 Strata Multitenant Cloud Manager 

 Device Security 

 Cloud-Delivered Security Services 

 Integrations 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

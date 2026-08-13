---
url: https://docs.paloaltonetworks.com/iot/integration/network-management/integrate-iot-security-with-cisco-prime/set-up-iot-security-and-xsoar-for-cisco-prime-integration
fetched_at: 2026-08-13T16:37:22Z
source: palo-alto-main
---

# Set up Device Security and XSOAR for Cisco Prime Integration Clear

Set up Device Security and XSOAR for Cisco Prime Integration 

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

 Set up Device Security and XSOAR for Cisco Prime Integration 

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

 Network Management 

 Integrate Device Security with Cisco Prime 

 Set up Device Security and XSOAR for Cisco Prime Integration 

 Download PDF 

 Device Security 

 Set up Device Security and XSOAR for Cisco Prime Integration 

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

 Set up Cisco Prime to Accept Connections from Device Security 

 Next 

 Integrate Device Security with HPE Juniper Networking Mist AI 

 Set up Device Security and XSOAR for Cisco Prime Integration 

 Set up Device Security and Cortex XSOAR to integrate with
Cisco Prime Infrastructure. 

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

 AND 

 A free Cortex XSOAR Engine (on-premises integration)

 A full-featured Cortex XSOAR server

 To set up Device Security to integrate through
 Cortex XSOAR with Cisco Prime Infrastructure, you must add a Cortex XSOAR engine to your network. 

 You must also configure the
Cisco Prime integration instance in XSOAR. To do this, you need
the IP address of your Cisco Prime system and the username and password
of the NBI read-only user account that the Cortex XSOAR engine will use
when forming a secure connection with Prime. 

 Cortex XSOAR Engine Installation 

 The Cortex XSOAR engine initiates connections
to Cisco Prime Infrastructure and to the Cortex cloud and provides
the means through which they communicate with each other. Although
it's possible to install a Cortex XSOAR engine on machines running Windows,
macOS, and Linux operating systems, only an engine on a Linux machine
supports Device Security integrations. For more information about operating
system and hardware requirements, see the Cortex XSOAR . 

 We recommend downloading the Cortex XSOAR engine using the shell
 installer script and installing it on a Linux machine. This simplifies the
 deployment by automatically installing all required dependencies and also
 enables remote engine upgrades.

 When
placing the Cortex XSOAR engine on your network, make sure it can form
HTTPS connections to your Cisco Prime system on TCP port 443. The
XSOAR engine uses TCP 443 when authenticating with Cisco Prime and
 requesting and receiving device data. 

 The on-premises firewall must allow the Cortex XSOAR engine to form
 HTTPS connections on TCP port 443 to the Cortex cloud at
 https://<your-domain>.iot.demisto.live/. You can see the URL of your
 Cortex XSOAR instance when you log in to Device Security 
 and click Integrations and then click Launch
 Cortex XSOAR . It’s visible in the address bar
 of the web page displaying the Cortex XSOAR interface.

 To create an Cortex XSOAR engine, access the Cortex XSOAR 
 interface (from Device Security , click
 Integrations and then click Launch
 Cortex XSOAR ). In the Cortex XSOAR UI,
 click Settings Engines + Create New Engine . Choose
 Shell as the type.

 For Cortex XSOAR engine installation instructions, see Engine Installation .

 For help troubleshooting Cortex XSOAR engines, including installations,
 upgrades, connectivity, and permissions, see Troubleshoot Engines and Troubleshoot Integrations Running on
 Engines .

 Configure Device Security and Cortex XSOAR 

 Log in to Device Security and from there
access Cisco Prime settings in Cortex XSOAR . 

 Log in to Device Security and then click Integrations . 

 Device Security uses Cortex XSOAR to integrate with Cisco Prime, and the settings you
 must configure to integrate with Prime are in the XSOAR
 interface. To access these settings, click Launch
 Cortex XSOAR . 

 The Cortex XSOAR interface opens
in a new browser window. 

 Click Settings in the left navigation
menu, search for cisco prime to locate it
among other instances. 

 Configure the Cisco Prime instance. 

 Click Add instance to open
the settings panel. 

 Enter the following and leave other settings at their default
values: 

 Name : Use the default name
of the instance (Cisco Prime_instance_1) or enter a new one. 

 Remember
the instance name because you are going to use it again when creating
jobs that Cortex XSOAR will run. 

 Cisco Prime
Server URL : Enter the Cisco Prime Server URL. 

 Cisco
Prime username : Enter the name of the NBI read-only
user account you previously created in Cisco Prime. 

 Password :
Enter the password associated with the user account. 

 Run
on Single engine : Choose the Cortex XSOAR engine that you want
to communicate with the Cisco Prime system. 

 When finished, click Run test or
 Test . 

 If the test is successful, a Success message appears. If not, check
 that the settings were entered correctly and then test the
 configuration again. 

 After the test succeeds, click Save &
 exit to save your changes and close the settings
 panel. 

 To enable Cisco Prime Integration Instance, click Enable . 

 Create a job for XSOAR to get a list of MAC addresses
of active devices from Device Security and then query Cisco Prime for
details about the devices in the list. 

 Device Security and XSOAR only request details from
Prime if a device has a MAC address. If your network has static
IP devices without MAC addresses, they will not be included. 

 Copy
the name of the instance you just created, navigate to Jobs, and
then click New Job at the top of the page. 

 In the New Job
panel that appears, enter the following and leave the other settings
at their default values: 

 Recurring :
Select this because you want to periodically poll Cisco Prime for
device details. 

 Every : Enter a number
and set the interval value (Minutes, Hours, Days, or Weeks) and
select the days on which to run the job. This determines how often
XSOAR sends a list of MAC addresses of currently active devices
from Device Security to Cisco Prime and receives device details in
response. 

 As a general rule of thumb, this job takes
about 15 minutes per 1000 devices to complete. Other factors that
might affect the time required to complete a job are the Cisco DNA
Center API processing speed and settings. 

 Name :
Enter a name for the job. 

 Playbook :
Choose Cisco Prime Clients . 

 Integration
Instance Name : Paste the instance name you copied a
few moments ago. 

 Playbook Poll Interval :
Enter a number (the value, though unspecified, is minutes) defining
the period of time during which Device Security must see device activity
to include it in the list of currently active devices it provides
to XSOAR. It’s common to use the same interval as the one above
for running the recurring job. 

 Site Names :
By default, the XSOAR retrieves device data from all sites that
 Device Security manages. If there are multiple sites and you want to
get device data from a subset of them or Cisco Prime is managing
a subset of them, specify them by name here. Separate multiple names with
commas. Use quotation marks around names with spaces. Because the
 Cortex XSOAR UI opens in a new browser window, you can return to
the previous window with the Device Security portal and navigate to Administration Sites and Firewalls Sites to view a list of site
names. 

 Click Create
new job . 

 The job appears at the bottom of the
Jobs list. 

 Enable the job and run it. 

 Check the Job Status for the job you created. If it’s Disabled,
select its check box and then click Enable . 

 After
you enable it, keep the check box selected and click Run
now . The Run Status changes from Idle to Running. In
addition, running a job in XSOAR triggers the referenced integration
instance to appear on the Integrations page in the Device Security 
portal. 

 At the defined interval, XSOAR begins the job by first
requesting an active device list from Device Security and then using
that list to query Cisco Prime for client details, which it forwards
to the Device Security cloud. 

 If you have multiple Prime instances, add more jobs as
necessary. 

 To add another, click Add instance ,
configure the settings as previously explained, and then click Done. 

 You
can configure multiple instances with different Cortex XSOAR engines retrieving
device information from the same Cisco Prime server. However, a
single engine cannot retrieve information from multiple servers. 

 Run
each job you create at least once to populate the Integrations page
with all the integration instances you’re using in XSOAR. 

 Return to Device Security and check the status
 of the Cisco Prime integration. 

 An integration instance can be in one of the following four states, which
 Device Security displays in the Status column on the Integrations page:

 Active — the integration was
 configured and enabled and is functioning properly.

 Disabled — either the integration
 was configured but intentionally disabled or it was never configured
 and a job that references it is enabled and running.

 Error — the integration was
 configured and enabled but is not functioning properly, possibly due
 to a configuration error or network condition.

 Inactive — the integration was
 configured and enabled but no job has run for at least the past 60
 minutes.

 When you see that the status of an integration instance is Active ,
 its setup is complete.

 Previous 

 Set up Cisco Prime to Accept Connections from Device Security 

 Next 

 Integrate Device Security with HPE Juniper Networking Mist AI 

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

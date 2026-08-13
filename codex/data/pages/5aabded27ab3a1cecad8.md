---
url: https://docs.paloaltonetworks.com/iot/integration/asset-discovery/integrate-iot-security-with-rockwell-automation-assetcentre/set-up-iot-security-and-xsoar-for-assetcentre-integration
fetched_at: 2026-08-13T16:36:50Z
source: palo-alto-main
---

# Set up Device Security and XSOAR for AssetCentre Integration Clear

Set up Device Security and XSOAR for AssetCentre Integration 

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

 Set up Device Security and XSOAR for AssetCentre Integration 

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

 Asset Discovery 

 Integrate Device Security with Rockwell Automation AssetCentre 

 Set up Device Security and XSOAR for AssetCentre Integration 

 Download PDF 

 Device Security 

 Set up Device Security and XSOAR for AssetCentre Integration 

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

 Set up AssetCentre for Integration 

 Next 

 Learn Device Attributes by Polling 

 Set up Device Security and XSOAR for AssetCentre Integration 

 Set up Device Security and Cortex XSOAR to integrate with AssetCentre. 

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

 To set up Device Security to integrate through Cortex XSOAR with AssetCentre, configure
 XSOAR with a Rockwell AssetCentre integration instance and jobs to import device
 data. You can set the job to import device data incrementally to run at regular
 intervals. The configuration requires the following information from
 AssetCentre: 

 IP address or hostname, port number, and name of the Microsoft SQL server 

 Username and password of the Windows Active Directory user account that XSOAR
 uses when connecting to the Microsoft SQL server 

 When using a cohosted XSOAR instance, a cloud-hosted XSOAR server, or an
 on-premises XSOAR server that cannot reach part of the network, you must also add a
 Cortex XSOAR engine to your network. 

 Cortex XSOAR Engine Installation 

 When using a cohosted XSOAR instance, a cloud-hosted XSOAR server, or an on-premises XSOAR server that cannot reach part of the network, XSOAR communicates with AssetCentre through an on-premises Cortex XSOAR XSOAR engine. Although it's possible to install a Cortex XSOAR engine on machines running Windows, macOS, and Linux operating systems, only an engine on a Linux machine supports Device Security integrations. For more information about operating system and hardware requirements, see the Cortex Administrator’s Guide . 

 We recommend downloading the Cortex XSOAR engine using the shell
 installer script and installing it on a Linux machine. This simplifies the
 deployment by automatically installing all required dependencies and also
 enables remote engine upgrades.

 When placing the Cortex XSOAR engine on your network, make sure it can form connections to your AssetCentre system on the TCP port on which it’s listening for connection requests. The default port number is TCP 1433. 

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

 Log in to Device Security and from there access AssetCentre settings in
 Cortex XSOAR . 

 Log in to Device Security and then click
 Integrations . 

 Device Security uses Cortex XSOAR to integrate with
 AssetCentre, and the settings you must configure to integrate
 Device Security with it are in the XSOAR interface. To
 access these settings, click Launch Cortex XSOAR . 

 The Cortex XSOAR interface opens in a new browser
 window. 

 Click Settings in the left navigation
 menu, search for assetcentre to locate it among
 other instances. 

 Configure the Rockwell AssetCentre integration instance. 

 Click Add instance to open the settings
 panel. 

 Enter the following and leave the other settings at their default
 values: 

 Name : Either use the default
 name (Rockwell AssetCentre_instance_1) or enter a new one. 

 Remember the instance name because you are going to use it
 again when creating a job that Cortex XSOAR will run to
 gather data from the SQL database specified in this
 integration instance. 

 SQL Server Host/IP : Enter the
 domain name or IP address of the Microsoft SQL server. 

 SQL Server Port : Enter the
 default TCP port number 1433 or, if a different port number is
 set on the SQL server, enter that. 

 SQL Database : Enter the name of the
 database from which you want XSOAR to retrieve device
 information. 

 Each integration instance can retrieve device information
 from a single database. If you want to retrieve device
 information from other databases, you must create additional
 integration instances for them. 

 Username : Enter the name of the
 user account you previously configured for XSOAR to access the
 Microsoft SQL server. 

 Password : Enter the password
 associated with the user account. 

 Run on Single engine : Choose the XSOAR
 engine that you want to communicate with the Microsoft SQL
 server. 

 When finished, click Run test or
 Test . 

 If the test is successful, a Success message appears. If not, check
 that the settings were entered correctly and then test the
 configuration again. 

 After the test succeeds, click Save &
 exit to save your changes and close the settings
 panel. 

 To enable the Rockwell FactoryTalk AssetCentre integration instance, click
 Enable . 

 Create a job for XSOAR to retrieve information about devices in the
 AssetCentre SQL database specified in the integration instance and then
 forward it to Device Security . 

 Copy the name of the integration instance and open a
 duplicate browser window. 

 Navigate to Jobs in the new window, and then click
 New Job at the top of the page. 

 In the New Job panel that appears, enter the following
 and leave the other settings at their default values: 

 Time triggered : (select) 

 Recurring : Select this because
 you want to periodically import device information from
 AssetCentre. 

 Every : Enter a number and set
 the interval value (Minutes, Hours, Days, or Weeks) and select
 the days and times on which to run the job. This determines how
 often and when XSOAR retrieves data from AssetCentre. Consider
 running the job every day or every other day at a time when
 network activity is light, such as late at night, to help reduce
 potential latency. As a general guideline, it takes
 approximately 20 minutes for XSOAR to import data for 10,000
 devices into Device Security . You can see the run status of a
 recurring job on the Jobs page and note how long it takes. When
 in progress, its status is Running . When
 done, its status changes to
 Completed . 

 Name : Enter a name for the
 job. 

 Playbook : Choose
 Import Rockwell AssetCentre devices to PANW IoT
 cloud . 

 Integration Instance Name : Paste
 the name of the integration instance that you copied
 earlier. 

 Playbook Poll Interval : If you
 want to import device information incrementally from
 AssetCentre, enter a number indicating the period of time that
 XSOAR polls AssetCentre for any newly discovered devices or new
 or different attributes for previously discovered devices. The
 value you enter, though unspecified, is minutes. When XSOAR runs
 the next job, it then imports the devices and attributes to Device Security that AssetCentre discovered during this
 interval. It’s common to use the same interval as the one for
 running the recurring job. However, if you increase the interval
 between jobs, you can set a shorter interval for polling than
 that for the job. 

 If you leave it blank, Cortex XSOAR imports all
 available device attributes each time the job runs the playbook.
 XSOAR then uploads whatever is new or has changed since the last
 import to Device Security . 

 Create new job . 

 Optional Create more integration instances and jobs to import
 device information from other AssetCentre databases into Device Security . 

 To create more integration instances, repeat the previous
 steps, entering unique names for each one and different settings as
 appropriate for your AssetCentre databases. 

 For each additional integration instance, create a job for
 Cortex XSOAR to run, with a similar configuration as the one you
 initially created. However, as you add more jobs, consider staggering
 their run times so that the data retrievals are spread out. 

 Return to Device Security and check the status of the
 AssetCentre integration.

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

 Set up AssetCentre for Integration 

 Next 

 Learn Device Attributes by Polling 

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

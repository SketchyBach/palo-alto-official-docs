---
url: https://docs.paloaltonetworks.com/panorama/administration/transition-to-a-different-panorama-model/migrate-from-an-m-500-appliance-to-an-m-700-appliance
fetched_at: 2026-08-13T17:18:08Z
source: palo-alto-main
---

# Migrate from an M-100 or M-500 Appliance to an M-300 or M-700 Appliance Clear

Migrate from an M-100 or M-500 Appliance to an M-300 or M-700 Appliance 

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

 Migrate from an M-100 or M-500 Appliance to an M-300 or M-700 Appliance 

 Updated on 

 Thu Jul 30 16:22:01 PDT 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Panorama Docs 

 Getting Started 

 Administration 

 New Features 

 Updated on 

 Thu Jul 30 16:22:01 PDT 2026 

 Focus 

 Home 

 Panorama 

 Transition to a Different Panorama Model 

 Migrate from an M-100 or M-500 Appliance to an M-300 or M-700 Appliance 

 Download PDF 

 Panorama 

 Migrate from an M-100 or M-500 Appliance to an M-300 or M-700 Appliance 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Panorama Docs 

 Getting Started 

 Administration 

 New Features 

 Previous 

 Migrate from an M-Series Appliance to a Panorama Virtual Appliance 

 Next 

 Migrate from an M-200 or M-600 Appliance to an M-300 or M-700 Appliance 

 Migrate from an M-100 or M-500 Appliance to an M-300 or M-700 Appliance 

 Migrate the Panorama™ management server configuration from an M-500 appliance to an M-600
 appliance. 

 You can migrate the Panorama configurations, managed firewalls, and log collectors from an M-500
 appliance to an M-700 appliance. You can migrate Panorama configurations between the
 appliances when both the appliances are running the same PAN-OS version. However,
 the M-500 appliance supports up to PAN-OS version 10.1, while the M-700 appliance
 requires at least PAN-OS version 10.2. 

 To migrate the Panorama configurations across appliances with different
 PAN-OS versions, you must use an intermediate virtual appliance that supports both
 versions, and perform the migration in the following two phases: 

 First, migrate the configurations from the M-500 appliance to the
 intermediate Panorama virtual appliance. For more information about
 migrating an M-Series appliance to a Panorama virtual appliance see,
 Migrate from an M-Series
 Appliance to a Panorama Virtual Appliance . 

 Next, upgrade the intermediate Panorama virtual appliance to a preferred
 PAN-OS version, and migrate the configurations from the intermediate
 Panorama virtual appliance to the M-700 appliance running the same preferred
 PAN-OS version. For more information about migrating a Panorama virtual
 appliance to an M-Series appliance, see Migrate from a Panorama Virtual
 Appliance to an M-Series Appliance . 

 Ensure that all the Log Collectors in the Collector Group are the same Panorama
 model. For example, if you want to add the local Log Collector on the new M-700
 appliance to a Collector Group, the target Collector Group must contain only M-700
 appliances. The same is true for the local Log Collector for an M-700 appliance. 

 This procedure assumes you are no longer using the M-500 appliance for
 device management or log collection. If you intend to continue using the M-500
 appliance as a log collector, you must get a device management license for the
 M-500 appliance. Without a device management license, you cannot use the M-500
 appliance as a log collector. 

 If you do not plan to use the M-500 appliance as a log collector, but
 the M-500 appliance contains log data that you must access at a later date, use
 the panorama web interface to query and
 generate reports using the existing log data. Palo Alto Networks recommends
 reviewing the log retention policy before decommissioning the M-500
 appliance. 

 Policy rule usage is not preserved when you migrate to
 a different Panorama model. This indicates that all the existing policy rule
 usage data from the old Panorama model is no longer displayed after you migrate
 to a new Panorama model. After a successful migration, Panorama begins tracking
 policy rule usage data based on the date the migration was completed. For
 example, the Created date displays the date the
 migration was completed. 

 Plan the migration. 

 Ensure the new Panorama is ready with a Device management and support
 license. These base licenses enable core functionalities of Panorama to
 operate successfully, such as onboarding firewalls, downloading threat
 and content updates, and generating OTPs for Panorama certificates. 

 Ensure that both the M-500 appliance and the intermediate Panorama
 virtual appliance are running the same PAN-OS version. Upgrade the
 M-700 appliance to a recommended supported PAN-OS version. 

 In the second phase of the migration, before migrating the
 configurations from the Panorama Virtual appliance to the M-700
 appliance, you must upgrade the Panorama virtual appliance to the
 same PAN-OS version that is running on the M-700 appliance. For
 important details about software versions, see Panorama, Log Collector,
 Firewall, and WildFire Version Compatibility . 

 Ensure that the M-500 appliance, the intermediate Panorama virtual
 appliance, and the M-700 appliance are on the same system mode. 

 Schedule a maintenance window for the migration. Firewalls can buffer
 logs after the M-500 appliance goes offline and then forward the
 logs after the M-700 appliance comes online. However, completing the
 migration during a maintenance window ensures that the logs do not
 exceed the buffer capacities and are not lost during the transition
 between the Panorama models. 

 Capture and export a fresh set of running configurations from your
 old Panorama. 

 If the new Panorama keeps the same IP address, you must migrate the
 migrate the SC3 security
 certificates to ensure that the managed firewalls
 onboarded using an auth key automatically reconnect (without
 requiring re-onboarding). 

 Your old
 Panorama must be running PAN-OS 11.1.8 or a later 11.1 release,
 or PAN-OS 11.2.5 or a later release, to use the SC3 certificate
 migration feature. 

 ( Prisma Access ) Plan to transfer your Prisma Access licenses to
 the new target appliance. 

 ( SD-WAN only ) Plan export the MongoDB database, in addition to
 your standard configuration snapshot, to the new Panorama. 

 Contact Palo Alto Networks Customer
 Support for assistance with running database export
 commands. 

 Purchase the new M-700 appliance, and migrate your subscriptions to the new
 appliance. 

 Purchase the new M-700 appliance. 

 Purchase the new support license and migration license. 

 When purchasing the new M-700 appliance, provide your sales
 representative with the serial number and device management auth-code of
 the M-500 appliance that you are phasing out, and the date when you
 expect your migration. After you receive the M-700 appliance, register
 it and activate the device management and support licenses by using the
 migration and support auth-codes from Palo Alto Networks. On the
 migration date, the device management license on the M-500 will be
 decommissioned, preventing you from managing devices or collecting logs
 using the M-500 appliance. However, the support license is preserved and
 the Panorama appliance remains under support. You can complete the
 migration after the effective date, but you will not be able to commit
 any configuration changes on the decommissioned M-500 appliance. Palo
 Alto Networks allows up to a 90 day migration grace period when
 migrating between M-Series appliances. Contact your Palo Alto Networks
 sales representative for more information about your migration. 

 Obtain and apply an evaluation or temporary license on the intermediate
 Panorama virtual appliance. 

 Log in to the Palo Alto Networks Customer Support Portal . 

 Select Assets Devices Register New Device . 

 In the Device Type window, select Register
 device using Serial Number or Authorization Code , and click
 Next . 

 To activate the Panorama software, enter the serial number you received
 in the Request for Software Evaluation Approved 
 email. 

 If you plan to use the Panorama software offline, select
 Device will be used Offline , and enter the
 required information. 

 Review the EULA and Support Agreement. 

 If you agree, click Agree and
 Submit . 

 After successful registration, the Assets screen displays the newly
 registered and activated Eval Panorama. 

 Perform the initial setup of the intermediate Panorama virtual appliance. 

 Set Up the Panorama Virtual
 Appliance . 

 Perform Initial Configuration of the
 Panorama Virtual Appliance to define the network connections
 required to activate licenses and install updates. 

 Register Panorama . 

 Activate a Panorama Support
 License . 

 Activate/Retrieve a Firewall
 Management License when the Panorama Virtual Appliance is
 Internet-connected 

 ( Optional ) For Panorama-managed Prisma Access, ensure that you
 transfer the licenses to the new
 panorama appliance . 

 Install Content and Software Updates
 for Panorama . Install the same versions as those on the
 M-Series appliance. 

 This step is required before loading configuration from the old
 Panorama virtual appliance. Ensure that all required content
 updates are installed to avoid security outages. 

 ( PAN-OS 11.2.x and earlier releases ) Select Panorama Plugins and install all plugins that were installed on the old
 Panorama virtual appliance. 

 Edit the M-500 interface configuration to use only the management
 interface. 

 The Panorama virtual appliance supports only the management
 interface for device management and log collection. 

 Log in to the Panorama web
 interface of the M-Series appliance. 

 Select Panorama Setup Management . 

 Edit the General Settings , modify the
 Hostname , and click
 OK . 

 Select Panorama Setup Interfaces Management interface , and enable the required services. 

 Disable the services for the other interfaces. 

 Select Commit Commit to Panorama . 

 Add the IP address of the new Panorama. 

 On the old M-Series appliance, add the Public IP address of the Panorama
 virtual appliance as the second Panorama Server to manage devices from the
 new Panorama management server. 

 Select Device Setup . 

 In the Template context drop-down, select the template or template
 stack containing the Panorama server configuration. 

 Edit the Panorama Settings. 

 Enter the Panorama virtual appliance public IP address and click
 OK . 

 Select Commit Commit and Push . 

 Export the Panorama configuration from the M-500 appliance. 

 Log in to the Panorama web
 interface . 

 Select Panorama Setup Operations . 

 Click Save named Panorama configuration
 snapshot , enter a Name to identify
 the configuration, and click OK . 

 Click Export named Panorama configuration
 snapshot , select the Name of the
 configuration you just saved, and click OK . 
 Panorama exports the configuration to your client system as an XML
 file. 

 ( SD-WAN Only ) Export the mongodump to your external SCP server
 by entering the following command: mongodump --db
 pl_sd_wan -o /opt/panlogs/ld1/mdbdump 

 Contact Palo Alto Networks Customer
 Support for assistance with running database export
 commands. 

 Load the Panorama configuration snapshot that you exported from the M-500
 appliance into the Panorama virtual appliance. 

 The Panorama Policy rule
 Creation and Modified 
 dates are updated to reflect the date you commit the imported Panorama
 configuration on the new Panorama. The universally unique identifier
 (UUID) for each policy rule persists when you migrate the
 Panorama configuration. 

 The Creation and Modified 
 for managed firewalls are not impacted when you monitor policy rule usage
 for a managed firewall because this data is stored locally on
 the managed firewall and not on Panorama. 

 Log in to the Panorama web
 interface of the Panorama virtual appliance. 

 Select Panorama Setup Operations . 

 Click Import named Panorama configuration
 snapshot . 

 Browse for the configuration file you exported
 from the M-500 appliance, and click OK . 

 Click Load named Panorama configuration
 snapshot , and select the Name of the
 configuration you just imported. 

 ( SD-WAN only ) Import the mongodump, which you previously
 exported, from the SCP server and restore it to the new Panorama by
 using the following command. mongorestore --db pl_sd_wan
 pl_sd_wan 

 Contact Palo Alto Networks Customer
 Support for assistance with running database export
 commands. 

 Select a Decryption Key (the master key for Panorama ) and
 click OK . 

 Panorama overwrites its current candidate configuration with the loaded
 configuration. Panorama displays any errors that occur when loading the
 configuration file. If errors occur, save the errors to a local file.
 Resolve each error to ensure the migrated configuration is valid. 

 Log in to the Panorama web interface 
 of the M-700 appliance, select Panorama Setup Interfaces , and verify that the IP address on the management interface is
 different from the IP address of the M-500 appliance. 
 This is to ensure that the connectivity to the Panorama virtual appliance is
 not disrupted post commit. 

 Select Commit Commit to Panorama Validate Commit to review and resolve any configuration issues. Commit the
 Panorama configuration. 

 Upgrade the intermediate Panorama virtual
 appliance to the same version installed on the M-700 appliance. 

 Perform the initial setup of the new M-700 appliance, 

 Set Up the M-series
 appliance . 

 Perform Initial Configuration of the
 M-series appliance . 

 Register Panorama . 

 Activate a Panorama Support
 License . 

 ( Optional ) For Panorama-managed Prisma Access, ensure that you
 transfer the licenses to the new
 panorama appliance . 

 Install Content and Software Updates
 for Panorama . Install the same versions as those on the
 M-Series appliance. 

 This step is required before loading
 configuration from the old Panorama virtual appliance. Ensure that
 all required content updates are installed to avoid security
 outages. 

 ( PAN-OS 11.2.x and earlier releases ) Select Panorama Plugins and install all plugins that were installed on the old
 Panorama virtual appliance. 

 Export the Panorama configuration from the Panorama virtual appliance. 

 Log in to the Panorama web
 interface of the Panorama virtual appliance. 

 Select Panorama Setup Operations . 

 Click Save named Panorama configuration
 snapshot , enter a Name to identify
 the configuration, and click OK . 

 Click Export named Panorama configuration
 snapshot , select the Name of the
 configuration you just saved, and click OK . 
 Panorama exports the configuration to your client system as an XML
 file. 

 ( SD-WAN Only ) Export the mongodump to your external SCP server
 by entering the following command: mongodump --db
 pl_sd_wan -o /opt/panlogs/ld1/mdbdump 

 Contact Palo Alto Networks Customer
 Support for assistance with running database export
 commands. 

 Load the Panorama configuration snapshot that you exported from the Panorama
 virtual appliance to the M-700 appliance. 

 The Panorama Policy rule
 Creation and Modified 
 dates are updated to reflect the date you commit the imported Panorama
 configuration on the new Panorama. The universally unique identifier
 (UUID) for each policy rule persists when you migrate the
 Panorama configuration. 

 The Creation and Modified 
 for managed firewalls are not impacted when you monitor policy rule usage
 for a managed firewall because this data is stored locally on
 the managed firewall and not on Panorama. 

 Log in to the Panorama web
 interface of the Panorama virtual appliance. 

 Select Panorama Setup Operations . 

 Click Import named Panorama configuration
 snapshot . 

 Browse for the configuration file you exported
 from the Panorama virtual appliance, and click
 OK . 

 Click Load named Panorama configuration
 snapshot , and select the Name of the
 configuration you just imported. 

 Select a Decryption Key (the master key for Panorama ) and
 click OK . 

 ( SD-WAN only ) Import the mongodump, which you previously
 exported, from the SCP server and restore it to the new Panorama by
 using the following command. mongorestore --db pl_sd_wan
 pl_sd_wan 

 Contact Palo Alto Networks Customer
 Support for assistance with running database export
 commands. 

 Panorama overwrites its current candidate configuration with the loaded
 configuration. Panorama displays any errors that occur when loading the
 configuration file. If errors occur, save the errors to a local file.
 Resolve each error to ensure the migrated configuration is valid. 

 Review the network configuration on the M-700 appliance. 

 ( Optional ) Log in to the Panorama web
 interface of the M-500 appliance, select Panorama Setup Operations , and click Shutdown Panorama . 
 Shut down the M-500 appliance if you plan to have the same IP address
 on both the M-500 and M-700 appliances. 

 Log in to the Panorama web
 interface of the M-700 appliance, select Panorama Setup Interfaces , and verify the network configuration on the Management
 interface to ensure that the connectivity to the M-700 appliance is not
 disrupted post commit. 

 Ensure that all the interface configurations are set up based on your
 requirements for the M-700 appliance. 

 Select Commit Commit to Panorama Validate Commit to review and resolve any configuration issues. Commit the
 Panorama configuration. 

 Generate a new device registration authentication key for managed device
 connectivity. 

 In the Panorama web interface of the M-700 appliance, select Panorama Device Registration Auth Key and Add a new authentication
 key. 

 Configure the authentication key. 

 Name —Enter a descriptive name for the
 authentication key. 

 Lifetime —Enter the key lifetime to
 specify the duration of the validity of the authentication
 key. 

 Count —Enter the number of devices that
 will use the authentication key for connecting to
 Panorama. 

 Device Type —Specify whether the
 authentication key may be used for
 Firewalls , Log
 Collectors , or Any 
 device. 

 Click OK . 

 Copy Auth Key and
 Close . 

 Migrate the SC3 certificates 
 to ensure your existing managed firewalls automatically trust and reconnect to
 the new Panorama without manual intervention. 

 This is required when transitioning
 from one Panorama model to another. 

 Select Commit Commit to Panorama Validate Commit . Next, Commit All Changes to the Panorama
 configuration. 

 Synchronize the M-700 appliance with the managed devices. 

 Select Commit Push to Devices and Edit Selections . 

 Select all the devices under Device Groups ,
 Templates , and Collector
 Groups , and click OK . 

 Push All Changes. 

 Select Panorama Managed Devices Summary , and verify that all the firewalls are connected. Also,
 verify that the shared policy and template configurations of the
 firewalls are In sync with Panorama. 

 Select Panorama Managed Collectors , and verify that the configuration status is
 In Sync with Panorama, and the health status
 is Green for all the log collectors. 

 ( HA only) Set up the Panorama HA peer. 

 If the Panorama management servers are in a high availability configuration,
 perform the steps below on the HA peer. 

 Perform the initial setup of
 the M-Series appliance . 

 Add the IP address of the
 new Panorama . 

 ( HA only ) Modify the M-series appliance HA peer configuration. 

 On an HA peer, log in to the Panorama web
 interface , select Panorama High Availability and edit the Setup . 

 In the Peer HA IP Address field, enter the new
 IP address of the HA peer and click OK . 

 Select Commit Commit to Panorama and Commit your change 

 Repeat these steps on the other peer in the HA peer. 

 ( HA only ) Synchronize the Panorama peers. 

 Access the Dashboard on one of the HA peers and
 select Widgets System High Availability to display the HA widget. 

 Sync to peer , click Yes ,
 and wait for the Running Config to display
 Synchronized . 

 Access the Dashboard on the remaining HA peer
 and select Widgets System High Availability to display the HA widget. 

 Verify that the Running Config displays
 Synchronized . 

 After you migrate, if there are connectivity issues between Panorama and
 the managed firewalls, recover the connectivity of
 the managed devices to Panorama to resolve the issues. 

 Previous 

 Migrate from an M-Series Appliance to a Panorama Virtual Appliance 

 Next 

 Migrate from an M-200 or M-600 Appliance to an M-300 or M-700 Appliance 

 On This Page 

 Activation and Onboarding 

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

 Panorama 

 Service Provider 

 VM-Series 

 Plugins 

 SASE 

 Prisma Access 

 Prisma SASE Multitenant Platform 

 AI-Powered ADEM 

 Prisma Access Monitoring & Visibility 

 Prisma SD-WAN 

 ION Devices 

 Next-Generation CASB 

 Cloud-Delivered Security Services 

 Advanced WildFire 

 Advanced URL Filtering 

 Advanced Threat Prevention 

 Advanced DNS Security 

 AI Access Security 

 Device Security 

 Enterprise DLP 

 SaaS Security 

 Network Security 

 Shared Policy for NGFWs and Prisma Access 

 IPSec VPN 

 Security Policy 

 Quantum Security 

 Endpoints 

 GlobalProtect 

 Remote Browser Isolation 

 Prisma Access Agent 

 Visibility & Monitoring 

 Dashboards 

 Incidents and Alerts 

 Reports 

 Autonomous DEM 

 FedRAMP 

 Prisma SASE for FedRAMP 

 Autonomous DEM for FedRAMP 

 Prisma SD-WAN Experts Corner 

 Network Policy 

 QoS Whitepaper 

 Security Architecture Whitepaper 

 External Antennas for ION-C Series 

 Dynamic Path Selection 

 Best Practices 

 Best Practices Library 

 Experts Corner 

 Solutions Docs from Product Experts 

 Resources 

 All Products A - Z 

 All Release Notes 

 Compatibility Matrix 

 Experts Corner 

 Network Security Platform 

 Security Policy 

 Decryption 

 Device-ID 

 IPSec VPN 

 Quality of Service 

 Quantum Security 

 11.1 & Later 

 Next-Generation Firewall 

 Administration 

 Panorama 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

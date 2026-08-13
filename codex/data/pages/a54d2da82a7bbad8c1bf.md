---
url: https://docs.paloaltonetworks.com/panorama/administration/manage-wildfire-appliances/add-standalone-wildfire-appliances-to-manage-with-panorama
fetched_at: 2026-08-13T17:17:56Z
source: palo-alto-main
---

# Add Standalone WildFire Appliances to Manage with Panorama Clear

Add Standalone WildFire Appliances to Manage with Panorama 

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

 Add Standalone WildFire Appliances to Manage with Panorama 

 Updated on 

 Jul 30, 2026 

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

 Jul 30, 2026 

 Focus 

 Home 

 Panorama 

 Manage WildFire Appliances 

 Add Standalone WildFire Appliances to Manage with Panorama 

 Download PDF 

 Panorama 

 Add Standalone WildFire Appliances to Manage with Panorama 

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

 Manage WildFire Appliances 

 Next 

 Configure Basic WildFire Appliance Settings on Panorama 

 Add Standalone WildFire Appliances to Manage with Panorama 

 You can manage up to 200 WildFire® appliances
with a Panorama® M-Series or virtual appliance. The WildFire 200-appliance
limit is a combined total of standalone appliances and WildFire
appliance cluster nodes (if you also Configure
a Cluster and Add Nodes on Panorama ). 

 Ensure that your
Panorama server is running PAN-OS® 8.1.0 or a later PAN-OS version,
and that any WildFire appliance you add to your Panorama management server
is also running PAN-OS 8.1.0 or a later release. 

 A device
registration authentication key is used to securely authenticate
and connect the Panorama management server and the WildFire appliance
on first connect. To configure the device registration authentication
key, specify the key lifetime and the number of times you can use
the authentication key to onboard new WildFire appliances. Additionally,
you can specify one or more WildFire appliance serial numbers for
which the authentication key is valid. 

 The authentication
key expires 90 days after the key lifetime expires. After 90 days, you
are prompted to re-certify the authentication key to maintain its
validity. If you do not re-certify, then the authentication key
becomes invalid. A system log is generated each time a WildFire
appliance uses the Panorama-generated authentication key. The WildFire
appliance uses the authentication key to authenticate Panorama when
it delivers the device certificate that is used for all subsequent communications. 

 For WildFire appliances running a PAN-OS 10.1 release, Panorama running PAN-OS
 11.1 supports onboarding WildFire appliances running PAN-OS 10.1.3 or later
 release only. You cannot add a WildFire appliance running PAN-OS 10.1.2 or
 earlier PAN-OS 11.1 release to Panorama management if Panorama is running PAN-OS
 11.1 or later release. 

 Panorama supports onboarding WildFire appliances running the following
 releases: 

 Panorama running PAN-OS 10.2 or later release— WildFire appliances
 running PAN-OS 10.1.3 or later release, and WildFire appliances running
 PAN-OS 10.0 or earlier PAN-OS release. 

 There is no impact to WildFire appliances already managed by Panorama on upgrade
 to PAN-OS 10.2 or later release. 

 Using the local CLI, verify that each WildFire
appliance that you want to manage on a Panorama management server
is running PAN-OS 8.1.0 or a later release. 

 admin@qa16> show system info | match version 
sw-version: 11.0.0 
wf-content-version: 702-283 
logdb-version: 8.0.15 

 On each Panorama appliance you want to use to manage
WildFire appliances, verify that the Panorama management server
is running PAN-OS 8.1.0 or a later release. 

 Dashboard General
Information Software Version displays
the running software version. 

 If you aren’t sure whether a WildFire appliance belongs
to a WildFire appliance cluster or
is a standalone appliance on the local WildFire appliance CLI, check the Node mode to
ensure that the status is stand_alone and
check the Applicationstatus to ensure
that the global-db-service and global-queue-service indicate ReadyStandalone . 

 admin@WF-500> show cluster membership 
Service Summary: wfpc signature 
Cluster name: 
Address: 10.10.10.100 
Host name: WF-500 
Node name: wfpc-012345678901-internal 
Serial number: 012345678901 
 Node mode: stand_alone 
Server role: True 
HA priority: 
Last changed: Mon, 06 Mar 2017 16:34:25 -0800 
Services: wfcore signature wfpc infra 
Monitor status: 
 Serf Health Status: passing 
 Agent alive and reachable 
Application status: 
 global-db-service: ReadyStandalone 
 wildfire-apps-service: Ready 
 global-queue-service: ReadyStandalone 
 wildfire-management-service: Done 
 siggen-db: ReadyMaster 
Diag report: 
 10.10.10.100: reported leader '10.10.10.100', age 0. 
 10.10.10.100: local node passed sanity check. 

 If the WildFire appliances you want to manage with Panorama
are new, check Get Started with WildFire to ensure that
you complete basic steps such as confirming your WildFire license
is active, enabling logging, connecting firewalls to WildFire appliances,
and configuring basic WildFire features. 

 Create a device registration authentication key. 

 Select Panorama Device Registration Auth Key and Add a
new authentication key. 

 Configure the authentication key. 

 Name —Add a descriptive name
for the authentication key. 

 Lifetime —Specify the key lifetime
for how long you can use the authentication key used to onboard
new WildFire appliances. 

 Count —Specify how many times you can
use the authentication key to onboard new WildFire appliances. 

 Device Type —Specify that the authentication
key is used to authenticate Any device. 

 ( Optional ) Devices —Enter
one or more device serial numbers to specify for which WildFire
appliances the authentication key is valid. 

 Click OK . 

 Copy Auth Key and Close . 

 On the local CLI of each WildFire appliance the Panorama
server will manage, configure the IP address of the Panorama server
and add the device registration authentication key. 

 Before you register standalone WildFire appliances to a
Panorama appliance, you must first configure the Panorama IP address
or FQDN and add the device registration authentication key on each
WildFire appliance. This enables each WildFire appliance to securely
connect to the Panorama appliance that manages the WildFire appliance.
The device registration authentication key is used only for the
initial connection to the Panorama server. 

 Configure the IP address or FQDN of the
management interface for the primary Panorama server. 

 admin@WF-500# set deviceconfig system panorama-server <ip-address | FQDN> 

 If you use a backup Panorama appliance for high availability
( recommended ), configure the IP address or FQDN of the
management interface for the backup Panorama server: 

 admin@WF-500# set deviceconfig system panorama-server-2 <ip-address | FQDN> 

 Add the device registration authentication key. 

 admin> request authkey set <auth-key> 

 Register WildFire appliances on the primary Panorama
appliance. 

 From the Panorama web interface, Panorama Managed WildFire Appliances and Add
Appliance . 

 Enter the serial number of each WildFire appliance
on a separate line. If you do not have a list of serial numbers,
on each WildFire appliance, run: 

 admin@WF-500> show system info | match serial 
serial: 012345678901 

 Several local CLI commands display
the WildFire appliance serial number, including show cluster membership . 

 Click OK . 

 If it is available, information about configuration that
is already committed on the WildFire appliances displays, such as
IP address and software version. 

 ( Optional ) Import WildFire appliance configurations
into the Panorama appliance. 

 Select the appliances that have configurations
you want to import from the list of managed WildFire appliances. 

 Import Config . 

 Select Yes . 

 Importing configurations updates the displayed information
and makes the imported configurations part of the Panorama appliance
candidate configuration. 

 Commit to Panorama to make
the imported WildFire appliance configurations part of the Panorama
running configuration. 

 Configure or confirm the configuration of the WildFire
appliance interfaces. 

 Each WildFire appliance has four interfaces: Management (Ethernet0), Analysis Network
Environment (Ethernet1), Ethernet2 ,
and Ethernet3 . 

 Select Panorama Managed WildFire Appliances and
select a WildFire appliance. 

 Select Interfaces . 

 Select an interface to configure or edit it. You can
enable the interface, set the speed and duplex, and configure the
IP address and netmask, the default gateway, the MTU, the DNS server,
the link state, and the Management Services for
each interface. You can also Add permitted
IP addresses so that an interface accepts traffic only from specified
addresses. 

 The Analysis Network Environment , Ethernet2 ,
and Ethernet3 interfaces support only Ping as
a Management Services option. 

 The Management interface
supports Ping , SSH ,
and SNMP as Management Services options.
In addition, the Management interface supports
proxy server configuration in case a direct connection to the internet
is not possible. 

 Click OK save your changes. 

 Commit the configuration on the Panorama appliance and
push it to the appliance or to multiple appliances. 

 Commit and Push . 

 If there are configurations on the Panorama appliance
that you do not want to push, Edit Selections to
choose the appliances to which you want to push configurations.
The pushed configuration overwrites the running configuration on
a WildFire appliance. 

 Verify the configuration. 

 Select Panorama Managed WildFire Appliances . 

 Check the following fields: 

 Connected —The state is Connected . 

 Role —The role of each WildFire appliance
is Standalone . 

 Config Status —The status is InSync . 

 Last Commit State — Commitsucceeded . 

 Previous 

 Manage WildFire Appliances 

 Next 

 Configure Basic WildFire Appliance Settings on Panorama 

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

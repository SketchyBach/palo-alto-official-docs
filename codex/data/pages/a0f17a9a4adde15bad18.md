---
url: https://docs.paloaltonetworks.com/panorama/getting-started/set-up-panorama/set-up-the-panorama-virtual-appliance/set-up-the-panorama-virtual-appliance-with-local-log-collector
fetched_at: 2026-08-13T17:18:41Z
source: palo-alto-main
---

# Set Up the Panorama Virtual Appliance with Local Log Collector Clear

Set Up the Panorama Virtual Appliance with Local Log Collector 

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

 Set Up the Panorama Virtual Appliance with Local Log Collector 

 Updated on 

 Jul 14, 2026 

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

 Jul 14, 2026 

 Focus 

 Home 

 Panorama 

 Set Up Panorama 

 Set Up the Panorama Virtual Appliance 

 Set Up the Panorama Virtual Appliance with Local Log Collector 

 Download PDF 

 Panorama 

 Set Up the Panorama Virtual Appliance with Local Log Collector 

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

 Set Up The Panorama Virtual Appliance as a Log Collector 

 Next 

 Set up a Panorama Virtual Appliance in Panorama Mode 

 Set Up the Panorama Virtual Appliance with Local Log Collector 

 Where Can I Use This? What Do I Need? 

 NGFW (Managed by Panorama) 

 Device management licence 

 Support license 

 Outbound Internet Access 

 Customer Support Portal (CSP) Account 

 If the Panorama virtual appliance is in Legacy
mode after you upgrade from a Panorama 8.0 or earlier release to
a Panorama 8.1 (or later) release, switch to Panorama mode in order
to create a local Log Collector, add multiple logging disks without
losing existing logs. increase log storage up to 24TB, and enable
faster report generation. 

 Once you
change from Legacy mode to Panorama mode, Legacy mode will no longer
be available. 

 After upgrading to Panorama 8.1, the
first step is to increase the system resources on the virtual appliance
to the minimum required for Panorama mode. Panorama reboots when
you increase resources, so perform this procedure during a maintenance
window. You must install a larger system disk (81GB), increase CPUs and memory based
on the log storage capacity, and add a virtual logging disk. The
new logging disk must have at least as much capacity as the appliance
currently uses in Legacy mode and cannot be less than 2TB. Adding
a virtual disk enables you to migrate existing logs to the Log Collector
and enables the Log Collector to store new logs. 

 If Panorama
is deployed in an HA configuration, perform the following steps
on the secondary peer first and then on the primary peer. 

 Determine
which system resources you need to increase before the virtual appliance
can operate in Panorama mode. 

 You must run the command specified
in this step even if you have determined that Panorama already has
adequate resources. 

 Access the Panorama CLI: 

 Use terminal emulation software
such as PuTTY to open an SSH session to the IP address that you
specified for the Panorama MGT interface. 

 Log in to the CLI when prompted. 

 Check the resources you must increase by running the
following command: 

 > request system system-mode panorama 

 Enter y when
prompted to continue. The output specifies the resources you must increase.
For example: 

 Panorama mode not supported on current system disk of size 52.0 GB. 
Please attach a disk of size 81.0 GB, then use 'request system clone-system-disk' to migrate the current system disk 
Please add a new virtual logging disk with more than 50.00 GB of storage capacity. 
Not enough CPU cores: Found 4 cores, need 8 cores 

 Increase the CPUs and memory, and replace the system
disk with a larger disk. 

 Access the VMware ESXi vSphere Client, select Virtual
Machines , right-click the Panorama virtual appliance,
and select Power Power
Off . 

 Right-click the Panorama virtual appliance and Edit
Settings . 

 Select Memory and enter the
new Memory Size . 

 Select CPUs and specify the
number of CPUs (the Number of virtual sockets multiplied
by the Number of cores per socket ). 

 Add
a virtual disk. 

 You will use this disk to replace the existing system disk. 

 In the Hardware settings, Add a
disk, select Hard Disk as the hardware type,
and click Next . 

 Create a new virtual disk and click Next . 

 Set the Disk Size to exactly 81GB
and select the Thick Provision Lazy Zeroed disk
format. 

 Select Specify a datastore or datastore structure as
the location, Browse to a datastore of at
least 81GB, click OK , and click Next . 

 Select a SCSI Virtual Device Node (you
can use the default selection) and click Next . 

 Panorama will fail to boot if you select
a format other than SCSI. 

 Verify that the settings are correct and then click Finish and OK . 

 Right-click the Panorama virtual appliance and select Power Power On .
Wait for Panorama to reboot before continuing. 

 Return to the Panorama CLI and copy the data from
the original system disk to the new system disk: 

 > request system clone-system-disk target sdb 

 Enter y when
prompted to continue. 

 The copying process takes around 20
to 25 minutes, during which Panorama reboots. When the process finishes,
the output tells you to shut down Panorama. 

 Return to the vSphere Client console, right-click
the Panorama virtual appliance, and select Power Power Off . 

 Right-click the Panorama virtual appliance and Edit
Settings . 

 Select the original system disk, click Remove ,
select Remove from virtual machine , and click OK . 

 Right-click the Panorama virtual appliance and Edit
Settings . 

 Select the new system disk, set the Virtual
Device Node to SCSI (0:0) , and
click OK . 

 Right-click the Panorama virtual appliance and select Power Power On .
Before proceeding, wait for Panorama to reboot on the new system
disk (around 15 minutes). 

 Add a virtual logging disk. 

 This is the disk to which you will migrate existing logs. 

 In the VMware ESXi vSphere Client, right-click
the Panorama virtual appliance and select Power Power Off . 

 Right-click the Panorama virtual appliance and Edit
Settings . 

 Repeat the steps to Add
a virtual disk. Set the Disk Size to
a multiple of 2TB based on the amount of log storage you need. The
capacity must be at least as large as the existing virtual disk
or NFS storage that Panorama currently uses for logs. The disk capacity
must be a multiple of 2TB and can be up to 24TB. For example, if
the existing disk has 5TB of log storage, you must add a new disk
of at least 6TB. 

 After you switch to Panorama mode, Panorama will automatically
divide the new disk into 2TB partitions, each of which will function
as a separate virtual disk. 

 Right-click the Panorama virtual appliance and select Power Power On .
Wait for Panorama to reboot before continuing. 

 Switch
from Legacy mode to Panorama mode. 

 After switching the mode, the appliance reboots again and
then automatically creates a local Log Collector and Collector Group.
The existing logs won’t be available for querying or reporting until
you migrate them later in this procedure. 

 Return to the Panorama CLI and run the following
command. 

 > request system system-mode panorama 

 Enter y when
prompted to continue. After rebooting, Panorama automatically creates
a local Log Collector (named Panorama) and creates a Collector Group (named
default) to contain it. Panorama also configures the virtual logging
disk you added and divides it into separate 2TB disks. Wait for
the process to finish and for Panorama to reboot (around five minutes)
before continuing. 

 Log in to the Panorama web interface. 

 In the Dashboard , General
Information settings, verify that the Mode is
now panorama . 

 In an HA deployment, the secondary peer is in a suspended
state at this point because its mode (Panorama) does not match the
mode on the primary peer (Legacy). You will un-suspend the secondary
peer after switching the primary peer to Panorama mode later in
this procedure. 

 Select Panorama Collector Groups to verify that
the default collector group has been created,
and that the local Log Collector is part of the default collector group. 

 Push the configuration to the managed devices. 

 If there are no pending changes: 

 Select Commit Push to Devices and Edit
Selections . 

 Select Collector Group and make sure
the default collector group is selected. 

 Click OK and Push . 

 If you have pending changes: 

 Select Commit Commit and Push and Edit
Selections . 

 Verify that your Device Group devices
and Templates are included. 

 Select Collector Group and make sure
the default collector group is selected. 

 Click OK and Commit and
Push . 

 Select Panorama Managed Collectors and verify
that the columns display the following information for the local
Log Collector: 

 Collector Name—This defaults to the Panorama hostname.
It should be listed under the default Collector
Group. 

 Connected—Check mark 

 Configuration Status—In sync 

 Run Time Status—connected 

 ( HA only ) Switch the primary Panorama from Legacy
mode to Panorama mode. 

 This step triggers failover. 

 Repeat Step
1 through Step
4 on the primary Panorama. 

 Wait for the primary Panorama to reboot and return to an
active HA state. If preemption is not enabled, you must manually
fail back: select Panorama High Availability and, in the
Operational Commands section, Make local Panorama functional . 

 On the primary Panorama, select Dashboard and,
in the High Availability section, Sync to peer ,
click Yes , and wait for the Running
Config to display Synchronized status. 

 On the secondary Panorama, select Panorama High Availability and,
in the Operational Commands section, Make local Panorama
functional . 

 This step is necessary to bring the secondary Panorama
out of its suspended HA state. 

 Migrate existing logs to the new virtual logging disks. 

 If you deployed Panorama in an HA configuration, perform
this only on the primary peer. 

 Palo Alto Networks recommends
migrating existing logs to the new virtual logging disks during
your maintenance window. The log migration requires a large number
of the Panorama virtual appliance CPU cores to execute and impacts
Panorama operational performance. 

 Return to the Panorama CLI. 

 Start the log migration: 

 > request logdb migrate vm start 

 The
process duration varies by the volume of log data you are migrating.
To check the status of the migration, run the following command: 

 > request logdb migrate vm status 

 When
the migration finishes, the output displays: migrationhas been done . 

 Verify that the existing logs are available. 

 Log in to the Panorama web
interface. 

 Select Panorama Monitor ,
select a log type that you know matches some existing logs (for
example, Panorama Monitor System ), and verify that the
logs display. 

 Next steps... 

 Configure log forwarding to Panorama so
that the Log Collector receives new logs from firewalls. 

 Previous 

 Set Up The Panorama Virtual Appliance as a Log Collector 

 Next 

 Set up a Panorama Virtual Appliance in Panorama Mode 

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

 Getting Started 

 Panorama 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

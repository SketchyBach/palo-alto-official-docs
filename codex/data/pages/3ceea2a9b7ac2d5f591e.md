---
url: https://docs.paloaltonetworks.com/iot/administration/discover-iot-devices-and-take-inventory/parse-industrial-ot-device-files
fetched_at: 2026-08-13T16:36:24Z
source: palo-alto-main
---

# Parse Industrial OT Device Files Clear

Parse Industrial OT Device Files 

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

 Parse Industrial OT Device Files 

 Updated on 

 Thu Jul 30 16:42:12 PDT 2026 

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

 Thu Jul 30 16:42:12 PDT 2026 

 Focus 

 Home 

 Device Security 

 Device Security Administration Guide 

 Discover IoT Devices and Take Inventory 

 Parse Industrial OT Device Files 

 Download PDF 

 Device Security 

 Parse Industrial OT Device Files 

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

 IP Endpoints 

 Next 

 Discover Mobile Device Attributes 

 Parse Industrial OT Device Files 

 Add industrial operational technology (OT) device files, such as PLC configuration,
 program, and inventory files, to Device Security to enrich your asset
 inventory.

 Where Can I Use This? What Do I Need? 

 Device Security (Managed by Strata Cloud Manager) 

 (Legacy) IoT Security (Standalone portal) 

 One of the following subscriptions, with the
 Industrial OT vertical enabled:

 Device Security subscription

 Precision AI bundle subscription

 Device Security X subscription

 Programmable Logic Controller (PLC) configuration, program, and inventory files,
 referred to as device files, control and manage machinery and processes for
 industrial operational technology (OT) devices. Because device files define
 parameters and customize industrial devices to suit operational requirements, they
 contain detailed asset information. This can include information such as the name,
 model, vendor, and firmware of devices, as well as information about hardware
 components and downstream devices. In particular, device files can contain
 information for industrial OT equipment that operate in isolated network segments.
 If firewalls don't see traffic from those industrial OT devices,
 Device Security can't learn about those assets from passive traffic monitoring.

 Use device files along with Device Security features, such as
 Network Discovery Polling 
 and third-party integrations ,
 to enrich your asset inventory. To use device files to augment
 your Device Security asset inventory, you need to have an
 OT Device Security subscription. On an OT Device Security 
 tenant, view and add devices files at
 Assets Device Files .

 On the Device Files page, the Overview section shows a summary
 of files added, devices learned, and devices enriched from
 device files in the past 30 days. Below the Overview section,
 the Parsing History table displays all device files uploaded to
 your Device Security tenant. This table includes information
 such as the parsing history of each file, and how many devices
 were updated or how many devices were missing critical
 information, such as MAC and IP address, in each file. You can
 also download previously uploaded device files from the table.

 When adding a device file, you need to choose a site association
 before uploading a file. The site association helps avoid
 potential conflicts with overlapping IP addresses, and it serves
 as the site assignment for any new devices learned. You can
 upload only one file at a time. Device Security supports the following device
 file types for parsing:

 Beckhoff TwinCAT (.tnzip file containing a Project Solution File (.sln) and
 a project file (.tsproj))

 Emerson DeltaV Explorer (.fhx) 

 Mitsubishi MELSOFT Series GX Works2 (.gxw) 

 Rockwell AssetCentre (.raai) 

 Siemens PRONETA (.xml)

 Siemens TIA Portal (.zip file containing a Project
 Library File (.plf) and an Index File (.idx))

 Device files parsing only supports Siemens TIA Portal version 17 files.

 Studio 5000 Logix Designer (.l5x) 

 Unity Application Exchange File (.xef) 

 Upload Device Files 

 You can only upload one device file at a time. Verify the
 parsed content and submit a device file before adding
 another device file.

 Log into your OT Device Security and
 navigate to Assets Device Files .

 In the Parsing History table, click on the Upload icon
 to open the File Parsing side panel.

 Select the site to associate your device file with.

 Drag and drop your device file into the Select Files
 box, or Browse your folders and
 select the device file to upload.

 Review the result of the parsed device file.

 After Device Security parses a file, it displays
 a table with the parsed output. The table lists the
 names of all devices discovered from the device
 file, as well as whether those devices are new or if
 they match to an existing device in the
 Device Security assets inventory.

 When a device matches an existing device in
 Device Security , you can click on the Device Name
 field to open up the corresponding Device Details
 page in a new tab or window. After you submit the
 device file, the data from the device file will
 supplement the information on that existing device
 identity.

 If the Parsing Output field says
 Additional Info Required ,
 then Device Security can't determine if the
 device is new or if it matches an existing device.
 Click on Additional Info
 Required to add an IP address and a MAC
 address. A device that has an IP address but no MAC
 address will be created as a static IP address. If
 you don't want to add the information right away,
 you can submit the device file first and update the
 information from the Parsing History table later.

 After verifying the results of the parsed device file,
 Submit the file to add the
 devices and device information to Device Security .

 After submitting the device file, you can view the
 submitted device file in the Parsing History table.

 Update Devices Missing Critical Information 

 When viewing the Parsing History table, some rows might have a
 value under the field Devices Missing Critical Information.
 This field indicates the number of devices in that file that
 are missing an IP address and maybe a MAC address. Update the
 devices with this information to help Device Security 
 determine if those devices are new or if they match existing
 devices in the asset inventory.

 Click on the number in the Devices Missing Critical
 Information field for a device file.

 This brings up the File Parsing Side panel, where
 you can review the list of devices that are missing
 an IP address and maybe a MAC address.

 For each device, click Additional Info
 Required in the Parsing Output field to
 bring up the Device Attributes pop-up.

 Enter the IP Address for the
 device.

 Optional Enter the
 MAC Address for the device.

 Providing a MAC address in addition to the IP address helps
 Device Security determine if a device already exists in the
 asset inventory, and enrich the device data accordingly.

 If you don't provide a MAC address, Device Security adds the
 device as an IP endpoint rather than as an asset.

 Apply the updates.

 Continue updating all devices that are missing critical
 information, and then Submit the
 changes after you're done.

 Download Past Device Files 

 Navigate to Assets Device Files and view the Parsing History table.

 Select the check box next to the device files that you
 want to download.

 Download the device files.

 Previous 

 IP Endpoints 

 Next 

 Discover Mobile Device Attributes 

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

 Administration 

 Cloud-Delivered Security Services 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

---
url: https://docs.paloaltonetworks.com/prisma-access-browser/administration/manage-prisma-access-browser-devices
fetched_at: 2026-08-13T17:23:13Z
source: palo-alto-main
---

# Manage Prisma Browser Devices Clear

Manage Prisma Browser Devices 

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

 Manage Prisma Browser Devices 

 Updated on 

 Jul 28, 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma Browser Docs 

 Activation & Onboarding 

 Getting Started 

 Deployment 

 Administration 

 Integrations 

 User Guide 

 Updated on 

 Jul 28, 2026 

 Focus 

 Home 

 Prisma Browser 

 Prisma Access Browser Administration 

 Manage Prisma Browser Devices 

 Download PDF 

 Prisma Browser 

 Manage Prisma Browser Devices 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma Browser Docs 

 Activation & Onboarding 

 Getting Started 

 Deployment 

 Administration 

 Integrations 

 User Guide 

 Previous 

 Manage Configuration Versions (Draft Mode) 

 Next 

 Manage Prisma Browser Device Groups 

 Manage Prisma Browser Devices 

 Learn how to monitor devices running Prisma Browser , and create device
 groups. 

 Where Can I Use This? What Do I Need? 

 Strata Cloud Manager 

 Prisma Browser standalone 

 Prisma Access with Prisma Browser bundle license or
 Prisma Browser standalone license 

 Superuser or Prisma Browser 
 role 

 The device directory provides a roster of your Prisma Browser devices and device
 groups. 

 The page is tabbed so that you can choose which view you want to see:
 Devices or Device Groups . The
 Device Groups tab allows you to create and examine groups
 of devices. This becomes important when defining rules and policies. 

 Manage Devices 

 From Strata Cloud Manager , select Configuration Prisma Browser Directory Devices . 

 You can see the total number of Prisma Browser devices displayed at
 the top of the page. By default, the Devices screen displays the first
 50 devices based on your sort order. Click Load 50
 More to move to the next page of devices. 

 Review the device data. 
 The Device Directory allows you to see the details of each device, and
 includes the following information: 
 Name —The device's host name. 

 User —The Prisma Browser user's browser login name. Click
 the name to see user details, such as the devices and device groups
 associated with the user. 

 IP address —The device's external IP address. 

 Device groups —The number of device groups to which the device
 belongs. 

 Browser version —The browser version that's running on the
 device. 

 Device type —The type of device. The options are: 
 Desktop 

 Laptop 

 VM 

 Mobile 

 Unknown 

 OS platform —The operating system installed on the device
 (Windows, macOS, iOS, Android, Linux, Unknown). 

 OS version —The version of OS running on the device. 

 Last seen —The time the device last recorded an event to Prisma Browser . Hover over the field to see the full
 timestamp. 

 Investigate devices using search and filters. 

 Search by device name or user name . 

 Filter the devices based on Device Groups ,
 OS platform , EPP
 status , Last seen date ,
 Screen lock status , Disk
 encryption status , and Firewall
 status . 

 View details about a specific device. 

 Click on a specific device on the list to see the device
 details. 

 Review the device-specific details, including: 

 User —The device user's name. 

 Device type —The device type (desktop, laptop, VM,
 mobile, or unknown). 

 OS platform —The operating system installed on the
 device (Windows, macOS, iOS, Android, Linux, or
 Unknown). 

 OS version —The OS version installed on the
 device. 

 Browser brand —The name of the selected browser. 

 Browser version —The browser version running on the
 device. 

 First Seen —The elapsed time since the device first
 connected to the network. Hover over the field to see the
 full timestamp. 

 Last Seen —The time the device last recorded an event
 to Prisma Browser . Hover over the field to see the full
 timestamp. 

 Model —The device model. 

 Device management —The device management system that's
 managing the device. 

 Serial number —The device serial number. 

 IP address —The device's external IP address. 

 User-Agent —The request string that identifies the
 browser, device, and OS to network peers. 

 MAC addresses —The MAC addresses of the network cards
 installed on the device. 

 Posture —The status of the different posture
 requirements. Specific postures have a link to the details,
 and others have some additional information. 

 Extensions —The Extensions (if any) installed with the
 browser. 

 Device Groups —A list of the device groups to which
 the device belongs. Each group displays the relevant posture
 information, and a link to the device group. 

 User Groups —A list of the user groups to which the
 device user belongs. 

 Export device details for offline investigation. 

 Click the Export icon. 

 In the Export window, select one of the following options: 

 Export all —Export all device data. 

 Export filtered data —Export device details based on
 the current filters. 

 Manage Device Groups 

 The Prisma Browser has a device group function that allows you to create
 different groups for different devices. Groups are dynamic. For example, you can
 set up groups for specific managed devices, different subsidiary devices, or
 contractors. As an administrator, you can exercise a considerable amount of
 flexibility in configuring the device groups you need within your organization.
 For example, groups meet changing business, operational, and organizational
 circumstances. You can use device groups either with sign-in rules to set the
 security bar for accessing Prisma Browser , or with posture-focused scoping
 for policy rules. For managing mobile device groups, see Create, Edit, and
 Delete Prisma Browser for Mobile Device Groups. 

 From Strata Cloud Manager , select Configuration Prisma Browser Directory Devices and then select the Device Groups 
 tab. 

 You can see the total number of Prisma Browser device groups
 displayed at the top of the page. By default, the Device Groups screen
 displays the first 50 device groups based on your sort order. Click
 Load 50 More to move to the next page of
 devices. 

 Review the device group data. 
 The Device Group Directory allows you to see the details of each device
 group, and includes the following information: 
 Name —The device group name. 

 Type — Prisma Browser , Mobile, Prisma Browser 
 Extension, or Chromebook. 

 Attributes —Matching criteria for identifying which devices
 belong to the device group. 

 Created at —The device group creation date. Hover over the
 field to see the full timestamp. 

 Updated at —The device group last update date. Hover over the
 field to see the full timestamp. 

 Add a device group. 

 From the Device groups tab, click
 Add device group . 

 Name the device group. 

 Select whether you want to create a device group for
 Prisma Browser endpoints or
 for Mobile devices. 

 Select and configure the attributes that devices must match in
 order to be part of the device group. 
 Attributes match against device criteria, such as whether the
 device has disk encryption enabled, active endpoint protection, or
 complex password policy requirements. Enforcing device group
 membership based on attributes provides a granular way for you to
 ensure that the devices Prisma Browser allows have good security
 posture. There are different attributes depending on whether you are
 creating a device group for Windows and macOS
 devices or for mobile devices. 

 Click Create . 

 To edit or delete a device group, hover over the
 device group name in the director and click the pencil icon (to edit) or
 the trash icon (to delete). 

 Investigate devices using search and filters. 

 Search by name or id . 

 Filter the device groups based on Type ,
 Attributes , Created
 at , and Updated at . 

 Export device details for offline investigation. 

 Click the Export icon. 

 In the Export window, select one of the following options: 

 Export all —Export all device group data. 

 Export filtered data —Export device group details
 based on the current filters. 

 Previous 

 Manage Configuration Versions (Draft Mode) 

 Next 

 Manage Prisma Browser Device Groups 

 On This Page 

 Activation & Onboarding 

 Strata Cloud Manager 

 Cloud Identity Engine 

 Strata Logging Service 

 Device Associations 

 Hub 

 Identity and Access Management 

 Tenant Management 

 SASE 

 Prisma Access 

 Strata Multitenant Cloud Manager 

 AI-Powered ADEM 

 Prisma Access Monitoring and Visibility 

 Prisma SD-WAN 

 ION Devices 

 Next-Generation CASB 

 Prisma Browser 

 Administration 

 Prisma Access 

 Strata Cloud Manager 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

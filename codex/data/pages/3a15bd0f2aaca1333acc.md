---
url: https://docs.paloaltonetworks.com/prisma-access-agent/administration/troubleshoot-prisma-access-agents/download-host-information-profile-reports-for-the-agent/what-hip-data-is-collected-by-the-agent
fetched_at: 2026-08-13T17:22:26Z
source: palo-alto-main
---

# What HIP Data is Collected by the Prisma Access Agent Clear

What HIP Data is Collected by the Prisma Access Agent 

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

 What HIP Data is Collected by the Prisma Access Agent 

 Updated on 

 Wed Jul 29 16:23:07 PDT 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma Access Agent Docs 

 Administration 

 User Guide 

 Release Notes 

 New Features 

 Updated on 

 Wed Jul 29 16:23:07 PDT 2026 

 Focus 

 Home 

 Prisma Access Agent 

 Prisma Access Agent Administration 

 Troubleshoot Prisma Access Agents 

 Download Host Information Profile Reports for Prisma Access Agents 

 What HIP Data is Collected by the Prisma Access Agent 

 Download PDF 

 Prisma Access Agent 

 What HIP Data is Collected by the Prisma Access Agent 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma Access Agent Docs 

 Administration 

 User Guide 

 Release Notes 

 New Features 

 Previous 

 Download Host Information Profile Reports for Prisma Access Agents 

 Next 

 Download Prisma Access Agent Logs 

 What HIP Data is Collected by the Prisma Access Agent 

 Review the types of Host Information Profile data that is collected by the Prisma Access Agent . 

 Where Can I Use This? What Do I Need? 

 Prisma Access (Managed by Strata Cloud Manager) 

 Prisma Access (Managed by Panorama) 

 NGFW (Managed by Panorama) 

 Check the prerequisites for the deployment you're
 using 

 Contact your Palo Alto Networks account representative to
 activate the Prisma Access Agent feature 

 The Host Information Profile (HIP) feature enables you to collect information about the
 security status of your endpoints—such as whether they have the latest security patches
 and antivirus definitions installed, whether they have disk encryption enabled, whether
 the endpoint is jailbroken or rooted, or whether it is running specific software you
 require within your organization—and base the decision as to whether to allow or deny
 access to a specific host based on adherence to the host policies you define. 

 The Prisma Access Agent collects information about the host that the agent runs on
 and submits the host information to the gateway upon successful connection. The gateway
 checks the raw host information against any HIP objects and HIP profiles that have been
 defined. If it finds a violation, the corresponding security policy is enforced. For
 example, you can configure endpoints to have a minimum version of anti-malware software
 installed before they are allowed access to corporate resources and applications. 

 By default, the Prisma Access Agent collects vendor-specific data about the end
 user security packages that are running on the endpoint and reports this data to the
 gateway for policy enforcement. The agent uses OPSWAT technology to assess the security
 posture of endpoints connecting to the network. You can configure HIP data collection settings in the Prisma Access Agent
 Settings . 

 HIP Retry 

 ( Prisma Access Agent 25.7 ) Prisma Access Agent automatically attempts to
 resubmit HIP reports when initial transmission to the gateway fails due to network
 timeouts or connectivity issues. The agent performs up to three retry attempts using
 non-configurable timeout values for HIP check and HIP send requests to the gateway
 and logs all retry attempts with timestamps for troubleshooting purposes. You can
 monitor retry status through the pacli hip status command,
 which provides visibility into retry attempts and their outcomes. 

 What Data Does Prisma Access Agent Collect on Desktop Devices? 

 Prisma Access Agent collects the following types of data for desktop devices
 (macOS, Windows, and Linux): 

 HIP Data Category Description 

 General 

 Information about the host itself, including the hostname, logon
 domain, operating system, app version, and, for Windows systems,
 the domain to which the machine belongs. 

 Patch Management 

 Information about any patch management software that is enabled
 or installed on the host and whether thy are missing any
 patches. 

 Not supported on Panorama Managed
 deployments. 

 Firewall 

 Information about any firewalls that are installed or enabled on
 the host. 

 Anti-malware 

 Information about any antivirus or anti-spyware software that is
 enabled or installed on the endpoint, whether or not real-time
 protection is enabled, the virus definition version, last scan
 time, and the vendor and product name. 

 Disk Backup 

 Information about whether disk backup software is installed, the
 last backup time, and the vendor and product name of the
 software. 

 Disk Encryption 

 Information about whether disk encryption software is installed,
 which paths are configured for encryption, and the vendor and
 product name of the software. 

 Data Loss Prevention 

 Information about whether data loss prevention (DLP) software is
 installed or enabled to prevent sensitive corporate information
 from leaving the corporate network or from being stored on a
 potentially insecure device. This information is only collected
 from Windows endpoints. 

 Certificate 

 Information about the machine certificate installed on the
 endpoint. 

 Custom Checks 

 Information about whether specific registry keys (Windows only),
 property lists (plists) (macOS only), process lists (Linux
 only), or operating system processes and user-space application
 processes are present. 

 What Data Does Prisma Access Agent Collect on iOS? 

 ( Prisma Access Agent 
 25.7 ) The following table describes the data collected by the Prisma Access Agent app on iOS devices: 

 HIP Report Attribute Description 

 Report Generation Time 

 Date and time that the HIP report was generated. 

 User IP Address 

 IP address of the users’ iOS device. 

 Machine Name 

 User-assigned device name + identifierForVendor 

 The user-assigned device name will defer depending on the
 device's iOS version. 

 In iOS 15 and earlier, the name property returns the
 device's name (for example, "Adam's iPhone"). 

 In iOS 16 and later, the name property returns a generic
 device name by default (for example, "iPhone"). 

 Domain 

 Field is empty on iOS devices. 

 Serial Number 

 Field is empty on iOS device. 

 Managed 

 Value that indicates whether the iOS device is managed. If this
 value is set to Yes , the device is
 managed. If this value is set to No , the
 device is unmanaged. 

 OS 

 Application name and vendor name of the target OS. 

 Host ID 

 Unique ID that is assigned by Prisma Access Agent to identify the
 host. The host ID value is UDID on iOS devices. 

 Client Version 

 Version number of the currently installed Prisma Access Agent 
 app. 

 WiFi SSID 

 Information about the network connectivity such as
 WiFi SSID on the iOS device. 

 Network Interface 

 Following settings are identified for the network interface: 

 Interface —Type of network
 interface detected on the iOS device. 

 MAC Address —MAC address is the
 unique hardware identifier assigned to each network
 interface on the iOS device. 

 IP Address —IP address assigned to
 each network interface on the iOS device. 

 Mobile Device 

 Information about the mobile device, including the device name,
 logon domain, operating system, app version, and the network to
 which the device is connected. 

 Device Compliance 

 Following attributes are used to determine the compliance status
 of the iOS device: 

 Rooted/Jailbroken —Status on the
 iOS device that has been rooted or jailbroken to obtain
 administrative privileges. The security policies can be
 removed or bypassed in the operating system from a
 compromised device. 

 Disk Encryption Not Set —Status on
 the iOS device that is enabled for disk encryption. 

 Passcode Not Set —Status on the iOS
 device that is set to a passcode. 

 Has Malware —Status on the iOS
 device that has malware-infected apps installed. 

 MDM Attributes 

 When you integrate your Prisma Access Agent deployment with an
 MDM vendor, the Prisma Access Agent app for iOS devices can
 obtain the following data attributes and tags from the MDM
 system: 

 udid —Unique device identifier
 (UDID) of the iOS device. 

 managed-by-mdm —Value that
 indicates whether the iOS device is managed. If this
 value is set to Yes , the iOS
 device is managed. If this value is set to
 No , the iOS device is
 unmanaged. 

 tag —Tags to enable you to match
 against other MDM-based attributes. 

 compliance —Compliance status that
 indicates whether the iOS device is compliant with the
 compliance policies that you have defined. 

 ownership —Ownership category of
 the iOS device (for example, Employee
 Owned ). This value is appended to the
 Tag attribute in the HIP
 report. 

 What Data Does Prisma Access Agent Collect on Android? 

 ( Prisma Access Agent 
 25.7 ) The following table describes the data collected by the Prisma Access Agent app on Android devices: 

 The Prisma Access Agent app for Android on a Chromebook uses the same HIP
 report attributes. 

 HIP Report Attribute Description 

 Report Generation Time 

 Date and time that the HIP report was generated. 

 User IP Address 

 IP address of the users’ Android device. 

 Machine Name 

 Host name and serial number of the Android device. 

 Domain 

 Field is empty on Android devices. 

 Serial Number 

 Serial number of the Android device. 

 Managed 

 Value that indicates whether the Android device is managed. If
 this value is set to Yes , the device is
 managed. If this value is set to No , the
 device is unmanaged. 

 OS 

 Application name and vendor name of the target OS. 

 Host ID 

 Prisma Access Agent assigned unique alphanumeric string with
 length of 16 characters to identify the host. The host ID value
 is Android ID on Android devices. 

 Client Version 

 Version number of the currently installed Prisma Access Agent 
 app. 

 WiFi SSID 

 Specific information about the network connectivity such as
 WiFi SSID on the Android device. 

 Network Interface 

 Following settings are identified for the network interface: 

 Interface —Type of network
 interface detected on the Android device. 

 MAC Address —MAC address is the
 unique hardware identifier assigned to each network
 interface on the Android device. 

 IP Address —IP address assigned to
 each network interface on the Android device. 

 Mobile Device 

 Information about the mobile device, including the device name,
 logon domain, operating system, app version, and the network to
 which the device is connected. 

 Tags 

 Tags to enable you to match against other MDM-based
 attributes. 

 Device Compliance 

 The Rooted/Jailbroken attribute is used to
 determine the compliance status of the Android device that has
 been rooted or jailbroken to obtain administrative privileges.
 The security policies can be removed or bypassed in the
 operating system from a compromised device. 

 Passcode Not Set —Status on the iOS device
 that is set to a passcode. 

 MDM Attributes 

 When you integrate your Prisma Access Agent deployment with an
 MDM vendor, the Prisma Access Agent app for Android devices can
 obtain the following data attributes and tags from the MDM
 system: 

 udid —Unique device identifier
 (UDID) of the Android device. 

 managed-by-mdm —Value that
 indicates whether the Android device is managed. If this
 value is set to Yes , the Android
 device is managed. If this value is set to
 No , the Android device is
 unmanaged. 

 tag —Tags to enable you to match
 against other MDM-based attributes. 

 compliance —Compliance status that
 indicates whether the Android device is compliant with
 the compliance policies that you have defined. 

 ownership —Ownership category of
 the Android device (for example, Employee
 Owned ). This value is appended to the
 Tag attribute in the HIP
 report. 

 Previous 

 Download Host Information Profile Reports for Prisma Access Agents 

 Next 

 Download Prisma Access Agent Logs 

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

 Visibility & Monitoring 

 Dashboards 

 Incidents and Alerts 

 Reports 

 Autonomous DEM 

 Best Practices 

 Best Practices Library 

 Experts Corner 

 Solutions Docs from Product Experts 

 Prisma Access Agent 

 Next-Generation Firewall 

 Administration 

 Prisma Access 

 Panorama 

 Strata Cloud Manager 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

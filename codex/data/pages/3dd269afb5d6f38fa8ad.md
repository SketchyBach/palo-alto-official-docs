---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsiam/protect-your-endpoints/endpoint-security/install-and-manage-endpoints/harden-endpoint-security/host-inventory
fetched_at: 2026-09-06T09:30:36Z
source: cortex-platform
---

# Host Inventory | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSIAM 

 Cortex XSIAM Documentation 

 Protect your endpoints 

 Endpoint security 

 Install and manage endpoints 

 Harden endpoint security 

 Cortex XSIAM 

 Host Inventory 

 Use Cortex XSIAM Host Inventory to review endpoint hardware, software, services, and security details. 

 Cortex XSIAM Host Inventory, also called Host Insights, provides endpoint asset inventory and operational visibility. Review hardware, software, services, and autoruns across endpoints to identify IT and security issues, such as suspicious services or new autoruns. 

 Host Inventory data collection 

 The Cortex XDR agent scans the endpoint every 24 hours for any updates and displays the data found over the last 30 days. Alternatively, you can rescan the endpoint to retrieve the most updated data. It can take Cortex XSIAM up to 6 hours to collect initial data from all endpoints in your network. 

 Host Inventory prerequisites 

 The following requirements apply when enabling Host Inventory: 

 Requirement 

 Description 

 Supported Platforms 

 Windows, Mac, and Linux. 

 Setup and Permissions 

 Ensure Host Inventory Data Collection is enabled for your Cortex XDR agent. 

 Host Inventory entities 

 Cortex XSIAM Host Inventory includes the following endpoint entities by operating system: 

 Entity 

 Windows 

 Mac 

 Linux 

 Accessibility 

 – 

 ✓ 

 – 

 Applications 

 ✓ 

 ✓ 

 ✓ 

 Autoruns 

 ✓ 

 ✓ 

 ✓ 

 Daemons 

 – 

 ✓ 

 ✓ 

 Disks 

 ✓ 

 ✓ 

 ✓ 

 Drivers 

 ✓ 

 – 

 ✓ 

 Extensions 

 – 

 ✓ 

 – 

 Groups 

 ✓ 

 ✓ 

 ✓ 

 Mounts 

 – 

 ✓ 

 ✓ 

 Services 

 ✓ 

 – 

 – 

 Shares 

 ✓ 

 ✓ 

 ✓ 

 System Information 

 ✓ 

 ✓ 

 ✓ 

 Users 

 ✓ 

 ✓ 

 – 

 Users to Groups 

 ✓ 

 ✓ 

 ✓ 

 For each entity, Cortex XSIAM lists all the details about the entity, and the details about the endpoint it applies to. For example, the default Services view lists a separate row for every service on every endpoint: 

 Alternatively, to better understand the overall presence of each entity on the total number of endpoints, you can switch to an aggregated view (click ) and group the data by the main entity. You can also sort and filter according to the number of affected endpoints. For example, in the Services aggregated view, you can sort by the number of affected endpoints to identify the least commonly deployed service in your network. To get a closer view of all endpoints, right-click and select View affected endpoints. 

 View Host Inventory 

 To view the Host inventory, go to Inventory → Endpoints → Host Inventory. You can export the tables and respective asset views to a tab-separated values (TSV) file. 

 If you have Cloud Posture Security, Cloud Runtime Security, or Cortex XSIAM Premium licenses, go to Inventory → Host Insights → Host Inventory. 

 Data 

 Description 

 Accessibility 

 Details about installed applications that require and were allowed special permissions to enable a camera, microphone, accessibility features, full disk access, or screen captures. 

 Applications 

 Details about all applications installed on your endpoints. 

 For each application, Cortex XSIAM lists the existing CVEs and the vulnerability severity score that reflects the highest NIST vulnerability score detected for the application. 

 To further examine these vulnerabilities, see Application Analysis . 

 Autoruns 

 Details about executables that start automatically when the user logs in or boots the endpoint. 

 Cortex XSIAM displays information about autoruns that are configured in the endpoint Registry, startup folders, scheduled tasks, services, drivers, daemons, extensions, Crond tasks, login items, login, and logout hooks. 

 For each autorun, Cortex XSIAM lists the autorun type and configuration, such as startup method, CMD, user details, and image path. 

 Daemons 

 Details about all daemons that exist on the endpoint. 

 For each daemon, Cortex XSIAM lists the following details. 

 Information about the daemon, such as the name, type, and path 

 Daemon state, indicating whether it is loaded, running, or not running 

 Disks 

 Details about the disk volumes that exist on an endpoint. 

 For each disk that exists on an endpoint, Cortex XSIAM lists details such as the drive type, name, file system, free space, and total size. 

 Drivers 

 Details about all the drivers installed on an endpoint. 

 For each driver, Cortex XSIAM lists all the following details: 

 Information about the driver, such as the driver name, type, and path. 

 Listing details about the driver runtime configuration: 

 Driver type 

 Whether the driver is currently running, in which mode, and the runtime state 

 Extensions 

 Details about the system and kernel extensions currently running on your Mac endpoints. 

 For each extension, Cortex XSIAM lists the following details: 

 Extension type, name, path, and version 

 Extension state, indicating whether it is running, requires enabling, or unloaded 

 Groups 

 Details about all user groups defined on an endpoint. 

 For each group, Cortex XSIAM lists identifying details, such as name, SID/GID name, and type. 

 Mounts 

 Details about all the drives, volumes, and disks that were mounted on endpoints. 

 For each mount, Cortex XSIAM lists the mount point directory, file system type, mount spec, and GUID. 

 Services 

 Details about all the services running on an endpoint. 

 For each service, Cortex XSIAM lists all the following details: 

 Information about the service, such as the service name, type, and path 

 Listing details about the service runtime configuration and status: 

 Whether the service is currently running and what is the runtime state 

 Whether you can stop, pause, or delay the service start time 

 Whether the service requires interaction with the endpoint desktop 

 The name of the user who started the service and the start mode 

 Shares 

 Details about network shared folders defined on an endpoint. 

 For each folder, Cortex XSIAM lists all the following details: 

 Shared network folder type: Disk Drive, Print Queue, Device, IPC, Disk Drive Admin, Print Queue Admin, Device Admin, IPC Admin 

 Identifying details such as folder name, description, and path 

 Whether the folder is limited to a maximum number of shares, and the maximum number of allowed shares 

 System Information 

 General system information about an endpoint. 

 For each endpoint, Cortex XSIAM lists all the following details: 

 Information about the endpoint hardware, such as manufacturer, model, physical memory, processor architecture, and CPU 

 The operating system name and release running on the endpoint 

 Users 

 List of users whose credentials are stored on the endpoint. 

 For each user, Cortex XSIAM lists all the following details. 

 Identifying details about the user, such as name and SID/UID 

 Details about the account, such as whether the account is active and the account type 

 Information about the password set for this user account, such as whether it is required to login, has an expiration date or can be changed 

 Users to Groups 

 A list mapping all the users, local and in your domain, to the existing user groups on an endpoint. 

 Cortex XSIAM includes only the first 10,000 results per endpoint. 

 Cortex XSIAM lists only users that belong to each group directly, and does not include users who belong to a group within the main group. 

 If a local users group includes a domain user (whose credentials are stored on the Domain Controller server and not on the endpoint), Cortex XSIAM includes this user in the user-to-group mapping, but does not include it in the user's insights view. 

 Previous Disk encryption 

 Next Vulnerability Assessment 

 Last updated 12 days ago 

 Was this helpful?

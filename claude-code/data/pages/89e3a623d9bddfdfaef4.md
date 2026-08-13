---
url: https://docs.paloaltonetworks.com/iot/integration/attribute-reference/attribute-reference-microsoft-windows-server
fetched_at: 2026-08-13T16:37:02Z
source: palo-alto-main
---

# Microsoft Windows Server Attribute Reference Clear

Microsoft Windows Server Attribute Reference 

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

 Microsoft Windows Server Attribute Reference 

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

 Attribute Reference 

 Microsoft Windows Server Attribute Reference 

 Download PDF 

 Device Security 

 Microsoft Windows Server Attribute Reference 

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

 Microsoft SCCM Attribute Reference 

 Next 

 NetBox Attribute Reference 

 Microsoft Windows Server Attribute Reference 

 This reference lists the attributes that Device Security collects from Microsoft Windows
 Server, their names as stored in Device Security , and the Device Security fields
 they map to.

 Device Security integrates with Microsoft Windows Server to collect network data
 that enriches the device inventory. The attributes in this reference cover DHCP
 lease records and detailed device information gathered from the Windows Server
 DHCP service. 

 The third-party attribute name in Device Security refers to the attribute name
 as it appears in the Assets Inventory table and in Query Engine. This follows the format
 of third-party-name . attribute-name .
 When viewing the attribute name in the Assets Inventory table column selector or on a
 Device Details page, where the third-party name can be found as a header for the
 attributes section, then the third-party name is removed from the attribute name.

 For example, micrsoft_defender_xdr.macAddress would appear in the
 Query Builder and in the Assets Inventory table, but under Device Details Attributes Integration Specific Attributes Microsoft Defender , the attribute would appear as macAddress .

 DHCP Lease Attributes 

 Device Security collects DHCP lease attributes from the Microsoft Windows Server DHCP service. Each record describes an active or historical DHCP lease assigned to a device.
 The following table lists each Microsoft Windows Server attribute, its name as stored
 in Device Security , and the Device Security field it maps to (if applicable).

 Microsoft Windows Server Attribute 

 Device Security Attribute Name 

 Device Security Common Attribute* 

 Description 

 is_ip_address_static 

 microsoft_windows_server.is_ip_address_static 

 — 

 Indicates whether the IP address is statically assigned 

 — 

 — 

 is_ip_address_static 

 Indicates whether the IP address is statically assigned 

 LeaseExpiryTime 

 — 

 dhcp_lease_expiry_time 

 Expiration date and time of the DHCP lease 

 IPAddress.IsIPv6Multicast 

 microsoft_windows_server.IPAddress.IsIPv6Multicast 

 — 

 Indicates whether the address is an IPv6 multicast address 

 IPAddress.IsIPv6SiteLocal 

 microsoft_windows_server.IPAddress.IsIPv6SiteLocal 

 — 

 Indicates whether the address is an IPv6 site-local address 

 IPAddress.IsIPv6Teredo 

 microsoft_windows_server.IPAddress.IsIPv6Teredo 

 — 

 Indicates whether the address is an IPv6 Teredo address 

 IPAddress.IPAddressToString 

 microsoft_windows_server.IPAddress.IPAddressToString 

 — 

 IP address as a string 

 IPAddress.IsIPv6LinkLocal 

 microsoft_windows_server.IPAddress.IsIPv6LinkLocal 

 — 

 Indicates whether the address is an IPv6 link-local address 

 IPAddress.IsIPv4MappedToIPv6 

 microsoft_windows_server.IPAddress.IsIPv4MappedToIPv6 

 — 

 Indicates whether the IPv4 address is mapped to IPv6 

 IPAddress.ScopeId 

 microsoft_windows_server.IPAddress.ScopeId 

 — 

 Scope ID of the IP address 

 IPAddress.AddressFamily 

 microsoft_windows_server.IPAddress.AddressFamily 

 — 

 Address family (IPv4 or IPv6) 

 IPAddress.Address 

 microsoft_windows_server.IPAddress.Address 

 — 

 Numeric IP address value 

 ScopeId.IsIPv6Multicast 

 microsoft_windows_server.ScopeId.IsIPv6Multicast 

 — 

 Indicates whether the address is an IPv6 multicast address 

 ScopeId.IsIPv6LinkLocal 

 microsoft_windows_server.ScopeId.IsIPv6LinkLocal 

 — 

 Indicates whether the address is an IPv6 link-local address 

 ScopeId.IsIPv6SiteLocal 

 microsoft_windows_server.ScopeId.IsIPv6SiteLocal 

 — 

 Indicates whether the address is an IPv6 site-local address 

 ScopeId.IsIPv6Teredo 

 microsoft_windows_server.ScopeId.IsIPv6Teredo 

 — 

 Indicates whether the address is an IPv6 Teredo address 

 ScopeId.IsIPv4MappedToIPv6 

 microsoft_windows_server.ScopeId.IsIPv4MappedToIPv6 

 — 

 Indicates whether the IPv4 address is mapped to IPv6 

 ScopeId.IPAddressToString 

 microsoft_windows_server.ScopeId.IPAddressToString 

 — 

 IP address as a string 

 ScopeId.ScopeId 

 microsoft_windows_server.ScopeId.ScopeId 

 — 

 Scope ID of the IP address 

 ScopeId.AddressFamily 

 microsoft_windows_server.ScopeId.AddressFamily 

 — 

 Address family (IPv4 or IPv6) 

 ScopeId.Address 

 microsoft_windows_server.ScopeId.Address 

 — 

 Numeric IP address value 

 PSComputerName 

 microsoft_windows_server.PSComputerName 

 — 

 PowerShell computer name (source server) 

 ServerIP 

 microsoft_windows_server.ServerIP 

 — 

 IP address of the DHCP server 

 ProbationEnds 

 microsoft_windows_server.ProbationEnds 

 — 

 Date and time the NAP probation period ends 

 PolicyName 

 microsoft_windows_server.PolicyName 

 — 

 DHCP policy name applied to the lease 

 NapStatus 

 microsoft_windows_server.NapStatus 

 — 

 Network Access Protection status of the device 

 NapCapable 

 microsoft_windows_server.NapCapable 

 — 

 Indicates whether the device is Network Access Protection capable 

 LeaseExpiryTime 

 microsoft_windows_server.LeaseExpiryTime 

 — 

 DHCP lease expiry timestamp 

 HostName 

 microsoft_windows_server.HostName 

 — 

 Hostname of the device 

 DnsRR 

 microsoft_windows_server.DnsRR 

 — 

 DNS resource record associated with the lease 

 DnsRegistration 

 microsoft_windows_server.DnsRegistration 

 — 

 DNS registration status of the lease 

 Description 

 microsoft_windows_server.Description 

 — 

 Description of the DHCP lease 

 ClientType 

 microsoft_windows_server.ClientType 

 — 

 DHCP client type (DHCP or static) 

 ClientId 

 microsoft_windows_server.ClientId 

 — 

 DHCP client identifier (MAC address) 

 AddressState 

 microsoft_windows_server.AddressState 

 — 

 Address state of the DHCP lease 

 HostName 

 — 

 Hostname 

 Hostname of the device 

 — 

 — 

 ipv4_address 

 IPv4 address of the device 

 ClientId 

 — 

 MAC Address 

 MAC address of the device 

 Device Detail Attributes 

 Device Security collects device detail attributes from Microsoft Windows Server. Each record provides hardware, operating system, and network configuration details for a managed device.
 The following table lists each Microsoft Windows Server attribute, its name as stored
 in Device Security , and the Device Security field it maps to (if applicable).

 Microsoft Windows Server Attribute 

 Device Security Attribute Name 

 Device Security Common Attribute* 

 Description 

 BitlockerStatus.KeyProtector 

 microsoft_windows_server.BitlockerStatus.KeyProtector 

 — 

 List of BitLocker key protectors for the volume 

 BitlockerStatus.ProtectionStatus 

 microsoft_windows_server.BitlockerStatus.ProtectionStatus 

 — 

 BitLocker protection status of the volume 

 BitlockerStatus.MountPoint 

 microsoft_windows_server.BitlockerStatus.MountPoint 

 — 

 Drive mount point of the BitLocker volume 

 BitlockerStatus.MetadataVersion 

 microsoft_windows_server.BitlockerStatus.MetadataVersion 

 — 

 Metadata version of the BitLocker volume 

 BitlockerStatus.VolumeStatus 

 microsoft_windows_server.BitlockerStatus.VolumeStatus 

 — 

 Status of the BitLocker volume 

 BitlockerStatus.VolumeType 

 microsoft_windows_server.BitlockerStatus.VolumeType 

 — 

 Type of the BitLocker volume 

 BitlockerStatus.WipePercentage 

 microsoft_windows_server.BitlockerStatus.WipePercentage 

 — 

 Percentage of the volume that has been wiped 

 BitlockerStatus.LockStatus 

 microsoft_windows_server.BitlockerStatus.LockStatus 

 — 

 Lock status of the BitLocker volume 

 BitlockerStatus.EncryptionPercentage 

 microsoft_windows_server.BitlockerStatus.EncryptionPercentage 

 — 

 Percentage of the volume that is encrypted 

 BitlockerStatus.EncryptionMethodFlags 

 microsoft_windows_server.BitlockerStatus.EncryptionMethodFlags 

 — 

 Flags describing the BitLocker encryption method 

 BitlockerStatus.EncryptionMethod 

 microsoft_windows_server.BitlockerStatus.EncryptionMethod 

 — 

 BitLocker encryption method used 

 BitlockerStatus.CapacityGB 

 microsoft_windows_server.BitlockerStatus.CapacityGB 

 — 

 Volume capacity in gigabytes 

 BitlockerStatus.AutoUnlockKeyStored 

 microsoft_windows_server.BitlockerStatus.AutoUnlockKeyStored 

 — 

 Indicates whether the BitLocker auto-unlock key is stored 

 BitlockerStatus.AutoUnlockEnabled 

 microsoft_windows_server.BitlockerStatus.AutoUnlockEnabled 

 — 

 Indicates whether BitLocker auto-unlock is enabled 

 BitlockerStatus.ComputerName 

 microsoft_windows_server.BitlockerStatus.ComputerName 

 — 

 Name of the computer 

 SystemManufacturer 

 microsoft_windows_server.SystemManufacturer 

 — 

 System manufacturer (hardware vendor) 

 ProcessorName 

 microsoft_windows_server.ProcessorName 

 — 

 Processor name and model 

 ProcessorManufacturer 

 microsoft_windows_server.ProcessorManufacturer 

 — 

 Processor manufacturer 

 ProcessorFamily 

 microsoft_windows_server.ProcessorFamily 

 — 

 Processor family 

 PSComputerName 

 microsoft_windows_server.PSComputerName 

 — 

 PowerShell computer name (source server) 

 OSVersion 

 microsoft_windows_server.OSVersion 

 — 

 Operating system version 

 OSSuiteMask 

 microsoft_windows_server.OSSuiteMask 

 — 

 Bitmask representing the operating system suite 

 OSSuite 

 microsoft_windows_server.OSSuite 

 — 

 Operating system suite 

 OSSku 

 microsoft_windows_server.OSSku 

 — 

 Operating system SKU 

 OSName 

 microsoft_windows_server.OSName 

 — 

 Operating system name 

 NumberOfProcessors 

 microsoft_windows_server.NumberOfProcessors 

 — 

 Number of physical processors 

 Name 

 microsoft_windows_server.Name 

 — 

 Device name 

 MacAddress 

 microsoft_windows_server.MacAddress 

 — 

 MAC address of the device 

 IPAddress 

 microsoft_windows_server.IPAddress 

 — 

 IP address of the device 

 NumberOfLogicalProcessors 

 microsoft_windows_server.NumberOfLogicalProcessors 

 — 

 Number of logical processors 

 NumberOfCores 

 microsoft_windows_server.NumberOfCores 

 — 

 Number of CPU cores 

 Model 

 microsoft_windows_server.Model 

 — 

 Device model 

 CollectedDateTime 

 microsoft_windows_server.CollectedDateTime 

 — 

 Date and time the data was collected 

 ChassisSerialNumber 

 microsoft_windows_server.ChassisSerialNumber 

 — 

 Chassis serial number of the device 

 ChassisSerialNumber 

 — 

 Serial Number 

 Device serial number 

 NetworkAdapters 

 — 

 third_party_learned_network_interfaces 

 Network interface data collected from the device 

 InstalledSoftware 

 — 

 third_party_learned_installed_software 

 Installed software data collected from the device 

 OSVersion 

 — 

 OS Version 

 Operating system version 

 OSName 

 — 

 OS Name 

 Operating system name 

 SystemManufacturer 

 — 

 Vendor 

 System manufacturer (hardware vendor) 

 Name 

 — 

 Hostname 

 Hostname of the device 

 IPAddress 

 — 

 ipv4_address 

 IPv4 address of the device 

 MacAddress 

 — 

 MAC Address 

 MAC address of the device 

 * Only some attributes map to a Device Security Common Attribute. 

 Previous 

 Microsoft SCCM Attribute Reference 

 Next 

 NetBox Attribute Reference 

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

 Reference 

 Cloud-Delivered Security Services 

 Integrations 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

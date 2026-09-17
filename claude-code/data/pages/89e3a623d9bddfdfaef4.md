---
url: https://docs.paloaltonetworks.com/iot/integration/attribute-reference/attribute-reference-microsoft-windows-server
fetched_at: 2026-09-15T15:14:39Z
source: palo-alto-main
---

# Microsoft Windows Server Attribute Reference Clear

Updated on 

 Mon Aug 17 11:22:37 PDT 2026 

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

 NetBox Labs Attribute Reference 

 Microsoft Windows Server Attribute Reference 

 This reference lists the attributes that Device Security collects from Microsoft Windows Server,
 their names as stored in Device Security , and the Device Security fields they map to.

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

 Dhcp Leases Attributes 

 Device Security collects dhcp leases attributes from Microsoft Windows Server. The following table lists each Microsoft Windows Server attribute, its name as stored in Device Security , and the Device Security field it maps to (if applicable).

 Microsoft Windows Server Attribute 

 Device Security Attribute Name 

 Device Security Common Attribute* 

 Description 

 LeaseExpiryTime 

 microsoft_windows_server.LeaseExpiryTime 

 dhcp_lease_expiry_time 

 LeaseExpiryTime 

 HostName 

 microsoft_windows_server.HostName 

 hostname 

 HostName 

 IPAddress.IPAddressToString 

 microsoft_windows_server.IPAddress.IPAddressToString 

 IP Address 

 IPAddressToString 

 Type 

 microsoft_windows_server.is_ip_address_static 

 is_ip_address_static 

 Type 

 ClientId 

 microsoft_windows_server.ClientId 

 MAC; id 

 ClientId 

 AddressState 

 microsoft_windows_server.AddressState 

 — 

 AddressState 

 ClientType 

 microsoft_windows_server.ClientType 

 — 

 ClientType 

 Description 

 microsoft_windows_server.Description 

 — 

 Description 

 DnsRegistration 

 microsoft_windows_server.DnsRegistration 

 — 

 DnsRegistration 

 DnsRR 

 microsoft_windows_server.DnsRR 

 — 

 DnsRR 

 IPAddress.Address 

 microsoft_windows_server.IPAddress.Address 

 — 

 Address 

 IPAddress.AddressFamily 

 microsoft_windows_server.IPAddress.AddressFamily 

 — 

 AddressFamily 

 IPAddress.IsIPv4MappedToIPv6 

 microsoft_windows_server.IPAddress.IsIPv4MappedToIPv6 

 — 

 IsIPv4MappedToIPv6 

 IPAddress.IsIPv6LinkLocal 

 microsoft_windows_server.IPAddress.IsIPv6LinkLocal 

 — 

 IsIPv6LinkLocal 

 IPAddress.IsIPv6Multicast 

 microsoft_windows_server.IPAddress.IsIPv6Multicast 

 — 

 IsIPv6Multicast 

 IPAddress.IsIPv6SiteLocal 

 microsoft_windows_server.IPAddress.IsIPv6SiteLocal 

 — 

 IsIPv6SiteLocal 

 IPAddress.IsIPv6Teredo 

 microsoft_windows_server.IPAddress.IsIPv6Teredo 

 — 

 IsIPv6Teredo 

 IPAddress.ScopeId 

 microsoft_windows_server.IPAddress.ScopeId 

 — 

 ScopeId 

 NapCapable 

 microsoft_windows_server.NapCapable 

 — 

 NapCapable 

 NapStatus 

 microsoft_windows_server.NapStatus 

 — 

 NapStatus 

 PolicyName 

 microsoft_windows_server.PolicyName 

 — 

 PolicyName 

 ProbationEnds 

 microsoft_windows_server.ProbationEnds 

 — 

 ProbationEnds 

 PSComputerName 

 microsoft_windows_server.PSComputerName 

 — 

 PSComputerName 

 ScopeId.Address 

 microsoft_windows_server.ScopeId.Address 

 — 

 Address 

 ScopeId.AddressFamily 

 microsoft_windows_server.ScopeId.AddressFamily 

 — 

 AddressFamily 

 ScopeId.IPAddressToString 

 microsoft_windows_server.ScopeId.IPAddressToString 

 — 

 IPAddressToString 

 ScopeId.IsIPv4MappedToIPv6 

 microsoft_windows_server.ScopeId.IsIPv4MappedToIPv6 

 — 

 IsIPv4MappedToIPv6 

 ScopeId.IsIPv6LinkLocal 

 microsoft_windows_server.ScopeId.IsIPv6LinkLocal 

 — 

 IsIPv6LinkLocal 

 ScopeId.IsIPv6Multicast 

 microsoft_windows_server.ScopeId.IsIPv6Multicast 

 — 

 IsIPv6Multicast 

 ScopeId.IsIPv6SiteLocal 

 microsoft_windows_server.ScopeId.IsIPv6SiteLocal 

 — 

 IsIPv6SiteLocal 

 ScopeId.IsIPv6Teredo 

 microsoft_windows_server.ScopeId.IsIPv6Teredo 

 — 

 IsIPv6Teredo 

 ScopeId.ScopeId 

 microsoft_windows_server.ScopeId.ScopeId 

 — 

 ScopeId 

 ServerIP 

 microsoft_windows_server.ServerIP 

 — 

 ServerIP 

 Details Attributes 

 Device Security collects details attributes from Microsoft Windows Server. The following table lists each Microsoft Windows Server attribute, its name as stored in Device Security , and the Device Security field it maps to (if applicable).

 Microsoft Windows Server Attribute 

 Device Security Attribute Name 

 Device Security Common Attribute* 

 Description 

 Name 

 microsoft_windows_server.Name 

 hostname 

 Name 

 IPAddress 

 microsoft_windows_server.IPAddress 

 IP Address 

 IPAddress 

 MacAddress 

 microsoft_windows_server.MacAddress 

 MAC; id 

 MacAddress 

 OSName 

 microsoft_windows_server.OSName 

 OS Name 

 OSName 

 OSVersion 

 microsoft_windows_server.OSVersion 

 OS Version 

 OSVersion 

 ChassisSerialNumber 

 microsoft_windows_server.ChassisSerialNumber 

 Serial Number 

 ChassisSerialNumber 

 InstalledSoftware 

 — 

 third_party_learned_installed_software 

 InstalledSoftware 

 NetworkAdapters 

 — 

 third_party_learned_network_interfaces 

 NetworkAdapters 

 SystemManufacturer 

 microsoft_windows_server.SystemManufacturer 

 Vendor 

 SystemManufacturer 

 BitlockerStatus.AutoUnlockEnabled 

 microsoft_windows_server.BitlockerStatus.AutoUnlockEnabled 

 — 

 AutoUnlockEnabled 

 BitlockerStatus.AutoUnlockKeyStored 

 microsoft_windows_server.BitlockerStatus.AutoUnlockKeyStored 

 — 

 AutoUnlockKeyStored 

 BitlockerStatus.CapacityGB 

 microsoft_windows_server.BitlockerStatus.CapacityGB 

 — 

 CapacityGB 

 BitlockerStatus.ComputerName 

 microsoft_windows_server.BitlockerStatus.ComputerName 

 — 

 ComputerName 

 BitlockerStatus.EncryptionMethod 

 microsoft_windows_server.BitlockerStatus.EncryptionMethod 

 — 

 EncryptionMethod 

 BitlockerStatus.EncryptionMethodFlags 

 microsoft_windows_server.BitlockerStatus.EncryptionMethodFlags 

 — 

 EncryptionMethodFlags 

 BitlockerStatus.EncryptionPercentage 

 microsoft_windows_server.BitlockerStatus.EncryptionPercentage 

 — 

 EncryptionPercentage 

 BitlockerStatus.KeyProtector 

 microsoft_windows_server.BitlockerStatus.KeyProtector 

 — 

 KeyProtector 

 BitlockerStatus.LockStatus 

 microsoft_windows_server.BitlockerStatus.LockStatus 

 — 

 LockStatus 

 BitlockerStatus.MetadataVersion 

 microsoft_windows_server.BitlockerStatus.MetadataVersion 

 — 

 MetadataVersion 

 BitlockerStatus.MountPoint 

 microsoft_windows_server.BitlockerStatus.MountPoint 

 — 

 MountPoint 

 BitlockerStatus.ProtectionStatus 

 microsoft_windows_server.BitlockerStatus.ProtectionStatus 

 — 

 ProtectionStatus 

 BitlockerStatus.VolumeStatus 

 microsoft_windows_server.BitlockerStatus.VolumeStatus 

 — 

 VolumeStatus 

 BitlockerStatus.VolumeType 

 microsoft_windows_server.BitlockerStatus.VolumeType 

 — 

 VolumeType 

 BitlockerStatus.WipePercentage 

 microsoft_windows_server.BitlockerStatus.WipePercentage 

 — 

 WipePercentage 

 CollectedDateTime 

 microsoft_windows_server.CollectedDateTime 

 — 

 CollectedDateTime 

 Model 

 microsoft_windows_server.Model 

 — 

 Model 

 NumberOfCores 

 microsoft_windows_server.NumberOfCores 

 — 

 NumberOfCores 

 NumberOfLogicalProcessors 

 microsoft_windows_server.NumberOfLogicalProcessors 

 — 

 NumberOfLogicalProcessors 

 NumberOfProcessors 

 microsoft_windows_server.NumberOfProcessors 

 — 

 NumberOfProcessors 

 OSSku 

 microsoft_windows_server.OSSku 

 — 

 OSSku 

 OSSuite 

 microsoft_windows_server.OSSuite 

 — 

 OSSuite 

 OSSuiteMask 

 microsoft_windows_server.OSSuiteMask 

 — 

 OSSuiteMask 

 ProcessorFamily 

 microsoft_windows_server.ProcessorFamily 

 — 

 ProcessorFamily 

 ProcessorManufacturer 

 microsoft_windows_server.ProcessorManufacturer 

 — 

 ProcessorManufacturer 

 ProcessorName 

 microsoft_windows_server.ProcessorName 

 — 

 ProcessorName 

 PSComputerName 

 microsoft_windows_server.PSComputerName 

 — 

 PSComputerName 

 * Only some attributes map to a Device Security Common Attribute. 

 Previous 

 Microsoft SCCM Attribute Reference 

 Next 

 NetBox Labs Attribute Reference

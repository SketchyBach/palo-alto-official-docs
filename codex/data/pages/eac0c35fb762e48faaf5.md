---
url: https://docs.paloaltonetworks.com/ngfw/help/11-1/globalprotect/objects-globalprotect-hip-objects/hip-objects-general-tab
fetched_at: 2026-08-13T16:45:39Z
source: palo-alto-main
---

# HIP Objects General Tab Clear

HIP Objects General Tab 

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

 HIP Objects General Tab 

 Updated on 

 Thu Jun 25 17:39:35 PDT 2026 

 Focus 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 한국어 (Korean) 

 Filter

 Expand All 
 | 
 Collapse All 

 Next-Generation Firewall Docs 

 Getting Started 

 Administration 

 Networking 

 Quick Start 

 Reference 

 Incidents & Alerts 

 Release Notes 

 Select a Document 

 PAN-OS 12.2 

 PAN-OS 12.1 

 PAN-OS 11.2 

 PAN-OS 11.1 

 PAN-OS 11.0 (EoL) 

 PAN-OS 10.2 

 PAN-OS 10.1 (EoL) 

 PAN-OS 10.0 (EoL) 

 PAN-OS 9.1 (EoL) 

 PAN-OS 9.0 (EoL) 

 PAN-OS 8.1 (EoL) 

 Help 

 Select a Document 

 PAN-OS 12.2 

 PAN-OS 12.1 

 PAN-OS 11.2 

 PAN-OS 11.1 

 PAN-OS 10.2 

 PAN-OS 10.1 

 New Features 

 Updated on 

 Thu Jun 25 17:39:35 PDT 2026 

 Focus 

 Home 

 Next-Generation Firewall 

 GlobalProtect 

 Objects > GlobalProtect > HIP Objects 

 HIP Objects General Tab 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 한국어 (Korean) 

 Next-Generation Firewall 

 HIP Objects General Tab 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Next-Generation Firewall Docs 

 Getting Started 

 Administration 

 Networking 

 Quick Start 

 Reference 

 Incidents & Alerts 

 Release Notes 

 Select a Document 

 PAN-OS 12.2 

 PAN-OS 12.1 

 PAN-OS 11.2 

 PAN-OS 11.1 

 PAN-OS 11.0 (EoL) 

 PAN-OS 10.2 

 PAN-OS 10.1 (EoL) 

 PAN-OS 10.0 (EoL) 

 PAN-OS 9.1 (EoL) 

 PAN-OS 9.0 (EoL) 

 PAN-OS 8.1 (EoL) 

 Help 

 Select a Document 

 PAN-OS 12.2 

 PAN-OS 12.1 

 PAN-OS 11.2 

 PAN-OS 11.1 

 PAN-OS 10.2 

 PAN-OS 10.1 

 New Features 

 Previous 

 Objects > GlobalProtect > HIP Objects 

 Next 

 HIP Objects Mobile Device Tab 

 HIP Objects General Tab 

 Objects GlobalProtect HIP Objects <hip-object> General 

 Select the General tab to specify a name
for the new HIP object and configure the object to match against
general host information such as domain, operating system, or the
type of network connectivity it has. 

 HIP Object General Settings 

 Description 

 Name 

 Enter a name for the HIP object (up to 31
characters). The name is case-sensitive and must be unique. Use
only letters, numbers, spaces, hyphens, and underscores. 

 Shared 

 If you select Shared ,
the current HIP objects become available to: 

 Every virtual
system (vsys) on the firewall, if you are logged in to a firewall
that is in multiple virtual system mode. If you clear this selection, the
object will be available to only the vsys selected in the Virtual
System drop-down of the Objects tab.
For a firewall that is not in multi-vsys mode, this option is not
available in the HIP Object dialog. 

 All device groups on Panorama™.
If you clear this selection, the object will be available only to
the device group selected in the Device Group drop-down
of the Objects tab. 

 After you save
the object, you cannot change its Shared setting.
Select Objects GlobalProtect HIP Objects to see the current Location . 

 Description 

 ( Optional ) Enter a description. 

 Host Info 

 Select this option to activate the options
for configuring the host information. 

 Managed 

 Filter based on whether the endpoint is
managed or not managed. To match endpoints that are managed, select Yes .
To match endpoints that are not managed, select No . 

 Disable override ( Panorama only ) 

 Controls override access to the HIP object
in the device groups that are descendants of the Device
Group selected in the Objects tab.
Select this option to prevent administrators from creating local
copies of the object in descendant device groups by overriding its
inherited values. This option is cleared by default (override is
enabled). 

 Domain 

 To match on a domain name, choose an operator
from the drop-down and enter a string to match. 

 OS 

 To match on a host OS, choose Contains from
the first drop-down, select a vendor from the second drop-down, and
then select an OS version from the third drop-down; or you can select All to
match on any OS version from the selected vendor. 

 Client Version 

 To match on a specific version number, select
an operator from the drop-down and then enter a string to match
(or not match) in the text box. 

 Host Name 

 To match on a specific host name or part
of a host name, select an operator from the drop-down and then enter
a string to match (or not match, depending on what operator you
selected) in the text box. 

 Host ID 

 The host ID is a unique ID that GlobalProtect
assigns to identify the host. The host ID value varies by device
type: 

 Windows —Machine GUID stored in the Windows
registry (HKEY_Local_Machine\Software\Microsoft\Cryptography\MachineGuid) 

 macOS —MAC address of the first built-in physical network
interface 

 Android —Android ID 

 iOS —UDID 

 Linux —Product UUID retrieved from the system DMI table 

 Chrome —GlobalProtect-assigned unique alphanumeric
string with length of 32 characters 

 To match on
a specific host ID, select the operator from the drop-down and then
enter a string to match (or not match, depending on what operator
you selected) in the text box. 

 Serial Number 

 To match on all or part of an endpoint serial
number, choose an operator from the drop-down and then enter a string
to match. 

 Network 

 Use this field to enable filtering on a
specific mobile device network configuration. This match criteria
applies to mobile devices only. 

 Select an operator from the
drop-down and then select the type of network connection to filter
on from the second drop-down: Wifi , Mobile , Ethernet (available
only for Is Not filters), or Unknown .
After you select a network type, enter any additional strings to
match on, if available, such as the Mobile Carrier or
Wifi SSID . 

 Previous 

 Objects > GlobalProtect > HIP Objects 

 Next 

 HIP Objects Mobile Device Tab 

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

 Cloud Management for NGFWs 

 Cloud NGFW for AWS 

 Cloud NGFW for Azure 

 CN-Series 

 Firewalls 

 PAN-OS 

 PAN-OS SD-WAN 

 Service Provider 

 VM-Series 

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

 Shared Policy for NGFWs and Prisma Access 

 Visibility & Monitoring 

 Dashboards 

 Incidents and Alerts 

 Reports 

 Autonomous DEM 

 Best Practices 

 Best Practices Library 

 Experts Corner 

 Solutions Docs from Product Experts 

 PAN-OS 

 11.1 

 Next-Generation Firewall 

 Help 

 Web Interface 

 Panorama 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

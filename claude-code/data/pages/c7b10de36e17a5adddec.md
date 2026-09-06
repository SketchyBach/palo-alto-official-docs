---
url: https://cortex-docs.paloaltonetworks.com/xsiam-data-model-schema/fields/target/host
fetched_at: 2026-09-06T10:57:06Z
source: cortex-platform
---

# xdm.target.host | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Schemas 

 XSIAM Data Model Schema 

 XDM Fields 

 xdm.target 

 xdm.target.host 

 The target host of the activity. 

 Datatype 

 Compound.Host 

 Dataclass 

 Compound 

 Fields 

 xdm.target.host.hostname 

 Description 

 The host name of the target host of the activity. 

 Datatype 

 String 

 Dataclass 

 Scalar 

 xdm.target.host.os_family 

 Description 

 The operating system of the target host of the activity. 

 Datatype 

 XDM_CONST.OS_FAMILY 

 Dataclass 

 Scalar 

 Examples 

 XDM_CONST.OS_FAMILY_WINDOWS, XDM_CONST.OS_FAMILY_MACOS, XDM_CONST.OS_FAMILY_LINUX, XDM_CONST.OS_FAMILY_ANDROID, XDM_CONST.OS_FAMILY_IOS 

 xdm.target.host.os 

 Description 

 The specific operating system of the target host of the activity, including version. 

 Datatype 

 String 

 Dataclass 

 Scalar 

 xdm.target.host.os_distribution 

 Description 

 The operating system distribution of the target host of the activity. 

 Datatype 

 XDM_CONST.OS_FAMILY 

 Dataclass 

 Scalar 

 Examples 

 XDM_CONST.OS_FAMILY_WINDOWS, XDM_CONST.OS_FAMILY_MACOS, XDM_CONST.OS_FAMILY_LINUX, XDM_CONST.OS_FAMILY_ANDROID, XDM_CONST.OS_FAMILY_IOS 

 xdm.target.host.os_release 

 Description 

 The operating system distro release of the target host of the activity. 

 Datatype 

 String 

 Dataclass 

 Scalar 

 Examples 

 jammy 

 xdm.target.host.fqdn 

 Description 

 The fully-qualified domain name (FQDN) of the target host of the activity. 

 Datatype 

 String 

 Dataclass 

 Scalar 

 xdm.target.host.device_category 

 Description 

 The device category of the target host of the activity. 

 Datatype 

 String 

 Dataclass 

 Scalar 

 Examples 

 Infusion System, ATM Machine, Personal Computer, 3D Printer 

 xdm.target.host.device_model 

 Description 

 The device model of the target host of the activity. 

 Datatype 

 String 

 Dataclass 

 Scalar 

 Examples 

 iPad, PA-3200, ThinkPad E14, e2-highmem-8, t2.micro 

 xdm.target.host.device_id 

 Description 

 The unique device ID of the target host of the activity. 

 Datatype 

 String 

 Dataclass 

 Scalar 

 xdm.target.host.ipv4_addresses 

 Description 

 The IPv4 addresses of the target host of the activity. 

 Datatype 

 IPv4 

 Dataclass 

 Array 

 xdm.target.host.ipv6_addresses 

 Description 

 The IPv6 addresses of the target host of the activity. 

 Datatype 

 IPv6 

 Dataclass 

 Array 

 xdm.target.host.ipv4_public_addresses 

 Description 

 The IPv4 public addresses of the target host of the activity. 

 Datatype 

 IPv4 

 Dataclass 

 Array 

 xdm.target.host.ipv6_public_addresses 

 Description 

 The IPv6 public addresses of the target host of the activity. 

 Datatype 

 IPv6 

 Dataclass 

 Array 

 xdm.target.host.mac_addresses 

 Description 

 The MAC addresses of the target host of the activity. 

 Datatype 

 String 

 Dataclass 

 Array 

 xdm.target.host.manufacturer 

 Description 

 The device manufacturer of the target host of the activity. 

 Datatype 

 String 

 Dataclass 

 Scalar 

 xdm.target.host.hardware_uuid 

 Description 

 The unique hardware manufacturing ID of the target host of the activity. 

 Datatype 

 String 

 Dataclass 

 Scalar 

 xdm.target.host.boot_time 

 Description 

 The last known start up time of the target host of the activity. 

 Datatype 

 Timestamp 

 Dataclass 

 Scalar 

 xdm.target.host.image 

 Description 

 The image/runtime name/ID of the target host of the activity. 

 Datatype 

 String 

 Dataclass 

 Scalar 

 Examples 

 ami-19231, python3.9, nodejs14.x 

 xdm.target.host.memory 

 Description 

 The memory capacity size in bytes of the target host of the activity. 

 Datatype 

 Number 

 Dataclass 

 Scalar 

 Unit 

 Bytes 

 xdm.target.host.state 

 Description 

 The state of the target host of the activity. 

 Datatype 

 XDM_CONST.HOST_STATE_TYPE 

 Dataclass 

 Scalar 

 Examples 

 XDM_CONST.HOST_STATE_TYPE_RUNNING, XDM_CONST.HOST_STATE_TYPE_SUSPENDED, XDM_CONST.HOST_STATE_TYPE_STOPPED, XDM_CONST.HOST_STATE_TYPE_TERMINATED 

 xdm.target.host.found_in_vm_image 

 Description 

 Whether a finding present on of the target host of the activity. 

 Datatype 

 Boolean 

 Dataclass 

 Scalar 

 Previous xdm.target 

 Next xdm.target.agent 

 Last updated 1 month ago 

 Was this helpful?

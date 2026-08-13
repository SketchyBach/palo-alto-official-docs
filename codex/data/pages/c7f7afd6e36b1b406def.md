---
url: https://docs.paloaltonetworks.com/compatibility-matrix/reference/vm-series-firewalls/sr-iov-and-dpdk-drivers
fetched_at: 2026-08-13T15:31:46Z
source: palo-alto-main
---

# PacketMMAP and DPDK Drivers on VM-Series Firewalls Clear

PacketMMAP and DPDK Drivers on VM-Series Firewalls 

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

 PacketMMAP and DPDK Drivers on VM-Series Firewalls 

 Updated on 

 Thu Jul 30 22:18:00 PDT 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Compatibility Matrix 

 Reference 

 Updated on 

 Thu Jul 30 22:18:00 PDT 2026 

 Focus 

 Home 

 Compatibility Matrix 

 VM-Series Firewalls 

 PacketMMAP and DPDK Drivers on VM-Series Firewalls 

 Download PDF 

 Compatibility Matrix 

 PacketMMAP and DPDK Drivers on VM-Series Firewalls 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Compatibility Matrix 

 Reference 

 Previous 

 OpenShift Virtualization and Hypervisor Support 

 Next 

 Partner Interoperability for VM-Series Firewalls 

 PacketMMAP and DPDK Drivers on VM-Series Firewalls 

 The Palo Alto Networks list of PacketMMAP and DPDK drivers on VM-Series firewall
 deployments. 

 The VM-Series firewall supports the PacketMMAP and Data
Plane Development Kit (DPDK) drivers listed in the tables below. VM-Series
firewalls use their own drivers to communicate with the drivers
on the host. You should install host-driver versions that are equal to
or later than the driver versions on your VM-Series firewall. 

 To choose host drivers for SR-IOV: 

 KVM —On your KVM host, install a physical function (PF) driver version that is equal to or
 later than the virtual function (VF) native driver version listed below. 

 ESXi —Refer to the VMware Compatibility Matrix and
install the latest driver for the firmware version (PF=i40e, VF=i40evf). 

 For more information about communication between VF drivers on the VM-Series firewall and PF
 drivers on the host (the hypervisor), review the list of PacketMMAP and DPDK Drivers on VM-Series
 Firewalls in the VM-Series deployment guide. 

 SR-IOV Access Mode 

 PacketMMAP Driver Versions 

 DPDK Driver Versions 

 SR-IOV Access Mode 

 VM-Series firewalls support SR-IOV Access Mode on KVM and ESXi
 hypervisors. To enable single root I/O virtualization (SR-IOV) access mode, you can
 include the bootstrap parameter file:
 plugin-op-commands=sriov-access-mode-on in the
 initcfg.txt 

 ESXi —Requires PAN-OS 9.1.5 or a later PAN-OS 9.1 version or PAN-OS
 10.1 or a later PAN-OS version with VM-Series plugin 2.0.5 or a later plugin
 version. 

 OCI —Requires PAN-OS 11.2.14 or 12.2.0 or later. 

 KVM —Requires PAN-OS 9.1.5 or a later PAN-OS version with VM-Series plugin 2.0.1 or a later
 plugin version. 

 Intel Ice driver is supported in KVM environments in PAN-OS 10.2.11 or later. 

 Ice Driver Versions 

 The following are the minimum required driver and firmware versions: 

 PA-VM Version PA-VM DPDK Version Ice Kernel Driver VErsion NVM Version Firmware DPD OS Package DPD Comms Package 

 12.2.x 25.11 2.3.14 4.90 1.7.9.1 1.3.50.0 1.3.58.0 

 12.1.x 23.11 1.13.7 4.40 1.7.3.13 1.3.35.0 1.3.45.0 

 11.2.x 22.11 1.11.14 4.20 1.7.2.4 1.3.30.0 1.3.40.0 

 11.1.x 22.11 1.11.14 4.20 1.7.2.4 1.3.30.0 1.3.40.0 

 10.2.x 20.11 1.4.11 2.40/2.42 1.5.4.5 1.3.24.0 1.3.28.0 

 PacketMMAP Driver Versions 

 VM-Series firewalls use their virtual function (VF)
drivers to communicate with the host's physical function (PF) drivers during
SR-IOV. For example, i40e is a PF driver and i40evf is a VF driver. 

 PAN-OS Version 

 Driver Filename 

 ARM Driver Filename 

 Virtual Firewall Native Drivers (Linux Version) 

 Comment 

 11.2 

 bnx2x 

 mlx5 

 1.713.36-0 

 i40e 

 i40e 

 2.14.13 

 iavf 

 4.0.2 

 igb 

 5.6.0 

 igbvf 

 2.4.0 

 ixgbe 

 5.1.0 

 The minimum version for multiple queues is 4.2.5 

 ixgbevf 

 4.1.0 

 mlnx-en 

 4.9 

 11.1 

 bnx2x 

 mlx5 

 1.713.36-0 

 i40e 

 i40e 

 2.14.13 

 iavf 

 4.0.2 

 igb 

 5.6.0 

 igbvf 

 2.4.0 

 ixgbe 

 5.1.0 

 The minimum version for multiple queues is 4.2.5 

 ixgbevf 

 4.1.0 

 mlnx-en 

 4.9 

 11.0 

 bnx2x 

 1.713.36-0 

 i40e 

 2.14.13 

 iavf 

 4.0.2 

 igb 

 5.6.0 

 igbvf 

 2.4.0 

 ixgbe 

 5.1.0 

 The minimum version for multiple queues is 4.2.5 

 ixgbevf 

 4.1.0 

 mlnx-en 

 4.9 

 10.2 

 bnx2x 

 1.712.30-0 

 i40e 

 2.13.10 

 iavf 

 3.2.3 

 i40evf renamed to iavf; still compatible with i40en host
 driver. 

 igb 

 5.4.0 

 igbvf 

 2.4.0 

 ixgbe 

 5.1.0 

 The minimum version for multiple queues is 4.2.5 

 ixgbevf 

 4.1.0 

 mlnx-en 

 4.9 

 10.1 

 bnx2x 

 1.712.30-0 

 i40e 

 2.13.10 

 iavf 

 3.2.3 

 i40evf renamed to iavf; still compatible with i40en host
 driver. 

 igb 

 5.4.0 

 igbvf 

 2.4.0 

 ixgbe 

 5.1.0 

 The minimum version for multiple queues is 4.2.5 

 ixgbevf 

 4.1.0 

 mlnx-en 

 4.9 

 9.1 

 bnx2x 

 1.713.36-0 

 i40e 

 2.3.2 

 i40evf 

 3.2.2 

 Compatible with i40en host driver. 

 igb 

 5.4.0 

 igbvf 

 2.4.0 

 ixgbe 

 5.1.0 

 The minimum version for multiple queues is 4.2.5 

 ixgbevf 

 4.1.0 

 DPDK Driver Versions 

 When the firewall is in DPDK mode, it uses DPDK drivers.
Please check the official DPDK release notes for more
information. 

 By default DPDK is enabled on VM-Series firewalls as stated below.
If the VM-Series firewall detects an unsupported driver, the firewall reverts
to PacketMMap mode. 

 Hypervisor 

 Virtual Driver 

 NIC Drivers 

 KVM 

 virtio 

 ixgbe, ixgbevf, i40e, i40evf, and mlnx-en (PAN-OS 10.1 and later) 

 ESXi 

 VMXNET3 

 ixgbe, ixgbevf, i40e, i40evf 

 ARM KVM 

 virtio 

 I40e and mlx5 (PAN_OS 11.1 and later) 

 See VM-Series for KVM and VM-Series for VMWare vSphere
Hypervisor (ESXi) for PAN-OS versions that support DPDK,
DPDK with SR-IOV, or DPDK with Virtio. 

 PAN-OS Version 

 DPDK Version 

 Comment 

 12.2 

 25.11 

 12.1 

 23.11.0 

 11.2 

 22.11.1 

 11.1 

 22.11.1 

 11.0 

 20.11.1 

 10.2 

 20.11.1 

 10.1 

 19.11.3 

 9.1 

 18.11 

 Previous 

 OpenShift Virtualization and Hypervisor Support 

 Next 

 Partner Interoperability for VM-Series Firewalls 

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

 Prisma SASE Multitenant Platform 

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

 IoT Security 

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

 10.1 

 11.0 

 10.2 

 11.1 

 11.2 

 Reference 

 VM-Series 

 9.1 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

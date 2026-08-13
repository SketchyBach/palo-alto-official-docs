---
url: https://docs.paloaltonetworks.com/vm-series/getting-started/vm-series-performance
fetched_at: 2026-08-13T17:42:28Z
source: palo-alto-main
---

# VM-Series Performance Clear

VM-Series Performance 

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

 VM-Series Performance 

 Updated on 

 Mon Jul 06 21:45:23 PDT 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 VM-Series Firewall Docs 

 Activation & Onboarding 

 Getting Started 

 Upgrade 

 Deployment 

 Select a Document 

 Public Cloud 

 Private Cloud 

 Updated on 

 Mon Jul 06 21:45:23 PDT 2026 

 Focus 

 Home 

 VM-Series 

 VM-Series Performance 

 Download PDF 

 VM-Series 

 VM-Series Performance 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 VM-Series Firewall Docs 

 Activation & Onboarding 

 Getting Started 

 Upgrade 

 Deployment 

 Select a Document 

 Public Cloud 

 Private Cloud 

 Previous 

 VM-Series Firewall Deployments 

 Next 

 VM-Series on Amazon Web Services Performance and Capacity 

 VM-Series Performance 

 VM-Series firewall performance. 

 Where Can I Use This? What Do I Need? 

 VM-Series deployment 

 VM-Series 10.x or above 

 Panorama running PAN-OS 10.1.x or above versions 

 Customer Support Portal (CSP) account with one of the
 following user roles: 
 Superuser, Standard User, Limited User, Threat
 Researcher, AutoFocus Trial Role, Group superuser,
 Group Standard User, Group Limited User, Group
 Threat Researcher, Authorized Support Center (ASC)
 User, and ASC Full Service User. 

 Superuser access to the VM-Series 
 firewall 

 For a complete listing of all VM-Series firewall features and capacities, refer to
 the firewall comparison tool . Use this
 information for VM-Series performance characteristics. 

 PacketMMAP and DPDK Driver Support 

 Single-root input/output virtualization (SR-IOV) relies on
 communication between virtual function (VF) drivers on the VM-Series firewall, and physical function (PF) drivers on the
 host (the hypervisor). The host uses PF drivers to talk to its physical NICs,
 and the VM-Series firewall uses VF drivers to talk to the PF drivers. 

 The following diagram is a simple visualization of that concept. 

 SR-IOV 

 Why use SR-IOV? SR-IOV is a packet acceleration technology that allows a virtual
 machine to directly access packets from the NIC. In contrast, when using a
 virtual switch, the host processes the packets, send the packets through a
 virtual switch, and then the virtual machine receives its packets. 

 In the Compatibility Matrix, PacketMMAP Driver Versions lists both
 the host version and the native driver version on the VM-Series 
 firewall. For example, i40e on the host, and on the firewall, i40e (for
 PCI-passthrough) and i40evf (for SR-IOV). 

 For SR-IOV, let's consider a NIC that uses the i40e PF driver. The host
 communicates with the NIC via the i40e driver. The VM-Series firewall can use
 its VF driver (i40evf) to directly communicate with the host's PF driver. This
 allows VM-Series firewall direct access, which improves packet
 processing speed. To ensure compatibility, install a host PF driver version that
 is later than the native PF driver version. 

 PCI-Passthrough 

 Why does VM-Series firewall have native PF drivers? As mentioned
 in Options for Attaching VM-Series on the
 Network , when using PCI-passthrough, the NIC is reserved for the VM-Series firewall, so the host (or other guests on the host)
 cannot access the NIC. In a PCI-passthrough configuration, the VM-Series firewall uses its native PF driver to communicate
 directly with the host NIC. 

 Refer to the PacketMMAP Driver Versions list to
 determine which PF driver version to install on the host. Install a PF version
 that is higher than VM-Series firewall native PF driver. 

 Refer to Enable SR-IOV on ESXi and Enable SR-IOV on KVM for
 PCI-Passthrough. 

 DPDK 

 PAN-OS has two packet processing modes—DPDK (default) and MMAP—and
 each mode has a corresponding native driver on the VM-Series 
 firewall. For example, if the firewall is in DPDK mode, the firewall uses the
 DPDK i40evf driver version to communicate with the host's i40e driver (when
 using SR-IOV). Alternatively, when the firewall is Packet MMAP, it will use a
 different i40evf driver version to communicate with the host's i40e driver. 

 You can enable DPDK on the host (the hypervisor), or on the guest
 (the VM-Series firewall). Enabling both yields the best results. 

 Compiling OVS with DPDK is part of enabling DPDK on the host. 
 Refer to
 Configure OVS and DPDK on the
 Host . 

 VM-Series DPDK enables the native DPDK driver on the
 VM-Series firewall, so DPDK does not need to be enabled on the host, but
 it is recommended for best performance. 

 Enable NUMA Performance Optimization on the VM-Series 

 To improve performance of your VM-Series firewalls, you can enable
 non-uniform memory access (NUMA) performance optimization. When NUMA
 performance optimization is enabled, the VM-Series firewall dataplane uses
 vCPUs attached to NUMA node 0. The VM-Series firewall
 dataplane uses vCPUs belonging to NUMA node 0 only. The VM-Series management plane uses core 0 and the remaining
 vCPUs on NUMA node 0 can be used by the VM-Series dataplane. This feature
 requires PAN-OS 10.1.1 or later and VM-Series plugin 2.1.1 or later. 

 NUMA performance optimization is disabled by default in PAN-OS 10.1. 

 If you have a device that contains 64 cores across two NUMA nodes, when NUMA
 performance optimization is not enabled, the dataplane vCPUs used by the VM-Series firewall might be on different nodes, which impacts
 performance. For example, if your system is organized shown in the following
 example and you deploy a VM-Series firewall with 32 total
 cores with 24 dataplane cores. 

 Without NUMA performance optimization, the VM-Series firewall
 uses cores 1 through 15 on Node 0 and 16 to 24 on Node 1 because it assigns
 cores in numerical order, regardless of the node location. With NUMA
 optimization enabled, the VM-Series only uses cores on Node
 0, in this case 1 through 15 and 33 through 39, regardless of the numerical
 order. Any cores not used by the dataplane are assigned to the management
 plane. 

 With NUMA performance optimization with custom dataplane core settings, the
 NUMA settings takes precedence. For example, for a 64 CPU VM with NUMA
 performance optimization enabled and 47 dataplane core setting, the NUMA
 settings take precedence. 

 If the number of cores assigned to your VM-Series firewall
 exceeds the number of vCPUs on Node 0, the VM-Series uses
 all the cores on Node 0 but does not use any cores from other nodes. For
 example, if you assign 30 cores to your VM-Series firewall but Node 0
 has only 24 cores, the VM-Series firewall will only use
 the 24 cores on Node 0 for the dataplane. 

 Log in to the VM-Series CLI. 

 Execute the following command. 

 request plugins vm_series numa-perf-optimize enable
 on 

 Previous NUMA performance optimization:
 None 

 Requested NUMA performance optimization:
 Enabled 

 Please reboot the PA-VM. 

 After the reboot is complete, log in to the VM-Series 
 CLI and verify that NUMA optimization was enabled. 

 show plugins vm_series numa-perf-optimize 

 NUMA performance optimization:
 Enabled 

 Verify the number of dataplane cores. 

 show plugins vm_series dp-cores 

 Current DP cores:31 configured custom DP cores: 47
 (Current total cores: 64) 

 To disable NUMA performance optimization, use the following command.
 This command requires you to reboot the VM-Series firewall. 

 request plugins vm_series numa-perf-optimize enable
 off 

 Enable ZRAM on the VM-Series Firewall 

 If your VM-Series firewall experiences low or out-of memory
 conditions, you can enable ZRAM to improve memory usage. ZRAM, also called
 compcache (compressed cache), is a Linux kernel module for creating a
 compressed block device in RAM. When enabled, ZRAM is used as swap disk and
 allows for faster I/O of swap because it resides in the RAM. 

 Complete the following steps to enable ZRAM. 

 Log in to the VM-Series CLI. 

 Find the total memory on the VM by using the following CLI
 command. 

 grep pattern "MiB Mem :" mp-log
 mp-monitor.log 

 KiB Mem : 9202656 total, 566504 free, 3475840 used, 5160312 buff/cache
KiB Mem : 9202656 total, 497112 free, 3481944 used, 5223600 buff/cache
KiB Mem : 9202656 total, 511744 free, 3466768 used, 5224144 buff/cache
KiB Mem : 9202656 total, 511668 free, 3466340 used, 5224648 buff/cache
KiB Mem : 9202656 total, 512124 free, 3465700 used, 5224832 buff/cache
KiB Mem : 9202656 total, 511436 free, 3465976 used, 5225244 buff/cache
KiB Mem : 9202656 total, 510984 free, 3465944 used, 5225728 buff/cache 

 Convert the above total memory from KB to MB. For example: 

 9202656 / 1024 = 8987 MB 

 Take note of the total memory value in MB. You will need this value
 in the next step. 

 Enable ZRAM using the following two CLI commands. 

 debug software kernelcfg zram-swap enable 

 debug software kernelcfg zram-swap modify
 host-mem-threshold <total-memory-in-MB> 

 Reboot the VM-Series firewall. 

 Verify that ZRAM is enabled. 

 debug software kernelcfg zram-swap show
 run-time 

 debug software kernelcfg zram-swap show run-time

ZRAM MODULE: LOADED
ZRAM SWAP: ON
ZRAM DEVICE NUM: 1
ZRAM MEM_LIMIT(MB): 1350
ZRAM DISK_SIZE(MB): 4000
ZRAM ORI_DATA_SIZE(B): 22163456
ZRAM COMP_DATA_SIZE(B): 1957437
ZRAM MEM_USED_TOTAL(B): 2465792 

 You can verify ZRAM status in the
 pan_kernelcfg.log . 

 INFO: Zram swap is turned on now
INFO: Done with ZRAM mem_limit configuration 

 Previous 

 VM-Series Firewall Deployments 

 Next 

 VM-Series on Amazon Web Services Performance and Capacity 

 On This Page 

 Activation and Onboarding 

 Strata Cloud Manager 

 Next-Generation Firewalls 

 Firewalls 

 PAN-OS 

 PAN-OS SD-WAN 

 VM-Series 

 Plugins 

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

 Resources 

 All Release Notes 

 Compatibility Matrix 

 Experts Corner 

 Network Security 

 VM-Series 

 Getting Started 

 Licensing 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

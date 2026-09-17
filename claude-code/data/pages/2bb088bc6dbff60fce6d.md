---
url: https://cortex-docs.paloaltonetworks.com/cortex-xdr-agent/8.9/cortex-xdr-agent-for-linux/cortex-xdr-agent-for-linux-requirements
fetched_at: 2026-09-16T09:13:58Z
source: cortex-platform
---

# Cortex XDR Agent for Linux Requirements | 8.9 (EoL) | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XDR Agent 

 Cortex XDR Agent Documentation 

 8.9 (EoL) 

 Cortex XDR Agent for Linux 

 Cortex XDR agent 8.9 EoL 

 Cortex XDR Agent for Linux Requirements 

 Linux endpoints must meet the following requirements to install the Cortex XDR agent. 

 Requirement 

 Minimum specification 

 Processor 

 Processor 2.3 GHz dual-core processor 

 RAM 

 4GB; 8GB recommended 

 Hard disk space 

 10 GB (available for the /opt/traps directory) 

 Architecture 

 x86_64 (x86 64bit) For aarch64 (ARM 64 bit) see Cortex XDR Agent for Linux Requirements for details. 

 Operating system versions 

 See the Cortex XDR Compatibility Matrix . 

 Kernel version 

 Kernel Mode On Linux endpoints, to perform malware analysis of Executable and Linkable Format (ELF) files and collect data for endpoint detection and response (EDR) and behavioral threat analysis, the Cortex XDR agent requires one of the Linux Kernels that are listed in supported Kernel Module Versions . If you deploy the Cortex XDR agent on a Linux server that is not running one of the kernel versions required for these additional protection capabilities, the agent will operate in asynchronous mode. User Space Mode User Space operation mode is supported from Cortex XDR agent version 7.7 User space operation mode requires Kubernetes node to run one of the supported operation systems with Kernel version 5.0 or later. 

 Software packages 

 The following software packages are required to be installed on your endpoint, depending on the operating system. 

 Verify that you have standard Unix programs installed. 

 ca-certificates 

 All Distributions require openssl 1.0.0 or a later release. 

 In addition, SLES 11 requires openssl-certs 

 In addition, SLES 12 and 15 require ca-certificates 

 glibc—Required for exploit protection of containerized processes using the ROP Mitigation and Brute Force Protection modules. If glibc is not installed, these modules are disabled but all other exploit and malware protection functionality work as expected. 

 CentOS 6.10—Enable the dynamic CA instead of the legacy CA: 1. Enable the dynamic CA configuration: update-ca-trust force-enable 2. Import the certificates: cp XDR-certificate.crt /etc/pki/ca-trust/source/anchors/. 3. Rebuild the certificate database: update-ca-trust extract 

 For systems with SELinux enabled in enforcing or permissive mode, see the Required Packages table below. 

 Networking 

 Allow communication on the TCP port from the Cortex XDR agent to the server (the default is port 443). 

 Allow your Cortex management console and Cortex XDR agent to communicate with external and internal resources required for enforcing endpoint protection. For more information, see Enable Access to Required PANW Resources in the applicable Cortex product documentation. 

 Required packages 

 Operating System 

 Packages 

 RHEL 6, CentOS 6, CentOS Stream 6, Oracle Linux 6, AlmaLinux 6, Rocky Linux 6 

 policycoreutils-python 

 RHEL 7, CentOS 7, CentOS Stream 7, Oracle Linux 7, AlmaLinux 7, Rocky Linux 7 

 policycoreutils-python selinux-policy-devel selinux-policy-targeted 

 RHEL 8/9, CentOS 8/9, CentOS Stream 8/9, Oracle Linux 8/9, AlmaLinux 8/9, Rocky Linux 8/9 

 policycoreutils-python-utils selinux-policy-devel selinux-policy-targeted 

 Amazon Linux 1 

 policycoreutils-python, selinux-policy 

 Amazon Linux 2 

 policycoreutils-python, selinux-policy-devel 

 Amazon Linux 2023 

 policycoreutils-python-utils, selinux-policy-devel 

 TencentOS 

 policycoreutils-python-utils, selinux-policy-devel 

 Fedora Server 

 policycoreutils-python-utils, selinux-policy-devel 

 SLES and openSUSE 

 policycoreutils-python, selinux-policy-devel 

 Mariner 

 policycoreutils-python-utils, selinux-policy-devel 

 Previous Cortex XDR supported Kernel Module versions by distribution 

 Next Install the Cortex XDR agent for Linux 

 Last updated 13 days ago 

 Was this helpful?

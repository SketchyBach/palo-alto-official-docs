---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsoar-8-on-prem/8.12/configure-cortex-xsoar/engines/install-an-engine/podman
fetched_at: 2026-09-16T08:54:00Z
source: cortex-platform
---

# Podman | 8.12 | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSOAR 8 

 Cortex XSOAR 8 On-prem Documentation 

 8.12 

 Configure Cortex XSOAR 

 Engines 

 Install an engine 

 Cortex XSOAR 8.12 On-prem 

 Podman 

 In Cortex XSOAR 8.12 On-prem, run Podman containers on RHEL 8 or later. 

 Podman is a daemonless container engine for developing, managing, and running OCI Containers on the Linux System. Containers can either be run as root or in rootless mode. 

 If you use the Shell installer to install an engine, Cortex XSOAR automatically detects the container management type based on the operating system. For example, if your operating system is running RHEL v8 and higher, Cortex XSOAR installs Podman packages and configures the operating system to enable Podman in rootless mode. 

 Note 

 When upgrading an engine, the engine keeps the previously used container management type (regardless of distribution version). 

 If using PowerShell integrations, you may need to configure the default SELinux policy as Podman can affect processes which mmap to /dev/zero . 

 Docker hardening guidelines 

 Docker hardening guidelines can be applied to Podman, with the exception of Limit Available Memory, Limit Available CPU, and Limit PIDS. 

 Previous Docker hardening guide 

 Next Change container storage directory 

 Last updated 1 month ago 

 Was this helpful?

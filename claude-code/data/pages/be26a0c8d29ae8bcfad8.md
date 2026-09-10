---
url: https://cortex-docs.paloaltonetworks.com/xsoar-6-administrator-guide/6.12/onboard-cortex-xsoar/podman/podman-overview
fetched_at: 2026-09-06T10:47:05Z
source: cortex-platform
---

# Podman Overview | 6.12 (EoL) | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSOAR 6 

 Cortex XSOAR 6 Administrator Guides 

 6.12 (EoL) 

 Onboard Cortex XSOAR 

 Podman 

 Cortex XSOAR 6.12 EoL 

 Podman Overview 

 Understand Podman containers for Cortex XSOAR 6.12 deployments. 

 Cortex XSOAR supports both Docker and Podman as the container management tool. Podman is a daemonless container engine for developing, managing, and running OCI containers on the Linux System. Containers can either be run as root or in rootless mode. 

 When installing a server or engine, Cortex XSOAR automatically detects the container management type based on the operating system. For example, if your operating system is running RHEL v8 and higher, Cortex XSOAR installs Podman packages and configures the operating system to enable Podman in rootless mode. 

 Note 

 When upgrading a server or engine, the server or engine keeps the previously used container management type (regardless of distribution version). To migrate an existing server or engine to Podman, see Migrate From Docker to Podman . 

 If using PowerShell integrations, you may need to configure the default SELinux policy as Podman can affect processes which mmap to /dev/zero . 

 Docker hardening guidelines can be applied to Podman, with the exception of Limit Available Memory, Limit Available CPU, and Limit PIDS. 

 Previous Podman 

 Next Change container storage directory 

 Last updated 1 month ago 

 Was this helpful?

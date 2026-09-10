---
url: https://cortex-docs.paloaltonetworks.com/xdr-agent-release-notes/9.2/release-information/known-issues
fetched_at: 2026-09-06T10:53:16Z
source: cortex-platform
---

# Cortex XDR agent known limitations | 9.2 | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Release Notes 

 Cortex XDR Agent 

 Cortex XDR Agent 9.x 

 9.2 

 Cortex XDR Agent 9.2 Release Information 

 Cortex XDR agent known limitations 

 The following table describes the known limitations in the Cortex XDR agent 9.2. 

 ISSUE 

 DESCRIPTION 

 Windows on ARM 

 The Cortex XDR agent 9.2 on ARM architecture has the following limitations: 

 Behavioral Threat Protection: Not fully supported 

 Exploit Protection: Not supported 

 File Examination: JScript, VBScript, and PowerShell file examination not fully supported 

 GKE Autopilot 

 When using GKE Autopilot, if there is a timing issue encountered during Cortex XDR agent installation (GKE Warden constraints violations), the YAML installation command should be repeated. 

 Custer-level scoping 

 Cluster name is currently not supported in Oracle Cloud, GCP, Azure and Openshift (any cloud). For these operating systems, use the node name instead. 

 Live Terminal support 

 Live Terminal is currently not supported for pure IPv6 endpoints, on all platforms. 

 Live Terminal will not be supported with GKE Autopilot. 

 Device control 

 When enabling Device Control protection for the first time, some devices that are already connected (or paired in case of Bluetooth) to the machine will not be immediately affected by the change. 

 The profile change will affect the connected device after one of the following occurs: 

 Disconnect and reconnect the device 

 A computer restart 

 In case of Bluetooth: Toggle the Bluetooth off and on, or manually unpair the device. 

 Linux Kubernetes Platform, TalOS 

 When using TalOS, note the following: 

 Collect insights and compliance collection are disabled. 

 Live Terminal startup location is inside the agent pod and not on the host. 

 All the server and user script execution initial working directories are inside the agent pod. 

 VA scanning engine 

 When using the Vulnerability Assessment engine, note the following issues: 

 In some cases, the reported application version may be missing or incomplete. 

 Applications installed for specific users will not be scanned. 

 During a scan, memory spikes may occur. 

 SELinux 

 When installing Cortex XDR agent on a system with SELinux enabled, injection is supported only to SELinux unconfined processes. 

 SLES 15 

 Installing Cortex XDR agent on SLES (SUSE Linux Enterprise) 15 with SELinux enabled is unsupported. 

 CPATR-18568 

 [Linux] On some occasions, when a container is a short-lived container (exits within a short period of time) retrieval of the container information is not guaranteed. 

 Previous Addressed issues in Cortex XDR agent 9.2 

 Last updated 1 month ago 

 Was this helpful?

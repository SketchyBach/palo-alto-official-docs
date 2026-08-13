---
url: https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-admin/policy/cli-commands-for-dynamic-ip-addresses-and-tags
fetched_at: 2026-08-13T17:09:53Z
source: palo-alto-main
---

# CLI Commands for Dynamic IP Addresses and Tags Clear

CLI Commands for Dynamic IP Addresses and Tags 

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

 CLI Commands for Dynamic IP Addresses and Tags 

 Updated on 

 Mon Aug 11 16:31:23 PDT 2025 

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

 Updated on 

 Mon Aug 11 16:31:23 PDT 2025 

 Focus 

 Home 

 PAN-OS 

 Policy 

 CLI Commands for Dynamic IP Addresses and Tags 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 한국어 (Korean) 

 CLI Commands for Dynamic IP Addresses and Tags 

 Table of Contents 

 Filter

 Previous 

 Use Dynamic Address Groups in Policy 

 Next 

 Enforce Policy on Endpoints and Users Behind an Upstream Device 

 CLI Commands for Dynamic IP Addresses and Tags 

 The Command Line Interface on the firewall and Panorama
give you a detailed view into the different sources from which tags
and IP addresses are dynamically registered. It also allows you
to audit registered and unregistered tags. The following examples
illustrate the capabilities in the CLI. 

 Example 

 CLI Command 

 View all registered IP addresses that match
the tag, state.poweredOn or that are
not tagged as vSwitch0 . 

 show log iptag tag_name equal state.poweredOn 
 show log iptag tag_name not-equal switch.vSwitch0 

 View all dynamically registered IP addresses
that were sourced by VM Information Source with name vmware1 and
tagged as poweredOn . 

 show vm-monitor source source-name vmware1 tag state.poweredOn registered-ip all 
registered IP Tags 
---------------------- --------------- 
fe80::20c:29ff:fe69:2f76  "state.poweredOn" 
10.1.22.100               "state.poweredOn" 
2001:1890:12f2:11:20c:29ff:fe69:2f76"state.poweredOn" 
fe80::20c:29ff:fe69:2f80 "state.poweredOn" 
192.168.1.102            "state.poweredOn" 
10.1.22.105              "state.poweredOn" 
2001:1890:12f2:11:2cf8:77a9:5435:c0d"state.poweredOn" 
fe80::2cf8:77a9:5435:c0d "state.poweredOn" 

 Clear all IP addresses and tags learned
from a specific VM Monitoring source without disconnecting the source. 

 debug vm-monitor clear source-name <name> 

 Display IP addresses registered from all
sources. 

 show object registered-ip all 

 Display the count for IP addresses registered
from all sources. 

 show object registered-ip all option count 

 Clear IP addresses registered from all sources 

 debug object registered-ip clear all 

 Add or delete tags for a given IP address
that was registered using the XML API. 

 debug object registered-ip test [<register/unregister>] <ip/netmask><tag> 

 View all tags registered from a specific
information source. 

 show vm-monitor source source-name vmware1 tag all 
vlanId.4095 
vswitch.vSwitch1 
host-ip.10.1.5.22 
portgroup.TOBEUSED 
hostname.panserver22 
portgroup.VM Network 2 
datacenter.ha-datacenter 
vlanId.0 
state.poweredOn 
vswitch.vSwitch0 
vmname.Ubuntu22-100 
vmname.win2k8-22-105 
resource-pool.Resources 
vswitch.vSwitch2 
guestos.Ubuntu Linux 32-bit 
guestos.Microsoft Windows Server 2008 32-bit 
annotation. 
version.vmx-08 
portgroup.VM Network 
vm-info-source.vmware1 
uuid.564d362c-11cd-b27f-271f-c361604dfad7 
uuid.564dd337-677a-eb8d-47db-293bd6692f76 
Total: 22 

 View all tags registered from a specific
data source, for example from the VM Monitoring Agent on the firewall,
the XML API, Windows User-ID Agent or the CLI. 

 To view tags registered from the
CLI: 

 show log iptag datasource_type equal unknown 

 To view tags registered from the XML API: 

 show log iptag datasource_type equal xml-api 

 To view tags registered from VM Information sources: 

 show log iptag datasource_type equal vm-monitor 

 To view tags registered from the Windows User-ID agent: 

 show log iptag datasource_type equal xml-api datasource_subtype equal user-id-agent 

 View all tags that are registered for a
specific IP address (across all sources). 

 debug object registered-ip show tag-source ip ip_address tag all 

 Previous 

 Use Dynamic Address Groups in Policy 

 Next 

 Enforce Policy on Endpoints and Users Behind an Upstream Device 

 On This Page 

 PAN-OS 

 Next-Generation Firewall 

 Policy 

 11.1 

 Network Security 

 11.1 & Later 

 Administration 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

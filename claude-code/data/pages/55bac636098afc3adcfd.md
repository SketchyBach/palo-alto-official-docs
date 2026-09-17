---
url: https://docs.paloaltonetworks.com/pan-os/10-1/pan-os-cli-quick-start/use-the-cli/cli-jump-start
fetched_at: 2026-09-16T07:34:58Z
source: palo-alto-main
---

# CLI Jump Start Clear

Updated on 

 Thu Aug 28 22:57:13 PDT 2025 

 Focus 

 Home 

 Next-Generation Firewall 

 Use
the CLI 

 CLI Jump Start 

 Download PDF 

 Next-Generation Firewall 

 CLI Jump Start 

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

 Use Secure Copy to Import and Export Files 

 Next 

 CLI Cheat Sheet: Device Management 

 CLI Jump Start 

 Use this quick reference to see the most common commands
you will need to being managing your next-gen firewall using the
command-line interface (CLI). 

 Where Can I Use This? What Do I Need? 

 NGFW (Managed by PAN-OS or Panorama) 

 No prerequisites needed 

 The following table provides quick start information
for configuring the features of Palo Alto Networks devices from
the CLI. Where applicable for firewalls with multiple virtual systems
(vsys), the table also shows the location to configure shared settings
and vsys-specific settings. 

 To configure... 

 Start here... 

 MGT interface 

 # set deviceconfig system ip-address 

 admin password 

 # set mgt-config users admin password 

 DNS 

 # set deviceconfig system dns-setting servers 

 NTP 

 # set deviceconfig system ntp-servers 

 Interfaces 

 # set network interface 

 System settings 

 # set deviceconfig system 

 Zones 

 # set zone <name> 
# set vsys <name> zone <name> 

 Security Profiles 

 HIP Objects/Profiles 

 URL
Filtering Profiles 

 WildFire Analysis Profiles 

 # set profiles 
# set vsys <name> profiles 
# set shared profiles 

 Server Profiles 

 # set server-profile 
# set vsys <name> server-profile 
# set shared server-profile 

 Authentication Profiles 

 # set authentication-profile 
# set vsys <name> authentication-profile 
# set shared authentication-profile 

 Certificate Profiles 

 # set certificate-profile 
# set vsys <name> certificate-profile 
# set shared certificate-profile 

 Policy 

 # set rulebase 
# set vsys vsys1 rulebase 

 Log Quotas 

 # set deviceconfig setting management quota-settings 

 User-ID 

 # set user-id-agent 
# set vsys <name> user-id-agent 
# set user-id-collector 
# set vsys <name> user-id-collector 

 HA 

 # set deviceconfig high-availability 

 AutoFocus Settings 

 # set deviceconfig setting autofocus 

 WildFire Settings 

 # set deviceconfig setting wildfire 

 Panorama 

 # set deviceconfig system panorama-server 

 Restart 

 > request restart system 

 Previous 

 Use Secure Copy to Import and Export Files 

 Next 

 CLI Cheat Sheet: Device Management

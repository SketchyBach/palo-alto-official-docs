---
url: https://docs.paloaltonetworks.com/content/techdocs/en_US/pan-os/10-0/pan-os-cli-quick-start/use-the-cli/modify-the-configuration.html
fetched_at: 2026-09-16T10:42:34Z
source: palo-alto-main
---

# Modify the Configuration Clear

Updated on 

 Mon Aug 28 18:33:05 PDT 2023 

 Focus 

 Home 

 PAN-OS 

 PAN-OS CLI Quick Start 

 Use
the CLI 

 Modify the Configuration 

 Download PDF 

 PAN-OS CLI Quick Start 

 Modify the Configuration 

 Table of Contents 

 Filter

 Version 

 10.0 (EoL) 

 11.1 & Later 

 10.2 

 10.1 

 10.0 (EoL) 

 9.1 (EoL) 

 Expand all | Collapse all 

 Get Started with the CLI 

 Access the CLI 

 Verify SSH Connection to Firewall 

 Refresh SSH Keys and Configure Key Options for Management Interface Connection 

 Give Administrators Access to the CLI 

 Administrative Privileges 

 Set Up a Firewall Administrative Account and Assign CLI Privileges 

 Set Up a Panorama Administrative Account and Assign CLI Privileges 

 Change CLI Modes 

 Navigate the CLI 

 Find a Command 

 View the Entire Command Hierarchy 

 Find a Specific Command Using a Keyword Search 

 Get Help on Command Syntax 

 Get Help on a Command 

 Interpret the Command Help 

 Customize the CLI 

 Use the CLI 

 View Settings and Statistics 

 Modify the Configuration 

 Commit Configuration Changes 

 Test the Configuration 

 Test the Authentication Configuration 

 Test Policy Matches 

 Load Configurations 

 Load Configuration Settings from a Text File 

 Load a Partial Configuration 

 Xpath Location Formats Determined by Device Configuration 

 Load a Partial Configuration into Another Configuration Using Xpath Values 

 Use Secure Copy to Import and Export Files 

 Export a Saved Configuration from One Firewall and Import it into Another 

 Export and Import a Complete Log Database (logdb) 

 CLI Jump Start 

 CLI Cheat Sheets 

 CLI Cheat Sheet: Device Management 

 CLI Cheat Sheet: User-ID 

 CLI Cheat Sheet: HA 

 CLI Cheat Sheet: Networking 

 CLI Cheat Sheet: VSYS 

 CLI Cheat Sheet: Panorama 

 CLI Changes in PAN-OS 10.0 

 Load Commands Changed in PAN-OS 10.0 

 Load Commands Removed in PAN-OS 10.0 

 Revert Commands Changed in PANOS-10.0 

 Set Commands Introduced in PAN-OS 10.0 

 Set Commands Changed in PAN-OS 10.0 

 Set Commands Removed in PAN-OS 10.0 

 Show Commands Introduced in PAN-OS 10.0 

 Show Commands Removed in PAN-OS 10.0 

 End-of-Life (EoL)

 Modify the Configuration 

 You can also modify the device configuration
from the CLI using the set , delete ,
and edit commands (if your administrative
role has a Privilege
Level that allows you to write to the configuration). In
most cases you must be in Configure mode to modify the configuration. 

 To change the value of a setting, use
a set command. For example, to configure
an NTP server, you would enter the complete hierarchy to the NTP
server setting followed by the value you want to set: 

 admin@PA-3060# set deviceconfig system ntp-servers primary-ntp-server ntp-server-address pool.ntp.org 

 To target a command to a specific virtual system
(vsys), enter the following operational mode command: set system setting target-vsys <vsys-name> .
To go back to issuing commands that apply to the firewall instead
of the targeted vsys, use set system target-vsys none . 

 To change to a different location in the configuration
hierarchy and/or to modify a setting, use the edit command.
The edit commands are very similar to the set commands,
except that when you enter an edit command, you
switch context to the corresponding node in the command hierarchy.
This can be useful if you need to enter several commands in a node
that is nested far down in the command hierarchy. For example, if
you want to configure all of the NTP server settings, instead of
entering the full command syntax each time using the set command,
you could use the edit command to move to
the ntp-servers node as follows: 

 [edit] 
admin@PA-3060# edit deviceconfig system ntp-servers 
[edit deviceconfig system ntp-servers] 
admin@PA-3060# 

 Notice that when you enter the command,
your new location in the command hierarchy is displayed. You can
now use the set command to configure the
NTP server settings without entering the entire command hierarchy: 

 admin@PA-3060# set secondary-ntp-server ntp-server-address 10.1.2.3 

 Use the up command to
move up a level in the command hierarchy. Use the top command
to move back to the top of the command hierarchy. 

 To delete an existing configuration setting, use a delete command.
For example, to delete the secondary NTP server address, you would
enter the following command: 

 admin@PA-3060# delete deviceconfig system ntp-servers secondary-ntp-server ntp-server-address 

 When deleting configuration settings or
objects using the CLI, the device does not check for dependencies
like it does in the web interface. Therefore, when you use delete from
the CLI, you must manually search the configuration for other places
where the configuration object might be referenced. For example,
before you delete an application filter group named browser-based
business, you should search the CLI for that value to see if it
is used anywhere in profiles or policies, using the following command: 

 admin@PA-3060> show config running | match "browser-based business" 

 Notice
that because the object you are matching on has a space in it, you
must enclose it in quotation marks. 

 Previous 

 View Settings and Statistics 

 Next 

 Commit Configuration Changes

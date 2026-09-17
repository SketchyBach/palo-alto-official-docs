---
url: https://docs.paloaltonetworks.com/content/techdocs/en_US/pan-os/10-0/pan-os-cli-quick-start/use-the-cli/load-configurations/load-a-partial-configuration/xpath-location-formats-determined-by-device-configuration.html
fetched_at: 2026-09-16T10:42:34Z
source: palo-alto-main
---

# Xpath Location Formats Determined by Device Configuration Clear

Updated on 

 Aug 28, 2023 

 Focus 

 Home 

 PAN-OS 

 PAN-OS CLI Quick Start 

 Use
the CLI 

 Load
Configurations 

 Load a Partial Configuration 

 Xpath Location Formats Determined by Device Configuration 

 Download PDF 

 PAN-OS CLI Quick Start 

 Xpath Location Formats Determined by Device Configuration 

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

 Xpath Location Formats Determined by Device Configuration 

 You specify the source and destination of the load partial command
using xpath locations, which specify the XML node in the configuration
you are copying from ( from-xpath ) and the
XML node in the candidate configuration you are copying to ( to-xpath ).
Determining the correct xpath is a critical part of using this command.
The following table shows the format for the from-xpath and to-xpath on
different types of devices. Notice that the from-xpath begins
at devices or shared ,
whereas the to-xpath begins with /config . 

 Type of Device Configuration 

 Xpath Formats 

 Multi-vsys Firewall 

 from-xpath 

 devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys-ID']/<object> 

 to-xpath 

 /config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys-ID']/<object> 

 Single-vsys Firewall 

 from-xpath 

 devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/<object> 

 to-xpath 

 /config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/<object> 

 Panorama Shared Object 

 from-xpath 

 shared/<object> 

 to-xpath 

 /config/shared/<object> 

 Panorama Device Group Object 

 from-xpath 

 devices/entry[@name='localhost.localdomain']/device-group/entry[@name='device-group-name']/ <object> 

 to-xpath 

 /config/devices/entry[@name='localhost.localdomain']/device-group/entry[@name='device-group- name']/<object> 

 Previous 

 Load a Partial Configuration 

 Next 

 Load a Partial Configuration into Another Configuration Using Xpath Values

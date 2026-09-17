---
url: https://docs.paloaltonetworks.com/content/techdocs/en_US/pan-os/10-0/pan-os-cli-quick-start/cli-changes/deleted-load-commands.html
fetched_at: 2026-09-16T10:42:36Z
source: palo-alto-main
---

# Removed Load Commands Clear

Updated on 

 Mon Aug 28 18:33:05 PDT 2023 

 Focus 

 Home 

 PAN-OS 

 PAN-OS CLI Quick Start 

 CLI Changes in PAN-OS 10.0 

 Load Commands Removed in PAN-OS 10.0 

 Download PDF 

 PAN-OS CLI Quick Start 

 Load Commands Removed in PAN-OS 10.0 

 Table of Contents 

 Filter

 Version 

 10.0 (EoL) 

 10.0 (EoL) 

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

 Load Commands Removed in PAN-OS 10.0 

 Command line interface 'load' commands that are removed
 in PAN-OS 10.0: 

 The following commands are no longer available in the 10.0 release. 

load config key <value>|<default> regenerate-rule-uuid-all <yes|no> from <value>
load config key <value>|<default> regenerate-rule-uuid-all <yes|no> version <value>|<1-1048576>
load config key <value>|<default> regenerate-rule-uuid-all <yes|no> last-saved

load config key <value>|<default> regenerate-rule-uuid-all <yes|no> partial shared-objects <included> shared-policies <included> from <value> from-xpath <value> to-xpath <value> mode <merge|replace|append> device-group
load config key <value>|<default> regenerate-rule-uuid-all <yes|no> partial shared-objects <included> shared-policies <included> from <value> from-xpath <value> to-xpath <value> mode <merge|replace|append> device-group [ <device-group1> <device-group2>... ]

load config key <value>|<default> regenerate-rule-uuid-all <yes|no> partial shared-objects <included> shared-policies <included> from <value> from-xpath <value> to-xpath <value> mode <merge|replace|append> template
load config key <value>|<default> regenerate-rule-uuid-all <yes|no> partial shared-objects <included> shared-policies <included> from <value> from-xpath <value> to-xpath <value> mode <merge|replace|append> template [ <template1> <template2>... ]

load config key <value>|<default> regenerate-rule-uuid-all <yes|no> partial shared-objects <included> shared-policies <included> from <value> from-xpath <value> to-xpath <value> mode <merge|replace|append> template-stack
load config key <value>|<default> regenerate-rule-uuid-all <yes|no> partial shared-objects <included> shared-policies <included> from <value> from-xpath <value> to-xpath <value> mode <merge|replace|append> template-stack [ <template-stack1> <template-stack2>... ]

 Previous 

 Load Commands Changed in PAN-OS 10.0 

 Next 

 Revert Commands Changed in PANOS-10.0

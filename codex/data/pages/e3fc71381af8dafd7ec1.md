---
url: https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-cli-quick-start/get-started-with-the-cli/customize-the-cli
fetched_at: 2026-09-16T07:39:42Z
source: palo-alto-main
---

# Customize the CLI Clear

Updated on 

 Thu Aug 28 22:57:13 PDT 2025 

 Focus 

 Home 

 Next-Generation Firewall 

 Get Started with the CLI 

 Customize the CLI 

 Download PDF 

 Next-Generation Firewall 

 Customize the CLI 

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

 Get Help on Command Syntax 

 Next 

 Use the CLI 

 Customize the CLI 

 Configure CLI settings, preferences, and display options to personalize your PAN-OS command-line interface experience. 

 Where Can I Use This? What Do I Need? 

 NGFW (Managed by PAN-OS or Panorama) 

 No prerequisites needed 

 Specify how long an administrative session
to the management interface (CLI or web interface) can remain idle
before logging the administrator out: 

 username@hostname# set deviceconfig setting management idle-timeout ? 
  0        never 
  <value>  <1-1440> 

 If you
want to set the CLI timeout value to a value different from the
global management idle-timeout value, use
the set cli timeout command in operational
mode. 

 Specify the format for command output: 

 username@hostname> set cli config-output-format ? 
  default   default 
  json      json 
  set       set 
  xml       xml 

 For example, in the default setting
the config-output-format looks like this: 

 username@hostname# show deviceconfig system dns-setting servers 
servers {
 primary 1.2.3.4;
 secondary 1.2.3.5;
}

 Changing the setting to set results
in output that looks like this: 

 username@hostname# show deviceconfig system dns-setting servers 
set deviceconfig system dns-setting servers primary 1.2.3.4
set deviceconfig system dns-setting servers secondary 1.2.3.5
[edit] 
[edit] 

 Changing the setting to xml results
in output that looks like this: 

 username@hostname# show deviceconfig system dns-setting servers 
<response status="success" code="19"> 
  <result total-count="1" count="1"> 
    <servers> 
      <primary>1.2.3.4</primary>
 <secondary>1.2.3.5</secondary>        
    </servers> 
  </result> 
</response> 

 Switch to scripting mode. In scripting mode, you can
copy and paste commands from a text file directly into the CLI.
Although you can do this without scripting-mode enabled (up to 20
lines). If you cut-and-paste a block of text into the CLI, examine
the output of the lines you pasted. If you see lines that are truncated
or generate errors, you may have to re-paste a smaller section of
text, or switch to scripting-mode : 

 username@hostname> set cli scripting-mode on 

 When in scripting-mode, you cannot use Tab to
complete commands or use ? to get help on
command syntax. When you are done pasting commands, switch back
to regular mode using the set cli scripting-mode off command. 

 Previous 

 Get Help on Command Syntax 

 Next 

 Use the CLI

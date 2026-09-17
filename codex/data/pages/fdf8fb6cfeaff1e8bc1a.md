---
url: https://cortex-docs.paloaltonetworks.com/7.x/7.2-eol/features-introduced-in-cortex-r-xdr-tm-agent-7.2
fetched_at: 2026-09-16T09:14:58Z
source: cortex-platform
---

# Features Introduced in Cortex® XDR™ Agent 7.2 | 7.2 (EoL) | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Release Notes 

 Cortex XDR Agent 

 Cortex XDR Agent 7.x 

 7.2 (EoL) 

 Features Introduced in Cortex® XDR™ Agent 7.2 

 Features Introduced in Cortex® XDR™ Agent 7.2 

 Features Introduced in Cortex XDR Agent 7.2.4 

 There are no new features in this release. 

 Features Introduced in Cortex XDR Agent 7.2.3 

 Linux 

 Linux Agent Feature 

 Description 

 New Distribution Support 

 You can now install the Cortex XDR agent on the following Linux endpoints:

• SUSE 15 SP2
• Debian 10

For information on supported operating systems and compatibility with third-party security products, see the Palo Alto Networks® Compatibility Matrix. 

 Features Introduced in Cortex XDR Agent 7.2.2 

 There are no new features in this release. 

 Features Introduced in Cortex XDR Agent 7.2.1 

 Cross-Platform Features 

 Feature 

 Description 

 Supportfor FQDN Proxy Server Address 

 Starting with this release, you can configure the Cortex XDR agent proxy also using the proxy server Fully Qualified Domain Name (FQDN). When you enter the FQDN, you can use both lowercase and uppercase letters. Avoid using special characters or spaces.

• For example, you can set these three proxies through Endpoint Administration:

My.Network.Name:808,10.196.20.244:8080

• Avoid these formats:
• Missing port numbers
My.Network.Name,100.120.130.140
• Spaces between IP, FQDN and port
My.Network.Name:808,100.120.130.140:8080
• Unsupported characters
My.Network.Name:808,100. .130.140: 

 Features Introduced in Cortex XDR Agent 7.2 

 Cross-Platform Features 

 Cross-Platform Agent Features 

 Description 

 Host Insights Add-on

(Requires a Cortex XDR Pro per Endpoint license) 

 Cortex XDR now offers additional security capabilities you can add to improve the security posture of your organization. Add-ons require an additional license. After you activate an add-on for your tenant, you can access the module from the new Add-ons menu.

Host Insights is the first add-on module that is available in Cortex XDR. This module requires a Cortex XDR Pro per Endpoint license, and is free for a 3 month trial period. The Host Insights add-on provides the following:

• System Visibility—(Windows) Full visibility into the business and IT operational data on all your endpoints. By reviewing insights for all your hosts in a single place, you can quickly identify IT and security issues that exist in your network, such as identifying a suspicious service or autoruns that were added to an endpoint. The Cortex XDR Host Inventory includes information about Users, Groups, Users to groups mapping, Services, Drivers, Autoruns, System information, Shares, and Disks.

• Application Inventory—(Windows, Mac, and Linux)) As introduced in previous Cortex XDR releases, the inventory lists all the applications running on all your endpoints (previously named Application Inventory). Application inventory is supported for Cortex XDR agent 7.1 and later releases.

• Vulnerability Management—(Linux) As introduced in previous Cortex XDR releases, Vulnerability Management enables you to identify and quantify the security vulnerabilities on your endpoints (previously named Vulnerability Assessment). Vulnerability Management is supported for Cortex XDR agent 7.1 and later releases.

• Search and Destroy—(Windows) Search and Destroy files on your endpoints to take immediate action on known and suspected malicious files. You can search from Cortex XDR for a file by hash or path on endpoints, and after you identify the presence of the file, you can immediately destroy the file from any or all endpoints on which the file exists.

To enable the Cortex XDR agent to collect the endpoint data required for the Host insights module, you must enable Endpoint Data Collection in the Global Agent Settings of your tenant. 

 Cortex XDR Agents Migration Between Managing XDR Servers 

 You can now migrate existing agents between Cortex XDR tenants directly from the Cortex XDR management console. This can be useful during POCs or to change the allocation of agents between tenants. When you change the tenant that manages the agent, the agent transfers to the new tenant, as a freshly installed agent, without any data that was previously stored for it on the original tenant.

After the Cortex XDR registers with the new tenant, it can no longer communicate with the previous tenant.

To register to another tenant, the Cortex XDR agent requires a distribution ID from the available installation packages on the target tenant, matching the same operating system and for the same or a previous agent version. The Change managing server option is available from the advanced options menu only and for a user with administrator permissions. 

 Custom Port Configuration for the Agent Proxy Applet 

 In closed networks where the Cortex XDR agents communicate with the Cortex XDR management console through the Palo Alto Networks Broker VM, you can now configure a custom port for the communication.

To set a custom port, activate the Agent Proxy applet in your global tenant settings and edit the default 8888 port set by Cortex XDR. 

 Global Uninstall Agent Password Update 

 Now, you can edit the global agent uninstall password that you defined upon the initial setup of Cortex XDR for all the default profiles. Changing the global default password applies to new and existing agents for which the previous global password applied. If you want to use a different password to uninstall specific agents, you can override the default global uninstall password by setting a different password for those agents in the Agent Settings profile. 

 Bandwidth Calculator for Content Updates 

 Now, when you allocate for Cortex XDR the network bandwidth for content updates, Cortex XDR recommends the optimal value of Mbps based on the number of active agents in your network, and including overhead considerations for large content updates. 

 Windows 

 Windows Agent Feature 

 Description 

 Installed KB Visibility

(Requires a Cortex XDR Pro per Endpoint license) 

 The Cortex XDR agent now includes information about all the Microsoft patches installed on a Windows endpoint, including a link to the Microsoft official Knowledge Base (KB) support article. 

 Enhanced Endpoint Scanning 

 When the Cortex XDR agent encounters a file that is unknown to WildFire during an endpoint scan, the agent can now leverage its built-in Cortex XDR Local analysis engine to process the file directly on the endpoint and assign the file a benign or malicious verdict. Local analysis is used in all types of scans: periodic scans, malware scans you initiate from Cortex XDR, and custom scans you initiate from the endpoint. For future reference, the agent also uploads the file to the WildFire service for further analysis. 

 Improved Local Analysis Engine for Office Files with Macros 

 The local analysis engine for Cortex XDR agents running on Windows endpoints now provides enhanced coverage for Microsoft Office files with macros. When the endpoint user attempts to open an Office file with a macro, and the WildFire verdict for the file is unavailable (if the sample is unknown to WildFire or the endpoint is currently disconnected from Cortex XDR), the Cortex XDR agent will analyze the file using the new advanced machine learning model for local analysis. 

 Device Control for User Defined Device Classes 

 You can now extend your Device Control policy rules for Windows endpoints to include custom USB connected device classes beyond Disk Drive, CD-ROM, Portable Devices and Floppy Disk Drives, such as USB connected network adapters. When you create a custom device class, you must provide the official ClassGuid identifier used by Microsoft. Alternatively, if you configured a GUID value to a specific USB connected device, you must use this value for the new device class. After you add a custom device class, you can enforce any device control rules and exceptions on this device class. 

 Post Detection Alert Response 

 The Cortex XDR agent can now proactively apply your malware security policy—such as quarantine and block settings—and enforce them when a post-detection alert is raised. A post-detection alert is raised for activity, files, or processes that were previously thought to be benign but are now—as a result of additional information, analysis, or administrator action—known to be malicious.

For example, if your security policy enables the Cortex XDR agent to block malicious files and processes, the agent can immediately halt running files and processes and block any future attempts to run. If you also enable the Cortex XDR agent to quarantine files, the agent can proactively quarantine detected malware even if it is dormant and not currently running.

After the Cortex XDR agent enforces the security policy, Cortex XDR updates the action from detected to prevented for the corresponding alert. 

 HostIdentification by its Fully Qualified Domain Name 

 To help you uniquely identify the host in an alert, Cortex XDR now displays also the fully qualified domain name (FQDN) of Windows hosts. This is especially helpful if you have multiple domains or duplicate host names in your network. 

 Mac 

 Mac Agent Feature 

 Description 

 Device Control of USB-Connected Devices 

 To protect Mac endpoints from loading malicious files from USB-connected removable devices (CD-ROM, disk drives, and floppy disks), Cortex XDR now extends Device Control to Mac endpoints. With Device Control, you can configure different policies to manage USB-connectivity on your endpoint. For example, you can:

• Block all supported USB-connected devices.
• Temporarily block only some USB-connected device types.
• Block a USB-connected device type but allow a specific vendor or product from that list read/write permissions on the endpoint.

To apply Device Control to your Mac endpoints, you define Device Control profiles according to the device types, and configure device control policies that apply to Cortex XDR endpoints or endpoint groups. 

 Disk Encryption Using FileVault 

 Cortex XDR now provides visibility into Mac endpoints that encrypt their hard drives using FileVault, the Apple built-in encryption tool, through Endpoints > Disk Encryption Visibility. Additionally, you can enforce FileVault encryption on the endpoint operating system disk through Cortex XDR, by configuring Disk Encryption profiles and applying them to your Mac endpoints.

The Cortex XDR Disk Encryption profile for Mac can encrypt the endpoint disk, however it cannot decrypt it. You have to perform the decryption manually on the endpoint. If you use an institutional recovery key (IRK) to decrypt the endpoint, you must ensure the key is signed by a valid authority. 

 Host Firewall 

 To reduce the attacks that occur during network communications on the endpoint, you can now control all inbound communications on your Mac endpoints, using the Cortex XDR Host Firewall. To use the host firewall, you set rules that allow or block inbound traffic on the endpoint, and apply them to your endpoints using Cortex XDR policy rules.

Cortex XDR enables you to configure different sets of rules according to the current location of the device within the organization network. To fine tune your control over the inbound communication, you can also:

• Hide your mac endpoint from all TCP and UDP networks using Apple Stealth mode.
• Block all incoming communications on the endpoint.
• Allow or block specific programs running on the endpoint using Apple BundleID.

To control inbound communication of your endpoints, Cortex XDR leverages the Mac Application Firewall APIs. The Cortex XDR agent applies the Application Firewall rules on the endpoint according to the settings configured in the Cortex XDR management console. 

 Network Location Resolution 

 To apply location based Host Firewall rules on your Mac endpoints, Cortex XDR can now determine whether the Cortex XDR agent is within the organization network or outside also for Mac endpoints. Similarly to the network location test performed for Windows endpoints, Cortex XDR performs a domain controller connectivity test and DNS test to determine whether the Cortex XDR agent is within the organization network or outside. 

 DMG Analysis 

 On macOS endpoints, the Cortex XDR agent can now Analyze and prevent malicious DMG files from running. To enable DMG file examination, you configure the new option in your Malware Security profiles. When an unknown DMG file attempts to run, the Cortex XDR agent sends the file to Cortex XDR for analysis by WildFire. The agent can then prevent the DMG from running until it receives the benign verdict for the file. 

 macOS 11.0 Support 

 You can install the Cortex XDR agent 7.2 on endpoints running macOS 11.0 Big Sur. For complete compatibility information, see the Palo Alto Networks Compatibility Matrix.

The Cortex XDR Host Firewall capability is not supported with macOS 11.0. 

 Linux 

 Linux Agent Feature 

 Description 

 Web Shell Exploits Protection 

 The Cortex XDR agent now protects your Linux endpoints against PHP webshells. With advanced machine learning algorithms, the new Local Threat-Evaluation Engine (LTEE) analyses PHP scripts to detect webshells. When Local File Threat Examination is enabled in your Malware profile, the Cortex XDR agent creates an alert for any malicious PHP script. You can also set the policy to quarantine malicious PHP files on the endpoint.

You enable Local File Threat Examination in the Malware security proile. 

 Crypto Mining Protection 

 The Cortex XDR agent now protects your endpoint against crypto-mining attacks that could consume the endpoint CPU computing power, as part of the Behavioral threat protection (BTP) module. 

 New Distribution Support 

 You can now install the Cortex XDR agent on the following Linux endpoints:

• Ubuntu Server 20
• Ubuntu Server 16, Ubuntu Server 18, and Ubuntu Server 20 with Azure kernel modules
• Ubuntu Server 16, Ubuntu Server 18, and Ubuntu Server 20 with GCP kernel modules
• Red Hat 8.2

For full compatibility information, see the Compatibility Matrix. 

 Previous Cortex® XDR™ Agent 7.2 Release Information 

 Next Changes to Default Behavior 

 Last updated 1 month ago 

 Was this helpful?

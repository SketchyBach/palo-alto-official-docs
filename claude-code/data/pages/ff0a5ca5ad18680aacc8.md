---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsiam/protect-your-endpoints/endpoint-security/install-and-manage-endpoints/set-up-endpoint-protection/set-up-endpoint-profiles-and-exception-rules/set-up-malware-prevention-profiles
fetched_at: 2026-08-13T15:12:22Z
source: cortex-platform
---

# Set up malware prevention profiles | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

Set up malware prevention profiles | Cortex Documentation Portal 

 ⌘ Ctrl k 

 Blog Support 
 More 

 Home 

 Products 

 Guides 

 Release Notes 

 API 

 Reference 

 AI Assistant 

 Good afternoon 
 I'm here to help you with the docs. 

 What is this page about? What should I read next? Can you give an example? 

 ⌘ Ctrl i 

 AI Based on your context 
 Send 

 Learn about Cortex XSIAM 

 Navigate the Cortex XSIAM docs 

 Get started with Cortex XSIAM 

 Agentic AI in Cortex XSIAM 

 Cortex XSIAM product licenses 

 In-product support ticket creation 

 Supported web browsers 

 Use the interface 

 Manage API keys 

 Onboard Cortex XSIAM 

 How to onboard Cortex XSIAM 

 Plan and prepare 

 Deployment steps 

 Post-deployment 

 Configure Cortex XSIAM 

 Learn how to configure Cortex XSIAM 

 Data management 

 Cortex XSIAM Data Sources and Connectors 

 Marketplace 

 Configure the Cortex Agentic Assistant 

 Cortex MCP server 

 Automations 

 Engines 

 Remote repository management 

 Customize cases and issues 

 XQL query management 

 Multi-Tenant 

 Managed Services configuration in Cortex 

 Protect your endpoints 

 Endpoint security 

 Endpoint protection 

 Install and manage endpoints 

 Set up endpoint protection 

 Set up endpoint profiles and exception rules 

 Set up malware prevention profiles 

 Set up exploit prevention profiles 

 Set up agent settings profiles 

 Set up restrictions prevention profiles 

 Set up exception profiles and rules 

 Set up Identity profiles 

 Define endpoint groups 

 Configure global agent settings 

 Apply profiles to endpoints 

 Create an agent installation package 

 Harden endpoint security 

 Manage endpoint protection 

 Endpoint DLP 

 Detect, Investigate, and respond to threats 

 Monitor dashboards and reports 

 Investigation and response 

 Agentic Assistant chat 

 Asset management 

 Threat management 

 Attack surface management 

 Vulnerability management 

 Exposure management 

 Cortex Advanced Email Security 

 Identity Threat Detection and Response (ITDR) 

 Cloud Security 

 Monitor and track compliance adherence 

 Cloud security rules and policies 

 Cortex Cloud Data Classification 

 Cortex Data Security 

 Cloud Identity Security 

 Network exposure detection 

 Cortex Cloud SaaS Security 

 Cortex Cloud AI Security 

 Serverless function posture security 

 Cortex Cloud Application Security 

 Cloud workload policies and rules 

 Base image rules 

 Web and API Security (WAAS) 

 Serverless function runtime security 

 Reference and developer docs 

 Cortex XSIAM XQL 

 Graph Search 

 Cortex CLI 

 Role-Based Access Control 

 API documentation 

 Reference 

 Migrating to a new Broker VM image 

 Learn more about migrating to the latest broker VM image 

 Standalone Broker VM 

 Broker VM high availability cluster node 

 On this page 

 For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSIAM 

 Cortex XSIAM Documentation 

 Protect your endpoints 

 Endpoint security 

 Install and manage endpoints 

 Set up endpoint protection 

 Set up endpoint profiles and exception rules 

 Set up malware prevention profiles 

 Malware prevention profiles protect against the execution of malware including trojans, viruses, worms, and grayware. Malware prevention profiles serve two main purposes: to define how to treat behavior common with malware, such as ransomware or script-based attacks, and to define how to treat known malware and unknown files. 

 You can configure the action that Cortex XDR agents take when known malware, macros, and unknown files try to run on endpoints. By default, the Cortex XDR agent will receive the default profile that contains a pre-defined configuration for each malware protection capability supported by the platform. The default setting for each capability is shown in parentheses in the user interface. To fine-tune your malware prevention policy, you can override the configuration of each capability to block the malicious behavior or file, allow but report it, or disable the module. 

 For each setting that you override, clear the Use Default option, and select the setting of your choice. 

 Note 

 In this profile, the Report options configure the endpoints to report the corresponding suspicious files, actions, processes, or behaviors to Cortex XSIAM, without blocking them. The Disabled options configure the endpoints to neither analyze nor report the corresponding malware or behavior. 

 The tasks below are organized according to the operating systems used by your organization's endpoints. 

 Windows 

 Add a new profile and define basic settings. 

 From Cortex XSIAM, select Inventory → Endpoints → Policy Management → Prevention → Profiles . Click +Add Profile , and select whether to create a new profile, or to import a profile from a file. 

 Note 

 New profiles based on imported profiles are added, and do not replace existing ones. 

 Select the Windows platform, and Malware as the profile type. 

 Click Next . 

 For Profile Name , enter a unique name for the profile. The name can contain only letters, numbers, or spaces, and must be no more than 30 characters. The name will be visible from the list of profiles when you configure a policy rule. 

 For Description , to provide additional context for the purpose or business reason for creating the profile, enter a profile description. For example, you might include a case identification number or a link to a help desk ticket. 

 Configure Portable Executable and DLL Examination . The Cortex XDR agent can analyze and prevent malicious executable files and DLL files from running on Windows endpoints. 

 Note 

 As part of the anti-malware security flow, the Cortex XDR agent leverages the operating system's capability to identify revoked certificates for executables, and DLL files that attempt to run on the endpoint by accessing the Windows Certificate Revocation List (CRL). To allow the Cortex XDR agent access the CRL, you must enable internet access over port 80 for Windows endpoints. If the endpoint is not connected to the internet, or you experience delays with executables and DLLs running on the endpoint, contact Customer Support. 

 Item 

 Options 

 More details 

 Action Mode 

 Block 

 Report 

 Disabled 

 When the Cortex XDR agent detects attempts to run malware, it performs the configured action. 

 Quarantine Malicious Executables 

 Disabled 

 Quarantine WildFire malware verdict 

 Quarantine WildFire and Local Analysis malware verdict 

 By default, the Cortex XDR agent blocks malware from running, but does not quarantine the file. You can enable one of the options to quarantine files, depending on the verdict issuer. 

 Note 

 The Quarantine Malicious Executables feature is not available for malware identified on network drives. 

 Action when file is unknown to WildFire 

 Allow 

 Run Local Analysis 

 Block 

 Allow : Unknown files are not blocked and local verdicts are not issued for them. 

 Run Local Analysis : The Cortex XDR agent uses embedded machine learning to determine the likelihood that an unknown file is malware, and issues a local verdict for the file. 

 Block : Block unknown files but do not run local analysis. In this case, unknown files remain blocked until the Cortex XDR agent receives an official WildFire verdict. 

 Action when file is benign with low confidence 

 Allow 

 Run Local Analysis 

 Block 

 Select the action to take when a file with a Benign Low Confidence verdict from WildFire tries to run on the endpoint. When local analysis is enabled, the Cortex XDR agent uses embedded machine learning to determine the likelihood that an unknown file is malware, and issues a local verdict for the file. If you block this file but do not run a local analysis, the file remains blocked until the Cortex XDR agent receives a high-confidence WildFire verdict. 

 To enable this capability, ensure that WildFire analysis scoring is also enabled in Global Agent Settings. 

 Warning 

 For optimal user experience, we recommend that you set the action mode to either Allow or Run Local Analysis . 

 Upload unknown files to WildFire 

 Enabled 

 Disabled 

 When enabled, the Cortex XDR agent sends unknown files to Cortex XSIAM, and Cortex XSIAM sends the files to WildFire for analysis. 

 The file types that the Cortex XDR agent analyzes depend on the platform type. WildFire accepts files up to 300 MB in size. 

 Treat Grayware as Malware 

 Enabled 

 Disabled 

 When enabled, Cortex XSIAM treats all grayware with the same Action Mode as configured for malware. 

 When disabled, grayware is considered benign, and is not blocked. 

 Configure options for Office Files with Macros Examination . The Cortex XDR agent can analyze and prevent malicious macros embedded in Microsoft Office files (Word, Excel) from running on Windows endpoints. 

 Item 

 Options 

 More details 

 Action Mode 

 Block 

 Report 

 Disabled 

 When the Cortex XDR agent detects attempts to run malware, it performs the configured action. 

 Action when file is unknown to WildFire 

 Allow 

 Run Local Analysis 

 Block 

 Select the action to take when a file is not recognized by WildFire. When local analysis is enabled, the Cortex XDR agent uses embedded machine learning to determine the likelihood that an unknown file is malware, and issues a local verdict for the file. 

 If you block unknown files, but do not run local analysis, unknown files remain blocked until the Cortex XDR agent receives an official WildFire verdict. 

 Action when WildFire verdict is Benign Low Confidence 

 Allow 

 Run Local Analysis 

 Block 

 Select the action to take when a file with a Benign Low Confidence verdict from WildFire tries to run on the endpoint. When local analysis is enabled, the Cortex XDR agent uses embedded machine learning to determine the likelihood that an unknown file is malware, and issues a local verdict for the file. 

 If you block this file but do not run a local analysis, the file remains blocked until the Cortex XDR agent receives a high-confidence WildFire verdict. 

 To enable this capability, ensure that WildFire analysis scoring is also enabled in Global Agent Settings. 

 Warning 

 For optimal user experience, we recommend that you set the action mode to either Allow or Run Local Analysis . 

 Upload unknown files to WildFire 

 Enabled 

 Disabled 

 When enabled, the Cortex XDR agent sends unknown files to Cortex XSIAM, and Cortex XSIAM sends the files to WildFire for analysis. For macro analysis, the Cortex XDR agent sends the Microsoft Office file containing the macro. 

 The file types that the Cortex XDR agent analyzes depend on the platform type. WildFire accepts files up to 300 MB in size. 

 Examine Office files from network drives 

 Enabled 

 Disabled 

 You can enable the Cortex XDR agent to examine Microsoft Office files on network drives when they contain a macro that attempts to run. 

 Configure JScript File Examination to protect endpoints from JScript-based attacks by detecting and preventing malicious JScript files from being executed or written to disk. 

 Item 

 Options 

 More details 

 Action Mode 

 Block 

 Report 

 Disabled 

 When the Cortex XDR agent detects attempts to run malware, it performs the configured action. 

 Quarantine Malicious Script Files 

 Disabled 

 Quarantine WildFire malware verdict 

 Quarantine WildFire and Local Analysis malware verdict 

 By default, the Cortex XDR agent blocks malware from running, but does not quarantine the file. You can enable one of the options to quarantine files, depending on the verdict issuer. 

 Action when file is unknown to WildFire 

 Allow 

 Run Local Analysis 

 Block 

 Allow : Unknown files are not blocked and local verdicts are not issued for them. 

 Run Local Analysis : The Cortex XDR agent uses embedded machine learning to determine the likelihood that an unknown file is malware, and issues a local verdict for the file. 

 Block : Block unknown files but do not run local analysis. In this case, unknown files remain blocked until the Cortex XDR agent receives an official WildFire verdict. 

 Upload unknown files to WildFire 

 Enabled 

 Disabled 

 When enabled, the Cortex XDR agent sends unknown files to Cortex XSIAM, and Cortex XSIAM sends the files to WildFire for analysis. 

 The file types that the Cortex XDR agent analyzes depend on the platform type. WildFire accepts files up to 300 MB in size. 

 Configure PowerShell Script Files to analyze and prevent malicious PowerShell script files from running on Windows-based endpoints. 

 Item 

 Options 

 More details 

 Action Mode 

 Block 

 Report 

 Disabled 

 When the Cortex XDR agent detects attempts to run malicious PowerShell script files, it performs the configured action. 

 Quarantine Malicious Script Files 

 Disabled 

 Quarantine WildFire malware verdict 

 Quarantine WildFire and Local Analysis malware verdict 

 By default, the Cortex XDR agent blocks malware from running, but does not quarantine the file. You can enable one of the options to quarantine files, depending on the verdict issuer. 

 Note 

 The Quarantine Malicious Script Files feature is not available for malware identified on network drives. 

 Action when file is unknown to WildFire 

 Allow 

 Run Local Analysis 

 Block 

 Allow : Unknown files are not blocked and local verdicts are not issued for them. 

 Run Local Analysis : The Cortex XDR agent uses embedded machine learning to determine the likelihood that an unknown file is malware, and issues a local verdict for the file. 

 Block : Block unknown files but do not run local analysis. In this case, unknown files remain blocked until the Cortex XDR agent receives an official WildFire verdict. 

 Upload unknown files to WildFire 

 Enabled 

 Disabled 

 When enabled, the Cortex XDR agent sends unknown files to Cortex XSIAM, and Cortex XSIAM sends the files to WildFire for analysis. 

 The file types that the Cortex XDR agent analyzes depend on the platform type. WildFire accepts files up to 300 MB in size. 

 For On-Write File Examination settings, configure the actions that Cortex XSIAM should take during the on-write process for various file types. 

 Note 

 If on-write actions were configured in earlier versions of Cortex XSIAM, the same configuration has been preserved and applied globally for all file types. 

 On-write file protection may have an impact on the resources required by the Cortex XDR agent. 

 Item 

 Options 

 More details 

 Portable Executable and DLL Examination 

 Enabled 

 Disabled 

 When a file type is enabled, the Cortex XDR agent monitors for malicious files during the on-write process, and if it finds any, it generates issues and quarantines the files. 

 Office files with macros 

 Enabled 

 Disabled 

 PowerShell script files 

 Enabled 

 Disabled 

 ASP & ASPX files 

 Enabled 

 Disabled 

 VBScript files 

 Enabled 

 Disabled 

 JScript files 

 Enabled 

 Disabled 

 Configure ASP & ASPX Files to analyze and prevent malicious ASP and ASPX files from being written to the file system. If you want to enable this capability, enable On-write File Examination . 

 Item 

 Options 

 More details 

 Action Mode 

 Block 

 Report 

 Disabled 

 When the Cortex XDR agent detects attempts to write malicious ASP and ASPX files, it performs the configured action. 

 When Action Mode is set to Block, quarantine is enabled. 

 Action when file is unknown to WildFire 

 Allow 

 Run Local Analysis 

 Block 

 Allow : Unknown files are not blocked and local verdicts are not issued for them. 

 Run Local Analysis : The Cortex XDR agent uses embedded machine learning to determine the likelihood that an unknown file is malware, and issues a local verdict for the file. 

 Block : Block unknown files but do not run local analysis. In this case, unknown files remain blocked until the Cortex XDR agent receives an official WildFire verdict. 

 Upload unknown files to WildFire 

 Enabled 

 Disabled 

 When enabled, the Cortex XDR agent sends unknown files to Cortex XSIAM, and Cortex XSIAM sends the files to WildFire for analysis. 

 The file types that the Cortex XDR agent analyzes depend on the platform type. WildFire accepts files up to 300 MB in size. 

 Configure On-demand File Examination to scan endpoints and attached removable drives for dormant, inactive malware. 

 Note 

 On-demand file protection may have an impact on the resources required by the Cortex XDR agent. 

 Item 

 Options 

 More details 

 End-User Initiated Local Scan 

 Enabled 

 Disabled 

 When enabled, the endpoint user can perform a local scan on the endpoint. 

 Periodic Scan 

 Enabled 

 Disabled 

 Note 

 We recommend that you disable scheduled scanning. VDI machine scans are based on the golden image and additional files will be examined upon execution. 

 Periodic scanning enables you to scan endpoints on a recurring basis without waiting for malware to run on the endpoint. When enabled, you can set the time interval (weekly or monthly) and the day and time at which to start scanning. In addition, you can choose to enable or disable scanning of removable media drives. 

 Periodic scanning is persistent, and if the scan is scheduled to start while the endpoint is turned off, the scan will be initiated when the endpoint is turned on again. The scheduling of future scans is not affected by this delay. 

 Note 

 When periodic scanning is enabled in your profile, the Cortex XDR agent initiates an initial scan when it is first installed on the endpoint, regardless of the periodic scanning scheduling time. 

 Configure VB Scripts Examination to analyze and prevent malicious VB script files from running. 

 Item 

 Options 

 More details 

 Action Mode 

 Block 

 Report 

 Disabled 

 When the Cortex XDR agent detects attempts to run malicious VB script files, it performs the configured action. 

 Quarantine Malicious Files 

 Disabled 

 Quarantine WildFire malware verdict 

 Quarantine WildFire and Local Analysis malware verdict 

 The Cortex XDR agent can quarantine VB script files that WildFire or local analysis determine are malware. 

 When disabled, the Cortex XDR agent does not quarantine malicious VB script files. 

 Action when file is unknown to WildFire 

 Allow 

 Run Local Analysis 

 Block 

 Allow : Unknown files are not blocked and local verdicts are not issued for them. 

 Run Local Analysis : The Cortex XDR agent uses embedded machine learning to determine the likelihood that an unknown file is malware, and issues a local verdict for the file. 

 Upload unknown files to WildFire 

 Enabled 

 Disabled 

 When enabled, the Cortex XDR agent sends unknown files to Cortex XSIAM, and Cortex XSIAM sends the files to WildFire for analysis. 

 The file types that the Cortex XDR agent analyzes depend on the platform type. WildFire accepts files up to 300 MB in size. 

 Configure LDAP Protection to analyze and act upon suspicious LDAP queries sent by the agent to a Domain Controller. This feature is designed to detect and block Active Directory reconnaissance attacks. 

 Notice 

 Requires the ITDR add-on. 

 Note 

 This feature only comes into effect after a restart. 

 Item 

 Options 

 More details 

 Action Mode 

 Block 

 Report 

 Disabled 

 When the Cortex XDR agent detects suspicious attempts to query a Domain Controller, it performs the configured action. 

 Monitor and Collect Domain Controller LDAP Events 

 Enabled 

 Disabled 

 When set to Enabled , the Cortex XDR agent collects information about LDAP queries and creates events for them. These events can be used investigate suspicious LDAP queries. 

 Configure the Global Behavioral Threat Protection Rules . Use these rules to protect endpoints from malicious causality chains. 

 Item 

 Options 

 More details 

 Action Mode 

 Block 

 Report 

 Disabled 

 The Cortex XDR agent protects against malicious causality chains, using behavioral threat protection rules. When the action mode is set to Block , the Cortex XDR agent terminates all processes and threads in the event chain up to the causality group owner (CGO). 

 Quarantine Malicious Files 

 Enabled 

 Disabled 

 When enabled, the Cortex XDR agent quarantines the processes and the artifacts, such as files, related to the CGO. 

 When disabled, the Cortex XDR agent does not quarantine the CGO of an event chain, nor any scripts or files called by the CGO. 

 Action Mode for Vulnerable Drivers Protection 

 Block 

 Report 

 Disabled 

 Behavioral threat protection rules can also detect attempts to load vulnerable drivers which can be used to bypass the Cortex XDR agent. As with other rules, Palo Alto Networks threat researchers can deliver changes to vulnerable driver rules with content updates. 

 Advanced API Monitoring 

 Enabled 

 Disabled 

 When enabled, the Cortex XDR agent adds additional hooks in user mode processes for increased coverage of anti-exploit and anti-malware modules. 

 Configure Credential Gathering Protection to protect endpoints from processes trying to access or steal passwords and other credentials. 

 Item 

 Options 

 More details 

 Action Mode 

 Block 

 Report 

 Disabled 

 The Cortex XDR agent protects against all processes and threads in the event chain up to the credential gathering process or file. 

 When this module is disabled, the Cortex XDR agent does not analyze the event chain and does not block credential gathering. 

 Quarantine Malicious Files 

 Enabled 

 Disabled 

 When enabled, the Cortex XDR agent quarantines the process or file related to the credential gathering event chain. 

 Configure Anti Webshell Protection to protect endpoint processes from dropping malicious web shells. 

 Item 

 Options 

 More details 

 Action Mode 

 Block 

 Report 

 Disabled 

 In a causality chain, when the Cortex XDR agent detects a process that attempts to drop malicious web shells, it performs the configured action. 

 Quarantine Malicious Files 

 Enabled 

 Disabled 

 When enabled, the Cortex XDR agent quarantines the processes or files that are related to the web shell drop event chain, and any scripts or files called by the web shell dropping process. 

 Configure Financial Malware Threat Protection to protect against techniques specific to financial and banking malware. 

 Item 

 Options 

 More details 

 Action Mode 

 Block 

 Report 

 Disabled 

 In a causality chain, when the Cortex XDR agent detects a process that attempts to access or steal financial or banking information, the Cortex XDR agent performs the configured action. 

 Quarantine Malicious Files 

 Enabled 

 Disabled 

 When enabled, the Cortex XDR agent quarantines the processes or files related to the financial information gathering event chain, and scripts or files called by the financial information gathering process. 

 Crypto Wallet Protection 

 Enabled 

 Disabled 

 When enabled, provides protection for cryptocurrency wallets that are stored on endpoints. Cryptocurrency wallets store private keys that are used to access crypto assets. 

 Configure Cryptominers Protection to protect against attempts to locate or steal cryptocurrencies. 

 Item 

 Options 

 More details 

 Action Mode 

 Block 

 Report 

 Disabled 

 In a causality chain, when the Cortex XDR agent detects a cryptomining process or file, the Cortex XDR agent performs the configured action. 

 Quarantine Malicious Files 

 Enabled 

 Disabled 

 When enabled, the Cortex XDR agent quarantines the process or file detected during a cryptocurrency gathering attempt. 

 Configure In-process shellcode protection to protect against in-process shellcode attack threats. 

 Item 

 Options 

 More details 

 Action Mode 

 Block 

 Report 

 Disabled 

 In a causality chain, when the Cortex XDR agent detects a process that attempts to run in-process shellcodes to load malicious code, the Cortex XDR agent performs the configured action. 

 Quarantine Malicious Files 

 Enabled 

 Disabled 

 When enabled, the Cortex XDR agent quarantines the in-process shellcode processes or files related to a causality chain. 

 Process Injection 32 Bit 

 Enabled 

 Disabled 

 When enabled, the Cortex XDR agent quarantines 32 bit in-process shellcode processes or files related to a causality chain. 

 Process injection 32 bit is set to Enabled by default for all new tenants created after 25 June 2023. For tenants created before this date, the default was set to Disabled . 

 Shellcode AI Protection 

 Enabled 

 Disabled 

 When enabled, Precision AI-based detection rules use machine learning to detect and prevent in-memory shellcode attacks.When enabled, Precision AI-based detection rules use machine learning to detect and prevent in-memory shellcode attacks. 

 Configure Malicious Device Prevention to protect against the connection of potentially malicious devices to endpoints. 

 Item 

 Options 

 More details 

 Action Mode 

 Block 

 Report 

 Disabled 

 When the Cortex XDR agent detects the connection of potentially malicious external device to an endpoint, the Cortex XDR agent performs the configured action. 

 Configure UAC Bypass Prevention to protect against the User Access Control (UAC) bypass mechanism that is associated with privilege elevation attempts. 

 Item 

 Options 

 More details 

 Action Mode 

 Block 

 Report 

 Disabled 

 When the Cortex XDR agent detects a UAC bypass mechanism, the Cortex XDR agent performs the configured action. The Block option blocks all processes and threads in the event chain up to the UAC bypass mechanism. 

 Quarantine Malicious Files 

 Enabled 

 Disabled 

 When enabled, the Cortex XDR agent quarantines the UAC bypass processes or files related to the chain, and any scripts or files released to the UAC bypass mechanism. 

 Configure Anti Tampering Protection to protect against tampering attempts. 

 Item 

 Options 

 More details 

 Action Mode 

 Block 

 Report 

 Disabled 

 When the Cortex XDR agent detects a tampering attempt, including modification and/or termination of the Cortex XDR agent, it performs the configured action. 

 If you choose the Block option, you must also enable XDR Agent Tampering Protection in the Agent Settings profile, and ensure that both profiles are assigned to the same endpoints. 

 Quarantine Malicious Files 

 Enabled 

 Disabled 

 When enabled, the Cortex XDR agent quarantines the processes or files that are related to the tampering attempt. 

 Malicious Safe Mode Rebooting Protection 

 Block 

 Report 

 Disabled 

 Define the action to take when the Cortex XDR agent detects safe mode reboot attempts made suspiciously by other apps. 

 Configure IIS Protection to protect against Internet Information Server (IIS) attacks. 

 Item 

 Options 

 More details 

 Action Mode 

 Block 

 Report 

 Disabled 

 When the Cortex XDR agent detects a threat that targets an Internet Information Server (IIS), the Cortex XDR agent performs the configured action. 

 Quarantine Malicious Files 

 Enabled 

 Disabled 

 When enabled, the Cortex XDR agent quarantines the processes or files that are related to the IIS attack. 

 Configure UEFI Protection , to protect the endpoint from Unified Extensible Firmware Interface (UEFI) manipulation attempts. 

 Item 

 Options 

 More details 

 Action Mode 

 Block 

 Report 

 Disabled 

 When the Cortex XDR agent detects UEFI manipulation attempts, it performs the configured action. When Block is selected, the Cortex XDR agent blocks all processes and threads in the event chain, up to the UEFI threat. 

 Quarantine Malicious Files 

 Enabled 

 Disabled 

 When enabled, the Cortex XDR agent quarantines the processes or files that are related to the UEFI threat. 

 Configure Ransomware Protection to protect against encryption-based activity associated with ransomware attacks. 

 Item 

 Options 

 More details 

 Action Mode 

 Block 

 Report 

 Disabled 

 When the Cortex XDR agent detects ransomware activity locally on the endpoint or in pre-defined network folders, the Cortex XDR agent performs the configured action. 

 Quarantine Malicious Process 

 Enabled 

 Disabled 

 When enabled, the Cortex XDR agent quarantines the processes that are related to the ransomware activity. 

 The Quarantine Malicious Process option is only available if Action Mode is set to Block . 

 Protection Mode 

 Normal 

 Aggressive 

 By default, Protection Mode is set to Normal , where the decoy files on the endpoint are present, but do not interfere with benign applications and end user activity on the endpoint. If you suspect your network has been infected with ransomware, and you need to provide better coverage, you can apply the Aggressive protection mode. Aggressive mode exposes more applications in your environment to the Cortex XDR agent decoy files. However, it also increases the likelihood that benign software is exposed to decoy files, generating false ransomware issues, and impairing user experience. 

 Configure Malicious Child Process Protection to prevent script-based attacks. Such attacks can be used to deliver malware by blocking targeted processes that are commonly used to bypass traditional security methods. 

 Item 

 Options 

 More details 

 Action Mode 

 Block 

 Report 

 Disabled 

 When the Cortex XDR agent detects known suspicious parent-child relationships that are used to bypass security, the Cortex XDR agent performs the configured action. When Block is selected, known suspicious child processes are blocked from starting. 

 To prevent attacks that extract passwords from memory using the Mimikatz tool, set Password Theft Protection to Enabled . 

 Configure Respond to Malicious Causality Chains options, which define the automatic response actions taken by the Cortex XDR agent when it identifies malicious causality chains. 

 Item 

 Options 

 More details 

 Terminate Connection and Block IP Address of Remote Causality Group Owner 

 Enabled 

 Disabled 

 When the Cortex XDR agent identifies a remote network connection that attempts to perform malicious activity—such as encrypting endpoint files—the agent can automatically block the IP address to close all existing communication, and to block new connections from this IP address to the endpoint. When Cortex XSIAM blocks an IP address per endpoint, that address remains blocked throughout all agent profiles and policies, including any host-firewall policy rules. You can view the list of all blocked IP addresses per endpoint from the Action Center, as well as unblock them to re-enable communication as appropriate. 

 Configure the Network Packet Inspection Engine to analyze network packet data for malicious behavior. 

 Item 

 Options 

 More details 

 Action Mode 

 Terminate session 

 Report 

 Disabled 

 By analyzing the network packet data, the Cortex XDR agent can already detect malicious behavior at the network level, and provide protection to the growing corporate network boundaries. The engine leverages both Palo Alto Networks NGFW content rules, and new Cortex XDR content rules created by the Cortex XDR Research Team. The Cortex XDR content rules are updated through the security content. This feature focuses on detecting outbound C2 activity. 

 The Terminate session option configures Cortex XDR agents to analyze connections and to drop the malicious connections. 

 The Report option configures XDR agents to analyze connections, to allow the transmission of packets in your network, but to report them to Cortex XSIAM. 

 Configure Dynamic Kernel Protection to protect the endpoint from kernel-level threats such as bootkits, rootkits, and susceptible drivers. 

 Item 

 Options 

 More details 

 Action Mode 

 Block 

 Report 

 Disabled 

 When set to Block , this protection module loads during the boot process to protect the endpoint against malicious processes running at boot time. 

 Configure Dynamic Driver Protection to protect the endpoint against the abuse of Kernel drivers. 

 Item 

 Options 

 More details 

 Action Mode 

 Block 

 Report 

 Disabled 

 When set to Block , runtime prevention of driver-based attacks that attempt to escalate privileges or exploit the kernel. 

 Quarantine Malicious Files 

 Enabled 

 Disabled 

 When enabled, the Cortex XDR agent quarantines the drivers that are a threat. 

 Configure Security Measures Bypass to protect the endpoint from malicious actors attempting to bypass Windows built-in security controls. 

 Item 

 Options 

 More details 

 Action Mode 

 Block 

 Report 

 Disabled 

 When set to Block , this protection module blocks techniques used by attackers to bypass endpoint security controls. 

 Quarantine Malicious Files 

 Enabled 

 Disabled 

 When enabled, the Cortex XDR agent quarantines the processes that are related to bypass techniques. 

 Configure Breach and Attack Simulation (BAS) Tools settings . 

 Item 

 Options 

 More details 

 Action Mode 

 Enabled 

 Disabled (default) 

 When BAS mode is enabled, BAS tools will receive special handling. Only the simulation itself is terminated. 

 When BAS mode is disabled, BAS tools are treated like any other malicious process. Based on the profile settings, BAS tools will face the same prevention measures as all other threats 

 Note 

 When you are actively evaluating with BAS tools, it is recommended to enable the BAS mode setting only for the duration of your evaluation, and for a limited number of agents. 

 Note 

 BAS tools mode with content older than version 1850 cannot be configured, the agent will be treated as Enabled. 

 To save the profile, click Create . 

 What to do next 

 If you are ready to apply your new profile to endpoints, you do this by adding it to a policy rule. If you still need to define other profiles, you can do this later. During policy rule creation or editing, you select the endpoints to which to assign the policy. There are different ways of doing this, such as: 

 macOS 

 Add a new profile and define basic settings. 

 From Cortex XSIAM, select Inventory → Endpoints → Policy Management → Prevention → Profiles . Click +Add Profile , and select whether to create a new profile, or to import a profile from a file. 

 Note 

 New profiles based on imported profiles are added, and do not replace existing ones. 

 Select the macOS platform, and Malware as the profile type. 

 Click Next . 

 For Profile Name , enter a unique name for the profile. The name can contain only letters, numbers, or spaces, and must be no more than 30 characters. The name will be visible from the list of profiles when you configure a policy rule. 

 For Description , to provide additional context for the purpose or business reason for creating the profile, enter a profile description. For example, you might include a case identification number or a link to a help desk ticket. 

 Configure Respond to Malicious Causality Chains . This is the agent's automatic response actions to malicious causality chains. 

 Item 

 Options 

 More details 

 Terminate connection and block IP address of remote causality group owner 

 Enabled 

 Disabled 

 When enabled, the Cortex XDR agent terminates the connection and blocks the IP address of a remote causality group owner. 

 Configure the Network Packet Inspection Engine to detect malicious behavior. 

 Item 

 Options 

 More details 

 Action Mode 

 Terminate Session 

 Report 

 Disabled 

 When the Cortex XDR agent detects malicious behavior, it performs the configured action. 

 Configure the Global Behavioral Threat Protection Rules . These rules can be used to protect endpoints from malicious causality chains. 

 Item 

 Options 

 More details 

 Action Mode 

 Block 

 Report 

 Disabled 

 The Cortex XDR agent protects against malicious causality chains, using behavioral threat protection rules. When the action mode is set to Block , the Cortex XDR agent terminates all processes and threads in the event chain up to the causality group owner (CGO). 

 Quarantine Malicious Files 

 Enabled 

 Disabled 

 When enabled, the Cortex XDR agent quarantines the processes and the artifacts, such as files, related to the CGO. 

 When disabled, the Cortex XDR agent does not quarantine the CGO of an event chain, nor any scripts or files called by the CGO. 

 Configure Credential Gathering Protection to protect endpoints from processes trying to access or steal passwords and other credentials. 

 Item 

 Options 

 More details 

 Action Mode 

 Block 

 Report 

 Disabled 

 The Cortex XDR agent protects against all processes and threads in the event chain up to the credential gathering process or file. 

 When this module is disabled, the Cortex XDR agent does not analyze the event chain and does not block credential gathering. 

 Quarantine Malicious Files 

 Enabled 

 Disabled 

 When enabled, the Cortex XDR agent quarantines the process or file related to the credential gathering event chain. 

 Configure Anti Webshell Protection to protect endpoint processes from dropping malicious web shells. 

 Item 

 Options 

 More details 

 Action Mode 

 Block 

 Report 

 Disabled 

 In a causality chain, when the Cortex XDR agent detects a process that attempts to drop malicious web shells, it performs the configured action. 

 Quarantine Malicious Files 

 Enabled 

 Disabled 

 When enabled, the Cortex XDR agent quarantines the processes or files that are related to the web shell drop event chain, and any scripts or files called by the web shell dropping process. 

 Configure Financial Malware Threat Protection to protect against techniques specific to financial and banking malware. 

 Item 

 Options 

 More details 

 Action Mode 

 Block 

 Report 

 Disabled 

 In a causality chain, when the Cortex XDR agent detects a process that attempts to access or steal financial or banking information, the Cortex XDR agent performs the configured action. 

 Quarantine Malicious Files 

 Enabled 

 Disabled 

 When enabled, the Cortex XDR agent quarantines the processes or files related to the financial information gathering event chain, and scripts or files called by the financial information gathering process. 

 Crypto Wallet Protection 

 Enabled 

 Disabled 

 When enabled, provides protection for cryptocurrency wallets that are stored on endpoints. Cryptocurrency wallets store private keys that are used to access crypto assets. 

 Configure Cryptominers Protection to protect against attempts to locate or steal cryptocurrencies. 

 Item 

 Options 

 More details 

 Action Mode 

 Block 

 Report 

 Disabled 

 In a causality chain, when the Cortex XDR agent detects a cryptomining process or file, the Cortex XDR agent performs the configured action. 

 Quarantine Malicious Files 

 Enabled 

 Disabled 

 When enabled, the Cortex XDR agent quarantines the process or file detected during a cryptocurrency gathering attempt. 

 Configure Malicious Device Protection to identify and block potentially malicious Human Interface Devices (HIDs), such as the USB Rubber Ducky. This capability allows organizations to significantly reduce their physical attack surface and defend against social engineering-based hardware threats. 

 Item 

 Options 

 More details 

 Action Mode 

 Block 

 Report 

 Disabled 

 When set to Block , the Cortex XDR agent blocks malicious HIDs. 

 When set to Report , an issue is generated, but no action is taken. 

 Configure Anti Tampering Protection to protect against tampering attempts. 

 Item 

 Options 

 More details 

 Action Mode 

 Block 

 Report 

 Disabled 

 When the Cortex XDR agent detects a tampering attempt, including modification and/or termination of the Cortex XDR agent, it performs the configured action. 

 If you choose the Block option, you must also enable XDR Agent Tampering Protection in the Agent Settings profile, and ensure that both profiles are assigned to the same endpoints. 

 Quarantine Malicious Files 

 Enabled 

 Disabled 

 When enabled, the Cortex XDR agent quarantines the processes or files that are related to the tampering attempt. 

 Configure Ransomware Protection to protect against encryption-based activity associated with ransomware attacks. 

 Item 

 Options 

 More details 

 Action Mode 

 Block 

 Report 

 Disabled 

 When the Cortex XDR agent detects ransomware activity locally on the endpoint or in pre-defined network folders, the Cortex XDR agent performs the configured action. 

 Quarantine Malicious Files 

 Enabled 

 Disabled 

 When enabled, the Cortex XDR agent quarantines the files that are related to the ransomware activity. 

 Configure Malicious Child Process Protection to prevent script-based attacks. Such attacks can be used to deliver malware by blocking targeted processes that are commonly used to bypass traditional security methods. 

 Item 

 Options 

 More details 

 Action Mode 

 Block 

 Report 

 Disabled 

 When the Cortex XDR agent detects known suspicious parent-child relationships that are used to bypass security, the Cortex XDR agent performs the configured action. When Block is selected, known suspicious child processes are blocked from starting. 

 Quarantine Malicious Files 

 Enabled 

 Disabled 

 When enabled, the Cortex XDR agent quarantines the files that are related to a malicious child process. 

 Configure On-demand File Examination to scan endpoints and attached removable drives for dormant, inactive malware. 

 Item 

 Options 

 More details 

 Periodic Scan 

 Enabled 

 Disabled 

 Note 

 We recommend that you disable scheduled scanning. VDI machine scans are based on the golden image and additional files will be examined upon execution. 

 Periodic scanning enables you to scan endpoints on a recurring basis without waiting for malware to run on the endpoint. When enabled, you can set the time interval (weekly or monthly) and the day and time at which to start scanning. In addition, you can choose to enable or disable scanning of removable media drives. 

 Periodic scanning is persistent, and if the scan is scheduled to start while the endpoint is turned off, the scan will be initiated when the endpoint is turned on again. The scheduling of future scans is not affected by this delay. 

 Note 

 When periodic scanning is enabled in your profile, the Cortex XDR agent initiates an initial scan when it is first installed on the endpoint, regardless of the periodic scanning scheduling time. 

 Configure Mach-O Execution Examination to check Mach-O files for malware upon execution. 

 Item 

 Options 

 More details 

 Action Mode 

 Block 

 Report 

 Disabled 

 When the Cortex XDR agent detects attempts to run malware, it performs the configured action. 

 Quarantine malicious Mach-O files 

 Disabled 

 Quarantine WildFire malware verdict 

 Quarantine WildFire and Locals Analysis malware verdict 

 By default, the Cortex XDR agent blocks malware from running, but does not quarantine the file. You can enable one of the options to quarantine files, depending on the verdict issuer. 

 Note 

 The Quarantine Malicious Mach-O Files feature is not available for malware identified on network drives. 

 Action on unknown Mach-O files to WildFire 

 Allow 

 Run Local Analysis 

 Block 

 Allow : Unknown files are not blocked and local verdicts are not issued for them. 

 Run Local Analysis : The Cortex XDR agent uses embedded machine learning to determine the likelihood that an unknown file is malware, and issues a local verdict for the file. 

 Block : Block unknown files but do not run local analysis. In this case, unknown files remain blocked until the Cortex XDR agent receives an official WildFire verdict. 

 Action when WildFire verdict is Benign Low Confidence 

 Allow 

 Run Local Analysis 

 Block 

 Select the action to take when a file with a Benign Low Confidence verdict from WildFire tries to run on the endpoint. When local analysis is enabled, the Cortex XDR agent uses embedded machine learning to determine the likelihood that an unknown file is malware, and issues a local verdict for the file. If you block this file but do not run a local analysis, the file remains blocked until the Cortex XDR agent receives a high-confidence WildFire verdict. 

 Warning 

 For optimal user experience, we recommend that you set the action mode to either Allow or Run Local Analysis . 

 Upload Mach-O files for cloud analysis 

 Enabled 

 Disabled 

 When enabled, the Cortex XDR agent sends unknown files to Cortex XSIAM, and Cortex XSIAM sends the files to WildFire for analysis. 

 The file types that the Cortex XDR agent analyzes depend on the platform type. WildFire accepts files up to 300 MB in size. 

 Treat Grayware as Malware 

 Enabled 

 Disabled 

 When enabled, Cortex XSIAM treats all grayware with the same Action Mode as configured for malware. 

 When disabled, grayware is considered benign, and is not blocked. 

 Configure Mach-O Loading Examination to detect and prevent execution of malicious Mach-O files when being loaded on macOS-based endpoints. 

 Item 

 Options 

 More details 

 Action Mode 

 Block 

 Report 

 Disabled 

 When the Cortex XDR agent detects attempts to run malware, it performs the configured action. 

 Quarantine malicious Mach-O files 

 Disabled 

 Quarantine WildFire malware verdict 

 Quarantine WildFire and Locals Analysis malware verdict 

 By default, the Cortex XDR agent blocks malware from running, but does not quarantine the file. You can enable one of the options to quarantine files, depending on the verdict issuer. 

 Action on unknown Mach-O files to WildFire 

 Allow 

 Run Local Analysis 

 Block 

 Allow : Unknown files are not blocked and local verdicts are not issued for them. 

 Run Local Analysis : The Cortex XDR agent uses embedded machine learning to determine the likelihood that an unknown file is malware, and issues a local verdict for the file. 

 Block : Block unknown files but do not run local analysis. In this case, unknown files remain blocked until the Cortex XDR agent receives an official WildFire verdict. 

 Action when WildFire verdict is Benign Low Confidence 

 Allow 

 Run Local Analysis 

 Block 

 Select the action to take when a file with a Benign Low Confidence verdict from WildFire tries to run on the endpoint. When local analysis is enabled, the Cortex XDR agent uses embedded machine learning to determine the likelihood that an unknown file is malware, and issues a local verdict for the file. If you block this file but do not run a local analysis, the file remains blocked until the Cortex XDR agent receives a high-confidence WildFire verdict. 

 Warning 

 For optimal user experience, we recommend that you set the action mode to either Allow or Run Local Analysis . 

 Upload Mach-O files for cloud analysis 

 Enabled 

 Disabled 

 When enabled, the Cortex XDR agent sends unknown files to Cortex XSIAM, and Cortex XSIAM sends the files to WildFire for analysis. 

 The file types that the Cortex XDR agent analyzes depend on the platform type. WildFire accepts files up to 300 MB in size. 

 Treat Grayware as Malware 

 Enabled 

 Disabled 

 When enabled, Cortex XSIAM treats all grayware with the same Action Mode as configured for malware. 

 When disabled, grayware is considered benign, and is not blocked. 

 Configure Local File Threat Examination to enable detection of malicious files on the endpoint. 

 Note 

 This module is supported by Cortex XDR agent 8.1.0 and later releases. 

 Item 

 Options 

 More details 

 Action Mode 

 Enabled 

 Disabled 

 When enabled, the Local Threat-Evaluation Engine (LTEE) analyzes the endpoint for PHP files arriving from a web server and generates issues about any malicious PHP scripts. 

 Terminate Malicious Processes 

 Enabled 

 Disabled 

 When enabled, the Cortex XDR agents terminates malicious PHP files on the endpoint. 

 Quarantine Malicious Files 

 Enabled 

 Disabled 

 When enabled, the Cortex XDR agent quarantines malicious files on the endpoint and does not quarantine updated files. 

 Configure DMG File Examination to check DMG files for malware. 

 Item 

 Options 

 More details 

 Action Mode 

 Block 

 Report 

 Disabled 

 When the Cortex XDR agent detects attempts to run malware in DMG files, it performs the configured action. 

 Quarantine Malicious Executables 

 Enabled 

 Disabled 

 When enabled, the Cortex XDR agent quarantines malicious executable DMG files. 

 Note 

 The Quarantine Malicious Executables feature is not available for malware identified on network drives. 

 Upload unknown files to WildFire 

 Enabled 

 Disabled 

 When enabled, the Cortex XDR agent sends unknown files to Cortex XSIAM, and Cortex XSIAM sends the files to WildFire for analysis. 

 The file types that the Cortex XDR agent analyzes depend on the platform type. WildFire accepts files up to 300 MB in size. 

 Configure Breach and Attack Simulation (BAS) Tools settings . 

 Item 

 Options 

 More details 

 Action Mode 

 Enabled 

 Disabled (default) 

 When BAS mode is enabled, BAS tools will receive special handling. Only the simulation itself is terminated. 

 When BAS mode is disabled, BAS tools are treated like any other malicious process. Based on the profile settings, BAS tools will face the same prevention measures as all other threats 

 Note 

 When you are actively evaluating with BAS tools, it is recommended to enable the BAS mode setting only for the duration of your evaluation, and for a limited number of agents. 

 Note 

 BAS tools mode with content older than version 1850 cannot be configured, the agent will be treated as Enabled. 

 To save the profile, click Create . 

 What to do next 

 If you are ready to apply your new profile to endpoints, you do this by adding it to a policy rule. If you still need to define other profiles, you can do this later. During policy rule creation or editing, you select the endpoints to which to assign the policy. There are different ways of doing this, such as: 

 Linux 

 Add a new profile and define basic settings. 

 From Cortex XSIAM, select Inventory → Endpoints → Policy Management → Prevention → Profiles . Click +Add Profile , and select whether to create a new profile, or to import a profile from a file. 

 Note 

 New profiles based on imported profiles are added, and do not replace existing ones. 

 Select the Linux platform, and Malware as the profile type. 

 Click Next . 

 For Profile Name , enter a unique name for the profile. The name can contain only letters, numbers, or spaces, and must be no more than 30 characters. The name will be visible from the list of profiles when you configure a policy rule. 

 For Description , to provide additional context for the purpose or business reason for creating the profile, enter a profile description. For example, you might include an incident identification number or a link to a help desk ticket. 

 Configure ELF Execution Examination to analyze ELF files on endpoints and prevent malicious ELF files from being executed. 

 Item 

 Options 

 More details 

 Action Mode 

 Block 

 Report 

 Disabled 

 When the Cortex XDR agent detects attempts to run malware in ELF files, it performs the configured action. 

 Quarantine malicious ELF files 

 Disabled 

 Quarantine WildFire malware verdict 

 Quarantine WildFire and Local Analysis malware verdict 

 By default, the Cortex XDR agent blocks malware from running, but does not quarantine the file. You can enable one of the options to quarantine files, depending on the verdict issuer. 

 Note 

 The Quarantine Malicious ELF Files feature is not available for malware identified on network drives. 

 Action on unknown ELF files to WildFire 

 Allow 

 Run Local Analysis 

 Block 

 Allow : Unknown files are not blocked and local verdicts are not issued for them. 

 Run Local Analysis : The Cortex XDR agent uses embedded machine learning to determine the likelihood that an unknown file is malware, and issues a local verdict for the file. 

 Block : Block unknown files but do not run local analysis. In this case, unknown files remain blocked until the Cortex XDR agent receives an official WildFire verdict. 

 Upload ELF files for cloud analysis 

 Enabled 

 Disabled 

 When enabled, the Cortex XDR agent sends unknown files to Cortex XSIAM, and Cortex XSIAM sends the files to WildFire for analysis. 

 The file types that the Cortex XDR agent analyzes depend on the platform type. WildFire accepts files up to 300 MB in size. 

 Treat Grayware as Malware 

 Enabled 

 Disabled 

 When enabled, Cortex XSIAM treats all grayware with the same Action Mode as configured for malware. 

 When disabled, grayware is considered benign, and is not blocked. 

 Configure Loaded Kernel Modules Examination to determine what Kernel modules have been installed on the endpoint. 

 Item 

 Options 

 More details 

 Action Mode 

 Block 

 Report 

 Disabled 

 When the Cortex XDR agent detects Kernel modules, it performs the configured action. 

 Configure Local File Threat Examination to enable detection of malicious files on the endpoint. 

 Note 

 This module is supported by Cortex XDR agent 8.1.0 and later releases. 

 Item 

 Options 

 More details 

 Action Mode 

 Enabled 

 Disabled 

 When enabled, the Local Threat-Evaluation Engine (LTEE) analyzes the endpoint for PHP files arriving from a web server and generates issues about any malicious PHP scripts. 

 Quarantine Malicious Files 

 Enabled 

 Disabled 

 When enabled, the Cortex XDR agent quarantines malicious files on the endpoint and does not quarantine updated files. 

 Configure On-write file examination to scan and take action on cross-platform files during the write process. 

 Item 

 Options 

 More details 

 ELF files 

 Enabled 

 Disabled 

 When enabled, the Cortex XDR agent monitors for malicious ELF files during the on-write process, and if it finds any, it generates issues and quarantines the files. 

 ELF file examination is based on the extension, only. 

 Portable executable files (Windows) 

 Enabled 

 Disabled 

 When enabled, the Cortex XDR agent monitors for portable executable files during the on-write process, and if it finds any, it generates issues. It can also perform these actions: 

 Quarantine malicious executables : you can enable an option to quarantine files, depending on the verdict. 

 Treat grayware as malware : When enabled, a grayware verdict is considered malware. When disabled, grayware is considered benign. 

 Mach-O files (macOS) 

 Enabled 

 Disabled 

 When enabled, the Cortex XDR agent monitors for malicious Mach-O files during the on-write process, and if it finds any, it generates alerts. It can also perform the following actions: 

 Quarantine malicious executables : you can enable an option to quarantine files, depending on the verdict. 

 Treat grayware as malware : When enabled, a grayware verdict is considered malware. When disabled, grayware is considered benign. 

 Configure On-demand File Examination to scan endpoints for dormant, inactive malware. 

 Note 

 Enabling on-demand scanning will automatically scan these core system directories: /etc , /tmp , /home , /usr , /bin , /sbin , /lib , /var , /opt , /dev , /root , /boot . 

 Item 

 Options 

 More details 

 Periodic Scan 

 Enabled 

 Disabled 

 Note 

 We recommend that you disable scheduled scanning. VDI machine scans are based on the golden image and additional files will be examined upon execution. 

 Periodic scanning enables you to scan endpoints on a recurring basis without waiting for malware to run on the endpoint. When enabled, you can set the time interval (weekly or monthly) and the day and time at which to start scanning. 

 Periodic scanning is persistent, and if the scan is scheduled to start while the endpoint is turned off, the scan will be initiated when the endpoint is turned on again. The scheduling of future scans is not affected by this delay. 

 Note 

 When periodic scanning is enabled in your profile, the Cortex XDR agent initiates an initial scan when it is first installed on the endpoint, regardless of the periodic scanning scheduling time. 

 Scan Timeout 

 Number of hours 

 If a scan exceeds the number of hours configured here, the Cortex XDR agent stops the scan. 

 Scan Additional Directories 

 1. If you want to scan additional directories, click +Add . 

 2. Enter a directory path. Use ? to match a single character or * to match any string of characters in the directory path. 

 3. Press Enter or click the check mark. 

 4. To add additional folders, repeat these steps. 

 Configure the Global Behavioral Threat Protection Rules . These rules can be used to protect endpoints from malicious causality chains. 

 Item 

 Options 

 More details 

 Action Mode 

 Block 

 Report 

 Disabled 

 The Cortex XDR agent protects against malicious causality chains, using behavioral threat protection rules. When the action mode is set to Block , the Cortex XDR agent terminates all processes and threads in the event chain up to the causality group owner (CGO). 

 Quarantine Malicious Files 

 Enabled 

 Disabled 

 When enabled, the Cortex XDR agent quarantines the processes and the artifacts, such as files, related to the CGO. 

 When disabled, the Cortex XDR agent does not quarantine the CGO of an event chain, nor any scripts or files called by the CGO. 

 Configure Credential Gathering Protection to protect endpoints from processes trying to access or steal passwords and other credentials. 

 Item 

 Options 

 More details 

 Action Mode 

 Block 

 Report 

 Disabled 

 The Cortex XDR agent protects against all processes and threads in the event chain up to the credential gathering process or file. 

 When this module is disabled, the Cortex XDR agent does not analyze the event chain and does not block credential gathering. 

 Quarantine Malicious Files 

 Enabled 

 Disabled 

 When enabled, the Cortex XDR agent quarantines the process or file related to the credential gathering event chain. 

 Configure Financial Malware Threat Protection to protect against techniques specific to financial and banking malware. 

 Item 

 Options 

 More details 

 Action Mode 

 Block 

 Report 

 Disabled 

 In a causality chain, when the Cortex XDR agent detects a process that attempts to access or steal financial or banking information, the Cortex XDR agent performs the configured action. 

 Quarantine Malicious Files 

 Enabled 

 Disabled 

 In a causality chain, when the Cortex XDR agent detects a process that attempts to access or steal financial or banking information, the Cortex XDR agent performs the configured action. 

 Configure Cryptominers Protection to protect against attempts to locate or steal cryptocurrencies. 

 Item 

 Options 

 More details 

 Action Mode 

 Block 

 Report 

 Disabled 

 In a causality chain, when the Cortex XDR agent detects a cryptomining process or file, the Cortex XDR agent performs the configured action. 

 Quarantine Malicious Files 

 Enabled 

 Disabled 

 When enabled, the Cortex XDR agent quarantines the process or file detected during a cryptocurrency gathering attempt. 

 Configure Container Escaping Protection to protect against container-escaping attempts. 

 Item 

 Options 

 More details 

 Action Mode 

 Block 

 Report 

 Disabled 

 When the Cortex XDR agent detects container escaping attempts, it performs the configured action. 

 Configure Reverse Shell Protection to prevent attempts to redirect standard input and output streams to network sockets. 

 Item 

 Options 

 More details 

 Action Mode 

 Block 

 Report 

 Disabled 

 When the Cortex XDR agent detects attempts to redirect standard input and output streams to network sockets, it performs the configured action. 

 Configure Anti Webshell Protection to protect endpoint processes from dropping malicious web shells. 

 Item 

 Options 

 More details 

 Action Mode 

 Block 

 Report 

 Disabled 

 In a causality chain, when the Cortex XDR agent detects a process that attempts to drop malicious web shells, it performs the configured action. 

 Quarantine Malicious Files 

 Enabled 

 Disabled 

 When enabled, the Cortex XDR agent quarantines the processes or files that are related to the web shell drop event chain, and any scripts or files called by the web shell dropping process. 

 Configure Malicious Child Process Protection to prevent process creation based on examination of suspicious relations between parent and child processes. For this option, we support User Mode, and Kernel Mode for kernel versions 4.4 and later. 

 Item 

 Options 

 More details 

 Action Mode 

 Block 

 Report 

 Disabled 

 When the Cortex XDR agent detects known suspicious parent-child relationships that are used to bypass security, the Cortex XDR agent performs the configured action. When Block is selected, known suspicious child processes are blocked from starting. 

 Quarantine Malicious Files 

 Enabled 

 Disabled 

 When enabled, the Cortex XDR agent quarantines the files that are related to a malicious child process. 

 Configure Breach and Attack Simulation (BAS) Tools settings . 

 Item 

 Options 

 More details 

 Action Mode 

 Enabled 

 Disabled (default) 

 When BAS mode is enabled, BAS tools will receive special handling. Only the simulation itself is terminated. 

 When BAS mode is disabled, BAS tools are treated like any other malicious process. Based on the profile settings, BAS tools will face the same prevention measures as all other threats 

 Note 

 When you are actively evaluating with BAS tools, it is recommended to enable the BAS mode setting only for the duration of your evaluation, and for a limited number of agents. 

 Note 

 BAS tools mode with content older than version 1850 cannot be configured, the agent will be treated as Enabled. 

 To save the profile, click Create . 

 What to do next 

 If you are ready to apply your new profile to endpoints, you do this by adding it to a policy rule. If you still need to define other profiles, you can do this later. During policy rule creation or editing, you select the endpoints to which to assign the policy. There are different ways of doing this, such as: 

 Android 

 Add a new profile and define basic settings. 

 From Cortex XSIAM, select Inventory → Endpoints → Policy Management → Prevention → Profiles . Click +Add Profile , and select whether to create a new profile, or to import a profile from a file. 

 Note 

 New profiles based on imported profiles are added, and do not replace existing ones. 

 Select the Android platform, and Malware as the profile type. 

 Click Next . 

 For Profile Name , enter a unique name for the profile. The name can contain only letters, numbers, or spaces, and must be no more than 30 characters. The name will be visible from the list of profiles when you configure a policy rule. 

 For Profile Name , enter a unique name for the profile. The name can contain only letters, numbers, or spaces, and must be no more than 30 characters. The name will be visible from the list of profiles when you configure a policy rule. 

 Configure APK Files Examination , to analyze and prevent malicious APK files from running on endpoints. 

 Note 

 From Cortex XDR agent for Android version 9.0 and later, part of this module, which performs local analysis on the Android device itself, is deprecated. APK analysis will be handled only by Wildfire. 

 Item 

 Options 

 More details 

 Action Mode 

 Block 

 Report 

 Disabled 

 When the Cortex XDR agent detects attempts to run malicious APK files, it performs the configured action. 

 Action on unknown APK files to WildFire 

 Allow 

 Run Local Analysis 

 Block 

 Allow : Unknown files are not blocked and local verdicts are not issued for them. 

 Run Local Analysis : The Cortex XDR agent uses embedded machine learning to determine the likelihood that an unknown file is malware, and issues a local verdict for the file. 

 Block : Block unknown files but do not run local analysis. In this case, unknown files remain blocked until the Cortex XDR agent receives an official WildFire verdict. 

 Upload APK files for cloud analysis 

 Enabled 

 Disabled 

 When enabled, the Cortex XDR agent sends unknown files to Cortex XSIAM, and Cortex XSIAM sends the files to WildFire for analysis. 

 The file types that the Cortex XDR agent analyzes depend on the platform type. WildFire accepts files up to 300 MB in size. 

 Treat Grayware as Malware 

 Enabled 

 Disabled 

 When enabled, Cortex XSIAM treats all grayware with the same Action Mode as configured for malware. 

 When enabled, Cortex XSIAM treats all grayware with the same Action Mode as configured for malware. 

 To save the profile, click Create . 

 What to do next 

 If you are ready to apply your new profile to endpoints, you do this by adding it to a policy rule. If you still need to define other profiles, you can do this later. During policy rule creation or editing, you select the endpoints to which to assign the policy. There are different ways of doing this, such as: 

 iOS 

 Add a new profile and define basic settings. 

 Select Inventory → Endpoints → Policy Management → Prevention → Profiles . Click +Add Profile , and select whether to create a new profile, or to import a profile from a file. 

 Note 

 New profiles based on imported profiles are added, and do not replace existing ones. 

 Select the iOS platform, and Malware as the profile type. 

 Click Next . 

 For Profile Name , enter a unique name for the profile. The name can contain only letters, numbers, or spaces, and must be no more than 30 characters. The name will be visible from the list of profiles when you configure a policy rule. 

 For Description , to provide additional context for the purpose or business reason for creating the profile, enter a profile description. For example, you might include a case identification number or a link to a help desk ticket. 

 Configure URL filtering to analyze and block or report malicious URLs, and to block or allow custom URLs. 

 Note 

 Blocking functionality is different for each security module. For SMS/MMS, Cortex XDR agent will move detected messages containing such URLs from unknown senders to the Junk folder. 

 Item 

 Options 

 More details 

 Action Mode 

 Block 

 Report 

 Disabled 

 When the Cortex XDR agent detects malicious URLs, the Cortex XDR agent performs the configured action. 

 To add numbers to the Block List , click +Add and enter the URL. Press Enter to add more URLs. 

 To add URLs to the Allow List , define a list on the Legacy Agent Exceptions page. 

 Configure Spam Reports to report calls and messages as spam. 

 Item 

 Options 

 More details 

 Spam Report 

 Enabled 

 Disabled 

 Configure reporting of spam calls and messages to Cortex analysts. 

 Configure Call and Messages Blocking for incoming calls and messages from known spam numbers. 

 Item 

 Options 

 More details 

 Action Mode 

 Block 

 Report 

 Disabled 

 When the Cortex XDR agent detects incoming calls or messages from known spam numbers, the Cortex XDR agent performs the configured action. 

 To add numbers to the Block List , click +Add and enter the phone number. Press Enter to add more numbers. 

 To add numbers to the Allow List , define a list on the Legacy Agent Exceptions page. 

 Note 

 Ensure that the same numbers are not added multiple times with different leading zeros. 

 Configure Safari Browser Security Module . This security module can provide proactive gating of suspicious sites accessed using Safari, and provides informative site analysis to the device user. This option is recommended for iOS devices that do not belong to your organization and do not use the Network Shield feature. 

 Note 

 To fully enable the Safari browser security module on the device side, each iOS device user must enable the Safari Safeguard module on the device, and grant it permission to work on all websites. If the iOS device user does not do this, the endpoint's operation status is reported as Partially Protected . 

 The Safari browser security module will only function when the URL filtering module (see earlier in this procedure) is set to Block . 

 Item 

 Options 

 More details 

 Enforce use of Safari Security Module 

 Enabled 

 Disabled 

 When set to Enabled , the Safari Safeguard security module displays "Required" on the Modules screen of the app. Full protection for Safari will only be active after the iOS device user has also activated it on the device. When this module is also activated on the device, issue notifications are forwarded to the tenant. 

 When set to Disabled , and users decide to enable the module on their devices, issue notifications are visible locally on the iOS device only, and are not forwarded to the tenant. 

 Safari malicious JS blocking 

 Enabled 

 Disabled 

 When set to Enabled , the Cortex XDR agent blocks the entire page in Safari where malicious JS files are detected. 

 Configure Network and EDR Security Module . This module lets you configure granular control and monitoring of network traffic on iOS-based supervised devices. The devices' profiles must be also configured for this on the MDM side as explained in the Cortex XDR Agent iOS Guide. 

 Note 

 Cortex XDR agent version 8.4 or higher are required for this feature. 

 Item 

 Options 

 More details 

 Auto detected malicious URL filtering 

 Enabled 

 Disabled 

 When set to Enabled , the Cortex XDR agent automatically filters known malicious URLs. 

 URL filtering 

 Enabled 

 Disabled 

 When set to Enabled , the Cortex XDR agent filters URLs according to the lists of allowed and blocked URLs configured in the URL Filtering section above. 

 Predefined Blocked Apps 

 List of apps 

 A list of commonly known apps that your organization may be interested in blocking on supervised devices is provided here. The Cortex XDR agent will block use of the selected apps. You can select one or more apps. 

 Blocked Bundle IDs 

 A Bundle ID is an app's unique identifier, in string format, that is used to identify the app in an app store. Communication will be blocked for any process with exactly the Bundle ID defined here, or for a Bundle ID that has the defined string as a suffix. 

 For example, the Calculator app's Bundle ID is: com.apple.calculator. When you add com.apple.calculator to the list, the Cortex XDR agent app will block all of these Bundle IDs: 

 com.apple.calculator 

 H3DT34.com.apple.calculator 

 widget.com.apple.calculator 

 To block apps according to Bundle ID, enter a Bundle ID and press Enter. To add another Bundle ID to the list, click +Add and repeat this process. 

 Block List of Remote IPV4/IPV6 IP Address 

 The Cortex XDR agent will block the IP addresses that you add to this field. Both IPV4 and IPv6 addresses are supported. 

 To block apps according to IP address, enter an IP address with a subnet mask, a range, or an individual IP address, and press Enter. To add another IP address to the list, click +Add and repeat this process. 

 Digest issues 

 Enabled 

 Disabled 

 Digest issues are issues that contain a summary of blocked network activity over a prolonged time period. 

 When set to Enabled , the Cortex XDR agent sends a digest to the tenant. 

 Digest issues max frequency 

 1 to 7 days 

 When Digest issues is enabled, you can limit the digest to no more than one per <selected number of days>. 

 Max issues per app 

 Hours 

 Minutes 

 Limit issue notifications by the Cortex XDR agent app to one issue for each app per <selected period of time>. 

 Max user notifications 

 Hours 

 Limit issue notifications by the Cortex XDR agent app to one user notification per <selected number of hours>. 

 To save the profile, click Create . 

 Previous Set up endpoint profiles and exception rules Next Set up exploit prevention profiles 

 Last updated 22 days ago 

 Was this helpful? 

 ‍ 

 Trust Center 

 ‍ 

 Privacy 

 ‍ 

 Terms of Use 

 ‍ 

 Legal 

 © 2026 Palo Alto Networks, Inc. All rights reserved. 

 Was this helpful?

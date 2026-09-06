---
url: https://cortex-docs.paloaltonetworks.com/cortex-xdr-3.x/cortex-xdr-3.x-documentation/endpoint-security/install-and-manage-endpoints/set-up-endpoint-protection/set-up-endpoint-profiles-and-exception-rules/set-up-exception-profiles-and-rules/add-a-legacy-exception-rule
fetched_at: 2026-09-06T09:48:16Z
source: cortex-platform
---

# Add a legacy exception rule | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XDR 

 Cortex XDR 3.x Documentation 

 Cortex XDR 3.x Documentation 

 Endpoint security 

 Install and manage endpoints 

 Set up endpoint protection 

 Set up endpoint profiles and exception rules 

 Set up exception profiles and rules 

 Add a legacy exception rule 

 Learn how to use Cortex XDR Legacy Exception rules to configure an exception to prevention and protection modules on endpoints for selected profiles. 

 Legacy Exception rules enable you to configure an exception to prevention and protection modules on endpoints for selected profiles. 

 Items included in allow lists may continue to generate Cortex XDR security events. If you want to exclude event reporting, configure this on the Alert Exclusions page ( Settings → Exception Configurations → Alert Exclusions ). 

 Keep in mind the following: 

 Prior to Cortex XDR version 3.5, legacy exceptions were configured through profiles. 

 Starting with version 3.5, Cortex XDR enables you to manage the malware security exceptions from a central location and easily apply them across multiple profiles in the Legacy Agent Exceptions Management page. 

 To manage the prevention profile exceptions from Exception Configuration , you must first migrate your existing exceptions configured via the prevention profiles. 

 Your migrated rules are displayed on the Settings → Exception Configurations → Legacy Agent Exceptions page. For more information about the migration, see Exception configuration . 

 Select Settings → Exception Configurations → Legacy Agent Exceptions , and then click + Add Rule . 

 Select the platform for which you want to create an agent exception. 

 Select the module for which you want to create an exception. 

 For each module, specify the following parameters: 

 Type 

 Module 

 Platform 

 Parameters 

 Malware 

 Respond to Malicious Causality Chains 

 Windows, 

 MacOS 

 Add to your allow list specific and known safe IP address or IP address ranges that you do not want Cortex XDR to block. 

 Behavioral Threat Protection 

 Windows, MacOS, Linux 

 Add to your allow list the file or folder path you want to exclude from evaluation. Use ? to match a single character or * to match any string of characters. 

 Office Files with Macros Examination 

 Windows 

 Add to your allow list the file or folder path you want to exclude from evaluation. Use ? to match a single character or * to match any string of characters. 

 Portable Executable and DLL Examination 

 Windows 

 Add to your allow list the file or folder path and the signers you want to exclude from evaluation. Use ? to match a single character or * to match any string of characters. 

 Malicious Child Process Protection 

 Windows, MacOS, Linux 

 Add to your allow list the parent processes that can launch child processes to your allow list with optional execution criteria. Specify the allow list criteria including the Parent Process Name , Child Process Name , and Command Line Params . Use ? to match a single character or * to match any string of characters. 

 Endpoint Scanning 

 Windows, MacOS, Linux 

 Add to your allow list the file or folder path and the signers you want to exclude from evaluation. Use ? to match a single character or * to match any string of characters. 

 PDF Examination 

 Windows 

 Add to your allow list the file or folder paths to exclude from evaluation. Use ? to match a single character or * to match any string of characters. 

 Credential Gathering Protection 

 Windows, MacOS, Linux 

 Add to your allow list the file or folder paths to exclude from evaluation. Use ? to match a single character or * to match any string of characters. 

 Anti Webshell Protection 

 Windows, MacOS, Linux 

 Add to your allow list the file or folder paths to exclude from evaluation. Use ? to match a single character or * to match any string of characters. 

 Financial Malware Threat Protection 

 Windows, MacOS, Linux 

 Add to your allow list the file or folder paths to exclude from evaluation. Use ? to match a single character or * to match any string of characters. 

 Cryptominers Protection 

 Windows, MacOS, Linux 

 Add to your allow list the file or folder paths to exclude from evaluation. Use ? to match a single character or * to match any string of characters. 

 In-process Shellcode Protection 

 Windows 

 Add to your allow list the file or folder paths to exclude from evaluation. Use ? to match a single character or * to match any string of characters. 

 Malicious Device Prevention 

 Windows 

 Add to your allow list the file or folder paths to exclude from evaluation. Use ? to match a single character or * to match any string of characters. 

 UAC Bypass Prevention 

 Windows 

 Add to your allow list the file or folder paths to exclude from evaluation. Use ? to match a single character or * to match any string of characters. 

 Anti Tampering Protection 

 Windows, MacOS 

 Add to your allow list the file or folder paths to exclude from evaluation. Use ? to match a single character or * to match any string of characters. 

 UEFI Protection 

 Windows 

 Add to your allow list the file or folder paths to exclude from evaluation. Use ? to match a single character or * to match any string of characters. 

 PowerShell Script Files 

 Windows 

 Add to your allow list the file or folder paths to exclude from evaluation. Use ? to match a single character or * to match any string of characters. 

 Mach-O Execution Examination 

 MacOS 

 Add to your allow list the file or folder paths to exclude from evaluation. Use ? to match a single character or * to match any string of characters. 

 Mach-O Loading Examination 

 MacOS 

 Add to your allow list the file or folder paths to exclude from evaluation. Use ? to match a single character or * to match any string of characters. 

 DMG File Examination 

 MacOS 

 Add to your allow list the file or folder paths to exclude from evaluation. Use ? to match a single character or * to match any string of characters. 

 Local File Threat Examination 

 Linux 

 Add to your allow list the file or folder paths to exclude from evaluation. Use ? to match a single character or * to match any string of characters. 

 ELF File Examination 

 Linux 

 Add to your allow list the file or folder paths to exclude from evaluation. Use ? to match a single character or * to match any string of characters. 

 Reverse Shell Protection 

 Linux 

 Specify the Process Path . Local IP Address and port, and the Remote IP Address and port of the process you want to allow. Use ? to match a single character or * to match any string of characters. 

 APK Files Examination 

 Android 

 Specify the signers you want to exclude from evaluation. Use ? to match a single character or * to match any string of characters. 

 SMS and MMS Malicious URL filtering Allow list 

 iOS 

 Add to your allow list and known safe URLs that you do not want Cortex XDR to block. 

 Call and Messages Blocking Allow list 

 iOS 

 Add to your allow list names and phone numbers of contacts that you do not want Cortex XDR to block. 

 Dynamic Kernel Protection 

 Windows 

 Add to your allow list the file or folder path you want to exclude from evaluation. Use ? to match a single character or * to match any string of characters. 

 ASP and ASPX File Examination 

 Windows 

 Add to your allow list the file or folder paths to exclude from evaluation. Use ? to match a single character or * to match any string of characters. 

 VB Scripts Examination 

 Windows 

 Add to your allow list the file or folder paths to exclude from evaluation. Use ? to match a single character or * to match any string of characters. 

 JScript File Examination 

 Windows 

 Add to your allow list the file or folder paths to exclude from evaluation. Use ? to match a single character or * to match any string of characters. 

 LDAP Query Protection 

 Windows 

 Add to your allow list specific and known safe IP address or IP address ranges that you do not want Cortex XDR to block. 

 Add to your allow list users whom you do not want to block. 

 Portable executable files (Windows) 

 Linux 

 Add to your allow list the file or folder paths to exclude from evaluation. Use ? to match a single character or * to match any string of characters. 

 Mach-O files (macOS) 

 Linux 

 Add to your allow list the file or folder paths to exclude from evaluation. Use ? to match a single character or * to match any string of characters. 

 Restrictions 

 Executable Files 

 Windows 

 Add to your allow list the file or folder paths to exclude from evaluation. Use ? to match a single character or * to match any string of characters. 

 Network Location Files 

 Windows 

 Add to your allow list the file or folder paths to exclude from evaluation. Use ? to match a single character or * to match any string of characters. 

 Optical Drive Files 

 Windows 

 Add to your allow list the file or folder paths to exclude from evaluation. Use ? to match a single character or * to match any string of characters. 

 Removable Media Files 

 Windows 

 Add to your allow list the file or folder paths to exclude from evaluation. Use ? to match a single character or * to match any string of characters. 

 Exceptions 

 Process Exceptions 

 Windows, MacOS, Linux 

 Add to your allow list the process and the module names to exclude from evaluation. Use ? to match a single character or * to match any string of characters. 

 Operational Agent Exceptions 

 Windows 

 This option excludes any intervention from a given list of processes, which are specified by their full path. 

 When you create this exception rule, it will disable the following modules: 

 All anti-exploitation modules for the process. 

 All anti-malware modules, by disabling triggers such as on-execution, on-load, on-access, on-write, and on-demand. 

 * Most event collection operations based on tracking the process (*some event collection operations might still occur, such as process events). 

 Perform these steps: 

 1. For Target Properties Process Path , enter the path of the process that you want to exclude, and press ENTER. To add additional processes, repeat this step. 

 2. For Scope , select a rule scope. 

 Global : Apply this rule to all profiles 

 Profiles (existing or new): Apply this rule to a specific profile, or to multiple profiles. You can create a new profile from here, if necessary. 

 3. Go to step 6. 

 Select all to apply the exception to all profiles for this module or select specific profiles. 

 Click Next . 

 Review the rule conditions, and when you are done, select the checkbox for I understand the risk . 

 Click Create . 

 Important 

 If you don't migrate the legacy exceptions, you can continue to create exceptions through the profiles. 

 Add a new exceptions security profile 

 Add a global endpoint policy exception 

 Set up exploit prevention profiles 

 Set up malware prevention profiles 

 Set up restrictions prevention profiles 

 Previous Add a support exception rule 

 Next Add a new exceptions security profile 

 Last updated 1 month ago 

 Was this helpful?

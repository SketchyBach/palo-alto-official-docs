---
url: https://cortex-docs.paloaltonetworks.com/cortex-cloud-runtime-security/endpoint-security/endpoint-protection/file-analysis-and-protection-flow
fetched_at: 2026-09-16T08:44:33Z
source: cortex-platform
---

# File analysis and protection flow | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex Cloud 

 Cortex CLOUD Runtime Security 

 Endpoint security 

 Endpoint protection 

 Cortex Cloud Runtime 

 File analysis and protection flow 

 The Cortex XDR agent utilizes advanced multi-method protection and prevention techniques to protect from both known and unknown malware and software exploits. 

 The Cortex XDR agent utilizes advanced multi-method protection and prevention techniques to protect your endpoints from both known and unknown malware and software exploits. 

 Exploit protection for protected processes 

 In a typical attack scenario, an attacker attempts to gain control of a system by first corrupting or bypassing memory allocation or handlers. Using memory-corruption techniques, such as buffer overflows and heap corruption, a hacker can trigger a bug in the software or exploit a vulnerability in a process. The attacker must then manipulate a program to run code provided or specified by the attacker while evading detection. If the attacker gains access to the operating system, the attacker can then upload malware, such as Trojan horses (programs that contain malicious executable files), or can otherwise use the system to their advantage. The Cortex XDR agent prevents such exploit attempts by employing roadblocks—or traps—at each stage of an exploitation attempt. 

 end-c1.png 

 When a user opens a non-executable file, such as a PDF or Word document, and the process that opened the file is protected, the Cortex XDR agent seamlessly injects code into the software. This occurs at the earliest possible stage before any files belonging to the process are loaded into memory. The Cortex XDR agent then activates one or more protection modules inside the protected process. Each protection module targets a specific exploitation technique and is designed to prevent attacks on program vulnerabilities based on memory corruption or logic flaws. 

 In addition to automatically protecting processes from such attacks, the Cortex XDR agent reports any security events to Cortex Cloud and performs additional actions as defined in the endpoint security policy. Common actions performed by the Cortex XDR agent include collecting forensic data and notifying the user about the event. 

 The default endpoint security policy protects the most vulnerable and most commonly used applications but you can also add other third-party and proprietary applications to the list of protected processes. 

 Malware Protection 

 The Cortex XDR agent provides malware protection in a series of four evaluation phases: 

 end-c2.png 

 Phase 1: Evaluation of child process protection policy 

 When a user attempts to run an executable, the operating system attempts to run the executable as a process. If the process tries to launch any child processes, the Cortex XDR agent first evaluates the child process protection policy. If the parent process is a known targeted process that attempts to launch a restricted child process, the Cortex XDR agent blocks the child processes from running and reports the security event to Cortex Cloud. For example, if a user tries to open a Microsoft Word document (using the winword.exe process) and the document has a macro that tries to run a blocked child process (such as WScript), the Cortex XDR agent blocks the child process and reports the event to Cortex Cloud. If the parent process does not try to launch any child processes or tries to launch a child process that is not restricted, the Cortex XDR agent next moves to Phase 2: Evaluation of the restriction policy. 

 Phase 2: Evaluation of the restriction policy 

 The Cortex XDR agent verifies that the executable file does not violate any restriction rules. For example, you might have a restriction rule that blocks executable files launched from network locations. If a restriction rule applies to an executable file, the Cortex XDR agent blocks the file from executing and reports the security event to Cortex Cloud and, depending on the configuration of each restriction rule, the Cortex XDR agent can also notify the user about the prevention event. 

 If no restriction rules apply to an executable file, the Cortex XDR agent next moves to Phase 3: Hash verdict determination. 

 Phase 3: Hash verdict determination 

 The Cortex XDR agent calculates a unique hash using the SHA-256 algorithm for every file that attempts to run on the endpoint. Depending on the features that you enable, the Cortex XDR agent performs additional analysis to determine whether an unknown file is malicious or benign. The Cortex XDR agent can also submit unknown files to Cortex Cloud for in-depth analysis by WildFire. 

 Note 

 To enhance performance and efficiency, hash verdict requests from the Cortex XDR agent will be routed to the WildFire service with the lowest latency. File uploads for analysis will strictly adhere to the designated Cortex Cloud and WildFire regions, ensuring data remains within the appropriate geographical boundaries. 

 To determine a verdict for a file, the Cortex XDR agent evaluates the file in the following order: 

 Hash exception : A hash exception enables you to override the verdict for a specific file without affecting the settings in your Malware Security profile. The hash exception policy is evaluated first and takes precedence over all other methods to determine the hash verdict. 

 For example, you may want to configure a hash exception for any of the following situations: 

 You want to block a file that has a benign verdict. 

 You want to allow a file that has a malware verdict to run. In general, we recommend that you only override the verdict for malware after you use available threat intelligence resources—such as WildFire—to determine that the file is not malicious. 

 You want to specify a verdict for a file that has not yet received an official WildFire verdict. 

 After you configure a hash exception, Cortex Cloud distributes it at the next heartbeat communication with any endpoints that have previously opened the file. 

 When a file launches on the endpoint, the Cortex XDR agent first evaluates any relevant hash exception for the file. The hash exception specifies whether to treat the file as malware. If the file is assigned a benign verdict, the Cortex XDR agent permits it to open. 

 If a hash exception is not configured for the file, the Cortex XDR agent next evaluates the verdict to determine the likelihood of malware. 

 Highly trusted signers (Windows and Mac): The Cortex XDR agent distinguishes highly trusted signers such as Microsoft from other known signers. To keep parity with the signers defined in WildFire, Palo Alto Networks regularly reviews the list of highly trusted and known signers and delivers any changes with content updates. The list of highly trusted signers also includes signers that are included in the allow list from Cortex Cloud. When an unknown file attempts to run, the Cortex XDR agent applies the following evaluation criteria: Files signed by highly trusted signers are permitted to run, and files signed by prevented signers are blocked, regardless of the WildFire verdict. Otherwise, when a file is not signed by a highly trusted signer or by a signer included in the block list, the Cortex XDR agent next evaluates the WildFire verdict. For Windows endpoints, evaluation of other known signers takes place if the WildFire evaluation returns an unknown verdict for the file. 

 WildFire verdict : If a file is not signed by a highly trusted signer on Windows and Mac endpoints, the Cortex XDR agent performs a hash verdict lookup to determine if a verdict already exists in its local cache. 

 If the executable file has a malware verdict, the Cortex XDR agent reports the security event to Cortex Cloud , and, depending on the configured behavior for malicious files, the Cortex XDR agent performs one of the following actions. 

 Blocks the file. 

 Blocks and quarantines the file. 

 Notifies the user about the file but still allows the file to execute. 

 Logs the issue without notifying the user and allows the file to execute. 

 If the verdict is benign, the Cortex XDR agent moves on to the next stage of evaluation: Phase 4: Evaluation of Malware Protection Policy. 

 If the hash does not exist in the local cache or has an unknown verdict, the Cortex XDR agent next evaluates whether the file is signed by a known signer. 

 Local analysis : When an unknown executable, DLL, or macro attempts to run on a Windows or Mac endpoint, the Cortex XDR agent uses local analysis to determine if it is likely to be malware. On Windows endpoints, if the file is signed by a known signer, the Cortex XDR agent permits the file to run and does not perform additional analysis. For files on Mac endpoints and files that are not signed by a known signer on Windows endpoints, the Cortex XDR agent performs local analysis to determine whether the file is malware. Local analysis uses a static set of pattern-matching rules that inspect multiple file features and attributes, and a statistical model that was developed with machine learning on WildFire threat intelligence. The model enables the Cortex XDR agent to examine hundreds of characteristics for a file and issue a local verdict (benign or malicious) while the endpoint is offline or Cortex Cloud is unreachable. The Cortex XDR agent can rely on the local analysis verdict until it receives an official WildFire verdict or hash exception. 

 Local analysis is enabled by default in a Malware Security profile. Because local analysis always returns a verdict for an unknown file, if you enable the Cortex XDR agent to Block files with unknown verdict , the agent only blocks unknown files if a local analysis error occurs or local analysis is disabled. To change the default settings (not recommended), see Set up malware prevention profiles . 

 Phase 4: Evaluation of malware security policy 

 If the prior evaluation phases do not identify a file as malware, the Cortex XDR agent observes the behavior of the file and applies additional malware protection rules. If a file exhibits malicious behavior, such as encryption-based activity common with ransomware, the Cortex XDR agent blocks the file and reports the security event to the Cortex Cloud. 

 If no malicious behavior is detected, the Cortex XDR agent permits the file (process) to continue running but continues to monitor the behavior for the lifetime of the process. 

 Previous Exploit protection 

 Next Endpoint protection capabilities 

 Last updated 1 month ago 

 Was this helpful?

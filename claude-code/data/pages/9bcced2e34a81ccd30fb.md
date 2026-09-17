---
url: https://cortex-docs.paloaltonetworks.com/analytics-alerts/alerts-by-name/ldap-traffic-from-non-standard-process
fetched_at: 2026-09-16T09:07:20Z
source: cortex-platform
---

# LDAP traffic from non-standard process | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 Analytics Alerts 

 Alerts by name 

 LDAP traffic from non-standard process 

 Synopsis 

 Field 

 Value 

 Activation Period 

 14 Days 

 Training Period 

 30 Days 

 Test Period 

 N/A (single event) 

 Deduplication Period 

 1 Day 

 Required Data 

 XDR Agent 

 ATT&CK Tactic 

 Discovery (TA0007) 

 ATT&CK Technique 

 Account Discovery (T1087) 

 Severity 

 Informational 

 Description 

 LDAP traffic is usually performed by a standard set of processes. The endpoint had a non-standard process communicating over ports normally used by LDAP. This may be indicative of Active Directory domain enumeration, which may be used during attacks against the organization. 

 Attacker's Goals 

 An attacker is attempting to enumerate Active Directory. 

 Investigative actions 

 Make sure the process is not a scanner that implements its version of the protocol, and that the scanner use is for sanctioned purposes. For example, nmap enumerating LDAP. 

 Make sure the process is not a sanctioned security product that creates standalone binaries for its use. For example, Illusive Network honeypots. 

 Investigate the process to see if the high-level language used to implement the application is the source of the alert. Some high-level programming languages provide their protocol implementations. 

 Examine the endpoint to see if it is infected with malware. If the parent-child chain of initiating processes has been infiltrated with a malicious replacement, then that replacement could be known malware. 

 Variations 
 LDAP traffic from reverse SSH tunnel 

 Synopsis 

 Field 

 Value 

 ATT&CK Tactic 

 Discovery (TA0007) 

 ATT&CK Technique 

 Account Discovery (T1087) 

 Severity 

 Medium 

 Description 

 LDAP traffic is usually performed by a standard set of processes. The endpoint had a non-standard process communicating over ports normally used by LDAP. This may be indicative of Active Directory domain enumeration, which may be used during attacks against the organization. 

 Attacker's Goals 

 An attacker is attempting to enumerate Active Directory. 

 Investigative actions 

 Make sure the process is not a scanner that implements its version of the protocol, and that the scanner use is for sanctioned purposes. For example, nmap enumerating LDAP. 

 Make sure the process is not a sanctioned security product that creates standalone binaries for its use. For example, Illusive Network honeypots. 

 Investigate the process to see if the high-level language used to implement the application is the source of the alert. Some high-level programming languages provide their protocol implementations. 

 Examine the endpoint to see if it is infected with malware. If the parent-child chain of initiating processes has been infiltrated with a malicious replacement, then that replacement could be known malware. 

 LDAP traffic from non-standard and uncommon process 

 Synopsis 

 Field 

 Value 

 ATT&CK Tactic 

 Discovery (TA0007) 

 ATT&CK Technique 

 Account Discovery (T1087) 

 Severity 

 Low 

 Description 

 LDAP traffic is usually performed by a standard set of processes. The endpoint had a non-standard process communicating over ports normally used by LDAP. This may be indicative of Active Directory domain enumeration, which may be used during attacks against the organization. 

 Attacker's Goals 

 An attacker is attempting to enumerate Active Directory. 

 Investigative actions 

 Make sure the process is not a scanner that implements its version of the protocol, and that the scanner use is for sanctioned purposes. For example, nmap enumerating LDAP. 

 Make sure the process is not a sanctioned security product that creates standalone binaries for its use. For example, Illusive Network honeypots. 

 Investigate the process to see if the high-level language used to implement the application is the source of the alert. Some high-level programming languages provide their protocol implementations. 

 Examine the endpoint to see if it is infected with malware. If the parent-child chain of initiating processes has been infiltrated with a malicious replacement, then that replacement could be known malware. 

 LDAP traffic from non-standard process executed under an unsigned causality actor in a commonly abused directory 

 Synopsis 

 Field 

 Value 

 ATT&CK Tactic 

 Discovery (TA0007) 

 ATT&CK Technique 

 Account Discovery (T1087) 

 Severity 

 Low 

 Description 

 LDAP traffic is usually performed by a standard set of processes. The endpoint had a non-standard process communicating over ports normally used by LDAP. This may be indicative of Active Directory domain enumeration, which may be used during attacks against the organization. 

 Attacker's Goals 

 An attacker is attempting to enumerate Active Directory. 

 Investigative actions 

 Make sure the process is not a scanner that implements its version of the protocol, and that the scanner use is for sanctioned purposes. For example, nmap enumerating LDAP. 

 Make sure the process is not a sanctioned security product that creates standalone binaries for its use. For example, Illusive Network honeypots. 

 Investigate the process to see if the high-level language used to implement the application is the source of the alert. Some high-level programming languages provide their protocol implementations. 

 Examine the endpoint to see if it is infected with malware. If the parent-child chain of initiating processes has been infiltrated with a malicious replacement, then that replacement could be known malware. 

 LDAP traffic from an injected thread within a non-standard process 

 Synopsis 

 Field 

 Value 

 ATT&CK Tactic 

 Discovery (TA0007) 

 ATT&CK Technique 

 Account Discovery (T1087) 

 Severity 

 Low 

 Description 

 LDAP traffic is usually performed by a standard set of processes. The endpoint had a non-standard process communicating over ports normally used by LDAP. This may be indicative of Active Directory domain enumeration, which may be used during attacks against the organization. 

 Attacker's Goals 

 An attacker is attempting to enumerate Active Directory. 

 Investigative actions 

 Make sure the process is not a scanner that implements its version of the protocol, and that the scanner use is for sanctioned purposes. For example, nmap enumerating LDAP. 

 Make sure the process is not a sanctioned security product that creates standalone binaries for its use. For example, Illusive Network honeypots. 

 Investigate the process to see if the high-level language used to implement the application is the source of the alert. Some high-level programming languages provide their protocol implementations. 

 Examine the endpoint to see if it is infected with malware. If the parent-child chain of initiating processes has been infiltrated with a malicious replacement, then that replacement could be known malware. 

 Previous LDAP search query from an unpopular and unsigned process 

 Next Linux local user account creation 

 Was this helpful?

---
url: https://docs.paloaltonetworks.com/content/techdocs/en_US/network-security/security-policy/administration/security-rules/create-a-security-policy-rule/create-a-security-policy-rule-panorama.html
fetched_at: 2026-09-16T09:58:34Z
source: palo-alto-main
---

# Create a Security Policy Rule (PAN-OS & Panorama)  Clear

Updated on 

 Fri Aug 07 10:46:39 PDT 2026 

 Focus 

 Home 

 Network Security 

 Network Security: Security Policy 

 Security Policy Rules 

 Create a Security Policy Rule 

 Create a Security Policy Rule (PAN-OS & Panorama) 

 Download PDF 

 Network Security 

 Create a Security Policy Rule (PAN-OS & Panorama) 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Network Security Docs 

 Security Policy 

 IPsec VPN 

 Decryption 

 Device-ID 

 Quantum Security 

 Quality of Service 

 Create a Security Policy Rule (PAN-OS & Panorama) 

 Learn how to create a security rule. 

 To ensure that end users authenticate when they try to access your network
 resources, authentication is evaluated before Security policy. For details, see
 Authentication Policy . 

 The interface includes components for defining Security rules. Familiarize yourself with them before you get started. 

 ( Optional ) Delete the default Security rule. 

 By default, the firewall includes a security rule named rule1 
 that allows all traffic from Trust zone to Untrust zone. You can either
 delete the rule or modify the rule to reflect your zone naming
 conventions. 

 Add a rule. 

 Select Policies Security and Add a new rule. 

 In the General tab, enter a descriptive
 Name for the rule. 

 Select a Rule Type . 

 Define the matching criteria for the source fields in the packet. 

 In the Source tab, select a Source
 Zone . 

 Specify a Source IP Address or leave the value
 set to any . You can optionally specify the source
 as an External Dynamic List with a curated list
 of IP addresses or a Region using IP addresses
 that have been mapped to a country code based on a Palo Alto Networks
 managed internal database. 

 If you decide to Negate a region as a Source
 Address , ensure that all regions that
 contain private IP addresses are added to the
 Source Address to avoid
 connectivity loss between those private IP
 addresses. 

 (Available in PAN-OS 12.1 and later) If your network
 operates using IPv6 (or a dual stack deployment) and
 would like to use IPv6 geolocation, you must
 Enable IPv6 Firewalling as
 well as Enable IPv6 Geolocation 
 from Device Sessions Session Settings . 

 The following platforms configured with less than 9GB do
 not support IPv6 geolocation: 

 Hardware NGFWs: PA-410, PA-410R, PA-410R-5G,
 PA-415, and PA-415-5G 

 VM-Series: Software NGFW
 Credits and VM-Series
 models with less than 9GB (e.g. VM-100,
 VM-50, etc) 

 Specify a Source User or leave the value set to
 any . 

 Define the matching criteria for the destination fields in the packet. 

 In the Destination tab, set the
 Destination Zone . 

 Specify a Destination IP Address or leave the
 value set to any . You can optionally specify the
 destination as an External Dynamic List with a
 curated list of IP addresses or a Region using IP
 addresses that have been mapped to a country code based on a Palo Alto
 Networks managed internal database. 

 If you decide to Negate a region as the
 Destination Address , ensure
 that all regions that contain private IP addresses are
 added to the Destination Address 
 to avoid connectivity loss between those private IP
 addresses. 

 (Available in PAN-OS 12.1 and later) If your network
 operates using IPv6 (or a dual stack deployment) and
 would like to use IPv6 geolocation, you must
 Enable IPv6 Firewalling as
 well as Enable IPv6 Geolocation 
 from Device Sessions Session Settings . 

 The following platforms configured with less than 9GB do
 not support IPv6 geolocation: 

 Hardware NGFWs: PA-410, PA-410R, PA-410R-5G,
 PA-415, and PA-415-5G 

 VM-Series: Software NGFW
 Credits and VM-Series
 models with less than 9GB (e.g. VM-100,
 VM-50, etc) 

 As a best practice, use address objects as the
 Destination Address to enable access
 to only specific servers or specific groups of servers
 especially for commonly exploited services, such as DNS and
 SMTP. By restricting users to specific destination server
 addresses, you can prevent data exfiltration and
 command-and-control traffic from establishing communication
 through techniques such as DNS tunneling. 

 Specify the application that the rule will allow or block. 

 As a best practice, always use application-based security rules
 instead of port-based rules and always set the Service to
 application-default unless you're using a more restrictive list of ports
 than the standard ports for an application. 

 In the Applications tab,
 Add the Application 
 you want to safely enable. You can select multiple applications or you
 can use application groups or application filters. 

 In the Service/URL Category tab, keep the
 service set to application-default to ensure that
 any applications that the rule allows are allowed only on their standard
 ports. 

 ( Optional ) Specify a URL category as match criteria for the
 rule. 

 In the Service/URL Category tab, select the
 URL Category . 

 If you select a URL category, only web traffic will match the rule and only
 if the traffic is destined for that specified category. 

 Define what action you want the firewall to take for traffic that matches the
 rule. 

 In the Actions tab, select an
 Action . See Security Rule Actions for a description of each
 action. 

 Configure the log settings. 

 By default, the rule is set to Log at Session
 End . You can disable this setting if you don’t want any logs
 generated when traffic matches this rule or you can select
 Log at Session Start for more detailed
 logging. 

 Select a Log Forwarding profile. 

 As a best practice, don't select the check box to Disable
 Server Response Inspection (DSRI). Selecting this option
 prevents the firewall from inspecting packets from the server to the
 client. For the best security posture, the firewall must inspect both
 the client-to-server flows and the server-to-client flows to detect and
 prevent threats. 

 For information about when sessions may not appear in logs and when to enable
 session start logging, see Session Logging Considerations . 

 Attach security profiles to enable the firewall to scan all allowed traffic for
 threats. 

 Make sure you create best practice security
 profiles that help protect your network from both known and
 unknown threats. 

 In the Actions tab, select
 Profiles from the Profile
 Type drop-down and then select the individual security
 profiles to attach to the rule. 

 Alternatively, select Group from the
 Profile Type drop-down and select a security
 Group Profile to attach. 

 Click Commit to save the security rule to the running
 configuration on the firewall. 

 To verify that you have set up your basic Security policies effectively, test
 whether your security rules are being evaluated and determine which
 security rule applies to a traffic flow. 

 The output displays the best rule that matches the source and destination IP
 address specified in the CLI command. 

 For example, to verify the security rule that will be applied for a server in
 the data center with the IP address 208.90.56.11 when it accesses the
 Microsoft update server: 

 Select Device Troubleshooting , and select Security Policy Match 
 from the Select Test drop-down. 

 Enter the Source and Destination IP addresses. 

 Enter the Protocol. 

 Execute the Security policy match test. 

 After waiting long enough to allow traffic to pass through the firewall, View Security Rule Usage to monitor the
 security rule usage status and determine the effectiveness of the policy
 rule.

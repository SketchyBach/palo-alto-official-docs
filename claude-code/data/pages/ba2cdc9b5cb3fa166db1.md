---
url: https://docs.paloaltonetworks.com/vm-series/deployment/private-cloud/set-up-the-vm-series-firewall-on-nsx/deploy-the-vm-series-firewall-on-nsx-t-east-west/apply-policies-to-the-vm-series-firewall-nsx-t-ew
fetched_at: 2026-08-13T17:41:32Z
source: palo-alto-main
---

# Apply Security Policies to the VM-Series Firewall on NSX-T
        (East-West) Clear

Apply Security Policies to the VM-Series Firewall on NSX-T
 (East-West) 

 Home 

 EN

 Location 

 Documentation Home 

 Palo Alto Networks 

 Support 

 Live Community 

 Knowledge Base 

 >

 Strata Copilot

 Apply Security Policies to the VM-Series Firewall on NSX-T
 (East-West) 

 Updated on 

 Fri Jun 19 07:13:50 PDT 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 VM-Series Firewall Docs 

 Activation & Onboarding 

 Getting Started 

 Upgrade 

 Deployment 

 Select a Document 

 Public Cloud 

 Private Cloud 

 Updated on 

 Fri Jun 19 07:13:50 PDT 2026 

 Focus 

 Home 

 VM-Series 

 VM-Series Firewall on VMware NSX-T 

 Deploy the VM-Series Using the Operations-Centric Workflow 

 Apply Security Policies to the VM-Series Firewall on NSX-T
 (East-West) 

 Download PDF 

 VM-Series 

 Apply Security Policies to the VM-Series Firewall on NSX-T
 (East-West) 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 VM-Series Firewall Docs 

 Activation & Onboarding 

 Getting Started 

 Upgrade 

 Deployment 

 Select a Document 

 Public Cloud 

 Private Cloud 

 Previous 

 Direct Traffic to the VM-Series Firewall 

 Next 

 Use vMotion to Move the VM-Series Firewall Between Hosts 

 Apply Security Policies to the VM-Series Firewall on NSX-T
 (East-West) 

 This section describes security policies and its applications. 

 Where Can I Use
 This? What Do I Need? 

 VMware NSX 

 VM-Series Firewall License (BYOL) 

 Panorama 

 VM-Series plugin 

 Panorama plugin for NSX 

 Now that you have created the redirection rules on the NSX-T Manager, you can now use
 Panorama for centrally administering policies on the VM-Series firewalls. 

 To manage centralized policy, attach the Dynamic Address Group as a source or
 destination address in security policy and push it to the firewalls; the firewalls
 can dynamically retrieve the IP addresses of the virtual machines that are included
 in each security group to enforce compliance for traffic that originates from or is
 destined to the virtual machines in the specified group. 

 Log in to Panorama. 

 Create Dynamic Address Groups. 

 Select Objects Address Groups . 

 Select the Device Group you created for managing your VM-Series on the
 NSX-T firewall from the Device Group 
 drop-down. 

 Click Add and enter a
 Name and Description 
 for the Dynamic Address Group. 

 Select Type as
 Dynamic . 

 Add Match Criteria to your Dynamic Address Group. 

 Some browser extensions may block API calls between Panorama and
 NSX-T, which prevents Panorama from receiving match criteria. If
 Panorama displays no match criteria and you're using browser
 extensions, disable the extensions and Synchronize Dynamic
 Objects to populate the tags available to Panorama. 

 Click Add Match Criteria . 

 Select the And or Or 
 operator and click the plus (+) icon next to the security group name to
 add it to the Dynamic Address Group. 

 The security groups that display in the match criteria dialog are
 derived from the groups you defined on the NSX-T Manager. Only the
 groups that are referenced in the security policies and from which
 traffic is redirected to the VM-Series firewall are available
 here. 

 Click OK . 

 Repeat these steps to create the appropriate number of Dynamic Address
 Groups required for your deployment. 

 Commit your changes. 

 Create security policy rules. 

 Select Policies Security Prerules . 

 Select the Device Group that you created for
 managing the VM-Series firewalls on NSX-T in Create Template Stacks and Device Groups on Panorama . 

 Click Add and enter a
 Name and a Description 
 for the rule. In this example, the security rule allows all traffic
 between the WebFrontEnd servers and the Application servers. 

 Select the Source Zone and
 Destination Zone . The zone name must be the
 same in both columns. 

 For the Source Address and
 Destination Address , select or type in an
 address, address group or region. In this example, we select an address
 group, the Dynamic Address Group you created previously. 

 Select the Application to allow. In this
 example, we create an Application Group that
 includes a static group of specific applications that are grouped
 together. 

 Click Add and select New
 Application Group . 

 Click Add to select the application to
 include in the group. 

 Click OK to create the application
 group. 

 Specify the action— Allow or
 Deny —for the traffic, and optionally attach
 the default security profiles for antivirus, antispyware, and
 vulnerability protection, under Profiles. 

 Repeats the steps above to create the pertinent policy rules. 

 Click Commit , select Commit Type as
 Panorama . Click OK . 

 Apply the policies to the VM-Series firewalls for NSX-T. 

 Click Commit , and select Commit Type
 Device Groups . 

 Select the device group, NSX-T Device Group in this example and click
 OK . 

 Verify that the commit is successful. 

 Validate that the members of the Dynamic Address Group are populated on the
 VM-Series firewall. 

 From Panorama, switch device context to launch the web interface of a
 firewall to which you pushed policies. 

 On the VM-Series firewall, select Policies Security , and select a rule. 

 Select the drop-down arrow next to the address group link, and select
 Inspect . You can also verify that the match
 criteria are accurate. 

 Click the more link and verify that the list of
 registered IP addresses is displayed. 

 The policy will be enforced for all IP addresses that belong to this
 address group, and are displayed here. 

 ( Optional ) Use a template to push a base configuration for network and
 device configuration such as DNS server, NTP server, Syslog server, and login
 banner. 

 Refer to the Panorama Administrator’s Guide for
 information on using templates. 

 Create a Zone Protection profile and attach it to a zone. 

 A zone protection profile provides
 flood protection and has the ability to protect against port scanning, port
 sweeps, and packet-based attacks. It allows you to secure intratier and
 inter-tier traffic between virtual machines within your data center and
 traffic from the internet that is destined to the virtual machines
 (workloads) in your data center. 

 Select your Template . 

 Select Network Network Profiles Zone Protection to add and configure a new profile. 

 Select Network Zones , click the default-zone listed and select the profile in
 the Zone Protection Profile drop down. 

 Create a DoS Protection profile and attach it to a DoS Protection policy rule. 

 Select your Device Group . 

 Select Objects Security Profiles DoS Protection to add and configure a new profile. 

 A classified profile allows the creation of a threshold that
 applies to a single source IP. For example, you can
 configure a max session rate for an IP address that matched
 the policy, and then block that single IP address once the
 threshold is triggered. 

 An aggregate profile allows the creation of a max session
 rate for all packets matching the policy. The threshold
 applies to the new session rate for all IP addresses
 combined. Once the threshold is triggered, it affects all
 traffic that matches the policy. 

 Create a new DoS Protection policy rule in Policy DoS Protection, and attach the new profile to it. 

 Previous 

 Direct Traffic to the VM-Series Firewall 

 Next 

 Use vMotion to Move the VM-Series Firewall Between Hosts 

 On This Page 

 Activation and Onboarding 

 Strata Cloud Manager 

 Next-Generation Firewalls 

 Firewalls 

 PAN-OS 

 PAN-OS SD-WAN 

 VM-Series 

 Plugins 

 Cloud-Delivered Security Services 

 Advanced WildFire 

 Advanced URL Filtering 

 Advanced Threat Prevention 

 Advanced DNS Security 

 AI Access Security 

 Device Security 

 Enterprise DLP 

 SaaS Security 

 Network Security 

 Shared Policy for NGFWs and Prisma Access 

 IPSec VPN 

 Security Policy 

 Quantum Security 

 Endpoints 

 GlobalProtect 

 Resources 

 All Release Notes 

 Compatibility Matrix 

 Experts Corner 

 Network Security 

 Deployment 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

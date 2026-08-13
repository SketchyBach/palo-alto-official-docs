---
url: https://docs.paloaltonetworks.com/vm-series/deployment/private-cloud/set-up-the-vm-series-firewall-on-nsx/deploy-the-vm-series-using-the-security-centric-workflow/create-dynamic-address-group-membership-criteria
fetched_at: 2026-08-13T17:41:34Z
source: palo-alto-main
---

# Create Dynamic Address Group Membership Criteria Clear

Create Dynamic Address Group Membership Criteria 

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

 Create Dynamic Address Group Membership Criteria 

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

 Deploy the VM-Series Using the Security-Centric Workflow 

 Create Dynamic Address Group Membership Criteria 

 Download PDF 

 VM-Series 

 Create Dynamic Address Group Membership Criteria 

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

 Apply Security Policies to the VM-Series Firewall on NSX-T (East-West) 

 Next 

 Generate Steering Policy 

 Create Dynamic Address Group Membership Criteria 

 Learn how to create Dynamic Address Group Membership Criteria. 

 Where Can I Use
 This? What Do I Need? 

 VMware NSX 

 VM-Series Firewall License (BYOL) 

 Panorama 

 VM-Series plugin 

 Panorama plugin for NSX 

 In NSX-T, you can configure the membership criteria for your virtual machines and IP set
 belonging to an NSX-T security group (Dynamic Address Group) in the Panorama plugin
 for NSX. For each Dynamic Address Group, you must specify a service definition and
 define up to five match criteria and each criterion includes up to five match
 rules. 

 You create this membership criteria on the plugin and then push it to NSX-T Manager. However,
 this does not apply the membership criteria to guest virtual machines in your
 deployment. Define and apply membership data, such as tags, to your guest VMs in
 NSX-T Manager. 

 The rules that the Panorama plugin for NSX-T identifies and classifies virtual machines based on
 two membership types—virtual machine or IP set. The keys and operators usable with
 each member type are listed in the table below. 

 Member Type Key Operator 

 IP Set 

 Tag 

 Equals 

 Virtual Machine 

 Tag 

 Name 

 OS Name 

 Computer Name 

 Equals 

 Contains 

 Starts With 

 Ends With 

 Not Equals ( Not applicable with Tag key ) 

 Membership criteria changes should be made only on Panorama; do not make changes on NSX-T
 Manager. If you make changes on NSX-T Manager, the Panorama plugin for VMware
 NSX shows the service definition as out-of-sync. Click on the
 Out-of-Sync link to see the specific reason for the
 out-of-sync status. If a membership criteria change is the cause, perform a
 configuration sync by clicking NSX-T Config-Sync . 

 Select Panorama VMware NSX-T Membership
Criteria Add . 

 To add or modify membership criteria for a service definition, with at least one Dynamic Address
 Group, you can click on the service definition name instead of clicking
 Add . 

 From the Name , select a service
definition for the Membership Criteria. The selected service definition
must have East_West insertion type and used as part of a security-centric
deployment. 

 Click Add to specify a dynamic
address group. 

 Select a Dynamic Address Group from the drop-down. The
 drop-down lists the Dynamic Address Groups associated with the specified service
 definition. 

 The plugin UI displays dynamic and static address groups configured on
 Panorama. Take care not accidently select a static address group when
 configuring membership criteria. 

 Click Add to define the criteria
associated with the chosen dynamic address group. 

 Enter a descriptive name for the Criteria . 

 Click Add to define a rule. 

 Define a rule. You can create up to five rules. 

 Enter a descriptive name for the rule. 

 Select the Member Type —Virtual
Machine or IP Set. 

 Select the Key —Tag, Name, OS
Name, Computer Name. 

 Select the Operator —Equals,
Contains, Starts With, Ends With, Not Equals. 

 Enter the Value . 

 If the Key is set to Tag, the Value is the Tag. The plugin
user interface does not list the Tags, so you must use the Panorama
CLI (with NSX-T Manager 3.0.0. and later). 

 request plugins vmware_nsx nsx_t nsxt-tags service-definition <SD_name> 

 ( Optional ) Enter the Scope .
Scope is applicable only with the key Tag .
Scope is an optional value applied to an object tag in NSX-T. The
scope is defined on NSX-T Manager. For example, if you tag virtual machines
based on operating system, you can create tags for Windows, Linux,
and MacOS and then set the scope of each tag to OS. 

 To view the tags and scope, use the Panorama CLI (with
NSX-T Manager 3.0.0 and later). 

 Execute the following command
to view the list of tags. 

 request plugins vmware_nsx nsx_t nsxt-tags service-definition <SD_name> 

 Execute
the following command to view the scope associated with the specified
tag. 

 request plugins vmware_nsx nsx_t nsxt-scope tag <tag_value> service-definition <SD-name> 

 Click OK . 

 ( Optional ) Click Add to
create additional (up to five total) rules. 

 On the Dynamic Address Group window, click OK to
finish or Add to create additional criteria
(up to five total) and rules. 

 On the Membership Criteria window, click OK to finish or
 Add to specify additional Dynamic Address Groups . 

 Previous 

 Apply Security Policies to the VM-Series Firewall on NSX-T (East-West) 

 Next 

 Generate Steering Policy 

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

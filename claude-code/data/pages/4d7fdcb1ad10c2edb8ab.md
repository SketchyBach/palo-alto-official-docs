---
url: https://docs.paloaltonetworks.com/ngfw/help/12-1/policies/policies-authentication/create-and-manage-authentication-policy
fetched_at: 2026-08-13T16:50:56Z
source: palo-alto-main
---

# Create and Manage Authentication Policy Clear

Create and Manage Authentication Policy 

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

 Create and Manage Authentication Policy 

 Updated on 

 Thu Jun 25 18:50:04 PDT 2026 

 Focus 

 Download PDF 

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

 Updated on 

 Thu Jun 25 18:50:04 PDT 2026 

 Focus 

 Home 

 Next-Generation Firewall 

 Policies 

 Policies > Authentication 

 Create and Manage Authentication Policy 

 Download PDF 

 Next-Generation Firewall 

 Create and Manage Authentication Policy 

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

 Building Blocks of an Authentication Policy Rule 

 Next 

 Policies > DoS Protection 

 Create and Manage Authentication Policy 

 Select the Policies Authentication page to create
and manage Authentication policy rules: 

 Task 

 Description 

 Add 

 Perform the following prerequisites before
creating Authentication policy rules: 

 Configure the User-ID™ Authentication Portal settings (see Device
> User Identification > Authentication Portal Settings ). The
firewall uses Authentication Portal to display the first authentication
factor that the Authentication rule requires. Authentication Portal
also enables the firewall to record the timestamps associated with
authentication Timeout periods
and to update user mappings. 

 Configure a server profile that specifies how the firewall
can access the service that will authenticate users (see Device
> Server Profiles ). 

 Assign the server profile to an authentication profile that
specifies authentication settings (see Device
> Authentication Profile ). 

 Assign the authentication profile to an authentication enforcement object
that specifies the authentication method (see Objects
> Authentication ). 

 To create a rule, perform
one of the following steps and then complete the fields described
in Building
Blocks of an Authentication Policy Rule : 

 Click Add . 

 Select a rule on which to base the new rule and click Clone
Rule . The firewall inserts the copied rule, named <rulename>#,
below the selected rule, where # is the next available integer that
makes the rule name unique, and generates a new UUID for the cloned
rule. For details, see Move
or Clone a Policy Rule . 

 Modify 

 To modify a rule, click the rule Name and
edit the fields described in Building
Blocks of an Authentication Policy Rule . 

 If the
firewall received the rule from Panorama, the rule is read-only;
you can edit it only on Panorama. 

 Move 

 When matching traffic, the firewall evaluates
rules from top to bottom in the order that the Policies Authentication page lists them.
To change the evaluation order, select a rule and Move
Up , Move Down , Move
Top , or Move Bottom . For details,
see Move
or Clone a Policy Rule . 

 Delete 

 To remove an existing rule, select and Delete it. 

 Enable/Disable 

 To disable a rule, select and Disable it.
To re-enable a disabled rule, select and Enable it. 

 Highlight Unused Rules 

 To identify rules that have not matched
traffic since the last time the firewall was restarted, Highlight
Unused Rules . You can then decide whether to disable
or delete unused rules. The page highlights unused rules with a
dotted yellow background. 

 Preview rules ( Panorama only ) 

 Click Preview Rules to
view a list of the rules before you push the rules to the managed
firewalls. Within each rulebase, the page visually demarcates the
rule hierarchy for each device group (and managed firewall) to facilitate
scanning of numerous rules. 

 Previous 

 Building Blocks of an Authentication Policy Rule 

 Next 

 Policies > DoS Protection 

 On This Page 

 Activation & Onboarding 

 Strata Cloud Manager 

 Activate a License or Product 

 Cloud Identity Engine 

 Strata Logging Service 

 Device Associations 

 Hub 

 Identity and Access Management 

 Tenant Management 

 Next-Generation Firewalls 

 AIOps for NGFW 

 Cloud Management for NGFWs 

 Cloud NGFW for AWS 

 Cloud NGFW for Azure 

 CN-Series 

 Firewalls 

 PAN-OS 

 PAN-OS SD-WAN 

 Service Provider 

 VM-Series 

 SASE 

 Prisma Access 

 Strata Multitenant Cloud Manager 

 AI-Powered ADEM 

 Prisma Access Monitoring and Visibility 

 Prisma SD-WAN 

 ION Devices 

 Next-Generation CASB 

 Cloud-Delivered Security Services 

 Advanced WildFire 

 Advanced URL Filtering 

 Advanced Threat Prevention 

 Advanced DNS Security 

 Device Security 

 Enterprise DLP 

 SaaS Security 

 Network Security 

 Shared Policy for NGFWs and Prisma Access 

 Visibility & Monitoring 

 Dashboards 

 Incidents and Alerts 

 Reports 

 Autonomous DEM 

 Best Practices 

 Best Practices Library 

 Experts Corner 

 Solutions Docs from Product Experts 

 Network Security 

 PAN-OS 

 Next-Generation Firewall 

 12.1 

 Help 

 Web Interface 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

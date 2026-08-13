---
url: https://docs.paloaltonetworks.com/prisma-access/administration/ztna-connector-in-prisma-access/ztna-connector-application-tags
fetched_at: 2026-08-13T17:25:46Z
source: palo-alto-main
---

# ZTNA Connector Application Tags Clear

ZTNA Connector Application Tags 

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

 ZTNA Connector Application Tags 

 Updated on 

 Mon Aug 10 14:01:14 PDT 2026 

 Focus 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 Deutsch (German) 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma Access Docs 

 Release Notes 

 Select a Document 

 6.2 Preferred and Innovation 

 6.1 Preferred and Innovation 

 6.0 Preferred and Innovation 

 5.2 Preferred and Innovation 

 5.1 Preferred and Innovation 

 5.0 Preferred and Innovation 

 4.2 Preferred 

 4.1 Preferred 

 4.0 Preferred 

 3.2 Preferred and Innovation 

 Activation & Onboarding 

 Administration 

 Select a Document 

 4.0 & Later 

 Prisma Access China 

 Integrations 

 Incidents & Alerts 

 New Features 

 Updated on 

 Mon Aug 10 14:01:14 PDT 2026 

 Focus 

 Home 

 Prisma Access 

 Prisma Access Administration 

 Prisma Access ZTNA Connector 

 ZTNA Connector Application Tags 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 Deutsch (German) 

 Prisma Access 

 ZTNA Connector Application Tags 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma Access Docs 

 Release Notes 

 Select a Document 

 6.2 Preferred and Innovation 

 6.1 Preferred and Innovation 

 6.0 Preferred and Innovation 

 5.2 Preferred and Innovation 

 5.1 Preferred and Innovation 

 5.0 Preferred and Innovation 

 4.2 Preferred 

 4.1 Preferred 

 4.0 Preferred 

 3.2 Preferred and Innovation 

 Activation & Onboarding 

 Administration 

 Select a Document 

 4.0 & Later 

 Prisma Access China 

 Integrations 

 Incidents & Alerts 

 New Features 

 Previous 

 ZTNA Connector Diagnostic Tools 

 Next 

 Active Directory Domain Services Support with ZTNA Connector 

 ZTNA Connector Application Tags 

 Assign tags to private application targets to automate security policy enforcement
 through dynamic address groups without manual address object management. 

 Where Can I Use This? What Do I Need? 

 Prisma Access (Managed by Strata Cloud Manager) 

 Prisma Access (Managed by Panorama) 

 We require a minimum version of Prisma Access 5.0 to
 enable ZTNA Connector support. 

 Prisma Access Base (ZTNA or Enterprise) license includes 10
 Connectors. 

 Private App Access add-on license
 includes up to 200 Connectors. 

 Tags are metadata labels you assign to FQDN targets, IP subnet targets, and wildcard
 targets in Prisma Access ® ZTNA Connector. Without application tagging, you manually
 create individual address objects for each target, which increases administrative
 overhead as your private application inventory grows and can result in overly permissive
 access controls. When you assign a tag to an application target, the firewall
 automatically creates address objects from the tag-to-IP mappings and populates the
 corresponding dynamic address group , eliminating manual address object
 updates and policy rewrites as application targets change. 

 When you tag a target in ZTNA Connector, Prisma Access automatically translates the
 tag-to-IP mappings into address objects and pushes them to the firewall. The firewall
 updates the membership of any dynamic address group that references the tag, and any
 security policy rule that uses the dynamic address group as a destination automatically
 enforces the updated membership — no commit or push is required. As ZTNA Connector
 resolves application targets to IP addresses—whether through DNS resolution of FQDN
 targets or direct IP subnet assignments—the firewall keeps dynamic address group
 membership current in real time. You reference the dynamic address group in a security
 policy rule to enforce access controls across all tagged targets without rewriting the
 rule as your application inventory changes. 

 For wildcard targets, ZTNA Connector automatically applies the parent wildcard target's
 tag to any FQDN applications discovered under the wildcard. This inheritance extends
 policy coverage to newly identified applications without additional configuration. If
 you update a tag on a wildcard target, the change propagates to all FQDN applications
 discovered under that wildcard. 

 You can assign up to five tags per application target. Tags referenced by a dynamic
 address group can't be deleted until you remove or update those dynamic address groups
 to use different match criteria. Before you remove a tag from a target, verify that no
 dynamic address group uses the tag as a match criterion, because the firewall can't
 remove the corresponding address objects from a dynamic address group that still
 references the tag. 

 Tag a Private Application Target 

 Assign tags to application targets so that Prisma Access can automatically create
 address objects from the tag-to-IP mappings and populate dynamic address groups. Tags
 you assign to wildcard targets automatically propagate to all FQDN applications
 discovered under that wildcard. You can assign up to five tags per target. 

 Select Configuration ZTNA Connector and then select Connector Groups . 

 Select the Connector Group that contains the application targets you want to
 tag. 

 Select the target type to tag: 
 To tag an FQDN-based application, select FQDN
 Targets . 

 To tag an IP subnet-based application, select IP Subnet
 Targets . 

 To tag a wildcard-based application and all applications discovered under
 it, select Wildcard Targets . 

 Add to create a new target, or select an existing target and
 click Edit . 

 In the Tags field, select one or more existing tags from the
 dropdown, or Create a tag to define a new tag. To create a
 new tag, enter a Name , optionally choose a
 Color and enter a Description ,
 then Create 

 . 
 You can assign up to five tags per target. Tags are shared across all
 targets in a connector group, allowing you to group related private applications
 and enforce consistent security policy across the group. 

 Save to apply the tags. 
 After you save, Prisma Access 
 automatically translates the tag-to-IP mappings into address objects and pushes
 them to the firewall. The firewall automatically updates the membership of any
 dynamic address group that references the tag, and any security policy rule that
 uses the dynamic address group as a destination enforces the change immediately —
 no commit or push is required. 

 ( Optional ) To remove a tag from a target, select the target,
 Edit , remove the tag from the Tags 
 field, and Save . 

 Before removing a tag, verify that no dynamic address group uses the tag as a
 match criterion. Remove or update any dynamic address groups that reference the
 tag before removing it from the target. The firewall can't remove address
 objects from a dynamic address group that still references the tag. 

 Create a Dynamic Address Group Using ZTNA Connector Tags 

 Create a dynamic address group that filters membership by ZTNA Connector tags. Prisma Access automatically populates the group with the IP addresses it resolves
 for application targets with matching tags, and updates membership as tags and targets
 change. Before creating a dynamic address group, tag your ZTNA Connector application
 targets as described in the previous section. 

 Select Configuration NGFW and Prisma Access Objects Address Address Groups and click Add Address Group . 

 Enter a Name and optional Description 
 for the address group. 

 For Type , choose Dynamic . 

 Select Add Match Criteria , then select the ZTNA
 Connector tab in the match criteria panel. 

 Select one or more tags from the list to use as match criteria, choose
 AND or OR to define how multiple
 tags are evaluated, then click Save . 
 Selecting
 OR includes targets that match any of the specified
 tags. Selecting AND includes only targets that match all
 specified tags. 

 Save and Push Config to save and push
 your configuration changes. 

 Create a Security Policy Rule Using the Dynamic Address Group 

 Create a security policy rule that uses the dynamic address group as the destination to
 enforce access controls for all tagged ZTNA Connector application targets. When
 application targets change or tags are updated, the dynamic address group membership
 updates automatically and the policy remains in effect without a rule rewrite. 

 Select Configuration NGFW and Prisma Access Security Services Security Policy and click Add Rule . 

 Enter a Name for the rule. 

 Under Destination , Add next to
 Address and select the dynamic address group you
 created. 

 For Action , choose Allow . 

 Save and Push Config to save and push
 your configuration changes. 

 Previous 

 ZTNA Connector Diagnostic Tools 

 Next 

 Active Directory Domain Services Support with ZTNA Connector 

 On This Page 

 Activation and Onboarding 

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

 Panorama 

 Service Provider 

 VM-Series 

 Plugins 

 SASE 

 Prisma Access 

 Prisma SASE Multitenant Platform 

 AI-Powered ADEM 

 Prisma Access Monitoring & Visibility 

 Prisma SD-WAN 

 ION Devices 

 Next-Generation CASB 

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

 Remote Browser Isolation 

 Prisma Access Agent 

 Visibility & Monitoring 

 Dashboards 

 Incidents and Alerts 

 Reports 

 Autonomous DEM 

 FedRAMP 

 Prisma SASE for FedRAMP 

 Autonomous DEM for FedRAMP 

 Hardware Reference 

 ION 1000 

 ION 1200 

 ION 1200-S 

 ION 2000 

 ION 3000 

 ION 3200 

 ION 5200 

 ION 7000 

 ION 9000 

 ION 9200 

 Hardware Quick Start Guides 

 ION 1200 

 ION 1200 4G 

 ION 1200 5G 

 ION 1200-S 

 ION 1200-S 4G 

 ION 1200-S 5G 

 ION 3200 

 ION 5200 

 ION 9200 

 Virtual ION Deployment 

 Virtual ION on AWS 

 Virtual ION on Azure 

 Virtual ION on GCP 

 Virtual ION on KVM for NFV 

 Virtual ION on OCI 

 Virtual ION on VMware 

 3rd Party Integrations 

 AWS Cloud-WAN Integration (GRE Connect) 

 AWS Cloud-WAN Integration (Tunnel-less Connect) 

 Checkpoint Integration 

 LiveAction Integration 

 Netskope Integration 

 Symantec Web Security Services Integration 

 Best Practices 

 Best Practices Library 

 Experts Corner 

 Solutions Docs from Product Experts 

 Administration 

 Prisma Access 

 Prisma SASE 

 Prisma Access 

 4.0 & Later 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

---
url: https://docs.paloaltonetworks.com/ngfw/help/12-2/objects/objects-tags/create-tags
fetched_at: 2026-08-13T16:52:43Z
source: palo-alto-main
---

# Create Tags Clear

Create Tags 

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

 Create Tags 

 Updated on 

 Mon Aug 03 19:43:33 PDT 2026 

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

 Mon Aug 03 19:43:33 PDT 2026 

 Focus 

 Home 

 Next-Generation Firewall 

 PAN-OS Web Interface Help 

 Objects 

 Objects > Tags 

 Create Tags 

 Download PDF 

 Next-Generation Firewall 

 Create Tags 

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

 Objects > Tags 

 Next 

 View Rulebase as Groups 

 Create Tags 

 Objects Tags 

 Select Tags to create a tag, assign a

color or to delete, rename, and clone tags. Each object can have

up to 64 tags; when an object has multiple tags, it displays the

color of the first tag applied. 

 On the firewall, the Tags tab displays

the tags that you define locally on the firewall or push from Panorama

to the firewall. On Panorama, the Tags tab

displays the tags that you define on Panorama. This tab does not

display the tags that are dynamically retrieved from the VM Information

sources defined on the firewall for forming dynamic address groups

nor does it display tags that are defined using the XML or REST

API. 

 When you create a new tag, the tag is automatically created in

the Virtual System or Device Group that is currently selected on

the firewall or Panorama. 

 Tag Settings 

 Description 

 Name 

 Enter a unique tag name (up to 127 characters).

The name is not case-sensitive. 

 Shared 

 Select this option if you want the tag to

be available to: 

 Every virtual system (vsys) on a

multi-vsys firewall. If you clear this selection, the tag is available

only to the Virtual System selected in the Objects tab. 

 Every device group on Panorama. If you disable (clear) this

option, the tag will be available only to the Device Group selected

in the Objects tab. 

 Disable override ( Panorama only ) 

 Select this option to prevent administrators

from overriding the settings of this tag in device groups that inherit

the tag. This selection is cleared by default, which means administrators

can override the settings for any device group that inherits the

tag. 

 Color 

 Select a color from the color palette in

the drop-down (default is None). 

 Comments 

 Add a label or description to describe for

what the tag is used. 

 Add a tag: Add a tag and then

fill in the following fields: 

 You can also create a new tag

when you create or edit policy in the Policies tab.

The tag is automatically created in the Device Group or Virtual System

that is currently selected. 

 Edit a tag: Click a tag to edit, rename, or assign a color

to a tag. 

 Delete a tag: Click Delete and select

the tag. You cannot delete a predefined tag. 

 Move or Clone a tag: The options to move or clone a tag allow

you to copy a tag or move a tag to a different Device Group or Virtual

System on firewalls with multiple virtual systems enabled. 

 Move

or Clone and select the tag. Select the Destination location—Device

Group or Virtual System. Disable (clear) this option to Error

out on first detected error in validation if you want

the validation process to discover all errors for the object before

displaying the errors. This option is enabled by default and the

validation process stops when the first error is detected and only

displays the error. 

 Override or Revert a tag ( Panorama only ): The Override option

is available only if you did not select the Disable override option

when you created the tag. The Override option

allows you to override the color assigned to the tag that was inherited

from a shared or ancestor device group. The Location is

the current device group. You can also Disable override to

prevent future override attempts. 

 Revert changes

to undo recent modifications of a tag. When you revert a tag, the Location field

displays the device group or virtual system from where the tag was

inherited. 

 Previous 

 Objects > Tags 

 Next 

 View Rulebase as Groups 

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

 12.2 

 PAN-OS 

 Help 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

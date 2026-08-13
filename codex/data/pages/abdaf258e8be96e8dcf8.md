---
url: https://docs.paloaltonetworks.com/prisma-access-browser/administration/manage-prisma-access-browser-devices/manage-prisma-access-browser-device-groups
fetched_at: 2026-08-13T17:23:13Z
source: palo-alto-main
---

# Manage Prisma Browser Device Groups Clear

Manage Prisma Browser Device Groups 

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

 Manage Prisma Browser Device Groups 

 Updated on 

 Tue Jul 28 09:38:39 PDT 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma Browser Docs 

 Activation & Onboarding 

 Getting Started 

 Deployment 

 Administration 

 Integrations 

 User Guide 

 Updated on 

 Tue Jul 28 09:38:39 PDT 2026 

 Focus 

 Home 

 Prisma Browser 

 Prisma Access Browser Administration 

 Manage Prisma Browser Devices 

 Manage Prisma Browser Device Groups 

 Download PDF 

 Prisma Browser 

 Manage Prisma Browser Device Groups 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma Browser Docs 

 Activation & Onboarding 

 Getting Started 

 Deployment 

 Administration 

 Integrations 

 User Guide 

 Previous 

 Manage Prisma Browser Devices 

 Next 

 Configure Prisma Browser Device Posture Attributes 

 Manage Prisma Browser Device Groups 

 Manage the Device groups in the Prisma Access Browser 

 Where Can I Use This? What Do I Need? 

 Strata Cloud Manager 

 Standalone Prisma Browser 

 Prisma Access with Prisma Browser bundle license or Prisma Browser standalone license 

 Role: Prisma Access Browser
 Roles 

 The Prisma Browser has a Device Group function, where you can create
 different groups for different devices. Groups are dynamic; you can set up groups
 for specific managed devices, specific posture attributes, specific user groups and
 so on. You can perform the following 

 Changes to device groups are saved to a draft
 configuration and do not take effect until you publish the draft. For more
 information, see Manage Configuration Versions (Draft Mode). 

 Below the tab, you can perform the following tasks: 

 Search the groups via the Device Group name . 

 Filter the Device Groups based on the Type ( Prisma Browser , Prisma Browser for Mobile, Prisma Browser Extension,
 Chromebook), the Attributes assigned to the device group , Created
 at date, or Updated at date. 

 The list of Device Groups allows you to see the group types, including the
 following information: 

 Name - The Device Group name. 

 Platform - Prisma Browser , Prisma Browser for Mobile,
 Prisma Browser Extension, Chromebook 

 Attributes - The specific criteria utilized to identify
 which devices belong to the Device Group. 

 Created at - The date when the Device Group was created.
 Hover over the field to see the full timestamp. 

 Updated at - The date when the Device Group was last
 updated. Hover over the field to see the full timestamp. 

 Export Device Groups 

 You can export a list of the device groups. The export file is saved in .csv
 format. 
 Click the Export icon 

 In the Export window, select one of the following options: 

 Export all - Export all of the device
 groups. 

 Export filtered data - Export the data that
 is visible in the filtered list. 

 The data will be exported to a .csv file. 

 Create Device Groups 

 As an administrator, you can exercise a considerable amount of
 flexibility in configuring the Device Groups needed in the organization. For
 example, groups meet changing business, operational, and organizational
 circumstances. 

 Device Groups can be used either with sign-in rules to set the security
 bar for accessing the Browser, or with posture-focused scoping for policy
 rules. 

 You can create new Device Groups as needed. 

 To create a new Device Group: 

 On the Devices screen, select the Devices Group 
 tab. 

 Click Add device group . 

 In the Add device group window, do the following: 
 Enter a descriptive Group name . 

 Select the platform. In the case, click Desktop browser .

 The method is the same for the
 Prisma Browser for Mobile and the Prisma Browser 
 Extension. 

 Select the Device group attributes that you want to use in the group.

 You can choose either positive or negative attributes. For more
 information, refer to Device Posture
 Attributes . 

 You can require the device group to include specific OS versions
 only. For example, your device group will only include devices
 running Windows 10 Pro, build 19045. 

 You can require the device group to include specific OS versions
 only. For example, your device group will Not include
 devices running Windows 10 Pro, build 19045. All other browser
 versions will be accepted. 

 Click Create . 

 Mobile Device group attributes: 

 Extension Device group attributes: 

 Rule Logic - AND vs. OR 

 When configuring sign-in rules with Device Groups , it’s important to
 understand how criteria logic works. This section explains how to achieve
 AND or OR behavior depending on how you group your
 criteria. 

 Default Behavior: AND Logic within a Single Device Group 

 If you define multiple criteria within the same Device Group , the system
 evaluates them using the AND operator. This means all conditions must
 be true for the Device Group to apply. 

 Example: 

 You create a Device Group with the following two criteria: 

 Operating System is not macOS 

 Device is not running Avira 

 You apply this Device Group to a sign-in rule set to Block . 

 Result: 

 If a user attempts to sign in from a macOS device without Avira
 installed: 

 The OS does not match the "not macOS" condition (because it
 is macOS). 

 The Device does match the "not Avira" condition. 

 Since the Device Group uses AND logic, the rule does not 
 match both conditions, so sign-in is allowed . 

 How to Use OR Logic: Create Separate Device Groups 

 To evaluate criteria using the OR operator, you need to create two or
 more separate Device Groups , each with its own condition. Then, add all
 of those Device Groups to the same sign-in rule. 

 To create OR logic: 

 Create one Device Group with the condition: 

 OS is not macOS 

 Create a second Device Group with the condition: 

 Device is not running Avira 

 In your sign-in rule (set to Block ), select both Device
 Groups under the Device Groups option. 

 Result: 

 If a user signs in from a macOS device without Avira: 

 The device does not match the first Device Group ("not
 macOS"). 

 But it does match the second Device Group ("not Avira"). 

 Since the rule uses OR logic across the two Device Groups,
 matching either group triggers the rule. 

 Therefore, sign-in is blocked as expected. 

 Previous 

 Manage Prisma Browser Devices 

 Next 

 Configure Prisma Browser Device Posture Attributes 

 On This Page 

 Activation & Onboarding 

 Strata Cloud Manager 

 Cloud Identity Engine 

 Strata Logging Service 

 Device Associations 

 Hub 

 Identity and Access Management 

 Tenant Management 

 SASE 

 Prisma Access 

 Strata Multitenant Cloud Manager 

 AI-Powered ADEM 

 Prisma Access Monitoring and Visibility 

 Prisma SD-WAN 

 ION Devices 

 Next-Generation CASB 

 Prisma Browser 

 Administration 

 Prisma Access 

 Strata Cloud Manager 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

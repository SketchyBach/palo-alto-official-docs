---
url: https://docs.paloaltonetworks.com/prisma-sd-wan/administration/prisma-sd-wan-stacked-policies/create-modify-device-management-policies
fetched_at: 2026-08-13T17:28:49Z
source: palo-alto-main
---

# Configure Device Management Policy Clear

Configure Device Management Policy 

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

 Configure Device Management Policy 

 Updated on 

 Mon Aug 10 04:14:37 PDT 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma SD-WAN Docs 

 Activation & Onboarding 

 Administration 

 CloudBlades 

 Select a Document 

 CloudBlade Integrations 

 CloudBlades Integration with Prisma Access 

 Deployment 

 Incidents & Alerts 

 Reference 

 Release Notes 

 Select a Document 

 ION 6.8 

 ION 6.6 

 ION 6.5 

 ION 6.4 

 ION 6.3 

 ION 6.1 

 ION 5.6 

 Prisma SD-WAN Controller 

 Prisma SD-WAN On-Premises Controller 

 Prisma SD-WAN CloudBlades 

 Prisma Access CloudBlade Cloud Managed 

 Prisma Access CloudBlade Panorama Managed 

 New Features 

 Updated on 

 Mon Aug 10 04:14:37 PDT 2026 

 Focus 

 Home 

 Prisma SD-WAN 

 Prisma SD-WAN Administrator’s Guide 

 Prisma SD-WAN Stacked Policies 

 Configure Device Management Policy 

 Download PDF 

 Prisma SD-WAN 

 Configure Device Management Policy 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma SD-WAN Docs 

 Activation & Onboarding 

 Administration 

 CloudBlades 

 Select a Document 

 CloudBlade Integrations 

 CloudBlades Integration with Prisma Access 

 Deployment 

 Incidents & Alerts 

 Reference 

 Release Notes 

 Select a Document 

 ION 6.8 

 ION 6.6 

 ION 6.5 

 ION 6.4 

 ION 6.3 

 ION 6.1 

 ION 5.6 

 Prisma SD-WAN Controller 

 Prisma SD-WAN On-Premises Controller 

 Prisma SD-WAN CloudBlades 

 Prisma Access CloudBlade Cloud Managed 

 Prisma Access CloudBlade Panorama Managed 

 New Features 

 Previous 

 Device Management Policies 

 Next 

 Simplify Coffee Shop Deployment Policies for Prisma Access Traffic 

 Configure Device Management Policy 

 Prisma SD-WAN allows to create, modify, and delete device management
 policies. 

 Where Can I Use
 This? What Do I Need? 

 Prisma SD-WAN (Managed by Strata Cloud Manager ) 

 Prisma SD-WAN 

 If a site has two devices configured for High Availability (HA), you must apply
 this configuration to each device individually. 

 To configure access for a specific interface, you can perform several actions: review
 existing policies, create new ones, or delete those you no longer need. 

 Reviewing Policies : Start by reviewing any policies that have already
 been created for the interface. 

 Creating a New Policy : To create a new policy, first select the
 interface. Then, specify the desired access (for example, Allow Ping, Allow
 SSH). You must also provide a name for the policy extension, such as
 "remote-monitoring," and a prefix for the policy to define the source of the
 traffic. 

 Deleting Policies : You can delete existing policies as needed to remove
 access rules. 

 Disabling a Policy : The Disabled button is a useful feature for
 troubleshooting. It allows you to keep a policy configuration in place while
 temporarily bypassing its rules without having to delete them. 

 Create a New Device Management Policy 

 Select Configuration Resources Device Management Policy . 

 In the Choose Site, Element section, search for a
 Site and select it. 

 Choose the Element (ION device) from the
 dropdown. 
 A list of all interfaces on the selected ION device, including all
 sub-interfaces, is displayed. 

 Select the Interface to which the policy is to be
 applied and click Get . 

 In the View/Set Configuration section, fill in the
 policy details: 

 Name : Enter a name for the policy. 

 Namespace : This field is auto-filled. 

 Interface : This field is auto-filled. 

 Enter the Prefix (IPv4 or IPv6) , select the
 App (for example, Ping), and choose an
 Action (for example, Allow). 

 Click Submit to save the new policy. 

 Modify or Delete a Policy Rule 

 In the Choose Site, Element section, select the
 Site , Element , and
 Interface associated with the policy you want to
 change. Click Get . 
 The View/Set Configuration section displays the
 existing policy rules. 

 To edit a rule, you can modify the Prefix (IPv4 or
 IPv6) , App , or
 Action for the desired line item. 

 To delete a rule, locate the specific rule you want to remove and click the
 Delete button next to it. 

 After making your changes, click Submit to update
 the policy. 

 Previous 

 Device Management Policies 

 Next 

 Simplify Coffee Shop Deployment Policies for Prisma Access Traffic 

 On This Page 

 Activation & Onboarding 

 Strata Cloud Manager 

 Activate a License or Product 

 Cloud Identity Engine 

 Hub 

 Identity and Access Management 

 Tenant Management 

 SASE 

 Prisma Access 

 Strata Multitenant Cloud Manager 

 AI-Powered ADEM 

 Prisma Access Monitoring and Visibility 

 Visibility & Monitoring 

 Dashboards 

 Incidents and Alerts 

 Reports 

 Autonomous DEM 

 FedRAMP 

 Prisma SASE for FedRAMP 

 Hardware Reference 

 ION 1000 

 ION 1200 

 ION 1200-S 

 ION 2000 

 ION 3000 

 ION 3200 and ION 3200H 

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

 ION 3200H 

 ION 3200H 5G 

 ION 5200 

 ION 9200 

 Virtual ION Deployment 

 Virtual ION on AWS 

 Virtual ION on Azure 

 Virtual ION on GCP 

 Virtual ION on Alibaba Cloud 

 Virtual ION on KVM for NFV 

 Virtual ION on OCI 

 Virtual ION on VMware 

 Virtual ION on Megaport Virtual Edge 

 Virtual ION on Dell PowerEdge 

 Prisma SD-WAN Integration 

 AWS Cloud-WAN Integration (GRE Connect) 

 AWS Cloud-WAN Integration (Tunnel-less Connect) 

 Checkpoint Integration 

 LiveAction Integration 

 Netskope Integration 

 Symantec Web Security Services Integration 

 Prisma SD-WAN Experts Corner 

 Network Policy 

 QoS Whitepaper 

 Security Architecture Whitepaper 

 External Antennas for ION-C Series 

 Dynamic Path Selection 

 Best Practices 

 Best Practices Library 

 Resources 

 All Products A - Z 

 Compatibility Matrix 

 SASE 

 Administration 

 Prisma SD-WAN 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

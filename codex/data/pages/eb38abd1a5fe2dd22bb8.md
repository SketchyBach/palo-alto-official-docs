---
url: https://docs.paloaltonetworks.com/cloud-ngfw/azure/cloud-ngfw-for-azure/panorama-policy-management
fetched_at: 2026-08-13T15:31:14Z
source: palo-alto-main
---

# Panorama Policy Management Clear

Panorama Policy Management 

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

 Panorama Policy Management 

 Updated on 

 Mon Jun 29 22:22:17 PDT 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Cloud NGFW for Azure Docs 

 Getting Started 

 Deployment 

 Administration 

 Reference 

 Release Notes 

 New Features 

 Updated on 

 Mon Jun 29 22:22:17 PDT 2026 

 Focus 

 Home 

 Cloud NGFW for Azure Administration 

 Protect Traffic with Cloud NGFW for Azure 

 Panorama Policy Management 

 Download PDF 

 Cloud NGFW for Azure 

 Panorama Policy Management 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Cloud NGFW for Azure Docs 

 Getting Started 

 Deployment 

 Administration 

 Reference 

 Release Notes 

 New Features 

 Previous 

 Set Up Outbound Decryption on Cloud NGFW for Azure 

 Next 

 Panorama Integration Prerequisites 

 Panorama Policy Management 

 Learn about Cloud NGFW for Azure Panorama policy management. 

 Where Can I Use This? What Do I Need? 

 Cloud NGFW for Azure 

 Cloud NGFW subscription 

 Palo Alto Networks Customer Support Portal account 

 Azure Marketplace subscription 

 You can use a Panorama appliance to manage a shared set of security rules centrally on
 Cloud NGFW resources alongside your physical and virtual firewall appliances. You can
 also manage all aspects of shared objects and profiles configuration, push these rules,
 and generate reports on traffic patterns or security incidents of your Cloud NGFW
 resources, all from a single Panorama console. 

 Panorama provides a single location from which you can have centralized policy and
 firewall management across hardware firewalls, virtual firewalls, and cloud firewalls,
 which increases operational efficiency in managing and maintaining a hybrid network of
 firewalls. 

 How does integration work? 

 When you create a Cloud NGFW resource using the Azure Portal , you have the option to use Palo Alto Networks
 Panorama to manage your security policy rules. You can then manage a shared set of
 security rules centrally on Cloud NGFW resources you create alongside your physical and
 virtual firewall appliances, and you can use logging, reporting and log analytics, all from
 a single Panorama console. 

 When a firewall reaches an unhealthy state and
 is disconnected, it's removed from Panorama after a period of time, typically three
 days. This ensures that the firewall isn’t deleted prematurely. 

 Integration Components 

 The following Palo Alto Networks components integrate your Cloud NGFW resource with
 Panorama. 

 Palo Alto Networks policy management is the primary and mandatory component of the
 solution. Use a Panorama appliance to author and manage policy rules for your
 Cloud NGFW resources. The policy management component also helps to associate your
 authored policy rules and objects to multiple Cloud NGFW resources in different Azure
 regions. 

 Panorama Azure plugin is a mandatory component of this solution. The Panorama
 Azure plugin enables you to create Cloud Device Groups and Cloud template stacks which
 help you manage policy rules and objects on NGFW resources linked with Panorama. 

 Cloud Device Groups (Cloud DG) are special-purpose Panorama device groups that
 allow you to author rules and objects for Cloud NGFW resources. You create Cloud DGs
 using the Panorama Azure plugin web interface by specifying the Cloud NGFW resource and
 Azure region information. Cloud DG manifests as a global rulestack in that region. 
 You can create multiple Cloud Device Groups using the Panorama Azure
 plugin. 

 You can use the native Panorama web interface’s device group page to manage
 policy and object configurations in Cloud Device Groups and their associated
 objects and Security Profiles. 

 You can also use your existing shared objects and profiles in your existing
 Panorama device groups by referring to them in the security rules you create in
 your Cloud device groups. 

 Alternatively, you can add these Cloud Device groups to the device-group
 hierarchy you manage in your Panorama to inherit the device group rules and
 objects. If inherited rules reference zones, these zones can be mapped to the
 zones applicable to Cloud NGFW — Public and Private, in the Azure
 Plugin > Cloud NGFW > Cloud Device Group . 

 You can associate the same Cloud DG with multiple regions of the Cloud NGFW
 resource. This Cloud DG will manifest as a dedicated global rulestack in each
 Azure region of your Cloud NGFW resource. 

 Cloud template stacks (Cloud TS) are special-purpose Panorama template stacks that
 allow your security rules in Cloud device groups to refer to object settings that
 Panorama allows you to manage using templates. When creating a Cloud DG, the Panorama
 Azure plugin enables you to create or specify a Cloud template stack. The plugin
 automatically creates this Cloud TS and adds it to the Cloud device group as a reference
 template stack. From now on, you can use the native Panorama web interface’s template
 stack page to configure your templates and add them to these Cloud template stacks. 
 Palo Alto Networks Cloud NGFW service manages most device and network
 configurations in your Cloud NGFW resources. Therefore, Cloud NGFW will ignore
 infrastructure settings such as interfaces, zones, and routing protocols if you
 have configured them in templates added to the Cloud TS. 

 Cloud NGFW currently honors Certificate management and log settings in your
 templates as referenced by the Cloud DG configuration. It ignores all other
 settings. 

 You don’t assign managed devices to Cloud Device Groups and Cloud template stacks
 . 

 Integration steps 

 There are a few steps to integrate Cloud NGFW with Panorama. You first prepare your
 Panorama virtual appliance for this integration by installing the Azure plugin. Once you
 have successfully linked Cloud NGFW, use Panorama to manage
 security objects and rules. 

 To integrate the Cloud NGFW service with your Panorama virtual appliance: 
 Verify Panorama meets the Panorama Integration
 Prerequisites . 

 Link Panorama to the Cloud NGFW.
 After linking use Panorama for Cloud NGFW policy management. 

 Previous 

 Set Up Outbound Decryption on Cloud NGFW for Azure 

 Next 

 Panorama Integration Prerequisites 

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

 Public Cloud 

 Administration 

 Cloud NGFW for Azure 

 Microsoft Azure 

 Cloud 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

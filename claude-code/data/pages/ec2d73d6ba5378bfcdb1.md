---
url: https://docs.paloaltonetworks.com/strata-cloud-manager/aiops/manage-incidents
fetched_at: 2026-08-13T17:37:11Z
source: palo-alto-main
---

# Manage Incidents Clear

Manage Incidents 

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

 Manage Incidents 

 Updated on 

 Wed Aug 12 11:44:17 PDT 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Strata Cloud Manager Docs 

 Activation & Onboarding 

 Subscription & Tenant Management 

 Getting Started 

 AIOps 

 Release Notes 

 New Features 

 Updated on 

 Wed Aug 12 11:44:17 PDT 2026 

 Focus 

 Home 

 Strata Cloud Manager 

 Strata Cloud Manager AIOps 

 Manage Incidents 

 Download PDF 

 Strata Cloud Manager 

 Manage Incidents 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Strata Cloud Manager Docs 

 Activation & Onboarding 

 Subscription & Tenant Management 

 Getting Started 

 AIOps 

 Release Notes 

 New Features 

 Previous 

 Analyze Metric Capacity 

 Next 

 Panorama Subtenancy Support for Prisma Access 

 Manage Incidents 

 Where Can I Use This? What Do I Need? 

 NGFW , including those funded by Software NGFW
 Credits 

 Prisma Access 

 WildFire 

 One of the following licenses: 

 AIOps for NGFW Free (use the AIOps for NGFW Free app) or AIOps for NGFW Premium license (use the Strata Cloud Manager app) 

 Prisma Access 

 Strata Cloud Manager Essentials 

 Strata Cloud Manager Pro 

 An incident is an indication of a fault in the system or a noncompliance with asset
 rules, whether predefined policies or user-defined policies, and security control
 policies. Incidents are triggered when the system detects issues, such as reaching
 system-defined or customer-defined thresholds, or when a fault occurs. 

 The Unified Incident Framework consolidates all incidents from various security products
 into a single interface, offering comprehensive visibility into your entire security
 infrastructure. This framework means that product-specific alerts and incidents are now
 located under the "Incidents" section, while previous dashboards remain in read-only
 mode for reference. 

 Configure default and custom incident settings to control how Strata Cloud Manager
 evaluates your infrastructure, detects deviations from best practices, and raises or
 suppresses incidents. Learn how to customize incident visibility, set priority levels,
 and attach notification profiles. 

 Default Settings —View and modify
 preconfigured incident settings that serve as the baseline configuration for all
 tenants. You can adjust actions, priority levels, notification profiles, and
 check rules for each incident code. 

 Custom Settings —Create tenant-specific
 settings that override defaults for granular control over incident management,
 including scheduled suppression, object-specific handling, and targeted
 notifications. 

 Create a Custom Incident
 Setting —Define a custom incident setting by selecting the product,
 severity, incident category, object type, and action (raise or suppress), then
 attach a notification profile. 

 Custom Posture Check Management —Create
 and manage custom posture checks that evaluate configuration compliance against
 your defined security policies using the Logic Builder to define conditions,
 exceptions, and enforcement actions. 

 Incident Customization for Raise and Clear
 Conditions —Define custom thresholds and monitoring parameters that
 control when Strata Cloud Manager raises or clears incidents for tunnel down,
 BGP down, tunnel flaps, and site long duration events in Prisma Access. 

 Incident Setting Resolution —Understand
 the precedence and longest-match logic that Strata Cloud Manager uses to
 determine which setting applies when multiple settings match a specific
 incident. 

 Incident Categories and
 Subcategories —Review the full list of incident categories (Device,
 Network & Traffic, Security Services, Network Services, Digital Experience,
 Configuration, and Endpoint) and their subcategories. 

 WildFire Incidents —Configure WildFire
 incident codes to surface findings from WildFire analysis as incidents. WildFire
 uses a suppress-by-default model, so you must create custom settings to receive
 alerts for specific resources. 

 Configure notification profiles to receive alerts through email or webhooks when Strata
 Cloud Manager raises, updates, or clears incidents. You can test email delivery and
 webhook connectivity before deploying profiles in production. 

 Associated Events Email
 Notifications —Control whether notification profiles send email alerts for
 associated events (new alerts correlated with an existing incident). This
 setting is disabled by default to reduce notification volume. 

 Webhook Data Schema for
 Incidents —Review the webhook payload data model, including field
 descriptions and an example JSON payload that Strata Cloud Manager sends to your
 configured endpoint. 

 Connect Strata Cloud Manager to ServiceNow to automatically create and update ServiceNow
 tickets when incidents are raised or cleared. You can configure bidirectional or
 unidirectional integration with OAuth authentication. 

 Configure a ServiceNow Notification
 Profile —Set up the ServiceNow notification profile in Strata Cloud
 Manager by entering your ServiceNow instance details, configuring field mappings,
 and testing the connection. 

 Previous 

 Analyze Metric Capacity 

 Next 

 Panorama Subtenancy Support for Prisma Access 

 On This Page 

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

 Endpoints 

 GlobalProtect 

 Visibility & Monitoring 

 Dashboards 

 Incidents and Alerts 

 Reports 

 Autonomous DEM 

 Best Practices 

 Best Practices Library 

 Experts Corner 

 Solutions Docs from Product Experts 

 AIOps 

 Strata Cloud Manager 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

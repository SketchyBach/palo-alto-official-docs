---
url: https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/activate-a-license-for-multitenant-service-provider-backbone
fetched_at: 2026-08-13T15:31:28Z
source: palo-alto-main
---

# Activate a License for Multitenant Service Provider Backbone Through Common Services Clear

Activate a License for Multitenant Service Provider Backbone Through Common Services 

 Home 

 EN

 Location 

 Documentation Home 

 Palo Alto Networks 

 Support 

 Live Community 

 Knowledge Base 

 Strata Copilot

 Common Services: License Activation, Subscription, & Tenant Management 

 : 
 Activate a License for Multitenant Service Provider Backbone Through Common Services 

 Updated on 

 Fri Apr 17 11:31:28 PDT 2026 

 Focus 

 Download PDF 

 Filter

 Expand all | Collapse all 

 Get Started with License Activation, Subscription, & Tenant Management 

 How Activation Works? 

 Firewall and SD-WAN 

 SASE 

 Remote Browser Isolation Activation 

 Prisma SD-WAN and Add-ons License Activation 

 Activate a License for Prisma SD-WAN and Add-ons 

 First Time License Activation - one CSP Account 

 First Time License Activation - multiple CSP Accounts 

 Return Visit License Activation 

 AIOPs Premium Activation 

 First Time Activation - One CSP 

 First Time Activation - Multiple CSPs 

 Return Visit Activation 

 CASB-X Activation 

 First Time Activation - One CSP 

 First Time Activation - Multiple CSPs 

 Return Visit Activation 

 Cloud Identity Engine Activation 

 First Time Activation - One CSP 

 Return Visit Activation 

 Share CIE 

 SaaS Security Inline Activation 

 First Time Activation - One CSP 

 First Time Activation - Multiple CSPs 

 Return Visit Activation 

 SaaS Security Posture Management Activation 

 First Time Activation - One CSP 

 First Time Activation - Multiple CSPs 

 Return Visit Activation 

 Convert SSPM Evaluation to Production 

 Software NGFW Credits Activation 

 Activate a Software NGFW Credits License for IoT Through 

 Activate a Software NGFW Credits License of for NGFW Through 

 Activate a Software NGFW Credits License for on Panorama Through 

 Enterprise License Agreement Add-on Activation 

 Activate ELA Through 

 Activate ELA for IoT Security Through 

 Subscription Management 

 Flexible License Management 

 Diagnose License Activation Issues 

 Convert Trial License to Production 

 Request Evaluation to Production Conversion 

 Modify a Subscription 

 Modify License Allocation 

 Extend or Renew a Subscription 

 Expiring and Expired Subscriptions 

 Deactivate a Product 

 Deactivate all Products 

 Deactivate an Individual Product 

 Tenant Management 

 What is a Tenant? 

 Add a Tenant 

 Edit a Tenant 

 Manage Tenant Licenses 

 Delete a Tenant 

 Transition from Single Tenant to Multitenant 

 Move an Internal Tenant 

 Acquire an External Tenant 

 Approve an External Tenant Acquisition 

 Limitations for Moving and Acquiring Tenants 

 Tenant Hierarchy Limits 

 Edit Telemetry Settings 

 Product Management 

 Release Updates 

 Known Issues 

 What’s New 

 Updated on 

 Fri Apr 17 11:31:28 PDT 2026 

 Focus 

 Home 

 Common Services 

 Common Services: License Activation, Subscription, & Tenant Management 

 Activate a License for Multitenant Service Provider Backbone Through Common Services 

 Download PDF 

 Common Services: License Activation, Subscription, & Tenant Management 

 Activate a License for Multitenant Service Provider Backbone Through Common Services 

 Table of Contents 

 Filter

 Expand all | Collapse all 

 Get Started with License Activation, Subscription, & Tenant Management 

 How Activation Works? 

 Firewall and SD-WAN 

 SASE 

 Remote Browser Isolation Activation 

 Prisma SD-WAN and Add-ons License Activation 

 Activate a License for Prisma SD-WAN and Add-ons 

 First Time License Activation - one CSP Account 

 First Time License Activation - multiple CSP Accounts 

 Return Visit License Activation 

 AIOPs Premium Activation 

 First Time Activation - One CSP 

 First Time Activation - Multiple CSPs 

 Return Visit Activation 

 CASB-X Activation 

 First Time Activation - One CSP 

 First Time Activation - Multiple CSPs 

 Return Visit Activation 

 Cloud Identity Engine Activation 

 First Time Activation - One CSP 

 Return Visit Activation 

 Share CIE 

 SaaS Security Inline Activation 

 First Time Activation - One CSP 

 First Time Activation - Multiple CSPs 

 Return Visit Activation 

 SaaS Security Posture Management Activation 

 First Time Activation - One CSP 

 First Time Activation - Multiple CSPs 

 Return Visit Activation 

 Convert SSPM Evaluation to Production 

 Software NGFW Credits Activation 

 Activate a Software NGFW Credits License for IoT Through 

 Activate a Software NGFW Credits License of for NGFW Through 

 Activate a Software NGFW Credits License for on Panorama Through 

 Enterprise License Agreement Add-on Activation 

 Activate ELA Through 

 Activate ELA for IoT Security Through 

 Subscription Management 

 Flexible License Management 

 Diagnose License Activation Issues 

 Convert Trial License to Production 

 Request Evaluation to Production Conversion 

 Modify a Subscription 

 Modify License Allocation 

 Extend or Renew a Subscription 

 Expiring and Expired Subscriptions 

 Deactivate a Product 

 Deactivate all Products 

 Deactivate an Individual Product 

 Tenant Management 

 What is a Tenant? 

 Add a Tenant 

 Edit a Tenant 

 Manage Tenant Licenses 

 Delete a Tenant 

 Transition from Single Tenant to Multitenant 

 Move an Internal Tenant 

 Acquire an External Tenant 

 Approve an External Tenant Acquisition 

 Limitations for Moving and Acquiring Tenants 

 Tenant Hierarchy Limits 

 Edit Telemetry Settings 

 Product Management 

 Release Updates 

 Known Issues 

 What’s New 

 Activate a License for Multitenant Service Provider Backbone Through Common Services 

 Learn how to activate a multitenant service provider (sp) backbone through Common Services . 

 Where Can I Use
 This? What Do I Need? 

 Tenant or Tenant
 Service Group (TSG) 

 Commercial deployments 

 Prisma Access license 

 Service Provider (SP) Backbone license 

 Email activation link 

 Role :
 Multitenant Superuser or Superuser 

 Service Provider (SP) Backbones enable service providers to offer granular
 Prisma Access egress traffic routes to their customers. Verify if this
 activation process applies to you . 

 SP Backbone
 activation can be done only at the top-most, root-level, parent tenant. Only one
 backbone license can be claimed per root tenant. The first step is to create a backbone configuration . After
 creating the backbone configuration, you can activate the license at the root level
 of your tenant hierarchy. After that is done, subtenants can be activated to use the
 backbone that is set up. 

 The following steps assume that
 you have already added tenants to create a multitenant hierarchy and created a backbone configuration . 

 After you receive an email from Palo Alto Networks identifying the Service
 Provider (SP) Backbone license you are activating, click the email link to begin the
 activation process. 

 Select Get Started with Service Provider Backbone in
 your email. 

 You are automatically directed to Common Services Subscription & Add-ons , where you activate the subscription for your product. 

 Select an existing top-most, root-level, parent
 Tenant : 

 Select the Customer Support Account for the tenant.

 Agree to the terms and conditions , and
 Activate . 

 Common Services Tenant Management displays the status of the activation, such as
 initializing or
 complete . 

 After the status is complete , you can activate a 
 Prisma Access (Managed by Strata Cloud Manager) license for any tenant in the multitenant hierarchy and
 assign the SP Backbone to it. 

 For Add SP Interconnect to Tenant, select one of the following: 

 Use Prisma Access backbone to use Prisma Access 
 for egress traffic. This uses public cloud providers for network
 backbone, such as: GCP, AWS, Azure. 

 Use Service Provider backbone to use internet
 service provider backbones for Prisma Access egress traffic, such as:
 BT, Orange, AT&T. Choose one of the backbones that you configured.

 If you selected to use a Service Provider backbone, you can Set
 Region Exceptions to exclude internet service provider backbones
 in these regions. The excluded regions use Prisma Access for network backbone
 instead. 

 Save and done . 

 Agree to the Terms and Conditions and
 Activate . 

 ( Optional ) Manage and monitor your service provider
 backbones and connections. 

 Previous 

 Next 

 How Activation Works? 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

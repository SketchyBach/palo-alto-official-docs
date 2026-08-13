---
url: https://docs.paloaltonetworks.com/iot/integration/get-started-with-iot-security-integrations/activate-a-third-party-integrations-add-on
fetched_at: 2026-08-13T16:37:10Z
source: palo-alto-main
---

# Activate a Third-party Integrations Cortex XSOAR Clear

Activate a Third-party Integrations Cortex XSOAR 

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

 Activate a Third-party Integrations Cortex XSOAR 

 Updated on 

 Thu May 14 09:23:33 PDT 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Device Security Docs 

 Activation & Onboarding 

 Getting Started 

 Administration 

 Enterprise Administration 

 Integrations 

 Release Notes 

 Best Practice 

 New Features 

 Updated on 

 Thu May 14 09:23:33 PDT 2026 

 Focus 

 Home 

 Device Security 

 Device Security Integration Guide 

 Get Started with Device Security Integrations 

 Activate a Third-party Integrations Cortex XSOAR 

 Download PDF 

 Device Security 

 Activate a Third-party Integrations Cortex XSOAR 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Device Security Docs 

 Activation & Onboarding 

 Getting Started 

 Administration 

 Enterprise Administration 

 Integrations 

 Release Notes 

 Best Practice 

 New Features 

 Previous 

 Get Started with Device Security Integrations 

 Next 

 Third-party Integrations Using Cohosted XSOAR 

 Activate a Third-party Integrations Cortex XSOAR 

 Activate a Device Security Third-party Integrations Cortex XSOAR for
 Device Security to integrate with third-party solutions.

 Where Can I Use This? What Do I Need? 

 Device Security (Managed by Strata Cloud Manager) 

 (Legacy) IoT Security (Standalone portal) 

 One of the following subscriptions: 

 Device Security subscription for an advanced
 Device Security product (Enterprise Plus,
 Industrial OT, or Medical)

 Device Security X subscription

 One of the following Cortex XSOAR setups:

 A free, cohosted, limited-featured
 Cortex XSOAR instance

 A full-featured Cortex XSOAR server

 Integrating with a third-party solution requires either the use of a full-featured
 Cortex XSOAR server or
 the activation of a free Device Security cloud-based, cohosted, limited
 Cortex XSOAR instance. Regardless of which Cortex XSOAR you have,
 Device Security provides access to
 all supported integrations .

 Device Security with a Cohosted Cortex XSOAR Instance

 If you want to integrate Device Security with third-party systems but don't
 have a full-featured Cortex XSOAR server, you can activate a free, limited,
 cohosted Cortex XSOAR through Device Security .
 After you activate it, IoT Security automatically generates a cohosted
 Cortex XSOAR instance with the functionality necessary to support
 Device Security integrations. When Device Security communicates with
 third-party systems, it does so through the Cortex XSOAR instance, which
 connects with other systems and runs various jobs such as importing device data into
 Device Security or sending work orders for security alerts and vulnerabilities to
 other systems for investigation and remediation.

 More information about cohosted Cortex XSOAR instances is available at
 Third-party Integrations Using Cohosted XSOAR .

 Log in to Device Security in Strata Cloud Manager . 

 The free, cohosted Cortex XSOAR is exclusive to Device Security 
 in Strata Cloud Manager . If you still access the Legacy IoT Security portal,
 take advantage of this opportunity to familiarize yourself with
 Device Security in Strata Cloud Manager .

 Navigate to Integrations Integration Management .

 Click Initialize XSOAR .

 The first time you initialize the cohosted Cortex XSOAR ,
 Device Security automatically creates the instance and associates it with
 your Device Security tenant.

 Access your Cortex XSOAR from Integrations Integration Management , clicking Manage Integrations , and
 then clicking Launch Cortex XSOAR .

 Device Security with a Full-featured Cortex XSOAR Server

 If you already have a full-featured Cortex XSOAR server deployed on premises
 or in the cloud, you can use that to integrate Device Security with
 third-party systems. For the Cortex XSOAR server to support
 Device Security third-party integrations, you must install a Device Security 
 content pack and configure an integration instance on the XSOAR server. The content
 pack provides XSOAR with all the third-party integration instance settings,
 playbooks, and jobs that Device Security requires, and the Palo Alto Networks IoT
 3rd Party integration instance allows XSOAR to establish a permanent web socket
 connection with the Device Security application.

 The Cortex XSOAR server continues to provide the same functionality it did before it was
 set up to work with Device Security . However, the Device Security integrations
 the XSOAR server supports are limited to those in the content pack you install. The
 content pack has the same set of integrations that a cohosted XSOAR instance has
 with one exception: you can modify the playbooks for Device Security integrations
 on an XSOAR server but not on a cohosted instance. To be precise, you can’t modify
 the playbooks directly, but you can duplicate them, modify the duplicate playbooks,
 and then use those on the server, which is something you can’t do in a cloud-hosted
 instance.

 When integrating Device Security with third-party systems in a deployment
 that must comply with FedRAMP Moderate, you must use a full on-premises
 Cortex XSOAR server running a vendor-approved
 FIPS version that complies with the
 FIPS 140-2 standard. This option supports all the same
 Device Security integrations as the cohosted version but is FIPS compliant.

 The Device Security web interface (and the documentation) refer to this as
 a full-featured Cortex XSOAR server,
 which is a useful way to distinguish it from a cohosted Cortex XSOAR instance.
 Nevertheless, the XSOAR server only needs to be deployed on premises to comply
 with FedRAMP regulations. If your deployment doesn’t need to be FedRAMP
 compliant, you can deploy the XSOAR server on premises or in the cloud. In
 either case, the XSOAR server connects to Device Security in the same way.

 The setup of a full-featured XSOAR server to work with Device Security is
 described in
 Third-Party Integrations Using a Full-Featured XSOAR Server .

 Cortex XSOAR Using the Device Security API

 If you have a Cortex XSOAR instance and your goal is
to integrate it with Device Security —for example, to run an automation
or playbook that downloads its inventory of IoT devices—see Palo Alto Networks IoT .
There you can learn the commands to create a direct Device Security -to-Cortex
XSOAR integration. Note that this is different from the type of
integrations in which Device Security leverages XSOAR to work with
 third-party systems as described in this guide.

 Previous 

 Get Started with Device Security Integrations 

 Next 

 Third-party Integrations Using Cohosted XSOAR 

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

 Firewalls 

 PAN-OS 

 PAN-OS SD-WAN 

 Service Provider 

 VM-Series 

 SASE 

 Prisma Access 

 Strata Multitenant Cloud Manager 

 Device Security 

 Cloud-Delivered Security Services 

 Integrations 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

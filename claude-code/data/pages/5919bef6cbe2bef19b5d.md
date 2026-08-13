---
url: https://docs.paloaltonetworks.com/iot/getting-started/prepare-your-firewall-for-iot-security/create-service-routes-for-iot-security
fetched_at: 2026-08-13T16:36:48Z
source: palo-alto-main
---

# Configure Service Routes for Device Security Clear

Configure Service Routes for Device Security 

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

 Configure Service Routes for Device Security 

 Updated on 

 Thu Jul 23 17:42:23 PDT 2026 

 Focus 

 Download PDF 

 English 

 中文 (Chinese Simplified) 

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

 Thu Jul 23 17:42:23 PDT 2026 

 Focus 

 Home 

 Device Security 

 Getting Started 

 Prepare Your Firewall for Device Security 

 Configure Service Routes for Device Security 

 Download PDF 

 English 

 中文 (Chinese Simplified) 

 Device Security 

 Configure Service Routes for Device Security 

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

 Prepare Your Firewall for Device Security 

 Next 

 Configure Policies for Log Forwarding 

 Configure Service Routes for Device Security 

 Configure service routes for your firewall to access Device Security and
 Strata Logging Service through a data interface.

 Where Can I Use This? What Do I Need? 

 NGFW (Managed by PAN-OS or Panorama) 

 Device Security (Managed by Strata Cloud Manager) 

 (Legacy) IoT Security (Standalone portal) 

 One of the following subscriptions: 

 Device Security subscription

 Precision AI bundle subscription

 Device Security X subscription

 When you configure your next-generation firewall to obtain and log network traffic
 metadata, you can use a data interface to access Strata Logging Service 
 and Device Security . To use a data interface, you need to configure
 service routes 
 and Security policy rules , and commit your
 configuration changes once you are done.

 By default, the firewall uses its management interface to send data logs to the
 logging service, get recommended policy rule sets and IP address-to-device mappings
 from Device Security , and download device dictionary files from the update
 server. When a firewall uses its management interface for all this, a service route
 and a Security policy rule are not needed.

 However, when a firewall accesses the logging service, Device Security , and
 update server through a data interface, then you must add a service route
 identifying the source data interface, source interface IP address, and service
 type. In addition, you must add an interzone Security policy rule permitting
 Data Services from 127.168.0.0/16 to the destination zone where the logging service,
 Device Security , and update server are.

 When a firewall generates traffic that it sends through a data interface, it
 uses an IP address in the 127.168.0.0/16 subnet as its internal source and then
 translates it to the IP address of the source interface. Because
 Security policy rules are applied to the original source IP address before NAT,
 the source IP address must be 127.168.0.0/16 instead of the IP address of the
 source interface.

 Configure Service Routes 

 If necessary, configure the data interface 
 you want to use as the source interface for required Device Security 
 communications.

 Select Device Setup Services Service Route Configuration and
 then select Customize .

 On the IPv4 tab, select Data Services , choose the
 data interface you want to use as the Source Interface, and then click
 OK .

 Its IP address autofills the Source Address field. This service route is
 for forwarding Enhanced Application logs (EALs) to the logging service.

 Device-ID and Device Security don’t support IPv6. 

 Click IoT , choose the same data interface as the
 Source Interface, and then click OK .

 This service route is for pulling IP address-to-device mappings and
 policy rule recommendations from Device Security .

 Click Palo Alto Networks Services , choose the same
 data interface, and then click OK .

 This service route is for forwarding other logs besides EALs to the
 logging service and for pulling device dictionary files from the
 update server.

 Click OK to save your configuration changes. 

 Add Security Policy Rules 

 When you create services routes, you need to add outbound Security policy rules
 permitting services required for the firewall to use Device Security . 

 Select Policies Security + Add .

 On the General tab, enter a name for the Security policy rule and choose
 interzone as the Rule Type.

 On the Source tab, select Any as the source zone
 and then Add 127.168.0.0/16 as the source address.

 On the Destination tab, Add the destination zone
 with Device Security , and Add the
 edge services 
 FQDN for your region as the destination address.

 On the Application tab, Add paloalto-iot-security .

 The firewall uses this application to pull IP address-to-device mappings
 and policy rule recommendations from Device Security .

 On the Actions tab, choose Allow and then click
 OK .

 Create or select an intranet policy rule that allows all intranet traffic
 in the zone where Strata Logging Service and the update server are.

 If you have an intranet policy rule that allows all intranet traffic
 in the zone where the logging service and update server are, you can
 use that rule to allow the firewall to forward logs to
 Strata Logging Service and pull dictionary files from the
 update server.

 Otherwise, create an intranet policy rule that allows the firewall to
 send these three applications to Strata Logging Service and
 update server from the IP address of the firewall interface in the
 same zone:

 paloalto-shared-services to forward EALs and
 session logs to the logging service

 paloalto-logging-service to forward other
 logs besides EALs to the logging service

 paloalto-updates to pull
 device dictionary files from the update server

 Previous 

 Prepare Your Firewall for Device Security 

 Next 

 Configure Policies for Log Forwarding 

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

 Getting Started 

 Cloud-Delivered Security Services 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

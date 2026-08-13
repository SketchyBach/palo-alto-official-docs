---
url: https://docs.paloaltonetworks.com/panorama/administration/configure-administrative-access-to-panorama/configure-an-access-domain
fetched_at: 2026-08-13T17:17:32Z
source: palo-alto-main
---

# Configure
an Access Domain Clear

Configure
an Access Domain 

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

 Configure
an Access Domain 

 Updated on 

 Thu Jul 30 16:22:01 PDT 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Panorama Docs 

 Getting Started 

 Administration 

 New Features 

 Updated on 

 Thu Jul 30 16:22:01 PDT 2026 

 Focus 

 Home 

 Panorama 

 Configure Administrative Access to Panorama 

 Configure
an Access Domain 

 Download PDF 

 Panorama 

 Configure
an Access Domain 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Panorama Docs 

 Getting Started 

 Administration 

 New Features 

 Previous 

 Configure an Admin Role Profile for Selective Push to Managed Firewalls 

 Next 

 Configure Administrative Accounts and Authentication 

 Configure
an Access Domain 

 Use Access Domains to define access for Device Group and Template administrators 

 Where Can I Use This? What Do I Need? 

 NGFW (Managed by Panorama) 

 Panorama superuser role 

 Use Access Domains to define access for Device
 Group and Template administrators for specific device groups and templates, and also
 to control the ability of those administrators to switch context to the web
 interface of managed firewalls. Panorama supports up to 4,000 access domains. 

 Select Panorama Access Domain and click Add . 

 Enter a Name to identify the access
domain. 

 Select an access privilege for Shared Objects : 

 write 

 Administrators can perform all operations on Shared objects. This is
 the default value. 

 read 

 Administrators can display and clone but cannot perform other
 operations on Shared objects. When adding non-Shared objects or
 cloning Shared objects, the destination must be a device group
 within the access domain, not the Shared location. 

 shared-only 

 Administrators can add objects only to the Shared location.
 Administrators can display, edit, and delete Shared objects but
 cannot move or clone them. 

 A consequence of this option is that administrators
can’t perform any operations on non-Shared objects other than to
display them. An example of why you might select this option is
for an organization that requires all objects to be in a single,
global repository. 

 Toggle the icons in the Device Groups tab
to enable read-write or read-only access for device groups in the
access domain. 

 If you set the Shared
Objects access to shared-only ,
Panorama applies read-only access to the objects in any device groups
for which you specify read-write access. 

 Select the Templates tab and Add each
template you want to assign to the access domain. 

 Select the Device Context tab,
select firewalls to assign to the access domain, and click OK .
Administrators can access the web interface of these firewalls by
using the Context drop-down in Panorama. 

 Previous 

 Configure an Admin Role Profile for Selective Push to Managed Firewalls 

 Next 

 Configure Administrative Accounts and Authentication 

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

 Prisma SD-WAN Experts Corner 

 Network Policy 

 QoS Whitepaper 

 Security Architecture Whitepaper 

 External Antennas for ION-C Series 

 Dynamic Path Selection 

 Best Practices 

 Best Practices Library 

 Experts Corner 

 Solutions Docs from Product Experts 

 Resources 

 All Products A - Z 

 All Release Notes 

 Compatibility Matrix 

 Experts Corner 

 Network Security Platform 

 Security Policy 

 Decryption 

 Device-ID 

 IPSec VPN 

 Quality of Service 

 Quantum Security 

 11.1 & Later 

 Next-Generation Firewall 

 Administration 

 Panorama 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

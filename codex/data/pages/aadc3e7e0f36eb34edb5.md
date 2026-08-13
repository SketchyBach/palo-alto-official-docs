---
url: https://docs.paloaltonetworks.com/vm-series/activation-and-onboarding/software-ngfw/migrate-panorama-to-a-flexible-license
fetched_at: 2026-08-13T17:41:00Z
source: palo-alto-main
---

# Migrate Panorama to a Software NGFW License Clear

Migrate Panorama to a Software NGFW License 

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

 Migrate Panorama to a Software NGFW License 

 Updated on 

 Fri Jun 19 07:15:14 PDT 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 VM-Series Firewall Docs 

 Activation & Onboarding 

 Getting Started 

 Upgrade 

 Deployment 

 Select a Document 

 Public Cloud 

 Private Cloud 

 Updated on 

 Fri Jun 19 07:15:14 PDT 2026 

 Focus 

 Home 

 VM-Series 

 Software NGFW Credits 

 Migrate Panorama to a Software NGFW License 

 Download PDF 

 VM-Series 

 Migrate Panorama to a Software NGFW License 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 VM-Series Firewall Docs 

 Activation & Onboarding 

 Getting Started 

 Upgrade 

 Deployment 

 Select a Document 

 Public Cloud 

 Private Cloud 

 Previous 

 Provision Panorama 

 Next 

 Transfer Credits 

 Migrate Panorama to a Software NGFW License 

 Migrate a single Panorama, or an HA pair from fixed VM-ELA
or a perpetual virtual Panorama licensing to a Software Next Generation
Firewall license. 

 Where Can I Use This? What Do I Need? 

 VM-Series deployment 

 VM-Series 10.x or above 

 Panorama running PAN-OS 10.1.x or above versions 

 Customer Support Portal (CSP) account with one of the
 following user roles: 
 Super User, Standard User, Limited User, Threat
 Researcher, AutoFocus Trial Role, Group Super User,
 Group Standard User, Group Limited User, Group
 Threat Researcher, Authorized Support Center (ASC)
 User, and ASC Full Service User. 

 Superuser access to the VM-Series firewall 

 You can migrate VM-ELA or perpetual virtual
Panorama licensing to Software Next Generation Firewall (Software
NGFW) licensing. 

 Migrate a Panorama with Access to the CSP 

 Complete the following procedure to migrate
your VM-ELA or perpetual virtual Panorama license to a Software
NGFW license. This migration allows you to move your existing Panorama
devices to the Software NGFW license without disruption while retaining
your existing serial number. Because your serial number does not change,
your logs and existing policies are retained. 

 Select Products Assets Software NGFW Credits and click the Details link on the
 credit pool you used to create your profile. 

 On the far right, select the vertical ellipsis (More
Options) and select Provision Panorama and
then click Migrate Existing . 

 The CSP displays all virtual Panorama devices associated
with your account. 

 Select the check box for each virtual Panorama to be
migrated. 

 Click Migrate . 

 Verify that the Current Support Expiration Date has
been updated. Additionally, you can expand each row to view the
individual licenses applied to the selected Panorama. 

 Migrate a Panorama HA Pair That Can Access the CSP 

 Complete the following procedure to migrate an HA pair with VM-ELA or perpetual licenses to a
 Software NGFW licensing. This migration allows you to move your existing
 Panorama devices to the Software NGFW license without disruption while retaining
 your existing serial number. Because your serial numbers don't change, your logs
 and the existing policies are retained. 

 Select Products Assets Software NGFW Credits and click the Details link on the
 credit pool you used to create your profile. 

 On the far right, select the vertical ellipsis (More
Options) and select Provision Panorama and
then click Migrate Existing . 

 The CSP displays all virtual Panorama devices associated
with your account. 

 Check the box for each virtual Panorama to be migrated. 

 Select Migrate . 

 Verify that the Current Support Expiration Date has
been updated. Additionally, you can expand each row to view the
individual licenses applied to the selected Panorama. 

 Migrate a Standalone Panorama That Cannot Access the CSP to a Flexible License 

 Complete the following procedure to migrate
your VM-ELA or perpetual virtual Panorama license to a Software
NGFW license even though your Panorama cannot access the CSP. Migration
without the CSP requires a serial number change, but it allows your
Panorama devices to migrate to Software NGFW licenses and retain
your existing policies. 

 The minimum version for Panorama
support is 8.1. If you must upgrade PAN-OS, do it before you start
the migration process. If you want to manage firewalls that are
using flexible vCPUs and advanced services, the PAN-OS version must be
10.0.4 or later. 

 On your Panorama, upgrade if necessary, and note
the serial number and the current support expiration date. 

 In the CSP, select Products Assets Software NGFW Credits and click the Details link on a credit
 pool. Select a deployment profile, or create one. 

 On the far right, select the vertical ellipsis (More
Options) and select Provision Panorama and
select Migrate Existing . 

 The CSP displays all virtual Panorama devices associated
with your account. 

 Check each virtual Panorama to be migrated and select Migrate . 

 On Panorama, replace the serial number with the serial number from the
 Panorama you provisioned in the CSP. Wait 1 minute, then refresh the
 page. 

 In the CSP select your provisioned Panorama and download
all licenses (the support license, the management license, and Panorama
as a log manager if your deployment profile includes it. 

 Securely pass the licenses to your Panorama. 

 Upload all Software NGFW licenses. 

 Verify that the Current Support Expiration
Date has been updated. Additionally, you can expand
each row to view the support license and/or logging license applied
to the selected Panorama. 

 Migrate an HA Pair That Cannot Access the CSP to a Flexible License 

 Use this procedure when your HA pair cannot communicate
with the CSP. This procedure initiates a failover. 

 Select Products Assets Software NGFW Credits and click the Details button on the
 credit pool. 

 On the far right, select the vertical ellipsis (More
Options) and select Provision Panorama . 

 The CSP displays all virtual Panorama devices associated
with the current support account. 

 Select Provision New , and check
the box for each virtual Panorama to be migrated and select Migrate . 

 The migrated Panoramas are displayed as Software NGFW Devices. 

 Verify that the Current Support Expiration
Date has been updated. Additionally, you can expand
each line to view the individual licenses applied to the selected
Panorama. 

 Previous 

 Provision Panorama 

 Next 

 Transfer Credits 

 On This Page 

 Activation and Onboarding 

 Strata Cloud Manager 

 Next-Generation Firewalls 

 Firewalls 

 PAN-OS 

 PAN-OS SD-WAN 

 VM-Series 

 Plugins 

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

 Resources 

 All Release Notes 

 Compatibility Matrix 

 Experts Corner 

 Network Security 

 Activation & Onboarding 

 Licensing 

 Panorama 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

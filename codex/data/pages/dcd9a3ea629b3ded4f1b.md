---
url: https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-admin/firewall-administration/reference-web-interface-administrator-access/panorama-web-interface-access-privileges
fetched_at: 2026-08-13T17:04:33Z
source: palo-alto-main
---

# Panorama Web Interface Access Privileges Clear

Panorama Web Interface Access Privileges 

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

 Panorama Web Interface Access Privileges 

 Updated on 

 Mon Aug 03 13:41:44 PDT 2026 

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

 Mon Aug 03 13:41:44 PDT 2026 

 Focus 

 Home 

 Next-Generation Firewall 

 Firewall Administration 

 Reference: Web Interface Administrator Access 

 Panorama Web Interface Access Privileges 

 Download PDF 

 Next-Generation Firewall 

 Panorama Web Interface Access Privileges 

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

 Provide Granular Access to Operations Settings 

 Next 

 Reference: Port Number Usage 

 Panorama Web Interface Access Privileges 

 Reference information for administrator access privileges and permissions in the
 Panorama web interface for centralized firewall management and configuration. 

 Where Can I Use This? What Do I Need? 

 NGFW (Managed by PAN-OS or Panorama) 

 No prerequisites needed 

 The custom Panorama administrator roles allow you to
define access to the options on Panorama and the ability to only
allow access to Device Groups and Templates ( Policies , Objects , Network , Device tabs). 

 The administrator roles you can create are Panorama and Device
Group and Template . You can’t assign CLI access privileges
to a Device Group and Template Admin Role
profile. If you assign superuser privileges for the CLI to a Panorama Admin
Role profile, administrators with that role can access all features
regardless of the web interface privileges you assign. 

 Access Level 

 Description 

 Enable 

 Read Only 

 Disable 

 Dashboard 

 Controls access to the Dashboard tab.
If you disable this privilege, the administrator will not see the
tab and will not have access to any of the Dashboard widgets. 

 Yes 

 No 

 Yes 

 ACC 

 Controls access to the Application Command
Center (ACC). If you disable this privilege, the ACC tab
will not display in the web interface. Keep in mind that if you want
to protect the privacy of your users while still providing access
to the ACC, you can disable the Privacy Show Full IP Addresses option
and/or the Show User Names In Logs And Reports option. 

 Yes 

 No 

 Yes 

 Monitor 

 Controls access to the Monitor tab.
If you disable this privilege, the administrator will not see the Monitor tab
and will not have access to any of the logs, packet captures, session
information, reports or to App Scope. For more granular control
over what monitoring information the administrator can see, leave
the Monitor option enabled and then enable or disable specific nodes on
the tab as described in Provide
Granular Access to the Monitor Tab . 

 Yes 

 No 

 Yes 

 Policies 

 Controls access to the Policies tab.
If you disable this privilege, the administrator will not see the Policies tab
and will not have access to any policy information. For more granular
control over what policy information the administrator can see,
for example to enable access to a specific type of policy or to
enable read-only access to policy information, leave the Policies option
enabled and then enable or disable specific nodes on the tab as
described in Provide
Granular Access to the Policy Tab . 

 Yes 

 No 

 Yes 

 Objects 

 Controls access to the Objects tab.
If you disable this privilege, the administrator will not see the Objects tab
and will not have access to any objects, security profiles, log forwarding
profiles, decryption profiles, or schedules. For more granular control
over what objects the administrator can see, leave the Objects option
enabled and then enable or disable specific nodes on the tab as
described in Provide
Granular Access to the Objects Tab . 

 Yes 

 No 

 Yes 

 Network 

 Controls access to the Network tab.
If you disable this privilege, the administrator will not see the Network tab
and will not have access to any interface, zone, VLAN, virtual wire,
virtual router, IPsec tunnel, DHCP, DNS Proxy, GlobalProtect, or
QoS configuration information or to the network profiles. For more
granular control over what objects the administrator can see, leave
the Network option enabled and then enable
or disable specific nodes on the tab as described in Provide
Granular Access to the Network Tab . 

 Yes 

 No 

 Yes 

 Device 

 Controls access to the Device tab.
If you disable this privilege, the administrator will not see the Device tab
and will not have access to any firewall-wide configuration information,
such as User-ID, High Availability, server profile or certificate configuration
information. For more granular control over what objects the administrator
can see, leave the Device option enabled
and then enable or disable specific nodes on the tab as described
in Provide
Granular Access to the Device Tab . 

 You can’t
enable access to the Admin Roles or Administrators nodes
for a role-based administrator even if you enable full access to
the Device tab. 

 Yes 

 No 

 Yes 

 Panorama 

 Controls access to the Panorama tab.
If you disable this privilege, the administrator will not see the Panorama tab
and will not have access to any Panorama-wide configuration information,
such as Managed Devices, Managed Collectors, or Collector Groups. 

 For
more granular control over what objects the administrator can see,
leave the Panorama option enabled and then
enable or disable specific nodes on the tab as described in Provide
Granular Access to the Panorama Tab . 

 Yes 

 No 

 Yes 

 Privacy 

 Controls access to the privacy settings described
in Define
User Privacy Settings in the Admin Role Profile . 

 Yes 

 No 

 Yes 

 Validate 

 When disabled, an administrator cannot validate
a configuration. 

 Yes 

 No 

 Yes 

 Save 

 Sets the default state (enabled or disabled) for
all the save privileges described below (Partial Save and Save For
Other Admins). 

 Yes 

 No 

 Yes 

 Partial Save 

 When disabled, an administrator cannot save
changes that any administrator made to the Panorama configuration. 

 Yes 

 No 

 Yes 

 Save For Other Admins 

 When disabled, an administrator cannot save
changes that other administrators made to the Panorama configuration. 

 Yes 

 No 

 Yes 

 Commit 

 Sets the default state (enabled or disabled) for
all the commit, push, and revert privileges described below (Panorama, Device
Groups, Templates, Force Template Values, Collector Groups, WildFire Appliance
Clusters). 

 Yes 

 No 

 Yes 

 Panorama 

 When disabled, an administrator cannot commit
or revert configuration changes that any administrators made, including
his or her own changes. 

 Yes 

 No 

 Yes 

 Commit for Other Admins 

 When disabled, an administrator cannot commit
or revert configuration changes that other administrators made. 

 Yes 

 No 

 Yes 

 Push All Changes 

 When disabled, an administrator cannot push
all configuration changes made by admins. 

 Yes 

 No 

 Yes 

 Push For Other Admins 

 When disabled, an administrator cannot select
and push configuration changes made by another admin. 

 Yes 

 No 

 Yes 

 Object Level Changes 

 When disabled, an administrator cannot select
individual configuration objects to push. 

 Yes 

 No 

 Yes 

 Device Groups 

 When disabled, an administrator cannot push
changes to device groups. 

 Yes 

 No 

 Yes 

 Templates 

 When disabled, an administrator cannot push
changes to templates. 

 Yes 

 No 

 Yes 

 Force Template Values 

 This privilege controls access to the Force Template
Values option in the Push Scope Selection dialog. 

 When
disabled, an administrator cannot replace overridden settings in
local firewall configurations with settings that Panorama pushes
from a template. 

 If you push a configuration
with Force Template Values enabled, all overridden
values on the firewall are replaced with values from the template.
Before you use this option, check for overridden values on the firewalls
to ensure your commit does not result in any unexpected network outages
or issues caused by replacing those overridden values. 

 Yes 

 No 

 Yes 

 Collector Groups 

 When disabled, an administrator cannot push
changes to Collector Groups. 

 Yes 

 No 

 Yes 

 WildFire Appliance Clusters 

 When disabled, an administrator cannot push
changes to WildFire appliance clusters. 

 Yes 

 No 

 Yes 

 Tasks 

 When disabled, an administrator cannot access
the Task Manager. 

 Yes 

 No 

 Yes 

 Global 

 Controls access to the global settings (system
alarms) described in Provide
Granular Access to Global Settings . 

 Yes 

 No 

 Yes 

 Previous 

 Provide Granular Access to Operations Settings 

 Next 

 Reference: Port Number Usage 

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

 Network Security 

 PAN-OS 

 Next-Generation Firewall 

 Administration 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

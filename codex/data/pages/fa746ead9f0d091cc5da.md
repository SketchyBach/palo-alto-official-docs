---
url: https://docs.paloaltonetworks.com/ngfw/administration/firewall-administration/manage-firewall-administrators/configure-an-admin-role-profile/configure-an-admin-role-profile-strata-cloud-manager
fetched_at: 2026-08-13T16:39:52Z
source: palo-alto-main
---

# Configure an Admin Role Profile (Strata Cloud Manager) Clear

Configure an Admin Role Profile (Strata Cloud Manager) 

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

 Configure an Admin Role Profile (Strata Cloud Manager) 

 Updated on 

 Aug 3, 2026 

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

 Aug 3, 2026 

 Focus 

 Home 

 Next-Generation Firewall 

 Firewall Administration 

 Manage Firewall Administrators 

 Configure an Admin Role Profile 

 Configure an Admin Role Profile (Strata Cloud Manager) 

 Download PDF 

 Next-Generation Firewall 

 Configure an Admin Role Profile (Strata Cloud Manager) 

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

 Configure an Admin Role Profile ( Strata Cloud Manager ) 

 In Strata Cloud Manager, you can create and customize admin role profiles to define
 granular access permissions. You can control which parts of the firewall
 configuration an administrator can manage across the web UI, REST API, XML API, and
 command line interfaces. 

 Select Device Settings Admin Roles and click Add Admin Role . 

 Enter a Name to identify the role. 

 In the Web UI and REST API tabs,
 select the required feature to toggle it to the desired setting: Enable, Read
 Only or Disable. For the XML API tab select, Enable or
 Disable. For details on the Web UI options, see Web Interface
 Access Privileges . 

 Select the Command Line tab and select a CLI access
 option. 

 None —CLI access is not permitted
 (default). 

 superuser —Full access. Can define new
 administrator accounts and virtual systems. Only a superuser can
 create administrator users with superuser privileges. 

 superreader —Full read-only access. 

 deviceadmin —Full access to all settings except
 defining new accounts or virtual systems. 

 devicereader —Read-only access to all settings
 except password profiles (no access) and administrator accounts
 (only the logged in account is visible). 

 Click OK to save the profile. 

 Assign the role to an administrator. See Configure a
 Firewall Administrator Account . 

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

 © 2026 Palo Alto Networks, Inc. All rights reserved.

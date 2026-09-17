---
url: https://docs.paloaltonetworks.com/ngfw/administration/firewall-administration/manage-firewall-administrators/configure-an-admin-role-profile/configure-an-admin-role-profile-strata-cloud-manager
fetched_at: 2026-09-16T07:25:44Z
source: palo-alto-main
---

# Configure an Admin Role Profile (Strata Cloud Manager) Clear

Updated on 

 Aug 31, 2026 

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

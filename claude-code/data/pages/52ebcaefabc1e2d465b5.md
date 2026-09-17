---
url: https://docs.paloaltonetworks.com/ngfw/help/10-2/device/device-local-user-database-users
fetched_at: 2026-09-16T07:27:11Z
source: palo-alto-main
---

# Device > Local User Database > Users Clear

Updated on 

 Thu Jun 25 17:37:48 PDT 2026 

 Focus 

 Home 

 Next-Generation Firewall 

 Device 

 Device > Local User Database > Users 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 한국어 (Korean) 

 Next-Generation Firewall 

 Device > Local User Database > Users 

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

 Device > Server Profiles > Multi Factor Authentication 

 Next 

 Device > Local User Database > User Groups 

 Device > Local User Database > Users 

 You can set up a local database on the firewall to store
authentication information for firewall administrators 

 , Authentication Portal end users 

 , and end users who
authenticate to a GlobalProtect portal 

 and GlobalProtect gateway 

 . Local database
authentication requires no external authentication service; you
perform all account management on the firewall. After creating the
local database and (optionally) assigning the users to groups (see Device
> Local User Database > User Groups ), you can Device
> Authentication Profile based on the local database. 

 You cannot configure Device
> Password Profiles for administrative accounts that use
local database authentication. 

 To Add a local user to the database, configure
the settings described in the following table. 

 Local User Settings 

 Description 

 Name 

 Enter a name to identify the user (up to
31 characters). The name is not case-sensitive and must be unique.
Use only letters, numbers, spaces, hyphens, and underscores. 

 Location 

 Select the scope in which the user account
is available. In the context of a firewall that has more than one
virtual system (vsys), select a vsys or select Shared (all
virtual systems). In any other context, you can’t select the Location ;
its value is predefined as Shared ( firewalls ) or as Panorama.
After you save the user account, you can’t change its Location . 

 Mode 

 Use this field to specify the authentication
option: 

 Password —Enter and confirm
a password for the user. 

 Password Hash —Enter a hashed password
string. This can be useful if, for example, you want to reuse the
credentials for an existing Unix account but don’t know the plaintext
password, only the hashed password. The firewall accepts any string
of up to 63 characters regardless of the algorithm used to generate
the hash value. The operational CLI command request password-hash password uses
the SHA256 algorithm in normal and CC/FIPS modes. 

 Any Minimum
Password Complexity parameters you set for the firewall ( Device Setup Management )
do not apply to accounts that use a Password Hash . 

 Enable 

 Select this option to activate the user
account. 

 Previous 

 Device > Server Profiles > Multi Factor Authentication 

 Next 

 Device > Local User Database > User Groups

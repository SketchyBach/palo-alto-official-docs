---
url: https://docs.paloaltonetworks.com/ngfw/help/12-2/configure-user-id-for-numerous-mapping-information-sources
fetched_at: 2026-09-16T08:20:54Z
source: palo-alto-main
---

# Configure User-ID for Numerous Mapping Information Sources Clear

Updated on 

 Wed Aug 19 00:09:31 PDT 2026 

 Focus 

 Home 

 Next-Generation Firewall 

 PAN-OS Web Interface Help 

 Configure User-ID for Numerous Mapping Information Sources 

 Download PDF 

 Next-Generation Firewall 

 Configure User-ID for Numerous Mapping Information Sources 

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

 Configure User-ID for Numerous Mapping Information Sources 

 Configure Windows Log Forwarding on the member
servers that will collect login events. 

 Configure
Windows Log Forwarding . This step requires administrative
privileges for configuring group policies on Windows servers. 

 Install the Windows-based User-ID agent. 

 Install
the Windows-Based User-ID Agent on a Windows server that
can access the member servers. Make sure the system that will host
the User-ID agent is a member of the same domain as the servers
it will monitor. 

 Configure the User-ID agent to collect user mapping information
from the member servers. 

 Start the Windows-based User-ID agent. 

 Select User Identification Discovery and perform the following
steps for each member server that will receive events from domain controllers: 

 In the Servers section, click Add and
enter a Name to identify the member server. 

 In the Server Address field, enter
the FQDN or IP address of the member server. 

 For the Server Type , select Microsoft
Active Directory . 

 Click OK to save the server entry. 

 Configure the remaining User-ID agent settings (refer
to Configure
the Windows-Based User-ID Agent for User Mapping ). 

 If the User-ID sources provide usernames in multiple
formats, specify the format for the Primary Username when
you Map Users to Groups . 

 The primary username is the username that identifies the
user on the firewall and represents the user in reports and logs,
regardless of the format that the User-ID source provides. 

 Configure
an LDAP server profile to specify how the firewall connects to the
Global Catalog servers (up to four) for group mapping information. 

 To improve availability, use at
least two Global Catalog servers for redundancy. 

 You
can collect group mapping information only for universal groups,
not local domain groups (subdomains). 

 Select Device Server Profiles LDAP ,
click Add , and enter a Name for
the profile. 

 In the Servers section, for each Global Catalog, click Add and
enter the server Name , IP address ( LDAP
Server ), and Port . For a plaintext
or Start Transport Layer Security ( Start TLS ) connection,
use Port 3268. For an LDAP over SSL connection,
use Port 3269. If the connection will use
Start TLS or LDAP over SSL, select the Require SSL/TLS
secured connection check box. 

 In the Base DN field, enter
the Distinguished Name (DN) of the point in the Global Catalog server
where the firewall will start searching for group mapping information
(for example, DC=acbdomain,DC=com ). 

 For the Type , select active-directory . 

 Configure an LDAP server profile to specify how the firewall
connects to the servers (up to four) that contain domain mapping
information. 

 User-ID uses this information to map DNS domain names to
NetBIOS domain names. This mapping ensures consistent domain/username
references in policy rules. 

 To improve
availability, use at least two servers for redundancy. 

 The
steps are the same as for the LDAP server profile you created for
Global Catalogs in the previous step, except for the following fields: 

 LDAP Server —Enter the IP address of the
domain controller that contains the domain mapping information. 

 Port —For a plaintext or Start TLS connection,
use Port 389. For an LDAP over SSL connection,
use Port 636. If the connection will use
Start TLS or LDAP over SSL, select the Require SSL/TLS
secured connection check box. 

 Base DN —Select the DN of the point in
the domain controller where the firewall will start searching for
domain mapping information. The value must start with the string: cn=partitions,cn=configuration (for
example, cn=partitions,cn=configuration,DC=acbdomain,DC=com ). 

 Create a group mapping configuration for each LDAP server
profile you created. 

 Select Device User Identification Group Mapping
Settings . 

 Click Add and enter a Name to
identify the group mapping configuration. 

 Select the LDAP Server Profile and
ensure the Enabled check box is selected. 

 If the Global Catalog and domain mapping
servers reference more groups than your security rules require,
configure the Group Include List and/or Custom
Group list to limit the groups for which User-ID performs
mapping. 

 Click OK and Commit .

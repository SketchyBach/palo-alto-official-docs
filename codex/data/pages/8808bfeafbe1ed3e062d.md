---
url: https://docs.paloaltonetworks.com/ngfw/help/10-2/user-identification/device-user-identification-user-mapping/user-id-agent-setup/user-id-agent-setup-syslog-filters
fetched_at: 2026-08-13T16:45:00Z
source: palo-alto-main
---

# Syslog Filters Clear

Syslog Filters 

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

 Syslog Filters 

 Updated on 

 Thu Jun 25 17:37:48 PDT 2026 

 Focus 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 한국어 (Korean) 

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

 Thu Jun 25 17:37:48 PDT 2026 

 Focus 

 Home 

 Next-Generation Firewall 

 User Identification 

 Device > User Identification > User Mapping 

 Palo Alto Networks User-ID Agent Setup 

 Syslog Filters 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 한국어 (Korean) 

 Next-Generation Firewall 

 Syslog Filters 

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

 Redistribution 

 Next 

 Ignore User List 

 Syslog Filters 

 Device User Identification User Mapping Palo Alto Networks User-ID Agent Setup Syslog Filters 

 The User-ID agent uses Syslog Parse profiles to filter syslog messages 

 sent from the syslog
senders that the agent monitors for IP address-to-username mapping
information (see Configure
Access to Monitored Servers ). Each profile can parse syslog
messages for either of the following event types, but not both: 

 Authentication (login) events—Used to add user mappings
to the firewall. 

 Logout events—Used to delete user mappings that are no longer
current. Deleting outdated mappings is useful in environments where
IP address assignments change often. 

 Palo Alto Networks provides the firewall with predefined Syslog
Parse profiles through Applications content updates. To dynamically
update the list of profiles as vendors develop new filters, schedule
these dynamic content updates (see Device
> Dynamic Updates ). The predefined profiles are global to
the firewall, whereas the custom profiles you configure apply only
to the virtual system ( Location ) selected
under Device User
Identification User Mapping . 

 Syslog messages must meet the following criteria for a User-ID
agent to parse them: 

 Each message must be a single-line text string. A new
line (\n) or a carriage return plus a new line (\r\n) are the delimiters
for line breaks. 

 The maximum size for individual messages is 8,000 bytes. 

 Messages sent over UDP must be contained in a single packet;
messages sent over SSL can span multiple packets. A single packet
might contain multiple messages. 

 To configure a custom profile, click Add and
specify the settings described in the following table. The field
descriptions in this table use a login event example from a syslog
message with the following format: 

 [Tue Jul 5 13:15:04 2005 CDT] Administrator authentication success User:domain\johndoe_4 Source:192.168.0.212 

 The complete procedure 

 to configure the
User-ID agent to parse a syslog sender for user mapping information
requires additional tasks besides creating a Syslog Parse profile. 

 Field 

 Description 

 Syslog Parse Profile 

 Enter a name for the profile (up to 63 alphanumeric characters). 

 Description 

 Enter a description for the profile (up
to 255 alphanumeric characters). 

 Type 

 Specify the type of parsing for filtering
the user mapping information: 

 Regex Identifier —Use Event
Regex , Username Regex , and Address
Regex to specify regular expressions (regex) that describe
search patterns for identifying and extracting user mapping information
from syslog messages. The firewall uses the regex to match authentication or
logout events in syslog messages and to match the usernames and
IP addresses within matching messages. 

 Field Identifier —Use the Event
String , Username Prefix , Username
Delimiter , Address Prefix , Address
Delimiter , and Addresses Per Log fields
to specify strings for matching the authentication or logout event
and for identifying the user mapping information in syslog messages. 

 The
remaining fields in the dialog vary based on your selection. Configure
the fields as described in the following rows. 

 Event Regex 

 Enter the regex for identifying successful
authentication or logout events. For the example message used with
this table, the regex (authentication\ success) {1} extracts
the first {1} instance of the string authentication success .
The backslash before the space is a standard regex escape character
that instructs the regex engine not to treat the space as a special
character. 

 Username Regex 

 Enter the regex for identifying the username
field in authentication success or logout messages. For the example message
used with this table, the regex User:([a-zA-Z0-9\\\._]+) would match
the string User:johndoe_4 and extract acme\johndoe1
as the username. 

 Address Regex 

 Enter the regex to identify the IP address
portion of authentication success or logout messages. In the example message
used with this table, the regular expression Source:([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}) matches
the IPv4 address Source:192.168.0.212 and adds
192.168.0.212 as the IP address in the username mapping. 

 Event String 

 Enter a matching string to identify authentication
success or logout messages. For the example message used with this table,
you would enter the string authentication success . 

 Username Prefix 

 Enter the matching string to identify the
beginning of the username field within authentication or logout
syslog messages. The field does not support regex expressions such
as \s (for a space) or \t (for
a tab). In the example message used with this table, User: identifies
the start of the username field. 

 Username Delimiter 

 Enter the delimiter that marks the end of
the username field within an authentication or logout message. Use
\s to indicate a standalone space (as in the example message) and
\t to indicate a tab. 

 Address Prefix 

 Enter a matching string to identify the
start of the IP address field in syslog messages. The field does
not support regex expressions such as \s (for
a space) or \t (for a tab). In the example message
used with this table, Source: identifies
the start of the address field. 

 Address Delimiter 

 Enter the matching string that marks the
end of the IP address field within authentication success or logout
messages. For example, enter \n to indicate
the delimiter is a line break. 

 Addresses Per Log 

 Enter the maximum number of IP addresses
that you want the firewall to parse (default is 1; range is 1—3). 

 Previous 

 Redistribution 

 Next 

 Ignore User List 

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

 PAN-OS 

 10.2 

 Next-Generation Firewall 

 Help 

 Web Interface 

 Panorama 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

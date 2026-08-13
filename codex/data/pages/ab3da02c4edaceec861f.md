---
url: https://docs.paloaltonetworks.com/ngfw/help/10-1/panorama-web-interface/panorama-scheduled-config-export
fetched_at: 2026-08-13T16:42:38Z
source: palo-alto-main
---

# Panorama > Scheduled Config Export Clear

Panorama > Scheduled Config Export 

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

 Panorama > Scheduled Config Export 

 Updated on 

 Mon Jan 12 14:16:08 PST 2026 

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

 Mon Jan 12 14:16:08 PST 2026 

 Focus 

 Home 

 Next-Generation Firewall 

 Panorama Web Interface 

 Panorama > Scheduled Config Export 

 Download PDF 

 Next-Generation Firewall 

 Panorama > Scheduled Config Export 

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

 Panorama > Server Profiles > SCP 

 Next 

 Panorama > Software 

 Panorama > Scheduled Config Export 

 To schedule an export of all the running configurations on
Panorama and firewalls, Add an export task
and configure the settings as described in the following table. 

 If Panorama has a high availability (HA)
configuration, you must perform these instructions on each peer
to ensure the scheduled exports continue after a failover. Panorama
does not synchronize scheduled configuration exports between HA
peers. 

 Scheduled Configuration Export
Settings 

 Description 

 Name 

 Enter a name to identify the configuration
export job (up to 31 characters). The name is case-sensitive and
must be unique. Use only letters, numbers, hyphens, and underscores. 

 Description 

 Enter an optional description. 

 Enable 

 Select to enable the export job. 

 Scheduled export start time (daily) 

 Specify the time of day to start the export
(24 hour clock, format HH:MM). 

 Protocol 

 Select the protocol to use to export logs
from Panorama to a remote host. Secure Copy ( SCP )
is a secure protocol; FTP is not. 

 Hostname 

 Enter the IP address or hostname of the
target SCP or FTP server. 

 Port 

 Enter the port number on the target server. 

 Path 

 Specify the path to the folder or directory
on the target server that will store the exported configuration. 

 For
example, if the configuration bundle is stored in a folder called
exported_config within a top level folder called Panorama, the syntax
for each server type is: 

 SCP server: /Panorama/exported_config 

 FTP server: //Panorama/exported_config 

 The
following characters: . (period), + , { and } , / , - , _ , 0 - 9 , a - z ,
and A - Z . Spaces are
not supported in the file Path . 

 Enable FTP Passive Mode 

 Select to use FTP passive mode. 

 Username 

 Specify the username required to access
the target system. 

 Password / Confirm Password 

 Specify the password required to access
the target system. 

 Use a password with maximum length of 15
characters. If the password exceeds 15 characters, the test SCP
connection will display an error because the firewall encrypts the
password when it tries to connect to the SCP server and the length
of the encrypted password can be up to 63 characters only. 

 Test SCP server connection 

 Select to test communication between Panorama
and the SCP host/server. 

 ( PAN-OS 10.1.8 and earlier releases ) To enable the secure transfer of data, you must
 verify and accept the host key of the SCP server. The connection is
 not established until the host key is accepted. If Panorama has an
 HA configuration, you must perform this verification on each HA peer
 so that each one accepts the host key of the SCP server. 

 ( PAN-OS 10.1.9 and later releases ) A pop-up window is
 displayed requiring you to enter a clear text
 Password and then to Confirm
 Password in order to test the SCP server connection
 and enable the secure transfer of data. If Panorama has an HA
 configuration, perform this step on each HA peer so that each one
 can successfully connect to the SCP server. If Panorama can
 successfully connect to the SCP server. 

 Previous 

 Panorama > Server Profiles > SCP 

 Next 

 Panorama > Software 

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

 10.1 

 PAN-OS 

 Next-Generation Firewall 

 Help 

 Web Interface 

 Panorama 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

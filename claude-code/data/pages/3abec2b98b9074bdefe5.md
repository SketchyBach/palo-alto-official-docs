---
url: https://docs.paloaltonetworks.com/ngfw/help/10-1/device/device-setup-wildfire
fetched_at: 2026-08-13T16:41:28Z
source: palo-alto-main
---

# Device > Setup > WildFire Clear

Device > Setup > WildFire 

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

 Device > Setup > WildFire 

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

 Device 

 Device > Setup > WildFire 

 Download PDF 

 Next-Generation Firewall 

 Device > Setup > WildFire 

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

 Device > Setup > Content-ID 

 Next 

 Device > Setup > Session 

 Device > Setup > WildFire 

 Select Device Setup WildFire to
configure WildFire settings on the firewall and
Panorama. You can enable both the WildFire cloud and a WildFire
appliance to be used to perform file analysis. You can also set
file size limits and session information that will be reported.
After populating WildFire settings, you can specify what files to
forward to the WildFire cloud or the WildFire appliance by creating
a WildFire Analysis profile ( Objects Security Profiles WildFire Analysis ). 

 To forward decrypted content to WildFire, refer to Forward Decrypted SSL Traffic for WildFire Analysis . 

 WildFire Settings 

 Description 

 General Settings 

 WildFire Public Cloud 

 Enter wildfire.paloaltonetworks.com to
send files to the WildFire global cloud (U.S.), hosted in the United
States, for analysis. Alternatively, you can instead send files
to a WildFire regional cloud for
analysis. Regional clouds are designed to adhere to the data privacy
expectations you might have depending on your location. 

 Forward samples to a regional WildFire cloud
to ensure adherence to the data privacy and compliance standards specific
to your region. Regional clouds are: 

 Europe— eu.wildfire.paloaltonetworks.com 

 Japan— jp.wildfire.paloaltonetworks.com 

 Singapore— sg.wildfire.paloaltonetworks.com 

 United Kingdom— uk.wildfire.paloaltonetworks.com 

 Canada— ca.wildfire.paloaltonetworks.com 

 Australia— au.wildfire.paloaltonetworks.com 

 Germany— de.wildfire.paloaltonetworks.com 

 India— in.wildfire.paloaltonetworks.com 

 WildFire Private Cloud 

 Specify the IPv4/IPv6 address or FQDN of
the WildFire appliance. 

 The firewall sends files for analysis
to the specified WildFire appliance. 

 Panorama collects threat
IDs from the WildFire appliance to enable the addition of threat
exceptions in Anti-Spyware profiles (for DNS signatures only) and
Antivirus profiles that you configure in device groups. Panorama
also collects information from the WildFire appliance to populate
fields that are missing in the WildFire Submissions logs received
from firewalls running software versions earlier than PAN-OS 7.0. 

 File Size Limits 

 Specify the maximum file size that will
be forwarded to the WildFire server. For all best practice recommendations
about file size limits, if the limit is too large and prevents the
firewall from forwarding multiple large zero-day files at the same
time, lower and tune the maximum limit based on the amount of available
firewall buffer space. If more buffer space is available, you can
increase the file size limit above the best practice recommendation.
The best practice recommendations are a good starting place for
setting effective limits that don’t overtax firewall resources.
Available ranges are: 

 pe (Portable
Executable)—Range is 1 to 50MB; default is 16MB. 

 Set the size for PE files to 16MB. 

 apk (Android Application)—Range is
1 to 50MB; default 10MB. 

 Set the size
for APK files to 10MB. 

 pdf (Portable Document Format)—Range
is 100KB to 51,200KB; default is 3,072KB. 

 Set
the size for PDF files to 3,072KB. 

 ms-office (Microsoft Office)—Range
is 200KB to 51,200KB; default is 16,384KB. 

 Set
the size for ms-office files to 16,384KB. 

 jar (Packaged Java class file)—Range
is 1 to 20MB; default is 5MB. 

 Set
the size for jar files to 5MB. 

 flash (Adobe Flash)—Range is 1 to
10MB; default is 5MB. 

 Set the size
for flash files to 5MB. 

 MacOSX (DMG/MAC-APP/MACH-O PKG files)—Range
is 1 to 50MB; default is 10MB. 

 Set
the size for MacOSX files to 1MB. 

 archive (RAR and 7z files)—Range is
1 to 50MB; default is 50MB. 

 Set the
size for archive files to 50MB. 

 linux (ELF files)—Range is 1 to 50MB;
default is 50MB. 

 Set the size for
linux files to 50MB. 

 script (JScript, VBScript, PowerShell,
and Shell Script files)—Range is 10 to 4096KB; default is 20KB. 

 Set the size for script files to 20KB. 

 The
preceding values might differ based on the current version of PAN-OS
or the content release. To see valid ranges, click in the Size
Limit field; a pop-up displays the available range and
default value. 

 Report Benign Files 

 When this option is enabled (disabled by
default), files analyzed by WildFire that are determined to be benign
will appear in the Monitor WildFire Submissions log. 

 Even
if this option is enabled on the firewall, email links that WildFire
deems benign will not be logged because of the potential quantity
of links processed. 

 Report Grayware Files 

 When this option is enabled (disabled by
default), files analyzed by WildFire that are determined to be grayware
will appear in the Monitor WildFire Submissions log. 

 Even
if this option is enabled on the firewall, email links that WildFire
determines to be grayware will not be logged because of the potential
quantity of links processed. 

 Enable
reporting grayware files to log session information, network activity,
host activity, and other information that helps with analytics. 

 Session Information Settings 

 Settings 

 Specify the information to be forwarded
to the WildFire server. By default, all are selected and the best
practice is to forward all session information to provide statistics
and other metrics that enable you to take actions to prevent threat
events: 

 Source IP —Source IP address
that sent the suspected file. 

 Source Port —Source port that sent
the suspected file. 

 Destination IP —Destination IP address
for the suspected file. 

 Destination Port —Destination port
for the suspected file. 

 Vsys —Firewall virtual system that
identified the possible malware. 

 Application —User application that
was used to transmit the file. 

 User —Targeted user. 

 URL —URL associated with the suspected
file. 

 Filename —Name of the file that was
sent. 

 Email sender —Provides the sender name
in WildFire logs and WildFire detailed reports when a malicious
email link is detected in SMTP and POP3 traffic. 

 Email recipient —Provides the recipient
name in WildFire logs and WildFire detailed reports when a malicious
email link is detected in SMTP and POP3 traffic. 

 Email subject —Provides the email subject
in WildFire logs and WildFire detailed reports when a malicious
email link is detected in SMTP and POP3 traffic. 

 Previous 

 Device > Setup > Content-ID 

 Next 

 Device > Setup > Session 

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

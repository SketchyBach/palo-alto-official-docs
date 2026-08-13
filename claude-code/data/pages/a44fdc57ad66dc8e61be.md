---
url: https://docs.paloaltonetworks.com/ngfw/help/10-2/panorama-web-interface/panorama-device-deployment/schedule-dynamic-content-updates
fetched_at: 2026-08-13T16:44:33Z
source: palo-alto-main
---

# Schedule Dynamic Content Updates Clear

Schedule Dynamic Content Updates 

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

 Schedule Dynamic Content Updates 

 Updated on 

 Jun 25, 2026 

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

 Jun 25, 2026 

 Focus 

 Home 

 Next-Generation Firewall 

 Panorama Web Interface 

 Panorama > Device Deployment 

 Schedule Dynamic Content Updates 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 한국어 (Korean) 

 Next-Generation Firewall 

 Schedule Dynamic Content Updates 

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

 Display Software and Content Update Information 

 Next 

 Revert Content Versions from Panorama 

 Schedule Dynamic Content Updates 

 Panorama > Device Deployment
> Dynamic Updates 

 To schedule an automatic download
and installation of an update , click Schedules , click Add ,
and configure the settings as described in the following table. 

 Dynamic
Update Schedule Settings 

 Name 

 Enter a name to identify the scheduled job
(up to 31 characters). The name is case-sensitive, must be unique,
and can contain only letters, numbers, hyphens, and underscores. 

 Disabled 

 Select to disable the scheduled job. 

 Download Source 

 Select the download source for the content
update. You can select to download content updates from the Palo
Alto Networks Updates Server or from an SCP server. 

 SCP Profile ( SCP only ) 

 Select a configured SCP profile from which
to download. 

 SCP Path ( SCP only ) 

 Enter the specific path on the SCP server
from which to download the content update. 

 Type 

 Select the type of content update to schedule: App , App
and Threat , Antivirus , WildFire ,
or URL Database . 

 Recurrence 

 Select the interval at which Panorama checks
in with the update server. The recurrence options vary by update
type. 

 Time 

 For a Daily update,
select the Time from the 24-hour clock. 

 For
a Weekly update, select the Day of
week, and the Time from the 24-hour clock. 

 Disable new apps in content update 

 You can disable new apps in content updates
only if you set the update Type to App or App
and Threat and only if Action is
set to Download and Install . 

 Select
to disable applications in the update that are new relative to the
last installed update. This protects against the latest threats
while giving you the flexibility to enable the applications after
preparing any policy updates. Then, to enable applications, log
in to the firewall, select Device Dynamic Updates , click Apps in
the Features column to display the new applications, and click Enable/Disable for
each application you want to enable. 

 Action 

 Download Only —Panorama™
will download the scheduled update. You must manually install the
update on firewalls and Log Collectors. 

 Download and Install —Panorama will
download and automatically install the scheduled update. 

 Download and SCP —Panorama will download
and transfer the content update package to the specified SCP server. 

 Devices 

 Select Devices and
then select the firewalls that will receive scheduled content updates. 

 Log Collectors 

 Select Log Collectors and
then select the managed collectors that will receive scheduled content
updates. 

 Previous 

 Display Software and Content Update Information 

 Next 

 Revert Content Versions from Panorama 

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

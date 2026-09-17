---
url: https://docs.paloaltonetworks.com/ngfw/help/10-2/device/device-setup-telemetry
fetched_at: 2026-09-16T07:27:18Z
source: palo-alto-main
---

# Device > Setup > Telemetry Clear

Updated on 

 Thu Jun 25 17:37:48 PDT 2026 

 Focus 

 Home 

 Next-Generation Firewall 

 Device 

 Device > Setup > Telemetry 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 한국어 (Korean) 

 Next-Generation Firewall 

 Device > Setup > Telemetry 

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

 Device > Setup > Interfaces 

 Next 

 Device > Setup > Content-ID 

 Device > Setup > Telemetry 

 Telemetry is the process of collecting and transmitting data for threat and support
 analysis, and to enable application logic. To collect and transmit telemetry to 
 Palo Alto Networks, you must first select a destination region. If your organization
 currently has a Strata Logging Service license, then your destination region is limited to
 the region where your Strata Logging Service instance resides.

 Telemetry data is used to power applications that increase your ability to manage and
 configure your Palo Alto Networks products and services. These apps offer you improved
 visibility into device health, performance, capacity planning, and configuration. Palo Alto
 Networks also continually uses this data to improve threat prevention, and to help you
 maximize your product usage benefits.

 Select Device Setup Telemetry to see the
 currently collected telemetry categories. To change these categories, edit the Telemetry
 widget. Deselect any categories that you don't want the firewall to collect, and commit your change.

 Generate Telemetry File to obtain a live example of the data that
 the firewall will send to Palo Alto Networks at the next 

 telemetry transmission interval .

 To disable telemetry transmission entirely, make sure Enable Telemetry is not checked, and commit your change.

 Telemetry Autoenablement 

 Beginning with PAN-OS 10.2.17, 11.1.11, 11.2.8, 12.1.2, and later releases, the
 telemetry autoenablement feature configures telemetry to be enabled by default on your
 devices. When you onboard a new device, telemetry is automatically enabled. Its settings are
 centrally managed through Strata Cloud Manager, rather than on individual devices. This
 centralized method ensures uniform telemetry settings across your entire environment.
 Metrics are streamed automatically to your data residency region, removing the need for
 manual setup. 

 You can view the read-only telemetry status and tiers by navigating to Device Setup Telemetry . There are two tiers: 

 Diagnostic tier provides essential information to determine system
 operational status and pinpoint immediate causes of system failures. 

 Full tier provides specialized, granular, and feature-rich capabilities that
 expand upon the Diagnostic tier. 

 You can manage telemetry settings from either your hub or
 Strata Cloud Manager. 

 Previous 

 Device > Setup > Interfaces 

 Next 

 Device > Setup > Content-ID

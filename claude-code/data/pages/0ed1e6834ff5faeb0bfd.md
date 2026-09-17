---
url: https://docs.paloaltonetworks.com/ngfw/incidents-and-alerts/incidents/firewall-disconnected-from-strata-cloud-manager
fetched_at: 2026-09-16T07:32:31Z
source: palo-alto-main
---

# Firewall Disconnected from Strata Cloud Manager Clear

Updated on 

 Thu Aug 20 10:58:28 PDT 2026 

 Focus 

 Home 

 Next-Generation Firewall 

 Incidents 

 NGFW Incidents Reference 

 Firewall Disconnected from Strata Cloud Manager 

 Download PDF 

 Next-Generation Firewall 

 Firewall Disconnected from Strata Cloud Manager 

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

 Firewall Disconnected from Panorama 

 Next 

 Firewall Disconnected from Strata Logging Service 

 Firewall Disconnected from Strata Cloud Manager 

 Incident Code 

 INC_NGFW_TO_MANAGING_SCM_CONNECTIVITY 

 Severity 

 Warning 

 Category 

 Device 

 Subcategory 

 Management 

 Description 

 This incident triggers when the connection between the firewall and Strata Cloud
 Manager has been lost 

 Raise Condition 

 This incident is raised when a Next--Generation Firewall (NGFW) loses its
 connection for more than 1 hour to its managing Strata Cloud Manager (SCM). This
 indicates that the firewall is currently unable to communicate with its central
 management, which may impact policy updates, logging, and monitoring. The system
 will continue to try and re-establish the connection. 

 Clear Condition 

 This incident will clear automatically as soon as the connection between the NGFW
 and Strata Cloud Manager (SCM) is successfully restored and stays connected for
 atleast 2 hour. If a firewall is permanently decommissioned while this incident is
 active, the incident will be automatically cleared after a 90-day grace
 period. 

 Previous 

 Firewall Disconnected from Panorama 

 Next 

 Firewall Disconnected from Strata Logging Service

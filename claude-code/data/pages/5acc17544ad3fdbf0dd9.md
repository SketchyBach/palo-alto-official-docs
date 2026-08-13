---
url: https://docs.paloaltonetworks.com/iot/integration/security-information-and-event-management/send-vulnerabilities-to-siem
fetched_at: 2026-08-13T16:37:28Z
source: palo-alto-main
---

# Send Vulnerabilities to SIEM Clear

Send Vulnerabilities to SIEM 

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

 Send Vulnerabilities to SIEM 

 Updated on 

 Thu May 14 09:23:33 PDT 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Device Security Docs 

 Activation & Onboarding 

 Getting Started 

 Administration 

 Enterprise Administration 

 Integrations 

 Release Notes 

 Best Practice 

 New Features 

 Updated on 

 Thu May 14 09:23:33 PDT 2026 

 Focus 

 Home 

 Device Security 

 Device Security Integration Guide 

 Security Information and Event Management 

 Send Vulnerabilities to SIEM 

 Download PDF 

 Device Security 

 Send Vulnerabilities to SIEM 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Device Security Docs 

 Activation & Onboarding 

 Getting Started 

 Administration 

 Enterprise Administration 

 Integrations 

 Release Notes 

 Best Practice 

 New Features 

 Previous 

 Send Security Alerts to SIEM 

 Next 

 Network Access Control 

 Send Vulnerabilities to SIEM 

 Manually send device vulnerabilities from Device Security through Cortex XSOAR 
 to SIEM.

 Where Can I Use This? What Do I Need? 

 Device Security (Managed by Strata Cloud Manager) 

 (Legacy) IoT Security (Standalone portal) 

 One of the following subscriptions: 

 Device Security subscription for an advanced
 Device Security product (Enterprise Plus,
 Industrial OT, or Medical)

 Device Security X subscription

 One of the following Cortex XSOAR setups:

 A free, cohosted, limited-featured
 Cortex XSOAR instance

 AND 

 A free Cortex XSOAR Engine (on-premises integration)

 A full-featured Cortex XSOAR server

 From Device Security , send a device vulnerability to SIEM from the
 Vulnerability Details page. You can also do this in the Actions menu in the
 Vulnerabilities section on the Device Details page.

 By integrating Device Security through Cortex XSOAR with a third-party SIEM server,
 XSOAR automatically exports data about devices, security alerts, and device
 vulnerability in periodic incremental updates from Device Security to SIEM. Therefore,
 it might be unnecessary to send a vulnerability to SIEM manually. However, if you
 haven’t performed a bulk export to SIEM and you want to send a device vulnerability
 that wasn’t exported through the automatic incremental update process, then you can
 use this option to send it manually.

 Strata Cloud Manager 

 Legacy IoT Security 

 Strata Cloud Manager 

 Manually send device vulnerabilities from Device Security in Strata Cloud Manager 
 through Cortex XSOAR to SIEM.

 Select a vulnerability to investigate. 

 Log in to Device Security in Strata Cloud Manager , click Risks Vulnerabilities , click a vulnerability name, and then select the check box of
 an active instance that you want to investigate.

 The Send to SIEM panel appears. 

 Add a comment. 

 After you enter a comment, the Send button changes from
gray to blue, indicating that you can proceed. 

 Click Send . 

 After you click Send , a link appears. When you click it, a new browser
 window opens to the Cortex XSOAR playbook for this action. 

 To confirm
that the vulnerability was sent, click the link to the XSOAR playbook for
this action. 

 For the link in Device Security to open the
corresponding playbook in Cortex XSOAR , you must already be logged
in to your XSOAR instance before clicking it. 

 The green
boxes in the playbook indicate that a particular step was successfully
performed. Following the path through the playbook gives you feedback
about whether an action was carried out successfully or, if not,
where the process changed course. 

 Also, the action “Sent to
SIEM” appears in the Vulnerability Responses column. If you don’t see this column, click
 the Columns icon ( 

 )
 and select Vulnerability Responses . 

 Legacy IoT Security 

 Manually send device vulnerabilities from the Device Security portal
 through Cortex XSOAR to SIEM.

 Select a vulnerability to investigate. 

 Log in to the Device Security portal, click Vulnerabilities Vulnerability Overview All Vulnerabilities , click a vulnerability name, and then select the check box of
 an active instance that you want to investigate.

 The Send to SIEM panel appears. 

 Add a comment. 

 After you enter a comment, the Send button changes from
gray to blue, indicating that you can proceed. 

 Click Send . 

 After you click Send , a link appears. When you click it, a new browser
 window opens to the Cortex XSOAR playbook for this action. 

 To confirm
that the vulnerability was sent, click the link to the XSOAR playbook for
this action. 

 For the link in Device Security to open the
corresponding playbook in Cortex XSOAR , you must already be logged
in to your XSOAR instance before clicking it. 

 The green
boxes in the playbook indicate that a particular step was successfully
performed. Following the path through the playbook gives you feedback
about whether an action was carried out successfully or, if not,
where the process changed course. 

 Also, the action “Sent to
SIEM” appears in the Vulnerability Responses column. If you don’t see this column, click
 the Columns icon ( 

 )
 and select Vulnerability Responses . 

 Previous 

 Send Security Alerts to SIEM 

 Next 

 Network Access Control 

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

 Firewalls 

 PAN-OS 

 PAN-OS SD-WAN 

 Service Provider 

 VM-Series 

 SASE 

 Prisma Access 

 Strata Multitenant Cloud Manager 

 Device Security 

 Cloud-Delivered Security Services 

 Integrations 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

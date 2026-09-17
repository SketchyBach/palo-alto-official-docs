---
url: https://docs.paloaltonetworks.com/iot/integration/asset-management/integrate-iot-security-with-servicenow/send-security-alerts-to-servicenow
fetched_at: 2026-09-16T07:23:37Z
source: palo-alto-main
---

# Send Security Alerts to ServiceNow Clear

Updated on 

 Mon Aug 17 11:22:37 PDT 2026 

 Focus 

 Home 

 Device Security 

 Device Security Integration Guide 

 Asset Management 

 Integrate Device Security with ServiceNow 

 Send Security Alerts to ServiceNow 

 Download PDF 

 Device Security 

 Send Security Alerts to ServiceNow 

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

 Set up Device Security and XSOAR for ServiceNow Integration 

 Next 

 Send Vulnerabilities to ServiceNow 

 Send Security Alerts to ServiceNow 

 Manually send security alerts from Device Security through Cortex XSOAR to
 ServiceNow to make work orders.

 Where Can I Use This? What Do I Need? 

 Device Security (Managed by Strata Cloud Manager) 

 (Legacy) IoT Security (Standalone portal) 

 One of the following subscriptions: 

 Device Security subscription

 Precision AI bundle subscription

 Device Security X subscription

 One of the following Cortex XSOAR setups:

 A free, cohosted, limited-featured
 Cortex XSOAR instance

 A full-featured Cortex XSOAR server

 From Device Security , send a security
alert to ServiceNow. Before sending it, Device Security converts the
alert into a security incident, which ServiceNow receives in its
Zingbox alerts vulnerability incident table. From there, a ServiceNow
 user can create a work order for a network security analyst to investigate. 

 Strata Cloud Manager 

 Legacy IoT Security 

 Strata Cloud Manager 

 Manually send security alerts from Device Security in Strata Cloud Manager 
 through Cortex XSOAR to ServiceNow to make work orders.

 Log in to Device Security in Strata Cloud Manager , click Alerts Security Alerts , and then select the check box of the alert you want to send as an
incident to ServiceNow. 

 Click More Send to ServiceNow . 

 The Send
to ServiceNow panel appears. 

 Add a comment and then click Send . 

 After you
click Send , a link appears. When you click
it, a new browser window opens to the XSOAR playbook for this action. 

 To confirm that the work
 order was sent, click the link to the XSOAR playbook for
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
ServiceNow” appears in the Last Action column. If you don’t see
this column, click the Columns icon ( 

 ) and select Last
Action . 

 Log in to ServiceNow and check the table you created
for receiving security incidents from Device Security . 

 You
can also send an alert to ServiceNow from the Alert Details page
and from the Alerts section on the Device Details page. 

 Legacy IoT Security 

 Manually send security alerts from the Device Security portal
 through Cortex XSOAR to ServiceNow to make work orders.

 Log in to the Device Security portal, click Alerts Security Alerts All Alerts , and then select the check box of the alert you want to send as an
incident to ServiceNow. 

 Click More Send to ServiceNow . 

 The Send to ServiceNow panel appears. 

 Add a comment and then click Send . 

 After you
click Send , a link appears. When you click
it, a new browser window opens to the XSOAR playbook for this action. 

 To confirm that the work
 order was sent, click the link to the XSOAR playbook for
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
ServiceNow” appears in the Last Action column. If you don’t see
this column, click the Columns icon ( 

 ) and select Last
Action . 

 Log in to ServiceNow and check the table you created
for receiving security incidents from Device Security . 

 You
can also send an alert to ServiceNow from the Alert Details page
and from the Alerts section on the Device Details page. 

 Previous 

 Set up Device Security and XSOAR for ServiceNow Integration 

 Next 

 Send Vulnerabilities to ServiceNow

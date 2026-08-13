---
url: https://docs.paloaltonetworks.com/iot/integration/vulnerability-scanning/integrate-iot-security-with-qualys/perform-a-vulnerability-scan-using-qualys
fetched_at: 2026-08-13T16:37:28Z
source: palo-alto-main
---

# Perform a Vulnerability Scan Using Qualys Enterprise TruRisk Clear

Perform a Vulnerability Scan Using Qualys Enterprise TruRisk 

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

 Perform a Vulnerability Scan Using Qualys Enterprise TruRisk 

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

 Vulnerability Scanning 

 Integrate Device Security with Qualys Enterprise TruRisk 

 Perform a Vulnerability Scan Using Qualys Enterprise TruRisk 

 Download PDF 

 Device Security 

 Perform a Vulnerability Scan Using Qualys Enterprise TruRisk 

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

 Set up Device Security and XSOAR for Qualys Enterprise TruRisk Integration 

 Next 

 Integrate Device Security with Rapid7 

 Perform a Vulnerability Scan Using Qualys Enterprise TruRisk 

 Use Device Security integration with Qualys to perform a vulnerability scan.

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

 A full-featured Cortex XSOAR server

 Because active scanning can be disruptive
to the services running on a scanned device, only account owners
have permission to perform vulnerability scans by default. Owners
can also set scanning permissions per administrator account, thereby
delegating it to just a few individuals. 

 By default, vulnerability
scanning is disabled for new administrator accounts. To enable it,
log in to the Device Security portal as an owner, click Administration User Accounts ,
and then click the email address (username) of an administrator
for whom you want to enable vulnerability scanning. Slide the Allow
device vulnerability scans toggle from Off to On and
then Save . 

 The
ability to do vulnerability scanning is only available to owners
and administrators. There is no option to enable vulnerability scanning
for deployment and read-only users. 

 Initiate a Qualys vulnerability scan from IoT
Security. 

 Log in as an owner or administrator who has vulnerability scanning
enabled, click Devices , and then click the
entry in the Device Name column for the device you want to scan. 

 Because Device Security only supports one vulnerability scan
of a device at a time, make sure no other scans of this device are
currently in progress. 

 Click Reports Vulnerability Scan Reports and
check the Status column. If you see Processing... for the
device you want to scan, wait until the current scan finishes before
starting a new one. 

 When
you see that the device isn’t already being scanned, you can continue with
a new scan. 

 Only initiate a scan of a device that’s
in the Qualys inventory and that’s not currently active (and will
remain inactive until the scan completes). 

 Click Devices and then click the entry
in the Device Name column for the device you want to scan. 

 At the top of the Device Details page, click the Action menu
(three vertical dots) and then click Scan . 

 Read the caution about scanning active devices and, if the
device is currently inactive, Continue . 

 Set parameters for the vulnerability scan you want Qualys
to perform. 

 Select the scan engine to perform the vulnerability scan
and a profile to define the type of scan to run. Qualys provides
a set of predefined profiles. You can also define and use your own. 

 Click Scan . 

 While the scan is in progress, a label appears at the top
of the Device Details page indicating its status. 

 When done,
the label changes to show that the scan either failed or succeeded. You
also receive an email alerting you that the report is ready. 

 Download the vulnerability scan report, which is in PDF format. 

 You have three options for viewing the report: 

 Click
the Vulnerability Report Ready label at the
top of the Device Details page. 

 Navigate to Reports Vulnerability Scan Reports and
then click the report name. 

 Click Download Report in the email
message. This opens the Reports Vulnerability Scan Reports page
where you can download the report. 

 Open the report in a PDF viewer. 

 The report consists of three major sections: Report Summary,
Summary of Vulnerabilities, and Detailed Results. 

 Device Security incorporates
the results of the vulnerability scan into the risk score calculations
for the device. In addition, any CVEs included in the scan report
are made available in the Risks section on the Device Details page
and on the Risks Vulnerabilities page.
 Device Security immediately updates the risk score and CVEs on
the Device Details page. Updates to the CVEs on the Risks Vulnerabilities page
are not made immediately and can take up to 24 hours to appear. 

 Previous 

 Set up Device Security and XSOAR for Qualys Enterprise TruRisk Integration 

 Next 

 Integrate Device Security with Rapid7 

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

---
url: https://docs.paloaltonetworks.com/cloud-ngfw/azure/cloud-ngfw-for-azure/logging/view-audit-logs-on-resource-groups
fetched_at: 2026-08-13T15:31:12Z
source: palo-alto-main
---

# View Audit Logs on Resource Groups Clear

View Audit Logs on Resource Groups 

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

 View Audit Logs on Resource Groups 

 Updated on 

 Mon Jun 29 22:22:17 PDT 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Cloud NGFW for Azure Docs 

 Getting Started 

 Deployment 

 Administration 

 Reference 

 Release Notes 

 New Features 

 Updated on 

 Mon Jun 29 22:22:17 PDT 2026 

 Focus 

 Home 

 Cloud NGFW for Azure Administration 

 Monitor Cloud NGFW for Azure Resources 

 View Activity Logs Natively in Azure 

 View Audit Logs on Resource Groups 

 Download PDF 

 Cloud NGFW for Azure 

 View Audit Logs on Resource Groups 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Cloud NGFW for Azure Docs 

 Getting Started 

 Deployment 

 Administration 

 Reference 

 Release Notes 

 New Features 

 Previous 

 View Audit Logs in a Firewall Resource 

 Next 

 View Cloud NGFW Metrics in Azure Monitor 

 View Audit Logs on Resource Groups 

 Learn how to view audit logs on resource groups in your Cloud NGFW for Azure
 resource. 

 Where Can I Use This? What Do I Need? 

 Cloud NGFW for Azure 

 Cloud NGFW subscription 

 Palo Alto Networks Customer Support Portal account 

 Azure Marketplace subscription 

 A log is an automatically generated, time-stamped file that provides an audit trail
 for system events on the firewall or network traffic events that the firewall
 monitors. Log entries contain artifacts, which are properties, activities, or
 behaviors associated with the logged event, such as the application type or the IP
 address of an attacker. Each log type records information for a separate event type.
 For example, the firewall generates a Threat log to record traffic that matches a
 spyware, vulnerability, or malware signature or a DoS attack that matches the
 thresholds configured for a port scan or host sweep activity on the firewall. 

 The Cloud NGFW for Azure can send traffic, threat, and decryption logs to an Azure
 Log Analytics Workspace that you will create in the Azure portal. The Log Analytics
 Workspace is associated with a workspace ID, primary Key, and a secondary key, which
 is retrieved through the logging API by the control plane. 

 To view audit logs on resource groups: 

 Navigate to Resource groups from the homepage. 

 Click the Resource group for which you wish to collect
 the activity log. 

 Click Activity Log on the left pane and select the
 desired Timespan for which you wish to view the logs and
 click Apply . The list of logs for the selected timespan
 appears. 

 Click the desired log to view the Summary and
 JSON of the log. 

 Previous 

 View Audit Logs in a Firewall Resource 

 Next 

 View Cloud NGFW Metrics in Azure Monitor 

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

 Public Cloud 

 Administration 

 Cloud NGFW for Azure 

 Microsoft Azure 

 Cloud 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

---
url: https://docs.paloaltonetworks.com/strata-logging-service/administration/monitoring/troubleshooting-disconnected-firewalls
fetched_at: 2026-08-13T17:39:52Z
source: palo-alto-main
---

# Troubleshooting Firewall Connectivity Clear

Troubleshooting Firewall Connectivity 

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

 Troubleshooting Firewall Connectivity 

 Updated on 

 Jul 9, 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Strata Logging Service Docs 

 Activation & Onboarding 

 Administration 

 Release Notes 

 Log Reference 

 New Features 

 Updated on 

 Jul 9, 2026 

 Focus 

 Home 

 Strata Logging Service 

 Strata Logging Service Administration 

 Monitor Strata Logging Service 

 Troubleshooting Firewall Connectivity 

 Download PDF 

 Strata Logging Service 

 Troubleshooting Firewall Connectivity 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Strata Logging Service Docs 

 Activation & Onboarding 

 Administration 

 Release Notes 

 Log Reference 

 New Features 

 Previous 

 Strata Logging Service Log Types 

 Next 

 View Logs in Strata Logging Service 

 Troubleshooting Firewall Connectivity 

 If you’re having trouble connecting your firewall to Strata Logging Service ,
 here are some steps you can try to solve the issue. 

 Where Can I Use This? What Do I Need? 

 NGFW , including those funded by Software NGFW
 Credits 

 Prisma Access 

 One of these: 
 Strata Cloud Manager Pro 

 Strata Logging Service 

 Find out what to do if one of the firewalls in your Inventory 
 shows one of these issues: 

 License Expired 

 Needs Certificate 

 Certificate Expired 

 Connected but Logging Rate is Zero 

 Failed to Fetch FQDN 

 License Expired 

 If a
 firewall is disconnected, check its license status by logging into the firewall CLI
 and entering the following: 
 request license info 

 Sample output: 

 Feature: Logging Service
 Description: Device Logging Service
 Expires: April 06, 2038
 Expired?: no 

 If you see Expired?:
 yes , follow the steps below to refresh the license on the
 firewall or on the Panorama managing the firewall. 

 Firewall Panorama 

 For Panorama-managed firewalls, refresh the license from
 Panorama . 
 For firewalls not managed by Panorama,
 manually refresh the license from Device > License in the firewall
 UI . If the license on the Panorama managing the firewall
 is expired, refresh the license on
 Panorama . 

 If the above does not resolve the issue, enter the following command in the
 firewall CLI: 

 If Strata Logging Service Forwarding is enabled,
 enter: request logging-service-forwarding status 

 If Duplicate Logging (Cloud and On-Premise) is enabled,
 enter: debug log-receiver log-forwarding-connections
 status 

 Sample output: 

 Logging Service Licensed: Yes
 Logging Service forwarding enabled: No
 Duplicate logging enabled: No
 Enhanced application logging enabled: No

 Logging Service License Status:
 Status:

 Fetch:

 Install:
 Status: Success
 Msg: Successfully install fetched license
 Last Fetched: 2021/12/22 11:56:34

 Upgrade:

 Logging Service Certificate information:
 Info: Failed
 Status: failure
 Last fetched: Mon Dec 27 15:20:44 2021

 Logging Service Customer file information:
 Info: Failed to validate server certificate for endpoint api.paloaltonetworks.com
 Status: failure
 Last Fetched: 2021/12/27 15:24:24

 If your output contains similar failures, this means that you upgraded a
 device from PAN-OS 10.0 or earlier to PAN-OS 10.1 or later, or you installed a device certificate on your
 10.1 or later device. In that case, you should restart the
 management-server or restart the device. You can use the
 following CLI command to restart the management-server :

 debug software
 restart process management-server 

 Needs
Certificate 

 If the Certificate Status of a firewall indicates that the firewall Needs Certificate, this means
 that the firewall must be onboarded to Strata Logging Service . 

 Certificate
Expired 

 To check the Certificate Status of a firewall, log into the firewall CLI and enter the
 following: 

 request logging-service-forwarding status 

 For Firewall running on 10.1 or earlier, enter: request
 logging-service-forwarding certificate info 

 For firewall running on 10.1 or later, enter: show device-certificate
 info show device-certificate status 

 If the output states that the certificate
has expired, then follow the steps below for manually refreshing
the certificate on the firewall. 

 If the output contains Info: Error sending CSR signing request to
 Panorama , then follow the steps for refreshing the certificate on
 Panorama. 

 Firewall Panorama Unmanaged Firewall 

 In the firewall CLI, enter 

 request logging-service-forwarding certificate
 delete 

 request logging-service-forwarding certificate
 fetch 

 In the Panorama CLI, enter 

 request plugins cloud_services
 logging-service status 

 If the output contains Logging service
 certificate expired , then fetch a new
 certificate using the following command: 

 request plugins cloud_services
 panorama-certificate fetch otp <value> 

 where value is the one time password OTP needed
 to fetch the certificate from the customer support portal(CSP)
 server. 

 If the command failed, check the plug-in log file with
 the following command: 

 less mp-log
 plugin_cloud_services.log 

 Otherwise, return to the CLI of the firewall you are
 troubleshooting and enter 

 request logging-service-forwarding
 certificate fetch 

 In the firewall CLI, enter 

 request logging-service-forwarding certificate
 fetch-noproxy pre-shared-key <value> 

 Here value is the pre-shared key from the
 customer support portal (CSP). 

 After you’ve completed the above, check the certificate status in your Strata Logging Service 
 Inventory . 

 Connected
but Logging Rate is Zero 

 If the Connection Status of your firewall is Connected but the Ingestion Rate is zero, then
 verify that your log forwarding profiles are correctly
 configured . 

 Failed to Fetch FQDN 

 The firewall may be unable to connect because it is not successfully
 retrieving the ingest/query FQDN for Strata Logging Service . To find out
 if this is the case, log in to the firewall CLI and enter 
 request
 logging-service-forwarding status 

 or 
 request logging-service-forwarding customerinfo show 
 Sample output: 

 Logging Service Customer file information:
 Customer ID: xxxxxxx
 EAL Ingest FQDN: xxxxx.fei.lcaas-qa.us.paloaltonetworks.com.
 Ingest FQDN: xxxxxx.in2.lcaas-qa.us.paloaltonetworks.com
 Info: Failed to fetch ingest/query FQDN for customer (curl failed)
 Query FQDN: xxxxx.api2.lcaas-qa.us.paloaltonetworks.com:444
 Status: failure
 Last Fetched: 2020/07/22 19:01:06 

 If you see
 Info: Failed to fetch ingest/query FQDN for customer (curl
 failed) as in the above, then enter request
 logging-service-forwarding customerinfo fetch 

 to manually refresh the certificate. Then, check the Connection Status
 in your Strata Logging Service 
 Inventory to see if the firewall is now connected.

 Previous 

 Strata Logging Service Log Types 

 Next 

 View Logs in Strata Logging Service 

 On This Page 

 Activation & Onboarding 

 Strata Cloud Manager 

 Activate a License or Product 

 Identity and Access Management 

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

 Endpoints 

 GlobalProtect 

 Visibility & Monitoring 

 Dashboards 

 Incidents and Alerts 

 Reports 

 Autonomous DEM 

 Best Practices 

 Best Practices Library 

 Experts Corner 

 Solutions Docs from Product Experts 

 Administration 

 Strata Logging Service 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

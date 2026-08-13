---
url: https://docs.paloaltonetworks.com/ngfw/administration/app-id/cloud-based-app-id-service/troubleshoot-cloud-based-app-id-service
fetched_at: 2026-08-13T16:39:23Z
source: palo-alto-main
---

# Troubleshoot App-ID Cloud Engine Clear

Troubleshoot App-ID Cloud Engine 

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

 Troubleshoot App-ID Cloud Engine 

 Updated on 

 Mon Aug 03 13:41:44 PDT 2026 

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

 Mon Aug 03 13:41:44 PDT 2026 

 Focus 

 Home 

 Next-Generation Firewall 

 App-ID 

 App-ID Cloud Engine 

 Troubleshoot App-ID Cloud Engine 

 Download PDF 

 Next-Generation Firewall 

 Troubleshoot App-ID Cloud Engine 

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

 Commit Failure Due to Cloud Content Rollback 

 Next 

 SaaS App-ID Policy Recommendation 

 Troubleshoot App-ID Cloud Engine 

 Troubleshoot issues with using cloud applications in policy. 

 Where Can I Use This? What Do I Need? 

 Prisma Access 

 Next-Generation Firewall 

 SaaS Security Inline license (for NGFW) 

 Prisma Access license (ACE is a core feature) 

 This topic provides general troubleshooting
information for the App-ID Cloud Engine (ACE). 

 To check if an appliance has a valid SaaS Security Inline
license, run the operational CLI command show cloud-appid connection-to-cloud .
If there is an issue, the command returns the message: 

 ACE Error: License check failed. Check if SaaS license is installed and activeCloud connection: failed 

 In
addition, the output shows the time of the last successful connection,
for example: Last successful gRPC connection: 2021-05-20 16:00:00 -0800 PDT 

 If
the license is installed and the connection to ACE is good, then
the command returns the URL for the ACE cloud server connection
and the status Cloud connection: connected ,
along with connection statistics and the status of the device certificate,
including the certificate validity dates. 

 Panorama commit all/push to managed firewalls fails. Check
if any of the following conditions exist and repair them: 

 Do
managed firewalls have a valid SaaS Security Inline license? If
not, then they do not have the ACE catalog and the commit all/push operation
fails. Depending on whether you want to managed firewalls to handle
ACE App-IDs, either remove the ACE objects from the pushed configuration
and try again or install valid SaaS Security Inline licenses on
the managed firewalls, wait for the catalog to download. 

 There
are fewer than four thousand content-provided App-IDs. After you
download the ACE catalog, you see many thousands more applications
on the firewall and can confirm by checking Objects Applications or by using the
operational CLI command show cloud-appid cloud-app-data application all to
see the new App-IDs. 

 Has the connection between a managed firewall and ACE has
gone down? Check the connection to the ACE cloud and restore the
connection if necessary. 

 The operational CLI command show cloud-appid connection-to-cloud provides
the cloud connection status and the ACE cloud server URL. 

 The ACE catalog on Panorama and the ACE catalog on managed
firewalls is out-of-sync, which results in pushed configurations
that include ACE apps that are not in the firewall’s catalog. If
the connection between the firewall and ACE is up, the outdated
catalog will update in the next few minutes automatically and resolve
the issue. (Wait five minutes and try again.) 

 You can
also run the operational CLI command debug cloud-appid cloud-manual-pull check-cloud-app-data to
update the catalog manually. 

 Are the firewalls all running PAN-OS 11.1 or later? (Pushing configurations that reference ACE
 applications and objects to firewalls running earlier versions than
 PAN-OS 11.1 is not allowed.) 

 In an HA pair (active/active or active/passive) that has
an ACE configuration, if you run the operational command show session all or show session id <id> ,
the output for ACE applications may show the global App-ID number
instead of the application name. The firewall only shows the application
name if its data plane has the cloud application data. If not, then
the firewall shows the global App-ID number for the application
instead. 

 To reset the connection to ACE (the gRPC connection), run
the operational CLI command debug cloud-appid reset connection-to-cloud . 

 View the ACE applications downloaded to the appliance with
the operational CLI command show cloud-appid cloud-app-data application .
You can view all downloaded apps or individual apps by App-ID or
application name. 

 View pending requests for ACE App-IDs with the operational
CLI command show cloud-appid signature-dp pending-request .
The output includes how many times the firewall sent the request
to ACE ( tries ). After eleven tries,
the send operation times out. 

 The operational CLI command show cloud-appid has
more useful options: 

 admin@PAN-ACE-VM-1> show cloud-appid ? 
> app-objects-in-policy Show application-filter/application-groups referred in policy
> app-to-filtergroup-mapping Show application to matched filter and groups
> application Show Application info for UI
> application-filter Show cloud apps in application-filters
> application-group Show cloud apps in application-groups
> cloud-app-data Show cloud application, container and metadata
> connection-to-cloud Show gRPC connection status to cloud application server
> ha-info Show statistics of cloud application high availability
> overlap-appid Show duplicated applications in predefined content
> signature-dp Show cloud signatures and applications used on DP
> task Show task on management-plane
> transaction Show cloud application transaction
> version Show Cloud-AppID version 

 To view the global counters for ACE, run the operational
CLI command show counter global filter value all category cad ( cad stands
for “cloud app-identification). 

 To view statistics for bytes and packets received and sent
to/from shared memory and to/from the security client for services
such as ACE, DLP, and IoT, run the operational command show ctd-agent statistics . 

 If you notice a discrepancy between the number of applications
that match an Application Filter when you look in the user interface
versus when you look in the CLI, it’s because of the way the firewall
counts matching applications in the user interfaces versus in the
CLI: 

 When you look at an Application Filter in Objects Application Filters ,
the firewall displays all of the matching applications in the ACE
catalog, regardless of whether the firewall has actually seen those
applications and downloaded their App-IDs, and the number count
includes all of those applications. 

 When you look at an Application Filter in the CLI with the show cloud-appid application-filter operational command,
the firewall only displays the number of matching applications for
which the firewall has downloaded ACE App-IDs. 

 For
this reason, the user interface may show more matching applications
than the CLI for the same Application Filter. 

 The same
thing applies to Application Groups when you look at them in the
user interface versus the CLI. 

 ACE App-IDs are supported for Security policy only. ACE App-IDs
are not supported for any other policy type. 

 However, when
you configure QoS or SD-WAN policy, ACE App-IDs are visible (able
to be selected) and may be present in Application Groups or Application
Filters applied to the rule, but adding them to QoS or SD-WAN policy
has no effect on the application traffic. (The QoS and SD-WAN policies don’t
control the application traffic.) 

 Previous 

 Commit Failure Due to Cloud Content Rollback 

 Next 

 SaaS App-ID Policy Recommendation 

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

 Network Security 

 PAN-OS 

 Next-Generation Firewall 

 Administration 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

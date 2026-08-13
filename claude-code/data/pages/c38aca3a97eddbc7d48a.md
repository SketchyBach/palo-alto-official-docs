---
url: https://docs.paloaltonetworks.com/strata-logging-service/log-reference/common-logs/common-audit-log/common-audit-leef-fields
fetched_at: 2026-08-13T17:40:03Z
source: palo-alto-main
---

# Audit LEEF Fields Clear

Audit LEEF Fields 

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

 Audit LEEF Fields 

 Updated on 

 Fri Jul 03 02:04:39 PDT 2026 

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

 Fri Jul 03 02:04:39 PDT 2026 

 Focus 

 Home 

 Strata Logging Service 

 Strata Logging Service Log Reference 

 Common Logs 

 Audit 

 Audit LEEF Fields 

 Download PDF 

 Strata Logging Service 

 Audit LEEF Fields 

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

 Audit HTTPS Fields 

 Next 

 Configuration 

 Audit LEEF Fields 

 The following table identifies the Audit field names that the Log Forwarding app
 uses when you forward logs using the LEEF log format.

When you 

create a syslog forwarding profile 
 ,
you can optionally create a profile token that the Log
Forwarding app uses when it sends logs to the syslog server. If you configure a profile token,
it appears in the log line immediately after the log type information (for example,
 TRAFFIC , THREAT ,
 HIPMATCH , and so forth). The token will appear on 
a parameter called profileToken .

 LEEF Name

 Query Name

 Field Type

 ActorDisplayName

 actor_display_name 

 Custom

 ActorID

 actor_id 

 Custom

 ConnectionErrorID

 connection_error.​id 

 Custom

 ConnectionErrorValue

 connection_error.​value 

 Custom

 CortexDataLakeTenantID

 customer_id 

 Custom

 EventCategory

 event_category 

 Custom

 EventClientIP

 event_client_ip.​value 

 Custom

 EventDescription

 event_description 

 Custom

 EventDestination

 event_dest.​value 

 Custom

 EventDestinationAction

 event_dest_action 

 Custom

 EventDestinationURL

 event_dest_url 

 Custom

 EventDestinationUserUserID

 event_dest_user.​user_id 

 Custom

 EventDestinationUserUUID

 event_dest_user.​uuid 

 Custom

 DestinationVendor

 event_dest_vendor 

 Custom

 EventDetails

 event_detail 

 Custom

 EventID

 event_id 

 Header

 EventName

 event_name 

 Custom

 EventResult

 event_result 

 Custom

 EventSource

 event_source.​value 

 Custom

 EventSourceURL

 event_source_url 

 Custom

 EventSourceUserDomain

 event_source_user.​domain 

 Custom

 EventSourceUser

 event_source_user.​user 

 Custom

 EventSourceUserUserID

 event_source_user.​user_id 

 Custom

 EventSourceUserUUID

 event_source_user.​uuid 

 Custom

 EventSourceUserEmail

 event_source_user_email 

 Custom

 EventSourceUserFirstName

 event_source_user_first_name 

 Custom

 EventSourceUserLastName

 event_source_user_last_name 

 Custom

 EventSourceUserUUIDV4

 event_source_user_uuid_v4 

 Custom

 EventSubCategory

 event_sub_category 

 Custom

 EventTime

 event_time 

 Custom

 LogSource

 log_source 

 Custom

 LogSourceGroupID

 log_source_group_id 

 Custom

 DeviceSN

 log_source_id 

 Custom

 DeviceName

 log_source_name 

 Custom

 LogSourceTimeZoneOffset

 log_source_tz_offset 

 Custom

 TimeReceived

 log_time 

 Custom

 cat

 log_type.​value 

 Predefined

 PlatformType

 platform_type 

 Custom

 Subtype

 sub_type.​value 

 Custom

 TSGID

 tsg_id 

 Custom

 Vendor

 vendor_name 

 Header

 VendorSeverity

 vendor_severity.​value 

 Custom

 Previous 

 Audit HTTPS Fields 

 Next 

 Configuration 

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

 Security Operations 

 Log Reference 

 Strata Logging Service 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

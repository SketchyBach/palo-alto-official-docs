---
url: https://docs.paloaltonetworks.com/prisma-access-browser/administration/investigate-prisma-access-browser-events/prisma-browser-event-types/prisma-browser-audit-events
fetched_at: 2026-08-13T17:23:09Z
source: palo-alto-main
---

# Audit Events Clear

Audit Events 

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

 Audit Events 

 Updated on 

 Tue Jul 28 09:38:39 PDT 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma Browser Docs 

 Activation & Onboarding 

 Getting Started 

 Deployment 

 Administration 

 Integrations 

 User Guide 

 Updated on 

 Tue Jul 28 09:38:39 PDT 2026 

 Focus 

 Home 

 Prisma Browser 

 Prisma Access Browser Administration 

 Explore Prisma Browser Events 

 Prisma Browser Event Types 

 Audit Events 

 Download PDF 

 Prisma Browser 

 Audit Events 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma Browser Docs 

 Activation & Onboarding 

 Getting Started 

 Deployment 

 Administration 

 Integrations 

 User Guide 

 Previous 

 Access Events 

 Next 

 Data Protection Events (DLP) 

 Audit Events 

 Audit events record administrative actions performed in the Prisma Browser management console, providing a complete audit trail of who changed what, when, and from where. 

 Audit Event Structure 

 Every audit event includes the following core fields: 

 Field Description 

 Category The area of the console where the action occurred 

 Type The specific action performed 

 Description A human-readable description of the change 

 Metadata Additional structured data about the change (varies by type) 

 User The admin who performed the action (email, ID) 

 Client IP The IP address from which the action was performed 

 Timestamp When the action occurred 

 Tenant The tenant where the action was performed 

 Policy Rules 

 Actions related to policy rule management. 

 Type Description 

 Rule created A new policy rule was created 

 Rule updated An existing rule was modified 

 Rule priority changed The priority order of rules was changed 

 Rule deleted A rule was deleted 

 Rule enabled A disabled rule was enabled 

 Rule disabled A rule was disabled 

 Rules bulk deleted Multiple rules were deleted at once 

 Rules bulk mode updated Multiple rules had their mode changed at once 

 Policy Profiles 

 Actions related to policy profile configuration. 

 Type Description 

 Profile created A new policy profile was created 

 Profile updated An existing profile was modified 

 Profile deleted A profile was deleted 

 Policy Sections 

 Actions related to policy section organization. 

 Type Description 

 Section created A new policy section was created 

 Section updated A section was renamed or modified 

 Section deleted A section was deleted 

 Configuration Management 

 Actions related to policy versioning and publishing. 

 Type Description 

 Version published A draft configuration was published (made active) 

 Settings 

 General settings changes. 

 Type Description 

 Setting updated A system setting was changed 

 Authentication profile updated The authentication/SSO profile was modified 

 User Management 

 Actions related to managing console users and end users. 

 Type Description 

 User created A new user was added 

 User role updated A user's role was changed 

 User deleted A user was removed 

 User suspended A user was suspended from the system 

 User activated A suspended user was reactivated 

 User force reauthenticated A user was forced to reauthenticate 

 Device Management 

 Actions related to managing endpoint devices. 

 Type Description 

 Device group created A new device group was created 

 Device group updated A device group's definition was changed 

 Device group deleted A device group was removed 

 Device archived A device was moved to archive 

 Device restored An archived device was restored 

 Device suspended A device was suspended 

 Device resumed A suspended device was reactivated 

 Device deleted A device record was removed 

 Device force reauthenticated A device was forced to reauthenticate 

 Applications 

 Actions related to application management. 

 Type Description 

 Custom application created A custom application definition was added 

 Custom application updated A custom application was modified 

 Custom application deleted A custom application was removed 

 Private application created A private application was added 

 Private application updated A private application was modified 

 Private application deleted A private application was removed 

 Application group created An application group was created 

 Application group updated An application group was modified 

 Application group deleted An application group was removed 

 Local desktop application created A BPY-monitored desktop application was added 

 Local desktop application updated A BPY-monitored desktop application was modified 

 Local desktop application deleted A BPY-monitored desktop application was removed 

 Local desktop catalog application updated A desktop app catalog entry was updated 

 AppID catalog application updated An AppID catalog entry was updated 

 Application Tags 

 Actions related to application classification tags. 

 Type Description 

 Application tag created A new application tag was created 

 Application tag updated An application tag was modified 

 Application tag deleted An application tag was removed 

 Event Forwarding 

 Actions related to SIEM and log forwarding integrations. 

 Type Description 

 Integration created A new event forwarding integration was configured 

 Integration updated An event forwarding integration was modified 

 Integration deleted An event forwarding integration was removed 

 API Key Management 

 Actions related to API key lifecycle. 

 Type Description 

 API key created A new API key was generated 

 API key updated An API key was modified 

 API key deleted An API key was revoked 

 Automation Token Management 

 Actions related to automation tokens. 

 Type Description 

 Automation token created A new automation token was generated 

 Automation token deleted An automation token was revoked 

 Permission Requests 

 Actions related to user bypass/permission requests. 

 Type Description 

 Permission request approved An admin approved a user's request to bypass a block 

 Permission request declined An admin declined a user's request 

 Permission request revoked A previously approved permission was revoked 

 Data Management 

 Actions related to data export and visibility features. 

 Type Description 

 Events exported Event data was exported from the console 

 Live session started A live session to a user's browser was initiated 

 Live session declined A live session request was declined 

 Live session request timeout A live session request timed out 

 Live session terminated A live session was ended 

 Live session remote controls Remote control was used during a live session 

 Live session recorded A live session was recorded 

 Enhanced Visibility 

 Actions related to enhanced visibility features. 

 Type Description 

 MSP default rules replaced Managed service provider default rules were replaced 

 Directory 

 Actions related to user directory management. 

 Type Description 

 Directory created A new user directory was connected 

 Directory updated A user directory configuration was modified 

 Directory deleted A user directory was disconnected 

 User group created A new user group was created 

 User group updated A user group was modified 

 User group deleted A user group was removed 

 Viewing Audit Events 

 Audit events are available in: 

 The Prisma Browser console under Analytics > Audit Log 

 Strata Cloud Manager Log Viewer 

 External systems via event forwarding (when audit log forwarding is enabled) 

 Audit events can be forwarded to the same destinations as browser events (Syslog, AWS S3, Splunk, Microsoft Sentinel, etc.) by enabling the Audit stream in event forwarding configuration. 

 Examples 

 Rule Created 

 Field Value 

 Category Policy Rules 

 Type Rule created 

 Description Created access rule "Block uploads to GenAI" 

 Admin user admin@acme.com 

 Client IP 203.0.113.42 

 Time 2026-07-06 09:00:00 UTC 

 Rule Updated — Mode Change 

 Field Value 

 Category Policy Rules 

 Type Rule updated 

 Description Updated rule "Monitor clipboard paste" — changed mode from Monitor to Enforce 

 Admin user admin@acme.com 

 Client IP 203.0.113.42 

 Time 2026-07-06 09:15:30 UTC 

 Version Published 

 Field Value 

 Category Configuration Management 

 Type Version published 

 Description Published configuration version 14 

 Admin user admin@acme.com 

 Client IP 203.0.113.42 

 Time 2026-07-06 09:20:00 UTC 

 User Suspended 

 Field Value 

 Category User Management 

 Type User suspended 

 Description Suspended user john.smith@acme.com — Reason: Security investigation 

 Admin user security.admin@acme.com 

 Client IP 198.51.100.15 

 Time 2026-07-06 10:30:00 UTC 

 Device Force Reauthenticated 

 Field Value 

 Category Device Management 

 Type Device force reauthenticated 

 Description Forced reauthentication on device ACME-LAPTOP-042 

 Admin user admin@acme.com 

 Client IP 203.0.113.42 

 Time 2026-07-06 11:00:00 UTC 

 Event Forwarding Integration Created 

 Field Value 

 Category Event Forwarding 

 Type Integration created 

 Description Created Splunk HEC event forwarding integration "Production SIEM" 

 Admin user siem.admin@acme.com 

 Client IP 10.0.1.50 

 Time 2026-07-06 14:00:00 UTC 

 API Key Created 

 Field Value 

 Category API Key Management 

 Type API key created 

 Description Created API key "Automation - Device Provisioning" 

 Admin user devops.admin@acme.com 

 Client IP 172.16.0.100 

 Time 2026-07-06 15:30:00 UTC 

 Permission Request Approved 

 Field Value 

 Category Permission Requests 

 Type Permission request approved 

 Description Approved bypass request from jane.doe@acme.com for rule "Block file uploads to unsanctioned apps" 

 Admin user team.lead@acme.com 

 Client IP 203.0.113.42 

 Time 2026-07-06 10:05:00 UTC 

 Live Session Started 

 Field Value 

 Category Data Management 

 Type Live session started 

 Description Started live session to user sarah.kim@acme.com on device ACME-MACBOOK-089 

 Admin user security.admin@acme.com 

 Client IP 198.51.100.15 

 Time 2026-07-06 13:45:00 UTC 

 Previous 

 Access Events 

 Next 

 Data Protection Events (DLP) 

 On This Page 

 Activation & Onboarding 

 Strata Cloud Manager 

 Cloud Identity Engine 

 Strata Logging Service 

 Device Associations 

 Hub 

 Identity and Access Management 

 Tenant Management 

 SASE 

 Prisma Access 

 Strata Multitenant Cloud Manager 

 AI-Powered ADEM 

 Prisma Access Monitoring and Visibility 

 Prisma SD-WAN 

 ION Devices 

 Next-Generation CASB 

 Prisma Browser 

 Administration 

 Prisma Access 

 Strata Cloud Manager 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

---
url: https://docs.paloaltonetworks.com/prisma-access/incidents-and-alerts/ai-powered-adem-incidents/incident-inc-globalprotect-gw-user-auth-timeout-failures-count-exceeded-above-baseline-all-pa-locations
fetched_at: 2026-08-13T17:25:53Z
source: palo-alto-main
---

# INC_GLOBALPROTECT_GW_USER_AUTH_ TIMEOUT_FAILURES_COUNT_EXCEEDED_
        ABOVE_BASELINE_ALL_PA_LOCATIONS Clear

INC_GLOBALPROTECT_GW_USER_AUTH_ TIMEOUT_FAILURES_COUNT_EXCEEDED_
 ABOVE_BASELINE_ALL_PA_LOCATIONS 

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

 INC_GLOBALPROTECT_GW_USER_AUTH_ TIMEOUT_FAILURES_COUNT_EXCEEDED_
 ABOVE_BASELINE_ALL_PA_LOCATIONS 

 Updated on 

 Fri May 22 03:04:12 PDT 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma Access Docs 

 Release Notes 

 Select a Document 

 6.2 Preferred and Innovation 

 6.1 Preferred and Innovation 

 6.0 Preferred and Innovation 

 5.2 Preferred and Innovation 

 5.1 Preferred and Innovation 

 5.0 Preferred and Innovation 

 4.2 Preferred 

 4.1 Preferred 

 4.0 Preferred 

 3.2 Preferred and Innovation 

 Activation & Onboarding 

 Administration 

 Select a Document 

 4.0 & Later 

 Prisma Access China 

 Integrations 

 Incidents & Alerts 

 New Features 

 Updated on 

 Fri May 22 03:04:12 PDT 2026 

 Focus 

 Home 

 Prisma Access 

 Prisma Access Incidents and Alerts Reference Guide 

 AI-Powered ADEM Incidents 

 INC_GLOBALPROTECT_GW_USER_AUTH_ TIMEOUT_FAILURES_COUNT_EXCEEDED_
 ABOVE_BASELINE_ALL_PA_LOCATIONS 

 Download PDF 

 Prisma Access 

 INC_GLOBALPROTECT_GW_USER_AUTH_ TIMEOUT_FAILURES_COUNT_EXCEEDED_
 ABOVE_BASELINE_ALL_PA_LOCATIONS 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma Access Docs 

 Release Notes 

 Select a Document 

 6.2 Preferred and Innovation 

 6.1 Preferred and Innovation 

 6.0 Preferred and Innovation 

 5.2 Preferred and Innovation 

 5.1 Preferred and Innovation 

 5.0 Preferred and Innovation 

 4.2 Preferred 

 4.1 Preferred 

 4.0 Preferred 

 3.2 Preferred and Innovation 

 Activation & Onboarding 

 Administration 

 Select a Document 

 4.0 & Later 

 Prisma Access China 

 Integrations 

 Incidents & Alerts 

 New Features 

 Previous 

 INC_CIE_DIRECTORY_DISCONNECT 

 Next 

 INC_GLOBALPROTECT_GW_USER_AUTH_ TIMEOUT_FAILURES_COUNT_EXCEEDED_ ABOVE_BASELINE_PER_PA_LOCATION 

 INC_GLOBALPROTECT_GW_USER_AUTH_ TIMEOUT_FAILURES_COUNT_EXCEEDED_
 ABOVE_BASELINE_ALL_PA_LOCATIONS 

 Learn about the
 INC_GLOBALPROTECT_GW_USER_AUTH_TIMEOUT_FAILURES_COUNT_EXCEEDED_ABOVE_BASELINE_
 ALL_PA_LOCATIONS incident. 

 Synopsis 

 Gateway authentication timeout failures are higher than twice the baseline for all
 Prisma Access locations. 

 Incident Code—INC_GLOBALPROTECT_GW_USER_AUTH_TIMEOUT_FAILURES_COUNT_EXCEEDED_ABOVE_
 BASELINE_ALL_PA_LOCATIONS 

 Severity—Critical 

 Required License 

 AI-Powered ADEM 

 Details 

 Description 

 Raise condition 

 The incident is raised at the tenant, when the average
 authentication timeouts are more than twice the baseline in 45
 minutes. 

 Clear condition 

 The incident is cleared at the tenant, when the average
 authentication timeouts are less than twice the baseline in 45
 minutes. 

 Correlated Alerts 

 AL_GLOBALPROTECT_GW_USER_AUTH_SUCCESS_COUNT_DROPPED_BELOW_BASELINE_
 ALL_PA_LOCATIONS 

 AL_GLOBALPROTECT_GW_USER_AUTH_SUCCESS_COUNT_DROPPED_BELOW_BASELINE_
 PER_PA_LOCATION 

 AL_GLOBALPROTECT_GW_USER_AUTH_TIMEOUT_FAILURES_COUNT_EXCEEDED_ABOVE_
 BASELINE_ALL_PA_LOCATIONS 

 AL_GLOBALPROTECT_GW_USER_AUTH_TIMEOUT_FAILURES_COUNT_EXCEEDED_
 ABOVE_BASELINE_PER_PA_LOCATION 

 AL_GLOBALPROTECT_USER_COUNT_DROPPED_BELOW_BASELINE_ACROSS_PER_PA_LOCATION 

 AL_GLOBALPROTECT_USER_COUNT_DROPPED_BELOW_BASELINE_ALL_PA_LOCATIONS 

 Remediation 

 Check your authentication service availability on those services. 

 For on-premise authentication services (such as LDAP, Radius, or Kerberos), you
 can review audit logs for incoming user requests or login errors. If there is a
 lapse in incoming requests, take packet captures on the relevant network
 path. 

 For public authentication services (such as SAML or cloud LDAP or Radius
 services), review audit logs provided by your authentication service. If there
 is a lapse in incoming requests, check with your authentication provider for any
 ongoing outages. 

 Previous 

 INC_CIE_DIRECTORY_DISCONNECT 

 Next 

 INC_GLOBALPROTECT_GW_USER_AUTH_ TIMEOUT_FAILURES_COUNT_EXCEEDED_ ABOVE_BASELINE_PER_PA_LOCATION 

 On This Page 

 Activation and Onboarding 

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

 Panorama 

 Service Provider 

 VM-Series 

 Plugins 

 SASE 

 Prisma Access 

 Prisma SASE Multitenant Platform 

 AI-Powered ADEM 

 Prisma Access Monitoring & Visibility 

 Prisma SD-WAN 

 ION Devices 

 Next-Generation CASB 

 Cloud-Delivered Security Services 

 Advanced WildFire 

 Advanced URL Filtering 

 Advanced Threat Prevention 

 Advanced DNS Security 

 AI Access Security 

 Device Security 

 Enterprise DLP 

 SaaS Security 

 Network Security 

 Shared Policy for NGFWs and Prisma Access 

 IPSec VPN 

 Security Policy 

 Quantum Security 

 Endpoints 

 GlobalProtect 

 Remote Browser Isolation 

 Prisma Access Agent 

 Visibility & Monitoring 

 Dashboards 

 Incidents and Alerts 

 Reports 

 Autonomous DEM 

 FedRAMP 

 Prisma SASE for FedRAMP 

 Autonomous DEM for FedRAMP 

 Hardware Reference 

 ION 1000 

 ION 1200 

 ION 1200-S 

 ION 2000 

 ION 3000 

 ION 3200 

 ION 5200 

 ION 7000 

 ION 9000 

 ION 9200 

 Hardware Quick Start Guides 

 ION 1200 

 ION 1200 4G 

 ION 1200 5G 

 ION 1200-S 

 ION 1200-S 4G 

 ION 1200-S 5G 

 ION 3200 

 ION 5200 

 ION 9200 

 Virtual ION Deployment 

 Virtual ION on AWS 

 Virtual ION on Azure 

 Virtual ION on GCP 

 Virtual ION on KVM for NFV 

 Virtual ION on OCI 

 Virtual ION on VMware 

 3rd Party Integrations 

 AWS Cloud-WAN Integration (GRE Connect) 

 AWS Cloud-WAN Integration (Tunnel-less Connect) 

 Checkpoint Integration 

 LiveAction Integration 

 Netskope Integration 

 Symantec Web Security Services Integration 

 Best Practices 

 Best Practices Library 

 Experts Corner 

 Solutions Docs from Product Experts 

 SASE 

 Incidents & Alerts 

 Prisma SASE 

 Prisma Access 

 Strata Cloud Manager 

 4.0 & Later 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

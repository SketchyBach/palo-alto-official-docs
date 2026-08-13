---
url: https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-admin/firewall-administration/manage-firewall-administrators/configure-administrative-accounts-and-authentication/configure-api-key-lifetime
fetched_at: 2026-08-13T17:04:30Z
source: palo-alto-main
---

# Configure API Key Lifetime Clear

Configure API Key Lifetime 

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

 Configure API Key Lifetime 

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

 Firewall Administration 

 Manage Firewall Administrators 

 Configure Administrative Accounts and Authentication 

 Configure API Key Lifetime 

 Download PDF 

 Next-Generation Firewall 

 Configure API Key Lifetime 

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

 Configure SSH Key-Based Administrator Authentication to the CLI 

 Next 

 Enable SCP Uploads for an Administrator 

 Configure API Key Lifetime 

 Protect API access with API key lifetime and the ability
to revoke API keys, in case of a compromise. 

 Where Can I Use This? What Do I Need? 

 NGFW (Managed by PAN-OS or Panorama) 

 No prerequisites needed 

 The API keys on the firewall and Panorama
enable you to authenticate API calls to the XML API and REST API.
Because these keys grant access to the firewall and Panorama that
are critical elements of your security posture, as a best practice,
specify an API key lifetime to enforce regular key rotation. After
you specify the key lifetime, when you regenerate an API key, each
key is unique. 

 In addition to setting a key lifetime that
prompts you to regenerate new keys periodically, you can also revoke
all currently valid API keys in the event one or more keys are compromised.
Revoking keys is a way to expire all currently valid keys. 

 Select Device Setup Management . 

 Edit Authentication Settings to specify the API
Key Lifetime (min) . 

 Set
the API key lifetime to protect against compromise and to reduce
the effects of an accidental exposure. By default, the API key lifetime
is set to 0, which means that the keys will never expire. To ensure
that your keys are frequently rotated and each key is unique when
regenerated, you must specify a validity period that ranges between
1—525600 minutes. Refer to the audit and compliance policies for
your enterprise to determine how you should specify the lifetime
for which your API keys are valid. 

 Commit the changes. 

 (To revoke all API keys) Select Expire
all API Keys to reset currently valid API keys. 

 If you have just set a key lifetime and want to reset all
API keys to adhere to the new term, you can expire all existing
keys. 

 On confirmation,
the keys are revoked and you can view the timestamp for when the API
Keys Last Expired . 

 Previous 

 Configure SSH Key-Based Administrator Authentication to the CLI 

 Next 

 Enable SCP Uploads for an Administrator 

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

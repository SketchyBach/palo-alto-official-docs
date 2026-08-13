---
url: https://docs.paloaltonetworks.com/prisma-access/incidents-and-alerts/prisma-access-license-incidents/incident-ai-adem-inc-rn-site-down
fetched_at: 2026-08-13T17:26:32Z
source: palo-alto-main
---

# INC_RN_SITE_DOWN Clear

INC_RN_SITE_DOWN 

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

 INC_RN_SITE_DOWN 

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

 Prisma Access Incidents 

 INC_RN_SITE_DOWN 

 Download PDF 

 Prisma Access 

 INC_RN_SITE_DOWN 

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

 INC_RN_SITE_CAPACITY_PREDICTION 

 Next 

 INC_RN_SITE_LONG_DURATION_CAPACITY_EXCEEDED_THRESHOLD 

 INC_RN_SITE_DOWN 

 Learn about the INC_RN_SITE_DOWN incident. 

 Synopsis 

 All tunnels (primary, secondary, and ECMP) for the RN site are down. 

 Incident Code—INC_RN_SITE_DOWN 

 Severity—Critical 

 For details about incident severity, see Incidents Distribution Over
 Time in Incidents and Alerts Overview . 

 Required License 

 Prisma Access 

 Details 

 Impact 

 RN user count when the site was down. 

 Raise condition 

 All tunnels (primary, secondary, and ECMP) for the RN site are
 down. 

 Clear condition 

 One tunnel (primary, secondary, or ECMP) for the RN site is
 up. 

 Correlated Alerts 

 AL_RN_ECMP_BGP_DOWN 

 AL_RN_ECMP_BGP_FLAP 

 AL_RN_ECMP_TUNNEL_DOWN 

 AL_RN_ECMP_TUNNEL_FLAP 

 AL_RN_PRIMARY_WAN_BGP_DOWN 

 AL_RN_PRIMARY_WAN_BGP_FLAP 

 AL_RN_PRIMARY_WAN_TUNNEL_DOWN 

 AL_RN_PRIMARY_WAN_TUNNEL_FLAP 

 AL_RN_SECONDARY_WAN_BGP_DOWN 

 AL_RN_SECONDARY_WAN_BGP_FLAP 

 AL_RN_SECONDARY_WAN_TUNNEL_DOWN 

 AL_RN_SECONDARY_WAN_TUNNEL_FLAP 

 AL_RN_SITE_DOWN 

 Remediation 

 Confirm whether the RN location is down by contacting the network team or users on
 site. If a complete network outage has occurred, contact Palo Alto Networks Customer Support Portal and provide
 the following detailed information: 

 If you have multiple sites in the same SPN location, confirm whether all sites
 are affected or just this particular RN site is affected. 

 Log in to your Strata Cloud Manager Managed Prisma Access or Panorama UI and check the status of the RN
 site or tunnel. If the RN tunnel is down, proceed to step 3 to verify whether
 the connectivity to the RN service IP failed. If the RN tunnel is up, proceed to
 step 3 to confirm whether connectivity was established correctly. 

 Perform a ping from your machine to the RN's service IP to verify whether it
 fails. If the ping fails, go to step 4. If the ping succeeds, proceed to step
 5. 

 Perform traceroute to the service IP to see whether
 traceroute is failing within your network. If it's
 failing within your network, work with your network team to resolve the
 connectivity issue. If traceroute is failing outside of your
 network, contact your ISP. If you can't resolve the issue, contact Palo Alto Networks Customer Support Portal . 

 Contact someone at the RN location to confirm whether users are able to access
 resources through the RN. If you can access resources successfully, confirm
 whether the alert is cleared. 

 Previous 

 INC_RN_SITE_CAPACITY_PREDICTION 

 Next 

 INC_RN_SITE_LONG_DURATION_CAPACITY_EXCEEDED_THRESHOLD 

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

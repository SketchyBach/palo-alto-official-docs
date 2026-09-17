---
url: https://docs.paloaltonetworks.com/prisma-access/incidents-and-alerts/prisma-access-license-incidents/incident-ai-adem-inc-rn-site-down
fetched_at: 2026-09-16T07:47:09Z
source: strata-and-sase
---

# INC_RN_SITE_DOWN Clear

Updated on 

 Mon Jun 15 11:08:47 PDT 2026 

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

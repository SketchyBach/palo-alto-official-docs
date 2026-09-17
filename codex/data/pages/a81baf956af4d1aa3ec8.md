---
url: https://docs.paloaltonetworks.com/prisma-agent/administration/configure-the-agent/mdm-posture-checks-for-prisma-agent
fetched_at: 2026-09-16T08:21:20Z
source: palo-alto-main
---

# MDM Posture Checks for Prisma Agent Clear

Updated on 

 Aug 27, 2026 

 Focus 

 Home 

 Prisma Agent 

 Configure the Prisma Agent 

 MDM Posture Checks for Prisma Agent 

 Download PDF 

 Prisma Agent 

 MDM Posture Checks for Prisma Agent 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma Agent Docs 

 Administration 

 User Guide 

 Release Notes 

 New Features 

 Previous 

 Create and Manage HIP Profiles for the Prisma Agent 

 Next 

 Configure MDM Posture Checks for Prisma Agent 

 MDM Posture Checks for Prisma Agent 

 Learn how MDM posture checks enforce device compliance from your MDM to authorize or
 block Prisma Agent tunnel connections. 

 Where Can I Use This? What Do I Need? 

 Prisma Access (Managed by Strata Cloud Manager) 

 Prisma Access 
 license with the
 Mobile User subscription 

 Windows or macOS
 (Microsoft Intune) ( Prisma Agent 26.2 and
 later) 

 macOS (Jamf) ( Prisma Agent 26.2 and later) 

 Contact your Palo Alto Networks account representative to
 activate this feature 

 MDM posture checks let you use device compliance data from your mobile device management
 (MDM) solution as the authoritative source for Prisma Agent tunnel
 authorization. 

 How It Works 

 The Endpoint Manager integrates directly with your MDM solution to query device
 attributes at pre-defined polling intervals. Upon successful user authentication, the
 Prisma Agent performs device authorization checks against your MDM to
 determine whether to allow or block the tunnel to Prisma Access. Tunnel establishment
 to NGFW or Prisma Access gateways is only allowed if the endpoint meets the following
 criteria: 

 It is registered and actively managed by the MDM. 

 It is compliant with the MDM-defined posture assessment profiles. 

 It is being used by the employee to whom it is assigned to access the network. 

 If a device is not enrolled in the MDM or fails a compliance check at the time of
 polling, the Prisma Agent blocks tunnel establishment, tears down any
 active tunnels, clears its gateway configuration, and notifies the user of the
 non-compliant status. 

 The Endpoint Manager will continue to monitor device posture and enforce access
 dynamically based on device state changes, network changes, or at predefined
 frequencies. This gives your security team a single source of truth for device
 compliance rather than maintaining parallel policies across MDM and HIP. 

 Prisma Access automatically handles API throttling responses from the MDM vendor and
 retries failed requests, so temporary MDM API errors do not require manual
 intervention. 

 Supported MDM Vendors 

 Microsoft Intune with Windows or macOS
 devices 

 Jamf with macOS devices 

 Admin Configuration 

 MDM posture checks require two components in Strata Cloud Manager: an MDM integration
 that defines your MDM vendor type and API credentials, and an MDM compliance check
 setting in your agent configuration that activates enforcement. When the MDM compliance
 check setting is disabled, Prisma Access does not query the MDM tenant even if an
 integration is configured, which lets you set up and validate the integration before
 turning on enforcement. 

 Previous 

 Create and Manage HIP Profiles for the Prisma Agent 

 Next 

 Configure MDM Posture Checks for Prisma Agent

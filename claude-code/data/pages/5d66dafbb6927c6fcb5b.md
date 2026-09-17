---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsoar-8-saas/configure-cortex-xsoar/incident-configuration/set-up-incident-mirroring
fetched_at: 2026-09-16T08:52:44Z
source: cortex-platform
---

# Set up incident mirroring | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSOAR 8 

 Cortex XSOAR 8 SaaS Documentation 

 Configure Cortex XSOAR 

 Incident configuration 

 Cortex XSOAR 8 (SaaS) 

 Set up incident mirroring 

 Set up incident mirroring in Cortex XSOAR 8 SaaS. 

 When mirroring incidents, you can make changes in a third-party application, such as ServiceNow and Jira that will be reflected in Cortex XSOAR, or vice versa. You can also attach files from either of the systems, which will then be available in the other system. 

 Setting up your integration to mirror incidents from the third-party application in Cortex XSOAR includes the following: 

 Configure mirroring for triggering incidents originating from your third-party application or from another fetching integration. For example, see the ServiceNow v2 integration. 

 Configure incoming and outgoing mappers. For more information, see Classification and mapping . 

 Configure account roles for API calls. For example, see the ServiceNow v2 integration. 

 Run mirroring commands. For more information about mirroring commands, see the Mirroring Integration or your third-party integration, for example ServiceNow v2 . 

 Enable mirroring for manually modified incident fields (dirty fields) 

 When incident mirroring is active, Cortex XSOAR automatically tracks which incident fields you manually edited. These are known as dirty fields. To prevent your manual changes from being overwritten, the platform protects dirty fields from being updated by the remote system (such as ServiceNow or Jira) during subsequent mirror synchronizations. 

 However, if you want to update previously edited incident fields during mirroring synchronization, you can run the resetDirtyFields command in the War Room or in an automation script. This command removes incident fields from the tracking list (stored in the dbotDirtyFields property), allowing the next incoming mirror synchronization to update them with data from the remote system. Running the resetDirtyFields command is relevant in situations where: 

 You accidentally edited an incident field. 

 A playbook or automation resolved a conflict and needs to re-enable mirroring for specific fields. 

 You want to force a full resync of all incident fields from the remote system. 

 Note 

 You must have the Incident Advanced Edit permission to execute the resetDirtyFields command. 

 The following are examples of how to use the resetDirtyFields command. 

 Update specific dirty fields of the current incident in context. 

 For example, an analyst manually edited the severity and owner fields but now wants those two fields to resynchronize from the remote system while keeping other manually edited incident fields protected. 

 In the CLI: !resetDirtyFields dirtyFields="severity,owner" 

 In an automation script: demisto.executeCommand("resetDirtyFields", {"dirtyFields": "severity,owner"}) 

 Result: Only severity and owner are removed from the dirty fields list. Other manually edited fields remain protected. The command returns Done . 

 Update all incident fields of the current incident in context. 

 This enables a full synchronization of the incident and takes precedence over any specific fields listed in the dirtyFields parameter. 

 For example, an analyst wants to allow all incident fields to be updated from the remote mirrored system on the next synchronization cycle. 

 In the CLI: !resetDirtyFields dirtyFieldsAll=true 

 In an automation script: demisto.executeCommand("resetDirtyFields", {"dirtyFieldsAll": "true"}) 

 Result: All fields are removed from the dirty fields list. The command returns Done . On the next incoming mirror synchronization, all fields are updated with values from the remote system. 

 Update specific dirty fields of an incident that is currently not in context. 

 For example, a playbook or automation needs to synchronize mirroring for the status and closeNotes dirty fields on a specific incident (12345) that is different from the one currently in context. 

 In the CLI: !resetDirtyFields id="12345" dirtyFields="status,closeNotes" 

 In an automation script: 

 Result: The status and closeNotes fields are removed from the dirty fields list for incident 12345. Other manually edited fields on that incident remain protected. The command returns Done . 

 Troubleshoot incident mirroring 

 In case of delays in incident mirroring, follow these troubleshooting steps: 

 Use !getMirrorStatistics in the War Room to check the status o the mirroring cycle. 

 Close unnecessary mirrored incidents to narrow down the scope of mirroring. 

 Remove redundant or disabled integration instances as deactivation alone may not free up resources. 

 If delays do not improve, contact support to discuss changing the time frame for mirrored incidents. 

 Previous Create an incident mapper 

 Next Incident deduplication in Cortex XSOAR 

 Last updated 2 months ago 

 Was this helpful?

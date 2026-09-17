---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsoar-8-on-prem/8.10/investigate-and-respond-to-threats/incidents-and-indicators-investigation/investigate-an-incident/limit-access-to-investigations-using-access-control
fetched_at: 2026-09-16T08:55:15Z
source: cortex-platform
---

# Limit access to investigations using access control | 8.10 | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSOAR 8 

 Cortex XSOAR 8 On-prem Documentation 

 8.10 

 Investigate and Respond to Threats 

 Incidents and indicators investigation 

 Investigate an incident 

 Cortex XSOAR 8.10 On-prem 

 Limit access to investigations using access control 

 Limit access to incidents and investigations in Cortex XSOAR 8.10 On-prem. 

 In any SOC team, there are various roles and responsibilities. For example, you may have specific teams to deal with threats, such as threat intelligence researchers, security analysts (Tier 1), senior analysts (Tier 2), SOC leads, SOC managers, and SIEM engineers. Administrators can exclude access to incident actions and investigations using role-based permissions. For example, you may want to limit the ability to change the incident status or manage the Work Plan. For more information, see Role-based permissions . 

 You can limit access to investigations by doing the following: 

 Restrict an investigation 

 Limit investigations according to specific user roles 

 Give read-only access to certain user roles 

 Restrict an investigation 

 You can restrict an investigation to the incident owner and the team associated with the investigation. 

 Restrict the incident to only team members. For example, if an incident contains sensitive data, and you only want specific users to investigate the incident, you can mark the incident as restricted. Other users cannot view or access the incident. Team members are added automatically when you send them a notification in the CLI. You can remove the restricted investigation at any time. 

 Note 

 All team members have read and write permissions. If you add team members, but their roles have read-only permission, the user still has read and write permission and can access the investigation. 

 Go to the Incidents page and select the incident you want to restrict. 

 Select Actions → Restrict incident . 

 To remove the restriction select Actions → Permit incident . 

 Confirmation appears in the War Room. 

 Note 

 If using the CLI, run the /investigation_restrict id=``<id number> or the /investigation_permit id=``<id number> command. 

 Limit access to investigations according to specific roles 

 When you add a role to the incident, you restrict access to all roles other than those you have specifically added. For example, after an investigation is closed, add administrators or those with specialty roles, so only they can reopen or link incidents. The added roles have read and write permission, but all other roles do not have access (unless you have added them in the XSOAR Read Only Roles field). 

 Note 

 If you add a role, but the incident has been restricted to team members, and the user is not a team member, the user cannot access the incident, regardless of the role. For example, if you restrict the incident to User A and User B team members who are Tier 1 analysts but then try to add Tier 2 analysts (none of whom are team members) to the list of roles, a Tier 2 analyst cannot access the incident. 

 If no role is set for the incident, all users with read/write permissions for incidents can access and edit the incident. To access an incident, you must be assigned the same role that is assigned to the incident, even if you are the creator of the incident. 

 On the Incident page, open the incident to restrict access. 

 Do one of the following: 

 If the Roles field is added to the incident layout, select the relevant role. 

 In the CLI, run !setIncident roles =``<name of role> to set the role. 

 You can also run the /incident_set command roles ``<name of role> , which has the same effect. 

 The War Room entry confirms that the role has been updated. 

 Note 

 When you create or edit an incident, you can select the required Role . 

 You can add this field to the incidents table on the Incidents page (you can't add roles in the table). 

 Give access to Read-only roles 

 You can add a Read-only role to the incident, which restricts access to the incident. When granting read-only access, the user can view the incident but not edit it. For example, when an incident is in triage (phase 1), you may want all Tier-2 analysts to have read-only access, so that Tier-1 can edit the incident. When the phase changes to phase 2, Tier-1 has read-only access. 

 Adding a team member overrides this restriction, so if you add User A (Tier 1) as a team member, even if you assign Tier-1 as a read-only role, the user still has read/write access. You need to remove the user as a Team Member. 

 Note 

 When an incident is restricted with a read-only role, existing team members automatically get read-only access. Their permissions are adjusted, allowing them to continue viewing the incident, though they will not have write permissions. 

 On the Incident page, open the incident to restrict access. 

 Do one of the following: 

 If the XSOAR Read Only Roles field is added to the incident layout, select the relevant role. 

 In the CLI, you run !setIncident xsoarReadOnlyRoles=``<name of role> to set the read-only role. 

 The War Room entry confirms that the role has been updated. 

 Note 

 If added to the opening incident form, when editing or creating an incident, you can select the required XSOAR Read Only Roles . 

 You can add this field to the incidents table on the Incidents page (you can't add roles in the table). 

 Previous Retain incidents 

 Next Incident Tasks 

 Last updated 2 months ago 

 Was this helpful?

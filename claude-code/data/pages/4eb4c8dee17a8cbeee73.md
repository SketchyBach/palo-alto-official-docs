---
url: https://cortex-docs.paloaltonetworks.com/cortex-xdr-5.x/onboard-cortex-xdr/post-deployment-steps/set-up-your-environment/data-and-log-forwarding/data-and-log-notification-formats/agent-audit-log-notification-format
fetched_at: 2026-09-16T08:38:00Z
source: cortex-platform
---

# Agent Audit log notification format | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XDR 

 Cortex XDR 5.x Documentation 

 Onboard Cortex XDR 

 Post-deployment steps 

 Set up your environment 

 Data and log forwarding 

 Data and log notification formats 

 Cortex XDR 5.x 

 Agent Audit log notification format 

 Review the email and syslog formats for agent audit log notifications. 

 License type: Forwarding agent audit logs requires a Cortex XDR Pro per Endpoint license. 

 Cortex XDR forwards the Agent Audit log to these external data resources: 

 Email account: Sent according to the settings you configured 

 Syslog receiver: Sent in a CEF format RFC 5425 according to the following mapping: 

 Section 

 Description 

 Syslog header 

 <9>: PRI (considered a prioirty field)1: version number2020-03-22T07:55:07.964311Z: timestamp of when issue/log was sentcortexxdr: host name 

 CEF hHeader 

 HEADER/Vendor="Palo Alto Networks" (as a constant string)HEADER/Device Product="Cortex XDR Agent" (as a constant string)HEADER/Device Version= Cortex XDR Agent version (7.0/7.1....)HEADER/Severity=(integer/0 - Unknown, 6 - Low, 8 - Medium, 9 - High)HEADER/Device Event Class ID="Agent Audit Logs" (as a constant string)HEADER/name = type 

 CEF body 

 dvchost=domain shost=endpoint_name cat=category end=timestamp rt=received_time cs1Label=agentversion (constant string) cs1=agent_version cs2Label=subtype (constant string) cs2=subtype cs3Label=result (constant string) cs3=result cs4Label=reason (constant string) cs4=reason msg=event_description tenantname=tenant_name tenantCDLid=tenant_id CSPaccountname=csp_id 

 Ask Copy 

 <182>1 2020-10-04T10:41:14.608731Z cortexxdr - - - - CEF:0|Palo Alto Networks|Cortex XDR Agent|Cortex XDR Agent 7.2.0.63060|Agent Audit Logs|Agent Service|9|dvchost=WORKGROUP shost=Test-Agent cat=Monitoring end=1601808073102 rt=1601808074596 cs1Label=agentversion cs1=7.2.0.63060 cs2Label=subtype cs2=Stop cs3Label=result cs3=N\/A cs4Label=reason cs4=None msg=XDR service cyserver was stopped on Test-Agent tenantname=Test tenantCDLid=123456 CSPaccountname=1234 

 Previous Issue notification format 

 Next Management Audit log notification format 

 Last updated 15 days ago 

 Was this helpful?

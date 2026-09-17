---
url: https://docs.prismacloud.io/admin-guide/32/audit/event-viewer
fetched_at: 2026-09-16T13:37:38Z
source: prisma-cloud
---

# Event viewer | 32 | Prisma Cloud arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Compute Edition 

 Admin Guide 

 32 

 Audit 

 Event viewer 

 Prisma Cloud creates and stores audit event records (audits) for all major subsystems. Audits can be reviewed in Monitor > Events , or they can be retrieved from the Prisma Cloud Compute API . If you have a centralized syslog collector, you can integrate Prisma Cloud with your existing infrastructure by configuring Prisma Cloud to send all audit events to syslog in RFC5424 -compliant format. 

 You can review some of the limits on storing audit events . 

 When you’re reviewing audits in a dialog, the list of audits isn’t updated in real-time. To retrieve all the latest data, close the dialog. If the Refresh button is decorated with a red indicator, click it to refresh the view with the latest data, then reopen the dialog. 

 Access audits 

 Access to any container resource protected by Defender is logged and aggregated in Console. You can also configure Prisma Cloud to record audits for sudo, SSH, and other events that are executed on hosts protected by Defender. This audit trail links access to system components to individual users. Access events can be viewed in Console under Monitor > Events . 

 Runtime audits 

 Prisma Cloud records an audit every time a runtime sensor (process, network, file system, and system call) detects activity that deviates from the sum of the predictive model plus any runtime rules you’ve defined. For example, a file system audit event is emitted when Prisma Cloud detects malware in a container. Runtime events for containers can be viewed in Console under Monitor > Events . Runtime events for hosts can be viewed in Console under Monitor > Events . 

 Firewall audits 

 Web Application and API Security (WAAS) is a layer 7 filtering engine that ensures only safe, clean traffic ever reaches your web app. Audits are generated when WAAS detects an attack, such as SQL injection or cross-site scripting. WAAS audits can be viewed under Monitor > Events . 

 Admin activity 

 All Prisma Cloud administrative activity can viewed under Manage > View Logs . 

 Prisma Cloud limits viewing of audit trails to those with a job-related need. To view audit events, you must log into Console. Only users with Administrator, Operator, Defender Manager, or Auditor roles can view audit data in Console. Similarly, only users with the above-mentioned roles can retrieve audit data from the Prisma Cloud API. 

 Previous Audit 

 Next Host activity 

 Last updated 2 months ago 

 Was this helpful?

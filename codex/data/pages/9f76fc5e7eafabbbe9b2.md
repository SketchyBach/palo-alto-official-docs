---
url: https://cortex-docs.paloaltonetworks.com/xsoar-6-administrator-guide/6.12/reference-docs/reference/server-configurations/playbook-server-configurations
fetched_at: 2026-09-06T10:49:33Z
source: cortex-platform
---

# Playbook Server Configurations | 6.12 (EoL) | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSOAR 6 

 Cortex XSOAR 6 Administrator Guides 

 6.12 (EoL) 

 Reference Docs 

 Reference 

 Server Configurations 

 Cortex XSOAR 6.12 EoL 

 Playbook Server Configurations 

 Reference playbook server configurations in Cortex XSOAR 6.12. 

 Key 

 Description 

 Default 

 clean.playbook.debug.sessions.interval 

 Changes the automatic termination of debugger sessions (in minutes). Can be used for debugger troubleshooting . 

 180 

 content.playbooks.unlock 

 Comma-separated playbook names to unlock. 

 N/a 

 ignore.default.in.playbooks 

 Whether to allow the Do Not Use By Default checkbox to affect playbooks. By default, the Cortex XSOAR playbook does not take Do not use by default into account (only for CLI Commands). For example, if you have 3 mail sender instances, 2 of them are set to not use by default, when running the playbook without specifying an instance, it sends with all 3 instances. After you set this configuration to true , it only sends from the one that is not marked as do not use by default . 

 false 

 messages.html.formats.externalFormSubmit 

 Customizes a Data Collection task . 

 N/a 

 messages.html.formats.externalAskSubmit 

 Customizes an Ask task . Add HTML with your customizations as the value. 

 N/a 

 modules.execute.retries.count.maximum 

 Determines how many times the script attempts to run before generating an error in a playbook task. 

 100 

 modules.execute.retries.interval.maximum 

 Determines the wait time (in seconds) between each execution of the script in a playbook task. 

 800 

 playbook.debug.sessions.duration.max 

 The maximum time in hours a debugger session can remain open. Can be used for debugger troubleshooting . 

 24 

 playbook.loop.max 

 Sets the maximum number of times the playbook loop will iterate, until it stops. 

 100 

 playbook.stuck.notification.users 

 Notifies users when Playbooks fail (comma-separated-user names). 

 N/a 

 soc.name 

 Customizes the SOC name in the survey header for an Ask task. For more information, see Customize the SOC Name . 

 N/a 

 workers.count.debug 

 Changes the number of workers, when using the Playbook debugger. Can be used in debugger troubleshooting . 

 ** 1 

 playbook.willnotexecute.old.eval 

 Prevents repeated task checks in playbooks. Do not change to true unless instructed to do so by Customer Support. 

 false 

 active.directory.auth.external.instance 

 When setting up communication task authentication with Active Directory, if you see the error message could not find a provider to authenticate with , add this server configuration. The value is the name of your Active Directory instance. 

 N/a 

 comm.ask.linktocontext.enabled 

 Whether to add generated links for an Ask task to the Context Data. 

 false 

 comm.datacollection.linktocontext.enabled 

 Whether to add generated links for a Data Collection task to the Context Data. 

 false 

 Previous Notification Server Configurations 

 Next Proxy Server Configurations 

 Last updated 3 days ago 

 Was this helpful?

---
url: https://cortex-docs.paloaltonetworks.com/xsoar-6-administrator-guide/6.14/onboard-cortex-xsoar/disaster-recovery-and-live-backup/troubleshoot-live-backup
fetched_at: 2026-09-16T08:56:04Z
source: cortex-platform
---

# Troubleshoot Live Backup | 6.14 | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSOAR 6 

 Cortex XSOAR 6 Administrator Guides 

 6.14 

 Onboard Cortex XSOAR 

 Disaster Recovery and Live Backup 

 Cortex XSOAR 6.14 

 Troubleshoot Live Backup 

 Troubleshoot live backup and disaster recovery scenarios in Cortex XSOAR 6.14. 

 The following are recommendations for live backup errors. 

 Live Backup Error Message on the Disaster Recovery Page 

 disaster-recovery-live-backup-error-message.PNG 

 This message indicates the system is in Recovery Mode and how many actions remain to be transferred before it exits Recovery Mode. 

 If due to connectivity issues data transfer is either slow or suspended between the live backup server and the production server, actions can accumulate on the live backup server. Once connectivity is restored, the system enters Recovery Mode until the accumulated actions are transferred. 

 Out of Memory Error Message 

 If you receive an out of memory error when live backup is enabled, consider changing the server configurations for disaster recovery. 

 Select Settings → ABOUT → Troubleshooting → Add Server Configuration . 

 Add the following configurations 

 Key 

 Description 

 Value 

 dr.batch.size 

 Controls the number of actions sent to the disaster recovery server in one request. A very high value can cause memory issues. A very low value can cause performance issues, which causes the backup server to be synced slower (not in real-time). 

 It is recommended to start low (25-50) and increase according to memory usage. 

 Default is 300 

 dr.memory.limit.mb 

 Limits the memory size (in MB) of the action items, which should prevent out of memory errors. 

 dr.batch.size and dr.memory.limit.db work together, so the threshold is reached when the limitation of either configuration is met. 

 If you receive an out of memory error, consider reducing to 100. 

 Default is 300 

 dr.queue.size 

 The total number of actions to keep in memory before entering recovery mode. It is recommended to keep the default number, as it is relative to the size of the dr.batch.size configuration. 

 Default is 10*dr.batch.size 

 Previous Restore a Partition 

 Next Users and Roles 

 Last updated 13 days ago 

 Was this helpful?

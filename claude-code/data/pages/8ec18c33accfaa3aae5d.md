---
url: https://cortex-docs.paloaltonetworks.com/xsoar-6-administrator-guide/6.14/reference-docs/reference/performance-tuning-for-cortex-xsoar
fetched_at: 2026-09-16T08:56:34Z
source: cortex-platform
---

# Performance Tuning for Cortex XSOAR | 6.14 | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSOAR 6 

 Cortex XSOAR 6 Administrator Guides 

 6.14 

 Reference Docs 

 Reference 

 Cortex XSOAR 6.14 

 Performance Tuning for Cortex XSOAR 

 Tune Cortex XSOAR 6.14 performance for reliable and scalable security operations. 

 Performance tuning may include general troubleshooting for memory and CPU usage, or troubleshooting of more specific UI issues, for example playbook execution. The information in this article will help you identify common causes of slow system performance and implement system improvements. 

 Memory Issues 

 Memory issues are a common cause of slow system performance. To verify if memory issues are causing performance issues, check for memory spikes in the system health dashboard and search the journalctl log for the following entry: kernel: Out of memory: Kill process X (server) score X or sacrifice child . 

 Issue 

 Relevant 

 Database 

 Verification 

 Solution 

 Storing large amount of historical data (more than 1 year) 

 BoltDB 

 Check the file sizes in the partition folder to verify that no file is larger than 10GB. The default directory is /var/lib/demisto/data/ partitionsData . 

 Archive old data. For more information, learn how to Free up Disk Space with Data Archiving . 

 Inefficient playbooks storing too much data 

 BoltDB 

 Validate with Largest Incidents by Storage Size widget. This widget is part of the Common Widgets content pack. 

 Archive old data. For more information, learn how to Free up Disk Space with Data Archiving . 

 Playbooks performing many loops or creating many entries 

 BoltDB 

 Verify with dbstats route https:// localhost:8443/ dbstats that no investigation has more than 500 entries. 

 Reduce the number of loops and/or entries. 

 Server machine does not meet the minimum memory requirements 

 BoltDB / Elasticsearch 

 Open the docker.log file in the log bundle and check the memory and CPU of the machine. 

 Verify that your server meets the minimum memory requirements . 

 Storage does not meeting minimum requirements 

 BoltDB 

 N/A 

 Verify that the disk is SSD based, with 3k dedicated IOPS. 

 Too much data indexing of investigation tasks or entries 

 BoltDB 

 Check folders with prefix /var/lib/demisto/data/demistoidx/ invTaskIdx_ for files larger than 3GB. 

 Add the following server configuration and value to limit indexing: investigation.task.partial.index = 7 . 

 Docker containers 

 BoltDB / Elasticsearch 

 Check docker.log file. Verify number of running containers, machine CPU/memory and Docker stats that indicate whether a container is consuming too many resources. 

 Limit container resources . 

 Audits index folder 

 BoltDB 

 Check the file sizes in the audits index folder to verify that no file is larger than 3GB. The default directory is /var/lib/demisto/data/demistoidx/audits . 

 Perform scheduled and manual audit purges . 

 Messages index 

 BoltDB 

 Check the file size of the messages index to verify it isn’t larger than 3GB. The default directory is /var/lib/demisto/data/demistoidx/messages . 

 Drop messages and delete the index. Add configuration setting: disable.msgs.sending . 

 CPU Spikes 

 Check for CPU spikes by viewing the system health dashboard or by using system tools such as the Linux top command. 

 Issue 

 Relevant Database 

 Verification 

 Solution 

 Too many threads 

 BoltDB / Elasticsearch 

 Check threads in the go_stats.log file. More than 3000 threads (referred to as goroutines in Golang) indicates a possible thread leak or too many processes/tasks running in parallel. 

 Restart service. If problem reoccurs, contact Cortex XSOAR customer support. 

 Workers overloaded 

 BoltDB / Elasticsearch 

 Check workers.log file. Available or Buffer Space == 0, indicates the system is overloaded. If Total == Busy, the system has all workers busy, and you need to increase workers. 

 Change default number of workers . 

 Docker containers overloaded 

 BoltDB / Elasticsearch 

 Check docker.log file. Verify number of running containers, machine CPU/memory and Docker stats that indicate whether a container is consuming too many resources. 

 Change limit for pool of running Docker images (default is 20) with the server configuration: containers.high.water.mark or for a specific Docker image containers.high.water.mark.${image_name} . 

 Slow Playbooks 

 Issue 

 Relevant Database 

 Verification 

 Solution 

 Indicator Extraction Enabled 

 BoltDB / Elasticsearch 

 N/A 

 Check Indicator Extraction settings and turn off Indicator Extraction where not needed. See Indicator Extraction . 

 Enrichment integrations that fail or timeout 

 BoltDB / Elasticsearch 

 Verify you don’t have enrichment integrations that fail frequently or experience timeouts. This might occur with free enrichment services that quickly exceed quotas. 

 Depending on the integration, you might need to increase the quota or modify integration settings. 

 Playbooks storing a large amount of data 

 BoltDB / Elasticsearch 

 Check if playbooks are storing more than 0.5 MB per incident. Confirm by running !PrintContext in the War Room, downloading output entry to a file and checking file size. If file size is not over 0.5 MB, run !Print value=${incident} to view incident data. 

 View playbook metadata to understand which tasks are generating large amounts of data and then optimize tasks to reduce data storage. 

 Complex playbooks with many tasks 

 BoltDB / Elasticsearch 

 Check for playbooks with a large number of tasks or sub playbooks. 

 Confirm that the playbook.willnotexecute.old.eval server configuration has NOT been set to True . By default, the playbook.willnotexecute.old.eval server configuration is set to False , which prevents repeated task checks in playbooks. 

 Other Possible Performance Issues 

 Issue 

 Relevant Database 

 Verification 

 Solution 

 Insufficient disk space 

 BoltDB 

 Check the filesystem.log in the log bundle for large files and folders. 

 Archive old data. For more information, learn how to Free up Disk Space with Data Archiving . 

 Indicators page 

 BoltDB / Elasticsearch 

 Check for noticeable lags on the Indicators page. 

 Exclude indicators that appear in every incident. 

 Check Indicator Extraction settings and turn off Indicator Extraction where not needed. See Indicator Extraction . 

 Overall slow UI 

 BoltDB / Elasticsearch 

 Check network latency and ping other Cortex XSOAR components, such as engines from the server. 

 Check with your IT admin regarding latency between client and server. 

 Large exclusion list impacts system performance 

 BoltDB/Elasticsearch 

 Go to Settings → About → System Diagnostics to check if list exceeds 1000 entries (yellow, Issue) or 5000 entries (red, At Risk). 

 Check if you can add a regex instead of specific indicator values. Using a regex will reduce the number of individual entries and improve performance. 

 Verify that exclusion list entries are up to date and remove any that are no longer relevant. 

 WebSockets 

 If the Cortex XSOAR server is responding slowly and does not receive data updates on certain pages and actions, the WebSocket might be disconnecting. 

 Verification Steps 

 Confirm that this issue persists across different browsers (Chrome, Firefox, etc.) 

 Check WebSocket messages on the server. 

 Check the server.log file for messages to confirm that the WebSocket scenario is working, e.g., WebSocket req arrived and HTTP connection upgraded to WebSocket. 

 Check for WebSocket errors such as: Closing WebSocket ReadPump with err: websocket: close 1005 (no status). 

 Previous Fix System Diagnostics Issues 

 Next Supported Ciphers 

 Last updated 13 days ago 

 Was this helpful?

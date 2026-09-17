---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsoar-8-on-prem/8.8/onboard-cortex-xsoar/back-up-and-restore-cortex-xsoar/restore-backups-between-clusters
fetched_at: 2026-09-16T09:13:21Z
source: cortex-platform
---

# Restore backups between clusters | 8.8 (EoL) | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSOAR 8 

 Cortex XSOAR 8 On-prem Documentation 

 8.8 (EoL) 

 Onboard Cortex XSOAR 

 Back up and Restore Cortex XSOAR 

 Cortex XSOAR 8.8 On-prem EoL 

 Restore backups between clusters 

 Restore backups between Cortex XSOAR 8.8 On-prem clusters. 

 Restoring a backup from one cluster to another enables setting a clean or standby Cortex XSOAR environment to the same state as the original backed-up Cortex XSOAR environment. 

 Danger 

 Verify you have an existing backup. View the available list of backups by running the sudo /home/viewer/sbin/backup-cli backup list command in your CLI. 

 Ensure the new cluster has the following configurations and hardware specifications. 

 The FQDN for the new cluster must be the same as the previous cluster. 

 The new cluster must have the same amount of nodes as the previous cluster. 

 The new cluster must have the same scale size (CPU, memory, and disk space) as the previous cluster. 

 The UI Account Admin user for the new cluster must have the same password as the UI Account Admin user in the previous cluster. 

 Note 

 The node IP addresses in the new cluster can differ from the previous one. 

 Ensure the NFS server is accessible from both deployments. The subnet should be the same, or another entry should exist for the new cluster but with the same path on the NFS server. 

 Verify the new cluster was installed successfully and the UI is accessible. 

 How to restore a backup between clusters 

 From the new cluster CLI, run the backup-cli install command to connect the NFS server to the new cluster. 

 Note 

 Use the same NFS server IP, path, and size limit from the previous deployment. 

 Ask Copy 

 sudo /home/viewer/sbin/backup-cli install [nfs-server-ip] [nfs-path] [size-limit (GB)] 

 Example: 

 Ask Copy 

 sudo /home/viewer/sbin/backup-cli install 1.1.1.1 /some/path/to/nfs/ 1024 

 The CLI shows a list of tasks performed to connect the NFS server to the cluster. This can take a few minutes. 

 opp-backup-restore-nfs-install.png 

 Run the backup list command to verify you can see the backups from the previous cluster. 

 Example: 

 Ask Copy 

 sudo /home/viewer/sbin/backup-cli backup list 

 Run the restore command to restore a specific backup to the new cluster. 

 Ask Copy 

 sudo /home/viewer/sbin/backup-cli restore [backup-name] 

 Example: 

 Ask Copy 

 sudo /home/viewer/sbin/backup-cli restore xsoar8-7-0-12-20240818050050 

 Validate that the data is restored to the new cluster. 

 For more information on the backup and restore commands, see Run backup and restore operations from the CLI . 

 Previous Run backup and restore operations from the CLI 

 Next Engines 

 Last updated 2 months ago 

 Was this helpful?

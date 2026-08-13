---
url: https://docs.paloaltonetworks.com/advanced-wildfire/wildfire-appliance/wildfire-appliance-clusters/upgrade-wildfire-appliance-in-a-cluster/wildfire-cluster-upgrade-validation
fetched_at: 2026-08-13T15:20:20Z
source: palo-alto-main
---

# WildFire Cluster Upgrade Validation Clear

WildFire Cluster Upgrade Validation 

 Home 

 EN

 Location 

 Documentation Home 

 Palo Alto Networks 

 Support 

 Live Community 

 Knowledge Base 

 >

 Strata Copilot

 WildFire Cluster Upgrade Validation 

 Updated on 

 Mon Mar 02 18:41:58 PST 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Advanced WildFire 

 Administration 

 Appliance 

 Updated on 

 Mon Mar 02 18:41:58 PST 2026 

 Focus 

 Home 

 Advanced WildFire Powered by Precision AI™ 

 WildFire Appliance Clusters 

 Upgrade WildFire Appliances in a Cluster 

 WildFire Cluster Upgrade Validation 

 Download PDF 

 Advanced WildFire Powered by Precision AI™ 

 WildFire Cluster Upgrade Validation 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Advanced WildFire 

 Administration 

 Appliance 

 Previous 

 Upgrade a Cluster Locally without an Internet Connection 

 Next 

 Troubleshoot a WildFire Cluster 

 WildFire Cluster Upgrade Validation 

 Where Can I Use
 This? What Do I Need? 

 WildFire Appliance 

 WildFire License 

 The following steps are recommended for validating the WildFire appliance cluster
 node(s) after upgrading the software on the
 appliance. 

 The following steps are to be performed on all WildFire appliance cluster
 controller nodes (active / passive), the worker server, and worker nodes. 

 View the status of the reboot tasks on the WildFire controller
 node. 

 On the WildFire cluster controller, run the following command and
 look for the job type Install and Status
 FIN : 

 admin@WF-500(active-controller)> show
cluster task pending 

 Check that the WildFire appliance is ready to resume sample analysis.
 This ensures all install jobs are completed, all services are up and
 functional. 

 Verify that the sw-version field shows the upgraded release
 version: 

 admin@WF-500(passive-controller)> show
system info | match sw-version 

 Confirm that all processes are running: 

 admin@WF-500(passive-controller)> show
system software status 

 Confirm that the auto-commit ( AutoCom )
 job is complete: 

 admin@WF-500(passive-controller)> show
jobs all 

 Confirm that data migration has successfully completed. Run
 show cluster
 data-migration-status to view the
 progress of the database merge. After the data merge is
 complete the completion timestamp displays: 

 100% completed on Mon Sep 9 21:44:48 PDT 2019 

 The duration of a data merge depends on the amount of
 data stored on the WildFire appliance. Be sure to allot
 at least several hours for recovery as the data merge
 can be a lengthy process. 

 Validate cluster membership. Ensure all nodes are still in
 their respective roles, all services have maintained their status
 (Leader, JoinedCluster, StandyWorker, etc). Make sure no services
 are in commit-lock status. 

 admin@WF-500(passive-controller)> show
cluster membership 

 admin@WF-500(passive-controller)> show
cluster all-peers 

 Make sure all the jobs have been completed: 

 admin@WF-500(passive-controller)> show jobs pending 

 admin@WF-500(passive-controller)> show jobs processed 

 Verify that all interfaces are up and the counter does not show any
 anomalies: 

 admin@WF-500(passive-controller)> show system disk-space 

 admin@WF-500(passive-controller)> show interface all 

 admin@WF-500(passive-controller)> show arp all 

 admin@WF-500(passive-controller)> show interface eth1 

 admin@WF-500(passive-controller)> show interface eth2 

 admin@WF-500(passive-controller)> show interface eth3 

 admin@WF-500(passive-controller)> show counter interface management 

 admin@WF-500(passive-controller)> show counter interface eth1 

 admin@WF-500(passive-controller)> show counter interface eth2 

 admin@WF-500(passive-controller)> show counter interface eth3

 Verify that all consul related configuration and task queue status
 are operational: 

 admin@WF-500(passive-controller)> debug cluster diagnostic 

 admin@WF-500(passive-controller)> debug cluster agent connectivity 

 admin@WF-500(passive-controller)> debug cluster agent dump-kv

 ( WildFire cluster active controller only ) The following steps are to
 be performed after completing Step 1 . 

 While the active controller is being upgraded, validate that the
 passive controller switches over to become active. 

 After the active controller is upgraded and accessible. Validate
 active controller comes up as passive controller. 

 ( After all nodes in the WildFire cluster have been upgraded ) Verify
 that a controller node (active / passive) or worker server is 
 Ready/ReadyLeader for Global-db and Global-queue
 service. 

 admin@WF-500(passive-controller)> show cluster membership 

 Active controller example: 

 Service Summary: wfpc signature
Cluster name: cluster1
Address: 1.2.3.321
Host name: wf101
Node name: wfpc-123456789123456-internal
Serial number: 123456789123456
Node mode: controller
Server role: True
HA priority: primary
Last changed: Mon, 10 Mar 2025 02:47:33 -0700
Services: infra signature wfcore wfpc
Monitor status:
 Serf Health Status: passing
 Agent alive and reachable
 Service 'infra' check: passing
Application status:
 global-queue-service: ReadyLeader
 global-db-service: ReadyLeader
 siggen-db: ReadyMaster
 wildfire-management-service: Done
 wildfire-apps-service: Ready
Work queue status:
 sample analysis queued: 0
 sample analysis running: 0
 sample copy queued: 0
 sample copy running: 0

Diag report:
 2.2.2.202: reported leader '2.2.2.204', age 0.
 2.2.2.204: local node passed sanity check.

 Passive controller example: 

 Service Summary: wfpc signature
Cluster name: cluster1
Address: 1.2.3.789
Host name: wf102
Node name: wfpc-1234567891234-internal
Serial number: 1234567891234
Node mode: controller
Server role: True
HA priority: secondary
Last changed: Mon, 10 Mar 2025 02:38:53 -0700
Services: infra signature wfcore wfpc
Monitor status:
 Serf Health Status: passing
 Agent alive and reachable
 Service 'infra' check: passing
Application status:
 global-queue-service: JoinedCluster
 global-db-service: Ready
 siggen-db: ReadySlave
 wildfire-management-service: Done
 wildfire-apps-service: Ready
Work queue status:
 sample analysis queued: 0
 sample analysis running: 0
 sample copy queued: 0
 sample copy running: 0

Diag report:
 2.2.2.202: reported leader '2.2.2.204', age 0.
 2.2.2.205: local node passed sanity check.

 Worker server node example: 

 Service Summary: wfpc
Cluster name: cluster1
Address: 1.2.3.456
Host name: wf103
Node name: wfpc-123456789123456-internal
Serial number: 123456789123456
Node mode: worker
Server role: True
HA priority:
Last changed: Mon, 10 Mar 2025 02:54:53 -0700
Services: infra wfcore wfpc
Monitor status:
 Serf Health Status: passing
 Agent alive and reachable
 Service 'infra' check: passing
Application status:
 global-queue-service: JoinedCluster
 global-db-service: JoinedCluster
 siggen-db: Stopped
 wildfire-management-service: Done
 wildfire-apps-service: Ready
Work queue status:
 sample analysis queued: 0
 sample analysis running: 0
 sample copy queued: 0
 sample copy running: 0

Diag report:
 2.2.2.202: reported leader '2.2.2.204', age 0.
 2.2.2.202: local node passed sanity check.

 Worker client node example: 

 Service Summary: wfpc
Cluster name: cluster1
Address: 1.2.3.123
Host name: wf206B
Node name: wfpc-123456789123456-internal
Serial number: 123456789123456
Node mode: worker
Server role: False
HA priority:
Last changed: Tue, 18 Mar 2025 09:08:16 -0700
Services: infra wfpc
Monitor status:
 Serf Health Status: passing
 Agent alive and reachable
 Service 'infra' check: passing
Application status:
 global-queue-service: StandbyAsWorker
 global-db-service: StandbyAsWorker
 siggen-db: Deregistered
 wildfire-management-service: Done
 wildfire-apps-service: Ready
Work queue status:
 sample analysis queued: 0
 sample analysis running: 0
 sample copy queued: 0
 sample copy running: 0

Diag report:
 2.2.2.201: reported leader '2.2.2.205', age 0.
 2.2.2.206: local node passed sanity check.

 Previous 

 Upgrade a Cluster Locally without an Internet Connection 

 Next 

 Troubleshoot a WildFire Cluster 

 On This Page 

 Activation & Onboarding 

 Strata Cloud Manager 

 Activate a License or Product 

 Strata Logging Service 

 Device Associations 

 Hub 

 Identity and Access Management 

 Tenant Management 

 Next-Generation Firewalls 

 AIOps for NGFW 

 Cloud Management for NGFWs 

 Firewalls 

 PAN-OS 

 Panorama 

 VM-Series 

 SASE 

 Prisma Access 

 Cloud-Delivered Security Services 

 Advanced WildFire 

 Advanced URL Filtering 

 Advanced Threat Prevention 

 Advanced DNS Security 

 AI Access Security 

 Device Security 

 Enterprise DLP 

 SaaS Security 

 Network Security 

 Security Policy 

 Visibility & Monitoring 

 Dashboards 

 Incidents and Alerts 

 Reports 

 WF-500-B Appliance 

 12.2 

 Network Security 

 PAN-OS 

 Advanced Wildfire 

 Appliance 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

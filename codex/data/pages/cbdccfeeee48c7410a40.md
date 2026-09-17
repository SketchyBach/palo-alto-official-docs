---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsoar-8-on-prem/8.11/onboard-cortex-xsoar/cortex-xsoar-installation/post-installation/optimize-performance-and-robustness-from-the-textual-ui
fetched_at: 2026-09-16T08:54:31Z
source: cortex-platform
---

# Optimize performance and robustness from the textual UI | 8.11 | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSOAR 8 

 Cortex XSOAR 8 On-prem Documentation 

 8.11 

 Onboard Cortex XSOAR 

 Cortex XSOAR Installation 

 Post-installation 

 Cortex XSOAR 8.11 On-prem 

 Optimize performance and robustness from the textual UI 

 Optimize Cortex XSOAR 8.11 On-prem from the VM textual UI. 

 Once Cortex XSOAR is installed, you can perform system performance optimization tasks from the textual UI, for example: 

 Set up an external load balancer. 

 Add or remove nodes from a cluster. 

 Scale up hardware resources. 

 How to access the textual UI menu 

 To access the textual UI menu, log in from the VM web console or from an external terminal using the ssh admin@<server ip address> command to SSH log in. 

 Important 

 If you lose the SSH password, you cannot recover or change it. To use SSH you will need to redeploy the VM. 

 For example: 

 opp-oci-cloud-shell.png 

 The textual UI menu opens with all the configuration and maintenance options. 

 Tip 

 To start using the textual UI, click anywhere on the screen. 

 To navigate between the menu items, use the up and down arrow keys. To select a menu item, press the Enter key. 

 To navigate between fields within a menu item, use the Tab key. To save settings, tab to the Save button and press the Enter key. 

 To go back to the menu from a specific menu item field, press the esc key. 

 Manage nodes in a cluster 

 If you deployed your Cortex XSOAR environment starting with three nodes, using the textual UI menu in your VM you can add a node, taint a node, remove a node, drain a node, and uncordon a node. 

 Important 

 If you deployed your Cortex XSOAR environment as a standalone (single node), you cannot add nodes to it and switch to a cluster. 

 A Kubernetes cluster consists of a control plane and one or more worker nodes. For Cortex XSOAR, in standalone (one VM), the VM acts as both control plane and as a worker node. In multi-node clusters, the first three nodes act as both control plane and as worker nodes, and any additional node added acts as a worker node. 

 If you remove one of the original three nodes in the cluster (one of the control planes), you cannot perform actions such as upgrade or scaling up. When you add a new node, Cortex XSOAR automatically assigns the new node as a control plane with the same IP address as the node that was removed. 

 You need to set the host again and reestablish trust between all the nodes if you want to add more nodes to the cluster after completing installation. 

 Add a node 

 Add a node to a cluster to increase its capacity and improve robustness for better load distribution. For example, by adding more nodes, playbook runs can be divided among them. This reduces the strain on each node and lowers the risk of system overload, while the workload capacity remains the same within the cluster. 

 From the textual UI menu in your VM, select Cluster Administration . 

 Set the host again and reestablish trust between all nodes in the cluster, including the new node (see Task 5. Establish trust between all nodes in a cluster). 

 Select Add Node . 

 Enter the IP Address and click Add . 

 Taint a node 

 Tainting a node marks the node as out of service for internal K8s functions. Taint a node to stop applications from running on it. 

 From the textual UI menu in your VM, select Cluster Administration . 

 Select the IP address of the node you want to taint. 

 Select Taint . 

 In the list of nodes in the Cluster Administration menu, the node IP will display as Ready,SchedulingDisabled . 

 Remove a node 

 Remove a node from a cluster to reduce resources, perform maintenance, or decommission the node, ensuring the cluster operates efficiently without unnecessary or malfunctioning components. 

 From the textual UI menu in your VM, select Cluster Administration . 

 Drain the node. 

 Select the IP address of the node you want to drain. 

 Select Drain . 

 In the list of nodes in the Cluster Administration menu, the node IP will display as Ready,SchedulingDisabled . 

 Remove the node. 

 Select the IP address of the node you want to remove. 

 Select Remove . 

 In the list of nodes in the Cluster Administration menu, the node IP will display as Ready . 

 Drain a node 

 Draining a node pauses the node activity in the cluster and marks it as unschedulable. Draining a node safely removes workloads from it, ensuring that running applications are gracefully terminated or moved to other nodes without disrupting service availability before you perform maintenance on the node. 

 From the textual UI menu in your VM, select Cluster Administration . 

 Select the IP address of the node you want to drain. 

 Select Drain . 

 In the list of nodes in the Cluster Administration menu, the node IP will display as Ready,SchedulingDisabled . 

 Uncordon a node 

 Uncordon a node in a cluster to make it available again for scheduling new workloads, for example after maintenance or troubleshooting is complete. 

 From the textual UI menu in your VM, select Cluster Administration . 

 Select the IP address of the node you want to uncordon. 

 Select Uncordon . 

 In the list of nodes in the Cluster Administration menu, the node IP will display as Ready . 

 Scale up hardware resources 

 The Scale Settings textual UI menu item enables scaling up resources for CPU, memory, and disk size. Before modifying your environment, it is critical to distinguish between scaling up deployment size and extending storage, as the procedures and downtime expectations differ. 

 Scaling up deployment size 

 Scaling up deployment size (CPU & RAM) refers to increasing the CPU cores and RAM to move between scale tiers (for example, Extra-Small → Small → Medium). While Cortex XSOAR allows for scaling, the necessary changes at the hypervisor level (for example, ESXi) often require the VM to be shut down to increase CPU and RAM. Downtime depends entirely on your hypervisor configuration. 

 To scale up the deployment size, first increase the resources on the hypervisor, and then use the Scan scale options in the textual UI. 

 Note 

 You can only scale up, you cannot scale down. 

 Extending storage (disk capacity) 

 Extending storage refers to increasing the data disk capacity of existing nodes to accommodate data growth. For most hypervisors (such as VMware), storage can be expanded on a running VM. This operation typically does not require a restart or service interruption. 

 If you extend storage, all nodes in the cluster must be extended equally to keep the cluster healthy. Do not extend disks on only one node. 

 Important 

 The System Diagnostics page displays storage usage as a percentage. To view the exact available capacity in GB, you may need to open a support session to run backend command-line tools (such as ceph df ), as these metrics are not currently exposed in the UI. 

 How to scale up hardware resources 

 Choose the scale you want and make sure your hardware resources meet the system requirements. For more information, see System requirements . 

 For CPU/RAM scaling: Shut down the VM (if required by your hypervisor), increase the CPU and RAM allocation, and restart the VM. 

 For storage extension: Expand the disk size in your hypervisor. This can usually be done while the VM is running. 

 Note 

 If you are working with more than one node, all the nodes in the cluster must meet the same hardware requirements. 

 When extending storage, every node's disk must be increased to the exact same size to ensure replication stability. 

 From the textual UI menu, select Scale Settings . 

 The supported scale sizes are: 

 Small: 16 CPU, 64 GB memory, 1 TB hard disk (1TB = 1024 GB) 

 Medium: 32 CPU, 128 GB memory, 1.5 TB hard disk 

 Large: 48 CPU, 192 GB memory, 2 TB hard disk 

 opp-tui-scale-settings.png 

 Select Scan Scale Options to run a scan to evaluate the cluster recommended scale. 

 Based on the results, the system indicates the current scale size and gives you the option to increase the scale size. 

 Note 

 The recommended scale is determined by the node with the least hardware resources. 

 Example 7. 

 The following is the type of system message you may see if you need to add resources to scale up. 

 opp-tui-scale-up-message.png 

 The following is the type of system message you may see if you have sufficient resources to scale up. 

 opp-tui-scale-up-message2.png 

 Previous Use a signed certificate instead of SSL verification 

 Next Manage your SSH admin password 

 Last updated 16 days ago 

 Was this helpful?

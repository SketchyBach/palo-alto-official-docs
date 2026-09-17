---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsoar-8-on-prem/8.10/onboard-cortex-xsoar/cortex-xsoar-installation/post-installation/optimize-performance-and-robustness-from-the-textual-ui/auto-expand-pvc-volumes
fetched_at: 2026-09-16T08:54:56Z
source: cortex-platform
---

# Auto expand PVC volumes | 8.10 | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSOAR 8 

 Cortex XSOAR 8 On-prem Documentation 

 8.10 

 Onboard Cortex XSOAR 

 Cortex XSOAR Installation 

 Post-installation 

 Optimize performance and robustness from the textual UI 

 Cortex XSOAR 8.10 On-prem 

 Auto expand PVC volumes 

 Automatically expand PVC volumes in Cortex XSOAR 8.10 On-prem. 

 Auto expansion enables automatically increasing Persistent Volume Claim (PVC) capacity when disk usage reaches a predefined threshold. This ensures application uptime by preventing disk full errors and eliminates the need for manual intervention during storage spikes. 

 You can dynamically enable or disable auto expansion at runtime without restarting or experiencing service interruption. 

 Your configuration choice is persistent, it survives TUI restarts, SSH session terminations, and full system reboots. 

 How auto expansion works 

 Auto expansion relies on an automated background process that regularly monitors disk usage and automatically increases Persistent Volume Claim (PVC) capacity based on predefined thresholds and limits. 

 Expansion trigger 

 The system automatically triggers a volume expansion when any PVC usage reaches 85% capacity. 

 Expansion amount and limits 

 The expansion size is calculated as 20% of the current volume size (rounded to the nearest GiB), capped at a maximum of 40 GiB per event with a minimum limit of 1 GiB. 

 Safety guardrails 

 To protect overall system health, the system enforces not using the full remaining disk space; it will always leave a minimum of 10% free space. 

 Standalone and multinode deployments 

 The auto expand feature operates seamlessly on both standalone and multinode clusters. In a multinode setup, the setting is applied from the primary node. 

 How to configure auto expand 

 From the textual UI menu, select Auto Expand. 

 The following message is displayed: Storage Groups will automatically expand once it reaches 85% capacity, provided there is enough available space on the system. 

 Click to enable or disable auto expansion. 

 In the confirmation dialog, select Apply to confirm the change, or click Back (or the ESC key) to cancel the operation and preserve your original state. 

 A progress indicator displays while applying the change, followed by a success notification upon completion. 

 Previous Scale up hardware resources 

 Next Troubleshoot your installation 

 Last updated 1 month ago 

 Was this helpful?

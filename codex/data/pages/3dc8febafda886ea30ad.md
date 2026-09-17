---
url: https://docs.paloaltonetworks.com/ngfw/help/11-2/device/device-high-availability/cluster-config
fetched_at: 2026-09-16T07:29:17Z
source: palo-alto-main
---

# Cluster Config Clear

Updated on 

 Thu Jun 25 17:41:47 PDT 2026 

 Focus 

 Home 

 Next-Generation Firewall 

 Device 

 Device > High Availability 

 Cluster Config 

 Download PDF 

 Next-Generation Firewall 

 Cluster Config 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Next-Generation Firewall Docs 

 Getting Started 

 Administration 

 Networking 

 Quick Start 

 Reference 

 Incidents & Alerts 

 Release Notes 

 Select a Document 

 PAN-OS 12.2 

 PAN-OS 12.1 

 PAN-OS 11.2 

 PAN-OS 11.1 

 PAN-OS 11.0 (EoL) 

 PAN-OS 10.2 

 PAN-OS 10.1 (EoL) 

 PAN-OS 10.0 (EoL) 

 PAN-OS 9.1 (EoL) 

 PAN-OS 9.0 (EoL) 

 PAN-OS 8.1 (EoL) 

 Help 

 Select a Document 

 PAN-OS 12.2 

 PAN-OS 12.1 

 PAN-OS 11.2 

 PAN-OS 11.1 

 PAN-OS 10.2 

 PAN-OS 10.1 

 New Features 

 Previous 

 HA Active/Active Config 

 Next 

 Device > Log Forwarding Card 

 Cluster Config 

 Add members of an HA cluster. 

 Device > High Availability > Cluster Config 

 Add members to an HA cluster by selecting Device High Availability Cluster Config . 

 Cluster Config 

 Description 

 Add 

 Add a cluster member.
You must add the local firewall and if you are using HA pairs, you
must add both HA peers of the pair as cluster members. 

 ( Supported
firewalls ) Device Serial Number —Enter
the unique serial number of the cluster member. 

 ( Panorama ) Device —Select a device
from the dropdown and enter a Device Name . 

 HA4 IP Address —Enter the IP address of the
HA4 link for the cluster member. 

 HA4 Backup IP Address —Enter the IP address
of the backup HA4 link for the cluster member. 

 Session Synchronization —Select to enable
session synchronization with this cluster member. 

 Description —Enter helpful description. 

 Delete 

 Select one or more cluster members and Delete them
from the cluster. 

 Enable 

 ( Supported firewalls ) You can determine
whether or not a cluster member synchronizes sessions with other
members. By default, all members are allowed to synchronize sessions.
If you disable synchronization for one or more members, select Enable to re-enable
synchronization for one or more members. 

 Disable 

 ( Supported firewalls ) Select one
or more members and Disable synchronization
with other members. 

 Refresh 

 ( Panorama ) Select Refresh to refresh
the list of HA devices in the HA cluster. 

 Previous 

 HA Active/Active Config 

 Next 

 Device > Log Forwarding Card

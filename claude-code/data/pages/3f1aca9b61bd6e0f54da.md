---
url: https://docs.paloaltonetworks.com/pan-os/10-1/pan-os-admin/firewall-administration/reference-port-number-usage/ports-used-for-panorama
fetched_at: 2026-09-16T07:34:16Z
source: palo-alto-main
---

# Ports Used for Panorama Clear

Updated on 

 Aug 31, 2026 

 Focus 

 Home 

 Next-Generation Firewall 

 Firewall Administration 

 Reference: Port Number Usage 

 Ports Used for Panorama 

 Download PDF 

 Next-Generation Firewall 

 Ports Used for Panorama 

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

 Ports Used for Clustering 

 Next 

 Ports Used for GlobalProtect 

 Ports Used for Panorama 

 Network ports and port numbers used by Panorama for firewall management, device
 communication, and administrative functions. 

 Panorama uses the following ports. 

 Destination Port 

 Protocol 

 Description 

 22 

 TCP 

 Used for communication from a client system
to the Panorama CLI interface. 

 443 

 TCP 

 Used for communication from a client system
to the Panorama web interface. 

 Used for outbound communications from Panorama to the Palo Alto
 Networks Update Server. 

 444 

 TCP 
 Used for communication between Panorama and Strata Logging Service . 

 3978 

 TCP 

 Used for communication between Panorama
and managed firewalls or managed collectors, as well as for communication
among managed collectors in a Collector Group: 

 For
communication between Panorama and firewalls. This connection is
initiated from the managed firewall to Panorama and facilitates
a bi-directional data exchange on which the firewalls forward logs
to Panorama and Panorama pushes configuration changes to the firewalls. Context
switching commands are sent over the same connection. 

 Log Collectors use this destination port to forward logs
to Panorama. 

 For communication with the default Log Collector on an M-Series
appliance in Panorama mode and with Dedicated Log Collectors. 

 28443 

 TCP 

 Used for managed devices (firewalls and
Log Collectors) to retrieve software and content updates from Panorama. 

 Only
devices that run PAN-OS 8.x and later releases retrieve updates
from Panorama over this port. For devices running earlier releases,
Panorama pushes the update packages over port 3978. 

 28769 

 28260 

 TCP 

 TCP 

 Used for the HA connectivity and synchronization
between Panorama HA peers using clear text communication. Communication
can be initiated by either peer. 

 ICMP must be allowed on the network for successful Panorama HA
 peer connection and synchronization. Additionally, ICMP is
 required to monitor the failover metrics used to
 detect whether an HA failover is required. 

 28 

 TCP 

 Used for the HA connectivity and synchronization
between Panorama HA peers using encrypted communication (SSH over
TCP). Communication can be initiated by either peer. 

 Used
for communication between Log Collectors in a Collector Group for
log distribution. 

 28270 

 9300 to 9302 (11.1 and later) 

 TCP 

 Used for communication among Log Collectors
in a Collector Group for log distribution. 

 2049 

 TCP 

 Used by the Panorama virtual appliance to
write logs to the NFS datastore. 

 10443 SSL Port that Panorama uses to provide contextual
information about a threat or to seamlessly shift your threat investigation
to the Threat Vault and AutoFocus. 

 23000 to 23999 

 TCP, UDP, or SSL 

 Used for Syslog communication between Panorama and the Traps ESM
 components. 

 8765 

 HTTP 

 Used as an offline license server to distribute licenses in
 air-gapped environments. Requests to 443 are routed to 8765 via
 nginx . 

 Previous 

 Ports Used for Clustering 

 Next 

 Ports Used for GlobalProtect

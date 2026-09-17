---
url: https://docs.paloaltonetworks.com/panorama/administration/troubleshooting/generate-a-stats-dump-file-for-a-managed-firewall
fetched_at: 2026-09-16T07:41:55Z
source: palo-alto-main
---

# Generate a Stats Dump File for a Managed Firewall Clear

Updated on 

 Fri Aug 07 00:12:33 PDT 2026 

 Focus 

 Home 

 Panorama 

 Troubleshooting 

 Generate a Stats Dump File for a Managed Firewall 

 Download PDF 

 Panorama 

 Generate a Stats Dump File for a Managed Firewall 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Panorama Docs 

 Getting Started 

 Administration 

 New Features 

 Previous 

 Troubleshoot Connectivity to Network Resources 

 Next 

 Recover Managed Device Connectivity to Panorama 

 Generate a Stats Dump File for a Managed Firewall 

 Generate a stats dump file for a managed firewall from
the Panorama™ management server. 

 Generate a set of XML reports that summarize
the network traffic over the last seven days for a single firewall
managed by the Panorama™ management server or for all firewalls
managed by Panorama. After you select a managed firewall and generate the
stats dump file, you can download the stats dump file locally to
your device. 

 The Palo Alto Networks or Authorized Partner
systems engineer use the stat dump file to create a Security Lifecycle
Review (SLR) and to perform security checkups after you successfully
deploy your managed firewalls to help strength your security posture.
The SLR highlights activity found on the network and the associated
business or security risks that may be present. For more information
on the SLR, contact your Palo Alto Networks or Authorized Partner
systems engineer. 

 Stats dump file
generation for multiple managed firewalls can take multiple hours
to complete. During this time, you are unable to navigate from the stats
dump file generation user interface so it is recommended to generate
the stats dump file from the CLI so you can continue using the Panorama
web interface. 

 Palo Alto Networks recommends generating a stats dump file for all managed firewalls from the
 Panorama CLI using the following
 command. Panorama must be able to reach your SCP or TFTP server to successfully
 export the stats dump file. 

 SCP
Server 

 admin> scp export stats-dump to <username@hostname:SCP_export_path> 

 TFTP Server 

 admin> tftp export stats-dump to <tftp_host_address> 

 Log in to the Panorama web
 interface . 

 Select Panorama Support and navigate to the Stats
Dump File . 

 Select a managed firewall for which to generate a stats
dump file. 

 It is recommended that you generate a stats dump file for
a single managed firewall from the Panorama web interface. 

 A
stats dump file is generated for All devices by
default if you do not select a managed firewall. 

 Generate Stats Dump File . 

 Click Yes when prompted to proceed
generating the stats dump file. 

 A progress bar of the stats
dump file generation status is displayed. 

 Generation may
take up to an hour for a single managed firewall depending on the volume
of log data. You are unable to navigate from the stats dump file
generation status window during this time. 

 Click Download Stats Dump File to
download the stats dump file to your local device. 

 The downloaded stat dumps file is in a tar.gz file
format. 

 Previous 

 Troubleshoot Connectivity to Network Resources 

 Next 

 Recover Managed Device Connectivity to Panorama

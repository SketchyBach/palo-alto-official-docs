---
url: https://docs.paloaltonetworks.com/advanced-url-filtering/administration/pan-db-private-cloud-overview/set-up-pan-db-private-cloud/configure-firewalls-to-access-pan-db-private-cloud
fetched_at: 2026-09-15T15:08:04Z
source: palo-alto-main
---

# Configure Firewalls to Access the PAN-DB Private Cloud Clear

Updated on 

 Thu Jul 30 19:58:44 PDT 2026 

 Focus 

 Home 

 Advanced URL Filtering 

 PAN-DB Private Cloud 

 Set Up PAN-DB Private Cloud 

 Configure Firewalls to Access the PAN-DB Private Cloud 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 Advanced URL Filtering 

 Configure Firewalls to Access the PAN-DB Private Cloud 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Advanced URL Filtering 

 Administration 

 Previous 

 Configure the PAN-DB Private Cloud 

 Next 

 Configure Authentication with Custom Certificates on the PAN-DB Private Cloud 

 Configure Firewalls to Access the PAN-DB Private Cloud 

 Follow these steps to configure firewall access to the
PAN-DB private cloud servers from your CLI or the firewall’s web
interface. 

 Where can I use
this? What do I need? 

 NGFW (Managed by PAN-OS or Panorama) 

 Advanced URL
 Filtering license (or a legacy URL filtering
 license) 

 Note: Legacy URL filtering licenses are
 discontinued, but active legacy licenses are still
 supported. 

 When using the PAN-DB public cloud, each firewall accesses the PAN-DB servers in the AWS cloud to
 download the list of eligible servers to which it can connect for URL lookups. With
 the PAN-DB private cloud, you must configure the firewalls with a (static) list of
 your PAN-DB private cloud servers that will be used for URL lookups. The list can
 contain up to 20 entries; IPv4 addresses, IPv6 addresses, and FQDNs are supported.
 Each entry on the list— IP address or FQDN—must be assigned to the management port
 or eth1 of the PAN-DB server. 

 From the PAN-OS CLI , add
a list of static PAN-DB private cloud servers used for URL lookups. 

 Use the following CLI command to add the IP addresses of the private PAN-DB servers: 

 > configure 

 # set deviceconfig setting pan-url-db cloud-static-list <IP addresses> 

 Alternatively, in the web interface for each firewall, select Device Setup Content-ID , edit the URL Filtering section, and then enter the
 IP addresses or FQDNs of the PAN-DB servers. The list must be
 comma-separated. 

 To delete the entries for the private PAN-DB servers, use the following CLI command: 

 # delete deviceconfig setting pan-url-db cloud-static-list <IP addresses> 

 Deleting the list of private PAN-DB servers triggers a reelection process on the firewall. The
 firewall first checks for the list of PAN-DB private cloud servers
 and when it can't find one, the firewall accesses the PAN-DB servers
 in the AWS cloud to download the list of eligible servers to which
 it can connect. 

 Enter # commit to save your changes. 

 To verify that the change is effective, use the following
CLI command on the firewall: 

 > show url-cloud status 
Cloud status: Up 
URL database version: 20150417-220 

 Previous 

 Configure the PAN-DB Private Cloud 

 Next 

 Configure Authentication with Custom Certificates on the PAN-DB Private Cloud

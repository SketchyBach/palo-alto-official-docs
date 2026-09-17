---
url: https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/administration/prisma-access-advanced-deployments/mobile-user-globalprotect-advanced-deployments/ddns-for-global-protect-mobile-users.html
fetched_at: 2026-09-16T11:36:48Z
source: palo-alto-main
---

# Dynamic DNS Registration Support for Mobile Users—GlobalProtect Clear

Updated on 

 Sep 3, 2026 

 Focus 

 Home 

 Prisma Access 

 Prisma Access Administration 

 Prisma Access Advanced Deployments 

 Prisma Access Mobile Users—GlobalProtect Advanced Deployments 

 Dynamic DNS Registration Support for Mobile Users—GlobalProtect 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 Deutsch (German) 

 Prisma Access 

 Dynamic DNS Registration Support for Mobile Users—GlobalProtect 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma Access Docs 

 Release Notes 

 Select a Document 

 6.2 Preferred and Innovation 

 6.1 Preferred and Innovation 

 6.0 Preferred and Innovation 

 5.2 Preferred and Innovation 

 5.1 Preferred and Innovation 

 5.0 Preferred and Innovation 

 4.2 Preferred 

 4.1 Preferred 

 4.0 Preferred 

 3.2 Preferred and Innovation 

 Activation & Onboarding 

 Administration 

 Select a Document 

 4.0 & Later 

 Prisma Access China 

 Integrations 

 Incidents & Alerts 

 New Features 

 Previous 

 Configure Dynamic DNS Updates for Prisma Access (Managed by Panorama) 

 Next 

 Enable DDNS for Mobile Users—GlobalProtect 

 Dynamic DNS Registration Support for Mobile Users—GlobalProtect 

 Learn about Dynamic DNS (DDNS) functionality and how
to use it in Prisma Access mobile user GlobalProtect deployments. 

 Where Can I Use This? What Do I Need? 

 Prisma Access (Managed by Panorama) 

 Next-Generation Firewalls that are managed by Panorama with a
 valid Strata Logging Service license and a Cloud Services
 plugin 

 Prisma Access 
 license 

 Minimum Required Prisma Access Version : 3.1.1 Preferred or
 Innovation 

 Supported on Panoramas running versions 10.2 and later (not
 supported on Panoramas running 10.1) 

 Your client endpoints must be domain joined. 

 When a mobile user connects remotely to Prisma Access using GlobalProtect,
the DNS Servers in your enterprise are not updated with the GlobalProtect
gateway-assigned IP address. Before enabling Dynamic DNS (DDNS),
there is no mapping of tunnel IP addresses with the endpoint name,
which are logged as address and pointer (A and PTR) records. Hence,
your IT administrator or user management software cannot map the
remote endpoint name to the IP address. 

 After you enable the DDNS feature on Prisma Access , Prisma Access 
 Cloud Services plugin checks GlobalProtect events in Strata Logging Service every
 15 minutes to capture endpoint hostname, domain name and tunnel IP address. It
 dynamically creates A and PTR records in the DNS server using NSUPDATE. 

 The Dynamic DNS Registration Support feature will be
 deprecated soon. For similar functionality with enhanced capabilities, consider
 using the following features: 
 For NGFW: DHCP Based IP Address Assignment and
 Management for GlobalProtect 

 For Prisma Access: Dynamic DNS Registration Support
 for Remote Troubleshooting and Updates 

 Dynamic DNS Workflow for Mobile Users—GlobalProtect 

 After
you enable DDNS and when a mobile user logs in with the GlobalProtect
app: 

 Read the following sections to get an overview of how
DDNS works, guidelines and requirements, and how to enable it. 

 GlobalProtect establishes an SSL tunnel between the GlobalProtect
endpoint and an on-premises or Prisma Access gateway. 

 GlobalProtect sends the mobile user device’s hostname, domain
name, and tunnel IP address information through the tunnel to the
on-premises or Prisma Access gateway. 

 The on-premises gateway or Prisma Access forwards this information
as GlobalProtect events to Strata Logging Service . 

 The Prisma Access Cloud Services plugin probes Strata Logging Service every 15 minutes
 to update the DNS server. 

 If the plugin
does not receive the GlobalProtect events from Strata Logging Service ,
it retries the request a maximum of five times. If the retry requests
were not successful, the plugin retries the operation every 15 minutes
for a maximum of four times. Therefore, the plugin can receive updates
for a time interval of one hour. 

 If you want more frequent
updates, you can enter the debug plugins cloud_services set-gp-ddns-interval command
to change the update interval to five minutes. A is not required
to update the time interval. If you change the interval to five
minutes, the Cloud Services plugin can update a maximum of 15,000
records with a network latency of 50 msec and can receive updates
for a time interval of 20 minutes. 

 No Commit is
required after you change the time interval using the command. 

 These numbers are from a controlled environment and real-world
operating conditions can affect these numbers. 

 After receiving the updates from Strata Logging Service , the Cloud
Services plugin packages A and PTR records as NSUPDATE, and updates
the primary DNS server every 15 minutes. 

 If you changed the
time interval to five minutes using the debug plugins cloud_services set-gp-ddns-interval command,
the plugin updates the DNS server every five minutes. 

 If the
plugin is unable to update the DNS server through NSUPDATE, the
plugin retries the update operation a maximum of five times. If
the updates were not successful, the plugin retries the update operation
every 15 minutes, or every five minutes if you changed the interval
to five minutes, for a maximum of four times. Therefore, the plugin
tries to update the events that are logged for a maximum of one
hour (if you use a 15-minute interval) or 20 minutes (if you use
a five-minute interval), after which it starts afresh. 

 After the A and PTR records of GlobalProtect mobile users
are available in the DNS server, an IT administrator or an enterprise
software uses these records through a DNS or RDNS lookup and resolves
the endpoint name or IP address. 

 The IT administrator or the endpoint management software
uses this information to manage the endpoint or push software updates. 

 The
following figure illustrates this workflow. 

 To
view the connection failure logs, select Dashboard System Logs or Monitor Logs System for Mobile_User_Device_Group . 

 Dynamic DNS Guidelines and Requirements 

 Before you enable DDNS ,
ensure that your deployment and DNS server meet the following guidelines
and requirements: 

 Your client endpoints must be domain joined. 

 Update your GlobalProtect client
to the following GlobalProtect app versions based on your OS: 

 Windows: 5.2.11 or later 

 Mac: 5.2.11 or later 

 Linux: 5.3.3 or later 

 Enable if
you use an on-premises gateway other than Prisma Access . 

 An Infoblox DNS server with a minimum version of 8.6.1 or
later that supports DDNS updates through NSUPDATE is required. 

 Multitenant Prisma Access deployments do not support DDNS. 

 Save the authentication key from your DNS server in base64
format with a file extension of .key. You can upload the key only
in this format in Prisma Access . 

 Enable NTP on your DNS server and ensure that it is same
as that of Prisma Access . 

 Create zones in Infoblox for reverse PTR and forward A addresses. 

 You can deploy Dynamic DNS in a standalone deployment with
 next-generation firewalls as well as with Prisma Access. For firewalls, all the
 prerequisites in this section apply, and you also must have a valid Strata Logging Service license and use the Cloud Services plugin in Panorama for
 logging. 

 Previous 

 Configure Dynamic DNS Updates for Prisma Access (Managed by Panorama) 

 Next 

 Enable DDNS for Mobile Users—GlobalProtect

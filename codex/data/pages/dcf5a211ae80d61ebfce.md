---
url: https://docs.paloaltonetworks.com/pan-os/10-1/pan-os-admin/monitoring/use-syslog-for-monitoring/configure-syslog-monitoring
fetched_at: 2026-08-13T17:00:27Z
source: palo-alto-main
---

# Configure Syslog Monitoring Clear

Configure Syslog Monitoring 

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

 Configure Syslog Monitoring 

 Updated on 

 Aug 3, 2026 

 Focus 

 Download PDF 

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

 Updated on 

 Aug 3, 2026 

 Focus 

 Home 

 Next-Generation Firewall 

 Monitoring 

 Use Syslog for Monitoring 

 Configure Syslog Monitoring 

 Download PDF 

 Next-Generation Firewall 

 Configure Syslog Monitoring 

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

 Use Syslog for Monitoring 

 Next 

 Syslog Field Descriptions 

 Configure Syslog Monitoring 

 Where Can I Use This? What Do I Need? 

 NGFW 

 For Strata Cloud Manager managed NGFWs: 

 Strata Cloud Manager Pro 

 To Use Syslog for
 Monitoring a Palo Alto Networks firewall, create a Syslog server profile
 and assign it to the log settings for each log type. Optionally, you can configure
 the header format used in syslog messages and enable client authentication for
 syslog over TLSv1.2. 

 For CEF-formated syslog events collection ,
 you must edit the default syslog configuration. The default syslog monitoring
 configuration is not supported for CEF syslog events collection. 

 PAN-OS 

 Strata Cloud Manager 

 Configure Syslog Monitoring (PAN-OS) 

 Configure syslog monitoring in PAN-OS. 

 Configure a Syslog server profile. 

 You can use separate profiles to send syslogs for each log type to a
 different server. To increase availability, define multiple servers (up
 to four) in a single profile. 

 Select Device Server Profiles Syslog . 

 Click Add and enter a
 Name for the profile. 

 If the firewall has more than one virtual system (vsys), select the
 Location (vsys or
 Shared ) where this profile is
 available. 

 For each syslog server, click Add and enter the
 information that the firewall requires to connect to it: 

 Name —Unique name for the server
 profile. 

 Syslog Server —IP address or fully
 qualified domain name (FQDN) of the syslog server. 

 If you configure an FQDN and use
 UDP transport, if the
 firewall cannot resolve the FQDN, the firewall uses the
 existing IP address resolution for the FQDN as the
 Syslog Server address. 

 Transport —Select
 TCP , UDP ,
 or SSL (TLS) as the protocol for
 communicating with the syslog server. For
 SSL , the firewall supports only
 TLSv1.2. 

 Port —The port number on which to send
 syslog messages (default is UDP on port 514); you must use
 the same port number on the firewall and the syslog
 server. 

 Format —Select the syslog message
 format to use: BSD (the default) or
 IETF . Traditionally,
 BSD format is over UDP and
 IETF format is over TCP or
 SSL/TLS. 

 Facility —Select a syslog standard
 value (default is LOG_USER ) to
 calculate the priority (PRI) field in your syslog server
 implementation. Select the value that maps to how you use
 the PRI field to manage your syslog messages. 

 ( Optional ) To customize the format of the syslog messages that
 the firewall sends, select the Custom Log Format 
 tab. For details on how to create custom formats for the various log
 types, refer to the Common Event Format Configuration
 Guide . 

 Click OK to save the server profile. 

 Configure syslog forwarding for Traffic, Threat, and WildFire Submission
 logs. 

 Configure the firewall to forward logs. For more information, see Step
 Create a
 Log Forwarding profile. 

 Select Objects Log Forwarding , click Add , and enter
 a Name to identify the profile. 

 For each log type and each severity level or WildFire
 verdict, select the Syslog server
 profile and click OK . 

 Assign the log forwarding profile to a security policy to trigger log
 generation and forwarding. For more information, See Step Assign the
 Log Forwarding profile to policy rules and network
 zones. 

 Select Policies Security and select a policy rule. 

 Select the Actions tab and select the
 Log Forwarding profile you
 created. 

 For Traffic logs, select one or both of the Log at
 Session Start and Log At Session
 End check boxes, and click
 OK . 

 For detailed information about configuring a log forwarding profile
 and assigning the profile to a policy rule, see Configure Log Forwarding . 

 Configure syslog forwarding for System, Config, HIP Match, and Correlation
 logs. 

 Select Device Log Settings . 

 For System and Correlation logs, click each Severity level, select the
 Syslog server profile, and click
 OK . 

 For Config, HIP Match, and Correlation logs, edit the section, select
 the Syslog server profile, and click
 OK . 

 ( Optional ) Configure the header format of syslog messages. 

 The log data includes the unique identifier of the firewall that generated
 the log. Choosing the header format provides more flexibility in filtering
 and reporting on the log data for some Security Information and Event
 Management (SIEM) servers. 

 This is a global setting and applies to all Syslog server profiles configured
 on the firewall. 

 Select Device Setup Management and edit the Logging and Reporting Settings. 

 Select the Log Export and Reporting tab and
 select the Syslog HOSTNAME Format: 

 FQDN (default)—Concatenates the
 hostname and domain name defined on the sending
 firewall. 

 hostname —Uses the hostname defined on
 the sending firewall. 

 ipv4-address —Uses the IPv4 address of
 the firewall interface used to send logs. By default, this
 is the MGT interface. 

 ipv6-address —Uses the IPv6 address of
 the firewall interface used to send logs. By default, this
 is the MGT interface. 

 none —Leaves the hostname field
 unconfigured on the firewall. There is no identifier for the
 firewall that sent the logs. 

 Click OK to save your changes. 

 Create a certificate to secure syslog communication over TLSv1.2. 

 Required only if the syslog server uses client authentication. The syslog
 server uses the certificate to verify that the firewall is authorized to
 communicate with the syslog server. 

 Ensure the following conditions are met: 

 The private key must be available on the sending firewall; the keys
 can’t reside on a Hardware Security Module (HSM). 

 The subject and the issuer for the certificate must not be
 identical. 

 The syslog server and the sending firewall must have certificates
 that the same trusted certificate authority (CA) signed.
 Alternatively, you can generate a self-signed certificate on the
 firewall, export the certificate from the firewall, and import it in
 to the syslog server. 

 The connection to a Syslog server over TLS is validated using the
 Online Certificate Status Protocol (OCSP) or using Certificate
 Revocation Lists (CRL) so long as each certificate in the trust
 chain specifies one or both of these extensions. However, you cannot
 bypass OCSP or CRL failures so you must ensure that the certificate
 chain is valid and that you can verify each certificate using OCSP
 or CRL. 

 Select Device Certificate Management Certificates , then Device Certificates ( PAN-OS 11.2 and
 earlier ) or
 Custom Certificates ( PAN-OS 12.1.0
 and later ) . Select
 Generate . 

 Enter a Name for the certificate. 

 In the Common Name field, enter the IP address
 of the firewall sending logs to the syslog server. 

 In Signed by , select the trusted CA or the
 self-signed CA that the syslog server and the sending firewall both
 trust. 

 The certificate can’t be a Certificate
 Authority nor an External
 Authority (certificate signing request [CSR]). 

 Click Generate . The firewall generates the
 certificate and key pair. 

 Click the certificate Name to edit it, select the
 Certificate for Secure Syslog check box, and
 click OK . 

 Commit your changes and review the logs on the syslog server. 

 Click Commit . 

 To review the logs, refer to the documentation of your syslog
 management software. You can also review the Syslog
 Field Descriptions . 

 ( Optional ) Configure the firewall to terminate the connection to the
 syslog server upon FQDN refresh. 

 When you configure a syslog server profile using a FQDN, the firewall
 maintains its connection to the syslog server by default in the event of an
 FQDN name change. 

 For example, you have replaced an existing syslog server with a new syslog
 server that uses a different FQDN name. If you want the firewall to connect
 to the new syslog server using a new FQDN name, you can configure the
 firewall to automatically terminate its connection to the old syslog server
 and establish a connection to the new syslog server using the new FQDN
 name. 

 Log in to the firewall
 CLI . 

 Configure the firewall to terminate the connection to the syslog server
 upon FQDN refresh. 

 admin> set syslogng fqdn-refresh yes 

 Configure Syslog Monitoring (SCM) 

 Configure syslog monitoring for Strata Cloud Manager. 

 Log in to Strata Cloud Manager . 

 Select Manage Configuration NGFW and Prisma Access Objects Log Forwarding Syslog Server Profile Configuration NGFW and Prisma Access Objects Log Forwarding Syslog Server Profile and select the Configuration Scope where you want to create the
 Syslog server profile. 

 You can select a folder or firewall from your Folders 
 or select Snippets to configure the Syslog server
 profile in a snippet. 

 Add Syslog . 

 Configure the Syslog server profile. 

 Enter a descriptive Name . 

 Add a syslog server. 

 Multiple syslog servers might be added to a single Syslog server
 profile. 

 Name —Unique name for the syslog
 server. 

 Syslog Server —IP address or fully
 qualified domain name (FQDN) of the syslog server. 

 If you configure an FQDN and use
 UDP transport, if the firewall
 can’t resolve the FQDN, the firewall uses the existing IP
 address resolution for the FQDN as the Syslog
 Server address. 

 Transport —Select
 TCP or UDP 
 as the protocol for communicating with the syslog
 server. 

 Port —The port number on which to send
 syslog messages (default is UDP on port 514); you must use
 the same port number on the firewall and the syslog
 server. 

 Format —Select the syslog message
 format to use: BSD (default) or
 IETF . Traditionally,
 BSD format is over UDP and
 IETF format is over TCP. 

 Facility —Select a syslog standard
 value (default is LOG_USER ) to
 calculate the priority (PRI) field in your syslog server
 implementation. Select the value that maps to how you use
 the PRI field to manage your syslog messages. 

 ( Optional ) Create a custom log/event
 format . 

 To customize the format of the syslog messages the firewall sends,
 select the Custom Log Format tab. 

 Save . 

 Configure syslog forwarding. 

 Select Manage Configuration Objects Log Forwarding Log Forwarding Profile Configuration NGFW and Prisma Access Objects Log Forwarding Log Forwarding Profile and select the Configuration Scope where you want to
 create the Log Forwarding profile. 

 You can select a folder or firewall from your
 Folders or select
 Snippets to configure the Log Forwarding
 profile in a snippet. 

 Add Log Forwarding Profile . 

 Enter a descriptive Name . 

 Add the profile match list for the Log
 Forwarding profile. 

 A match list profile specifies the log query filter, forwarding
 destinations, and automatic actions to take. Multiple profile match
 lists can be added to the same Log Forwarding profile to allow you
 to add different profile match lists for different log types in the
 same Log Forwarding profile. 

 Enter a descriptive Name . 

 Select the Log Type . 

 Only one log type can be added per profile match list. 

 ( Optional ) Configure the log query
 Filter . Default is
 All Logs . 

 Add the Syslog Profile you created in
 the previous step. 

 Save . 

 Repeat this step for all the log types that you want to
 forward to your syslog server. 

 Save . 

 Modify the log forwarding settings for the policy rule. 

 Security Policy —In the Actions, select
 Log Settings and select the Log
 Forwarding profile you created for External Log
 Forwarding . 

 Decryption —In the Log Settings, select the Log
 Forwarding profile you created for External Log
 Forwarding . 

 DoS Protection —Expand the Advanced Settings
 and select the Log Forwarding profile you created for Log
 Forwarding . 

 Authentication —In the Log Settings and select
 the Log Forwarding profile that you created for Log
 Forwarding . 

 Push Config to push your configuration changes. 

 Previous 

 Use Syslog for Monitoring 

 Next 

 Syslog Field Descriptions 

 On This Page 

 Activation & Onboarding 

 Strata Cloud Manager 

 Activate a License or Product 

 Cloud Identity Engine 

 Strata Logging Service 

 Device Associations 

 Hub 

 Identity and Access Management 

 Tenant Management 

 Next-Generation Firewalls 

 AIOps for NGFW 

 Cloud Management for NGFWs 

 Cloud NGFW for AWS 

 Cloud NGFW for Azure 

 CN-Series 

 Firewalls 

 PAN-OS 

 PAN-OS SD-WAN 

 Service Provider 

 VM-Series 

 SASE 

 Prisma Access 

 Strata Multitenant Cloud Manager 

 AI-Powered ADEM 

 Prisma Access Monitoring and Visibility 

 Prisma SD-WAN 

 ION Devices 

 Next-Generation CASB 

 Cloud-Delivered Security Services 

 Advanced WildFire 

 Advanced URL Filtering 

 Advanced Threat Prevention 

 Advanced DNS Security 

 Device Security 

 Enterprise DLP 

 SaaS Security 

 Network Security 

 Shared Policy for NGFWs and Prisma Access 

 Visibility & Monitoring 

 Dashboards 

 Incidents and Alerts 

 Reports 

 Autonomous DEM 

 Best Practices 

 Best Practices Library 

 Experts Corner 

 Solutions Docs from Product Experts 

 Network Security 

 PAN-OS 

 Next-Generation Firewall 

 Administration 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

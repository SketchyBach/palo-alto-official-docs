---
url: https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-admin/monitoring/use-syslog-for-monitoring/system-log-reference/medium-system-log-messages
fetched_at: 2026-08-13T17:09:38Z
source: palo-alto-main
---

# Medium System Log Messages Clear

Medium System Log Messages 

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

 Medium System Log Messages 

 Updated on 

 Aug 11, 2025 

 Focus 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 한국어 (Korean) 

 Filter

 Updated on 

 Aug 11, 2025 

 Focus 

 Home 

 PAN-OS 

 Monitoring 

 Use Syslog for Monitoring 

 Syslog Severity Reference 

 Medium System Log Messages 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 한국어 (Korean) 

 Medium System Log Messages 

 Table of Contents 

 Filter

 Previous 

 Low Severity System Log Messages 

 Next 

 High System Log Messages 

 Medium System Log Messages 

 E-Log 

 Log Tags: 

 auth 

 ddns 

 dhcp 

 dns-security 

 dynamic-updates 

 fips 

 general 

 hw 

 nat 

 ntpd 

 port 

 routing 

 satd 

 syslog 

 url-filtering 

 userid 

 wildfire 

 auth 

 Event ID Description 

 cas-message (profile id:<id>)<message> 

 auth-fail <type> with username "<name>" is invalid due
to special characters 

 auth-fail Allocated slot <id> for uid <uid> <id> 

 auth-fail Admin <name> failed to authenticate <num> times
- the unsuccessful authentication attempts threshold reached. 

 auth-fail Admin <name>'s account is being disabled
due to excessive failed authentication attempts. 

 auth-success Certificate validated for user '<name>'. <error> 

 auth-fail Certificate validation failed for user '<user>'. <error>
auth profile '<name>', vsys '<id>', reply message '<msg>'
From: <name>. 

 auth-fail failed authenticated for user '<name>'.
realm '<name>', EAP outer identity '<name>, inner identity
'<name>', auth profile '<name>', vsys '<id>', server profile
'<name>', server address '<addr>', admin role '<name>',
access domain '<name>', reply message '<msg>' From: <name>. 

 user-password-change-failed failed authenticated for user '<name>'.
realm '<name>', EAP outer identity '<name>, inner identity
'<name>', auth profile '<name>', vsys '<id>', server profile
'<name>', server address '<addr>', admin role '<name>',
access domain '<name>', reply message '<msg>' From: <name>. 

 auth-fail Kerberos SSO authentication failed for user '<name>'.
realm '<name>', EAP outer identity '<name>, inner identity
'<name>', auth profile '<name>', vsys '<id>', server profile '<name>',
server address '<addr>', admin role '<name>', access domain
'<name>', reply message '<msg>' From: <name>. 

 user-password-change-failed Kerberos SSO authentication failed for user '<name>'.
realm '<name>', EAP outer identity '<name>, inner identity
'<name>', auth profile '<name>', vsys '<id>', server profile '<name>',
server address '<addr>', admin role '<name>', access domain
'<name>', reply message '<msg>' From: <name>. 

 auth-fail SAML SSO authentication failed for user '<name>'.
realm '<name>', EAP outer identity '<name>, inner identity
'<name>', auth profile '<name>', vsys '<id>', server profile '<name>',
server address '<addr>', admin role '<name>', access domain
'<name>', reply message '<msg>' From: <name>. 

 user-password-change-failed SAML SSO authentication failed for user '<name>'.
realm '<name>', EAP outer identity '<name>, inner identity
'<name>', auth profile '<name>', vsys '<id>', server profile '<name>',
server address '<addr>', admin role '<name>', access domain
'<name>', reply message '<msg>' From: <name>. 

 auth-fail CAS SSO authentication failed for user '<name>'.
realm '<name>', EAP outer identity '<name>, inner identity
'<name>', auth profile '<name>', vsys '<id>', server profile '<name>',
server address '<addr>', admin role '<name>', access domain
'<name>', reply message '<msg>' From: <name>. 

 user-password-change-failed CAS SSO authentication failed for user '<name>'.
realm '<name>', EAP outer identity '<name>, inner identity
'<name>', auth profile '<name>', vsys '<id>', server profile '<name>',
server address '<addr>', admin role '<name>', access domain
'<name>', reply message '<msg>' From: <name>. 

 ddns 

 Event ID Description 

 ddns-unsupported Interface <name> DDNS config for host <host>
to <label> (<label>) is using a non-supported DDNS service
provider. Please convert to a supported service. 

 dhcp 

 Event ID Description 

 ip-already-in-use ip address is already in use 

 server-no-free-ip DHCP server runs out of ip pool 

 dns-security 

 Event ID Description 

 PAN_ELOG_EVENT_DNSSEC_DNS_CLOUD_QUERY_TIMEOUT DNS Security cloud query timeout. 

 dynamic-updates 

 Event ID Description 

 palo-alto-networks-message <message> 

 fips 

 Event ID Description 

 fips-entropy-rtciid RTC-IID error occurred - attempting recovery... 

 fips-entropy-rtciid RTC-IID - Reading record failure 

 general 

 Event ID Description 

 general CAS token sign cert "<name>" is invalid
with error msg "<msg>" 

 general PANDB: Authentication or Client Certificate failure. 

 general PANDB: Client Certificate has expired or is
not yet valid. 

 general PANDB: Device Client Certificate unavailable. 

 general PANDB: Mismatched Serial number in certificate
and payload. 

 general PANDB: Expired Client Certificate. 

 general PANDB: Revoked Client Certificate. 

 general PANDB: Reason - Unknown Issuer or Incomplete
or Incorrect Certificate chain. 

 general MLAV: Client Certificate has expired or is
not yet valid. 

 general MLAV: Device Client Certificate unavailable. 

 general MLAV: Mismatched Serial number in certificate and
payload. 

 general MLAV: Expired Client Certificate. 

 general MLAV: Revoked Client Certificate. 

 general MLAV: Reason - Unknown Issuer or Incomplete or
Incorrect Certificate chain. 

 general WFRTSIG: Authentication or Client Certificate failure. 

 general WFRTSIG: Client Certificate has expired or
is not yet valid. 

 general WFRTSIG: Device Client Certificate unavailable. 

 general WFRTSIG: Mismatched Serial number in certificate
and payload. 

 general WFRTSIG: Expired Client Certificate. 

 general WFRTSIG: Revoked Client Certificate. 

 general WFRTSIG: Reason - Unknown Issuer or Incomplete
or Incorrect Certificate chain. 

 general Server Cert: <name> is invalid, its name
does not match the server <server> 

 general Server Cert: <name> is invalid for server <name>:
<error> 

 general Slot s<num>: Application Pod '<name>
: <namespace>: <interface>' can't be served right now; All
<num> ports (<num> pods) in use, waiting for ports availability
(for <name>). 

 general Failed to connect to wildfire-realtime cloud, retry
after 30 seconds. 

 general CONFIG_UPDATE_INC : Incremental update to DP
failed please try to commit force the latest config 

 general Request made to <name> server returned with HTTP
response code : <code> 

 hw 

 Event ID Description 

 slot-up Slot <id> (PA-7000/5400-100G-NPC) ctd-mode is
AHO 

 nat 

 Event ID Description 

 fallback_report On vsys <id>, there are <num> NAT DIPP fallbacks
happeing in NAT rule <name>. 

 ntpd 

 Event ID Description 

 auth NTP sync to server <addr> failed, authentication
type autokey 

 auth NTP sync to server <addr> failed, authentication
type autokey 

 port 

 Event ID Description 

 invalid-module <name>: requires an SFP+ module. 

 invalid-module <buf>: requires an optical or copper SFP module. 

 routing 

 Event ID Description 

 routed-static-fqdn-changed Routed static fqdn mapping is changed 

 routed-static-fqdn-changed Routed static fqdn mapping is changed 

 routed-BGP-peer-mp-extension-negotiate BGP peer MP extension negotiation. MP-EXTENSION
negotiation to peer name: <name>, peer IP: <ip> successful" 

 routed-BGP-peer-enter-established BGP peer session enters established state.
peer name: <name>, peer IP: <ip>. 

 routed-BGP-refresh-sent ROUTE REFRESH message sent to a BGP peer. peer
name: <name>, peer IP: <ip>. 

 routed-BGP-ribout-recalc An RIB-Out is being recalculated as a result
of changed export policy. peer name: <name>, peer IP: <ip>. 

 routed-BGP-ribin-recalc An RIB-In is being recalculated as a result
of changed import policy. peer name: <name>, peer IP: <ip>. 

 satd 

 Event ID Description 

 satd-portal-gateway-duplicate GlobalProtect portal config duplicated gateway. 

 syslog 

 Event ID Description 

 syslog-conn-status <syslog-ng message> 

 url-filtering 

 Event ID Description 

 dynamic-url-connection-down Dynamic URL connection is unavailable please check
if service.brightcloud.com (<ip>) is reachable 

 connection-failure Failed to connect to Brightcloud update server: Cannot
fetch source IP address 

 url-download-failure The URL cloud list file was not found on the cloud. 

 cloud-election CLOUD ELECTION: cannot elect a cloud 

 url-cloud-connection-failure Failed to open connection with the cloud after "<num>
consecutive tries. 

 error-msg-from-cloud ERROR message from cloud. Invalid request. 

 error-msg-from-cloud ERROR message from cloud. Invalid request. 

 error-msg-from-cloud ERROR status from cloud 

 startup-failure PAN-DB engine startup failed. 

 update-version-failure Failed to update version <version>. 

 update-version-failure Failed to update version <version>. 

 update-version-failure Failed to update version <version>. 

 update-version-failure Failed to update version <version>. 

 update-version-failure Failed to update version <version>. 

 starts-from-empty-seed Failed to load the URL seed database, starting with
an empty database. 

 ha-sync-failure Unable to initiate file sync to peer: <error> 

 url-backup-seed-failure Failed to back up PAN-DB 

 engine-startup-failure May runs without URL filtering !!! 

 ha-sync-failure Failed to upload the new HA URL file to RAM, start
loading old URL file. 

 starts-from-empty-seed Failed to upload the old URL file to RAM,Starting
with an empty file. 

 engine-startup-failure Runs without URL filtering !!! 

 ha-sync-failure Failed to receive file completely from peer (<name>:<name>):
<error>. 

 userid 

 Event ID Description 

 connect-ldap-sever-failure ldap cfg <name> failed to connect to server <server>:
<error> 

 get-ldap-data-failure ldap cfg <name> failed to get info from
server <server> 

 connect-ldap-sever-failure ldap cfg <name> failed to connect to server <server>:
<error> 

 get-ldap-data-failure ldap cfg <name> failed to get info from
server <name> 

 wildfire 

 Event ID Description 

 wildfire-conn-success Successfully registered to <description> <name> 

 Slog 

 Queue '<name>' reached the
watermark limit at <num> 

 Removed Used AuthKey '<name>' 

 Removed Expired AuthKey '<name>' 

 Deleted AuthKey '<name>' 

 Created AuthKey '<name>' (Count:<num>, Life:< num>s, Type:'<type>',
Serial-Count:<num>) 

 Failed to SCP out Deployment file: '<file>' (rc: <num>) 

 Failed to SCP out Deployment metafile: '<file>' (rc: <num>) 

 Failed to SCP in Deployment metafile: '<file>' (rc: <num>) 

 Failed to SCP in Deployment file: '<file>' (rc: <num>) 

 Could not access threat vault 

 Failed to upload the sample to the cloud. 

 Registration to cloud failed. 

 Created new devicecert '<name>' 

 Created new cert '<name>' 

 mail send: <status> 

 Tor status is checked and changed to: <name>. 

 Failed to send test email using email profile <name>. 

 Previous 

 Low Severity System Log Messages 

 Next 

 High System Log Messages 

 On This Page 

 11.1 

 Network Security 

 11.1 & Later 

 PAN-OS 

 Next-Generation Firewall 

 Administration 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

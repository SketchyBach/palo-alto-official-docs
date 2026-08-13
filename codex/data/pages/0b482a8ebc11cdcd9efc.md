---
url: https://docs.paloaltonetworks.com/prisma/prisma-access/3-2/prisma-access-panorama-release-notes/prisma-access-about/prisma-access-known-issues
fetched_at: 2026-08-13T17:32:02Z
source: palo-alto-main
---

# Prisma Access Known Issues Clear

Prisma Access Known Issues 

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

 Prisma Access Known Issues 

 Updated on 

 May 29, 2026 

 Focus 

 Download PDF 

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

 Updated on 

 May 29, 2026 

 Focus 

 Home 

 Prisma 

 Prisma Access 

 Prisma Access Release Notes (Panorama Managed) 

 Prisma Access (Panorama Managed) Release Information 

 Prisma Access Known Issues 

 Download PDF 

 Prisma Access Known Issues 

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

 Previous 

 Upgrade the Cloud Services Plugin 

 Next 

 Prisma Access Addressed Issues 

 Prisma Access Known Issues 

 Prisma Access has the following known issues. 

 Issue ID 

 Description 

 CYR-32517 

 If you deploy a mobile users location that already has a location
 deployed in the same compute location, you might receive only one
 public IP address for the newly-deployed location instead of
 two. 

 Workaround : Enable the IP Allow Listing feature to receive
 more than one IP address. 

 CYR-32511 You can configure IPv6 DNS addresses even if IPv6 is
 disabled. 

 CYR-32186 
 This issue is now resolved in plugin
 version 3.2.0-h65 and 3.2.1-58. See Prisma Access 3.2.0-h65 Addressed Issues and Prisma Access 3.2.1-h58 Addressed Issues . 

 You receive a "Permission Denied" error when attempting to delete a
 remote network. 

 Workaround : Close the error window then retry the remote
 network deletion, or use the following CLI commands to delete the
 remote network: 

 delete plugins cloud_services remote-networks
 onboarding 
 <branch-name> 

 commit 

 push 

 CYR-32006 

 When using Dynamic DNS (DDNS) registration using the Cloud Services
 plugin 3.2, nsupdate commands are not working as expected, which
 causes issues with DDNS update queries. 

 CYR-30586 
 This issue is now resolved in plugin
 version 3.2.1-h36. See Prisma Access 3.2.1-h36 Addressed Issues . 

 When you select Use X-Authenticated-User (XAU) header on
 incoming HTTP/HTTPS requests for Identity under Panorama Cloud Services Configuration Mobile Users—Explicit Proxy Settings Authentication Settings and then click OK after you have activated the
 XAU functionality, the XAU checkbox will become deselected. 

 Workaround : Select the box again under Authentication Settings
 to enable XAU. 

 CYR-30455 
 This issue is now resolved in plugin
 version 3.2.1-h36. See Prisma Access 3.2.1-h36 Addressed Issues . 

 When you configure multiple portals in a multitenant deployment, the
 portal options Generate cookie for authentication
 override and Accept cookie for
 authentication override must be selected, but the
 user interface lets you deselect them. 

 Workaround: Do not deselect the Generate cookie for
 authentication override and Accept cookie
 for authentication override options in the portal
 configuration. 

 CYR-30414 

 If you have enabled multiple portals in a multitenant deployment that
 has only one tenant, and you then disable the multiple portal
 functionality on that single tenant, you are able to see both
 portals on the UI. 

 Workaround : Open a CLI session on the Panorama that manages
 Prisma Access and enter the following commands, then perform a local
 commit on the Panorama: 

 set plugins cloud_services multi-tenant tenants
 <tenant_name> mobile-users multi-portal-multi-auth
 no 

 request plugins cloud_services gpcs multi-tenant tenant-name
 <tenant_name> multi_portal_on_off 

 CYR-30332 
 This issue is now resolved in plugin
 version 3.2.1-h30. See Prisma Access 3.2.1-h30 Addressed Issues . 

 If you have configured inbound access, the Peer IP
 Address does not display in the Panorama Cloud Services Configuration Inbound Access Remote Networks tab. 

 Workaround : In Panorama, Refresh the UI (the two circular
 arrows at the top right of the screen). 

 CYR-30149 
 This issue is now resolved in 4.0.0-h90. See 4.0.0-h90 Addressed
 Issues . 

 When you use a Panorama with a version of 11.0.0 to manage Prisma
 Access and you attempt to delete an Explicit Proxy configuration by
 going to Panorama Cloud Services Configuration Mobile Users— Explicit Proxy , selecting Remove , and clicking Yes to
 confirm, the Explicit Proxy configuration is not removed. 

 Workaround : Click No instead of Yes when
 confirming the deletion operation, or open a CLI session with the
 Panorama that manages Prisma Access and enter the delete
 plugins cloud_services mobile-users-explicit-proxy
 onboarding command. 

 CYR-29700 

 If you configure multiple GlobalProtect portals in a multitenant
 Prisma Access Panorama Managed multitenant deployment, committing
 changes on a per-username basis fails with a
 global-protect-portal-8443 should have the value
 "GlobalProtect_Portal_8443 but it is [None]" 
 error. 

 Workaround : If you have enabled multiple GlobalProtect portals
 and have a Prisma Access multi-tenant deployment, perform Commit
 All commit operations instead of committing on a per-user
 basis. 

 CYR-29585 
 Predefined EDLs are not downloaded on newly
onboarded Explicit Proxy regions. This condition occurs only if
you configure and onboard new Explicit Proxy regions using XML APIs
or CLI. 

 Workaround : Select Panorama Cloud Services Configuration Mobile Users—Explicit Proxy ,
click the gear to edit the Settings , and
click OK to apply the predefined EDLs to
the Explicit Proxy configuration. 

 CYR-28795 
 This issue is now resolved in plugin
 version 3.2.1-h36. See Prisma Access 3.2.1-h36 Addressed Issues . 

 If you attempt to enable multiple portals in a multitenant deployment
 that has only one tenant, you will receive a commit validation
 error. 

 Workaround : Open a CLI session on the Panorama that manages
 Prisma Access and enter the following commands, then perform a local
 commit on the Panorama: 

 set plugins cloud_services multi-tenant tenants
 <tenant_name> mobile-users multi-portal-multi-auth
 yes 

 request plugins cloud_services gpcs multi-tenant tenant-name
 <tenant_name> multi_portal_on_off 

 CYR-28661 
 After upgrading to the 3.2.1 Cloud Services
plugin, the options to configure Mobile Users - GlobalProtect IP
Address Pool at a per-location group do not display; however the choices
to configure an IP Address pool at a Worldwide or Regional level
display. 

 Workaround : Log out and then log back in after
upgrading the plugin for the per-location group IP pool options
to display. 

 CYR-28574 
 When using a Panorama running 11.0 to manage
Prisma Access, logins to Panorama Managed Prisma Access take a long
period of time (two minutes or more). 

 CYR-28573 
 When using a Panorama with a version of
11.0 to manage Prisma Access, you cannot use the Edit
Selections option during Commit and Push operations
or all windows will close. 

 Workaround : Do not use
change the Edit Selections options, or uninstall
the Cloud Services plugin. 

 CYR-28288 
 When performing commits or upgrades, a Prisma
Access deployment requires internet connectivity; without internet
connectivity, certificate validation will fail and commits are not
possible. 

 CYR-27668 
 In Prisma Access Explicit Proxy deployments,
different device connections may show identical entries in the Authentication
logs if the source IP address and browser version are the same for
both device connections. 

 CYR-27513 
 When upgrading your Panorama from an earlier
10.1 version to 10.1.7 and you use HIP profiles, local commits fail
with 'hip-profiles unexpected here' and 'rules is invalid' errors.
This condition is the effect of HIP-profile objects in security
policies and authentication policies being replaced with source-hip
and destination-hip objects. 

 Workaround : Start a CLI
session with the Panorama that manages Prisma Access and enter the
following commands: 

 load config from running-config.xml 

 commit
force 

 CYR-27347 
 When onboarding an Inbound Access Remote
Network, commits fail with a Commit-all Error: Saas-Agent Exception: failed to get SPN error.
This is an intermittent issue. 

 Workaround : Delete the
Inbound Access Remote Network from Panorama and perform a Commit
and Push operation; then, re-add the Inbound Access Remote Network
and perform another commit and push operation. 

 CYR-27084 
 If you use a Panorama version of 10.2.3
or later to manage Prisma Access, certificates can be lost after
a plugin upgrade, which causes an OTP request to be issued. 

 CYR-26417 
 If you use a Panorama running PAN-OS version
10.1.7 to manage Prisma Access, attempting to access the online
help in the Cloud Services plugin area ( Panorama Cloud Services Configuration or Panorama Cloud Services Status ), the online help in
the 3.2 Cloud Services plugin does not display. 

 Workaround :
Upgrade your Panorama to 10.1.7-h1 to view the online help. 

 CYR-26226 
 If you have remote network locations that
were remapped to new compute locations as part of the 3.2 infrastructure
upgrade, you receive a null message
when attempting to allocate the bandwidth for the remapped compute
locations. 

 Workaround : Open a CLI session with the
Panorama that manages Prisma Access and enter the debug
plugins cloud_services prisma-access refresh-infra-files command
to refresh the location-to-compute location mapping. 

 CYR-26007 
 Advanced Threat Protection (ATP) is not
supported when using TLS 1.3. 

 CYR-25920 
 This issue is now resolved
in plugin version 3.2.1. See Prisma Access 3.2.1 Addressed Issues . 

 Authentication override values in portal
and gateway configurations are not accepted when the following conditions
apply: 

 You have a Mobile Users—GlobalProtect deployment. 

 You use the Cloud Identity Engine for SAML authentication. 

 You use an Authentication Profile with a Type of Cloud
Authentication Service . 

 If your deployment
meets these conditions, authentication cookie overrides are not applied
(the Generate cookie for authentication override and Accept
cookie for authentication override values in portal
and gateway configurations are not accepted). 

 CYR-25766 
 While browsing through various tabs under
in the Panorama UI under Panorama Cloud Services , a blank pop-up
window might display with a title of Error . 

 Workaround: This
issue has not been found to create any functional impact. Closing
the window and refreshing the UI should solve the display issue. 

 CYR-25759 
 While browsing through various tabs under
in the Panorama UI under Panorama Cloud Services , a blank pop-up
window might display with a title of Operation Failed . 

 Workaround: This
issue has not been found to create any functional impact. Closing
the window and refreshing the UI should solve the display issue. 

 CYR-25627 
 This issue is now resolved
in plugin version 3.2.0. See Prisma Access 3.2.0 Addressed Issues . 

 If you have QoS enabled in a Remote Network
compute location, and you reduce the bandwidth for a compute location
enough that Prisma Access removes an IPSec termination node from
that compute location, QoS is disabled for that compute location. 

 Workaround :
After the IPSec termination node has been deprovisioned, re-enable
QoS for that compute location. 

 CYR-25505 
 When using a Panorama running 10.2 to manage
Panorama Managed Prisma Access, Inactivity-Logout values can only
be configured using minutes. 

 CYR-25503 
 If you are managing an on-premise or VM
firewall running 10.0 with a Panorama running 10.1 or 10.2, an Inactivity-Logout configured
on Panorama is configured as disconnect-on-idle on
the managed firewall. 

 CYR-25128 
 Local commits to Panorama are not able to
be performed during a Prisma Access maintenance window. 

 CYR-24838 
 If a GlobalProtect mobile user has a dollar
sign ($) in the user name, they cannot log out of Prisma Access. 

 Workaround :
Do not use dollar signs in GlobalProtect user names. 

 CYR-24818 
 Onboarding and autoscaling of Mobile User
locations is successful even though the Mobile User IP address pool
is insufficient to onboard the locations or allow autoscaling events. 

 CYR-24654 
 If you are using a Panorama with a version
of 10.2 or later to manage Prisma Access and you specify Prisma
Access to append the ending token to URLs in URL filtering configuration
under Panorama Cloud
Services Configuration Service
Setup Settings Advanced ,
this setting might differ from the Append Ending Token setting in
the Device Setup URL Filtering area. 

 Workaround :
Make sure that the two values are the same in Panorama. 

 CYR-25402 
 This issue is now resolved
in plugin version 3.2.0. See Prisma Access 3.2.0 Addressed Issues . 

 When using a 10.2.2 Panorama to manage a
Panorama Managed Prisma Access 3.1.2 deployment, when attempting
to download Preview Rules in the Mobile_User_Device_Group ( Policies Preview Rules PDF/CSV ), a 500 Internal Server Error is
received. 

 CYR-24538 
 When using the South Africa West, France
North, Ireland, Bahrain, or South Korea Explicit Proxy locations,
mobile users have difficulty connecting to some websites. 

 Workaround :
Deactivate these locations and use any of the Explicit Proxy supported locations . 

 CYR-24323 
 After an upgrade from the 2.2 Preferred
Cloud Services plugin to 3.x, the Troubleshooting Commands ( Panorama Cloud Services Configuration Service Setup Troubleshooting Commands ) failed
to display the Logging status, Routing information, EDL info, EDL
status, EDL refresh, and Search EDL fields. 

 CYR-24033 
 This issue is now resolved
in plugin version 3.2.0. See Prisma Access 3.2.0 Addressed Issues . 

 When onboarding a remote network and selecting
options such as Summarize Mobile User Routes before advertising , Enable BGP , Don't
Advertise Prisma Access Routes , or Advertise Default Route ,
an Object already exists error is displayed. 

 Workaround :
Cancel the current onboarding attempt and retry the operation. This
error is transient and subsequent retries should not experience
this issue. 

 CYR-24000 
 Traffic that matches the intrazone-default
and interzone-default rules do not display in the logs. 

 Workaround :
This traffic does not display in the logs by default. To have them
display, create rules for the intrazone and interzone traffic. 

 CYR-23829 
 This issue is now resolved
in plugin version 3.2.0. See Prisma Access 3.2.0 Addressed Issues . 

 If you have enabled cloud provider redundancy
for service connections, the Redundancy Assessment area in the Network
Details tab ( Panorama Cloud Services Status Network Details Service Connection ) shows (link
to published locations). 

 CYR-23761 
 When, in an Explicit Proxy deployment that
does not have Remote Networks onboarded, you select Forward
Remote Network traffic to Explicit Proxy in the Advanced tab,
the first three octets of the IP addresses display as None (for
example, None.254 instead of 172.25.255.254 ). 

 Workaround :
Onboard a remote network and Commit and Push your
changes, making sure that both Explicit Proxy and Remote
Networks are selected in the Push Scope. 

 CYR-23628 
 This issue is now resolved
in plugin version 3.2.0. See Prisma Access 3.2.0 Addressed Issues . 

 If you have QoS profiles with a Class
Bandwidth Type of Mbps , validation
fails and you receive the following error: 

 For QoS profile profile-name , summation of its class egress-guaranteed is Mbps-value , which is larger than its egress-max Mbps-value . 

 This
error displays if all of the following conditions are true: 

 In
the Profile area of the QoS profile, the Egress
Guaranteed is set to 0 . 

 In the Classes area of the QoS profile,
the summation of all values in the Egress Guaranteed field exceeds
the Egress Max value entered in the Profile area. 

 If
you have an Egress Guaranteed value of 0
in the Profile area, the summation of the Egress Guaranteed values
in the Classes field cannot exceed the Egress
Max value in the Profile area. 

 This
restriction applies to all QoS profiles in the template stack, even
if they are not being used. 

 Workaround : Delete the
profile, or modify any QoS Profiles so that the summation of the
Egress Guaranteed values in the Classes field does not exceed the Egress
Max value in the Profile area. 

 CYR-27545 
 In Prisma Access 3.2.1, mobile user IP Address
pools and you specify IP addresses at a location group level, the
IP addresses in the pool do not get released after the mobile user
disconnects from GlobalProtect. 

 Workaround : Remove
the IP address pool at the location group level and use Worldwide
or Regional pool addresses only, or reach out to your Palo Alto Networks
account representative or partner, who will contact the SRE team
to release the IP pools. 

 CYR-23538 
 If you onboard service connections using
the Cloud Services plugin 3.0 in multitenant mode, you cannot view
the service connections in the drop-down list if you perform the
following actions: 

 Onboard service connections when
running the 3.0 plugin in Panorama. 

 Commit and Push your changes. 

 Upgrade the Cloud Services plugin to 3.1. 

 Commit your changes. 

 Load the configuration from Step 1. 

 Workaround :
Do not load a configuration from a previous plugin version after
upgrading to a newer plugin version. The configuration load also
causes the previous plugin version to be loaded, which is an unsupported
configuration. 

 CYR-23526 
 This issue is now resolved
in plugin version 3.2.0-h24. See Prisma Access 3.2.0-h24 Addressed Issues . 

 When changing the Local IP Address in the
BGP tab for a Remote Network connection that uses BGP, the following
issues can be seen: 

 An Operation Failed window with
an Object already exists message might
display. 

 The Peer IP Address might display as Loading... in
the Remote Networks Onboarding section in the Panorama UI. 

 Workaround :
Refresh the Panorama UI. If a refresh does not fix the issue, change
the Local IP Address to a placeholder value, click OK ,
and then re-enter the correct Local IP Address. 

 CYR-23496 
 When a new Explicit Proxy instance is created,
the threat logs may not send device group information. This behavior
can occur in a new deployment or can change in an existing deployment
after a maintenance activity or infrastructure upgrade. 

 Workaround :
Select All instead of a specific Device Group when viewing logs. 

 CYR-23448 
 After successfully completing a partial
commit, the Commit Status messages includes the message Changes to all template configuration . 

 Workaround :
Ignore the message regarding all templates being changed. The partial
commit was performed only for the template or Commit Scope you specified. 

 CYR-23367 
 This issue is now resolved
in plugin version 3.2.0. See Prisma Access 3.2.0 Addressed Issues . 

 After migrating from a remote network deployment
that allocates bandwidth by location to one that allocates bandwidth
by compute location, QoS statistics are not displayed for inbound
access sites. 

 CYR-23238 
 If you use the remote network aggregate
bandwidth model and you enable QoS for a remote network ( Panorama Cloud Services Configuration Remote Networks Settings QoS )
that has ECMP enabled, you must select Customize Per
Site and click OK or you will
receive an error on commit. 

 CYR-23058 
 When you log out mobile users from the Panorama Cloud Services Status Status Mobile
Users—GlobalProtect area using the Logout function, or
if you log out a user using CLI, the user is successfully logged
out, but the Current Users area might still
show the user as being logged in for up to five minutes after the
logout activity occurred. This behavior is the result of Prisma
Access refreshing the status of logged-in users every five minutes.
If you have configured a Connect Method of User-logon
(Always On) or Pre-logon (Always On) ,
and if the user reconnects during the five minute refresh interval,
the user might not be reflected as being logged out in the Current
Users area. 

 Workaround :
View the login and logout events from the GlobalProtect logs. 

 CYR-22879 
 In a multi-tenant environment, you cannot
enable the EDL Custom Category End Token Support feature until all
your tenants have had their infrastructure and dataplane upgraded
to meet the requirements for the 3.0 Cloud Services plugin. 

 Workaround :
Wait until all your tenants have had their infrastructure and dataplane
upgraded before enabling the EDL Custom Category End Token Support feature. 

 CYR-22827 
 When viewing the Push State Details after
a commit to a device group, you see a message similar to Interface tunnel.2 has no zone configuration ’. 

 Workaround :
This is a spurious message related to a backup tunnel configuration
and can be ignored. 

 CYR-22821 
 When using Traffic Steering, when a user
matches a URL in an EDL, pre-defined URL category, or Custom URL
Category, the first two sessions are not directed to the target
for internet-bound traffic. 

 CYR-22759 
 You cannot make any configuration changes
in the Advanced tab under Explicit Proxy Settings ( Panorama Cloud Services Configuration Explicit Proxy Settings Advanced ). 

 Workaround :
There is no workaround. This functionality will be supported in
a future Prisma Access release. 

 CYR-22629 
 When using the Egress IP Allow List feature
in Prisma Access, you might experience the following issues when
using the UI: 

 The Egress IP Allowlist section can
take up to 30 seconds to load. 

 When the Egress IP Allowlist area is populated, it can take
20 to 30 seconds for the new information to be displayed. 

 CYR-22525 
 If you install an Innovation release, configure
a feature that is only supported on an Innovation release, and then
migrate from an Innovation to a Preferred release, you receive a
commit validation error after making configuration changes in the
Cloud Services plugin. 

 Workaround : Delete the unsupported
feature by creating a CLI session with the Panorama that manages
Prisma Access in configuration mode and entering the delete plugins cloud_services <feature-name> command,
where <feature-name> is the name of the feature that
is unsupported in the Preferred release. 

 CYR-22201 
 When using the Enterprise DLP plugin with
Prisma Access, an uploaded file that matched a Block action on a
data filtering profile was not blocked from being uploaded, along
with an error DLP Skipped: missing boundary m in
the Data Filtering logs. 

 CYR-22142 
 When configuring QoS for remote networks ( Panorama Cloud Services Configuration Remote Networks Settings QoS ),
you can select None as a QoS Profile . 

 Workaround :
Select a valid QoS profile to enable QoS. None is
an invalid selection. 

 CYR-22066 
 When viewing logs for an Explicit Proxy
deployment, duplicate log entries might be seen. This behavior does
not affect Prisma Access functionality. 

 CYR-22043 
 If you are configuring a Mobile User - GlobalProtect
deployment, if you do not enable the allow listing feature when
configuring or onboarding the mobile user deployment, the plugin
logs might display spurious messages that are similar to the following
messages: 

 2022-01-13 13:14:27.217 -0800 INFO: [access-domain-xpaths] Sending result back <result><status>pass</status><msg>cloud_services</msg><msg>cloud_services/access-domain</msg></result>2022-01-13 13:14:27.290 -0800 ERROR: [get_ip_allowlist_addresses] yes-allow-list node not found! Please config yes-allow-list under ip-allow-list node. 

 Workaround :
Ignore the plugin messages; these messages do not affect normal
Prisma Access operation. 

 CYR-21665 
 If, when in an Explicit Proxy deployment
that is forwarding remote network traffic to Explicit Proxy, if
you deselect the Forward Remote Network Traffic to Explicit Proxy check
box in the Advanced tab, the IP addresses that were allocated by
Explicit Proxy still display in the Advanced tab. 

 Workaround :
Refresh the Panorama UI to clear the IP addresses in the UI. 

 CYR-21629 
 This issue is now resolved in plugin version 3.2.1-h68. See Prisma Access 3.2.1-h68 Addressed Issues . 

 When Prisma Access creates a new compute
location and remaps an existing remote network location to that
new location, if you do not delete and re-add the existing compute
location to take advantage of the latest compute location-to-location
mapping, you cannot view bandwidth statistics for the remapped location. 

 Workaround :
Delete and re-add the remote network location that is associated
with the new compute location. The Service IP Address will change,
so you will have to change the IP address for the IPSec tunnel on
your CPE to the new Service IP Address, and you will need to commit
and push your changes twice (once after you delete the location,
and once after you re-add it). 

 CYR-21565 
 When configuring the IP addresses to use
to forward remote network traffic to Explicit Proxy in the Explicit
Proxy Advanced settings ( Panorama Cloud Services Configuration Mobile Users—Explicit Proxy Settings Advanced ), Remote Networks
does not display in the Push Scope for a Commit and Push operation. 

 Workaround :
Select Remote Networks as well as Explicit Proxy in
the Push Scope before performing a Commit and Push operation. Forwarding
traffic from remote networks to Explicit Proxy requires that you commit
and push changes to both Explicit Proxy and remote networks. 

 CYR-21138 
 This issue is now resolved
in plugin version 3.2.0. See Prisma Access 3.2.0 Addressed Issues . 

 Strata Logging Service failed to reconnect after
a disconnect if a management IP address used for logging had an
IP address assignment type of DHCP. 

 CYR-21092 
 When you run the API to retrieve Prisma
Access IP addresses with a serviceType of all ,
the API times out if your deployment has a large number of Remote
Networks. 

 Workaround : If you have a large number of
remote networks, specify a serviceType of remote_network instead
of all when running the API. 

 CYR-20895 
 If you have created a remote network deployment
that allocates bandwidth by compute location and then delete the
remote network license, any commit for changes to features that
are still licensed fail with an Failed plugin validation error. 

 Workaround :
Delete the unused remote network configuration by opening a CLI
session with admin-level privileges, entering configure to
enter configuration mode, and then entering delete plugins cloud_services remote-networks .
Then, retry the commit operation. 

 CYR-20731 
 If the dataplane is not compatible with
the plugin you are running, a generic message indicating that the
Panorama is undergoing maintenance displays in the Panorama
Alert and Plugin Alert fields
in Panorama Cloud Services Configuration Service Setup . 

 CYR-20729 
 When completing a mobile user setup in a
FedRAMP Moderate deployment and configuring the mobile user IP address
pool, you receive an Operation Failed message
with text that indicates that Prisma Access could not auto-generate
an authentication cookie certificate. In addition, when committing
and pushing your changes, you receive a validation error related
to a cookie decryption certificate. 

 Workaround : Create
a signed certificate and apply it to the Mobile Users—GlobalProtect
configuration by completing the following steps: 

 Select Panorama Certificate Management Certificates and Generate a
certificate with the following attributes, leaving the other attributes
with their default values: 

 Certificate
Name : Enter a name for the certificate. 

 Common Name : Enter the common name
of the FedRAMP certificate. 

 Signed By : Enter the CN used by the
authentication cookie. 

 Algorithm : Elliptic Curve DSA 

 Digest : SHA512 

 Select Panorama Cloud
Services Configuration Mobile
Users—GlobalProtect and Configure the Hostname . 

 Select General Client
Authentication Authentication Override Certificate and
select the certificate you generated. 

 CYR-20496 
 If you are using a Panorama of a version
or 10.0 or lower, and you configure an invalid destination port
value anywhere in Panorama (for example, in Objects Services ), a commit-all operation
fails with a vague error related to a module or device having a Non digit value. 

 Workaround :
Fix the invalid port configuration, then retry the commit-all operation.
Panoramas running 10.1 or later disallow you from configuring an invalid
destination port value. 

 CYR-19975 
 When you Enable IPv6, a window displays
asking you to enable Telemetry Data Collection. 

 Workaround :
Click Remind Me Later to dismiss the window. 

 CYR-19888 
 If you have applied QoS to your remote network
deployment but have not yet committed and pushed your changes, the
QoS statistics screens display blank information. 

 Workaround : Commit
and Push your QoS changes for the QoS statistics to
display. 

 CYR-19653 
 This issue is now resolved
in plugin version 3.2.0. See Prisma Access 3.2.0 Addressed Issues . 

 If, when using Explicit Proxy, when the
following conditions exist, mobile users might experience issues
with CORS requests and non-decrypted traffic: 

 - The
mobile user changes locations and Explicit Proxy detects an ingress
or client IP address change 

 The Authentication Cache Service (ACS) cookie has not reached
its Cookie Lifetime expiration 

 Workaround :
Clear your browser's cache to re-authenticate with the ACS. 

 CYR-19646 
 BGP addresses ending with .0 or .255 are
not allowed to be entered in the UI as peer BGP addresses for service
connections or remote networks, regardless of the subnet being used. 

 Workaround :
Use CLI commands to enter the .0 or .255 address by logging in to
the Panorama that manages Prisma Access and entering one of the
following commands: 

 set plugins cloud_services service-connection onboarding sc-name protocol
bgp peer-ip-address ip-address 

 set
plugins cloud_services remote-networks onboarding rn-name protocol
bgp peer-ip-address ip-address 

 Where sc-name or rn-name is the
name of the service connection or remote network connection. 

 CYR-19545 
 If you have IPv6 enabled in your Prisma
Access deployment, the Private IPv4 address of mobile users ( Panorama Cloud
Services Status Monitor Mobile Users—GlobalProtect Locations Users ) is displayed, but the
IPv6 Private IPv6 address of mobile users is not. 

 CYR-19503 
 IP precedence-based classification is not
working for Prisma Access, when using either IPv4 or IPv6 IP addresses. 

 CYR-19487 
 When you enable IPv6 for a single tenant
in a multi-tenant deployment, the UI page refreshes and displays
the Cloud Services Configuration page, where
you select the drop-down for all tenants. 

 CYR-19282 
 When configuring mobile users DNS settings
in the Network Services tab, you should not
enter Custom DNS Server IP addresses (either
IPv4 or IPv6) without also specifying a Domain List . 

 Workaround :
Specify a Domain List . 

 CYR-19198 
 If you add an IPv6 address pool to your
Mobile Users—GlobalProtect deployment, select the regions to Enable
IPv6 in the IPv6 Availability tab, and Commit
and Push your changes, the pools appear in the IPv6
Availability tab. If you then disable all regions, effectively disabling
IPv6, and then Commit and Push your changes,
the IPv6 address pools still display in the IPv6 Address Pool tab. 

 Workaround :
There is no workaround. If you later enable IPv6 for one or more
regions, you can use the existing IPv6 address pool. You can also
specify a different IPv6 address in the IP Pools and,
after you commit and push your changes, the new IPv6 Address pool
overwrites the existing addresses and displays in the IPv6 Availability
tab. 

 CYR-19099 
 When viewing or changing QoS settings for
Remote Networks in Panorama Cloud Services Configuration Remote Networks Settings QoS , a newly-added compute
location or location does not display. 

 In addition, a newly-onboarded
location does not display in the Site Allocation (Customize Per
Site) page. 

 Workaround : Refresh the Panorama that manages
Prisma Access. 

 CYR-19093 
 In a multi-tenant deployment, you receive
a Configuration committed successfully message
along with a Not all Commit-All jobs got triggered message. 

 Workaround :
Either upgrade your Panorama to a minimum version of 10.1.4, or
select Commit Commit
and Push , Edit Selections ,
and in the Prisma Access tab, make sure that
the Push Scope includes the changes you made
for the Prisma Access configuration. Depending on the changes you
made, select one or more of the Remote Networks , Mobile Users , Service
Setup , and Explicit Proxy choices. 

 CYR-19030 
 If you are sinkholing IPv6 traffic, the
policy rule hit counts for traffic that matches the IPv6 sinkhole
policy do not increment when entering the CLI command show
rule-hit-count vsys vsys-name vsys1 rule-base security rules all . 

 CYR-18757 
 In a multi-tenant deployment, admin users
that have more than one access domain cannot configure new remote
networks or service connections, and can only view what is already
deployed. 

 Workaround : Create the access domain first,
then select the access domain you created when you convert the single
tenant to a multi-tenant setup. 

 CYR-18234 
 When you select Integrate with
Prisma SD-WAN , the integration fails. 

 CYR-18157 
 When downloading a large file (including
but not limited to programs, browser extensions, or apps) using
Explicit Proxy, if the download takes longer than the cookie lifetime,
the download fails when the cookie expires. 

 CYR-18156 
 If, after signing in to Explicit Proxy,
you open a link that contains a file to download, the file downloads
successfully but the Explicit Proxy sign-in page continues to display. 

 Workaround :
Since the link contained a downloaded file, there is no page to
display and the current page does not refresh. Select another webpage
to navigate away from the sign-in page. 

 CYR-17848 
 If you are using a Panorama with a version
of PAN-OS 10.1 to manage Prisma Access, and you migrate a Remote
Network deployment from allocating bandwidth by location to allocating
bandwidth by compute location, the migration banner displays the location
names in an incorrect (large) font. 

 Workaround : No
workaround is required. There is no change to the migration functionality;
the only issue is with the font displayed during the migration. 

 CYR-17826 
 When using Troubleshooting Commands ( Panorama Cloud Services Configuration Service Setup Service Operations Troubleshooting
Commands ) with Panoramas that are in High
Availability mode, the commands cannot be run from the passive Panorama. 

 CYR-17077 
 If you delete an explicit proxy configuration
and then reconfigure it within 10 minutes of its deletion, Prisma
Access cannot properly process the new configuration and explicit
proxy functionality could be affected. 

 Workaround :
Wait at least 10 minutes after deleting an explicit proxy configuration
before reconfiguring it. 

 CYR-17024 
 When using Panorama 10. x to manage
Prisma Access, if you configure an Authentication Enforcement Profile
under Objects Authentication and
specify an Authentication Profile that resides in a Shared location,
you receive an error when committing the changes. 

 Workaround :
If you use a Panorama 10. x to manage Prisma Access, do not
use a shared Authentication Profile for any Authentication Enforcement
Profile; instead, use an Authentication Profile that is under one
of the Prisma Access Templates. 

 CYR-16965 
 When using explicit proxy, there could be
a delay when displaying user details under Current User
Count due to a log ingestion issue between explicit
proxy and Strata Logging Service. 

 CYR-16789 
 When performing a local commit or Commit
and Push operation, you receive the error Internal Server Error: Failed to aggregate bandwidth configuration . 

 Workaround :
Check the DNS configuration of the Panorama appliance that manages
Prisma Access, and check that Panorama is able to contact your network's
DNS servers, then retry the operation. 

 CYR-16735 
 If, during Explicit Proxy onboarding, you
onboard a large number of locations, the Explicit Proxy status might
display its status incorrectly (for example, a status of ERROR might
display when the onboarding was successful). 

 CYR-16674 
 If you change the Explicit Proxy URL in
Prisma Access but do not change the PAC file to reflect the change,
the change won't be applied. 

 Workaround : Upload a new
PAC file with the same changes as you made in the Explicit Proxy
URL. 

 CYR-16673 
 If you change the proxy FQDN, the changes
are not immediately reflected after the job status completes. 

 Workaround :
Workaround: Wait 10 to 15 minutes for the changes to be reflected
after the Job status shows as Completed on Panorama. 

 CYR-16642 
 There is a delay observed to populate the
Rule Usage column on the Policies page. 

 Workaround :
Refresh the page by clicking on the refresh button on the right
side. 

 In addition, the Preview Rules tab does not display
the Rule Hit counters. 

 Workaround : Click the Used link
on Rule Usage column to display the Rule
Hit count for the rule. 

 CYR-16615 
 The maximum length of a URL that can be
used with explicit proxy is 1280 characters. 

 CYR-16583 
 This issue is now resolved
in plugin version 3.2.0. See Prisma Access 3.2.0 Addressed Issues . 

 WildFire logs show explicit proxy logs as
having a source zone of Proxy. If you use a name of Proxy for Clean
Pipe instances or remote networks, you will not be able to differentiate
between explicit proxy logs and logs with the clean pipe or remote
network name of Proxy. 

 Workaround : If you use explicit
proxy, do not specify a name of Proxy for any Clean Pipe instances
or remote networks. 

 CYR-16580 
 The Panorama Cloud Services Status Monitor Mobile Users Explicit Proxy page incorrectly
shows the current number of users as 0. 

 CYR-16351 
 When using Explicit Proxy, initial DNS Queries
(first leg) and Initial HTTP connect messages (first logs) are not
seen in the traffic logs in Panorama. 

 CYR-16284 
 When you enter the show pbf extended-address
all command to retrieve the traffic steering cache, an
FQDN displays with an asterisk, such as *.example.com. 

 Workaround :
No workaround is required. The displayed FQDN is correlated to the
FQDN server that presented the certificate. 

 CYR-16130 
 When configuring a Mobile Users - GlobalProtect
deployment using SAML authentication, you receive a pangp.gpcloudservice.com is missing certificate error
when you commit your configuration changes. 

 Workaround :
Add the missing certificate in your SAML IdP configuration by selecting Device Mobile_User_Template Authentication Profile in Panorama
and adding the certificate. 

 CYR-16097 
 A webpage may contain links of resources
from the domains other than the domain from where the webpage is
served. Most modern browsers do not send any cookie along with the
requests to get the resources from those third-party domains for
security reasons. Since there is no cookie present to identify the
user for those third-party domains, the user name cannot be logged
in the traffic logs for those domains. 

 In addition, there
will be some connections that Prisma Access redirects for authenticating
a user. Logs for such connections will not have any username. 

 CYR-16073 
 When using traffic steering, if you specify
External Dynamic List that has an IP address and port, traffic is
not forwarded to the target. 

 Workaround : Remove the
port number from the IP address. 

 CYR-16015 
 When using explicit proxy, if you update
the cookie lifetime to a shorter lifetime than the previously configured
value, the new lifetime value does not apply to users who are already
logged in until the original longer life time expires. New users
logging into the service receive the new shorter cookie life time. 

 CYR-15926 
 Explicit proxy configuration changes are
not applied to the configuration after a commit. 

 Workaround :
If you are not seeing the changes after retrying the commit operation,
contact Palo Alto Networks support. 

 CYR-15267 
 When administrators log out a mobile user
who is logged in using SAML from the Prisma Access status page ( Panorama Cloud Services Status Status Current
Users ), a Single Logout (SLO) request
is not generated. As a result, the user is logged out of the gateway
but is not logged out of the IdP, and if the client SAML cookie
is still valid, the user can reconnect without having to input credentials. 

 CYR-15091 
 This issue is now resolved
in plugin version 3.2.1. See Prisma Access 3.2.1 Addressed Issues . 

 Extra IPSec termination nodes are allocated
to a compute location if you allocate bandwidth multiple times in
a very short time interval. 

 CYR-14997 
 When you allocate Bandwidth to a compute
location from the Onboarding section, that allocation is not reflected
immediately in the Bandwidth Allocation tab until you manually refresh
the page. 

 Workaround : Manually refresh the Panorama
that manages Prisma Access. 

 CYR-14937 
 When you upgrade the Cloud Services plugin
and then perform a commit operation, not all Prisma Access components
are selected in the Push Scope. 

 Workaround : Select Commit Commit and Push , Edit
Selections in the Push Scope ,
and make sure that all Prisma Access components ( Service
Setup , Remote Networks , Mobile
User , and Clean Pipe , depending
on your license) are selected before committing and pushing your changes. 

 CYR-14984 
 When you change the name of a target service
connection group for traffic steering, the updated target name does
not display in the Traffic Steering Rules area. 

 Workaround :
Refresh the Panorama browser. 

 CYR-14980 
 If you use IKEv2 with certificate-based
authentication, only SHA1 is supported in IKE crypto profiles (Phase
1). 

 Workaround : Use an IKEv2 (Phase 1) cryptographic
profile of SHA1 on your customer premises equipment and in Prisma
Access. 

 CYR-14816 
 If a service connection loses both its active
and backup connectivity, mobile users lose connectivity to users
and resources connected to Remote Networks and Service Connections. 

 CYR-14754 
 If you have two Panorama appliances configured
in high-availability mode, the passive Panorama will display an out of sync message during
a commit and push operation. 

 Workaround : Open a command-line
interface (CLI) session on both the passive and active Panorama
and enter the following commands: 

 username@hostname> debugmd5sum_cache clear 

 username@hostname> configure 

 username@hostname# commit
force 

 CYR-14728 
 Prisma Access bypasses Traffic Steering
for rules with a service type of HTTP or HTTPS if you use an application
override policy for TCP ports 80 and 443. 

 In addition, traffic
steering does not work for URLs from URL categories referenced in
the traffic forwarding rule if you have configured an application
override policy for TCP ports 80 or 443. 

 CYR-14727 
 Mobile user route summarization is not supported
in hot potato routing mode. 

 CYR-14693 
 When using hot potato routing, Mobile User
route summarization may add extra latency for traffic between mobile
users and headquarters or branch traffic. 

 CYR-14673 
 After you create a traffic steering rule
with an IP address, IP address group, EDL, or custom URL category
as a Shared object, make changes to any of those objects, and then
commit and push your changes, only the Shared object displays in
the Push Scope. Prisma Access device groups doesn't get displayed
in the push scope. 

 Workaround : Select Commit Commit and Push , Edit
Selections in the Push Scope ,
and make sure that you select all device groups ( Service
Setup , Remote Networks , Mobile
User , and Clean Pipe , depending
on your license) before committing and pushing your changes. 

 CYR-14613 
 When adding or deleting URLs to a custom
URL category, Prisma Access does not purge its cache, and the change
does not immediately take effect. 

 Workaround : Perform
one of the following actions: 

 Wait 24 hours for Prisma
Access to automatically clear the cache, or manually clear the Panorama’s
browser cache. 

 Remove the custom URL category, perform a commit and push
operation, then re-add the custom URL category and perform another
commit and push operation. 

 CYR-14603 
 To make sure that Prisma Access can distinguish
between users if the same username is shared between users who authenticate
locally and users who authenticate using LDAP, you should authenticate
LDAP users in the format of domain/username and authenticate local
users in the format of username (without the domain name). 

 CYR-14277 
 Do not create any custom URL categories
that start with GPCS- , gpcs- .
or custom_url_category_pbf . 

 CYR-14110 
 If Panorama access is disabled in an Admin
Role Profile, you can still see the contents of the plugin, but
the fields are read-only. 

 CYR-13823 
 When you upgrade the Cloud Services plugin
to 1.7, Prisma Access prepends an asterisk to URLs in custom URL
categories, if you use this category in a traffic steering forwarding
rule. If you use the same URL category policies for both traffic
steering and other security policy rules, these changes apply to
both the traffic steering rules and other security policy rules. 

 If
you have custom URL categories that are not used in traffic steering
forwarding rules, Prisma Access does not change the URLs in those
categories. 

 CYR-13822 
 Prisma Access prepends an asterisk to URLs
in custom URL categories, which doubles the number of URLs entered
in a custom URL category. Prisma Access supports a maximum of 300,000
URLs in URL category entries; if you use custom URLs for traffic steering
and are close to this limit, the doubling of URLs might cause your
deployment to exceed the limit of URLs. 

 CYR-13751 
 If you used policy-based forwarding rules
to forward internet-bound traffic to service connections in Prisma
Access 1.6, Prisma Access makes the following additions to URLs
in custom URL categories after you upgrade from 1.6 to 1.7: 

 A
URL of example.com has a URL of *.example.com added 

 A URL of www.example.com has a URL of *.www.example.com added 

 A URL of fqdn.example.com has a URL of *.fqdn.example.com added 

 A URL of www.fqdn.example.com has a URL of *.www.fqdn.example.com added 

 If
you already have added URLs with wildcards, Prisma Access might
add URLs that duplicate existing URLs after the upgrade. 

 CYR-13612 
 Prisma Access does not support FTP data
transfers in active mode. 

 CYR-13511 
 This issue is now resolved in plugin version 3.2. See Prisma Access 3.2.0 Addressed Issues . 

 When Prisma Access performs a dataplane
upgrade on a mobile user instance (an upgrade to a Prisma Access
gateway or portal), any failed commits on the instance that were
performed before the upgrade will not be applied to the upgraded
instance. 

 CYR-13317 
 During a Prisma Access dataplane upgrade,
BGP statistics may not be available for 30 minutes in the Network
Details page. This unavailability has no impact on dataplane traffic. 

 CYR-13179 
 If you use Microsoft Edge or Firefox when
using traffic steering, the browser does not forward traffic on
its first attempt. 

 Workaround : Refresh the browser,
then retry the operation. 

 CYR-12912 
 If, in a traffic steering deployment with
multiple traffic forwarding rules, two URLs in two separate rules
resolve to the same IP address, Prisma Access sends traffic to the first
rule in the list and will not use the second traffic rule. Traffic
steering evaluates multiple traffic forwarding rules in order from
top to bottom. 

 CYR-12700 
 For a Prisma Access deployment with two
Panoramas configured in high availability, you are able to request
an upgrade to the GlobalProtect software version on the passive
Panorama. Software upgrade requests are not applied if you request
them on the passive Panorama. 

 Workaround : Do not request
software upgrades on the passive Panorama; only request upgrades
using the active Panorama. 

 CYR-12509 
 When using traffic steering, Palo Alto Networks
does not recommend using multiple service connections (whether dedicated
or non-dedicated) in a target service connection group that is referenced
in a traffic steering rule. 

 CYR-12166 
 Prisma Access does not support a rule type
of Intrazone if the source and destination zones are both Trust. 

 CYR-11897 
 When entering CLI to retrieve Prisma Access
job status, an invalid token message
is received. 

 CYR-11496 
 If you enable ECMP on a remote network,
the values shown in the Statistics tab under Panorama Cloud Services Status Monitor Remote Networks for Ingress
Peak Bandwidth (Mbps) are correct; however, if you click
the hyperlink for this value, the pop-up window that displays might
show an incorrect value. 

 CYR-11414 
 When creating a new mobile user deployment
in multi-tenant mode, you receive an error that the Portal Hostname
is not available when you assign it during mobile user onboarding. 

 Workaround: Before
you begin your mobile user configuration, add an Infrastructure
Subnet, commit all your changes to Panorama, and push the configuration
changes to Prisma Access. 

 CYR-11201 
 Some files are being skipped for DLP scanning
when using OneDrive to upload multiple files. 

 CYR-11087 
 When using DLP on Prisma Access, you can
upload up to 25 files at a time. 

 CYR-11019 
 When attaching a parent Device Group to
a new remote network tenant in multi-tenant mode, the administrator
is unable to attach device groups and templates. 

 Workaround: Log
out, then log back in to Panorama. 

 CYR-10909 
 If you use Box to upload multiple files,
and one or more of the files are larger than 5 MB, the upload of
all files will not complete. To continue, find the files in Box
that are larger than 5 MB and click X to
stop the download of those files. 

 CYR-10445 
 DLP on Prisma Access is not supported in
a Prisma Access multi-tenant deployment. 

 CYR-10053 
 If you change the master key in Panorama
(in Device Master
Key and Diagnostics ), the master key for
Cloud Services is not synchronized with this master key. 

 Workaround: Select Panorama Cloud Services Configuration Service Setup Service Operations Edit Master
Key and manually change the master key
to be the same as the Panorama master key. 

 CYR-10044 
 When using Slack to upload multiple files,
the Slack client treats the multiple file upload as a single request.
If one of the files is not successfully uploaded, Slack retries the
upload of all files a maximum of three times. If, after three retries,
Slack cannot upload one or more of the files, the Slack client displays
an error in the UI and doesn't upload any of the files. 

 CYR-10043 
 When you upload a file using Slack, and
the file is blocked, Slack detects the block operation as an upload
failure and retries the file upload, which results in the same file being
uploaded and blocked twice. 

 Workaround: This is normal
Slack file upload behavior. Be aware that a single file that is
uploaded using Slack might appear twice in the data filtering logs
as being blocked. 

 CYR-9613 
 When you delete a data filtering profile
from a Prisma Access device group that is not shared, the profile
name still appears when you add or configure a Security Profile Group,
in the Data Filtering Profile area. 

 CYR-9455 
 In a GlobalProtect deployment where the
portal has multiple agent configs, when a GlobalProtect client logs
in using the app, the portal looks for a matching agent config for the
client by checking its OS type along with the config selection criteria.
The agent configs are checked from top to bottom. If the OS type
matches, but the config selection criteria does not, GlobalProtect
marks the agent config as non-matching and moves to the next agent
config to check for a match; however it no longer checks the OS
type in these agent configs, and only looks for a match of the config
selection criteria. This condition can cause the client to receive
an agent config that has matching config selection criteria, but
a non-matching OS type. 

 CYR-9348 
 When configuring HIP redistribution, you
cannot retrieve HIP information and set policies for the following
use cases: 

 A user connected to a Prisma Access location
(gateway) who attempts to access an internal resource. 

 A user protected by a remote network who attempts to access
a resource from another remote network. 

 CYR-9213 
 When using DLP on Prisma Access, when you
upload a .docx file using SharePoint that was exported from Google
Docs, the upload fails. 

 CYR-9183 
 When setting up the GlobalProtect gateway
connection settings ( Network GlobalProtect Gateways Agent Connection Settings ) and
specifying a Netmask to Restrict Authentication Cookie Usage ,
the commit fails if only a Source IPv4 Netmask is
specified. 

 Workaround: Specify a Source
IPv6 Netmask of 0 , which disables
the option for the specified IP address type. 

 CYR-9061 
 If using Slack, Box, or Gmail to upload
a file using DLP on Prisma Access, the response page is not displayed
to the client if the upload is blocked. 

 CYR-9003 
 Reverse DNS queries do not work in Prisma
Access. 

 Workaround: Because type A and AAAA queries
for internal domains work, you can specify *.in-addr.arpa in
a query so that Prisma Access sends all reverse DNS queries to internal
DNS servers. 

 CYR-8244 
 When performing a Commit and
Push operation for the Clean Pipe service, you receive
an error that the Clean Pipe service had insufficient license resources,
even though you have sufficient licensed bandwidth. 

 Workaround: Select Panorama Licenses ,
then select Retrieve license keys from license server to
retrieve the Clean Pipe licenses again. 

 CYR-8017 
 If you add an existing template under one
of the template stacks of Prisma Access (for example, Service_Conn_Template_Stack , Mobile_User_Template_Stack ,
or Remote_Network_Template_Stack ), you cannot
use objects of the added template in other Prisma Access templates
that are part of the same template stack. 

 Previously, you
could view and use objects from existing templates in Prisma Access
templates if the templates were a part of a Prisma Access-specific
template stack, which is not standard Panorama behavior. 

 CYR-7907 
 In multi-tenant mode, Prisma Access automatically
creates a set of templates, template stacks, and device groups for
each tenant you create for remote networks, mobile users, and the
Clean Pipe service. Prisma Access creates tenant-specific sets for all
products, even if you are licensed for only one Prisma Access type. 

 When
you delete a tenant, Prisma Access deletes the template and device
group set for which you are licensed, but does not delete the unlicensed
set. For example, if you have a remote network deployment and delete
a tenant, Prisma Access does not delete the set it created for the
mobile users and Clean Pipe. 

 Workaround: Manually
delete the unused, unlicensed set of templates, template stacks,
and device groups after you delete a tenant. 

 CYR-7900 
 The Traffic Forwarding feature ( Panorama Cloud Services Configuration Service Setup Settings Traffic Forwarding )
is not supported with multi-tenant deployments. 

 CYR-7702 
 When you log out a Prisma Access mobile
user from the Current Users window, the user
still displays in the window after the logout operation. 

 Workaround: Close
and then reopen the Current Users window
to show the correct user status. 

 CYR-7440 
 If you have two Panoramas set up in an active-primary
and passive-secondary setup for Prisma Access, you cannot log out
mobile users from the passive-secondary Panorama. 

 CYR-7332 
 When you try to configure an Infrastructure
Subnet ( Panorama Cloud
Services Configuration Service Setup Settings ) in multi-tenant mode,
you can receive an Operation Failed message. 

 Workaround: Refresh
the Panorama UI to have Prisma Access correctly apply the infrastructure
subnet to the tenant's configuration. 

 CYR-7128 
 When you perform a Commit All operation
for mobile users, Prisma Access should display the commit status
for portals and gateways separately; however, Prisma Access is displaying
failures for portals under gateway status, and is displaying commit
failures for gateways under portal status. 

 Workaround: Enter
the debug plugins cloud_services prisma-access get-job-result
jobid commit-job-id-number command,
where commit-job-id-number is the ID of the commit
operation that failed, to check and verify the commit operation
for portals and gateways. 

 CYR-6384 
 Pre-defined IKE Crypto, IPSec Crypto, and
IKE Gateways templates do not display. 

 Workaround: Select Panorama Cloud Services Configuration Service Setup (for
service connections) or Panorama Cloud Services Configuration Remote Networks (for remote
network connections), click the gear icon in the Settings area
to open the Settings , then click OK . 

 CYR-6369 
 When in multi-tenant mode, if you create
a custom admin user with an Admin Role Profile that has Read Only
access to the Panorama tab and has Plugin access disabled, that
user can view, configure, and commit changes for subtenants. 

 Workaround: Disable
access to the Panorama tab in the Admin Role Profile. 

 CYR-6108 
 When you configure Clientless VPN with Prisma
Access, the default security rule configuration uses the application-default
service, which blocks clientless-vpn traffic. 

 Workaround: Change
the default security rule to any service or service-http and service-https. 

 CYR-6107 
 When configuring multi-tenant, if you create
any device groups that are children or grandchildren of other device
groups you create under the Shared parent device group, select only
the device group at the lowest hierarchical level (child or grandchild)
when you associate the device group to an access domain; do not
select the parent. 

 CYR-6080 
 You cannot reset the rule hit count for
all Authentication and Application
Override policies. 

 Workaround: Reset rules
using a list of rules or a rule name for Authentication and Application Override policies. 

 CYR-6013 
 When you migrate a single tenant to multi-tenant
mode, you must do a local commit and then push the configuration
before you add more tenants. 

 CYR-5867 
 After upgrading to a new version of the
Cloud Services plugin, you are able to downgrade. The downgrade
operation should be disallowed. 

 Workaround: Do not
downgrade the Cloud Services plugin after you have upgraded it. 

 CYR-5842 
 When using the multi-tenant feature and
migrating the first tenant to multi-tenancy, you can select template
stacks and templates that are not associated with the tenant that
you want to migrate, including templates that are used with on-premise firewalls. 

 Workaround: When
you convert to multi-tenant mode, be sure to choose only those templates
that you want to associate to the first tenant to migrate. 

 CYR-5690 
 When configuring multi-tenancy, if you are
planning to later configure Prisma Access for mobile users, you
must do a local Commit of the your changes for the plugin ( Commit Commit to Panorama )
after you add templates, template stacks, and device groups for
each tenant and before you onboard each tenant. 

 CYR-5563 
 When using the multi-tenancy feature, users
who manage single tenants cannot see the system logs. The Monitor Logs System choice
is not available. This limitation applies to all Administrators
who have an administrative role of Device Group and Template. Only
superusers can view system logs in multi-tenancy mode. 

 CYR-5561 
 When using the multi-tenancy feature and
logged in as a tenant-level administrative user, opening the Panorama
Task Manager (clicking Tasks at the bottom
of the Panorama web interface) shows all tasks for all tenants,
including any tasks done at the superuser (Admin) level. 

 CYR-5476 
 When you enable multi-tenancy and migrate
your configuration to the first sub-tenant, CLI commands are not
supported for this operation. As a result, you must, use the Panorama
user interface (UI). 

 CYR-5159 
 If you configure a mobile user IP address
pool for a single region instead of Worldwide, mobile users can
still view and attempt to connect to all available gateway regions
from their GlobalProtect app. This attempt fails because there is
no IP address pool to allocate for other regions. 

 Workaround: To
allow mobile users to manually select a gateway, either configure
an IP address pool for the region in the location where you want
the users to connect, or configure a Worldwide IP address pool for
mobile users in Prisma Access to allow them to select all the locations
you have deployed. 

 CYR-5139 
 In an environment with on-premise firewalls
on each side of Prisma Access and the remote network connections
to which the on-premise firewalls are connected are in different
regions, users behind one on-premise firewall cannot contact users
behind another on-premise firewall unless you have configured an
explicit policy to allow traffic between zone Trust and zone Trust. 

 CYR-5098 
 If you change the master key in Panorama
(in Device > Master Key and Diagnostics), the master key for Cloud
Services is not synchronized with this master key. 

 Workaround: Select
Panorama > Cloud Services > Configuration > Service Setup > Service
Operations > Edit Master Key and manually change the master key
to be the same as the Panorama master key. 

 CYR-5062 
 When regular dynamic updates are downloaded
to Panorama (by default, every Wednesday at 01:02), the MD5 checksum
is changed. This condition can cause the Panorama configuration
and the Prisma Access infrastructure to lose synchronization. While
no tunnels are affected by this out of synchronization state, the
status for Service Connections, Remote Networks, Mobile Users, and
the Logging Service show a Config Status of Out
of Sync . 

 Workaround: Perform a Commit and Push operation
on the Panorama. 

 CYR-4010 
 The BGP router configuration on the Prisma
Access firewalls can receive a maximum of 15000 prefixes from each
peer. And the total number of routes (static and dynamic) learned
through BGP cannot exceed 25000. Exporting more than 25000 routes may
adversely affect traffic flow on your network. 

 CYR-3952 
 After you generate a new API key by selecting Panorama Cloud Services Configuration Service Setup Generate new API Key , the previous
API key is still valid for a period of time (up to five minutes).
You use this API to retrieve the list of IP addresses for your Prisma
Access firewalls. 

 CYR-3638 
 For service and remote network connections
that have BGP enabled, the Prisma Access ignores any route it receives
from a neighbor with an AS number in its AS_PATH list that duplicates
an AS number in the Prisma Access AS infrastructure (Infra-AS). 

 CYR-3469 
 If you have configured a Notification
URL , when you onboard a new remote network location,
two notifications are sent to the URL instead of only one. 

 CYR-3385 
 When you configure the same AS number for
the service connection and remote network location(s), the routes
are not imported in to the firewall on the remote network location. 

 CYR-3330 
 Mobile users cannot connect to remote network
locations without a service connection. 

 CYR-3034 
 When configuring SAML, you must perform
all configuration with a role of Superuser, including any configuration
you perform for SAML using CLI. 

 CYR-2648 
 The  Panorama Cloud Services Configuration  page is
grayed out when Panorama is not in sync with NTP. 

 Workaround: Make
sure to synchronize time with NTP ( Panorama Setup Services NTP ). 

 CYR-2578 
 Master Keys do not work for two Panorama
appliances set as HA primary and secondary appliances. 

 Workaround: Deselect
the Enable HA check box on the secondary
Panorama appliance and commit the changes, set the same Master Key
on both the primary and secondary Panorama appliance, then re-enable
HA on the secondary Panorama appliance and commit the changes. 

 CYR-2028 
 The Device Setup Management page
is not available on the Panorama appliance running the Prisma Access
plugin. You cannot configure NT LAN Manager (NTLM). 

 CYR-1646 
 Although Panorama allows you to delete the
Mobile_User_Template that was created when the Prisma Access was
provisioned, deleting this template also deletes your onboarding
configuration and, upon commit, removes your Prisma Access for mobile users
configuration. 

 CYR-1189 
 When you onboard a new service connection
or a remote network, the count for service connection and total
remote peers displayed on  Panorama Cloud Services Status Status  is inaccurate
until the provisioning is complete. 

 CYR-1120 
 On Panorama, you cannot validate commit
on a device group or template configuration before pushing the configuration
to the Prisma Access infrastructure for remote networks and mobile
users. 

 CYR-575 
 You cannot configure the Prisma Access gateway
as an internal gateway. 

 Previous 

 Upgrade the Cloud Services Plugin 

 Next 

 Prisma Access Addressed Issues 

 On This Page 

 Activation and Onboarding 

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

 Panorama 

 Service Provider 

 VM-Series 

 Plugins 

 SASE 

 Prisma Access 

 Prisma SASE Multitenant Platform 

 AI-Powered ADEM 

 Prisma Access Monitoring & Visibility 

 Prisma SD-WAN 

 ION Devices 

 Next-Generation CASB 

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

 Shared Policy for NGFWs and Prisma Access 

 IPSec VPN 

 Security Policy 

 Quantum Security 

 Endpoints 

 GlobalProtect 

 Remote Browser Isolation 

 Prisma Access Agent 

 Visibility & Monitoring 

 Dashboards 

 Incidents and Alerts 

 Reports 

 Autonomous DEM 

 FedRAMP 

 Prisma SASE for FedRAMP 

 Autonomous DEM for FedRAMP 

 Hardware Reference 

 ION 1000 

 ION 1200 

 ION 1200-S 

 ION 2000 

 ION 3000 

 ION 3200 

 ION 5200 

 ION 7000 

 ION 9000 

 ION 9200 

 Hardware Quick Start Guides 

 ION 1200 

 ION 1200 4G 

 ION 1200 5G 

 ION 1200-S 

 ION 1200-S 4G 

 ION 1200-S 5G 

 ION 3200 

 ION 5200 

 ION 9200 

 Virtual ION Deployment 

 Virtual ION on AWS 

 Virtual ION on Azure 

 Virtual ION on GCP 

 Virtual ION on KVM for NFV 

 Virtual ION on OCI 

 Virtual ION on VMware 

 3rd Party Integrations 

 AWS Cloud-WAN Integration (GRE Connect) 

 AWS Cloud-WAN Integration (Tunnel-less Connect) 

 Checkpoint Integration 

 LiveAction Integration 

 Netskope Integration 

 Symantec Web Security Services Integration 

 Best Practices 

 Best Practices Library 

 Experts Corner 

 Solutions Docs from Product Experts 

 SASE 

 Release Notes 

 3.2 Preferred and Innovation 

 Prisma SASE 

 Prisma Access 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

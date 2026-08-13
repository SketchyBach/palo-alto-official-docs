---
url: https://docs.paloaltonetworks.com/advanced-url-filtering/administration/url-filtering-features/allow-password-access-to-certain-sites
fetched_at: 2026-08-13T15:18:44Z
source: palo-alto-main
---

# Allow Password Access to Certain Sites Clear

Allow Password Access to Certain Sites 

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

 Allow Password Access to Certain Sites 

 Updated on 

 Thu Jul 30 16:45:14 PDT 2026 

 Focus 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 Filter

 Expand All 
 | 
 Collapse All 

 Advanced URL Filtering 

 Administration 

 Updated on 

 Thu Jul 30 16:45:14 PDT 2026 

 Focus 

 Home 

 Advanced URL Filtering 

 URL Filtering Features 

 Allow Password Access to Certain Sites 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 Advanced URL Filtering 

 Allow Password Access to Certain Sites 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Advanced URL Filtering 

 Administration 

 Previous 

 Inspect SSL/TLS Handshakes 

 Next 

 Credential Phishing Prevention 

 Allow Password Access to Certain Sites 

 Set up password access to websites in blocked categories for special
 individuals. 

 Where can I use
this? What do I need? 

 Prisma Access (Managed by Strata Cloud Manager) 

 Prisma Access (Managed by Panorama) 

 NGFW (Managed by Strata Cloud Manager) 

 NGFW (Managed by PAN-OS or Panorama) 

 Advanced URL Filtering (or a legacy
 URL filtering license) 

 Notes: 

 Legacy URL filtering licenses are discontinued,
 but active legacy licenses are still
 supported. 

 Prisma Access licenses include Advanced URL Filtering capabilities. 

 In some cases, it may be necessary to require password access to websites in certain categories.
 For example, your company may block URL categories that threaten the safety and
 wellbeing of employees. However, certain employees may need access to these
 categories for research or other legitimate purposes. To balance safety and business
 needs, implementing URL admin overrides can be an effective solution. 

 To create a URL admin override, set the action for a category to
 override . Then, create a password that users must enter
 to access sites in this category. When users attempt to access a website in a
 category that you have overridden, a Continue and Override response page 
 appears. This page notifies users that a website is blocked and prompts them to
 enter a password to continue to the site. 

 Strata Cloud Manager 

 PAN-OS & Panorama 

 Allow Password Access to Certain Sites ( Strata Cloud Manager ) 

 If you’re using Panorama to manage Prisma Access : 

 Toggle over to the PAN-OS & Panorama tab
and follow the guidance there. 

 If you’re using Strata Cloud Manager , continue here. 

 Go to the URL Access Management dashboard. 

 Select Configuration NGFW and Prisma Access Security Services URL Access Management . 

 Select Settings . 

 Create a URL admin override password. 

 Go to URL Admin Overrides, and Add URL
Admin Overrides . 

 ( Optional ) Select a Mode for prompting
users for the password: 

 Transparent —The password
prompt appears to originate from the original destination URL. The
firewall intercepts the browser traffic destined for sites in a
URL category set to override and issues an HTTP 302 to prompt for
the password, which applies on a per-vsys level. 

 Redirect —The password prompt appears from
an Address (IP address or DNS hostname) that you
specify. The firewall intercepts HTTP or HTTPS traffic to a URL
category set to override and uses an HTTP 302 redirect to send the
request to a Layer 3 interface on the firewall. 

 Enter a Password , then enter
it again to Confirm Password . 

 ( Optional ) Select an SSL/TLS Service Profile . 

 You can create and manage SSL/TLS service profiles by clicking Create
New and Manage , respectively. 

 Save your changes. 

 ( Optional ) Set the duration of override access
and password lockouts. 

 By default, users can access websites in categories for
which they have successfully entered an override password for 15
minutes. After the default or custom interval passes, users must
re-enter the password. 

 By default, users are blocked for 30
minutes after three failed password attempts. After the user is
locked out for the default or custom duration, they can try to access the
websites again. 

 Customize the General Settings. 

 For URL Admin Override Timeout , enter
a value (in minutes) from 1 to 86,400. 

 For URL Admin Lockout Timeout , enter
a value (in minutes) from 1 to 86,400. 

 Save your changes. 

 Specify the URL categories that require password access. 

 On the URL Access Management dashboard,
under the Access Control tab, go to URL Access
Management Profiles and modify or Add Profile . 

 Under Access Control, select the categories that require
password access. 

 With all the categories selected, click Set Access and
then select Override . 

 You should see that Site Access for the highlighted categories
now say override . 

 Save your changes. 

 Apply the URL Access Management profile to a Security
policy rule. 

 A URL Access Management profile is only active when it’s
included in a profile group that a Security policy rule references. 

 Follow
the steps to activate a URL Access Management
profile (and any Security profile). Be sure to Push
Config when you are done. 

 Allow Password Access to Certain Sites ( PAN-OS & Panorama ) 

 Set a URL admin override password. 

 Select Device Setup Content ID . 

 In the URL Admin Override section, click Add . 

 In the Location field, select
the virtual system to which this password applies. 

 Enter a Password , then enter
it again to Confirm Password . 

 Select an SSL/TLS Service Profile . 

 SSL/TLS service profiles specify
the certificate that the firewall presents to the user if the site
with the override is an HTTPS site. 

 Select a Mode for prompting
user for the password: 

 Transparent —The password
prompt appears to originate from the original destination URL. The
firewall intercepts the browser traffic destined for sites in a
URL category set to override and issues an HTTP 302 to prompt for
the password, which applies on a per-vsys level. 

 The
client browser will display certificate errors if it does not trust
the certificate. 

 Redirect —The
password prompt appears from an Address (IP
address or DNS hostname) that you specify. The firewall intercepts
HTTP or HTTPS traffic to a URL category set to override and uses
an HTTP 302 redirect to send the request to a Layer 3 interface
on the firewall. 

 Click OK . 

 ( Optional ) Set the duration of override access
and password lockouts. 

 By default, users can access websites in categories for
which they have successfully entered an override password for 15
minutes. After the default or custom interval passes, users must
re-enter the password. 

 By default, users are blocked for 30
minutes after three failed password attempts. After the user is
locked out for the default or custom duration, they can try to access the
websites again. 

 Edit the URL Filtering section. 

 For URL Admin Override Timeout , enter
a value (in minutes) from 1 to 86,400. ---By default, users can
access sites within the category for 15 minutes without re-entering
the password. 

 For URL Admin Lockout Timeout , enter
a value (in minutes) from 1 to 86,400. 

 Click OK . 

 ( Redirect mode only ) Create a Layer 3 interface
to which to redirect web requests to sites in a category configured
for override. 

 Create a management profile to enable the
interface to display the URL Filtering Continue and Override Page
response page: 

 Select Network Interface Mgmt and click Add . 

 Enter a Name for the profile, select Response
Pages , and then click OK . 

 Create the Layer 3 interface. Be sure to attach the
management profile you just created (on the Advanced Other Info tab of the Ethernet
Interface dialog). 

 ( Redirect mode only ) To transparently redirect
users without displaying certificate errors, install a certificate
that matches the IP address of the interface to which you are redirecting
web requests to a site in a URL category configured for override.You
can either generate a self-signed certificate or import a certificate
that is signed by an external CA. 

 To use a self-signed certificate, you must first create
a root CA certificate and then use that CA to sign the certificate
you will use for URL admin override as follows: 

 To create a root CA certificate, select Device Certificate Management Certificates Device Certificates and
then click Generate . Enter a Certificate Name ,
such as RootCA. Do not select a value in the Signed By field
(this is what indicates that it is self-signed). Make sure you select
the Certificate Authority check box and then
click Generate the certificate. 

 To create the certificate to use for URL admin override,
click Generate . Enter a Certificate Name and
enter the DNS hostname or IP address of the interface as the Common
Name . In the Signed By field,
select the CA you created in the previous step. Add an IP address
attribute and specify the IP address of the Layer 3 interface
to which you will be redirecting web requests to URL categories
that have the override action. 

 Generate the certificate. 

 To configure clients to trust the certificate, select
the CA certificate on the Device Certificates tab
and click Export . You must then import the
certificate as a trusted root CA into all client browsers, either
by manually configuring the browser or by adding the certificate
to the trusted roots in an Active Directory Group Policy Object
(GPO). 

 Specify which URL categories require an override password
to enable access. 

 Select Objects URL Filtering and either select
an existing URL Filtering profile or Add a
new one. 

 On the Categories tab, set
the Action to override for each category
that requires a password. 

 Complete any remaining sections on the URL Filtering
profile and then click OK to save the profile. 

 Apply the URL Filtering profile to the Security policy
rule(s) that allows access to the sites requiring password override
for access. 

 Select Policies Security and select the appropriate
Security policy to modify it. 

 Select the Actions tab and
in the Profile Setting section, click the
drop-down for URL Filtering and select the
profile. 

 Click OK to save. 

 Commit the configuration. 

 Previous 

 Inspect SSL/TLS Handshakes 

 Next 

 Credential Phishing Prevention 

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

 IPSec VPN 

 Security Policy 

 Quantum Security 

 Endpoints 

 GlobalProtect 

 Remote Browser Isolation 

 Visibility & Monitoring 

 Dashboards 

 Incidents and Alerts 

 Reports 

 Autonomous DEM 

 Best Practices 

 Best Practices Library 

 11.0 

 10.1 

 Network Security 

 PAN-OS 

 10.2 

 11.1 

 Cloud-Delivered Security Services 

 Panorama 

 URL Filtering 

 Administration 

 Information Type 

 Prisma Access 

 Strata Cloud Manager 

 9.1 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

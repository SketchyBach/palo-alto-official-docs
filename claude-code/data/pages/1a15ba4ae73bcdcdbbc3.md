---
url: https://docs.paloaltonetworks.com/vm-series/activation-and-onboarding/what-happens-when-licenses-expire
fetched_at: 2026-08-13T17:41:14Z
source: palo-alto-main
---

# What Happens When Licenses Expire? Clear

What Happens When Licenses Expire? 

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

 What Happens When Licenses Expire? 

 Updated on 

 Fri Jun 19 07:15:14 PDT 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 VM-Series Firewall Docs 

 Activation & Onboarding 

 Getting Started 

 Upgrade 

 Deployment 

 Select a Document 

 Public Cloud 

 Private Cloud 

 Updated on 

 Fri Jun 19 07:15:14 PDT 2026 

 Focus 

 Home 

 VM-Series 

 What Happens When Licenses Expire? 

 Download PDF 

 VM-Series 

 What Happens When Licenses Expire? 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 VM-Series Firewall Docs 

 Activation & Onboarding 

 Getting Started 

 Upgrade 

 Deployment 

 Select a Document 

 Public Cloud 

 Private Cloud 

 Previous 

 Use the Licensing API 

 Next 

 Licenses for Cloud Security Service Providers (CSSPs) 

 What Happens When Licenses Expire? 

 Find out what happens when one of your Palo Alto Networks firewalls expires. 

 Where Can I Use This? What Do I Need? 

 VM-Series deployment 

 VM-Series 10.x or above 

 Panorama running PAN-OS 10.1.x or above versions 

 Customer Support Portal (CSP) account with one of the following
 user roles: 
 Superuser, Standard User, Limited User, Threat
 Researcher, AutoFocus Trial Role, Group superuser, Group
 Standard User, Group Limited User, Group Threat
 Researcher, Authorized Support Center (ASC) User, and
 ASC Full Service User. 

 Superuser access to the VM-Series firewall 

 Palo Alto Networks VM-Series firewall licenses and subscriptions provide the firewall with added
 functionality and/or access to a Palo Alto Networks cloud-delivered service. When a
 license is within 30 days of expiration, a warning message displays in the system log
 daily until you renew the subscription or it expires. Upon license expiration, some
 subscriptions continue to function in a limited capacity, and others stop operating
 completely. Here you can find out what happens when each subscription expires. 

 The precise moment of license expiry is at 12:00 AM Greenwich Mean Time (GMT) of the
 expiration date. For example, if your license expiration date is December 20, 2024,
 functionality will cease at 12:00 AM GMT on December 20, 2024. All license-related
 functions operate on GMT, regardless of the configured time zone on the
 firewall. 

 ( Panorama license ) If the support license expires, Panorama can still manage
 firewalls and collect logs, but software and content updates will be unavailable.
 The software and content versions on Panorama must be the same as or later than the
 versions on the managed firewalls, or else errors will occur. For details, see Panorama, Log Collector, Firewall, and WildFire
 Version Compatibility . 

 License Expiry Behavior 

 VM-Series 
 You can still: 

 You can continue to configure and use the firewall you deployed prior to the license expiring
 with no change in session capacity. The firewall won't reboot
 automatically and cause a disruption in traffic. 

 However, if the firewall reboots for any reason, the firewall enters an unlicensed state. While
 unlicensed, a firewall supports a maximum of 1,200 sessions. No
 other management plane features or configuration options are
 restricted. 

 Threat Prevention 
 Alerts appear in the system log indicating that the license has expired. 

 You can still: 

 Use signatures installed at the time the license expired, unless you install a new
 Applications-only content update either
 manually or as part of an automatic schedule. If you do, the
 update will delete your existing threat signatures and you will
 no longer receive protection against them. 

 Use and modify Custom App-ID™ and threat signatures. 

 You
can no longer: 

 Install new signatures. 

 Roll signatures back to previous versions. 

 DNS Security 
 You can still: 

 Use
local DNS signatures if you have an active Threat Prevention license. 

 You
can no longer: 

 Get new DNS signatures. 

 Advanced URL Filtering / URL Filtering 
 You can still: 

 Enforce
policy using custom URL categories. 

 Enforce policy using PALO ALTO NETWORKS-DB categories that were in your local cache when the
 license expired. 

 You can no longer: 

 Get updates to cached PAN-DB categories. 

 Connect to the PAN-DB URL filtering database. 

 Get PAN-DB categories of uncached URLs. 

 Analyze URL requests in real-time using Advanced URL Filtering. 

 WildFire 
 You can still: 

 Forward Portable Executable (PE) for analysis. 

 Get signature updates every 24-48 hours if you have an active Threat
Prevention subscription. 

 You can no longer: 

 Get five-minute updates through the WildFire public and private
clouds. 

 Forward advanced file types such as APKs, Flash files, PDFs, Microsoft
Office files, Java Applets, Java files (.jar and .class), and HTTP/HTTPS
email links contained in SMTP and POP3 email messages. 

 Use the WildFire API . 

 Use the WildFire appliance to host a WildFire private cloud or a WildFire hybrid cloud . 

 AutoFocus 
 You can still: 

 Use
an external dynamic list with AutoFocus data for a grace period
of three months. 

 You can no longer: 

 Access
the AutoFocus portal. 

 View the AutoFocus Intelligence Summary for
Monitor log or ACC artifacts. 

 Cortex Data Lake 
 You can still: 

 Store log data for a 30-day grace period, after which it's deleted. 

 Forward logs to Cortex Data Lake until the end of the 30-day grace
period. 

 GlobalProtect 
 You can still: 

 Use
the app for endpoints running Windows and macOS. 

 Configure single or multiple internal and external gateways . 

 You
can no longer: 

 Access the Linux OS app and mobile
app for iOS, Android, Chrome OS, and Windows 10 UWP. 

 Use IPv6 for external gateways. 

 Run HIP checks. 

 Use Clientless VPN . 

 Enforce split tunneling based on destination domain, client process,
and video streaming application. 

 Support 
 You can no longer: 

 Receive software updates. 

 Download VM images. 

 Benefit from technical support. 

 Previous 

 Use the Licensing API 

 Next 

 Licenses for Cloud Security Service Providers (CSSPs) 

 On This Page 

 Activation and Onboarding 

 Strata Cloud Manager 

 Next-Generation Firewalls 

 Firewalls 

 PAN-OS 

 PAN-OS SD-WAN 

 VM-Series 

 Plugins 

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

 Resources 

 All Release Notes 

 Compatibility Matrix 

 Experts Corner 

 Network Security 

 Activation & Onboarding 

 Licensing 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

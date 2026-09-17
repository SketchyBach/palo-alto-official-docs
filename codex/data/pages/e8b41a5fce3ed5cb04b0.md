---
url: https://docs.paloaltonetworks.com/panorama/administration/manage-firewalls/set-up-zero-touch-provisioning
fetched_at: 2026-09-16T07:41:44Z
source: palo-alto-main
---

# Set Up Zero Touch Provisioning Clear

Updated on 

 Aug 7, 2026 

 Focus 

 Home 

 Panorama 

 Manage Firewalls with Panorama 

 Set Up Zero Touch Provisioning 

 Download PDF 

 Panorama 

 Set Up Zero Touch Provisioning 

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

 Change Between Panorama Management and Cloud Management 

 Next 

 ZTP Configuration Elements 

 Set Up Zero Touch Provisioning 

 Set up Zero Touch Provisioning (ZTP) to simplify and
automate on-boarding new managed firewall deployments. 

 Where Can I Use This? What Do I Need? 

 NGFW (Managed by Panorama) 

 Device Management License 

 Panorama superuser role 

 Set up Zero Touch Provisioning (ZTP) is to simplify and automate the
 onboarding of new firewalls to the Panorama™ management server. ZTP streamlines the
 initial firewall deployment process by allowing network administrators to ship managed
 firewalls directly to their branches and automatically add the firewall to the Panorama™
 management server after the ZTP firewall successfully connects to the Palo Alto Networks
 ZTP service. This allows businesses to save on time and resources when deploying new
 firewalls at branch locations by removing the need for IT administrators to manually
 provision the new managed firewall. After successful onboarding, Panorama provides the
 means to configure and manage your ZTP configuration and firewalls. 

 The ZTP cloud service supports a direct internet connection to successfully onboard a ZTP
 firewall to Panorama management. The ZTP cloud service does not support an explicit web
 proxy and is unable to onboard a ZTP firewall to Panorama management if an explicit web
 proxy is configured as a gateway to the internet for your ZTP firewalls and
 Panorama. 

 ZTP onboarding requires on the ZTP firewall, you cable the Eth1/1 interface with an
 outbound internet connection before the ZTP firewall is powered on. This is required to
 successfully onboard the ZTP firewall to Panorama management, register your ZTP firewall
 with the CSP, and push the policy and network configurations from Panorama. 

 Only Panorama administrators with Superuser privileges can access the ZTP
 settings required to set up ZTP. 

 Review and subscribe to ZTP Service Status events to be notified
 about scheduled maintenance windows, outages, and workarounds. 

 ZTP is supported on the following ZTP firewalls: 

 PA-400 Series Firewalls 

 ( Support ZTP over cellular ) PA-410R-5G, PA-415-5G,
 PA-415R-5G, PA-455-5G, and PA-455R-5G 

 PA-820-ZTP and PA-850-ZTP 

 PA-1400 Series Firewalls 

 PA-3220-ZTP, PA-3250-ZTP, and PA-3260-ZTP 

 PA-3400 Series Firewalls 

 PA-5400 Series Firewalls 

 PA-5450 

 Before you begin setting up ZTP on Panorama, review the Firewall Hardware Quick Start and Reference Guides to
 understand how to correctly install your firewall to successfully leverage ZTP. 

 Previous 

 Change Between Panorama Management and Cloud Management 

 Next 

 ZTP Configuration Elements

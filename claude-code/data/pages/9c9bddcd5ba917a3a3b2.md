---
url: https://docs.paloaltonetworks.com/panorama/getting-started/set-up-panorama/set-up-the-m-series-appliance/perform-initial-configuration-of-an-air-gapped-m-series-appliance
fetched_at: 2026-08-13T17:18:30Z
source: palo-alto-main
---

# Perform Initial Configuration of an Air Gapped M-Series Appliance Clear

Perform Initial Configuration of an Air Gapped M-Series Appliance 

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

 Perform Initial Configuration of an Air Gapped M-Series Appliance 

 Updated on 

 Tue Jul 14 08:53:35 PDT 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Panorama Docs 

 Getting Started 

 Administration 

 New Features 

 Updated on 

 Tue Jul 14 08:53:35 PDT 2026 

 Focus 

 Home 

 Panorama 

 Set Up Panorama 

 Set Up the M-Series Appliance 

 Perform Initial Configuration of an Air Gapped M-Series Appliance 

 Download PDF 

 Panorama 

 Perform Initial Configuration of an Air Gapped M-Series Appliance 

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

 Perform Initial Configuration of the M-Series Appliance 

 Next 

 M-Series Setup Overview 

 Perform Initial Configuration of an Air Gapped M-Series Appliance 

 Initial configuration procedure for a standalone air gapped M-Series Panorama™
 management server. 

 Where Can I Use This? What Do I Need? 

 NGFW (Managed by Panorama) 

 M-series hardware appliance 

 Super user role 

 Perform the initial configuration for an air gapped M-Series appliance. By default,
 Panorama has an IP address of 192.168.1.1 and a username/password of admin/admin.
 For security reasons, you must change these settings before continuing with other
 configuration tasks. You must perform these initial configuration tasks either from
 the Management (MGT) interface or using a direct serial port connection to the
 console port on the M-700, M-600, M-500, M-300, or M-200 appliance. 

 The air gapped Panorama cannot connect to the Palo Alto Networks update server
 because an outbound internet connection is required. To activate licenses, upgrade
 the PAN-OS software version, and install dynamic content updates you must upload the
 relevant files to the air gapped firewalls manually. 

 If you are configuring an M-Series appliance in Log Collector mode with 10GB
 interfaces, you must complete this entire configuration procedure for the 10GB
 interfaces to display as Up . 

 Gather the required information from your network administrator. 

 Private IP address for the management (MGT) port 

 Netmask 

 Default gateway 

 DNS server address 

 NTP server address 

 Install and power on M-Series appliance. 

 Review your M-Series appliance hardware reference
 guide for details and best practices. 

 Connect to the M-Series appliance. 

 You must log in using the default admin username. You
 are immediately prompted to change the default
 admin password before you can continue. The
 new password must be a minimum of eight characters and include a minimum of
 one lowercase and one uppercase character, as well as one number or special
 character. 

 You can connect to the M-Series appliance in one of the following ways: 

 Connect a serial cable from your computer to the Console port and
 connect to the M-Series appliance using terminal emulation software
 (9600-8-N-1). Wait a few minutes for the boot-up sequence to complete;
 when the M-Series appliance is ready, the prompt changes to the name of
 the M-Series, for example M-500 login . 

 Log in to the Panorama CLI by connecting an
 RJ-45 Ethernet cable from your computer to the MGT interface on the
 M-Series appliance. From a browser, go to
 https://192.168.1.1 . 

 You may need to change the IP address on your computer to an
 address in the 192.168.1.0/24 network, such as 192.168.1.2, to
 access this URL. 

 Configure the network settings for the air gapped M-Series appliance. 

 The following commands set the interface IP allocation to
 static , configures the IP address for the
 MGT interface, the Domain Name Server (DNS), and Network Time Protocol (NTP)
 server. 

 admin> configure 

 admin# set deviceconfig system type static 

 admin# set deviceconfig system ip-address <IP-Address> netmask <Netmask-IP> default-gateway <Gateway-IP> 

 admin# set deviceconfig system dns-settings servers primary <IP-Address> secondary <IP-Address> 

 admin# set deviceconfig system ntp-servers primary-ntp-server ntp-server-address <IP-Address> 

 admin# set deviceconfig system ntp-servers secondary-ntp-server ntp-server-address <IP-Address> 

 Register the M-Series appliance with the Palo Alto Networks Customer
 Support Portal (CSP). 

 Log in to the Palo Alto Networks CSP . 

 Click Register a Device . 

 Select Register device using Serial Number and
 click Next . 

 Enter the required Device
 Information . 

 Enter the M-Series appliance Serial
 Number . 

 Check (enable) Device will be used
 offline . 

 Select the PAN-OS OS Release running
 on the M-Series appliance. 

 Enter the required Location
 Information . 

 Enter the City the M-Series appliance
 is located in, 

 Enter the Postal Code the M-Series
 appliance is located in, 

 Enter the Country the M-Series
 appliance is located in. 

 Agree and Submit . 

 Skip this step when prompted to generate the
 optional Day 1 Configuration config
 file. 

 Download the Panorama license keys. 

 The license key files are required to activate your Panorama licenses when
 air gapped. 

 Log in to the Palo Alto Networks CSP . 

 Select Product Devices and locate the M-Series appliance you added. 

 Download all license keys files from the download links available
 License column. 

 You must download a license key file for each license you want to
 active on Panorama. 

 Active the Panorama licenses. 

 Log in to the Panorama web
 interface . 

 Select Panorama Licenses and Manually upload license
 key . 

 Click Choose File to select the license key
 file you downloaded in the previous step and click
 OK . 

 Repeat this step to uploaded and activate all licenses. 

 ( Optional ) Configure general Panorama settings as needed. 

 Select Panorama Setup Management and edit the General Settings. 

 Enter a Hostname for Panorama and enter your
 network Domain name. The domain name is just a
 label; it will not be used to join the domain. 

 Enter Login Banner text that informs users who
 are about to log in that they require authorization to access the
 Panorama management functions. 

 As a best practice, avoid using welcoming verbiage. Additionally,
 you should ask your legal department to review the banner
 message to ensure it adequately warns that unauthorized access
 is prohibited. 

 Enter the Latitude and
 Longitude to enable accurate placement of the
 M-Series on the world map. 

 Click OK . 

 Commit and Commit to
 Panorama . 

 Upgrade the PAN-OS and dynamic content versions on
 Panorama. 

 Review the PAN-OS Upgrade Guide and PAN-OS Release Notes for detailed information
 about your target PAN-OS upgrade version. 

 Log in to the Palo Alto Networks CSP . 

 Download dynamic content updates. 

 Alternatively, you can use a Secure Copy Protocol (SCP) server to
 automatically download
 dynamic content updates for Panorama, managed
 firewalls, Log Collectors, and WildFire appliances. An outbound
 internet connection is required for the SCP server to download
 dynamic content updates from the Palo Alto Networks Update
 Server. 

 Select Updates Dynamic Updates . 

 Select the dynamic Content type 
 you want to install. 

 Download the dynamic content update to
 your local device. 

 Repeat this step to download all required dynamic content
 updates. 

 Download a PAN-OS software update. 

 Select Updates Software Updates . 

 For the Content type , select
 Panorama M Base . For the
 Release type , select
 All (default) or
 Preferred . 

 In the Download column, click
 the PAN-OS version to download the software image to your
 local device. 

 Log in to the Panorama web
 interface . 

 Select Panorama Dynamic Updates and Upload the dynamic content
 updates you downloaded. 

 Repeat this step to Browse and select all the
 dynamic content release versions. 

 Install the dynamic content updates. 

 Select Panorama Software and Upload the PAN-OS software
 image you download. 

 Install the PAN-OS software version. 

 Panorama needs to restart to finish installing the PAN-OS software
 upgrade. 

 Connect Panorama to your network. 

 Disconnect Panorama from your computer. 

 Connect the MGT port to a switch port on your management network using
 an RJ-45 Ethernet cable. Make sure that the switch port you cable on
 Panorama is configured for autonegotiation. 

 Previous 

 Perform Initial Configuration of the M-Series Appliance 

 Next 

 M-Series Setup Overview 

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

 Prisma SD-WAN Experts Corner 

 Network Policy 

 QoS Whitepaper 

 Security Architecture Whitepaper 

 External Antennas for ION-C Series 

 Dynamic Path Selection 

 Best Practices 

 Best Practices Library 

 Experts Corner 

 Solutions Docs from Product Experts 

 Resources 

 All Products A - Z 

 All Release Notes 

 Compatibility Matrix 

 Experts Corner 

 Network Security Platform 

 Security Policy 

 Decryption 

 Device-ID 

 IPSec VPN 

 Quality of Service 

 Quantum Security 

 11.1 & Later 

 Next-Generation Firewall 

 Getting Started 

 Panorama 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

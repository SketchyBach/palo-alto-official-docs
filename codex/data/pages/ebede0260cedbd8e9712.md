---
url: https://docs.paloaltonetworks.com/prisma-sd-wan/administration/prisma-sd-wan-sites-and-devices/set-up-devices/configure-device-access-otp
fetched_at: 2026-08-13T17:28:22Z
source: palo-alto-main
---

# Configure Device Access One-Time Password Clear

Configure Device Access One-Time Password 

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

 Configure Device Access One-Time Password 

 Updated on 

 Aug 10, 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma SD-WAN Docs 

 Activation & Onboarding 

 Administration 

 CloudBlades 

 Select a Document 

 CloudBlade Integrations 

 CloudBlades Integration with Prisma Access 

 Deployment 

 Incidents & Alerts 

 Reference 

 Release Notes 

 Select a Document 

 ION 6.8 

 ION 6.6 

 ION 6.5 

 ION 6.4 

 ION 6.3 

 ION 6.1 

 ION 5.6 

 Prisma SD-WAN Controller 

 Prisma SD-WAN On-Premises Controller 

 Prisma SD-WAN CloudBlades 

 Prisma Access CloudBlade Cloud Managed 

 Prisma Access CloudBlade Panorama Managed 

 New Features 

 Updated on 

 Aug 10, 2026 

 Focus 

 Home 

 Prisma SD-WAN 

 Prisma SD-WAN Administrator’s Guide 

 Prisma SD-WAN Sites and Devices 

 Set Up Devices 

 Configure Device Access One-Time Password 

 Download PDF 

 Prisma SD-WAN 

 Configure Device Access One-Time Password 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma SD-WAN Docs 

 Activation & Onboarding 

 Administration 

 CloudBlades 

 Select a Document 

 CloudBlade Integrations 

 CloudBlades Integration with Prisma Access 

 Deployment 

 Incidents & Alerts 

 Reference 

 Release Notes 

 Select a Document 

 ION 6.8 

 ION 6.6 

 ION 6.5 

 ION 6.4 

 ION 6.3 

 ION 6.1 

 ION 5.6 

 Prisma SD-WAN Controller 

 Prisma SD-WAN On-Premises Controller 

 Prisma SD-WAN CloudBlades 

 Prisma Access CloudBlade Cloud Managed 

 Prisma Access CloudBlade Panorama Managed 

 New Features 

 Previous 

 Assign a Device to a Shell 

 Next 

 Configure the ION Device at a Branch Site 

 Configure Device Access One-Time Password 

 Learn how to configure device access OTP in Prisma SD-WAN . 

 Where Can I Use
 This? What Do I
 Need? 

 Prisma SD-WAN (Managed by Strata Cloud Manager ) 

 Prisma SD-WAN 

 Device Access One-Time Password provides the ability to regain access to the device toolkit in
 the event that all toolkit passwords are forgotten and the device has lost
 connection to the controller. 

 In order to access an offline device, the device must be: 

 In a claimed or assigned state. 

 Offline and unable to talk to the controller. 

 To access the offline device: 

 At the console of the remote, offline device, log in with
 menu as the username and 
 digital>morgueS! as the password. 
 Once logged in, the console menu will present command options. 

 Select the Status option. 
 This verifies that the device is offline. 

 Once the device is offline and has a Claim certificate installed, select
 Device offline Access . 
 This generates the Challenge phrase . 

 Note down the Challenge phrase . 

 Log in to the Prisma SD-WAN web interface as a
 Super user and select Configuration Prisma SD-WAN ION Devices . 

 Select a device, click the ellipsis menu, and select Generate
 one-time password . 

 Enter the Challenge Phrase provided earlier by the
 device console, and click Submit . 

 If successful, a one-time password response will be generated. 

 Enter this one-time password on the device console for access to the Device
 Toolkit. 

 Note the following: 
 Challenge requests and incorrect entries in both forms will be logged. 

 The Challenge Phrase and subsequent response is only valid for the
 configured number of attempts. 

 Exiting from the Challenge prompt or logging out will automatically
 invalidate the Challenge string. 

 You can modify the maximum number of one-time password attempts and
 expiration timeframes from Configuration Prisma SD-WAN System Device Offline Access on the Prisma SD-WAN web interface. 

 Related CLIs 

 inspect connection 

 dump device status 

 clear connection 

 Previous 

 Assign a Device to a Shell 

 Next 

 Configure the ION Device at a Branch Site 

 On This Page 

 Activation & Onboarding 

 Strata Cloud Manager 

 Activate a License or Product 

 Cloud Identity Engine 

 Hub 

 Identity and Access Management 

 Tenant Management 

 SASE 

 Prisma Access 

 Strata Multitenant Cloud Manager 

 AI-Powered ADEM 

 Prisma Access Monitoring and Visibility 

 Visibility & Monitoring 

 Dashboards 

 Incidents and Alerts 

 Reports 

 Autonomous DEM 

 FedRAMP 

 Prisma SASE for FedRAMP 

 Hardware Reference 

 ION 1000 

 ION 1200 

 ION 1200-S 

 ION 2000 

 ION 3000 

 ION 3200 and ION 3200H 

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

 ION 3200H 

 ION 3200H 5G 

 ION 5200 

 ION 9200 

 Virtual ION Deployment 

 Virtual ION on AWS 

 Virtual ION on Azure 

 Virtual ION on GCP 

 Virtual ION on Alibaba Cloud 

 Virtual ION on KVM for NFV 

 Virtual ION on OCI 

 Virtual ION on VMware 

 Virtual ION on Megaport Virtual Edge 

 Virtual ION on Dell PowerEdge 

 Prisma SD-WAN Integration 

 AWS Cloud-WAN Integration (GRE Connect) 

 AWS Cloud-WAN Integration (Tunnel-less Connect) 

 Checkpoint Integration 

 LiveAction Integration 

 Netskope Integration 

 Symantec Web Security Services Integration 

 Prisma SD-WAN Experts Corner 

 Network Policy 

 QoS Whitepaper 

 Security Architecture Whitepaper 

 External Antennas for ION-C Series 

 Dynamic Path Selection 

 Best Practices 

 Best Practices Library 

 Resources 

 All Products A - Z 

 Compatibility Matrix 

 SASE 

 Administration 

 Prisma SD-WAN 

 Strata Cloud Manager 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

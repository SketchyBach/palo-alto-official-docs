---
url: https://docs.paloaltonetworks.com/prisma-sd-wan/administration/prisma-sd-wan-sites-and-devices/set-up-devices/configure-device-access-otp
fetched_at: 2026-09-16T07:47:49Z
source: strata-and-sase
---

# Configure Device Access One-Time Password Clear

Updated on 

 Mon Aug 24 08:54:44 PDT 2026 

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

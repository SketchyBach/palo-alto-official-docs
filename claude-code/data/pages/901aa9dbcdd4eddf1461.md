---
url: https://docs.paloaltonetworks.com/prisma-browser/administration/manage-prisma-browser-devices/prisma-browser-extension-device-posture-attributes
fetched_at: 2026-09-16T08:21:44Z
source: palo-alto-main
---

# Configure Prisma Browser Extension Posture Attributes Clear

Updated on 

 Thu Sep 10 09:47:19 PDT 2026 

 Focus 

 Home 

 Prisma Browser 

 Manage Prisma Browser Devices 

 Configure Prisma Browser Extension Posture Attributes 

 Download PDF 

 Prisma Browser 

 Configure Prisma Browser Extension Posture Attributes 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma Browser Docs 

 Activation & Onboarding 

 Getting Started 

 Deployment 

 Administration 

 Integrations 

 User Guide 

 Previous 

 Configure Prisma Browser Device Posture Attributes 

 Next 

 Configure Prisma Browser Mobile Device Posture Attributes 

 Configure Prisma Browser Extension Posture Attributes 

 Define the device posture attributes that determine which Devices can join the
 device group. 

 Where Can I Use This? What Do I Need? 

 Strata Cloud Manager 

 Prisma Browser standalone 

 Prisma Access with Prisma Browser bundle
 license or Prisma Browser standalone license 

 Superuser or Prisma Browser
 Roles 

 In Prisma Browser Extension, you can add attributes as match criteria when you
 add or edit a device group .
 Because Prisma Browser policy rules are enforced at the device group level, the
 attributes provide granular security that ensures the devices that Prisma Browser Extension allows to access your apps are adequately maintained and adhere with
 your security standards before they are allowed access to your network resources.
 For example, before allowing access to your most sensitive apps, you might want to
 ensure that the devices using the Prisma Browser Extension accessing your apps
 are using only the Opera browser. In this case, you would create a device group with
 an attribute that only allows devices using the extension that are only using the
 Opera browser. The following sections detail the attributes you can use to determine
 device group membership for devices using the Prisma Browser Extension. 

 To learn about attributes for managing device group membership on Windows and macOS
 devices, see Configure Prisma Browser Device Posture Attributes 

 Negative Postures 

 In some cases, you may want to exclude certain device attributes rather
 than require them. This is called creating a negative posture . 

 For example, you might normally create a rule that requires devices to run
 a specific operating system. However, if a new rule requires that devices
 must not use that operating system, you can use a negative posture
 instead. 

 This feature allows you to define rules that explicitly exclude certain
 attributes—such as a particular operating system—from being allowed. 

 Windows and macOS OS Versions 

 Creating a device group that uses the device's operating system as a posture is a
 good way to make sure that users have specific versions of the OS. If you add an
 OS version attribute as match criteria for a device group, Prisma Browser 
 checks the device OS version matches the attribute you defined before allowing
 membership in the device group. 

 Define the list of acceptable operating system versions for the Prisma Browser posture mechanism to check as follows. 

 When you add or edit a device
 group , add the OS version attribute. 

 Select the Windows or macOS versions, editions, and build numbers to allow
 into the device group. 

 Selecting All...versions
 will use all historical versions of the operating systems, including
 those that re deprecated it yes. 

 Selecting All...versions
 will use all historical versions of the operating systems, including
 those that re deprecated it yes. 

 Click Save . 

 Browser Brands 

 Enable the Browser Brands attribute to ensure that the
 device group only contains specific types of browsers—such as Chrome, Edge, or
 Brave. This can be especially useful when you need to create specialized rules
 for different browsers. 

 When you add or edit a device
 group , enable the Browser Brands 
 attribute. 

 Select the browser brands you want to support in the device group. 

 If you need to restrict the browsers to specific versions, click the pencil
 icon, and in the Specific brand version, enter the Minimum version of the
 browser that is acceptable. 

 Click Set . 

 Previous 

 Configure Prisma Browser Device Posture Attributes 

 Next 

 Configure Prisma Browser Mobile Device Posture Attributes

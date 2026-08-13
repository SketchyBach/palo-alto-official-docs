---
url: https://docs.paloaltonetworks.com/iot/administration/discover-iot-devices-and-take-inventory/devices-with-static-ip-addresses/add-a-static-ip-device-configuration
fetched_at: 2026-08-13T16:36:22Z
source: palo-alto-main
---

# Add a Static IP Device Configuration Clear

Add a Static IP Device Configuration 

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

 Add a Static IP Device Configuration 

 Updated on 

 Thu Jul 30 16:42:12 PDT 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Device Security Docs 

 Activation & Onboarding 

 Getting Started 

 Administration 

 Enterprise Administration 

 Integrations 

 Release Notes 

 Best Practice 

 New Features 

 Updated on 

 Thu Jul 30 16:42:12 PDT 2026 

 Focus 

 Home 

 Device Security 

 Device Security Administration Guide 

 Discover IoT Devices and Take Inventory 

 Devices with Static IP Addresses 

 Add a Static IP Device Configuration 

 Download PDF 

 Device Security 

 Add a Static IP Device Configuration 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Device Security Docs 

 Activation & Onboarding 

 Getting Started 

 Administration 

 Enterprise Administration 

 Integrations 

 Release Notes 

 Best Practice 

 New Features 

 Previous 

 Upload a List of Static IP Devices 

 Next 

 Upload a List of Subnets with Only Static IP Addresses 

 Add a Static IP Device Configuration 

 Add static IP devices to Device Security by manually configuring them. 

 Where Can I Use This? What Do I Need? 

 Device Security (Managed by Strata Cloud Manager) 

 (Legacy) IoT Security (Standalone portal) 

 One of the following subscriptions: 

 Device Security subscription

 Precision AI bundle subscription

 Device Security X subscription

 Instead of uploading a CSV file with a list
of static IP devices (see Upload a List of Static IP Devices ), you can
 add them individually. 

 Strata Cloud Manager 

 (Legacy) IoT Security 

 Strata Cloud Manager 

 Add static IP devices to Device Security in Strata Cloud Manager by manually
 configuring them.

 Navigate to Assets User-Defined Static IP Devices and then click Add Manually Add a Static IP Device .

 Define a static IP device and then click Add . 

 IP Address : Enter the static IP address of the device
you want to add to your inventory. The IP address is what Device Security 
uses to track user-defined static IP devices. 

 MAC Address (optional): If you want, add the MAC address of the device in hexadecimal
 notation. Device Security accepts any of the following MAC address formats: 

 aa:bb:cc:00:11:22 

 AA:BB:CC:00:11:22 

 aa.bb.cc.00.11.22 

 AA.BB.CC.00.11.22 

 aa-bb-cc-00-11-22 

 AA-BB-CC-00-11-22 

 aa bb cc 00 11 22 

 AA BB CC 00 11 22 

 aabbcc001122 

 AABBCC001122 

 If the user-defined MAC address is different
from the MAC address Device Security detects on the network, the detected
MAC address overrides the user-defined one. If Device Security does
not detect a MAC address, the user-defined MAC address appears on
the Devices and Device Details pages. 

 Vendor (optional): Enter the vendor for this device. 

 Model (optional): Enter the device model. 

 The vendor and model attributes provide extra information when referring to entries on the
 User-Defined Static IP Devices page later. However, they do not appear on
 the Devices and Device Details pages. 

 Click Add to add the configuration
to Device Security and then click OK to close
the confirmation message that appears. 

 After you add the static IP device, Device Security initially treats it as “not found”. It
 incrementally increases the Total User-Defined Static IP Devices counter by
 one and the Devices Not Found counter by one. Although it adds an entry for
 it to the User-Defined Static IP Devices list, the Result column remains
 empty – there isn’t a “matched” entry, indicating that Device Security detected
 network activity for this IP address, or a dash, indicating that no such
 activity was detected. 

 Because
 Device Security periodically compares entries in the user-defined static
IP devices list with those in its inventory and its internal database
of detected IP addresses without accompanying MAC addresses, the
page can remain in this initial state for several minutes. 

 If
a match is found, the Device Matches counter increases by one and
the Devices Not Found counter decreases by one. Also, “matched”
now appears in the Result column. 

 If
 Device Security does not find a match, it eventually displays a dash
in the Result column. 

 You might have to reload the User-defined
Static IP Devices page to see the updated data. 

 (Legacy) IoT Security 

 Add static IP devices to Device Security by manually configuring them. 

 Navigate to the User-defined Static IP Devices page ( Assets Devices User-Defined Static IP Devices ) and then click Add Manually Add a Static IP Device . 

 Define a static IP device and then click Add . 

 IP Address : Enter the static IP address of the device
you want to add to your inventory. The IP address is what Device Security 
uses to track user-defined static IP devices. 

 MAC Address (optional): If you want, add the MAC address of the device in hexadecimal
 notation. Device Security accepts any of the following MAC address formats: 

 aa:bb:cc:00:11:22 

 AA:BB:CC:00:11:22 

 aa.bb.cc.00.11.22 

 AA.BB.CC.00.11.22 

 aa-bb-cc-00-11-22 

 AA-BB-CC-00-11-22 

 aa bb cc 00 11 22 

 AA BB CC 00 11 22 

 aabbcc001122 

 AABBCC001122 

 If the user-defined MAC address is different
from the MAC address Device Security detects on the network, the detected
MAC address overrides the user-defined one. If Device Security does
not detect a MAC address, the user-defined MAC address appears on
the Devices and Device Details pages. 

 Vendor (optional): Enter the vendor for this device. 

 Model (optional): Enter the device model. 

 The vendor and model attributes provide extra information when referring to entries on the
 User-Defined Static IP Devices page later. However, they do not appear on
 the Devices and Device Details pages. 

 Click Add to add the configuration
to Device Security and then click OK to close
the confirmation message that appears. 

 After you add the static IP device, Device Security initially treats it as “not found”. It
 incrementally increases the Total User-Defined Static IP Devices counter by
 one and the Devices Not Found counter by one. Although it adds an entry for
 it to the User-Defined Static IP Devices list, the Result column remains
 empty – there isn’t a “matched” entry, indicating that Device Security detected
 network activity for this IP address, or a dash, indicating that no such
 activity was detected. 

 Because
 Device Security periodically compares entries in the user-defined static
IP devices list with those in its inventory and its internal database
of detected IP addresses without accompanying MAC addresses, the
page can remain in this initial state for several minutes. 

 If
a match is found, the Device Matches counter increases by one and
the Devices Not Found counter decreases by one. Also, “matched”
now appears in the Result column. 

 If
 Device Security does not find a match, it eventually displays a dash
in the Result column. 

 You might have to reload the User-defined
Static IP Devices page to see the updated data. 

 Previous 

 Upload a List of Static IP Devices 

 Next 

 Upload a List of Subnets with Only Static IP Addresses 

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

 Firewalls 

 PAN-OS 

 PAN-OS SD-WAN 

 Service Provider 

 VM-Series 

 SASE 

 Prisma Access 

 Strata Multitenant Cloud Manager 

 Device Security 

 Administration 

 Cloud-Delivered Security Services 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

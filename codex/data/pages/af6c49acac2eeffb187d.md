---
url: https://docs.paloaltonetworks.com/hardware/pa-220r-hardware-reference/before-you-begin/upgradedowngrade-considerations-for-firewalls-and-appliances
fetched_at: 2026-08-13T16:34:26Z
source: palo-alto-main
---

# Upgrade/Downgrade Considerations for Firewalls and Appliances Clear

Upgrade/Downgrade Considerations for Firewalls and Appliances 

 Home 

 EN

 Location 

 Documentation Home 

 Palo Alto Networks 

 Support 

 Live Community 

 Knowledge Base 

 Strata Copilot

 PA-220R Next-Gen Firewall Hardware Reference 

 : 
 Upgrade/Downgrade Considerations for Firewalls and Appliances 

 Updated on 

 Thu Aug 31 13:37:45 PDT 2023 

 Focus 

 Download PDF 

 Filter

 Expand all | Collapse all 

 Before You Begin 

 Upgrade/Downgrade Considerations for Firewalls and Appliances 

 Tamper Proof Statement 

 Third-Party Component Support 

 Product Safety Warnings 

 PA-220R Firewall Overview 

 PA-220R Front Panel 

 PA-220R Back Panel 

 PA-220R Status LEDs 

 Install the PA-220R Firewall 

 Install the PA-220R Firewall on a Flat Surface 

 Install the PA-220R Firewall on a DIN Rail 

 Install the PA-220R Firewall on a Wall 

 Install the PA-220R Firewall in a 19-inch Equipment Rack 

 Connect Power to a PA-220R Firewall 

 Prepare to Connect DC Power to a PA-220R Firewall 

 Connect DC Power to a PA-220R Firewall 

 PA-220R Firewall Specifications 

 PA-220R Physical Specifications 

 PA-220R Electrical Specifications 

 PA-220R Environmental Specifications 

 PA-220R Miscellaneous Specifications 

 PA-220R Firewall Hardware Compliance Statements Overview 

 PA-220R Firewall Hardware Compliance Statements 

 Updated on 

 Thu Aug 31 13:37:45 PDT 2023 

 Focus 

 Home 

 Firewalls & Appliances 

 PA-220R Next-Gen Firewall Hardware Reference 

 Before You Begin 

 Upgrade/Downgrade Considerations for Firewalls and Appliances 

 Download PDF 

 PA-220R Next-Gen Firewall Hardware Reference 

 Upgrade/Downgrade Considerations for Firewalls and Appliances 

 Table of Contents 

 Filter

 Expand all | Collapse all 

 Before You Begin 

 Upgrade/Downgrade Considerations for Firewalls and Appliances 

 Tamper Proof Statement 

 Third-Party Component Support 

 Product Safety Warnings 

 PA-220R Firewall Overview 

 PA-220R Front Panel 

 PA-220R Back Panel 

 PA-220R Status LEDs 

 Install the PA-220R Firewall 

 Install the PA-220R Firewall on a Flat Surface 

 Install the PA-220R Firewall on a DIN Rail 

 Install the PA-220R Firewall on a Wall 

 Install the PA-220R Firewall in a 19-inch Equipment Rack 

 Connect Power to a PA-220R Firewall 

 Prepare to Connect DC Power to a PA-220R Firewall 

 Connect DC Power to a PA-220R Firewall 

 PA-220R Firewall Specifications 

 PA-220R Physical Specifications 

 PA-220R Electrical Specifications 

 PA-220R Environmental Specifications 

 PA-220R Miscellaneous Specifications 

 PA-220R Firewall Hardware Compliance Statements Overview 

 PA-220R Firewall Hardware Compliance Statements 

 Upgrade/Downgrade Considerations for Firewalls and Appliances 

 Upgrade/downgrade considerations for firewalls and appliances. 

 The following table lists all hardware features that have upgrade or downgrade
 impact. Make sure you understand all upgrade/downgrade considerations before you
 upgrade or downgrade from the specified version of PAN-OS. 

 Feature Release Upgrade Considerations Downgrade Considerations 

 PA-7000 Log Forwarding Card (LFC) 10.0 
 If you are using an LFC with a PA-7000 Series
Firewall, when you upgrade to PAN-OS 10.0, you must configure the management
plane or dataplane interface for the service route because the LFC
ports do not support the requirements for the service route. We recommend
using the dataplane interface for the Data Services service route. 

 n/a 

 Upgrading a PA-7000 Series Firewall with a first
generation switch management card (PA-7050-SMC or PA-7080-SMC) PAN-OS 8.0 and later 
 Before upgrading the firewall, run the following
CLI command to check the flash drive’s status: debug system disk-smart-info disk-1 . 

 If
the value for attribute ID #232, Available_Reservd_Space 0x0000 ,
is greater than 20, then proceed with the upgrade. If the value
is less than 20, then contact support for assistance. 

 Before downgrading the firewall, run the
following CLI command to check the flash drive’s status: debug system disk-smart-info disk-1 . 

 If
the value for attribute ID #232, Available_Reservd_Space 0x0000 ,
is greater than 20, then proceed with the downgrade. If the value
is less than 20, then contact support for assistance. 

 Previous 

 Before You Begin 

 Next 

 Tamper Proof Statement 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

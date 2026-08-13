---
url: https://docs.paloaltonetworks.com/hardware/pa-400r-hardware-reference/before-you-begin/upgradedowngrade-considerations-for-firewalls-and-appliances
fetched_at: 2026-08-13T16:34:41Z
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

 PA-400R Series Next-Gen Firewall Hardware Reference 

 : 
 Upgrade/Downgrade Considerations for Firewalls and Appliances 

 Updated on 

 Fri Dec 12 15:26:24 PST 2025 

 Focus 

 Download PDF 

 Filter

 Expand all | Collapse all 

 Before You Begin 

 Safety and Compliance 

 Safety Warnings 

 Compliance Statements 

 Tamper Proof Statement 

 Third-Party Component Support 

 Parts List and Required Tools 

 PA-400R Series Firewall Overview 

 PA-400R Series Front Panel 

 PA-400R Series Back Panel 

 PA-400R Series Top and Bottom Panels 

 Interpret the LEDs on a PA-400R Series Firewall 

 Install the PA-400R Series Firewall 

 Install the PA-400R Series Firewall on a Flat Surface 

 Install the PA-400R Series Firewall on a Wall 

 Install the PA-400R Series Firewall on a Pole 

 Install the PA-400R Series Firewall in an Equipment Rack 

 Install the PA-400R Series Firewall on a DIN Rail 

 Connect Cables to the PA-400R Series Firewall 

 Connect Ethernet Cables to the PA-400R Series Firewall 

 Connect Fiber Cables to the PA-400R Series Firewall 

 Install Antennas on the PA-400R Series 5G Firewall 

 Insert a SIM Card into a PA-400R Series Firewall 

 Set Up a Connection to the Firewall 

 Connect Power to a PA-400R Series Firewall 

 Prepare to Connect Power to a PA-400R Series Firewall 

 Connect DC Power to a PA-400R Series Firewall 

 Connect AC Power to a PA-400R Series Firewall 

 PA-400R Series Firewall Specifications 

 Physical Specifications 

 Electrical Specifications 

 Environmental Specifications 

 Antenna Specifications 

 Miscellaneous Specifications 

 Updated on 

 Fri Dec 12 15:26:24 PST 2025 

 Focus 

 Home 

 Firewalls & Appliances 

 PA-400R Series Next-Gen Firewall Hardware Reference 

 Before You Begin 

 Upgrade/Downgrade Considerations for Firewalls and Appliances 

 Download PDF 

 PA-400R Series Next-Gen Firewall Hardware Reference 

 Upgrade/Downgrade Considerations for Firewalls and Appliances 

 Table of Contents 

 Filter

 Expand all | Collapse all 

 Before You Begin 

 Safety and Compliance 

 Safety Warnings 

 Compliance Statements 

 Tamper Proof Statement 

 Third-Party Component Support 

 Parts List and Required Tools 

 PA-400R Series Firewall Overview 

 PA-400R Series Front Panel 

 PA-400R Series Back Panel 

 PA-400R Series Top and Bottom Panels 

 Interpret the LEDs on a PA-400R Series Firewall 

 Install the PA-400R Series Firewall 

 Install the PA-400R Series Firewall on a Flat Surface 

 Install the PA-400R Series Firewall on a Wall 

 Install the PA-400R Series Firewall on a Pole 

 Install the PA-400R Series Firewall in an Equipment Rack 

 Install the PA-400R Series Firewall on a DIN Rail 

 Connect Cables to the PA-400R Series Firewall 

 Connect Ethernet Cables to the PA-400R Series Firewall 

 Connect Fiber Cables to the PA-400R Series Firewall 

 Install Antennas on the PA-400R Series 5G Firewall 

 Insert a SIM Card into a PA-400R Series Firewall 

 Set Up a Connection to the Firewall 

 Connect Power to a PA-400R Series Firewall 

 Prepare to Connect Power to a PA-400R Series Firewall 

 Connect DC Power to a PA-400R Series Firewall 

 Connect AC Power to a PA-400R Series Firewall 

 PA-400R Series Firewall Specifications 

 Physical Specifications 

 Electrical Specifications 

 Environmental Specifications 

 Antenna Specifications 

 Miscellaneous Specifications 

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

 Next 

 Safety and Compliance 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

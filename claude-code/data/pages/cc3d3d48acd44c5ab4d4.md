---
url: https://docs.paloaltonetworks.com/hardware/pa-400-hardware-reference/service-the-pa-400-firewall-hardware/interpret-the-leds-on-a-pa-400-firewall
fetched_at: 2026-08-13T16:34:40Z
source: palo-alto-main
---

# Interpret the LEDs on a PA-400 Series Firewall Clear

Interpret the LEDs on a PA-400 Series Firewall 

 Home 

 EN

 Location 

 Documentation Home 

 Palo Alto Networks 

 Support 

 Live Community 

 Knowledge Base 

 Strata Copilot

 PA-400 Series Next-Gen Firewall Hardware Reference 

 : 
 Interpret the LEDs on a PA-400 Series Firewall 

 Updated on 

 Jan 14, 2026 

 Focus 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 한국어 (Korean) 

 Русский (Russian) 

 Português (Portuguese) 

 Tiếng Việt (Vietnamese) 

 українська (Ukrainian) 

 Filter

 Expand all | Collapse all 

 Before You Begin 

 Safety and Compliance 

 Safety Warnings 

 Compliance Statements 

 Tamper Proof Statement 

 Third-Party Component Support 

 Parts List and Required Tools 

 PA-400 Series Firewall Overview 

 PA-400 Series Front Panel 

 PA-400 Series Back Panel 

 Install the PA-400 Series Firewall 

 Install the PA-400 Series Firewall on a Flat Surface 

 Install the PA-400 Series Firewall on a Wall 

 Install the PA-400 Series Firewall in a 19-inch Equipment Rack 

 Install the PA-400 Series Firewall Using the PAN-PA-400-RACKTRAY 

 Install Antennas on the PA-400 Series 5G Firewall 

 Insert a SIM Card into a PA-400 Series Firewall 

 Set Up a Connection to the Firewall 

 Connect Power to a PA-400 Series Firewall 

 Connect Power to a PA-400 Series Firewall 

 Connect Power to a PA-410 Firewall 

 Service the PA-400 Series Firewall Hardware 

 Interpret the LEDs on a PA-400 Series Firewall 

 Replace a Power Adapter on a PA-400 Series Firewall 

 PA-400 Series Firewall Specifications 

 Physical Specifications 

 Electrical Specifications 

 Environmental Specifications 

 Antenna Specifications 

 Miscellaneous Specifications 

 Updated on 

 Jan 14, 2026 

 Focus 

 Home 

 Firewalls & Appliances 

 PA-400 Series Next-Gen Firewall Hardware Reference 

 Service the PA-400 Series Firewall Hardware 

 Interpret the LEDs on a PA-400 Series Firewall 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 한국어 (Korean) 

 Русский (Russian) 

 Português (Portuguese) 

 Tiếng Việt (Vietnamese) 

 українська (Ukrainian) 

 PA-400 Series Next-Gen Firewall Hardware Reference 

 Interpret the LEDs on a PA-400 Series Firewall 

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

 PA-400 Series Firewall Overview 

 PA-400 Series Front Panel 

 PA-400 Series Back Panel 

 Install the PA-400 Series Firewall 

 Install the PA-400 Series Firewall on a Flat Surface 

 Install the PA-400 Series Firewall on a Wall 

 Install the PA-400 Series Firewall in a 19-inch Equipment Rack 

 Install the PA-400 Series Firewall Using the PAN-PA-400-RACKTRAY 

 Install Antennas on the PA-400 Series 5G Firewall 

 Insert a SIM Card into a PA-400 Series Firewall 

 Set Up a Connection to the Firewall 

 Connect Power to a PA-400 Series Firewall 

 Connect Power to a PA-400 Series Firewall 

 Connect Power to a PA-410 Firewall 

 Service the PA-400 Series Firewall Hardware 

 Interpret the LEDs on a PA-400 Series Firewall 

 Replace a Power Adapter on a PA-400 Series Firewall 

 PA-400 Series Firewall Specifications 

 Physical Specifications 

 Electrical Specifications 

 Environmental Specifications 

 Antenna Specifications 

 Miscellaneous Specifications 

 Interpret the LEDs on a PA-400 Series Firewall 

 View the status LEDs on the PA-400 Series firewall in
order to monitor the network connection, temperature, and other
device statuses. 

 The following table describes how to
interpret the status LEDs on the PA-400 Series firewalls. 

 The PA-410, PA-415, and PA-445 firewall only have PWR, STAT, and ALM front panel LEDs. They do
 not have any back panel LEDs. 

 LED Description 

 Front Panel LEDs 

 ( PA-410, PA-440, PA-450, and PA-460 ) 
 HA (High
 Availability) 

 ( PA-455 , PA-455-5G, and
 PA-415-5G ) 

 Green—The firewall is the active peer
in an active/passive configuration. 

 Yellow—The firewall is the passive peer in an active/passive configuration. 

 Off—High availability (HA) is not operational on this firewall. 

 In
an active/active configuration, the HA LED only indicates HA status
for the local firewall and has two possible states (green or off);
it does not indicate HA connectivity of the peer. Green indicates that
the firewall is either active-primary or active-secondary and off
indicates that the firewall is in any other state (for example,
non-functional or suspended). 

 ( PA-410, PA-440, PA-450, and PA-460 ) 
 STAT (Status) 

 ( PA-415 , PA-415-5G, PA-455, 
 PA-455-5G, and PA-445 ) 

 Green—The firewall is operating normally. 

 ( PA-410, PA-440, PA-450, and PA-460 ) Yellow—The firewall
is booting. 

 ( PA-415 , PA-415-5G, PA-455, 
 PA-455-5G, and PA-445 ) Red—The firewall is
 booting. 

 ( PA-410, PA-440, PA-450, and PA-460 ) 
 ALM (Alarm) 

 ( PA-415 , PA-415-5G, PA-455, 
 PA-455-5G, and PA-445 ) 

 Red—A hardware component failed, such
as a power adapter failure, a firewall failure that caused an HA
failover, a drive failure, or hardware is overheating and the temperature
is above the high temperature threshold. 

 Off—The firewall is operating normally. 

 TEMP (Temperature) 

 Green—The firewall temperature is normal. 

 Yellow—The firewall temperature is outside tolerance levels. 

 ( PA-410, PA-440, PA-450, and PA-460 ) 
 PWR (Power) 

 ( PA-415 , PA-415-5G, PA-455, 
 PA-455-5G, and PA-445 ) 

 Green—The firewall is powered on. 

 Off—The firewall is not powered on or an error has occurred
with the internal power system (for example, power is not within
tolerance levels). 

 SVC (Service) 

 This LED is disabled by default but can
be enabled by a remote administrator to illuminate the device for
a local operator. To enable the LED, use the following CLI command: 

 admin@PA-440> set system setting service-led enable yes 

 Off—The LED is disabled. 

 Blinking Red and Green—The firewall has been instructed to enable
the LED. 

 Temperature 

 ( PA-455-5G only ) 

 Green —The firewall temperature is normal. 

 Yellow —The firewall temperature is outside tolerance
 levels. 

 Fan 

 ( PA-455-5G only ) 

 Green —The fan is operating normally. 

 Yellow —The fan has failed. 

 Cellular 

 ( PA-415-5G and PA-455-5G 
 only ) 

 Green—The firewall has an active signal. 

 Red—The firewall does not have a signal or the antenna is not
 connected. 

 Off—The modem is disabled. 

 The PA-455-5G has two
 cellular LEDs — 1 and 2. Each corresponds to one of two active 5G
 modems in the firewall. 

 Ethernet port LEDs 

 PAN-OS 11.1 and later versions 

 Left LED—Blinking green indicates network activity. 

 Right LED—Solid green indicates a network link. 

 PAN-OS 10.2 and earlier versions 

 Left LED—Solid green indicates a network
link. 

 Right LED—Blinking green indicates network activity. 

 In the PA-455-5G, the link LED color varies based
 on the port speed. 

 Green—1Gbps 

 Yellow—10/100Mbps 

 If
you configure the link state to down on a
port, the LEDs on some active ports will not work. Similarly, if
the passive link state is set to shutdown ,
the HA link LEDs on the passive device in the HA pair will not work.
To ensure your LEDs display correctly, avoid configuring link states
to down or using the shutdown passive
link state unless needed for security reasons. 

 Back Panel LEDs 

 ( PA-440, PA-450, and PA-460 only )
PWR 1 and PWR 2 

 The following describes the power adapter
LEDs on the back of the firewall: 

 Green—The power input
is receiving power. 

 Off—The power input is not receiving power. 

 The
PWR LED on the front of the firewall shows green if one or both
power adapters are connected to the back power inputs. If both power
adapters are connected and one power adapter fails, the PWR LED
on the back of the firewall turns off and the ALM LED turns red. 

 Previous 

 Service the PA-400 Series Firewall Hardware 

 Next 

 Replace a Power Adapter on a PA-400 Series Firewall 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

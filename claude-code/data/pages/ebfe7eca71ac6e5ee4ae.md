---
url: https://docs.paloaltonetworks.com/hardware/pa-800-hardware-reference/pa-800-firewall-overview/pa-800-front-panel
fetched_at: 2026-08-13T16:35:37Z
source: palo-alto-main
---

# PA-800 Front Panel Clear

PA-800 Front Panel 

 Home 

 EN

 Location 

 Documentation Home 

 Palo Alto Networks 

 Support 

 Live Community 

 Knowledge Base 

 Strata Copilot

 PA-800 Series Next-Gen Firewall Hardware Reference 

 : 
 PA-800 Front Panel 

 Updated on 

 Aug 31, 2023 

 Focus 

 Download PDF 

 English 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 한국어 (Korean) 

 Русский (Russian) 

 Português (Portuguese) 

 Tiếng Việt (Vietnamese) 

 українська (Ukrainian) 

 مصر (Arabic) 

 ישראל (Hebrew) 

 Filter

 Expand all | Collapse all 

 Before You Begin 

 Upgrade/Downgrade Considerations for Firewalls and Appliances 

 Tamper Proof Statement 

 Third-Party Component Support 

 Product Safety Warnings 

 PA-800 Firewall Overview 

 PA-800 Front Panel 

 PA-800 Back-Panel 

 Install the PA-800 Series Firewall 

 Install the PA-800 Series Firewall in a Two-Post 19-inch Equipment Rack 

 Install the PA-800 Series Firewall in a Four-Post 19-inch Equipment Rack 

 Connect Power to a PA-800 Series Firewall Overview 

 Connect Power to a PA-800 Series Firewall 

 Service the PA-800 Series Firewall Hardware 

 Interpret the LEDs on a PA-800 Series Firewall 

 Replace a Power Supply on a PA-850 Firewall 

 PA-800 Series Firewall Specifications 

 PA-800 Series Physical Specifications 

 PA-800 Series Electrical Specifications 

 PA-800 Series Environmental Specifications 

 PA-800 Series Miscellaneous Specifications 

 PA-800 Series Firewall Compliance Statements Overview 

 PA-800 Series Firewall Compliance Statements 

 Updated on 

 Aug 31, 2023 

 Focus 

 Home 

 Firewalls & Appliances 

 PA-800 Series Next-Gen Firewall Hardware Reference 

 PA-800 Firewall Overview 

 PA-800 Front Panel 

 Download PDF 

 English 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 한국어 (Korean) 

 Русский (Russian) 

 Português (Portuguese) 

 Tiếng Việt (Vietnamese) 

 українська (Ukrainian) 

 مصر (Arabic) 

 ישראל (Hebrew) 

 PA-800 Series Next-Gen Firewall Hardware Reference 

 PA-800 Front Panel 

 Table of Contents 

 Filter

 Expand all | Collapse all 

 Before You Begin 

 Upgrade/Downgrade Considerations for Firewalls and Appliances 

 Tamper Proof Statement 

 Third-Party Component Support 

 Product Safety Warnings 

 PA-800 Firewall Overview 

 PA-800 Front Panel 

 PA-800 Back-Panel 

 Install the PA-800 Series Firewall 

 Install the PA-800 Series Firewall in a Two-Post 19-inch Equipment Rack 

 Install the PA-800 Series Firewall in a Four-Post 19-inch Equipment Rack 

 Connect Power to a PA-800 Series Firewall Overview 

 Connect Power to a PA-800 Series Firewall 

 Service the PA-800 Series Firewall Hardware 

 Interpret the LEDs on a PA-800 Series Firewall 

 Replace a Power Supply on a PA-850 Firewall 

 PA-800 Series Firewall Specifications 

 PA-800 Series Physical Specifications 

 PA-800 Series Electrical Specifications 

 PA-800 Series Environmental Specifications 

 PA-800 Series Miscellaneous Specifications 

 PA-800 Series Firewall Compliance Statements Overview 

 PA-800 Series Firewall Compliance Statements 

 PA-800 Front Panel 

 The following image shows the front panel
of the PA-800 Series firewall and the table describes each front
panel component. The only differences between the PA-820 (shown)
and PA-850 front panel is the model name and the Ethernet port speeds
as described in the table. 

 Item Component Description 

 1 

 Ethernet ports 1 through 4 

 Four RJ-45 10/100/1000Mbps ports for network traffic. 

 You
can set the link speed and duplex or choose auto-negotiate. 

 2 

 SFP ports 5 through 8 

 Four small form-factor pluggable (SFP) ports
for network traffic. 

 3 

 SFP/SFP+ ports 9 through 12 

 These ports are for network traffic and
their speed varies depending on your firewall and configuration. 
 PA-820
Firewalls 
 Four 1Gbps SFP ports; you cannot reconfigure these
ports. 
 PA-850 Firewalls 
 Four 1Gbps SFP ports or four
10Gbps SFP+ ports (default); you can specify which you want to use but
you cannot mix the two. 

 You can install up to 4 of the same
type transceivers (SFP or SFP+) as needed but if you install SFP
transceivers, then you also need to reconfigure ports 9 through
12 (as a group) to SFP using the command line interface (CLI). 

 To
confirm the current settings for these four ports, run the following
command: 

 admin@PA-850> show system setting ports-9-12-speed Device Ports 9-12 mode: sfp+ 

 The
output shows that the ports are set to SFP+. If the firewall is
not already set to the correct port type for your transceivers,
use the set system setting ports-9-12-speed command. For example,
if the output shows that these ports are set to SFP+ and you are
using SFP transceivers, then run the following commands to change
the port type from SFP+ to SFP and then restart the firewall to
apply the change: 

 admin@PA-850> set system setting ports-9-12-speed sfp 

 admin@PA-850> request restart system 

 4 

 HA1 and HA2 ports 

 Two RJ-45 10/100/1000Mbps ports for high-availability
control (HA1) and synchronization (HA2). 

 5 

 MGT port 

 Use this Ethernet 10/100/1000Mbps port to access
the management web interface and perform administrative tasks. The
firewall also uses this port for management services, such as retrieving
licenses and updating the threat and application signatures. 

 6 

 CONSOLE port (RJ-45) 

 Use this port to connect a management computer
to the firewall using a 9-pin serial to RJ-45 cable and terminal
emulation software. 

 The console connection provides access
to firewall boot messages, the Maintenance Recovery Tool (MRT),
and the command line interface (CLI). 

 If your management
computer does not have a serial port, use a USB-to-serial converter. 

 Use
the following settings to configure your terminal emulation software
to connect to the console port: 

 Data rate: 9600 

 Data bits: 8 

 Parity: none 

 Stop bits: 1 

 Flow control: None 

 7 

 USB port 

 Use the USB port to bootstrap the firewall. 

 Bootstrapping
enables you to provision the firewall with a specific PAN-OS configuration
and then license it and make it operational on your network. 

 8 

 CONSOLE port (Micro USB) 

 Use this port to connect a management computer
to the firewall using a standard Type-A USB-to-micro USB cable. 

 The
console connection provides access to firewall boot messages, the
Maintenance Recovery Tool (MRT), and the command line interface (CLI). 

 Refer
to Micro USB Console Port for
more information and to download the Windows driver or to learn
how to connect from a Mac or Linux computer. 

 9 

 LED status indicators 

 Six LEDs that indicate the status of the
firewall hardware components (see Interpret the LEDs on a PA-800 Series Firewall ). 

 Previous 

 PA-800 Firewall Overview 

 Next 

 PA-800 Back-Panel 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

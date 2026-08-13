---
url: https://docs.paloaltonetworks.com/prisma-sd-wan/ion-cli-reference/access-the-ion-cli-commands/assign-a-static-ip-address-using-the-console
fetched_at: 2026-08-13T17:29:37Z
source: palo-alto-main
---

# Assign a Static IP Address Using the Console Clear

Assign a Static IP Address Using the Console 

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

 Assign a Static IP Address Using the Console 

 Updated on 

 Tue Jun 02 09:34:24 PDT 2026 

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

 Tue Jun 02 09:34:24 PDT 2026 

 Focus 

 Home 

 Prisma SD-WAN 

 Access the ION Device CLI Commands 

 Assign a Static IP Address Using the Console 

 Download PDF 

 Prisma SD-WAN 

 Assign a Static IP Address Using the Console 

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

 Access through SSH 

 Next 

 Access the ION Device CLI Commands Using the Prisma SD-WAN Web Interface 

 Assign a Static IP Address Using the Console 

 Access the Prisma SD-WAN ION CLI commands through Console. 

 Access the Prisma SD-WAN ION device command-line
interface (CLI) using the console and assign a static IP address
to an unclaimed ION device controller or internet port. 

 Command-line interface (CLI) using the console and assigning a static
 IP address is only required to establish initial communication with the controller.
 Once a device is claimed, the controller will overwrite any further configuration
 changes done locally on the ION via the console or device toolkit. This is supported
 on all the Prisma SD-WAN ION Devices. 

 Connect an RJ-45 to USB cable to the AUX port
on the Prisma SD-WAN ION device. 

 Connect the other end of the RJ-45 to USB cable to your
computer and launch a terminal emulator. 

 Set the terminal or baud rate to 115200/8/n/1 on the
terminal window. 

 The Login menu displays the login prompt with the ION device
serial number. 

 <ION-device-serial-number> login: 

 Use the default user details username
 elem-admin / hackle628)bags for
 unclaimed devices. 

 CloudGenix 5.1.0-b23 
 30-001189-8149 login: elem-admin 
 Password: 
 Last login: Tue Nov 20 22:09:02 UTC 2018 on ttyS0 

 Configure the controller port or one of the internet
ports with the appropriate IP address, gateway address, and DNS server. 

 Assign a static IP address to the ION devices with controller ports
 using the config interface command. 

 # config interface controller1 ip static address=10.0.0.126/24 gw=10.0.0.1 dns=8.8.8.8 

 Verify your configuration using the dump
interface config command. 

 # dump interface config controller1
 Interface : controller 1 
 Description:
 ID : 15403462741430053 
 Type : port 
 Admin State : up 
 Alarms : enabled 
 MTU:1500 
 IP : static 
 Address : 10.0.0.126/24 
 Route : 0.0.0.0/0 via 10.0.0.1 metric 1
 DNS Server : 8.8.8.8

 # dump interface status controller1
 Interface: controller 1 
 Device : eth0 
 ID : 15403462741430053 
 MAC Address : ec:b9:07:00:12:3c 
 State: up 
 Last Change : 2018-11-20 21:55:40.785009014 +0000 UTC 
 Duplex: full
 Speed : 1000Mbps 
 Address : 10.0.0.126/24
 Route : 0.0.0.0/0 via 10.0.0.1 metric 0 
 DNS Server : 8.8.8.8 

 Use the config interface command to assign a static
 IP address to the internet port, this step is required for ION devices
 without controller ports. 

 # config interface 1 ip static address=24.4.5.2/30 gw=24.4.5.1 dns=8.8.8.8 

 Verify your configuration using the dump interface
 config command. 

 Verify the connection to the controller using the dump
controller status command. 

 # dump controller status
 Controller Connection : Partially Connected
 Number of Active Connections : 2
 -----------------------------------------------------------------
 tcp 0 0 10.0.0.126:57966 52.8.4.127:443 ESTABLISHED
 tcp 0 0 10.0.0.126:57338 52.8.4.127:443 ESTABLISHED
 ----------------------------------------------------------------- 

 Go to the Prisma SD-WAN web interface to claim your recently
configured ION device and assign it to a site. 

 After you change the device to the claimed state, change the default password to match your
 configured password. 

 Previous 

 Access through SSH 

 Next 

 Access the ION Device CLI Commands Using the Prisma SD-WAN Web Interface 

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

 CLI 

 Reference 

 Prisma SASE 

 Prisma SD-WAN ION CLI Reference 

 Prisma SD-WAN 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

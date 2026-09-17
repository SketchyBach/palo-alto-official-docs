---
url: https://docs.paloaltonetworks.com/panorama/11-1/panorama-admin/set-up-panorama/access-and-navigate-panorama-management-interfaces/log-in-to-the-panorama-cli
fetched_at: 2026-09-16T09:59:20Z
source: palo-alto-main
---

# Log in
to the Panorama CLI Clear

Updated on 

 Jul 16, 2026 

 Focus 

 Home 

 Panorama 

 Set Up Panorama 

 Access
and Navigate Panorama Management Interfaces 

 Log in
to the Panorama CLI 

 Download PDF 

 Panorama 

 Log in
to the Panorama CLI 

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

 Navigate the Panorama Web Interface 

 Next 

 Configure Administrative Access to Panorama 

 Log in
to the Panorama CLI 

 Where Can I Use This? What Do I Need? 

 NGFW (Managed by Panorama) 

 This is a core network security feature and does not have
 prerequisites 

 You can log in to the Panorama CLI using a
serial port connection or remotely using a Secure Shell (SSH) client. 

 Use SSH to log in to the Panorama CLI. 

 The same instructions apply to an M-Series appliance in
Log Collector mode. 

 Optionally, you can Configure an Administrator with SSH
 Key-Based Authentication for the CLI . 

 Ensure the following prerequisites are met: 

 You have a computer with network access to Panorama. 

 You know the Panorama IP address. 

 The Management interface supports SSH, which is the default
setting. If an administrator disabled SSH and you want to re-enable
it: select Panorama Setup Interfaces , click Management ,
select SSH , click OK ,
select Commit Commit to Panorama , and Commit your
changes to the Panorama configuration. 

 To access the CLI using SSH: 

 Enter the Panorama IP address
in the SSH client and use port 22. 

 Enter your administrative access credentials when prompted.
After you log in, the message of the day displays,
followed by the CLI prompt in Operational mode. For example: 

 admin@ABC_Sydney> 

 Use a serial port connection to log in to the Panorama
CLI. 

 Make sure that you have the following: 

 A null-modem serial cable that connects Panorama
to a computer with a DB-9 serial port 

 A terminal emulation program running on the computer 

 Use the following settings in the terminal emulation
software to connect: 9600 baud; 8 data bits; 1 stop bit; No parity;
No hardware flow control. 

 Enter your administrative access credentials when
prompted. After you log in, the message of the day displays, followed
by the CLI prompt in Operational mode. 

 Change to Configuration mode. 

 To switch to Configuration mode, enter the following command
at the prompt: 

 admin@ABC_Sydney> configure 

 The
prompt changes to admin@ABC_Sydney# . 

 Previous 

 Navigate the Panorama Web Interface 

 Next 

 Configure Administrative Access to Panorama

---
url: https://docs.paloaltonetworks.com/pan-os/10-1/pan-os-admin/firewall-administration/bootstrap-the-firewall/prepare-a-usb-flash-drive-for-bootstrapping-a-firewall
fetched_at: 2026-08-13T16:59:36Z
source: palo-alto-main
---

# Prepare a USB Flash Drive for Bootstrapping a Firewall Clear

Prepare a USB Flash Drive for Bootstrapping a Firewall 

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

 Prepare a USB Flash Drive for Bootstrapping a Firewall 

 Updated on 

 Mon Aug 03 13:41:44 PDT 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Next-Generation Firewall Docs 

 Getting Started 

 Administration 

 Networking 

 Quick Start 

 Reference 

 Incidents & Alerts 

 Release Notes 

 Select a Document 

 PAN-OS 12.2 

 PAN-OS 12.1 

 PAN-OS 11.2 

 PAN-OS 11.1 

 PAN-OS 11.0 (EoL) 

 PAN-OS 10.2 

 PAN-OS 10.1 (EoL) 

 PAN-OS 10.0 (EoL) 

 PAN-OS 9.1 (EoL) 

 PAN-OS 9.0 (EoL) 

 PAN-OS 8.1 (EoL) 

 Help 

 Select a Document 

 PAN-OS 12.2 

 PAN-OS 12.1 

 PAN-OS 11.2 

 PAN-OS 11.1 

 PAN-OS 10.2 

 PAN-OS 10.1 

 New Features 

 Updated on 

 Mon Aug 03 13:41:44 PDT 2026 

 Focus 

 Home 

 Next-Generation Firewall 

 Firewall Administration 

 Bootstrap the Firewall 

 Prepare a USB Flash Drive for Bootstrapping a Firewall 

 Download PDF 

 Next-Generation Firewall 

 Prepare a USB Flash Drive for Bootstrapping a Firewall 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Next-Generation Firewall Docs 

 Getting Started 

 Administration 

 Networking 

 Quick Start 

 Reference 

 Incidents & Alerts 

 Release Notes 

 Select a Document 

 PAN-OS 12.2 

 PAN-OS 12.1 

 PAN-OS 11.2 

 PAN-OS 11.1 

 PAN-OS 11.0 (EoL) 

 PAN-OS 10.2 

 PAN-OS 10.1 (EoL) 

 PAN-OS 10.0 (EoL) 

 PAN-OS 9.1 (EoL) 

 PAN-OS 9.0 (EoL) 

 PAN-OS 8.1 (EoL) 

 Help 

 Select a Document 

 PAN-OS 12.2 

 PAN-OS 12.1 

 PAN-OS 11.2 

 PAN-OS 11.1 

 PAN-OS 10.2 

 PAN-OS 10.1 

 New Features 

 Previous 

 Sample init-cfg.txt Files 

 Next 

 Bootstrap a Firewall Using a USB Flash Drive 

 Prepare a USB Flash Drive for Bootstrapping a Firewall 

 Prepare and configure a USB flash drive with the necessary files and folder structure
 to bootstrap a Palo Alto Networks firewall device. 

 Where Can I Use This? What Do I Need? 

 NGFW (Managed by PAN-OS or Panorama) 

 No prerequisites needed 

 You can use a USB flash drive to bootstrap
a physical firewall. However, to do so you must be running a PAN-OS
7.1.0 or later image and Reset
the Firewall to Factory Default Settings . For security reasons,
you can bootstrap a firewall only when it is in factory default
state or has all private data deleted. 

 Obtain serial numbers (S/Ns) and auth codes for
support subscriptions from your order fulfillment email. 

 Register S/Ns of new firewalls on the Customer Support
portal. 

 Go to support.paloaltonetworks.com, log
in, and select Assets Devices Register New Device Register device
using Serial Number or Authorization Code . 

 Follow the steps to register a firewall . 

 Click Submit . 

 Activate authorization codes on the Customer Support
portal, which creates license keys. 

 Go to support.paloaltonetworks.com, log
in, and select the Assets Devices on the left-hand navigation
pane. 

 For each device S/N you just registered, click the Action link
(the pencil icon). 

 Under Activate Licenses, select Activate Auth-Code . 

 Enter the Authorization code and
click Agree and Submit . 

 Add the S/Ns in Panorama. 

 Complete Step 1 in Add a Firewall as a Managed Device 
 in the Panorama Administrator’s Guide. 

 Create
the init-cfg.txt file. 

 Create the init-cfg.txt file, a mandatory file that provides
bootstrap parameters. The fields are described in Sample
init-cfg.txt Files . 

 If the init-cfg.txt file
is missing, the bootstrap process will fail and the firewall will
boot up with the default configuration in the normal boot-up sequence. 

 There
are no spaces between the key and value in each field; do not add
spaces because they cause failures during parsing on the management
server side. 

 You can have multiple init-cfg.txt files—one
each for different remote sites—by prepending the S/N to the file
name. For example: 

 0008C200105-init-cfg.txt 

 0008C200107-init-cfg.txt 

 If
no prepended filename is present, the firewall uses the init-cfg.txt
file and proceeds with bootstrapping. 

 ( Optional ) Create the bootstrap.xml file. 

 The optional bootstrap.xml file is a complete firewall
configuration that you can export from an existing production firewall. 

 Select Device Setup Operations Export named configuration snapshot . 

 Select the Name of the saved
or the running configuration. 

 Click OK . 

 Rename the file as bootstrap.xml . 

 Create and download the bootstrap bundle from the Customer
Support portal. 

 For a physical firewall, the bootstrap bundle requires
only the /license and /config directories. 

 Use one of the
following methods to create and download the bootstrap bundle: 

 Use Method 1 to create a bootstrap bundle specific to
a remote site (you have only one init-cfg.txt file). 

 Use Method 2 to create one bootstrap bundle for multiple sites. 

 Method 1 

 On your local system, go to support.paloaltonetworks.com
and log in. 

 Select Assets . 

 Select the S/N of the firewall you want to bootstrap. 

 Select Bootstrap Container . 

 Click Select . 

 Upload and Open the init-cfg.txt
file you created. 

 ( Optional ) Select the bootstrap.xml file
you created and Upload Files . 

 You must use a bootstrap.xml file
from a firewall of the same model and PAN-OS version. 

 Select Bootstrap Container Download to
download a tar.gz file named bootstrap_<S/N>_<date>.tar.gz to
your local system. This bootstrap container includes the license
keys associated with the S/N of the firewall. 

 Method 2 

 Create a tar.gz
file on your local system with two top-level directories: /license
and /config. Include all licenses and all init-cfg.txt files with
S/Ns prepended to the filenames. 

 The license key files you
download from the Customer Support portal have the S/N in the license
file name. PAN-OS checks the S/N in the file name against the firewall
S/N while executing the bootstrap process. 

 Import
the tar.gz file you created (to a firewall running a PAN-OS 7.1.0
or later image) using Secure Copy (SCP) or TFTP. 

 Access the CLI and enter one of the following commands: 

 tftp import bootstrap-bundle file <path and filename> from <host IP address> 
 For
example: 
 tftp import bootstrap-bundle file /home/userx/bootstrap/devices/pa5000.tar.gz from 10.1.2.3 

 scp import bootstrap-bundle from <<user>@<host>:<path to file>> 
 For
example: 
 scp import bootstrap-bundle from userx@10.1.2.3:/home/userx/bootstrap/devices/pa200_bootstrap_bundle.tar.gz 

 Prepare the USB flash drive. 

 Insert the USB flash drive into the firewall
that you used in the prior step. 

 Enter the following CLI operational command, using
your tar.gz filename in place of “ pa5000.tar.gz ”.
This command formats the USB flash drive, unzips the file, and validates
the USB flash drive: 

 request system bootstrap-usb prepare from pa5000.tar.gz 

 Press y to continue. The following
message displays when the USB drive is ready: 

 USB prepare completed successfully. 

 Remove the USB flash drive from the firewall. 

 You can prepare as many USB flash drives as needed. 

 Deliver the USB flash drive to your remote site. 

 If you used Method
2 to create the bootstrap bundle, you can use the same USB
flash drive content for bootstrapping firewalls at multiple remote
sites. You can translate the content into multiple USB flash drives
or a single USB flash drive used multiple times. 

 Previous 

 Sample init-cfg.txt Files 

 Next 

 Bootstrap a Firewall Using a USB Flash Drive 

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

 Cloud Management for NGFWs 

 Cloud NGFW for AWS 

 Cloud NGFW for Azure 

 CN-Series 

 Firewalls 

 PAN-OS 

 PAN-OS SD-WAN 

 Service Provider 

 VM-Series 

 SASE 

 Prisma Access 

 Strata Multitenant Cloud Manager 

 AI-Powered ADEM 

 Prisma Access Monitoring and Visibility 

 Prisma SD-WAN 

 ION Devices 

 Next-Generation CASB 

 Cloud-Delivered Security Services 

 Advanced WildFire 

 Advanced URL Filtering 

 Advanced Threat Prevention 

 Advanced DNS Security 

 Device Security 

 Enterprise DLP 

 SaaS Security 

 Network Security 

 Shared Policy for NGFWs and Prisma Access 

 Visibility & Monitoring 

 Dashboards 

 Incidents and Alerts 

 Reports 

 Autonomous DEM 

 Best Practices 

 Best Practices Library 

 Experts Corner 

 Solutions Docs from Product Experts 

 Network Security 

 PAN-OS 

 Next-Generation Firewall 

 Administration 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

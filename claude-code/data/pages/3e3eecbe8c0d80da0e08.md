---
url: https://docs.paloaltonetworks.com/panorama/getting-started/set-up-panorama/set-up-the-panorama-virtual-appliance/install-the-panorama-virtual-appliance/set-up-panorama-on-oracle-cloud-infrastructure
fetched_at: 2026-08-13T17:18:41Z
source: palo-alto-main
---

# Set Up Panorama on Oracle Cloud Infrastructure (OCI) Clear

Set Up Panorama on Oracle Cloud Infrastructure (OCI) 

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

 Set Up Panorama on Oracle Cloud Infrastructure (OCI) 

 Updated on 

 Tue Jul 14 08:53:35 PDT 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Panorama Docs 

 Getting Started 

 Administration 

 New Features 

 Updated on 

 Tue Jul 14 08:53:35 PDT 2026 

 Focus 

 Home 

 Panorama 

 Set Up Panorama 

 Set Up the Panorama Virtual Appliance 

 Install the Panorama Virtual Appliance 

 Set Up Panorama on Oracle Cloud Infrastructure (OCI) 

 Download PDF 

 Panorama 

 Set Up Panorama on Oracle Cloud Infrastructure (OCI) 

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

 Install Panorama on Hyper-V 

 Next 

 Perform Initial Configuration of the Panorama Virtual Appliance 

 Set Up Panorama on Oracle Cloud Infrastructure (OCI) 

 Set up and install a Panorama™ virtual appliance on Oracle
Cloud Infrastructure (OCI). 

 Where Can I Use This? What Do I Need? 

 NGFW (Managed by Panorama) 

 Device management licence 

 Support license 

 Panorama Virtual Appliance license (serial number) 

 Customer Support Portal (CSP) Account 

 Set up a Panorama™ virtual appliance
on Oracle Cloud Infrastructure (OCI) to centrally managed the configuration
of physical and VM-Series firewalls. 

 Upload the Panorama Virtual Appliance Image to OCI 

 Complete the following procedure to upload a Panorama qcow2 file for KVM and
 create a custom image that you need to launch the Panorama virtual appliance.
 Uploading and creating the image is required only once. You can use the same
 image for all subsequent deployments of the Panorama virtual appliance. 

 Download the Panorama qcow2 file for KVM from the Palo Alto Networks
 Customer Support Portal (CSP). 

 Log in to the Palo Alto Networks CSP . 

 Select Updates Software Updates and select Panorama Base
 Images from the software updates filter
 drop-down. 

 Download the latest version of the
 Panorama-KVM qcow2 image. 

 Log in to the Oracle Cloud Infrastructure
 console. 

 Create a storage bucket for the qcow2 file. 

 Select Object Storage Object Storage and Create Bucket . 

 Enter a descriptive Bucket Name . 

 For the Storage Tier, select Standard . 

 Create Bucket . 

 Upload the qcow2 image to the OCI storage bucket. 

 Click the storage bucket you created in the previous step to view
 the bucket details. 

 Click Upload and select the qcow2 image you
 downloaded from the Palo Alto Networks CSP. 

 Upload the image. 

 Create a pre-authenticated request for the qcow2 file. 

 This is required to create the object URL used in the creation of the
 custom image for the Panorama virtual appliance. 

 Select Object Storage Object Storage and click the storage bucket you created in the
 previous step. 

 Select Pre-Authenticated Requests Create Pre-Authenticated Request . 

 Enter a descriptive Name for your
 Pre-Authenticated Request. 

 Select Object and enter the qcow2 image name
 for the Object Name . 

 Create Pre-Authenticated Request . 

 For the Access Type, select Permit object reads and
 writes . 

 Enter an Expiration date and time. 

 Create Pre-Authenticated Request . 

 In the Pre-Authenticated Request Details, copy the
 Pre-Authenticated Request URL. 

 The Pre-Authenticated Request URL is required to create the
 custom image and must be copied when displayed to you. 

 The Pre-Authenticated Request URL is only displayed after the
 request is created and is not shown again. 

 Close the Pre-Authenticated Request Details
 after you copy the URL. 

 Import the qcow2 file and create a custom Panorama virtual appliance
 image. 

 Select Compute Custom Images and Import Image . 

 Enter a descriptive Name for your
 image. 

 Select Import from an Object Storage URL and
 paste the object storage URL. 

 For the Image type, select QCOW2 . 

 For the Launch Mode, select Paravirtualized
 Mode . 

 Import Image . 

 Install Panorama on Oracle Cloud Infrastructure (OCI) 

 Create a Panorama™ virtual appliance instance on Oracle Cloud Infrastructure
 (OCI). An OCI instance supports a single NIC by default. You must manually
 upload a Panorama virtual appliance qcow2 image downloaded from the Palo Alto
 Networks Customer Supported Portal (CSP) to OCI to successfully install the
 Panorama virtual appliance on OCI. 

 A Panorama virtual appliance deployed on OCI is Bring Your Own License (BYOL),
 supports all deployment modes (Panorama, Log Collector, and Management Only),
 and shares the same processes and functionality as the M-Series hardware
 appliances. For more information on Panorama modes, see Panorama Models . 

 A machine running a Linux operating system is required successfully install the
 Panorama on OCI. To successfully install Panorama on OCI, you must generate a
 .pub key using OpenSSH. Additionally, you can
 only use a Linux machine to log into the Panorama CLI for the initial network
 configuration. 

 Review the Setup Prerequisites for the Panorama Virtual Appliance to determine the virtual
 resources required for your needs. The virtual resources requirement for the
 Panorama virtual appliance is based on the total number of firewalls managed by
 the Panorama virtual appliance and the required Logs Per Second (LPS) for
 forwarding logs from your managed firewalls to your Log Collector. 

 Under-provisioning the Panorama virtual appliance will impact management
 performance. This includes the Panorama virtual appliance becoming slow or
 unresponsive depending on how under-provisioning the Panorama virtual
 appliance is. 

 Log in to the Oracle Cloud Infrastructure
 console. 

 Set up the Virtual Cloud Network (VCN) for your network needs. 

 Whether you launch the Panorama virtual appliance in an existing VCN or
 you create a new VCN, the Panorama virtual appliance must be able to
 receive traffic from other instances in the VCN and perform inbound and
 outbound communication between the VCN and the internet as needed. 

 Refer to the OCI VCN documentation for more
 information. 

 Configure a VCN or use an
 existing VCN. 

 Verify that the network and security components are appropriately
 defined. 

 Create an internet gateway to enable internet access to
 the subnet of your Panorama virtual appliance. Internet
 access is required to install software and content
 updates, activate licenses, and leverage Palo Alto
 Networks cloud services. Otherwise, you must manually
 install updates and activate licenses. 

 If the Panorama virtual appliance instance is part of a
 private subnet, you can configure a NAT gateway to
 enable only outbound internet access for the subnet. 

 Create subnets. Subnets are segments of the IP address
 range assigned to the VCN in which you can launch OCI
 instances. It is recommended that the Panorama virtual
 appliance belong to the management subnet so that you
 can configure it to access the internet if needed. 

 Add routes to the route table for a private subnet to
 ensure traffic can be routed across subnets in the VCN
 and from the internet if applicable. 

 Ensure you create routes between subnets to allow
 communication between: 

 Panorama, managed firewalls, and Log
 Collectors. 

 ( Optional ) Panorama and the
 internet. 

 Ensure that the following ingress security rules are
 allowed for the VCN to manage VCN traffic. The ingress
 traffic source for each rule is unique to your
 deployment topology. 

 See Ports Used for
 Panorama for more information. 

 Allow SSH (port 22 )
 traffic to enable access to the Panorama CLI. 

 Allow HTTPS (port 443 and
 28270 ) traffic to enable
 access to the Panorama web interface. 

 Allow traffic on port 3978 
 to enable communication between Panorama, manage
 firewalls, and managed Log Collectors. This port
 is also used by Log Collectors to forward logs to
 Panorama. 

 Allow traffic on port
 28443 to enable managed
 firewalls to get software and content updates from
 Panorama. 

 Select Compute Instances and Create Instance . 

 Enter a descriptive Name for the Panorama virtual
 appliance image. 

 Select the Availability domain . 

 Select the Palo Alto Networks Panorama image. 

 See Upload the Panorama Virtual Appliance Image to OCI to upload and maintain your own
 Panorama virtual appliance Custom Image on OCI. 

 Under Image and shape, select Change
 Image . 

 For the Image Source, select Partner
 Image . 
 If you maintain your own Panorama virtual appliance image, select
 Custom Image instead and select the
 Panorama virtual appliance image you uploaded to OCI. 

 Search for Palo Alto Networks Panorama and
 select (check) the image. 

 Skip this step if you selected Custom
 Image in the previous step. 

 PAN-OS 10.2.0 is the default PAN-OS version. 

 Select Image . 

 Configure the instance resources. 

 Refer to the Setup Prerequisites for the Panorama Virtual Appliance for more information
 for the minimum resources required based on your Panorama usage
 needs. 

 Under Image and shape, select Change
 Shape . 

 Select the shape with number of CPUs, amount of RAM, and number of
 interfaces you require. 

 Select Shape . 

 Configure the instance Networking settings. 

 For the Network, Select existing virtual cloud
 network and select the VCN. 

 For the Subnet, Select existing subnet and
 select the subnet. 

 It is recommended to deploy the Panorama virtual appliance
 instance in a management subnet to safely allow internet access
 if needed. 

 ( Optional ) For the Public IP Address, select
 Assign a public IPv4 address if you want
 to make the Panorama virtual appliance accessible from outside the
 VCN. 

 Configure the Panorama virtual appliance instance boot volume. 

 For the Boot volume, specify a custom boot volume
 size . 

 For the Boot volume size, enter 81 . 

 Create the Panorama virtual appliance image. 

 Log in to the Panorama virtual appliance CLI from the OCI console. 

 Generate a SSH Key for Panorama on
 OCI . 

 In the OCI console, select
 Instances and select the Panorama virtual
 appliance instance. 

 Select Console Connection and
 Create Console Connection . 

 Select Upload public key files (.pub) and
 upload the public SSH key you generated to Create Console
 Connection . 

 In the Instance Details screen, expand the Console Connection
 options and Copy Serial Connection for
 Linux/Mac . 

 On your Linux machine, open a terminal and paste the serial
 connection. 

 Configure a new administrative password for the Panorama virtual
 appliance. 

 You must configure a unique administrative password before you can access
 the web interface or CLI of the Panorama virtual appliance. The new
 password must be a minimum of eight characters and include a minimum of
 one lowercase character, one uppercase character, and one number or
 special character. 

 When you first log in to the Panorama CLI, you are prompted to enter the
 Old Password and the New
 Password for the admin user
 before you can continue. 

 Configure the system IP address settings for the Panorama virtual
 appliance. 

 Configure the initial network settings for the Panorama virtual
 appliance. 

 admin> configure 

 admin# set deviceconfig system type static 

 admin# set deviceconfig system ip-address <instance-private-IP address> netmask <netmask> default-gateway <default-gateway-IP> 

 admin# set deviceconfig system dns-setting servers primary <primary-dns-IP> 

 admin# set deviceconfig system dns-setting servers secondary <secondary-dns-IP> 

 admin# commit 

 Verify you can log in to the Panorama
 web interface . 

 If you cannot log in to the Panorama web interface, review your
 route table and VCN security rules to ensure the correct routes
 and security rules are created. 

 Register the Panorama virtual appliance and activate the device management
 license and support licenses. 

 ( VM Flex Licensing Only ) Provisioning the Panorama Virtual
 Appliance Serial Number . 

 When leveraging VM Flex licensing, this step is required to
 generate the Panorama virtual appliance serial number needed to
 register the Panorama virtual appliance with the Palo Alto
 Networks Customer Support Portal (CSP). 

 Register Panorama . 

 You must register the Panorama virtual appliance using the serial
 number provided by Palo Alto Networks in the order fulfillment
 email. 

 This step is not required when leveraging VM Flex licensing as
 the serial number is automatically registered with the CSP when
 generated. 

 Activate the firewall management license. 

 Activate/Retrieve a Firewall
 Management License when the Panorama Virtual
 Appliance is Internet-connected . 

 Activate/Retrieve a Firewall
 Management License when the Panorama Virtual
 Appliance is not Internet-connected . 

 Activate a Panorama Support License . 

 Complete configuring the Panorama virtual appliance for your deployment
 needs. 

 For Panorama in Log Collector Mode. 

 Add a Virtual Disk to Panorama on Oracle Cloud Infrastructure (OCI) as
 needed. 

 Adding at least one virtual logging disk is required
 before you can change the Panorama virtual appliance to
 Log Collector mode. 

 Begin at Step 6 to switch to Log Collector
 mode. 

 Enter the Public IP address of the Dedicated Log
 Collector when you add the Log Collector as a
 managed collector to the Panorama management server.
 You cannot specify the IP
 Address ,
 Netmask , or
 Gateway . 

 For Panorama in Panorama mode. 

 Add a Virtual Disk to Panorama on Oracle Cloud Infrastructure (OCI) . 

 Adding at least one virtual logging disk is required
 before you can change the Panorama virtual appliance to
 Panorama mode. 

 Set up a Panorama Virtual Appliance in Panorama Mode . 

 Configure a Managed
 Collector . 

 For Panorama in Management Only mode. 

 Set up a Panorama Virtual
 Appliance in Management Only Mode . 

 Configure a Managed
 Collector to add a Dedicated Log Collector to
 the Panorama virtual appliance. 

 Management Only mode does not support local log
 collection, and requires a Dedicated Log Collector to
 store managed device logs. 

 Generate a SSH Key for Panorama on OCI 

 To connect to the Panorama™ virtual appliance installed on Oracle Cloud
 Infrastructure (OCI), you must generate a public and private SSH key on a Linux
 machine. You use the generated SSH key to log in to the Panorama CLI to set up a
 new administrative password and configure the Panorama network settings. 

 A Linux machine is required to generate the SSH key and access the Panorama
 CLI for the initial configuration. Generating a SSH from OCI or third-party
 applications such as PuTTygen is not supported. 

 Open the terminal on your Linux machine. 

 Navigate to the hidden .ssh directory. 

 admin:~$ cd ~/.ssh 

 Generate an SSH key in the .ssh 
 directory. 

 admin:~/.ssh$ ssh-keygen 

 When prompted, save the key in the default
 .ssh directory. A password for the key
 is optional. 

 The default name for the private key is
 id_rsa and the default name for the
 public key is id_rsa.pub . 

 Copy the public key from the .ssh directory to
 your home directory. 

 This step is required to upload the public key to OCI. 

 admin: ~/.ssh$ cp id_rsa.pub ~ 

 Previous 

 Install Panorama on Hyper-V 

 Next 

 Perform Initial Configuration of the Panorama Virtual Appliance 

 On This Page 

 Activation and Onboarding 

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

 Panorama 

 Service Provider 

 VM-Series 

 Plugins 

 SASE 

 Prisma Access 

 Prisma SASE Multitenant Platform 

 AI-Powered ADEM 

 Prisma Access Monitoring & Visibility 

 Prisma SD-WAN 

 ION Devices 

 Next-Generation CASB 

 Cloud-Delivered Security Services 

 Advanced WildFire 

 Advanced URL Filtering 

 Advanced Threat Prevention 

 Advanced DNS Security 

 AI Access Security 

 Device Security 

 Enterprise DLP 

 SaaS Security 

 Network Security 

 Shared Policy for NGFWs and Prisma Access 

 IPSec VPN 

 Security Policy 

 Quantum Security 

 Endpoints 

 GlobalProtect 

 Remote Browser Isolation 

 Prisma Access Agent 

 Visibility & Monitoring 

 Dashboards 

 Incidents and Alerts 

 Reports 

 Autonomous DEM 

 FedRAMP 

 Prisma SASE for FedRAMP 

 Autonomous DEM for FedRAMP 

 Prisma SD-WAN Experts Corner 

 Network Policy 

 QoS Whitepaper 

 Security Architecture Whitepaper 

 External Antennas for ION-C Series 

 Dynamic Path Selection 

 Best Practices 

 Best Practices Library 

 Experts Corner 

 Solutions Docs from Product Experts 

 Resources 

 All Products A - Z 

 All Release Notes 

 Compatibility Matrix 

 Experts Corner 

 Network Security Platform 

 Security Policy 

 Decryption 

 Device-ID 

 IPSec VPN 

 Quality of Service 

 Quantum Security 

 11.1 & Later 

 Next-Generation Firewall 

 Getting Started 

 Panorama 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

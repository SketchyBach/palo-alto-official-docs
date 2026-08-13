---
url: https://docs.paloaltonetworks.com/panorama/getting-started/set-up-panorama/set-up-the-panorama-virtual-appliance/increase-the-system-disk-on-the-panorama-virtual-appliance/increase-the-system-disk-for-panorama-on-azure
fetched_at: 2026-08-13T17:18:37Z
source: palo-alto-main
---

# Increase the System Disk for Panorama on Azure Clear

Increase the System Disk for Panorama on Azure 

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

 Increase the System Disk for Panorama on Azure 

 Updated on 

 Jul 14, 2026 

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

 Jul 14, 2026 

 Focus 

 Home 

 Panorama 

 Set Up Panorama 

 Set Up the Panorama Virtual Appliance 

 Increase the System Disk on the Panorama Virtual Appliance 

 Increase the System Disk for Panorama on Azure 

 Download PDF 

 Panorama 

 Increase the System Disk for Panorama on Azure 

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

 Increase the System Disk for Panorama on AWS 

 Next 

 Complete the Panorama Virtual Appliance Setup 

 Increase the System Disk for Panorama on Azure 

 Migrate the existing system 81GB system disk to a 224GB system disk for Panorama
 deployed on Azure. 

 For the minimum resource requirements for the Panorama virtual appliance, see Setup Prerequisites for the Panorama Virtual
 Appliance . 

 Save and Export Panorama and Firewall
 Configurations . 

 Save and export your Panorama and firewall configuration to
 ensure you can recover Panorama if you encounter any issues. 

 Power off the Panorama virtual appliance. 

 Add a 224GB system disk to replace the default 81GB system disk. 

 Log in to the Azure Console. 

 Expand Settings and click Disks > Create and attach a
 new disk . 

 Enter a Disk name to the new disk you are creating. 

 Select the Storage type and Encryption similar to the
 ones you had selected for the 81 GB disk. 

 Enter 224 as the Size (GB) . 

 Select Read/write option for Host caching . 

 Click Apply . 

 Check the disk size in the Panorama. 

 Initiate disk cloning. 

 Initiate disk cloning by executing the following command: 

 request system clone-system-disk target <disk
 name> 

 Verify the ongoing cloning status from the console. 

 Shutdown the Panorama VM from the Azure console. 

 Detach the data disk from the Panorama VM to which it was added initially, and
 convert the data disk to OS disk using powershell commands. 

 $managedDisk = Get-AzDisk -DiskName pnrma_new_data_disk -ResourceGroupName arus-cpt-pnrma-rg
# Create disk configuration for the copy
$diskConfig = New-AzDiskConfig -SourceResourceId $managedDisk.Id -Location $managedDisk.Location -CreateOption Copy -OsType Linux
New-AzDisk -Disk $diskConfig -DiskName pnrma_new_data_os_disk -ResourceGroupName arus-cpt-pnrma-rg 

pnrma_new_data_disk - name of the Data Disk that was initially created in the previous step
arus-cpt-pnrma-rg - name of the resource group where disk is present
pnrma_new_data_os_disk - name of the new os disk that will be created

 $managedDisk = Get-AzDisk -DiskName pnrma_new_data_disk
 -ResourceGroupName arus-cpt-pnrma-rg 

 $diskConfig = New-AzDiskConfig -SourceResourceId $managedDisk.Id
 -Location $managedDisk.Location -CreateOption 

 New-AzDisk -Disk $diskConfig -DiskName pnrma_new_data_os_disk
 -ResourceGroupName arus-cpt-pnrma-rg 

 Verify the OS disk you created. 

 Create an Azure compute gallery. 

 From the Azure Console home page, click Azure compute
 galleries . 

 In the Azure compute gallery page, Click Create . 

 Select a Resource group . 

 You may retain the default settings for Sharing and Tags 
 tabs. 

 Click Review+create . 

 Add a VM image definition from the Azure compute gallery. 

 Add the following details: 

 Subscription 

 Resource Group 

 Region 

 Target Azure Compute Gallery 

 VM image definition name 

 OS type 

 Security type 

 VM generation 

 Higher storage performance with NVMe 

 Accelerated networking 

 VM architecture 

 Hibernation supported 

 OS state 

 Publisher - Enter publisher as paloaltonetworks 

 Offer - Enter offer as panorama 

 SKU - Enter SKU as byol 

 Ensure that the region, publisher, SKU, offer, and
 VM-Deployment sections are similar to that of the
 existing Panorama. You can view this information in the
 Source image details section of the VM Overview page in
 Azure Portal page. 

 The OS disk must be the one you created in step 5. Ensure
 that you select this OS disk under the version tab while
 creating a VM definition. 

 The CPU and memory values must be the same as that of the
 Panorama. 

 Click Review+Create to create the Azure compute gallery. 

 Create a VM from the Azure compute gallery. 

 Click the VM definition and click Create VM to create a VM from
 the Azure compute gallery. This will create a new Panorama instance
 which will boot from the VM definition. 

 Configure the Basics settings. 

 When choosing the image, select the relevant Gallery Image
 definition that was created in previous steps. 

 Ensure that the Azure infrastructure-related options align
 with the existing Panorama configuration. 

 Add the Disks settings and ensure that the OS Disk selected is 224GB or
 more. 

 Add the Networking settings similar to that of the existing Panorama.
 This will bring up a new panorama with the resized OS disk
 details. 

 Execute the following command to verify if the panrepo folder size has
 increased: 

 Show system disk space 

 The new Panorama will have a different private IP address. You need to
 configure it with the same IP address as the existing Panorama. To make the
 existing Panorama's IP address available, assign a temporary, unused IP address
 to the existing Panorama. The existing Panorama's IP address can only be changed
 when the VM is shut down. From the Azure portal, assign the existing Panorama's
 IP address to the new Panorama's interface. Once the IP addresses are swapped,
 the Network Interface Card (NIC) will reset, and the new Panorama will then have
 the IP address of the existing Panorama. 

 To change private/public IP of the Panorama, click PanoramaVM >
 Network Settings > IP configurations . Select the network
 for which you need to change the IP address and click Edit . 

 If your existing Panorama had any data disks, detach them and then reattach
 them to the new Panorama. Finally, boot the Panorama. The new Panorama should
 now have all devices connected and function identically to the existing
 Panorama. 

 For an Active-Passive Panorama setup, apply these steps first to the
 Passive Panorama, then repeat them for the Active Panorama. 

 In case of a Cloud NGFW set-up, the newly deployed Panorama
 instance will be assigned a different Private IP address. It is
 necessary to configure this new instance to use the same IP address as
 the existing Panorama. 

 To make the existing Panorama IP available to the new Panorama
 instance, you must first assign a temporary, unused IP address to the
 current Panorama. The existing Panorama IP address can only be changed
 while the VM is shut down. 

 Assign the existing Panorama IP to the new Panorama interface
 from the Azure portal. Interchanging the IP addresses will cause the NIC
 to reset, resulting in the new Panorama instance adopting the IP address
 of the existing Panorama instance. After replacing the existing
 Panorama, complete the following steps: 

 If the original Panorama had any data disks, detach
 them and reattach them to the new Panorama instance. 

 Start the new Panorama instance. The new Panorama should now be
 fully functional, with all devices connected, and operating the same
 way as the original Panorama. 

 After the Panorama is back online, you must re-fetch the device
 certificate and licenses. 

 Previous 

 Increase the System Disk for Panorama on AWS 

 Next 

 Complete the Panorama Virtual Appliance Setup 

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

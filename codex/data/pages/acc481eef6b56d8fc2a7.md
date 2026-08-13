---
url: https://docs.paloaltonetworks.com/vm-series/deployment/private-cloud/set-up-the-vm-series-firewall-on-nsx/launch-the-vm-series-firewall
fetched_at: 2026-08-13T17:41:39Z
source: palo-alto-main
---

# Deploy the VM-Series Firewall Clear

Deploy the VM-Series Firewall 

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

 Deploy the VM-Series Firewall 

 Updated on 

 Jun 19, 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 VM-Series Firewall Docs 

 Activation & Onboarding 

 Getting Started 

 Upgrade 

 Deployment 

 Select a Document 

 Public Cloud 

 Private Cloud 

 Updated on 

 Jun 19, 2026 

 Focus 

 Home 

 VM-Series 

 VM-Series Firewall on VMware NSX-T 

 Deploy the VM-Series Firewall 

 Download PDF 

 VM-Series 

 Deploy the VM-Series Firewall 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 VM-Series Firewall Docs 

 Activation & Onboarding 

 Getting Started 

 Upgrade 

 Deployment 

 Select a Document 

 Public Cloud 

 Private Cloud 

 Previous 

 Configure the Service Definition on Panorama 

 Next 

 Direct Traffic to the VM-Series Firewall 

 Deploy the VM-Series Firewall 

 Learn how to deploy the VM-Series firewall on VMware
NSX-T. 

 Where Can I Use
 This? What Do I Need? 

 VMware NSX 

 VM-Series Firewall License (BYOL) 

 Panorama 

 VM-Series plugin 

 Panorama plugin for NSX 

 After completing the configuration on Panorama, perform the following procedure to launch the
 VM-Series firewall in your NSX-T data center. 

 When deploying the VM-Series firewall
on NSX-T in high availability, both firewalls are deployed to the
same Device Group and Template Stack. 

 Log in to NSX-T Manager. 

 Select System Service
Deployments Deployment . 

 Select your service definition from the Partner
Service drop-down. 

 Click Deploy Service . 

 Enter a descriptive Service Deployment Name for
your VM-Series firewall. 

 Select a tier-0 or tier-1 router under Attachment
 Points . NSX-T Manager attaches the VM-Series firewall to the
 selected router and redirects traffic passing through that router to the
 VM-Series firewall for inspection. Select a router with no service insertion
 attached. 

 Select a Compute Manager . The compute manager is the
 vCenter server managing your data center. 

 Select a Cluster . You can deploy
the VM-Series firewall on any cluster that does not include any
Edge Transport Nodes. 

 Select a Datastore . 

 Configure your network settings. 

 Click Edit Details in
the Networks column. 

 Select the Primary Interface Network . 

 Enter the Primary Interface IP . 

 Enter the Primary Gateway Address . 

 Enter the Primary Subnet Mask . 

 Click Save . 

 NSX-T Manager prepopulates the Deployment
Specification and Deployment Template based
on the Partner Service you selected. 

 Set the Failure Policy to Allow
or Block. The failure policy defines how NSX-T Manager handles traffic
that is directed to the VM-Series firewall if the firewall becomes unavailable. 

 Select the Deployment Mode for
your VM-Series firewall—Standalone or High Availability. If you
have an edge node cluster and select High Availability, NSX-T Manager will
deploy an additional VM-Series firewall on the standby edge node
in addition to the firewall deployed on the active edge node. 

 Click Save to deploy the VM-Series
firewall. 

 Verify that your firewalls connected to Panorama. 

 Log in to Panorama. 

 Select Panorama Managed Devices Summary . 

 Confirm that your firewalls are listed under the correct
device group and the Device State shows Connected . 

 The Device Name for the VM-Series firewall is displayed
on Panorama as PA-VM:<nsx.clusterid> for
NSX-T (N-S) deployment and as PA-VM:<nsx.servicevmid> for
NSX-T (E-W) deployment. 

 Set a secure password for the admin account on your VM-Series
firewalls. 

 Each VM-Series firewall uses a default username and password
(admin/admin), which is used for initial login. Upon logging in
for the first time, you are prompted to set a new, more secure password.
The new password must be a minimum of eight characters and include
a minimum of one lowercase and one uppercase character, as well
as one number or special character. 

 You can update the password
on each firewall individually or all at once through Panorama. 

 Panorama —on Panorama, you can change the default password
for all firewalls in a template or delete the admin user and create
a new username and password. 

 Log in to Panorama 

 Select Device Administrators and
select the admin user. 

 Delete the user or click the user
and enter a new password. 

 If you changed the password, click OK . 

 Select Commit Push
to Devices Edit Selections Force
Template Values . 

 Click OK . 

 Firewall —this procedure must be repeated on each VM-Series
firewall. 

 Log in to the VM-Series firewall using the
default username and password. 

 Follow the prompts to reset the password. 

 Previous 

 Configure the Service Definition on Panorama 

 Next 

 Direct Traffic to the VM-Series Firewall 

 On This Page 

 Activation and Onboarding 

 Strata Cloud Manager 

 Next-Generation Firewalls 

 Firewalls 

 PAN-OS 

 PAN-OS SD-WAN 

 VM-Series 

 Plugins 

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

 Resources 

 All Release Notes 

 Compatibility Matrix 

 Experts Corner 

 Network Security 

 Deployment 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

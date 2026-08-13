---
url: https://docs.paloaltonetworks.com/vm-series/deployment/private-cloud/set-up-the-vm-series-firewall-on-openstack/install-the-vm-series-firewall-in-openstack
fetched_at: 2026-08-13T17:41:42Z
source: palo-alto-main
---

# Install the VM-Series Firewall in a
Basic Gateway Deployment Clear

Install the VM-Series Firewall in a
Basic Gateway Deployment 

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

 Install the VM-Series Firewall in a
Basic Gateway Deployment 

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

 VM-Series Firewall on OpenStack 

 Install the VM-Series Firewall in a
Basic Gateway Deployment 

 Download PDF 

 VM-Series 

 Install the VM-Series Firewall in a
Basic Gateway Deployment 

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

 Heat Templates for Service Chaining and Service Scaling 

 Next 

 Install the VM-Series Firewall with Service Chaining or Scaling 

 Install the VM-Series Firewall in a
Basic Gateway Deployment 

 Learn how to install the VM-Series firewall in a basic gateway deployment. 

 Where Can I Use This? What Do I Need? 

 Openstack 

 VM-Series Firewall License (BYOL) 

 Heat Template 

 Panorama 

 VM-Series plugin 

 Complete the following steps to prepare the
heat templates, bootstrap files, and software images needed to deploy
the VM-Series firewall in OpenStack. After preparing the files,
deploy the VM-Series firewall and Linux server. 

 Download the Heat template and bootstrap files. 

 Download the Heat template package from the GitHub repository . 

 Download the VM-Series base image. 

 Login in to the Palo Alto Networks Customer Support Portal . 

 Select Software Updates and choose PAN-OS for
 VM-Series KVM Base Images from the Filter By 
 drop-down. 

 Download the VM-Series for KVM qcow2 file. 

 Download Ubuntu 14.04 and upload the image to the OpenStack
controller. 

 The Heat template needs an Ubuntu image for launching the
Linux server. 

 Download Ubuntu 14.04. 

 Log in to the Horizon UI. 

 Select Project Compute Images Create
Image . 

 Name the image Ubuntu 14.04
to match the parameter in the pan_basic_gw_env.yaml file. 

 Set Image Source to Image File . 

 Click Choose File and navigate
to your Ubuntu image file. 

 Set the Format to match the file format of your Ubuntu
image. 

 Click Create Image . 

 Upload the VM-Series for KVM base image to the OpenStack
controller. 

 Log in to the Horizon UI. 

 Select Project Compute Images Create
Image . 

 Name the image to match the
image name in your Heat template. 

 Set Image Source to Image File . 

 Click Choose File and navigate
to your VM-Series image file. 

 Set the Format to QCOW2-QEMU Emulator . 

 Click Create Image . 

 Upload the bootstrap files. You have two options for
passing bootstrapping files to OpenStack—file injection (personality
files) or user data. To pass the bootstrap files using user-data, you
must place the files in a tar ball (.tgz file) and encode that tar
ball with base64. 

 File injection is no longer supported beginning with
OpenStack Queens; you must use user data instead. 

 For
file injection, upload the init-cfg.txt, bootstrap.xml, and your
 VM-Series auth codes to your OpenStack controller or a web server
that the OpenStack controller can access. 

 If using the --user-data method to
pass the bootstrap package to the config-drive, you can use the following
command to create the tar ball and encode the tar ball (.tgz file)
with base64: 
 tar -cvzf <file-name> .tgz config/
license software content
base64 -i <in-file> -o <outfile> 

 Edit the pan_basic_gw.yaml template to point to the bootstrap
files and auth codes. 

 If you are using personality files, specify the
file path or web server address to the location of your files under
personality. Uncomment whichever lines you are not using. 

 pan_fw_instance: 
 type: OS::Nova::Server 
 properties: 
 image: { get_param: pan_image } 
 flavor: { get_param: pan_flavor } 
 networks: 
 - network: { get_param: mgmt_network } 
 - port: { get_resource: pan_untrust_port } 
 - port: { get_resource: pan_trust_port } 
 user_data_format: RAW 
 config_drive: true 
 personality: 
 /config/init-cfg.txt: {get_file: "/opt/pan_bs/init-cfg.txt"} 
# /config/init-cfg.txt: { get_file: "http://web_server_name_ip/pan_bs/init-cfg.txt" } 
 /config/bootstrap.xml: {get_file: "/opt/pan_bs/bootstrap.xml"} 
# /config/bootstrap.xml: { get_file: "http://web_server_name_ip/pan_bs/bootstrap.xml" } 
 /license/authcodes: {get_file: "/opt/pan_bs/authcodes"} 
# /license/authcodes: {get_file: "http://web_server_name_ip/pan_bs/authcodes"} 

 If you are using user-data, specify the file path or web
server address to the location of your files under user_data. If
you have more than one 

 pan_fw_instance:
 type: OS::Nova::Server
 properties:
 image: { get_param: pan_image }
 flavor: { get_param: pan_flavor }
 networks:
 - port: { get_resource: mgmt_port }
 - port: { get_resource: pan_untrust_port }
 - port: { get_resource: pan_trust_port }
 user_data_format: RAW
 config_drive: true
 user_data:
# get_file: http://10.0.2.100/pub/repository/panos/images/openstack/userdata/boot.tgz
 get_file: /home/stack/newhot/bootfiles.tgz 

 Edit the pan_basic_gw_env.yaml template environment file
to suit your environment. Make sure that the management and public
network values match those that you created in your OpenStack environment.
Set the pan_image to match the name you assigned to the VM-Series 
base image file. You can also change your server key here. 

 root@node-2:~# cat basic_gateway/pan_basic_gw_env.yaml 
parameters: 
 mgmt_network: mgmt_ext_net 
 public_network: public_net 
 pan_image: pa-vm-image 
 pan_flavor: m1.medium 
 server_image: Ubuntu-14.04 
 server_flavor: m1.small 
 server_key: server_key 

 Deploy the Heat template. 

 Execute the command source openrc 

 Execute the command heat stack-create <stack-name> -f <template> -e ./ <env-template> 

 Verify that your VM-Series firewall is deployed successfully. 

 You can use the following commands to check the creation
status of the stack. 

 Check the stack status with heat stack-list 

 View a detailed list of events that occurred during stack creation
with heat event-list 

 View details about your stack with heat stack-show 

 Verify that the VM-Series firewall is bidirectionally
inspecting traffic accessing the Linux server. 

 Log in to the firewall. 

 Select Monitor Logs Traffic to
view the SSH session. 

 Previous 

 Heat Templates for Service Chaining and Service Scaling 

 Next 

 Install the VM-Series Firewall with Service Chaining or Scaling 

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

 VM-Series 

 Deployment 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

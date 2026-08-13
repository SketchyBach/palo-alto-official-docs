---
url: https://docs.paloaltonetworks.com/vm-series/deployment/public-cloud/set-up-the-vm-series-firewall-on-google-cloud-platform/setup-active-passive-ha-on-gcp/deploy-the-gcp-active-passive-ha
fetched_at: 2026-08-13T17:42:15Z
source: palo-alto-main
---

# Deploy the GCP Active/Passive HA Clear

Deploy the GCP Active/Passive HA 

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

 Deploy the GCP Active/Passive HA 

 Updated on 

 Wed Jul 08 11:47:59 PDT 2026 

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

 Wed Jul 08 11:47:59 PDT 2026 

 Focus 

 Home 

 VM-Series 

 VM-Series Firewall on Google Cloud Platform 

 Set up Active/Passive HA on Google Cloud Platform 

 Deploy the GCP Active/Passive HA 

 Download PDF 

 VM-Series 

 Deploy the GCP Active/Passive HA 

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

 Set up Active/Passive HA on Google Cloud Platform 

 Next 

 VM-Series Firewall on Oracle Cloud Infrastructure 

 Deploy the GCP Active/Passive HA 

 Learn the prerequisites, steps to deploy, and test the active/passive HA in
 GCP. 

 Where Can I Use This? What Do I Need? 

 Google Cloud Platform (GCP) 

 VM-Series License (PAYG or BYOL) 

 VM-Series plugin 

 Panorama 

 Panorama plugin for GCP 

 Use the following procedures to manage your existing deployment profiles. 

 Prepare to set up an Active/Passive HA in GCP 

 Enable the required APIs, generate an SSH key, and clone the GitHub
 repository using: 

 gcloud services enable compute.googleapis.com
ssh-keygen -f ~/.ssh/vmseries-tutorial -t rsa
git clone https://github.com/PaloAltoNetworks/google-cloud-vmseries-ha-tutorial
cd google-cloud-vmseries-ha-tutorial 

 Create a terraform.tfvars file. 

 cp terraform.tfvars.example terraform.tfvars 

 Edit the new terraform.tfvars file and set variables for the
 following variables: 

 Variable Description 

 project_id Set to your Google Cloud deployment project. 

 public_key_path Set to match the full path you created previously. 

 mgmt_allow_ips Set to a list of IPv4 ranges that can access the VM-Series
 management interface. 

 prefix (Optional) If set, this string will be prepended to the created
 resources. 

 vmseries_image_name (Optional) Defines the VM-Series image to deploy. A full list of
 images can be found here . 

 (Optional) If you are using BYOL image (i.e.
 vmseries-flex-byol-* ), the license can be applied during
 deployment by adding your VM-Series authcode to
 bootstrap_files/authcodes 

 Save your terraform.tfvars file. 

 Deploy the GCP Active/Passive HA 

 Initialize and apply the Terraform plan. 

 terraform init
 terraform apply

 Enter yes to start the deployment. After all the resources are created, the Terraform displays the following message: 

 Apply complete!

 Outputs:

 EXTERNAL_LB_IP = "ssh paloalto@1.1.1.1 -i ~/.ssh/vmseries-tutorial"
 EXTERNAL_LB_URL = "https://1.1.1.1"
 VMSERIES_ACTIVE = "https://2.2.2.2"
 VMSERIES_PASSIVE = "https://3.3.3.3"

 All the infrastructure should now be deployed and will boot up and configure by itself. Visit the external_nat_ip by using http://x.x.x.x after a few minutes after the deployment to find the default webpage from the workload-vm . 

 Test the GCP Active/Passive HA Deployment 

 You can now test the deployment by accessing the workload-vm 
 that resides in the trust VPC network. All the workload-vm 
 traffic is routed directly through the VM-Series HA pair. 

 Use the output EXTERNAL_LB_URL to access the web service
 on the workload-vm through the VM-Series firewall. 

 gcloud compute ssh workload-vm 

 Use the output EXTERNAL_LB_SSH to open an SSH session
 through the VM-Series to the workload-vm . 

 ssh paloalto@1.1.1.1 -i ~/.ssh/vmseries-tutorial 

 Run a preloaded script on the workload VM, to test the failover mechanism
 across the VM-Series firewalls. 

 /network-check.sh 

 You will observe an output similar to the code block below, where
 x.x.x.x is the IP address is
 EXTERNAL_LB_IP address. 

 Wed Mar 12 16:40:18 UTC 2023 -- Online -- Source IP = x.x.x.x
Wed Mar 12 16:40:19 UTC 2023 -- Online -- Source IP = x.x.x.x
Wed Mar 12 16:40:20 UTC 2023 -- Online -- Source IP = x.x.x.x
Wed Mar 12 16:40:21 UTC 2023 -- Online -- Source IP = x.x.x.x 

 Log in to the VM-Series firewalls using the
 VMSERIES_ACTIVE and
 VMSERIES_PASSIVE output values. Notice the HA
 Status of the firewalls in the bottom-right hand corner of the
 management window. 

 Perform a user-initiated failover. 

 On the Active firewall, click the
 Device > High Availabilty >
 Operational Commands . 

 Click Suspend local device for high availability. 

 When prompted, click OK to initiate the failover. 

 You might notice that the SSH session to the
 workload-vm is still active. This indicates the
 session successfully failed over between the VM-Series firewalls. The script output should also display the same source
 IP
 address. 

 Wed Mar 12 16:47:18 UTC 2023 -- Online -- Source IP = x.x.x.x
Wed Mar 12 16:47:19 UTC 2023 -- Online -- Source IP = x.x.x.x
Wed Mar 12 16:47:21 UTC 2023 -- Offline
Wed Mar 12 16:47:22 UTC 2023 -- Offline
Wed Mar 12 16:47:23 UTC 2023 -- Online -- Source IP = x.x.x.x
Wed Mar 12 16:47:24 UTC 2023 -- Online -- Source IP = x.x.x.x 

 Onboarding Internet Applications 

 You can onboard and secure multiple internet facing applications through the VM-Series firewall. This is done by mapping forwarding rules on the external load balancer to NAT policies defined on the VM-Series firewall. 

 In Cloud Shell, deploy a virtual machine into a subnet within the trusted
 VPC network. The virtual machine in this example runs a sample application
 for you. 

 gcloud compute instances create my-app2 \
 --network-interface subnet="panw-us-central1-trust",no-address \
 --zone=us-central1-a \
 --image-project=panw-gcp-team-testing \
 --image=ubuntu-2004-lts-apache-ac \
 --machine-type=f1-micro

 Record the INTERNAL_IP address of the new virtual machine. 

 name: my-app2
 ZONE: us-central1-a
 MACHINE_TYPE: f1-micro
 PREEMPTIBLE:
 INTERNAL_IP: 10.0.2.4
 EXTERNAL_IP:
 status: RUNNING

 Create a new forwarding rule on the external TCP load balancer. 

 gcloud compute forwarding-rules create panw-vmseries-extlb-rule2 \
 --load-balancing-scheme=EXTERNAL \
 --region=us-central1 \
 --ip-protocol=L3_DEFAULT \
 --ports=ALL \
 --backend-service=panw-vmseries-extlb

 Retrieve and record the address of the new forwarding rule. 

 gcloud compute forwarding-rules describe panw-vmseries-extlb-rule2 \
 --region=us-central1 \
 --format='get(IPAddress)'

 (Output) 

 34.172.143.223

 On the active VM-Series, click Policies > NAT > Add and enter a name for the rule. 

 Configure the Original Packet as follows:

 Source Zone: untrust 

 Destination Zone: untrust 

 service: service-http 

 Destination Address: Set to the forwarding rule's IP address
 (34.172.143.223). 

 In the Translated Packet tab, configure the Destination Address Translation as follows: 

 Translated Type: Static IP 

 Translated Address: Set to the INTERNAL_IP of the
 sample application (10.0.2.4). 

 Click OK and commit the changes. 

 Access the sample application using the forwarding rule's address. 

 http://34.172.143.223/ 

 Delete the Resources 

 You can delete all the resources when you no longer need them. 

 (Optional) If you onboarded an additional application, delete the forwarding rule and sample application machine. 

 gcloud compute forwarding-rules delete panw-vmseries-extlb-rule2 \
 --region=us-central1

 gcloud compute instances delete my-app2 \
 --zone=us-central1-a

 Delete the Terraform using the command: 

 terraform destroy 

 At the prompt to perform the actions, enter yes .
 After all the resources are deleted, Terraform displays the following message: 

 Destroy complete! 

 Previous 

 Set up Active/Passive HA on Google Cloud Platform 

 Next 

 VM-Series Firewall on Oracle Cloud Infrastructure 

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

 Cloud Infrastructure Protection 

 Network Security 

 Deployment 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

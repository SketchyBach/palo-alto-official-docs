---
url: https://docs.paloaltonetworks.com/vm-series/deployment/public-cloud/set-up-the-vm-series-firewall-on-google-cloud-platform/google-cloud-network-security-integration-nsi-with-vm-series-firewall
fetched_at: 2026-08-13T17:42:13Z
source: palo-alto-main
---

# Google Cloud Network Security Integration (NSI) with VM-Series Firewalls Clear

Google Cloud Network Security Integration (NSI) with VM-Series Firewalls 

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

 Google Cloud Network Security Integration (NSI) with VM-Series Firewalls 

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

 Google Cloud Network Security Integration (NSI) with VM-Series Firewalls 

 Download PDF 

 VM-Series 

 Google Cloud Network Security Integration (NSI) with VM-Series Firewalls 

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

 Securing VPC Networks with VM-Series Firewall on GCP 

 Next 

 Configure GCP NSI Overlay Support 

 Google Cloud Network Security Integration (NSI) with VM-Series Firewalls 

 Google Cloud’s Network Security Integration (NSI) enables traffic inspection for
 existing Virtual Private Cloud (VPC) networks by steering or mirroring traffic to Palo Alto
 Networks Software Firewalls without requiring changes to the underlying network
 configuration. The in-line deployment model uses packet intercept to redirect traffic to the
 software firewall for inspection, while the out-of-band deployment model uses packet
 mirroring to send a copy of the traffic for analysis. 

 Google Cloud's Network Security Integration (NSI) with Palo Alto Networks®
 software firewalls, including VM-Series Next-Generation Firewalls (NGFWs), addresses
 common cloud security challenges. Traditional cloud security deployments often faced
 complexities such as intricate routing, operational overhead, and VPC peering
 limitations. This integration simplifies deploying advanced security services within
 Google Cloud, ensuring consistent security policies and faster protection across
 cloud infrastructure without altering your application architecture or existing
 networking. It provides granular East-West traffic inspection, crucial for
 preventing lateral threat movement, and Layer 7 network runtime security through
 deep packet inspection, which controls applications, users, and content to protect
 against sophisticated threats. 

 The NSI architecture operates on a producer-consumer model for scalable
 security. In this model, security services (the producer) are deployed as a scalable
 backend behind a Google Cloud internal load balancer, serving workloads (the
 consumer). Key components include Palo Alto Networks® software firewalls with a load
 balancer for advanced threat prevention and efficient traffic distribution, along
 with Intercept Deployments and Endpoint Groups for security enforcement and policy
 management. Geneve encapsulation is used to tunnel traffic to the firewall for
 inspection without requiring extensive network modifications. Within the Geneve
 packets, both the Security Profile Group ID (SPG-ID) and VPC ID are passed,
 providing context for traffic. 

 NSI offers two primary modes: 

 Inline (Packet Intercept) — Provides inline inspection for
 real-time threat prevention and blocking. 

 Out-of-Band (Packet Mirroring) — Offers out-of-band monitoring for
 non-disruptive threat intelligence, compliance, and auditing. 

 Prerequisites 

 Before configuring the VM-Series firewall, ensure the following
 prerequisites are met: 

 Google Cloud Network Security Integration (NSI) Environment
 Setup: 

 Fully provisioned and operational Google Cloud NSI
 environment. 

 Producer and Consumer VPCs defined and interconnected. 

 Intercept Deployments and Endpoint Groups configured and
 linked. 

 Firewall rules in the Consumer VPC configured for Layer 7
 redirection. 

 Palo Alto Networks® VM-Series Firewall Deployment: 

 A VM-Series firewall instance deployed within your Google
 Cloud Producer VPC. 

 Google Cloud Deployment (for VM-Series Firewall Configuration) : 

 Create a Security Profile Group. 

 In GCP, go to Network Security
 Integration > Security Profile
 Groups . 

 Click Create Security Profile Group . 

 Define traffic inspection policies (For example:
 allow/block rules). 

 Click Save . 

 This defines inspection criteria for intercepted traffic. 

 Set Up Intercept Endpoint Group 

 Go to Network Security Integration >
 Intercept Endpoint Groups . 

 Click Create Intercept Endpoint Group . 

 Select the consumer VPC(s) whose traffic should be
 intercepted. 

 Associate the relevant Security Profile Group. 

 Click Save . 

 This links consumer VPCs to the security inspection pipeline. 

 Create Intercept Deployment Group 

 In the producer project: 

 Go to Network Security Integration >
 Intercept Deployment Groups . 

 Click Create Intercept Deployment Group . 

 Associate the previously created Intercept Endpoint
 Group. 

 Specify load balancing details if needed (to direct traffic
 to VM-Series firewall). 

 Click Save . 

 Deploy the Intercept Deployment 

 Go to Intercept Deployments . 

 Click Create Intercept Deployment . 

 Link it to the Intercept Deployment Group. 

 Configure backend service/load balancer pointing to
 VM-Series firewall NICs. 

 Save. 

 This step deploys the inspection service tied to the endpoint and
 deployment groups. 

 Configure Firewall Rules in Consumer VPCs. 

 In each consumer VPC, configure firewall rules to permit
 traffic destined for the Intercept Endpoint Group. 

 (Optional) , Set explicit routes if required by your
 architecture. 

 Enable Geneve Encapsulation on the VM-Series Firewall. 

 You must configure the VM-Series firewall to handle
 Geneve-encapsulated packets. 

 Option A: Enable via CLI : 

 SSH into the VM-Series firewall and run the following command: 

 request plugins vm_series geneve-inspect enable yes|no 

 This command requires you to reboot the VM-Series firewall. 

 Commit 

 Option B: Enable via Bootstrap Configuration : 

 Add the following setting to the init-cfg.txt in your bootstrap
 package: 

 geneve-inspect=enable 

 Configure necessary firewall rules in GCP to permit traffic
 redirection. You must ensure that routing rules allow return traffic
 post-inspection and validate endpoint associations across VPCs. 

 You can validate the deployment initiating the test
 traffic between VMs in the consumer VPC. 

 On the VM-Series firewall, go to
 Monitor > Traffic
 Logs for intercepted traffic entries. 

 Confirm traffic is processed according to your
 policies. 

 Previous 

 Securing VPC Networks with VM-Series Firewall on GCP 

 Next 

 Configure GCP NSI Overlay Support 

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

 VM-Series 

 Deployment 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

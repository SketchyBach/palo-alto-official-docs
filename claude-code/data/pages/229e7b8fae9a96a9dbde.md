---
url: https://docs.paloaltonetworks.com/cn-series/deployment/cn-deployment/deploy-the-cn-series-firewalls-new/deploy-the-cn-series-firewall-with-rancher-orchestration/setting-up-master-and-worker-node-on-rancher-cluster-
fetched_at: 2026-08-13T15:31:16Z
source: palo-alto-main
---

# Set up Master and Worker Node on Rancher Cluster Clear

Set up Master and Worker Node on Rancher Cluster 

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

 Set up Master and Worker Node on Rancher Cluster 

 Updated on 

 Dec 2, 2024 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 CN-Series Firewall Docs 

 Activation & Onboarding 

 Getting Started 

 Deployment 

 Select a Document 

 Deployment Modes 

 In-Cloud and On-Prem 

 Upgrade 

 Troubleshooting 

 Release Notes 

 Updated on 

 Dec 2, 2024 

 Focus 

 Home 

 CN-Series 

 CN-Series Firewall Deployment Modes 

 Deploy the CN-Series Firewalls 

 Deploy the CN-Series Firewall with Rancher Orchestration 

 Set up Master and Worker Node on Rancher Cluster 

 Download PDF 

 CN-Series 

 Set up Master and Worker Node on Rancher Cluster 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 CN-Series Firewall Docs 

 Activation & Onboarding 

 Getting Started 

 Deployment 

 Select a Document 

 Deployment Modes 

 In-Cloud and On-Prem 

 Upgrade 

 Troubleshooting 

 Release Notes 

 Previous 

 Rancher Cluster Deployment 

 Next 

 Modify the Rancher Cluster Options YAML File 

 Set up Master and Worker Node on Rancher Cluster 

 After creating a local cluster on Rancher
UI, set up a Master and Worker node, do the following: 

 Go to Rancher UI and click Add Cluster . 

 Click Existing nodes . 

 Enter your Cluster name and then select Flannel from
the Network provider drop-down. 

 Retain the default values for all other fields and then click Next . 

 Under Node options, select all three Node Role options,
and then run the given command into the Master node using SSH. 

 Verify that the Master node is added successfully. 

 SSH into each Worker node and run the following command: 

 sudo docker run -d --privileged --restart=unless-stopped --net=host -v /etc/kubernetes:/etc/kubernetes -v /var/run:/var/run rancher/rancher-agent:v2.5.8 --server https://10.8.70.226 --token 547vwm6nmvnbr877w2mfvjmst6m892vtzztgh2mfg59m6t7wbknbfr --ca-checksum 1ea40f7c3499beb82f4582ecf05cc4300baea8abee079099e87b52c80e40a7bb --worker 

 On successfully running the command on one Master and two Worker
nodes, you will see that Rancher cluster is ready as shown below: 

 Previous 

 Rancher Cluster Deployment 

 Next 

 Modify the Rancher Cluster Options YAML File 

 On This Page 

 Activation & Onboarding 

 Activate a License or Product 

 Strata Logging Service 

 Next-Generation Firewalls 

 Firewalls 

 PAN-OS 

 PAN-OS SD-WAN 

 VM-Series 

 Cloud-Delivered Security Services 

 Advanced URL Filtering 

 Advanced Threat Prevention 

 Advanced DNS Security 

 IoT Security 

 Best Practices 

 Best Practices Library 

 Experts Corner 

 Solutions Docs from Product Experts 

 Translated Documents 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 Deployment 

 AWS 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

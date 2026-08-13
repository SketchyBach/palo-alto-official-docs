---
url: https://docs.paloaltonetworks.com/prisma-access/administration/ztna-connector-in-prisma-access/onboard-a-cloud-instance-or-vm-for-the-ztna-connector/amazon-web-services-deployments-supported-by-ztna-connector/onboard-a-ztna-connector-in-amazon-web-services
fetched_at: 2026-08-13T17:25:43Z
source: palo-alto-main
---

# Onboard a ZTNA Connector in Amazon Web Services Clear

Onboard a ZTNA Connector in Amazon Web Services 

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

 Onboard a ZTNA Connector in Amazon Web Services 

 Updated on 

 Mon Aug 10 14:01:14 PDT 2026 

 Focus 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 Deutsch (German) 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma Access Docs 

 Release Notes 

 Select a Document 

 6.2 Preferred and Innovation 

 6.1 Preferred and Innovation 

 6.0 Preferred and Innovation 

 5.2 Preferred and Innovation 

 5.1 Preferred and Innovation 

 5.0 Preferred and Innovation 

 4.2 Preferred 

 4.1 Preferred 

 4.0 Preferred 

 3.2 Preferred and Innovation 

 Activation & Onboarding 

 Administration 

 Select a Document 

 4.0 & Later 

 Prisma Access China 

 Integrations 

 Incidents & Alerts 

 New Features 

 Updated on 

 Mon Aug 10 14:01:14 PDT 2026 

 Focus 

 Home 

 Prisma Access 

 Prisma Access Administration 

 Prisma Access ZTNA Connector 

 Onboard the ZTNA Connector VM in Your Data Center 

 Amazon Web Services Deployments Supported by ZTNA Connector 

 Onboard a ZTNA Connector in Amazon Web Services 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 Deutsch (German) 

 Prisma Access 

 Onboard a ZTNA Connector in Amazon Web Services 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma Access Docs 

 Release Notes 

 Select a Document 

 6.2 Preferred and Innovation 

 6.1 Preferred and Innovation 

 6.0 Preferred and Innovation 

 5.2 Preferred and Innovation 

 5.1 Preferred and Innovation 

 5.0 Preferred and Innovation 

 4.2 Preferred 

 4.1 Preferred 

 4.0 Preferred 

 3.2 Preferred and Innovation 

 Activation & Onboarding 

 Administration 

 Select a Document 

 4.0 & Later 

 Prisma Access China 

 Integrations 

 Incidents & Alerts 

 New Features 

 Previous 

 Amazon Web Services Deployments Supported by ZTNA Connector 

 Next 

 VMware ESXi Deployments Supported by Prisma Access ZTNA Connector 

 Onboard a ZTNA Connector in Amazon Web Services 

 Onboard a ZTNA Connector in Amazon Web Services. 

 Review the requirements and
 guidelines and the FQDNs and ports you need to
 configure to use ZTNA Connector in Amazon Web Services (AWS).
 Palo Alto Networks Prisma Access delivers the ZTNA Connector through an
 Amazon Web Services (AWS) Marketplace subscription. Once subscribed, launch
 the connector from the Cloud Formation Template for your deployment
 mode. 

 On the Prisma SASE Platform, retrieve and copy the Connector key and secret
 values: Configuration ZTNA Connector Connectors , find the Connector object you created in Prisma Access to
 associate with this VM, and select Copy Token ; then, copy
 the Key and Secret values. 

 For Prisma Access ZTNA Connector 1-Arm Auto-Scaling deployment, you
 must retrieve and copy the Connector Group key and secret values: Configuration ZTNA Connector Connector Groups , find the Connector Group object you created in Prisma Access 
 to associate with this VM, and select Copy Token ; then,
 copy the Key and Secret . 

 After you’ve met all the prerequisites, follow these steps to onboard a Prisma Access 
 ZTNA Connector in AWS. 

 Palo Alto Networks Prisma Access delivers ZTNA Connector through an AWS
 Marketplace BYOL (bring your own license) subscription. Go to AWS
 Marketplace , and search for Prisma Access ZTNA
 Connector , and subscribe. 

 Choose the Cloud Formation Template deployment option that best suites your
 network deployment. 

 ZTNA Connector 1-Arm in
 AWS 

 ZTNA Connector 1-Arm with Auto-Scale
 in AWS 

 ZTNA Connector 2-Arm in
 AWS 

 Deploy ZTNA Connector 1-Arm in AWS 

 Follow these steps to deploy ZTNA Connector 1-Arm in AWS. 

 Select Prisma Access ZTNA Connector 1-Arm cloud
 formation template. 

 Configure these on the Specify stack details 
 page: 

 Enter the Stack name to identify the
 stack. 

 In the Parameters section, specify the
 parameters defined in the stack template. 
 Select Which VPC should ZTNA Connector be
 deployed to . 

 Specify the subnet for the single
 port , where you've provisioned applications
 to onboard to this Connector. You need to have access to the
 internet from this subnet via a NAT Gateway. 

 Enter the Prisma ZTNA Connector License
 Key and Prisma ZTNA Connector License
 Secret values you retrieved from the Prisma SASE
 Portal. 

 Deploy ZTNA Connector 1-Arm with Autoscale in AWS 

 Follow these steps to deploy ZTNA Connector 1-Arm with Autoscale in AWS. 

 Select Prisma Access ZTNA Connector 1-Arm
 Auto-Scaling cloud formation template. 

 Configure these parameters on the Specify stack
 details page: 

 Enter the unique Stack name for the
 deployment. 

 Specify the parameters defined in the stack template in the
 Parameters section: 
 Select Which VPC should ZTNA Connector be
 deployed to . 

 Specify the subnet for the single
 port , where you've provisioned applications
 to onboard to this Connector. You need to have access to
 internet from this subnet via a NAT Gateway. 

 In the Required Auto Scaling Group
 Configuration : 
 Enter the Minimum ZTNA Connectors 
 required in the auto-scaling group. 

 Enter the Maximum ZTNA Connectors 
 required in the auto-scaling group. The maximum number of
 ZTNA Connectors allowed in the Connector Group is 4. 

 Set the Percentage of Network Bandwidth for Scale
 Out . The default and recommended value is
 70%. 

 Enter the Prisma ZTNA Connector License
 Key and ZTNA Connector License
 Secret values you retrieved 
 from the Prisma SASE Portal. 

 Deploy ZTNA Connector 2-Arm in AWS 

 Follow these steps to deploy ZTNA Connector 2-Arm in AWS. 

 Select Prisma Access ZTNA Connector 1-Arm Deployment cloud formation
 template. 

 On the Specify stack details page: 

 Enter the Stack name for the deployment. 

 Specify the parameters defined in your stack template In the
 Parameters section. 
 Select Which VPC should ZTNA Connector be
 deployed to . 

 Specify the public subnet for the Internet
 port for WAN connectivity to IPSec. This
 subnet needs to be associated with a NAT Gateway for
 internet connectivity. 

 Specify the private subnet for Data Center LAN
 port , where you've provisioned applications
 to onboard to this Connector. 

 Enter the Instance Name 

 Enter the Prisma ZTNA Connector License
 Key and Prisma ZTNA Connector License
 Secret values you retrieved from the Prisma SASE
 Portal. 

 Previous 

 Amazon Web Services Deployments Supported by ZTNA Connector 

 Next 

 VMware ESXi Deployments Supported by Prisma Access ZTNA Connector 

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

 Hardware Reference 

 ION 1000 

 ION 1200 

 ION 1200-S 

 ION 2000 

 ION 3000 

 ION 3200 

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

 ION 5200 

 ION 9200 

 Virtual ION Deployment 

 Virtual ION on AWS 

 Virtual ION on Azure 

 Virtual ION on GCP 

 Virtual ION on KVM for NFV 

 Virtual ION on OCI 

 Virtual ION on VMware 

 3rd Party Integrations 

 AWS Cloud-WAN Integration (GRE Connect) 

 AWS Cloud-WAN Integration (Tunnel-less Connect) 

 Checkpoint Integration 

 LiveAction Integration 

 Netskope Integration 

 Symantec Web Security Services Integration 

 Best Practices 

 Best Practices Library 

 Experts Corner 

 Solutions Docs from Product Experts 

 4.1 Preferred 

 5.0 Preferred and Innovation 

 Administration 

 Prisma SASE 

 Prisma Access 

 Strata Cloud Manager 

 SASE 

 4.2 Preferred 

 5.1 Preferred and Innovation 

 5.0.1 Preferred and Innovation 

 Panorama 

 6.0 Preferred and Innovation 

 Prisma Access 

 4.0 Preferred 

 4.0 & Later 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

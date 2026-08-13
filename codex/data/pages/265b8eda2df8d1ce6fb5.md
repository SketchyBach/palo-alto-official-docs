---
url: https://docs.paloaltonetworks.com/prisma-sd-wan/cloudblades/cloudblade-integrations/aws-transit-gateway-cloudblade-integration/prerequisites
fetched_at: 2026-08-13T17:28:59Z
source: palo-alto-main
---

# AWS and Prisma SD-WAN CloudBlade Prerequisites Clear

AWS and Prisma SD-WAN CloudBlade Prerequisites 

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

 AWS and Prisma SD-WAN CloudBlade Prerequisites 

 Updated on 

 Wed Feb 25 07:42:19 PST 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma SD-WAN Docs 

 Activation & Onboarding 

 Administration 

 CloudBlades 

 Select a Document 

 CloudBlade Integrations 

 CloudBlades Integration with Prisma Access 

 Deployment 

 Incidents & Alerts 

 Reference 

 Release Notes 

 Select a Document 

 ION 6.8 

 ION 6.6 

 ION 6.5 

 ION 6.4 

 ION 6.3 

 ION 6.1 

 ION 5.6 

 Prisma SD-WAN Controller 

 Prisma SD-WAN On-Premises Controller 

 Prisma SD-WAN CloudBlades 

 Prisma Access CloudBlade Cloud Managed 

 Prisma Access CloudBlade Panorama Managed 

 New Features 

 Updated on 

 Wed Feb 25 07:42:19 PST 2026 

 Focus 

 Home 

 Prisma SD-WAN 

 AWS Transit Gateway CloudBlade Integration 

 AWS and Prisma SD-WAN CloudBlade Prerequisites 

 Download PDF 

 Prisma SD-WAN 

 AWS and Prisma SD-WAN CloudBlade Prerequisites 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma SD-WAN Docs 

 Activation & Onboarding 

 Administration 

 CloudBlades 

 Select a Document 

 CloudBlade Integrations 

 CloudBlades Integration with Prisma Access 

 Deployment 

 Incidents & Alerts 

 Reference 

 Release Notes 

 Select a Document 

 ION 6.8 

 ION 6.6 

 ION 6.5 

 ION 6.4 

 ION 6.3 

 ION 6.1 

 ION 5.6 

 Prisma SD-WAN Controller 

 Prisma SD-WAN On-Premises Controller 

 Prisma SD-WAN CloudBlades 

 Prisma Access CloudBlade Cloud Managed 

 Prisma Access CloudBlade Panorama Managed 

 New Features 

 Previous 

 AWS Transit Gateway CloudBlade Integration 

 Next 

 Configure the AWS Transit Gateway Integration 

 AWS and Prisma SD-WAN CloudBlade Prerequisites 

 Lets learn more about the prerequisities used for AWS and Prisma SD-WAN CloudBlade. 

 Where Can I Use This? What Do I Need? 

 Prisma SD-WAN (Managed by Strata Cloud Manager ) 

 Prisma SD-WAN 

 AWS Transit Gateway CloudBlade 

 Prisma SD-WAN 

 An active Prisma SD-WAN subscription with sufficient licenses to
 install at least 2 x v7108 IONs, per region. 

 AWS 

 An AWS account with permissions to create, update, and delete CloudFormation
 templates (CFT) and associated VPC resources. 

 The following JSON file can used to create an IAM policy to give the appropriate
 permissions used by the CloudBlade. This can then be assigned to the user/role
 that has programmatic access. 

 To import this file in the AWS console navigate to IAM Policies Create Policy JSON and paste the complete JSON below. 

 { 
 "Version": "2012-10-17", 
 "Statement": [ 
 { 
 "Sid": "VisualEditor0", 
 "Effect": "Allow", 
 "Action": [ 
 "cloudformation:SetStackPolicy", 
 "cloudformation:CreateStack", 
 "cloudformation:DescribeStackResources", 
 "cloudformation:DescribeStacks", 
 "cloudformation:DeleteStack", 
 "cloudformation:SetStackPolicy", 
 "cloudformation:CreateStack", 
 "cloudformation:DeleteStack", 
 "cloudformation:DescribeStackResources", 
 "cloudformation:DescribeStacks", 
 "cloudformation:SetStackPolicy", 
 "cloudformation:CreateStack", 
 "cloudformation:DeleteStack", 
 "cloudformation:DescribeStackResources", 
 "cloudformation:DescribeStacks", 
 "cloudformation:SetStackPolicy", 
 "cloudformation:CreateStack", 
 "cloudformation:DeleteStack", 
 "cloudformation:DescribeStackResources", 
 "cloudformation:DescribeStacks", 
 "ec2:DeleteTransitGatewayConnectPeer", 
 "ec2:CreateTransitGatewayConnect", 
 "ec2:CreateNatGateway", 
 "ec2:CreateTags", 
 "ec2:CreateVpc", 
 "ec2:ModifyTransitGateway", 
 "ec2:CreateTransitGatewayConnectPeer", 
 "ec2:CreateTransitGatewayVpcAttachment", 
 "ec2:DeleteTransitGatewayVpcAttachment", 
 "ec2:CreateRoute", 
 "ec2:DeleteTransitGatewayConnect", 
 "ec2:DeleteNatGateway", 
 "ec2:AuthorizeSecurityGroupIngress", 
 "ec2:DeleteSubnet", 
 "ec2:TerminateInstances", 
 "ec2:AttachVpnGateway", 
 "ec2:DeleteRoute", 
 "ec2:DeleteNetworkInterface", 
 "ec2:CreateRouteTable", 
 "ec2:RunInstances", 
 "ec2:AttachInternetGateway", 
 "ec2:DeleteRouteTable", 
 "ec2:RevokeSecurityGroupIngress", 
 "ec2:CreateNetworkInterface", 
 "ec2:CreateRoute", 
 "ec2:CreateSecurityGroup", 
 "ec2:CreateInternetGateway", 
 "ec2:DeleteSecurityGroup", 
 "ec2:DeleteInternetGateway", 
 "ec2:CreateSubnet", 
 "ec2:DescribeAddresses", 
 "ec2:DescribeInstances", 
 "ec2:DescribeAvailabilityZones", 
 "ec2:DescribeVpcs", 
 "ec2:DescribeAccountAttributes", 
 "ec2:DescribeTransitGateways", 
 "ec2:DescribeNatGateways", 
 "ec2:DescribeTransitGatewayConnects", 
 "ec2:DescribeTransitGatewayVpcAttachments", 
 "ec2:DescribeTransitGatewayConnectPeers", 
 "ec2:DescribeSubnets", 
 "ec2:DescribeRouteTables", 
 "ec2:ReleaseAddress", 
 "ec2:DisassociateAddress", 
 "ec2:CreateTags", 
 "ec2:ModifyNetworkInterfaceAttribute", 
 "ec2:DetachInternetGateway", 
 "ec2:DisassociateRouteTable", 
 "ec2:DescribeSecurityGroups", 
 "ec2:AllocateAddress", 
 "ec2:AssociateRouteTable", 
 "ec2:DescribeInternetGateways", 
 "s3:GetObject", 
 "ec2:DescribeNetworkInterfaces", 
 "ec2:CreateInternetGateway", 
 "sts:DecodeAuthorizationMessage", 
 "ec2:ModifyVpcAttribute", 
 "ec2:DeleteVpc", 
 "ec2:DescribeRegions" 
 ], 
 "Resource": "*" 
 } 
 ]
 } 

 The AWS account must have sufficient permissions to generate AWS access keys. 

 An active AWS marketplace subscription to the
 Prisma SD-WAN ION Virtual Appliance. 

 In an upgrade scenario from version 2.0.0 to version 2.1.0 of the CloudBlade,
 existing deployments will not be impacted, however, any new deployments will
 require to subscribe to this marketplace. 

 The AWS account must have at least 2 Elastic IP addresses available per region
 for allocation. 

 An existing Transit Gateway in the regions where you wish to deploy a Prisma SD-WAN Data center. 

 The AWS Transit Gateway CloudBlade creates the transit gateway attachment
 between the Prisma SD-WAN VPC and the Transit Gateway. It
 also configures the BGP peering between the Prisma SD-WAN 
 Data center IONs and the Transit Gateway. 

 Routing from the application VPCs to reach Prisma SD-WAN remote
 networks and the VPC attachment between Application VPCs and the Transit Gateway
 must be configured by the customer. 

 Plan the Deployment 

 The AWS Transit Gateway Integration CloudBlade provides the automatic
 creation, management, and maintenance of an HA pair of Prisma SD-WAN 
 DC vIONs in an AWS Connect VPC and the establishment of BGP peering over a GRE VPN
 between the Prisma SD-WAN DC vIONs and the AWS Transit Gateway
 connect peer. 

 The CloudBlade automates the following configuration steps required to establish end
 to end connectivity from remote sites to the Application VPCs in AWS: 

 Deploys a Connect VPC in the region(s) where the transit gateway(s) are
 deployed. 

 Deploys a pair of vIONs within the connect VPC(s) in separate availability
 zones. 

 Claims and assigns the vION HA pair to a DC site per region. 

 Configures the Transit Gateway Connect attachment for each vION. 

 Configures GRE tunnels and BGP parameters on both the Prisma SD-WAN vIONs and
 the AWS Transit Gateway. 

 Activates the DC site. 

 Previous 

 AWS Transit Gateway CloudBlade Integration 

 Next 

 Configure the AWS Transit Gateway Integration 

 On This Page 

 Activation & Onboarding 

 Strata Cloud Manager 

 Activate a License or Product 

 Cloud Identity Engine 

 Hub 

 Identity and Access Management 

 Tenant Management 

 SASE 

 Prisma Access 

 Strata Multitenant Cloud Manager 

 AI-Powered ADEM 

 Prisma Access Monitoring and Visibility 

 Visibility & Monitoring 

 Dashboards 

 Incidents and Alerts 

 Reports 

 Autonomous DEM 

 FedRAMP 

 Prisma SASE for FedRAMP 

 Hardware Reference 

 ION 1000 

 ION 1200 

 ION 1200-S 

 ION 2000 

 ION 3000 

 ION 3200 and ION 3200H 

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

 ION 3200H 

 ION 3200H 5G 

 ION 5200 

 ION 9200 

 Virtual ION Deployment 

 Virtual ION on AWS 

 Virtual ION on Azure 

 Virtual ION on GCP 

 Virtual ION on Alibaba Cloud 

 Virtual ION on KVM for NFV 

 Virtual ION on OCI 

 Virtual ION on VMware 

 Virtual ION on Megaport Virtual Edge 

 Virtual ION on Dell PowerEdge 

 Prisma SD-WAN Integration 

 AWS Cloud-WAN Integration (GRE Connect) 

 AWS Cloud-WAN Integration (Tunnel-less Connect) 

 Checkpoint Integration 

 LiveAction Integration 

 Netskope Integration 

 Symantec Web Security Services Integration 

 Prisma SD-WAN Experts Corner 

 Network Policy 

 QoS Whitepaper 

 Security Architecture Whitepaper 

 External Antennas for ION-C Series 

 Dynamic Path Selection 

 Best Practices 

 Best Practices Library 

 Resources 

 All Products A - Z 

 Compatibility Matrix 

 Prisma SD-WAN 

 Strata Cloud Manager 

 Prisma SASE 

 CloudBlades 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

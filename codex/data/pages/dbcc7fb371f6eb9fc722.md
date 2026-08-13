---
url: https://docs.paloaltonetworks.com/next-gen-trust-security/next-gen-trust-security/about-vaas/c-Cloud-discovery-service-sectionOverview/discover-certificates-in-kubernetes-clusters/connect-kubernetes-cluster
fetched_at: 2026-08-13T16:38:38Z
source: palo-alto-main
---

# Connect a Kubernetes Cluster Clear

Connect a Kubernetes Cluster 

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

 Connect a Kubernetes Cluster 

 Updated on 

 Tue Jul 28 08:20:33 PDT 2026 

 Focus 

 Filter

 Expand All 
 | 
 Collapse All 

 Next-Gen Trust Security Docs 

 Getting Started 

 Updated on 

 Tue Jul 28 08:20:33 PDT 2026 

 Focus 

 Home 

 Next‑Gen Trust Security 

 Next-Gen Trust Security 

 Next-Gen Trust Security Overview 

 Discovery Overview 

 Discover Certificates in Kubernetes Clusters 

 Connect a Kubernetes Cluster 

 Next‑Gen Trust Security 

 Connect a Kubernetes Cluster 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Next-Gen Trust Security Docs 

 Getting Started 

 Previous 

 Kubernetes Components in Next-Gen Trust Security 

 Next 

 Discover Certificates On Machines 

 Connect a Kubernetes Cluster 

 Use the connection wizard to connect a Kubernetes cluster to Next-Gen Trust Security. Once connected, the cluster appears on the Kubernetes Clusters page and discovered certificates appear in the Certificate Inventory . 

 Note : Connecting a cluster uses the Discovery Agent for NGTS. Be sure to deploy only one instance of the Discovery Agent for each cluster. Each instance must use a dedicated Built-in Account . Using the same Built-in Account across multiple clusters isn't supported. 

 Prerequisites 

 To connect a Kubernetes cluster to NGTS, you must have: 

 A cluster with permission to create namespaces and secrets. Supported flavors are: 

 AWS Elastic Kubernetes Service (EKS). 

 Azure Kubernetes Service (AKS). 

 Google Kubernetes Engine (GKE). 

 Red Hat OpenShift. 

 Self-hosted Kubernetes distributions such as vanilla Kubernetes or Rancher. 

 helm and kubectl installed on your local machine. 

 Access to the NGTS registry at registry.ngts.paloaltonetworks.com . See Configuring Registry Access on the NGTS developer documentation site. 

 If using an existing Built-in Account , an account created with the Discovery Agent use case and Kubernetes Discovery scope. 

 To Connect a Kubernetes Cluster to NGTS 

 Sign in to Next-Gen Trust Security. 

 Click Insights > Kubernetes Clusters . 

 Click Connect . 

 Click Next . 

 Under Authentication Method , do one of the following: 

 Click Create new Built-in Account to generate credentials and save them to a new account. 

 Click Use Existing Built-in Account and select an account. 

 Enter a Cluster Name and Cluster Description . 

 (Optional) Turn on Defer certificate ownership to leave discovered certificates unclaimed so that child tenants can claim them. To learn more, see Access Management . 

 (Optional) If your cluster uses a proxy, click Yes and enter the URLs: 

 HTTP Proxy URL (optional): The proxy for HTTP traffic, for example https://proxy.example.com:8080 . 

 HTTPS Proxy URL (required): The proxy for HTTPS traffic, for example http://proxy.example.com:8443 . 

 (Optional) If your proxy uses a private or self-signed CA, click Yes and in PEM-encoded CAs , paste the CA certificates. 

 Click Continue . 

 Under Deploy and Connect , copy the cluster connection command and run it in your environment. 

 The command creates a namespace, stores your Built-in Account credentials in a Kubernetes Secret, generates a Helm values file with your configuration, and installs Discovery Agent in your cluster. Once installed, Discovery Agent connects the cluster to NGTS. 

 Wait for the command to complete. Then, select the checkbox and click Test Access to confirm the cluster is connected to NGTS. 

 Click View Cluster to finish using the wizard. The cluster appears in the right-hand details drawer . 

 Related Links 

 Discover Certificates in Kubernetes Clusters 

 Kubernetes Clusters Page 

 Kubernetes Cluster Details 

 Kubernetes Components in Next-Gen Trust Security 

 Previous 

 Kubernetes Components in Next-Gen Trust Security 

 Next 

 Discover Certificates On Machines 

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

 Virtual ION on Alibaba Cloud 

 Virtual ION on KVM for NFV 

 Virtual ION on Dell PowerEdge 

 Virtual ION on OCI 

 Virtual ION on VMware 

 Virtual ION on Megaport Virtual Edge 

 3rd Party Integrations 

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

 Next-Gen Trust Security 

 Getting Started 

 Certificate Management 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

---
url: https://docs.paloaltonetworks.com/next-gen-trust-security/next-gen-trust-security/about-vaas/c-Cloud-discovery-service-sectionOverview/discover-certificates-in-kubernetes-clusters/connect-kubernetes-cluster
fetched_at: 2026-09-16T07:24:23Z
source: palo-alto-main
---

# Connect a Kubernetes Cluster Clear

Updated on 

 Fri Sep 04 10:31:48 PDT 2026 

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

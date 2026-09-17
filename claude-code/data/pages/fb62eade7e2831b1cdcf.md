---
url: https://docs.paloaltonetworks.com/ai-runtime-security/administration/managed-ai-runtime-security-for-aws/managed-airs-for-aws-protect/managed-airs-secure-amazon-eks-traffic
fetched_at: 2026-09-16T07:54:45Z
source: ai-security
---

# Secure Amazon EKS Traffic Clear

Updated on 

 Mon Aug 24 04:41:52 PDT 2026 

 Focus 

 Home 

 Prisma AIRS 

 Administration 

 Managed AI Runtime Security for AWS 

 Protect 

 Secure Amazon EKS Traffic 

 Download PDF 

 Prisma AIRS 

 Secure Amazon EKS Traffic 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma AIRS Docs 

 Activation & Onboarding 

 Administration 

 AI Supply Chain Security 

 AI Red Teaming 

 Release Notes 

 New Features 

 Previous 

 Author and Enforce Managed AIRS for AWS Policies in Strata Cloud Manager 

 Next 

 Secure AI Traffic on Managed AIRS for AWS 

 Secure Amazon EKS Traffic 

 Secure AI container traffic in your Amazon EKS environment by deploying Managed AIRS
 for AWS. 

 Where Can I Use This? What Do I Need? 

 Managed AIRS for AWS 

 Access to Strata Cloud Manager (SCM) 

 Secure AI container traffic in your Amazon EKS environment by deploying Managed AIRS
 for AWS as a network intercept for your container workloads. 

 Complete Deploy Managed AIRS for AWS in
 Strata Cloud Manager . 

 Complete Create Endpoints for Managed AIRS for
 AWS . 

 View Registered Managed AIRS for AWS
 Resources in Strata Cloud Manager . 

 Ensure EKS POD-to-POD traffic is redirected to Managed AIRS for AWS
 resource. 

 Author and Enforce Managed AIRS for
 AWS Policies in Strata Cloud Manager . 

 Redirect Amazon EKS traffic to Managed AIRS resource 

 The following are the steps below to extract, configure, deploy, validate, and
 activate the PAN CNI Helm chart on your EKS cluster. 

 Download the Helm charts from the Resource page
 under the Managed AIRS section. 

 Extract the helm chart. 

 tar xzf fw-QBTNNHYZT-helm-chart.tgz
ls helm-chart/ 

 Expected Output: 

 Chart.yaml crds plugin-serviceaccount.yaml templates values.yaml 

 Locate and open the values.yaml file within the
 downloaded Helm folder structure. 

 Edit the values.yaml file to match your firewall
 deployment. 

 vi helm-chart/values.yaml 

 In values.yaml , populate the
 endpoints field as a list — one entry per
 Availability Zone where your EKS cluster has active nodes. Each entry
 requires two fields: address (the private IP of the
 GWLBE ENI in that Availability Zone) and zone (the
 exact Availability Zone name matching where your nodes run). 

 Single Availability Zone deployment: 

 endpoints:
 - address: 10.2.23.80
 zone: us-west-2b 

 Multi-Availability Zone deployment (one GWLBE ENI per Availability
 Zone): 

 endpoints:
 - address: 10.2.23.80
 zone: us-west-2b
 - address: 10.2.15.42
 zone: us-west-2a
 - address: 10.2.31.19
 zone: us-west-2c 

 Verify before you Save . 

 cat helm-chart/values.yaml 

 Install PAN CNI. 

 helm upgrade --install pan-cni ./helm-chart \
 --namespace kube-system \
 --values ./helm-chart/values.yaml \
 --wait \
 --timeout 300s 

 Validate the installation. 

 # Helm release
helm list -n kube-system

NAME NAMESPACE REVISION UPDATED STATUS CHART APP VERSION
pan-cni kube-system 3 2026-08-20 05:19:45 PDT deployed ai-runtime-security-0.1.0 11.2.2

# PAN CNI pod
kubectl get pods -n kube-system -l k8s-app=pan-cni

NAME READY STATUS RESTARTS AGE
pan-cni-dddnk 1/1 Running 0 24m

# EndpointSlice — confirms GWLBE ENI IP
kubectl get endpointslices -n kube-system | grep pan

pan-ngfw-svc-endpoints IPv4 6080 10.0.0.59 40h

# Service
kubectl get svc -n kube-system | grep pan

pan-ngfw-svc ClusterIP 172.20.157.197 <none> 6080/UDP 40h

# Service account
kubectl get serviceaccounts -n kube-system | grep pan

pan-cni-sa 40h

# CNI binary on node
kubectl exec -n kube-system \
 $(kubectl get pods -n kube-system -l k8s-app=pan-cni \
 -o jsonpath='{.items[0].metadata.name}') \
 -- ls /host/opt/cni/bin/ | grep pan

pan-cni
pan-cni-runfw.sh

# CNI chained in node config — pan-cni appended after aws-cni
kubectl exec -n kube-system \
 $(kubectl get pods -n kube-system -l k8s-app=pan-cni \
 -o jsonpath='{.items[0].metadata.name}') \
 -- cat /host/etc/cni/net.d/10-aws.conflist

The output confirms PAN CNI is chained as the last plugin in the AWS CNI conflist. Key fields to verify:
"name" → "pan-cni"
"mode" → "service"
"dpservicename" → "pan-ngfw-svc"
"firewall" → ["pan-fw"]
"security_namespaces"→ ["kube-system"]
"exclude_namespaces" → [] 

 Annotate the application namespace. 

 Annotate the namespace so that PAN CNI intercepts all pod traffic within
 it and redirects it to the firewall for inspection. The annotation value
 pa n-fw must match the firewall field
 in the pan-cni-config ConfigMap. 

 # Annotate namespace so PAN CNI intercepts all pod traffic in it
kubectl annotate namespace cngfw-traffic \
 paloaltonetworks.com/firewall=pan-fw

# Verify
kubectl describe namespace cngfw-traffic | grep paloaltonetworks 

 Expected Output: 

 Annotations: paloaltonetworks.com/firewall=pan-fw 

 Restart application pods. 

 Pods that were running before the annotation was applied retain their
 original routing and will not be intercepted by PAN CNI. Restarting the
 pods ensures all traffic is redirected through the firewall. 

 # Pods running before annotation must be restarted
kubectl rollout restart deployment -n cngfw-traffic

# Watch pods come back up
kubectl get pods -n cngfw-traffic -w 

 Previous 

 Author and Enforce Managed AIRS for AWS Policies in Strata Cloud Manager 

 Next 

 Secure AI Traffic on Managed AIRS for AWS

---
url: https://docs.paloaltonetworks.com/cn-series/deployment/cn-deployment/deploy-the-cn-series-firewalls-new/editable-parameters-in-cn-series-deployment-yaml-files
fetched_at: 2026-08-13T15:31:16Z
source: palo-alto-main
---

# Editable Parameters in CN-Series Deployment YAML Files Clear

Editable Parameters in CN-Series Deployment YAML Files 

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

 Editable Parameters in CN-Series Deployment YAML Files 

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

 Editable Parameters in CN-Series Deployment YAML Files 

 Download PDF 

 CN-Series 

 Editable Parameters in CN-Series Deployment YAML Files 

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

 Modify the Rancher Cluster Options YAML File 

 Next 

 Secure 5G With the CN-Series Firewall 

 Editable Parameters in CN-Series Deployment YAML Files 

 Review the parameters that you must modify to deploy
the CN-Series firewall 

 The YAML files include several editable parameters, the following tables list the
 ones you must modify to Deploy the CN-Series Firewalls successfully. 

 PAN-CN-MGMT-CONFIGMAP 

 PAN-CN-MGMT-SECRET 

 PAN-CN-MGMT 

 PAN-CN-NGFW-CONFIGMAP 

 PAN-CN-NGFW 

 PAN-CNI-CONFIGMAP 

 PAN-CNI 

 PAN-CNI-MULTUS 

 PAN-CN-MGMT-CONFIGMAP 

 PAN-CN-MGMT-CONFIGMAP 

 Advanced Routing (required for Kubernetes 3.0.0
deployments) 
 PAN_ADVANCED_ROUTING:”true” 
 If you are using Advanced Routing with the Kubernetes 3.0.0 plugin, you must
 configure first enable it in PAN-OS, then manually on the template
 stack. After enabling it, commit and push the configuration. For
 more information, see Advanced Routing . 

 Panorama IP Address 

 PAN_PANORAMA_IP: 

 Include the Panorama IP address to which
the CN-MGMT Pod will connect. If you have configured your Panorama
management servers in a high availability (HA) configuration, provide the
IP address of the primary-active Panorama. 

 You can locate
the Panorama IP address on Dashboard General Information . 

 Device Group Name 

 PAN_DEVICE_GROUP: 

 Specify the device group name to which you want
to assign the CN-NGFW Pods. From Panorama, you will push identical
policies to all CN-NGFW Pods that are managed by a pair of CN-MGMT
Pods (or that belong to a PAN-SERVICE-NAME). 

 You can locate
the device group name on Panorama Device Groups . 

 Template Stack Name 

 PAN_TEMPLATE_STACK: 

 Allows you to configure the settings that
enable firewalls (CN-NGFW Pods) to operate on the network. 

 You
can locate the template stack name on Panorama Templates . 

 Log Collector group name 

 PAN_PANORAMA_CGNAME: 

 Enables log storage for the logs generated
on the CN-NGFW firewalls. Without a Collector Group, the firewall
logs are not saved. 

 You can locate the collector group name
on Panorama Collector
Groups . 

 ( Optional ) 

 #CLUSTER_NAME: 

 Specify the cluster name. The hostname of
the CN-MGMT pod combines the StatefulSet name defined in the PAN-CN-MGMT.yaml and
this optional CLUSTER_NAME. This hostname enables you to identify
pods that are associated with different clusters, if you manage
multiple clusters on the same Panorama appliance. As a best practice,
use the same name here and on the Kubernetes plugin on Panorama. 

 ( Optional ) Panorama HA peer IP
address 

 #PAN_PANORAMA_IP2: 

 IP address of the Panorama peer (passive-secondary)
that is configured in a high availability setup. Verify that the PAN_PANORAMA_IP
is that of the primary-active Panorama. 

 You can locate the
Panorama HA peer IP address on Panorama High Availability Setup . 

 ( Required for GTP ) GTP Security 

 #PAN_GTP_ENABLED: "true" 

 Enable this parameter for GTP Security on
the CN-Series firewall. After you enable GTP, you can use Panorama
to configure GTP security and monitor GTP traffic on the firewall. 

 ( Required for jumbo frame support, if
primary CNI does not use jumbo frame ) Jumbo Frame Mode 

 #PAN_JUMBO_FRAME_ENABLED: "true" 

 The CN-MGMT pod during bootup uses the eth0 MTU
to auto-detect whether to enable jumbo-frame mode. So, if your secondary
CNI uses jumbo frames, while the primary CNI does not, you must
define PAN_JUMBO_FRAME_ENABLED: "True" to
enable jumbo frame mode on the CN-Series firewall. 

 You must
make this change before the CN-MGMT StatefulSet is deployed. 

 ( Required for flexible system resource
allocation ) 

 CN-Series as a DaemonSet 

 #PAN_NGFW_MEMORY: "42Gi" 

 CN-Series as a K8s Service 

 #PAN_NGFW_MEMORY: "6.5Gi" 

 #PAN_NGFW_MEMORY: "42Gi" 

 For
5G-Native Security 48Gi is recommended 

 If you need higher capacity and want to configure
more memory to address your deployment needs, define the memory
value using this parameter. 

 CN-Series as a DaemonSet 

 Small
capacity is 42Gi or less and large capacity is greater than 42Gi. 

 CN-Series as a K8s Service 

 Small capacity is less than
6.5Gi, medium capacity is between 6.5Gi and 42Gi, and large capacity
is greater than 42Gi. 

 This change also requires
the same or higher memory allocation on the pan-cn-ngfw.yaml . 

 ( Optional ) AF-XDP 

 #PAN_DATA_MODE: “next-gen” 

 This parameter is required to enable Address Family
eXpress Data Path (AF-XDP). 

 AF-XDP is an eBPF based socket
that is optimized for high performance packet processing suited
to cloud native services, to increase effective throughput. This
requires kernel version 5.4 or later. Additionally, jumbo mode is
not supported; EKS cannot use this parameter because jumbo mode
is enabled by default. 

 Additionally, privileged mode is required
in PAN-CN-NGFW . 

 ( Required to enable HPA ) 

 ( AKS
and GKE ) #HPA_NAME 

 ( EKS
only ) #PAN_NAMESPACE_EKS 

 ( AKS
only ) #PAN_INSTRUMENTATION_KEY 

 Several parameters are required to enable Horizontal Pod Autoscaling (HPA)
on the CN-Series firewall as a Service. 

 For each
environment, you must provide a unique name to identify the HPA
resource per namespace or per tenant. 

 For AKS deployment, you must provide an Azure Application
Insight instrumentation key. 

 The following default values
are defined in the pan-cn-mgmt-configmap.yaml file. 

 metadata:
 name: pan-mgmt-config
 namespace: kube-system
data: 
 PAN_SERVICE_NAME: pan-mgmt-svc
 PAN_MGMT_SECRET: pan-mgmt-secret 

 These default values
allow you to use these files for a quick proof-of-concept. If you
want to modify these e.g., to deploy more than one fault-tolerant
pair of PAN-MGMT Pods that manage up to 30 PAN-NGFW Pods, you must
modify pan-mgmt-svc to use another
service name. When you modify these values, you must update the
corresponding references in the other YAML files to match the values
you define in this file. 

 PAN-CN-MGMT-SECRET 

 PAN-CN-MGMT-SECRET 

 VM auth key 

 PAN_PANORAMA_AUTH_KEY: 

 Allows Panorama to authenticate the firewalls so
that it can add each firewall as a managed device. The VM auth key
is required for the lifetime of the deployment. Without a valid
key in the connection request, the CN-Series firewall will be unable
to register with Panorama. 

 See Install the Kubernetes
 Plugin for CN-Series Firewall . 

 Device certificate for the CN-Series 

 CN-SERIES-AUTO-REGISTRATION-PIN-ID 

 CN-SERIES-AUTO-REGISTRATION-PIN-VALUE 

 The firewall requires the device certificate
to get any site license entitlements and securely access the Palo
Alto cloud-delivered services. Generate the PIN ID and the PIN value
on the Palo Alto Networks CSP, and use the PIN before it expires.
For example: 

 CN-SERIES-AUTO-REGISTRATION-PIN-ID: 

 "01cc5-0431-4d72-bb84-something” 

 CN-SERIES-AUTO-REGISTRATION-PIN-VALUE: 

 "12………………….13e" 

 The
following additional field for CN-SERIES-AUTO-REGISTRATION-API-CSP
is commented out and is not required: "certificate.paloaltonetworks.com" 

 See Install a Device
 Certificate on the CN-Series Firewall . 

 PAN-CN-MGMT 

 PAN-CN-MGMT 

 Image path for the Init container image
for the CN-MGMT firewall 

 initContainers:
  - name: pan-mgmt-init
    image: <your-private-registry-image-path> 

 The init container generates certificates
which are used for securing communication between instances of CN-MGMT
Pods and between CN-MGMT pods and CN-NGFW pods. 

 Edit the
image path to point to the location to which you have uploaded the
docker image for the CN-MGMT container. 

 Image Path for the CN-MGMT image containers: 

 initContainers:
  - name: pan-mgmt
    image: <your-private-registry-image-path> 

 Edit the image path to point to the location
to which you have uploaded the docker image for the CN-MGMT container. 

 Hostname of the CN-MGMT firewall 

 kind: StatefulSet
metadata:
  name: pan-mgmt-sts 

 The hostname of the CN-MGMT firewall is derived
by combining the StatefulSet name and the optional cluster name
that you may have defined in the pan-cn-mgmt-configmap.yaml . 

 The
default hostname of the CN-MGMT pods is pan-mgmt-sts-0 and pan-mgmt-sts-1,
because the StatefulSet name is pan-mgmt-sts and the cluster name
is not defined. 

 If the hostname is more than 30 characters,
the name will be truncated at 30 characters. 

 ( Required if you defined memory for
flexible system resource allocation ) 

 If you allocated a memory value that is
more than or equal to 40Gi for #PAN_NGFW_MEMORY: "40Gi" in
the pan-cn-mgmt-configmap.yaml , make sure that
you have identical values in request and limit for
CPU and memory to achieve higher capacity utilization under 

containers:
 resources:
 requests:
 # configurable based on desired logging, capacities
 cpu: "4"
 memory: "16.0Gi"
 limits:
 cpu: "4"
 memory: "16.0Gi"

 For 5G-Native Security, recommended values are
cpu=4, memory=16Gi 

 ( Only for an on-premises or self-managed
Native Kubernetes deployment ) 

 storageClassName: local 

 For self-managed deployment, the default config
has “storageClassName: local”. 

 If your cluster has dynamically
provisioned Persistent Volumes (PV), you must modify the “storageClassName:
local” to match that storageClass or remove these lines if DefaultStorageClass
is being used. 

 If your cluster doesn’t have dynamically provisioned
PV, cluster admin can create static PVs with provided pan_cn_pv_local.yaml which has
2 sets of few PVs, one each for each PAN-CN-MGMT statefulSet pods.
You can modify pan_cn_pv_local.yaml to match
the volumes in your setup and deploy it before deploying the PAN-CN-MGMT.yaml . 

 PAN-CN-NGFW-CONFIGMAP 

 You do not need to modify any PAN-values unless
you need to change the following: 

 PAN_SERVICE_NAME: pan-mgmt-svc 

 The service name should match what you defined
on the PAN-CN-MGMT-CONFIGMAP . 

 FAILOVER_MODE: failopen 

 You can change this to failclose. It comes into
effect only when CN-NGFW fails to get a license. 

 In fail-open mode the firewall will receive the
packet and send it out without inspecting it. Transitioning to fail-open
mode causes an internal restart and a brief disruption to traffic. 

 In fail-close mode, the firewall will drop all the packets
it receives. The fail-close mode also brings down the CN-NFGW and
releases the slot allocated to let other licensed CN-NFGW use that
slot. 

 CPU Pinning—In the pan-cn-ngfw-configmap.yaml ,
CPU pinning and hyperthreading are disabled. Do not toggle this
setting to enable CPU pinning for dedicated physical cores instead
of logical cores with hyperthreading unless guided by Palo Alto
Networks Support. 

 PAN_CPU_PINNING_ENABLED: "True"/"False" PAN_HYPERTHREADING_ENABLE: "True"/"False" 

 PAN-CN-NGFW 

 PAN-CN-NGFW 

 Image path for the CN-NGFW
container image 
 image 

   containers: 
  - name: pan-ngfw-container
    image:
      <your-private-registry-image-path> 

 Edit the image path to point to the location
to which you have uploaded the docker image for the CN-NGFW container. 

 ( Required if you defined memory for
flexible system resource allocation ) 

 If you allocated a memory value that is
more than or equal to 40Gi for #PAN_NGFW_MEMORY: "40Gi" in
the pan-cn-mgmt-configmap.yaml , make sure that
you have identical values in request and limit for
cpu and memory to achieve guaranteed QoS under 

 containers:
 resources:
 requests:
 #configurable based on desired throughput, number of running pods
 cpu: "1"
 memory: "40.0Gi"
 limits:
 cpu: "1"
 memory: "40.0Gi"

 For 5G-Native Security, recommended values are
cpu=12, memory=48Gi. 

 Note: 

 The following annotation
identifies the PAN-NGFW daemonset: 

 paloaltonetworks.com/app: pan-ngfw-ds 

 Do
not modify this value. 

 The following annotation identifies the firewall name (“pan-fw”): 

 paloaltonetworks.com/firewall: pan-fw 

 In pan-cni-configmap.yaml ,
this firewall name must match exactly in the cni_network_config: “firewall” 

 And
this annotation should match exactly in the application yaml that
you use to deploy each application pod. 

 The CN-NGFW Pod on each node
secures the application pods and namespaces that have the annotation: 

 paloaltonetworks.com/firewall: pan-fw 

 Keep this annotation as is. 

 ( Optional ) AF-XDP 
 imagePullPolicy: Always securityContext: capabilities: #add: ["NET_ADMIN","NET_RAW","NET_BROADCAST","NET_BIND_SERVICE"] add: ["ALL"] privileged: true resources: 
 You must add privileged: true to
the section shown to the left. This parameter is required to enable
Address Family eXpress Data Path (AF-XDP). 

 You must also
enable AF-XDP in the PAN-CN-MGMT-CONFIGMAP . 

 PAN-CNI-CONFIGMAP 

 These
parameters are optional. 

 PAN-CNI-CONFIGMAP 

 List of firewall names that the application
pod might belong to: 

 "firewall": [ "pan-fw" ] 

 While no modifications are required, if
you change the annotation paloaltonetworks.com/firewall:
pan-fw in the pan-cn-ngfw.yaml ,
you must replace the value in "firewall": [ "pan-fw" ] to
match. 

 "exclude_namespaces": [] 

 While no modifications are required, if
you want to exclude specific namespaces, add it to “exclude_namespaces" ,
so that the application pod annotation in that namespace is ignored
and traffic is not redirected to the CN-NGFW pod for inspection. 

 "security_namespaces": [ "kube-system" ] 

 Add the namespaces in which you have deployed the
CN-NGFW daemonset in security_namespaces. The default namespace
is kube-system. 

 “interfaces” 

 Add the interfaces in the application pods
from which you want to redirect traffic to the CN-NGFW pod for inspection.
By default, only eth0 traffic is inspected, and you can add additional
interfaces as a comma-separated list of strings e.g. [“eth0”, “net1”,
“net 2”]. 

 cni_network_config: 

 {
"cniVersion": "0.3.0", 
"name": "pan-cni", 
"type": "pan-cni", 
"log_level": "debug", 
"appinfo_dir": "/var/log/pan-appinfo", 
"mode": "daemonset", 
"firewall": [ "pan-fw" ], 
"interfaces": ["eth0", "net1", "net2", "net3"], 

 } 

 In
addition to this, you must also append pan-cni to
the k8s.v1.cni.cncf.io/networks annotation
in the app pod. 

 For example: 

 metadata: name: testpod annotations: paloaltonetworks.com/firewall: pan-fw k8s.v1.cni.cncf.io/networks: sriov-net1, sriov-net2, macvlan-conf, pan-cni 

 CN-Series
currently doesn't support DPDK and it doesn't allow the app pod
to use DPDK. You might need to modify the app pod if the app does not
automatically adjust to non DPDK mode. 

 ( CN-Series as a Kubernetes Service only ) 

 “dpservicename” 

 “dpservicenamespace” 

 When the CN-Series is deployed as a service,
a dpservicename and dpservicenamespace are required.
By default, dpservicename is “pan-ngfw-svc” and dpservicenamespace is “kube-system” . 

 PAN-CNI 

 PAN-CNI 

 Image path for the PAN-CNI container image that
has the CNI binaries and the CNI network config file on each node. 

 containers: 
 name: install-pan-cni 
 image: <your-private-registry-image-path> 

 Edit the image path to point to the location
to which you have uploaded the docker image for the PAN-CNI container. 

 PAN-CNI-MULTUS 

 If
you are using Multus CNI on a self-managed or native implementation
of Kubernetes such as with VMware TKG+, use the pan-cni-multus.yaml instead
of the pan-cni.yaml . 

 Previous 

 Modify the Rancher Cluster Options YAML File 

 Next 

 Secure 5G With the CN-Series Firewall 

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

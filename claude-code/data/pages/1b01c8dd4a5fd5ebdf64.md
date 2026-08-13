---
url: https://docs.paloaltonetworks.com/prisma-sd-wan/cloudblades/prisma-access-integrations/prisma-access-for-networks-aggregate-bandwidth-licensing/determine-ipsec-termination-nodes
fetched_at: 2026-08-13T17:29:19Z
source: palo-alto-main
---

# Determine IPSec Termination Nodes  Clear

Determine IPSec Termination Nodes 

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

 Determine IPSec Termination Nodes 

 Updated on 

 Wed Feb 25 08:09:54 PST 2026 

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

 Wed Feb 25 08:09:54 PST 2026 

 Focus 

 Home 

 Prisma SD-WAN 

 Prisma SD-WAN CloudBlades Integration with Prisma Access 

 Prisma Access for Networks Aggregate Bandwidth Licensing 

 Determine IPSec Termination Nodes 

 Download PDF 

 Prisma SD-WAN 

 Determine IPSec Termination Nodes 

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

 IPSec Termination Nodes Within Prisma 

 Next 

 Configure Site-Level Settings to Onboard a Site 

 Determine IPSec Termination Nodes 

 Determine the nodes to begin configuration of a remote networking on-boardinf for the
 Panorama nd Cloud Managed CloudBlades. 

 Where Can I Use This? What Do I Need? 

 Supported CloudBlades: 

 Prisma Access for Networks (Managed by Panorama) 

 Prisma Access for Networks (Cloud Managed) 

 Prisma SD-WAN 

 Prisma Access 

 Supported Cloud Plugin Versions 

 Prisma Access for Networks (Managed by Panorama) CloudBlade versions 3.x.x and
 later 

 Prisma Access for Networks (Cloud Managed) CloudBlade versions 3.x.x and
 4.x.x 

 Determine the nodes to begin configuration of a Remote Networking on-boarding and select
 the appropriate region or location for both Panorama Managed and Cloud Managed
 CloudBlades. 

 Panorama Managed
 CloudBlade 

 Cloud Managed CloudBlade 

 Determine IPSec Termination Nodes (Panorama Managed CloudBlade) 

 Determine IPSec Termination Nodes (Panorama Managed CloudBlade) Method 1 and Method 2
 to begin configuration of a Remote Networking on-boarding. 

 In our example, the first method to determine the IPSec termination nodes, we use US
 East as the location, which has two nodes behind it. 

 Click the IPSec Termination Node drop-down to view the
 list of IPSec termination nodes.

 These node names are listed in the order they are deployed on the backend,
 not alphabetically. 

 The order of appearance of the two IPSec termination nodes is: 

 us-east-charlock 

 us-east-banyan 

 Determine IPSec Termination Nodes Method #2 

 The second method to obtain the IPSec Termination Nodes within Prisma
 Access for Networks is through the Panorama API. Within the API, you will see the
 abbreviation of SPN, which is the reference for the IPSec Termination Nodes. 

 Using Panorama, navigate to the following subtree in the API within Panorama,
 clicking on each item listed in bullets (notice the variation for single-tenant
 versus multitenant). 

 Single Tenant Environment 

 https://panorama/api 

 config 

 devices 

 localhost.localdomain (or appropriate name) 

 plugins 

 cloud_services 

 remote-networks 

 agg-bandwidth 

 Multi-Tenant Environment 

 https://panorama/api 

 Configuration Commands 

 devices 

 localhost.localdomain (or appropriate name) 

 plugins 

 cloud_services 

 multi-tenant 

 tenants 

 default-tenant 

 remote-networks 

 agg-bandwidth 

 The output of the API is similar to the following: 

 <response status="success" code="19"><result total-count="1" count="1"><agg-bandwidth><enabled>yes</enabled><region><entry name="europe-central"><allocated-bw>100</allocated-bw><spn-name-list><member>europe-central-aspen</member></spn-name-list></entry><entry name="us-east"><allocated-bw>600</allocated-bw><spn-name-list><member>us-east-charlock</member><member>us-east-banyan</member></spn-name-list></entry><entry name="canada-central"><allocated-bw>100</allocated-bw><spn-name-list> 

 A sample from the web interface would also look similar to the above. The
 us-east appears first in the list, followed by the node
 names underneath. 

 The IPSec Termination Node names are listed below the entry named
 spn-name-list with indentation. The order seen here’s the
 same order as the Panorama interface shown in the previous section. 

 IPSec Termination Node Conventions and Tag Nomenclature 

 With the information obtained above from our nodes for
 us-east , the tagging methodology for the CloudBlade can
 now be determined. The tag constructs for the CloudBlade with Aggregate
 Bandwidth licensing would look as follows: 

 Prisma_region: <<region name>>:<<IPSec Termination Node Name or
 Number>> 

 With this construct, the tags for the interfaces will look similar to the
 following: 

 prisma_region:us-east-1:us-east-charlock 

 prisma_region:us-east-1:us-east-banyan 

 OR 

 prisma_region:us-east-1:1 

 prisma_region:us-east-1:2 

 The node name (us-east-charlock) or order that the node appears in the list (1) can
 both be used in the naming convention for the interface tags. 

 To assist with the automation of the scripts and deployments, the Prisma SD-WAN 
 Tagger Utility Script can be used to help create or
 configure the tags. 

 Determine IPSec Termination Nodes (Cloud Managed CloudBlade) 

 Determine the IPSec termination nodes in the Cloud Managed CloudBlade to begin
 configuration of a Remote Networking on-boarding. 

 In Prisma Access, go to the Configuration NGFW and Prisma Access Remote Networks Add Remote Network . 

 In the General section, select a region from the
 Prisma Access Location drop-down. 

 After you choose the location, select from the available SPN names from the
 IPSec Termination Node drop-down. 

 IPSec Termination Node Conventions and Tag Nomenclature 

 Below is an example for the tagging methodology and tag constructs
 with aggregate bandwidth licensing for the CloudBlade. 

 Prisma_region: <<region name>>:<<IPSec Termination Node Name or
 Number>> 

 With this construct, the tags for the interfaces will look similar to the
 following. For example: 

 prisma_region:eu-west-3:france-north-portia 

 prisma_region:eu-west-3:france-north-bluebells 

 OR 

 prisma_region:eu-west-3:1 

 prisma_region:eu-west-3:2 

 The node name (france-north-portia) or order that the node appears in the list
 (1) can both be used in the naming convention for the interface tags. 

 You can refer to the region tag codes of the Prisma Access Regions. 

 To aid in automating scripts and deployments, the Prisma SD-WAN 
 Tagger script can also be used to create or
 configure the tags. 

 Previous 

 IPSec Termination Nodes Within Prisma 

 Next 

 Configure Site-Level Settings to Onboard a Site 

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

 SASE 

 Prisma SD-WAN 

 Strata Cloud Manager 

 CloudBlades 

 Prisma SASE 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

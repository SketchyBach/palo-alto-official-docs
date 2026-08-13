---
url: https://docs.paloaltonetworks.com/prisma-sd-wan/administration/prisma-sd-wan-sites-and-devices/set-up-sites/configure-ciphers
fetched_at: 2026-08-13T17:28:27Z
source: palo-alto-main
---

# Configure Ciphers Clear

Configure Ciphers 

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

 Configure Ciphers 

 Updated on 

 Aug 10, 2026 

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

 Aug 10, 2026 

 Focus 

 Home 

 Prisma SD-WAN 

 Prisma SD-WAN Administrator’s Guide 

 Prisma SD-WAN Sites and Devices 

 Set Up Sites 

 Configure Ciphers 

 Download PDF 

 Prisma SD-WAN 

 Configure Ciphers 

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

 Configure a Site Prefix 

 Next 

 Configure a DHCP Server 

 Configure Ciphers 

 Learn about the ciphers supported in Prisma SD-WAN and how to
 configure them. 

 Where Can I Use
 This? What Do I
 Need? 

 Prisma SD-WAN (Managed by Strata Cloud Manager ) 

 Prisma SD-WAN 

 Prisma SD-WAN supports the Cipher Block Chaining (CBC)
 and Galois/Counter Mode (GCM) modes in the Advanced Encryption Standard (AES)
 encryption. Prisma SD-WAN supports the following CBC and GCM
 encryption algorithms for Secure Fabric tunnels. 
 AES-256-GCM 

 AES-256-CBC 

 AES-128-GCM 

 AES-128-CBC 

 The order of algorithm selection for Secure Fabric tunnels by the controller is: 

 AES-256-GCM > AES-256-CBC > AES-128-GCM > AES-128-CBC 

 Note that: 
 All the four algorithms are enabled by default for Secure Fabric tunnels for
 a newly created site. 

 You can enable the GCM algorithms for existing sites. 

 The order of selection of the algorithms based on the device software versions is as
 follows: 

 Software Versions of ION devices Algorithm Selection Order 

 Both the ION devices are running software versions 6.5.1 or
 higher AES-256-GCM>AES-256-CBC>AES-128-GCM>AES-128-CBC 
 The best common algorithm based on the above order is
 selected. 

 One device running software version 6.5.1 or higher, second
 device running a version lower than 6.5.X. 

 AES-256-CBC>AES-128-CBC 

 (AES-GCM is supported for devices running software
 versions 6.5.1 or later) 

 Both the ION devices are running software versions lower than
 6.5.1. 

 AES-256-CBC>AES-128-CBC 

 (AES-GCM is supported for devices running software
 versions 6.5.1 or later) 

 The controller selects the best common algorithm between a pair of sites
 and pushes the same algorithm to both the sites. 

 Example: 

 Site1 VPN Ciphers: AES_128_CBC, AES_256_CBC, AES-128-GCM 

 Site2 VPN Ciphers: AES-128-GCM 

 Here, the controller will select AES-128-GCM for all the VPNs between all the devices
 in these two sites and then push the configuration accordingly to the devices. 

 If there are no common ciphers between two sites, then None 
 will be displayed and the tunnel will not be established. 

 Cipher Support for Standard VPN Tunnels 

 Prisma SD-WAN uses Standard VPN tunnels to connect to
 third-party services. Unlike Secure Fabric tunnels, these tunnels use both IKE and
 IPsec for tunnel formation. 

 You can select the algorithms for Standard VPNs when configuring IPSec profiles . 

 Note that: 
 Only IKEv2 supports the AES-GCM algorithm. IKEv1 does not support it. 

 Although the Pseudo Random Functions (PRF) algorithms in IKEv2 proposals are
 derived from Hash algorithms, you need to explicitly select the PRF
 algorithm for GCM. The algorithms are the same as the hash algorithms that
 Prisma SD-WAN supports i.e. SHA-256 and SHA-512. 

 Prisma SD-WAN uses the 16-octet (128-bit) authentication tag
 by default. 

 Configure Ciphers for Secure Fabric Tunnels 

 Select a site. On the Configuration tab, locate the
 Branch Site Details section and click
 Configure Ciphers . 

 Select the required ciphers and click Save . 

 All the ciphers are selected by default only
 for newly created sites. 

 You can view the selected ciphers
 between sites by selecting Configuration Prisma SD-WAN Branch Sites . Select a site, click Overlay
 Connections and then select Edit Secure Fabric
 Link . 

 Related CLIs 

 config controller cipher 

 dump controller cipher 

 Previous 

 Configure a Site Prefix 

 Next 

 Configure a DHCP Server 

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

 Administration 

 Prisma SD-WAN 

 Strata Cloud Manager 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

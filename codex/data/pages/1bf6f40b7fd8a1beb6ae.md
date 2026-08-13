---
url: https://docs.paloaltonetworks.com/prisma-sd-wan/cloudblades/cloudblade-integrations/shasta-lan-integration/configure-shasta-lan
fetched_at: 2026-08-13T17:29:13Z
source: palo-alto-main
---

# Configure Shasta LAN Clear

Configure Shasta LAN 

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

 Configure Shasta LAN 

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

 Shasta LAN Integration 

 Configure Shasta LAN 

 Download PDF 

 Prisma SD-WAN 

 Configure Shasta LAN 

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

 Shasta LAN Integration 

 Next 

 Branch Microsegmentation 

 Configure Shasta LAN 

 Learn to configure the Shasta LAN with Prisma SD-WAN. 

 Where Can I Use This? What Do I Need? 

 Prisma SD-WAN (Managed by Strata Cloud Manager ) 

 Prisma SD-WAN 

 To configure Shasta LAN: 

 On the CloudBlades page, select Configure on the Shasta LAN tile. 

 Install the Shasta LAN. 

 After the installation, configure and manage Shasta LAN on the Shasta Cloud
 portal. 

 As a first-time user, you will need to register on Shasta Cloud.
 After you register, you will receive an email invitation to log into Shasta
 Cloud. Complete the registration process to access the Shasta Cloud
 portal. 

 If you have access to Shasta Cloud, you can configure sites on
 Shasta Cloud. 

 After saving the configuration, the Shasta LAN tile shows as enabled on the
 CloudBlade page. 

 Onboard Using Zero Touch Provisioning 

 ZTP simplifies and automates the onboarding of new branch sites to the Prisma
 SASE portal. To onboard branch sites: 

 Navigate to Branch Sites and select a site. 

 Select to Configure Shasta LAN. 

 Click Next . 

 Enter the DHCP information like Subnet ,
 Default Gateway , IP Range ,
 and DNS Servers . You can up to three DNS
 servers. 

 To complete the Shasta LAN onboarding configuration, Select
 Networks that should be pushed to the access points
 associated with this site. 

 For a first site deployment, define the wireless network parameters such
 as SSID name, authentication mechanisms, and isolation policy for
 segmentation. 

 You can also configure additional VLANs for the data traffic, supporting
 both switch and wireless users and devices. 

 Click Next and Save your changes, and you can see the DHCP and
 network configured on the Shasta LAN. 

 Now, you can update and manage Shasta LAN ZTP network and Wireless network
 settings by selecting the Manage button. You can also
 Monitor Shasta LAN by using the link below the
 Manage button. 

 You can monitor the LAN infrastructure at the site along with the clients
 connected to the LAN infrastructure by clicking the Monitor link. This
 takes you to the CloudBlade Monitor tab. 

 Onboard New Switches and Access Points 

 After enabling ZTP provisioning for Shasta LAN at a site, you can now
 connect Shasta Switches and Access Points to your branch network. Connect your
 switch uplink ports to the ION device’s LAN interface. After the device receives
 a DHCP address, it will automatically connect to the Shasta Cloud portal, apply
 the default switch profile (default profiles can be modified in the Shasta Cloud
 portal), and be provisioned as part of a Venue (also known as a Prisma SD-WAN
 site). Any additional switches and access points connected will automatically
 attach to the Venue moving forward. 

 To monitor the status of switches and access points,
 navigate to the CloudBlade Shasta LAN Monitor page. Here, you can view real-time connectivity, device health,
 performance metrics, and event logs, ensuring optimal network operation and
 troubleshooting capabilities. 

 General - The General tab displays the total number of connected access
 points, switches, and clients to the site. 

 Switches - Switches shows the switches connected to the venue and their
 status. 

 Access Points - Access Points shows the access points connected to the
 venue and their status. 

 Wireless Clients - The page lists the wireless clients connected to the
 site. 

 Wired Clients - The page lists the wired clients connected to the
 site. 

 Block Lists - The Block lists show the list of clients that are banned or
 quarantined from connecting to the network. This is useful when dealing with a
 compromised device that you need to quarantine from the rest of the network to
 prevent lateral threats from moving throughout your LAN and WAN. 

 To add a device to the list, click Add to specify the Mac
 address and click Apply . 

 You can unblock clients that were banned earlier by using the
 Delete button. 

 Notifications - The Notifications shows any incidents and alarms for the
 switching and wireless infrastructure. 

 Previous 

 Shasta LAN Integration 

 Next 

 Branch Microsegmentation 

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

 © 2026 Palo Alto Networks, Inc. All rights reserved.

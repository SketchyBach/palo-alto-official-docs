---
url: https://docs.paloaltonetworks.com/prisma-access/integration/integrate-third-party-sd-wans-with-prisma-access/cisco-meraki-sd-wan-solution-guide/integrate-prisma-access-with-cisco-meraki-sd-wan
fetched_at: 2026-08-13T17:26:47Z
source: palo-alto-main
---

# Integrate Prisma Access with Cisco Meraki SD-WAN (Aggregate Bandwidth) Clear

Integrate Prisma Access with Cisco Meraki SD-WAN (Aggregate Bandwidth) 

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

 Integrate Prisma Access with Cisco Meraki SD-WAN (Aggregate Bandwidth) 

 Updated on 

 Thu Mar 26 14:01:29 PDT 2026 

 Focus 

 Download PDF 

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

 Thu Mar 26 14:01:29 PDT 2026 

 Focus 

 Home 

 Prisma Access 

 Integrate Third-Party SD-WANs with Prisma Access 

 Cisco Meraki SD-WAN Solution Guide 

 Integrate Prisma Access with Cisco Meraki SD-WAN (Aggregate Bandwidth) 

 Download PDF 

 Prisma Access 

 Integrate Prisma Access with Cisco Meraki SD-WAN (Aggregate Bandwidth) 

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

 Integrate Prisma Access with Cisco Meraki SD-WAN (Site Based Licensing) 

 Next 

 Integrate Prisma Access with Cisco Meraki SD-WAN (Manual Integration) 

 Integrate Prisma Access with Cisco Meraki SD-WAN (Aggregate Bandwidth) 

 Learn to integrate Prisma Access with Cisco Meraki in the aggregate bandwidth
 licensing model. 

 Where Can I Use
 This? What Do I Need? 

 Prisma Access (Managed by Strata Cloud Manager) 

 Prisma Access license 

 Minimum Required Prisma Access Version : 2.1 Preferred or a later
 version 

 Active Cisco Meraki Dashboard subscription 

 Physical Cisco Meraki (MX or Z) devices or virtual Cisco
 Meraki (vMX) devices with a minimum version of 15.12 

 Prisma Access provides a flexible way to effectively secure Cisco Meraki SD-WAN
 deployments. By delivering security from the cloud and closer to the branch
 networks, Prisma Access lets you optimize networking and security with the same
 protections that you have at corporate headquarters. 

 As with other SD-WAN deployments, you secure the Cisco Meraki SD-WAN by onboarding a
 remote network using IPSec tunnels between the Cisco Meraki SD-WAN and Prisma
 Access. Using Prisma Access, you can secure SD-WAN devices at a branch, at a data
 center, or both, as shown in the topic Integrate Third-Party SD-WANs with
 Prisma Access . 

 You can onboard a remote network using IPSec tunnels between the Cisco Meraki SD-WAN
 device and Prisma Access automatically or manually. See the product requirements
 below for eligible devices that support this automation. The automation also
 supports devices in MX Warm Spare – high-availability pair mode. To onboard the
 Cisco Meraki networks manually, see Integrate Prisma Access with Cisco Meraki SD-WAN (Manual Integration) . Ensure you meet the following
 requirements before you integrate Prisma Access with Cisco Meraki: 

 Product Requirement 

 Prisma Access 

 Update your Prisma Access to version 2.1 Preferred or a
 later version. 
 Migrate remote networks to the aggregate bandwidth
 model. 

 Activate bandwidth license per compute
 location. 

 Cisco Meraki 

 Active Cisco Meraki Dashboard subscription 

 Physical Cisco Meraki (MX or Z) devices or virtual Cisco
 Meraki (vMX) devices with a minimum version of 15.12 in
 Cisco Meraki Hub or
 Spoke networks 

 Cisco Meraki devices should be in
 Appliance or
 Combined type networks 

 Cisco Meraki networks that have enabled the VPN
 Mode in the Site-to-Site
 VPN configurations 

 To secure a Cisco Meraki SD-WAN with Prisma Access, complete the following steps.

 Configure Cisco Meraki SD-WAN based on the requirements
 mentioned above. 

 If you have not already, allocate bandwidth for Prisma Access locations. 

 Go to Configuration NGFW and Prisma Access Configuration Scope Prisma Access Remote Networks Bandwidth Management . 

 Edit the Assigned Bandwidth for the remote
 network’s compute location. 

 Push the changes. 

 Go to Cisco Meraki Integration with Prisma Access 
 settings. 

 Select System Settings Integrations Third Party SD-WAN . 

 Locate the Cisco Meraki Integration with Prisma
 Access application. 

 Contact your Palo Alto Networks account team if you don’t see
 this integration option. 

 Enter the information needed to establish a connection between Prisma Access
 and Cisco Meraki by editing the Settings . 

 Generate Cisco Meraki API Key in Cisco Meraki dashboard , and
 enter the key information. 

 Enter the PSK Seed , which is a string used to
 derive pre-shared keys (PSKs) per tunnel. 

 ( Optional ) Enter an FQDN IKE identifier as the
 Local Identifier in the following syntax:
 name@domain.com 
 This identifier acts as a template to generate a unique ID per
 tunnel. 

 ( Optional ) Enter an FQDN IKE identifier different from the
 local identifier as the Remote Identifier in the
 following syntax: name@domain.com 

 Set the Admin State as
 Enabled . 
 You can set Admin State in the following
 modes: 
 Enabled : Enables the integration to
 discover new networks on Cisco Meraki that are eligible for
 tunnel formation with Prisma Access. Additionally, this verifies
 current configurations. 

 Disabled : Disable the integration to
 remove all configurations created, in Prisma Access as well as
 in Cisco Meraki, when a connection was set up between them. 

 Upon disabling, the system will
 initiate a complete teardown of all configurations and
 objects on both Prisma Access and Cisco Meraki. 

 Paused : When you pause the integration,
 you can no longer add new networks or remove any unconfigured
 networks. However, the current configurations don't change. 

 Check Connectivity to verify the
 connection. 

 Save the changes. 

 You can Save changes
 only after you Check Connectivity every time
 you change settings or configurations. 

 After you save the changes, you can see the Cisco Meraki networks
 eligible for tunnel formation with Prisma Access in
 Discovered Sites . Cisco Meraki networks
 are displayed as sites here. It might take some time to view the
 discovered sites. 

 Establish the tunnel setup between Prisma Access and Cisco Meraki
 devices. 

 View the discovered Cisco Meraki networks and their information by
 clicking the site count. 

 The integration checks every 3 hours for new Cisco Meraki networks.
 You can also initiate an on-demand site discovery . 

 ( Optional ) Select the nearest Prisma Access
 Location for the networks. 

 ( Optional ) Select IPSec Termination
 Node for each site. 

 If you select the same Prisma Access location for multiple networks,
 ensure to allocate the bandwidth equally by selecting different
 IPSec termination nodes for the networks sharing the same Prisma
 Access location. 

 The integration assigns Prisma Access
 location and IPSec termination nodes automatically. However, you can
 choose other Prisma Access locations or IPSec termination nodes if
 needed. 

 Select the Cisco Meraki network and toggle the
 Enable option to establish a tunnel formation
 with Prisma Access. 

 Update the changes. 

 You can view all
 the Enabled Sites and Configured
 Sites in the Cisco Meraki Integration with
 Prisma Access application. 

 Verify the changes in Prisma Access. 

 Go to Settings Prisma Access Setup Remote Networks . 

 Alternatively, you can click Remote Networks - Cisco
 Meraki Integration with Prisma Access > . 

 Verify the tunnel status. The integration creates remote networks
 automatically. Such remote networks have names in the following
 syntax:
 AUTO-Meraki- Network_Name 

 The configuration status of Cisco Meraki networks will be
 In sync . 

 View the IPSec Tunnel, IKE gateway, IKE Crypto profile, and IPSec
 Crypto profile details. 
 Select the remote network site to view these details. 

 IPSec Tunnel
 details: 

 Select Activity Log Viewer Common Audit to view Cisco Meraki Integration with Prisma
 Access logs. 

 The Destination Vendor specifies if the
 changes were made in Prisma Access or in the Cisco Meraki
 dashboard. 

 ( Optional ) View errors or warnings in
 Messages . 

 Verify the tunnel status in the Cisco Meraki dashboard. 

 Log in to the dashboard, and select Security & SD-WAN Monitor VPN Status . 

 Check the status for non-Meraki peer. 

 View the logs under Network-wide Event Log for non-Meraki event types. 

 Contact Cisco Systems support for any errors
 you see in the Cisco Meraki networks and dashboard. 

 On-Demand Site Discovery 

 You can initiate network discoveries anytime to view
 new networks added in the Cisco Meraki dashboard. You can also initiate network
 discoveries to resolve any misconfiguration in the integration-created objects. To
 initiate on-demand network discovery, perform the following steps: 

 Select Settings Integrations Third Party SD-WAN. . 

 Locate the Cisco Meraki Integration with Prisma
 Access application. 

 View the discovered Meraki networks and their information by clicking the
 site count. 

 Discover Sites to identify new eligible Cisco Meraki
 networks when required. 

 Previous 

 Integrate Prisma Access with Cisco Meraki SD-WAN (Site Based Licensing) 

 Next 

 Integrate Prisma Access with Cisco Meraki SD-WAN (Manual Integration) 

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

 Prisma Access 

 SASE 

 Strata Cloud Manager 

 Prisma SASE 

 Integrations 

 4.0 & Later 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

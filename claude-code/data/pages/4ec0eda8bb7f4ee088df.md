---
url: https://docs.paloaltonetworks.com/prisma-sd-wan/administration/prisma-sd-wan-sites-and-devices/returned-merchandise-authorization-rma/replace-a-prisma-sd-wan-ion-device/return-device-to-prisma-sd-wan
fetched_at: 2026-08-13T17:28:21Z
source: palo-alto-main
---

# Return the ION Device to Prisma SD-WAN Clear

Return the ION Device to Prisma SD-WAN 

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

 Return the ION Device to Prisma SD-WAN 

 Updated on 

 Mon Aug 10 04:14:37 PDT 2026 

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

 Mon Aug 10 04:14:37 PDT 2026 

 Focus 

 Home 

 Prisma SD-WAN 

 Prisma SD-WAN Administrator’s Guide 

 Prisma SD-WAN Sites and Devices 

 Returned Merchandise Authorization (RMA) 

 Replace a FIPS-enabled ION Device 

 Return the ION Device to Prisma SD-WAN 

 Download PDF 

 Prisma SD-WAN 

 Return the ION Device to Prisma SD-WAN 

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

 Replace a FIPS-enabled ION Device 

 Next 

 Upgrade ION Device Software 

 Return the ION Device to Prisma SD-WAN 

 Learn how to return the ION device to Prisma SD-WAN . Before you remove a
 device from a site, you need to remove the configuration from the device first. 

 Where Can I Use
 This? What Do I
 Need? 

 Prisma SD-WAN (Managed by Strata Cloud Manager ) 

 Prisma SD-WAN 

 You can return an ION device to Palo Alto Networks. Before you remove a device from a site, you
 need to remove the configuration from the device first, you need to specifically
 remove the circuits attached to interfaces. These checks are for protection against
 accidental misconfiguration. 

 You must decommission Prisma SD-WAN vION instances using the
 documented return or replace procedure before you delete them from the hosting
 environment. Deleting a vION instance without this process causes an
 inconsistent system state or unpredictable behavior. 

 Select Configuration Prisma SD-WAN ION Devices Claimed 

 Confirm that the replacement device is assigned to the site and is
 Online . Also, confirm that the RMA device is
 assigned but Offline . 

 Click the ellipsis menu for the RMA device and select Unassign
device from site . 

 Click OK to confirm removal of
the device from the site. 

 The state of the device displays Unassigning . 

 (Optional) Remove circuits attached
to interfaces. 

 If you see a message Site WAN interface id exists
in this element , then go to the interface configuration
and remove each of the circuits labels attached to any WAN interface
of the device. 

 Click the ellipsis menu and select Put back
in inventory . 

 Click Ok to confirm unclaiming
of the device. 

 Click the Unclaimed tab to view
the device. 

 The device is offline and the State changes To
return . 

 Click the ellipsis menu and select Return to Prisma
 SD-WAN . 

 Click Return to confirm returning
the device to Prisma SD-WAN . 

 The device is then removed from your inventory. 

 The
device is visible under Unclaimed with status To Return . 

 Remove circuits attached to interfaces 

 Select Configuration Prisma SD-WAN ION Devices Claimed 

 Click the ellipsis menu for a device and select Configure
the device . 

 Click Interfaces . 

 Select an interface. 

 For Circuit Label , click update . 

 When
you click update , the device removes the
circuits attached to the interface. 

 Click Save Port . 

 Repeat these steps for all interfaces—ports or bypass
pairs which have circuits attached. 

 Previous 

 Replace a FIPS-enabled ION Device 

 Next 

 Upgrade ION Device Software 

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

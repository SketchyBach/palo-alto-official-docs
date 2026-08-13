---
url: https://docs.paloaltonetworks.com/network-security/device-id/administration/advanced-device-id-overview/manage-advanced-device-id
fetched_at: 2026-08-13T16:38:14Z
source: palo-alto-main
---

# Manage Advanced Device-ID Clear

Manage Advanced Device-ID 

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

 Manage Advanced Device-ID 

 Updated on 

 Aug 28, 2025 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Network Security Docs 

 Security Policy 

 IPsec VPN 

 Decryption 

 Device-ID 

 Quantum Security 

 Quality of Service 

 Updated on 

 Aug 28, 2025 

 Focus 

 Home 

 Network Security 

 Advanced Device-ID Overview 

 Manage Advanced Device-ID 

 Download PDF 

 Network Security 

 Manage Advanced Device-ID 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Network Security Docs 

 Security Policy 

 IPsec VPN 

 Decryption 

 Device-ID 

 Quantum Security 

 Quality of Service 

 Previous 

 Deploy Advanced Device-ID 

 Next 

 Configure Device-ID 

 Manage Advanced Device-ID 

 Manage Advanced Device-ID , from editing and monitoring to deleting an
 Advanced Device-ID .

 Where Can I Use This? What Do I Need? 

 NGFW (Managed by PAN-OS or Panorama) 

 (Legacy) IoT Security (Standalone portal) 

 Device Security subscription for an advanced
 Device Security product (Enterprise Plus,
 Industrial OT, or Medical)

 If you want to update or delete an Advanced Device-ID object, you need to make
 the changes in Device Security . Before making changes to your 
 Advanced Device-ID objects in Device Security , check if any
 Security policy rules or policy rule recommendations in PAN-OS 
 are using the Advanced Device-ID objects. Any changes you make to an
 Advanced Device-ID object will affect the Security policy rules or policy rule
 recommendations using that Advanced Device-ID object.

 Edit an Advanced Device-ID Object 

 View Advanced Device-ID Associations for IoT Assets 

 View Assets by Advanced Device-ID in Device Security 

 View Assets by Advanced Device-ID in the Firewall 

 Remove an Advanced Device-ID Object from the Firewall 

 Remove an Advanced Device-ID Object from Device Security 

 When your firewalls receive traffic from overlapping IP address blocks,
 use multi-vsys support for Device-ID so that each vsys applies policy
 against the correct device. Multi-vsys support assigns device context segments 
 to firewalls and vsys, and their traffic gets scoped to the corresponding segment.
 The segment identifier helps scope device context to the correct firewall or vsys,
 preventing merged baselines when the same address appears in more than one part of
 your network.

 Edit an Advanced Device-ID Object 

 Edit an existing Advanced Device-ID to modify the name and description, or to
 update the matching criteria. You can change the matching criteria to more 
 accurately scope the asset traffic that you want to apply Security policy rules to.
 Changes to an Advanced Device-ID matching criteria affect existing Security
 policy rules that use the Advanced Device-ID .

 In your Device Security portal, navigate to Policies Device-ID and find the Advanced Device-ID object that you want
 to edit in the Device-ID table.

 Access the Edit Device-ID page.

 From the Device-ID page : On the row for the
 Advanced Device-ID that you want to update, click on the
 Edit (pencil) icon to go to the Edit
 Device-ID page.

 From the Device-ID details page : Click on the name
 of the Advanced Device-ID that you want to edit to go to its
 Device-ID details page. Click on the
 Edit icon next to the Advanced Device-ID 
 name to go to the Edit Device-ID page.

 Configure the changes you want to make.

 Optional If you make changes to the matching criteria,
 Test the criteria to see the list of devices that
 match the new criteria.

 When you're editing an Advanced Device-ID object, the table of
 Impacted Devices has two tabs: Added Devices and Removed Devices. These
 tabs show which new devices match the new criteria and which devices
 from the old criteria don’t match the new criteria.

 Verify that your updated matching criterion accurately captures the
 types of devices that you want to use in a Security policy.

 Save your changes.

 If your changes affect a large number of devices, you could see the
 Advanced Device-ID name with a Pending chip while the updates are
 applied.

 View Advanced Device-ID Associations for IoT Assets 

 You can see which IoT devices are associated with which Advanced Device-ID 
 objects in both Device Security and in the firewall. This helps you understand if
 multiple Advanced Device-ID objects, and therefore possibly multiple Security
 policy rules, might affect a given device on your network. This also helps you see how
 many assets can be affected by a single Advanced Device-ID .

 View Assets by Advanced Device-ID in Device Security 

 In the Device Security portal, you can view assets by one or more
 Advanced Device-ID associations. To see all assets associated with a
 single Advanced Device-ID , view the Device-ID 
 details page or use the filter function in the Assets inventory. If
 you want to view all assets associated with any Advanced Device-ID , or
 if you want to find assets associated with a combination of
 Advanced Device-ID objects, use the filter and query functionality on
 the Asset inventory under Assets Devices .

 In your Device Security portal, navigate to Policies Device-ID , and choose whether you want to view devices on the
 Advanced Device-ID details page or in the Asset inventory.

 Device-ID details Click on the name of the
 Advanced Device-ID you want to inspect to go to the
 Advanced Device-ID details page.

 The Advanced Device-ID details page displays a table of
 Matching Devices that are associated with the
 Advanced Device-ID . You can sort the table by columns, or you
 can search for a device by name.

 Asset inventory On the row for the Advanced Device-ID that
 you're looking for, click on the number under the No. of Devices field
 to go to the Asset inventory.

 This brings up the Asset inventory table with a filter applied for
 the selected Advanced Device-ID . The filtered inventory table
 displays all assets associated with the
 Advanced Device-ID .

 View Assets by Advanced Device-ID in the Firewall 

 On the firewall, you can view a list of IoT devices and see what
 Advanced Device-ID they are associated with.

 In your firewall, or in Panorama , navigate to
 Monitor IoT Devices Asset Inventory .

 Find the associated Advanced Device-ID for each asset by viewing
 the Device ID column.

 If an asset has multiple Advanced Device-ID objects associated
 with it, they all show up in the Device ID field as a
 comma-separated list.

 To adjust your view, you can sort the table by the Device ID column, or
 you can use the filter function to select which Advanced Device-ID 
 objects you want to find associated assets for.

 Remove an Advanced Device-ID Object from the Firewall 

 When you no longer need an Advanced Device-ID in a Security policy rule,
 remove the local Advanced Device-ID object from the firewall.

 Ensure that no Security policy rules are using the Advanced Device-ID 
 object you're removing locally. If a Security policy rule is using the
 Advanced Device-ID object, then clearing local Device-ID 
 will fail.

 Navigate to Objects Devices and select the Advanced Device-ID objects that you want
 to remove.

 Only select Advanced Device-ID objects for which the field Locally
 Exists is set to “Yes.” If any selected object has Locally Exists set
 to “No,” then the Clear Local Device-ID 
 action won’t be available.

 Clear Local Device-ID for all selected
 Advanced Device-ID objects.

 Verify that the local Advanced Device-ID objects no longer exist by
 checking that the Locally Exists field now displays “No” for the selected
 rows.

 When the Locally Exists field changes from “Yes” to “No,” this means
 that the Advanced Device-ID object no longer exists locally on the
 firewall. However, the Advanced Device-ID object still exists in
 Device Security . To delete an Advanced Device-ID from the list,
 Remove an
 Advanced Device-ID Object from .

 Remove an Advanced Device-ID Object from Device Security 

 When you no longer need an Advanced Device-ID object, remove the
 Advanced Device-ID object from Device Security to free up space for a
 new Advanced Device-ID object.

 Ensure that no Security policy rules are using the Advanced Device-ID 
 object that you're deleting. If you delete an Advanced Device-ID in
 Device Security , but the firewall is still using the
 Advanced Device-ID in a Security policy rule, then the Security policy
 rule will fail.

 In your Device Security portal, navigate to Policies Device-ID .

 Find the Advanced Device-ID that you want to delete, and click the
 Delete (trashcan) icon on the far right of the row
 to bring up the Remove Device-ID pop-up.

 Continue to confirm that you want to remove the
 Advanced Device-ID .

 Previous 

 Deploy Advanced Device-ID 

 Next 

 Configure Device-ID 

 On This Page 

 Activation & Onboarding 

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

 Service Provider 

 VM-Series 

 SASE 

 Prisma Access 

 Strata Multitenant Cloud Manager 

 AI-Powered ADEM 

 Prisma Access Monitoring and Visibility 

 Prisma SD-WAN 

 ION Devices 

 Next-Generation CASB 

 Cloud-Delivered Security Services 

 Advanced WildFire 

 Advanced URL Filtering 

 Advanced Threat Prevention 

 Advanced DNS Security 

 Device Security 

 Enterprise DLP 

 SaaS Security 

 Network Security 

 Shared Policy for NGFWs and Prisma Access 

 Visibility & Monitoring 

 Dashboards 

 Incidents and Alerts 

 Reports 

 Autonomous DEM 

 Best Practices 

 Best Practices Library 

 Experts Corner 

 Solutions Docs from Product Experts 

 Network Security 

 Advanced Device-ID Administration 

 Device-ID 

 Device-ID 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

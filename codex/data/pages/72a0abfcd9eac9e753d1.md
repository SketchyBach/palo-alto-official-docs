---
url: https://docs.paloaltonetworks.com/enterprise-dlp/getting-started/edit-the-cloud-content-settings
fetched_at: 2026-09-16T09:59:19Z
source: palo-alto-main
---

# Edit the Cloud Content Settings Clear

Updated on 

 Fri Sep 04 15:49:18 PDT 2026 

 Focus 

 Home 

 Enterprise DLP 

 Edit the Cloud Content Settings 

 Download PDF 

 Enterprise DLP 

 Edit the Cloud Content Settings 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Enterprise DLP Docs 

 Activation & Onboarding 

 Getting Started 

 Administration 

 Reference 

 Release Notes 

 New Features by OS Version 

 New Features by Month 

 Previous 

 Enable Role Based Access 

 Next 

 Enable Advanced Forwarding 

 Edit the Cloud Content Settings 

 Edit the Cloud Content Settings to specify the server to send your Enterprise Data Loss Prevention (E-DLP) files for inspection. 

 Where Can I Use This? What Do I Need? 

 NGFW (Managed by Panorama) 

 Prisma Access (Managed by Panorama) 

 Enterprise Data Loss Prevention (E-DLP) license 

 Review the Supported
 Platforms for details on the required license
 for each enforcement point. 

 By default, Enterprise Data Loss Prevention (E-DLP) is configured using a Cloud Content Fully Qualified Domain
 Name (FQDN) that automatically resolves to the closet Cloud Services server to
 inspect matching traffic. If you have specific data residency requirements, you can
 specify a regional Cloud Services server by editing the Cloud Content FQDN to which
 to send your Enterprise DLP traffic for inspection. 

 Log in to the Panorama web
 interface. 

 Select Device Setup Content-ID and select the Template associated with
 the managed devices using Enterprise DLP . 

 Edit the Cloud Content FQDN. 

 Edit the Cloud Content Settings . 

 Modify the Public Cloud Server based
on your data residency requirements. 

 Enterprise DLP data and data processing, including DLP incidents , reports,
 and DLP verdicts, are generated in the specified Public Cloud Server
 region. The Default 
 Enterprise DLP Public Cloud Server automatically resolves to
 the closest Public Cloud Server. 

 Review the list of 

 Public Cloud Server by Region 

 Default — hawkeye.services-edge.paloaltonetworks.com 

 The default Public Cloud Server automatically
 resolves to the closest Public Cloud Server to where
 the inspected traffic originated. If a new Public
 Cloud Server is deployed in a region closer to where
 the inspected traffic originated, Enterprise DLP data and data processing is generated in that new
 region. 

 APAC — apac.hawkeye.services-edge.paloaltonetworks.com 

 Australia — au.hawkeye.services-edge.paloaltonetworks.com 

 Brazil — hawkeye.services-edge.paloaltonetworks.com 

 Enterprise DLP stores scans forwarded traffic,
 stores traffic contents evidence, time of scan, and
 snippets in a Brazil storage. However, Enterprise DLP stores incident metadata in the
 region where
 you deployed your Strata Cloud Manager tenant. 

 Canada — ca.hawkeye.services-edge.paloaltonetworks.com 

 Europe — eu.hawkeye.services-edge.paloaltonetworks.com 

 France — fr.hawkeye.services-edge.paloaltonetworks.com 

 India — in.hawkeye.services-edge.paloaltonetworks.com 

 Japan — jp.hawkeye.services-edge.paloaltonetworks.com 

 Switzerland — hawkeye.services-edge.paloaltonetworks.com 

 Enterprise DLP stores scans forwarded traffic,
 stores traffic contents evidence, time of scan, and
 snippets in a Switzerland storage bucket. However,
 Enterprise DLP stores incident metadata in
 the region where
 you deployed your Strata Cloud Manager tenant. 

 United
 Kingdom — uk.hawkeye.services-edge.paloaltonetworks.com 

 United
 States — us.hawkeye.services-edge.paloaltonetworks.com 

 Public Cloud Server for FedRAMP 

 Enterprise DLP requires you add the following Public
 Cloud Server to successfully forward traffic for inspection
 and verdict rendering in FedRAMP environments. 

 FedRAMP
 Moderate — hawkeye.services-edge.pubsec-cloud.paloaltonetworks.com 

 FedRAMP
 High — gov-hawkeye.services-edge.paloaltonetworks.com 

 Click OK . 

 Commit and push the new configuration to your managed devices. 

 The Commit and Push command isn’t recommended for
 Enterprise DLP configuration changes. Using the
 Commit and Push command requires the
 additional and unnecessary overhead of manually selecting the impacted
 templates and managed devices in the Push Scope Selection. 

 Full configuration push from Panorama 

 Select Commit Commit to Panorama and Commit . 

 Select Commit Push to Devices and Edit
 Selections . 

 Select Device Groups and
 Include Device and Network
 Templates . 

 Click OK . 

 Push your configuration changes to
 your managed devices that are using Enterprise DLP . 

 Partial configuration push from Panorama 

 You must always include the temporary
 __dlp administrator when
 performing a partial configuration push. This is required to
 keep Panorama and Strata Cloud Manager in sync. 

 For example, if admin is logged in
 and making changes, they must select both
 admin and
 __dlp in the partial commit and
 push. 

 Select Commit Commit to Panorama . 

 Select Commit Changes Made By and then
 click the current Panorama admin user to select
 additional admins to include in the partial commit. 

 Select your logged-in admin user, the
 __dlp user, and any other
 admins whose changes to include. Click
 OK to continue. 

 Commit . 

 Select Commit Push to Devices . 

 Select Push Changes Made By and then
 click the current Panorama admin user to select
 additional admins to include in the partial push. 

 Select your logged-in admin user, the
 __dlp user, and any other
 admins whose changes to include. Click
 OK to continue. 

 Select Device Groups and
 Include Device and Network
 Templates . 

 Click OK . 

 Push your configuration changes to
 your managed devices that are using Enterprise DLP . 

 Previous 

 Enable Role Based Access 

 Next 

 Enable Advanced Forwarding

---
url: https://docs.paloaltonetworks.com/enterprise-dlp/release-notes/known-issues-in-enterprise-dlp-plugin-50/known-issues-in-enterprise-dlp-plugin-508
fetched_at: 2026-09-15T15:10:51Z
source: palo-alto-main
---

# Known Issues in Enterprise DLP Plugin 5.0.8 Clear

Updated on 

 Aug 18, 2026 

 Focus 

 Home 

 Enterprise DLP 

 Release Notes 

 Known Issues in Enterprise DLP Plugin 5.0 

 Known Issues in Enterprise DLP Plugin 5.0.8 

 Download PDF 

 Enterprise DLP 

 Known Issues in Enterprise DLP Plugin 5.0.8 

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

 Known Issues in Enterprise DLP Plugin 5.0.9 

 Next 

 Known Issues in Enterprise DLP Plugin 5.0.7 

 Known Issues in Enterprise DLP Plugin 5.0.8 

 Known issues in Enterprise Data Loss Prevention (E-DLP) plugin 5.0.8. 

 PLUG-24286 

 This issue is addressed in Enterprise DLP plugin 5.0.9. 

 The Panorama® management server allows you to delete an application group ( Objects DLP ) referenced by a data profile Object DLP Data Filtering Profile ) and doesn't provide a warning or error. After deletion, the data profile
 retains a reference to the deleted object, which can cause unexpected behavior when the
 data profile is evaluated. 

 PLUG-23898 

 This issue is addressed in Enterprise DLP plugin 5.0.9. 

 The Panorama® management server fails to push a data profile ( Object DLP Data Filtering Profile ) to NGFW when the data profile is exclusively attached to
 an AI Security profile and that AI Security profile ( Objects Security Profiles AI Security ) is not referenced by any Security profile. Enterprise DLP 
 inspection does not apply to traffic that matches AI security policies. 

 Workaround : Attach the data profile to at least one Security profile in addition
 to the AI Security profile. This ensures Panorama can successfully push the
 data profile to managed NGFW . 

 PLUG-23877 

 This issue is addressed in Enterprise DLP plugin 5.0.9. 

 Enterprise Data Loss Prevention (E-DLP) tenant provisioning for Panorama -managed deployments
 fail due to certificate validation checks for Enterprise DLP do not complete
 successfully. This causes Enterprise DLP profile operations that depend on
 certificate chain verification to fail. 

 PLUG-23490 

 This issue is addressed in Enterprise DLP plugin 5.0.9. 

 The Panorama® management server allows you to delete an application filter ( Objects Application Filters ) currently referenced by a data profile ( Object DLP Data Filtering Profile ) and doesn't provide a warning or error. After deletion, the data profile
 retains a reference to the deleted object, which can cause unexpected behavior when the
 data profile is evaluated. 

 PLUG-21528 

 This issue is addressed in Enterprise DLP plugin 6.0.2. 

 On the Panorama® management server , the menu node for data filtering profiles ( Objects DLP Data Filtering Profiles also displays under Security Profiles ( Objects Security Profiles ). 

 PLUG-20948 

 This issue is addressed in Enterprise DLP plugin 6.0.2. 

 On the Panorama® management server , data filtering profiles ( Objects DLP Data Filtering Profiles ) fail to open and display the following error: 

 Operation Failed URL:
 https://enforcer-hawkeye.services-edge.paloaltonetworks.com:443/v1/dlp/data-profiles/
 - Server certificate is revoked. Please contact PaloAlto Networks Inc. support for
 more info. 

 PLUG-6145 

 On the Panorama management server, you
cannot create an admin role ( Panorama Admin Roles ) to control access
to Enterprise Data Loss Prevention (DLP) filtering settings and
snippet configuration ( Device Setup DLP ). 

 PAN-144897 

 Enterprise Data Loss Prevention (DLP)
data profile Thread ID/Name filter is not available
when you configure a custom report ( Manage Manage Custom Reports ) on the
Panorama management server or locally on a firewall leveraging Enterprise
DLP. 

 DSS-17763 

 On the Panorama management server, custom data profiles ( Objects DLP Data Filtering Profiles ) are not synchronized to the DLP cloud service if you have an active
 CASB-X license. This prevents you being able to associate the data profile with a
 Security policy rule and displays the error Data Profile does not
 exist . 

 Workaround : Contact Palo Alto Networks Support to restore synchronization
 functionality between the DLP cloud service and Panorama. 

 Previous 

 Known Issues in Enterprise DLP Plugin 5.0.9 

 Next 

 Known Issues in Enterprise DLP Plugin 5.0.7

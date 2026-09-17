---
url: https://docs.paloaltonetworks.com/prisma-sd-wan/deployment/upgrade-on-premises-controller/download-the-appdef
fetched_at: 2026-09-16T07:48:12Z
source: strata-and-sase
---

# Download the Appdef Clear

Updated on 

 Wed Feb 25 07:20:45 PST 2026 

 Focus 

 Home 

 Prisma SD-WAN 

 Upgrade On-Premises Controller 

 Download the Appdef 

 Download PDF 

 Prisma SD-WAN 

 Download the Appdef 

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

 Upgrade the Device Software 

 Next 

 Upgrade a Pre-Owned Device 

 Download the Appdef 

 Learn to work with appdefs. 

 Where Can I Use
 This? What Do I Need? 

 Prisma SD-WAN 

 Prisma SD-WAN 

 Application Definition (appdef) is a software package that enables ION devices to
 perform real-time application recognition. 

 Download the required appdef bundles
 and upload them using the Operator console. 

 Example of the bundle names:

 consolidated_app_defs_8547-7317_000003_000061.tgz consolidated_app_defs_9577-7316_000003_000068.tgz 
 The
 tgz files contain the following bundles: 

 app_defs_8547-7317_000003_000061.tar.gz 

 codecs_8547-7317_000003_000061.tar.gz 

 ngpcap-cgnx-8547-7317.tar.gz 

 policies_8547-7317_000003_000061.tar.gz 

 Prioritypolicies_8547-7317_000003_000061.tar.gz 

 To extract and verify the files, run the following command: 
 tar -xvzf consolidated_app_defs_8547-7317_000003_000061.tgz

 Log in to the Operator console and navigate to Configuration Image Management . 

 Select AppDefs and click Upload . 

 After the AppDefs is successfully uploaded, the uploaded version is
 reflected in the table with the Uploaded status. 

 Click Create . 

 After the AppDefs is successfully created, click
 Allocate . 

 You will get a success notification after allocation is complete. 

 Previous 

 Upgrade the Device Software 

 Next 

 Upgrade a Pre-Owned Device

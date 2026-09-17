---
url: https://docs.prismacloud.io/public-sector/release-findings/methodology
fetched_at: 2026-09-16T13:37:44Z
source: prisma-cloud
---

# Methodology | Prisma Cloud arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Compute Edition 

 Public Sector 

 Release Findings 

 Methodology 

 Every release of Prisma Cloud Compute we perform an SCAP scan of the Console and Defender images and post the results here. This process is based upon the U.S. Air Force’s Platform 1 "Repo One" OpenSCAP scan of the Prisma Cloud Compute images. We then compare the scan results to IronBank’s latest approved UBI8-minimal scan findings, any discrepancies are addressed or justified and the results are posted here. 

 The scanning process is as follows: 

 Build RedHat Enterprise Linux server 

 Install openscap-utils package 

 Pull the latest SCAP content from the Compliance as Code GitHub repository. 

 Download the most current binary archive from the repository releases page, eg - the scap-security-guide-<latest version>.tar.bz2 or scap-security-guide-<latest version>.zip files. The source file archives require additional build steps before they can be used to scan an image. 

 Once the archive file has been downloaded, expand it to create the subdirectory scap-security-guide-<latest version> . For example, if the current version is 0.1.67 , the files will be unpacked to scap-security-guide-0.1.67 . 

 Scan the Console and Defender images 

 Ask Copy 

 oscap-podman <imageID> xccdf eval \ 
 --fetch-remote-resources \ 
 --profile xccdf_org.ssgproject.content_profile_stig \ 
 --report scan_report_name.html scap-security-guide-<latest version>/ssg-rhel8-ds.xml 

 The text <imageID> should be replaced by the ID of the target image of the SCAP scan 

 The text scap-security-guide-<latest version> should be replaced by path to the directory where the archive was unpackage, eg - scap-security-guide-0.1.67 in the example given above. 

 The report file name, eg - scan_report.html in the command, is arbitrary and can be customized as desired. 

 Compare findings against the IronBank daily issued UBI8-minimal image. 

 Previous Release Findings 

 Next 31.01.123 Scan Results 

 Last updated 3 months ago 

 Was this helpful?

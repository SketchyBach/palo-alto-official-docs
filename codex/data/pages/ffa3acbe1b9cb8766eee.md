---
url: https://docs.prismacloud.io/admin-guide/upgrade/upgrade-onebox
fetched_at: 2026-09-16T13:36:18Z
source: prisma-cloud
---

# Onebox | Prisma Cloud arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Compute Edition 

 Admin Guide 

 34 

 Upgrade 

 Onebox 

 Upgrade Prisma Cloud Onebox. First upgrade Console. Console will then automatically upgrade all deployed Defenders for you. 

 If Console fails to upgrade one or more Defenders, manually upgrade your Defenders. 

 You must manually upgrade App-Embedded Defenders. 

 Upgrading Console 

 To upgrade Console, rerun the install script for the latest version of Prisma Cloud. Use this method for any Console that was originally installed with the twistlock.sh script. 

 Download the latest recommended release. 

 Unpack the downloaded tarball. 

 Optional: you may wish to unpack the tarball to a different folder than any previous tarballs. 

 Ask Copy 

 $ mkdir twistlock_<VERSION> 
 $ tar -xzf prisma_cloud_compute_edition_<VERSION>.tar.gz -C twistlock_<VERSION>/ 

 The setup package contains updated versions of twistlock.sh and twistlock.cfg . 

 Check the version of Prisma Cloud that will be installed: 

 Ask Copy 

 $ grep DOCKER_TWISTLOCK_TAG twistlock.cfg 

 Upgrade Prisma Cloud while retaining your current data and configs by using the -j option. The -j option merges your current configuration with any new configuration settings in the new version of the software. 

 You must use the same install target in your upgrade as your original installation. There are two install targets: onebox and console , where onebox installs both Console and Defender onto a host and console just installs Console. 

 To upgrade your onebox install, run: 

 Ask Copy 

 $ sudo ./twistlock.sh -syj onebox 

 To upgrade your console install, run: 

 Ask Copy 

 $ sudo ./twistlock.sh -syj console 

 Go to Manage > Defenders > Manage and validate that Console has upgraded your Defenders. 

 Previous Upgrade process 

 Next Kubernetes 

 Last updated 3 months ago 

 Was this helpful?

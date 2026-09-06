---
url: https://cortex-docs.paloaltonetworks.com/xsoar-6-administrator-guide/6.13/onboard-cortex-xsoar/engines/engine-installation/install-a-signed-engine
fetched_at: 2026-09-06T10:44:32Z
source: cortex-platform
---

# Install a Signed Engine | 6.13 | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSOAR 6 

 Cortex XSOAR 6 Administrator Guides 

 6.13 

 Onboard Cortex XSOAR 

 Engines 

 Engine Installation 

 Cortex XSOAR 6.13 

 Install a Signed Engine 

 Install a signed engine in Cortex XSOAR 6.13. 

 Some systems require a signed RPM file for installation. If you need a signed RPM file for installing an engine, you need to download the engine file from the download server. 

 When you download Cortex XSOAR for the first time, you are sent a link to the download server. You can update the link to include a signed engine file and a public certificate key. 

 After you download and install the signed engine, you need to create an engine (a configuration file only) in the Cortex XSOAR server. In the engine environment, you need to replace the d1.conf file with the configuration file created in the Cortex XSOAR server. 

 Note 

 If you do not need a signed engine, follow the procedure in Install a Cortex XSOAR Engine . 

 Copy the Cortex XSOAR build number by going to Settings → ABOUT → Version (under Build ). 

 Download the signed engine file by running the following command. 

 wget --content-disposition ‘ <download link> ’ 

 Use the original URL that was sent to you when installing Cortex XSOAR, by adding downloadName=<version><build-number>_signed_engine_rpm at the end of the URL. For example: 

 wget --content-disposition 'https://download.demisto.com/download-params?token=aBCiXjNoSSxy&email=user@panw.com&downloadName=6_12_0_493375_signed_engine_rpm' 

 Use the build number copied in step 1. 

 The signed engine file downloads and you should receive the following confirmation message similar to the following: 

 ‘signed_d1_d1_signed-6.12.0_493375-1.x86_64.rpm’ saved 

 Download the signed public key, by adding downloadName=signed_public_key to the same URL as step 2. 

 For example, wget --content-disposition ‘https://download.demisto.com/download-params?token=aBCiXjNoSSxy&email=user@demisto.com&downloadName=signed_public_key&eula=accept’ 

 The signed public key file downloads and you should receive the following confirmation message similar to the following: 

 ‘sign_public.key’ saved 

 (Ubuntu/DEB) Install the alien command. 

 sudo apt-get update 

 sudo apt-get -y install alien 

 Import the signed public key to the local signed engine. 

 For example, run the sudo rpm --import sign_public.key . 

 (Optional) If you encounter errors, you may need to manually install the makeself package. For example, to install makeself, run the sudo yum install makeself command. 

 You may need to install the Fedora EPEL Repository before installing makeself. 

 Install the signed RPM file on the machine where you want to install the engine, by running the following command. 

 sudo rpm -i`` `` <file-name> .rpm 

 For example, sudo rpm -i signed_d1_d1_signed-6.12_493375-1.x86_64.rpm 

 (Ubuntu/DEB) Run the alien command. For example, sudo alien -i signed_d1_d1_signed-6.12_493375-1.x86_64.rpm --scripts 

 In Cortex XSOAR, create a configuration file. 

 Select Settings → Engines → Create New Engine . 

 Type a meaningful name for the engine. 

 The name does not have to match the engine you installed in step 7. 

 In the Installer type field, select Configuration . 

 Click Create New Engine . 

 In the machine you installed the signed RPM file, replace the file /usr/local/demisto/d1.conf file with the file you created in step 8. 

 Start the engine by running the following command: 

 sudo systemctl start d1 

 (Ubuntu/DEB) sudo service d1 restart 

 Previous Install a Cortex XSOAR Engine 

 Next Install a Cortex XSOAR Engine Offline 

 Last updated 1 month ago 

 Was this helpful?

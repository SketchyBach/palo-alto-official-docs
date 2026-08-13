---
url: https://docs.paloaltonetworks.com/advanced-wildfire/administration/configure-advanced-wildfire-analysis/verify-wildfire-submissions/test-a-sample-malware-file
fetched_at: 2026-08-13T15:22:37Z
source: palo-alto-main
---

# Test a Sample Malware File Clear

Test a Sample Malware File 

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

 Test a Sample Malware File 

 Updated on 

 Jul 30, 2026 

 Focus 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 Filter

 Expand All 
 | 
 Collapse All 

 Advanced WildFire 

 Administration 

 Appliance 

 Updated on 

 Jul 30, 2026 

 Focus 

 Home 

 Advanced WildFire Powered by Precision AI™ 

 Configure Advanced WildFire Analysis 

 Verify Sample Submissions 

 Test a Sample Malware File 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 Advanced WildFire Powered by Precision AI™ 

 Test a Sample Malware File 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Advanced WildFire 

 Administration 

 Appliance 

 Previous 

 Verify Sample Submissions 

 Next 

 Verify File Forwarding 

 Test a Sample Malware File 

 Where Can I Use
This? What Do I Need? 

 NGFW (Managed by PAN-OS or Panorama) 

 VM-Series 

 CN-Series 

 Advanced
WildFire or WildFire License 

 Palo Alto Networks provides sample malware files
that you can use to test an Advanced WildFire configuration. Take
the following steps to download the malware sample file, verify
that the file is forwarded for Advanced WildFire analysis, and view
the analysis results. 

 Download one of the malware test files. You can
select from PE, APK, MacOSX, and ELF. 

 Before downloading an encrypted WildFire sample malware file, you must temporarily disable the
 *.wildfire.paloaltonetworks.com and wildfire.paloaltonetworks.com
 entries from the exclude from decryption list on the Device >
 Certificate Management > SSL Decryption Exclusion page,
 otherwise the sample will not download correctly. After conducting a
 verification test, be sure to re-enable the
 *.wildfire.paloaltonetworks.com and wildfire.paloaltonetworks.com
 entries on the SSL decryption exclusion page. 

 If you have SSL decryption enabled on the firewall,
use one of the following URLs: 

 PE— https://wildfire.paloaltonetworks.com/publicapi/test/pe 

 APK— https://wildfire.paloaltonetworks.com/publicapi/test/apk 

 MacOSX— https://wildfire.paloaltonetworks.com/publicapi/test/macos 

 ELF— wildfire.paloaltonetworks.com/publicapi/test/elf 

 If you do not have SSL decryption enabled on the firewall,
use one of the following URLs instead: 

 PE— http://wildfire.paloaltonetworks.com/publicapi/test/pe 

 APK— http://wildfire.paloaltonetworks.com/publicapi/test/apk 

 MacOSX— http://wildfire.paloaltonetworks.com/publicapi/test/macos 

 ELF— wildfire.paloaltonetworks.com/publicapi/test/elf 

 The test file is named wildfire-test- file_type -file.exe
and each test file has a unique SHA-256 hash value. 

 You
can also use the WildFire API to retrieve a malware test file. See
the WildFire API Reference for details. 

 On the firewall web interface, select Monitor WildFire Submissions to
confirm that the file was forwarded for analysis. 

 Please wait at least five minutes for analysis results
to be displayed for the file on the WildFire Submissions page.
The verdict for the test file will always display as malware. 

 Previous 

 Verify Sample Submissions 

 Next 

 Verify File Forwarding 

 On This Page 

 Activation & Onboarding 

 Strata Cloud Manager 

 Activate a License or Product 

 Strata Logging Service 

 Device Associations 

 Hub 

 Identity and Access Management 

 Tenant Management 

 Next-Generation Firewalls 

 AIOps for NGFW 

 Cloud Management for NGFWs 

 Firewalls 

 PAN-OS 

 Panorama 

 VM-Series 

 SASE 

 Prisma Access 

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

 Security Policy 

 Visibility & Monitoring 

 Dashboards 

 Incidents and Alerts 

 Reports 

 11.0 

 10.1 

 Network Security 

 PAN-OS 

 10.2 

 Advanced Wildfire 

 Administration 

 Prisma Access 

 9.1 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

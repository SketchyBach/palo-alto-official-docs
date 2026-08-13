---
url: https://docs.paloaltonetworks.com/ngfw/release-notes/12-1/changes-to-default-behavior/changes-to-default-behavior-in-pan-os-12-1
fetched_at: 2026-08-13T16:55:43Z
source: palo-alto-main
---

# Changes to Default Behavior in PAN-OS 12.1 Clear

Changes to Default Behavior in PAN-OS 12.1 

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

 Changes to Default Behavior in PAN-OS 12.1 

 Updated on 

 Aug 6, 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Next-Generation Firewall Docs 

 Getting Started 

 Administration 

 Networking 

 Quick Start 

 Reference 

 Incidents & Alerts 

 Release Notes 

 Select a Document 

 PAN-OS 12.2 

 PAN-OS 12.1 

 PAN-OS 11.2 

 PAN-OS 11.1 

 PAN-OS 11.0 (EoL) 

 PAN-OS 10.2 

 PAN-OS 10.1 (EoL) 

 PAN-OS 10.0 (EoL) 

 PAN-OS 9.1 (EoL) 

 PAN-OS 9.0 (EoL) 

 PAN-OS 8.1 (EoL) 

 Help 

 Select a Document 

 PAN-OS 12.2 

 PAN-OS 12.1 

 PAN-OS 11.2 

 PAN-OS 11.1 

 PAN-OS 10.2 

 PAN-OS 10.1 

 New Features 

 Updated on 

 Aug 6, 2026 

 Focus 

 Home 

 Next-Generation Firewall 

 Changes to Default Behavior 

 Changes to Default Behavior in PAN-OS 12.1 

 Download PDF 

 Next-Generation Firewall 

 Changes to Default Behavior in PAN-OS 12.1 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Next-Generation Firewall Docs 

 Getting Started 

 Administration 

 Networking 

 Quick Start 

 Reference 

 Incidents & Alerts 

 Release Notes 

 Select a Document 

 PAN-OS 12.2 

 PAN-OS 12.1 

 PAN-OS 11.2 

 PAN-OS 11.1 

 PAN-OS 11.0 (EoL) 

 PAN-OS 10.2 

 PAN-OS 10.1 (EoL) 

 PAN-OS 10.0 (EoL) 

 PAN-OS 9.1 (EoL) 

 PAN-OS 9.0 (EoL) 

 PAN-OS 8.1 (EoL) 

 Help 

 Select a Document 

 PAN-OS 12.2 

 PAN-OS 12.1 

 PAN-OS 11.2 

 PAN-OS 11.1 

 PAN-OS 10.2 

 PAN-OS 10.1 

 New Features 

 Previous 

 Changes to Default Behavior 

 Next 

 Limitations 

 Changes to Default Behavior in PAN-OS 12.1 

 What default behavior changes impact PAN-OS 12.1? 

 The following table details the changes in default behavior upon upgrade to
 PAN-OS® 12.1. You may also want to review the Upgrade/Downgrade Considerations before
 upgrading to this release. 

 Feature Change 

 IKE protocol version support 

 We have changed the default IKE protocol version support from IKEv1
 to IKEv2. 

 If you have not configured the IKE protocol version in the IKE
 gateway configuration, then PAN-OS supports the IKEv2 protocol
 version by default. 

 For VPN clusters, PAN-OS supports IKEv2 only
 mode by default and the support for
 IKEv1 only mode and IKEv2
 preferred mode configuration are removed. 

 Maintenance Mode Password Change 

 After upgrading to 12.1, you must change the default maintenance
 password using the following CLI commands: 

 Generate the <passwd-hash>: request password-hash
 password <password> 

 Update the maintenance password: set deviceconfig system
 maintenance-user password-hash <passwd-hash> 

 The firewall serial number is no longer valid for maintenance
 use. 

 OpenConfig 

 In 12.1.2, the OpenConfig 2.1.4 plugin will be bundled with
 the PAN-OS release. If you upgrade to 12.1.2, the plugin will only
 be reinstalled automatically if you had manually installed it in the
 previous release. For security reasons, if you had autoinstalled in
 the prior release, the plugin will not be installed. 

 Minimum Memory Requirements for Software Firewalls (VM-Series and
 Prisma AIRS) 

 A minimum of 8GB of memory is required to upgrade to PAN-OS version
 12.1.2 from any prior PAN-OS version. If you are upgrading to PAN-OS
 12.1.2 with memory configurations of 8GB-14GB, then the session capacity reduces.

 Change in Maximum Supported Sessions on Software Firewalls
 (VM-Series and Prisma AIRS ) 

 Starting with PAN-OS 12.1.2, the maximum number of supported sessions
 has been reduced. 

 For Flex Licenses: 

 8 GB: 64K sessions 

 9 GB: 128K sessions 

 10 GB: 128K sessions 

 12 GB: 256K sessions 

 14 GB: 512K sessions 

 For Fixed Licenses: 

 VM-100: 64K 

 VM-300: 128K 

 Minimum Disk Size for VM Panorama 

 Starting in PAN-OS 12.1.2, the VM Panorama requires a minimum 224GB
 disk. Before upgrading to 12.1.2, you must perform a disk migration
 to 224GB. 

 New Confirmation Prompt When Loading a Saved Configuration using
 the CLI and Web Interface 

 A new prompt for confirmation is displayed when a saved config is
 loaded. 

 This new prompt was added to avoid losing uncommitted changes in case
 of system/process restart. We recommend that you commit pending
 changes both before and after partial config load operations. 

 TLSv1.3 Decryption with P-192 Curve 

 Until PAN-OS 11.2, the firewall successfully decrypted SSL
 Forward Proxy sessions where a client and server negotiated a
 TLSv1.3 connection using only the P-192 curve. 

 Starting in PAN-OS 12.1.2, these sessions will
 fail ,because the firewall will no longer be able to decrypt
 this specific use of P-192 with TLSv1.3. This will result in a
 session failure for clients that exclusively use this weak
 configuration. 

 Workaround: S​​et TLSv1.2 as the maximum supported TLS version in the
 decryption profile. Apply the profile to the decryption policy rules
 that handle traffic from clients to servers that only negotiate the
 P-192 curve. 

 Show System Resources Output Changed 

 show system resources process names get
 truncated at 8 characters compared to 10 characters in earlier
 releases. The change was due to a kernel upgrade in PAN-OS
 12.1.2. 

 SSH Server Host Key Algorithm Restriction in FIPS-CC Mode 

 Starting in PAN-OS 12.1.8, firewalls running in FIPS-CC mode
 exclusively advertise rsa-sha2-512 for RSA host
 key authentication on the management SSH server. The previously
 supported ssh-rsa and
 rsa-sha2-256 algorithms are no longer permitted
 in FIPS-CC mode. This change is not applicable to normal
 (non-FIPS-CC) operation mode. 

 This restriction is required to comply with the collaborative
 Protection Profile for Network Devices Version 4.0
 (NDcPPv4.0e). 

 SSH clients that do not support rsa-sha2-512 
 (OpenSSH older than 7.2 or SecureCRT older than 9.0) will fail to
 connect to a firewall running PAN-OS 12.1.8 or later in FIPS-CC
 mode using default RSA host keys. 

 Workaround: Configure the default SSH host key for management
 SSH to an ECDSA key type and commit. ECDSA-based host key
 authentication is not restricted by this change. 

 Previous 

 Changes to Default Behavior 

 Next 

 Limitations 

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

 Release Notes 

 Network Security 

 PAN-OS 

 Next-Generation Firewall 

 12.1 

 Feature 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

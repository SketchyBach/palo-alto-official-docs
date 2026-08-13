---
url: https://docs.paloaltonetworks.com/network-security/quality-of-service/administration/configure-lockless-qos
fetched_at: 2026-08-13T16:38:20Z
source: palo-alto-main
---

# Configure Lockless QoS Clear

Configure Lockless QoS 

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

 Configure Lockless QoS 

 Updated on 

 Sep 24, 2025 

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

 Sep 24, 2025 

 Focus 

 Home 

 Network Security 

 Configure Lockless QoS 

 Download PDF 

 Network Security 

 Configure Lockless QoS 

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

 Configure QoS 

 Next 

 Configure QoS for a Virtual System 

 Configure Lockless QoS 

 Configure Lockless QoS for improved QoS performance that results in improved
 throughput and latency. Available on selected PA-Series models. 

 Where Can I Use This? What Do I Need? 

 NGFW 

 No separate license required for QoS when using NGFWs 

 The Palo Alto Networks firewalls supports two types of QoS: 
 Legacy QoS —In legacy QoS mode, the firewall
 supports both QoS and non-QoS traffics, where the legacy QoS shapes the QoS
 traffic. 

 ( PAN-OS
 10.2.5 and later 10.2 releases ) Lockless QoS —In
 Lockless QoS mode, the firewall supports both QoS and non-QoS traffics,
 where the Lockless QoS shapes the QoS traffic. The firewall shapes the
 packets from the same interface (or port) by the same core for achieving
 Lockless QoS. For firewalls with higher bandwidth QoS requirements, the
 Lockless QoS dedicates CPU cores to the QoS function that improves QoS
 performance, resulting in improved throughput and latency. 
 In Lockless
 QoS mode, as the members in a LAG have to be mapped to the same core,
 the overall LAG QoS throughput is limited by the per core
 throughput. 

 The QoS throughput on a 100G, 40G, and 25G port is limited to a
 single core throughput. 

 Whenever more than two ports are mapped to a single core, the
 QoS throughput of that core is shared. 

 We support Lockless QoS mode on the following firewall models.
 Regardless of the type of QoS configured, the maximum bandwidth (maximum
 rate of transfer) you can allocate at the port level and QoS profile
 level for the following platforms is 10G. 

 PA-3410 firewall 

 PA-3420 firewall 

 PA-3430 firewall 

 PA-3440 firewall 

 PA-5410 firewall 

 PA-5420 firewall 

 PA-5430 firewall 

 ( PAN-OS
 11.1 and later releases ) PA-5440
 firewall 

 ( PAN-OS
 11.1 and later releases ) PA-5445
 firewall 

 While several PA-5400 Series
 firewall models support Lockless QoS, the PA-5450 firewall does not. 

 Follow these steps to enable, disable, and view the status of the Lockless QoS. 

 Access the CLI 

 Use the operational command set lockless-qos yes to
 enable the Lockless QoS to improve the QoS performance. Commit and reboot the
 firewall for the changes to take effect. 

 username@hostname> set lockless-qos yes 
Changing lockless-qos enable requires reboot of the device. Do you want to continue? (y or n) 

 If you want to configure Lockless QoS where the legacy QoS is already
 configured, you can do so by running the set lockless-qos
 yes command and reboot your firewall. If you don't run this
 command, the firewall retains the legacy QoS behavior. When you disable the
 Lockless QoS, the firewall falls back to the legacy QoS behavior, if you
 have already configured legacy QoS before enabling Lockless QoS. 

 Use the operational command set lockless-qos no to
 disable the Lockless QoS. As a result, Lockless QoS isn't supported on the
 firewall. 

 username@hostname> set lockless-qos no 

 Use the operational command show lockless-qos enable to
 view the Lockless QoS enable status. 

 username@hostname> show lockless-qos enable 
lockless-qos enable : yes 

 Use the operational command show lockless-qos
 if-core-mapping to view the list of ports with the number of
 cores allocated for the QoS process by the Lockless QoS. 

 username@hostname> show lockless-qos if-core-mapping 
interface qos-core
ethernet1/41 71
ethernet1/42 72 

 ( PAN-OS 11.1.3 and later releases ) Use the operational command
 show lockless-qos core-num to view the number of CPU
 cores allocated for the lockless QoS feature. You will be able to view the
 number of CPU cores allocated for lockless QoS, only when the lockless QoS
 feature is enabled. 

 username@hostname> show lockless-qos core-num 
lockless-qos core-num : 6 

 The lockless QoS core number provides the number of CPU cores used by the
 firewall for lockless QoS. This information gives an approximate idea about an
 expected performance degradation on the firewall when this feature is
 enabled. 

 Previous 

 Configure QoS 

 Next 

 Configure QoS for a Virtual System 

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

 QoS 

 PAN-OS 

 Next-Generation Firewall 

 Quality of Service 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

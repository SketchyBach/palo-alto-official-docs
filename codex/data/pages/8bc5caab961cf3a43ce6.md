---
url: https://docs.paloaltonetworks.com/iot/integration/attribute-reference/attribute-reference-qualys
fetched_at: 2026-09-15T15:14:40Z
source: palo-alto-main
---

# Qualys Attribute Reference Clear

Updated on 

 Mon Aug 17 11:22:37 PDT 2026 

 Focus 

 Home 

 Device Security 

 Device Security Integration Guide 

 Attribute Reference 

 Qualys Attribute Reference 

 Download PDF 

 Device Security 

 Qualys Attribute Reference 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Device Security Docs 

 Activation & Onboarding 

 Getting Started 

 Administration 

 Enterprise Administration 

 Integrations 

 Release Notes 

 Best Practice 

 New Features 

 Previous 

 Philips Focal Point Attribute Reference 

 Next 

 Rapid7 Attribute Reference 

 Qualys Attribute Reference 

 This reference lists the attributes that Device Security collects from Qualys,
 their names as stored in Device Security , and the Device Security fields they map to.

 When Device Security integrates with Qualys , it enhances vulnerability
 management for your devices. The attributes in this reference cover Qualys appliance
 records, global asset view data, device details from vulnerability scans, and individual
 vulnerability findings. 

 The third-party attribute name in Device Security refers to the attribute name
 as it appears in the Assets Inventory table and in Query Engine. This follows the format
 of third-party-name . attribute-name .
 When viewing the attribute name in the Assets Inventory table column selector or on a
 Device Details page, where the third-party name can be found as a header for the
 attributes section, then the third-party name is removed from the attribute name.

 For example, micrsoft_defender_xdr.macAddress would appear in the
 Query Builder and in the Assets Inventory table, but under Device Details Attributes Integration Specific Attributes Microsoft Defender , the attribute would appear as macAddress .

 Appliance List Attributes 

 Device Security collects appliance list attributes from Qualys. The following table lists each Qualys attribute, its name as stored in Device Security , and the Device Security field it maps to (if applicable).

 Qualys Attribute 

 Device Security Attribute Name 

 Device Security Common Attribute* 

 Description 

 INTERFACE_SETTINGS.DNS.DOMAIN 

 — 

 domain 

 DOMAIN 

 INTERFACE_SETTINGS.IP_ADDRESS 

 — 

 IP Address; id 

 IP ADDRESS 

 ACTIVATION_CODE 

 qualys.scanner.activation_code 

 — 

 ACTIVATION CODE 

 ASSET_GROUP_COUNT 

 qualys.scanner.asset_group_count 

 — 

 ASSET GROUP COUNT 

 ASSET_GROUP_LIST 

 qualys.scanner.asset_group_list 

 — 

 ASSET GROUP LIST 

 COMMENTS 

 qualys.scanner.comments 

 — 

 COMMENTS 

 HEARTBEATS_MISSED 

 qualys.scanner.heartbeats_missed 

 — 

 HEARTBEATS MISSED 

 ID 

 qualys.scanner.id 

 — 

 ID 

 LAST_UPDATED_DATE 

 qualys.scanner.last_updated_date 

 — 

 LAST UPDATED DATE 

 MAX_CAPACITY_UNITS 

 qualys.scanner.max_capacity_units 

 — 

 MAX CAPACITY UNITS 

 ML_LATEST 

 qualys.scanner.ml_latest 

 — 

 ML LATEST 

 MODEL_NUMBER 

 qualys.scanner.model_number 

 — 

 MODEL NUMBER 

 NAME 

 qualys.scanner.name 

 — 

 NAME 

 POLLING_INTERVAL 

 qualys.scanner.polling_interval 

 — 

 POLLING INTERVAL 

 RUNNING_SCAN_COUNT 

 qualys.scanner.running_scan_count 

 — 

 RUNNING SCAN COUNT 

 RUNNING_SLICES_COUNT 

 qualys.scanner.running_slices_count 

 — 

 RUNNING SLICES COUNT 

 SERIAL_NUMBER 

 qualys.scanner.serial_number 

 — 

 SERIAL NUMBER 

 SOFTWARE_VERSION 

 qualys.scanner.software_version 

 — 

 SOFTWARE VERSION 

 SS_CONNECTION 

 qualys.scanner.ss_connection 

 — 

 SS CONNECTION 

 SS_LAST_CONNECTED 

 qualys.scanner.ss_last_connected 

 — 

 SS LAST CONNECTED 

 STATUS 

 qualys.scanner.status 

 — 

 STATUS 

 TYPE 

 qualys.scanner.type 

 — 

 TYPE 

 UPDATED 

 qualys.scanner.updated 

 — 

 UPDATED 

 USER_LOGIN 

 qualys.scanner.user_login 

 — 

 USER LOGIN 

 Global Asset View Assets Attributes 

 Device Security collects global asset view assets attributes from Qualys. The following table lists each Qualys attribute, its name as stored in Device Security , and the Device Security field it maps to (if applicable).

 Qualys Attribute 

 Device Security Attribute Name 

 Device Security Common Attribute* 

 Description 

 assetName 

 qualys.assetname 

 hostname 

 AssetName 

 address 

 qualys.address 

 IP Address 

 Address 

 MAC 

 — 

 MAC; id 

 MAC 

 hardware.model 

 qualys.hardware.model 

 Model 

 Model of the device 

 operatingSystem 

 — 

 raw_os 

 OperatingSystem 

 biosSerialNumber 

 qualys.biosserialnumber 

 Serial Number 

 BiosSerialNumber 

 softwareListData 

 — 

 third_party_learned_installed_software 

 SoftwareListData 

 networkInterfaceListData 

 — 

 third_party_learned_network_interfaces 

 NetworkInterfaceListData 

 activity.lastScannedDate 

 qualys.activity.lastscanneddate 

 — 

 LastScannedDate 

 activity.source 

 qualys.activity.source 

 — 

 Source 

 agent.activations 

 qualys.agent.activations 

 — 

 Activations 

 agent.configurationProfile 

 qualys.agent.configurationprofile 

 — 

 ConfigurationProfile 

 agent.connectedFrom 

 qualys.agent.connectedfrom 

 — 

 ConnectedFrom 

 agent.errorStatus 

 qualys.agent.errorstatus 

 — 

 ErrorStatus 

 agent.lastActivity 

 qualys.agent.lastactivity 

 — 

 LastActivity 

 agent.lastCheckedIn 

 qualys.agent.lastcheckedin 

 — 

 LastCheckedIn 

 agent.lastInventory 

 qualys.agent.lastinventory 

 — 

 LastInventory 

 agent.udcManifestAssigned 

 qualys.agent.udcmanifestassigned 

 — 

 UdcManifestAssigned 

 agent.version 

 qualys.agent.version 

 — 

 Version 

 agentId 

 qualys.agentid 

 — 

 AgentId 

 asn 

 qualys.asn 

 — 

 Asn 

 assetId 

 qualys.assetid 

 — 

 AssetId 

 assetType 

 qualys.assettype 

 — 

 AssetType 

 assetUUID 

 qualys.assetuuid 

 — 

 AssetUUID 

 assignedLocation 

 qualys.assignedlocation 

 — 

 AssignedLocation 

 biosAssetTag 

 qualys.biosassettag 

 — 

 BiosAssetTag 

 biosDescription 

 qualys.biosdescription 

 — 

 BiosDescription 

 businessAppListData 

 qualys.businessapplistdata 

 — 

 BusinessAppListData 

 businessInformation 

 qualys.businessinformation 

 — 

 BusinessInformation 

 cloudProvider 

 qualys.cloudprovider 

 — 

 CloudProvider 

 container.hasSensor 

 qualys.container.hassensor 

 — 

 HasSensor 

 container.noOfContainers 

 qualys.container.noofcontainers 

 — 

 NoOfContainers 

 container.noOfImages 

 qualys.container.noofimages 

 — 

 NoOfImages 

 container.product 

 qualys.container.product 

 — 

 Product 

 container.version 

 qualys.container.version 

 — 

 Version 

 cpuCount 

 qualys.cpucount 

 — 

 CpuCount 

 createdDate 

 qualys.createddate 

 — 

 CreatedDate 

 criticality.default 

 qualys.criticality.default 

 — 

 Default 

 criticality.isDefault 

 qualys.criticality.isdefault 

 — 

 IsDefault 

 criticality.lastUpdated 

 qualys.criticality.lastupdated 

 — 

 LastUpdated 

 criticality.score 

 qualys.criticality.score 

 — 

 Score 

 customAttributes 

 qualys.customattributes 

 — 

 CustomAttributes 

 dnsName 

 qualys.dnsname 

 — 

 DnsName 

 domain 

 qualys.domain 

 — 

 Domain 

 domainRole 

 qualys.domainrole 

 — 

 DomainRole 

 easmTags 

 qualys.easmtags 

 — 

 EasmTags 

 hardware.category 

 qualys.hardware.category 

 — 

 Category 

 hardware.category1 

 qualys.hardware.category1 

 — 

 Category1 

 hardware.category2 

 qualys.hardware.category2 

 — 

 Category2 

 hardware.fullName 

 qualys.hardware.fullname 

 — 

 FullName 

 hardware.lifecycle 

 qualys.hardware.lifecycle 

 — 

 Lifecycle 

 hardware.manufacturer 

 qualys.hardware.manufacturer 

 — 

 Manufacturer of the device 

 hardware.productFamily 

 qualys.hardware.productfamily 

 — 

 ProductFamily 

 hardware.productName 

 qualys.hardware.productname 

 — 

 ProductName 

 hardware.productUrl 

 qualys.hardware.producturl 

 — 

 ProductUrl 

 hardware.taxonomy.category1 

 qualys.hardware.taxonomy.category1 

 — 

 Category1 

 hardware.taxonomy.category2 

 qualys.hardware.taxonomy.category2 

 — 

 Category2 

 hardware.taxonomy.id 

 qualys.hardware.taxonomy.id 

 — 

 Id 

 hardware.taxonomy.name 

 qualys.hardware.taxonomy.name 

 — 

 Name of the device 

 hostId 

 qualys.hostid 

 — 

 HostId 

 hostingCategory1 

 qualys.hostingcategory1 

 — 

 HostingCategory1 

 hwUUID 

 qualys.hwuuid 

 — 

 HwUUID 

 inventory 

 qualys.inventory 

 — 

 Inventory 

 inventory.created 

 qualys.inventory.created 

 — 

 Created 

 inventory.lastUpdated 

 qualys.inventory.lastupdated 

 — 

 LastUpdated 

 inventory.source 

 qualys.inventory.source 

 — 

 Source 

 inventoryListData 

 qualys.inventorylistdata 

 — 

 InventoryListData 

 isContainerHost 

 qualys.iscontainerhost 

 — 

 IsContainerHost 

 isp 

 qualys.isp 

 — 

 Isp 

 lastBoot 

 qualys.lastboot 

 — 

 LastBoot 

 lastLocation 

 qualys.lastlocation 

 — 

 LastLocation 

 lastLoggedOnUser 

 qualys.lastloggedonuser 

 — 

 LastLoggedOnUser 

 lastModifiedDate 

 qualys.lastmodifieddate 

 — 

 LastModifiedDate 

 lparId 

 qualys.lparid 

 — 

 LparId 

 missingSoftware 

 qualys.missingsoftware 

 — 

 MissingSoftware 

 netbiosName 

 qualys.netbiosname 

 — 

 NetbiosName 

 openPortListData 

 qualys.openportlistdata 

 — 

 OpenPortListData 

 operatingSystem.architecture 

 qualys.operatingsystem.architecture 

 — 

 Architecture 

 operatingSystem.category 

 qualys.operatingsystem.category 

 — 

 Category 

 operatingSystem.category1 

 qualys.operatingsystem.category1 

 — 

 Category1 

 operatingSystem.category2 

 qualys.operatingsystem.category2 

 — 

 Category2 

 operatingSystem.cpe 

 qualys.operatingsystem.cpe 

 — 

 Cpe 

 operatingSystem.cpeId 

 qualys.operatingsystem.cpeid 

 — 

 CpeId 

 operatingSystem.cpeType 

 qualys.operatingsystem.cpetype 

 — 

 CpeType 

 operatingSystem.edition 

 qualys.operatingsystem.edition 

 — 

 Edition 

 operatingSystem.fullName 

 qualys.operatingsystem.fullname 

 — 

 FullName 

 operatingSystem.installDate 

 qualys.operatingsystem.installdate 

 — 

 InstallDate 

 operatingSystem.lifecycle 

 qualys.operatingsystem.lifecycle 

 — 

 Lifecycle 

 operatingSystem.marketVersion 

 qualys.operatingsystem.marketversion 

 — 

 MarketVersion 

 operatingSystem.osName 

 qualys.operatingsystem.osname 

 — 

 OsName 

 operatingSystem.productFamily 

 qualys.operatingsystem.productfamily 

 — 

 ProductFamily 

 operatingSystem.productName 

 qualys.operatingsystem.productname 

 — 

 ProductName 

 operatingSystem.productUrl 

 qualys.operatingsystem.producturl 

 — 

 ProductUrl 

 operatingSystem.publisher 

 qualys.operatingsystem.publisher 

 — 

 Publisher 

 operatingSystem.release 

 qualys.operatingsystem.release 

 — 

 Release 

 operatingSystem.taxonomy.category1 

 qualys.operatingsystem.taxonomy.category1 

 — 

 Category1 

 operatingSystem.taxonomy.category2 

 qualys.operatingsystem.taxonomy.category2 

 — 

 Category2 

 operatingSystem.taxonomy.id 

 qualys.operatingsystem.taxonomy.id 

 — 

 Id 

 operatingSystem.taxonomy.name 

 qualys.operatingsystem.taxonomy.name 

 — 

 Name of the device 

 operatingSystem.update 

 qualys.operatingsystem.update 

 — 

 Update 

 operatingSystem.version 

 qualys.operatingsystem.version 

 — 

 Version 

 organizationName 

 qualys.organizationname 

 — 

 OrganizationName 

 passiveSensor 

 qualys.passivesensor 

 — 

 PassiveSensor 

 processor.coresPerSocket 

 qualys.processor.corespersocket 

 — 

 CoresPerSocket 

 processor.description 

 qualys.processor.description 

 — 

 Description 

 processor.multithreadingStatus 

 qualys.processor.multithreadingstatus 

 — 

 MultithreadingStatus 

 processor.noOfSocket 

 qualys.processor.noofsocket 

 — 

 NoOfSocket 

 processor.numCPUs 

 qualys.processor.numcpus 

 — 

 NumCPUs 

 processor.speed 

 qualys.processor.speed 

 — 

 Speed of the device connection 

 processor.threadsPerCore 

 qualys.processor.threadspercore 

 — 

 ThreadsPerCore 

 provider 

 qualys.provider 

 — 

 Provider 

 riskScore 

 qualys.riskscore 

 — 

 RiskScore 

 sensor.activatedForModules 

 qualys.sensor.activatedformodules 

 — 

 ActivatedForModules 

 sensor.firstEasmScanDate 

 qualys.sensor.firsteasmscandate 

 — 

 FirstEasmScanDate 

 sensor.lastComplianceScan 

 qualys.sensor.lastcompliancescan 

 — 

 LastComplianceScan 

 sensor.lastEasmScanDate 

 qualys.sensor.lasteasmscandate 

 — 

 LastEasmScanDate 

 sensor.lastFullScan 

 qualys.sensor.lastfullscan 

 — 

 LastFullScan 

 sensor.lastPcScanDateAgent 

 qualys.sensor.lastpcscandateagent 

 — 

 LastPcScanDateAgent 

 sensor.lastPcScanDateScanner 

 qualys.sensor.lastpcscandatescanner 

 — 

 LastPcScanDateScanner 

 sensor.lastVMScan 

 qualys.sensor.lastvmscan 

 — 

 LastVMScan 

 sensor.lastVmScanDateAgent 

 qualys.sensor.lastvmscandateagent 

 — 

 LastVmScanDateAgent 

 sensor.lastVmScanDateScanner 

 qualys.sensor.lastvmscandatescanner 

 — 

 LastVmScanDateScanner 

 sensor.pendingActivationForModules 

 qualys.sensor.pendingactivationformodules 

 — 

 PendingActivationForModules 

 sensorLastUpdatedDate 

 qualys.sensorlastupdateddate 

 — 

 SensorLastUpdatedDate 

 serviceList.service 

 qualys.servicelist.service 

 — 

 Service 

 softwareComponent 

 qualys.softwarecomponent 

 — 

 SoftwareComponent 

 subdomain 

 qualys.subdomain 

 — 

 Subdomain 

 tagList.tag 

 qualys.taglist.tag 

 — 

 Tag 

 timeZone 

 qualys.timezone 

 — 

 TimeZone 

 totalMemory 

 qualys.totalmemory 

 — 

 TotalMemory 

 userAccountListData 

 qualys.useraccountlistdata 

 — 

 UserAccountListData 

 volumeListData 

 qualys.volumelistdata 

 — 

 VolumeListData 

 whois 

 qualys.whois 

 — 

 Whois 

 Rest Analysis Vulndetails Device Attributes 

 Device Security collects rest analysis vulndetails device attributes from Qualys. The following table lists each Qualys attribute, its name as stored in Device Security , and the Device Security field it maps to (if applicable).

 Qualys Attribute 

 Device Security Attribute Name 

 Device Security Common Attribute* 

 Description 

 DNS_DATA.HOSTNAME 

 qualys.dns_data.hostname 

 hostname 

 HOSTNAME 

 device_id 

 — 

 id; MAC 

 Device ID 

 IP 

 qualys.IP 

 IP Address 

 IP 

 OS 

 — 

 raw_os 

 OS 

 CLOUD_PROVIDER 

 qualys.cloud_provider 

 — 

 CLOUD PROVIDER 

 CLOUD_RESOURCE_ID 

 qualys.cloud_resource_id 

 — 

 CLOUD RESOURCE ID 

 CLOUD_SERVICE 

 qualys.cloud_service 

 — 

 CLOUD SERVICE 

 DNS 

 qualys.dns 

 — 

 DNS 

 DNS_DATA.DOMAIN 

 qualys.dns_data.domain 

 — 

 DOMAIN 

 DNS_DATA.FQDN 

 qualys.dns_data.fqdn 

 — 

 FQDN 

 EC2_INSTANCE_ID 

 qualys.ec2_instance_id 

 — 

 EC2 INSTANCE ID 

 QG_HOSTID 

 qualys.hostid 

 — 

 QG HOSTID 

 ID 

 qualys.id 

 — 

 ID 

 LAST_VM_AUTH_SCANNED_DATE 

 qualys.last_vm_auth_scanned_date 

 — 

 LAST VM AUTH SCANNED DATE 

 LAST_VM_AUTH_SCANNED_DURATION 

 qualys.last_vm_auth_scanned_duration 

 — 

 LAST VM AUTH SCANNED DURATION 

 METADATA.EC2.ATTRIBUTE.LAST_ERROR 

 qualys.metadata.ec2.attribute.last_error 

 — 

 LAST ERROR 

 METADATA.EC2.ATTRIBUTE.LAST_ERROR_DATE 

 qualys.metadata.ec2.attribute.last_error_date 

 — 

 LAST ERROR DATE 

 METADATA.EC2.ATTRIBUTE.LAST_STATUS 

 qualys.metadata.ec2.attribute.last_status 

 — 

 LAST STATUS 

 METADATA.EC2.ATTRIBUTE.LAST_SUCCESS_DATE 

 qualys.metadata.ec2.attribute.last_success_date 

 — 

 LAST SUCCESS DATE 

 METADATA.EC2.ATTRIBUTE.NAME 

 qualys.metadata.ec2.attribute.name 

 — 

 NAME 

 METADATA.EC2.ATTRIBUTE.VALUE 

 qualys.metadata.ec2.attribute.value 

 — 

 VALUE 

 NETBIOS 

 qualys.netbios 

 — 

 NETBIOS 

 Rest Analysis Vulndetails Vulnerability Attributes 

 Device Security collects rest analysis vulndetails vulnerability attributes from Qualys. The following table lists each Qualys attribute, its name as stored in Device Security , and the Device Security field it maps to (if applicable).

 Qualys Attribute 

 Device Security Attribute Name 

 Device Security Common Attribute* 

 Description 

 cveids 

 — 

 cve 

 Cveids 

 LAST_FOUND_DATETIME 

 qualys.last_found_datetime 

 detected_time 

 LAST FOUND DATETIME 

 device_id 

 — 

 id 

 Device ID 

 IP 

 — 

 IP Address 

 IP 

 SEVERITY 

 — 

 risk_level 

 SEVERITY 

 severity 

 qualys.severity 

 severity 

 Severity 

 QID 

 — 

 vulnerability_id 

 QID 

 CLOUD_PROVIDER 

 qualys.cloud_provider 

 — 

 CLOUD PROVIDER 

 CLOUD_RESOURCE_ID 

 qualys.cloud_resource_id 

 — 

 CLOUD RESOURCE ID 

 CLOUD_SERVICE 

 qualys.cloud_service 

 — 

 CLOUD SERVICE 

 deviceid 

 qualys.deviceid 

 — 

 Deviceid 

 DNS 

 qualys.dns 

 — 

 DNS 

 DNS_DATA.DOMAIN 

 qualys.dns_data.domain 

 — 

 DOMAIN 

 DNS_DATA.FQDN 

 qualys.dns_data.fqdn 

 — 

 FQDN 

 DNS_DATA.HOSTNAME 

 qualys.dns_data.hostname 

 — 

 HOSTNAME 

 EC2_INSTANCE_ID 

 qualys.ec2_instance_id 

 — 

 EC2 INSTANCE ID 

 FIRST_FOUND_DATETIME 

 qualys.first_found_datetime 

 — 

 FIRST FOUND DATETIME 

 IS_DISABLED 

 qualys.is_disabled 

 — 

 IS DISABLED 

 IS_IGNORED 

 qualys.is_ignored 

 — 

 IS IGNORED 

 LAST_PROCESSED_DATETIME 

 qualys.last_processed_datetime 

 — 

 LAST PROCESSED DATETIME 

 LAST_SCAN_DATETIME 

 qualys.last_scan_datetime 

 — 

 LAST SCAN DATETIME 

 LAST_TEST_DATETIME 

 qualys.last_test_datetime 

 — 

 LAST TEST DATETIME 

 LAST_UPDATE_DATETIME 

 qualys.last_update_datetime 

 — 

 LAST UPDATE DATETIME 

 LAST_VM_AUTH_SCANNED_DATE 

 qualys.last_vm_auth_scanned_date 

 — 

 LAST VM AUTH SCANNED DATE 

 LAST_VM_AUTH_SCANNED_DURATION 

 qualys.last_vm_auth_scanned_duration 

 — 

 LAST VM AUTH SCANNED DURATION 

 LAST_VM_SCANNED_DATE 

 qualys.last_vm_scanned_date 

 — 

 LAST VM SCANNED DATE 

 LAST_VM_SCANNED_DURATION 

 qualys.last_vm_scanned_duration 

 — 

 LAST VM SCANNED DURATION 

 METADATA.EC2.ATTRIBUTE.LAST_ERROR 

 qualys.metadata.ec2.attribute.last_error 

 — 

 LAST ERROR 

 METADATA.EC2.ATTRIBUTE.LAST_ERROR_DATE 

 qualys.metadata.ec2.attribute.last_error_date 

 — 

 LAST ERROR DATE 

 METADATA.EC2.ATTRIBUTE.LAST_STATUS 

 qualys.metadata.ec2.attribute.last_status 

 — 

 LAST STATUS 

 METADATA.EC2.ATTRIBUTE.LAST_SUCCESS_DATE 

 qualys.metadata.ec2.attribute.last_success_date 

 — 

 LAST SUCCESS DATE 

 METADATA.EC2.ATTRIBUTE.NAME 

 qualys.metadata.ec2.attribute.name 

 — 

 NAME 

 METADATA.EC2.ATTRIBUTE.VALUE 

 qualys.metadata.ec2.attribute.value 

 — 

 VALUE 

 NETBIOS 

 qualys.netbios 

 — 

 NETBIOS 

 OS 

 qualys.os 

 — 

 OS 

 QG_HOSTID 

 qualys.qg_hostid 

 — 

 QG HOSTID 

 RESULTS 

 qualys.results 

 — 

 RESULTS 

 SSL 

 qualys.ssl 

 — 

 SSL 

 STATUS 

 qualys.status 

 — 

 STATUS 

 TIMES_FOUND 

 qualys.times_found 

 — 

 TIMES FOUND 

 TRACKING_METHOD 

 qualys.tracking_method 

 — 

 TRACKING METHOD 

 TYPE 

 qualys.type 

 — 

 TYPE 

 UNIQUE_VULN_ID 

 qualys.unique_vuln_id 

 — 

 UNIQUE VULN ID 

 * Only some attributes map to a Device Security Common Attribute. 

 Previous 

 Philips Focal Point Attribute Reference 

 Next 

 Rapid7 Attribute Reference

---
url: https://docs.paloaltonetworks.com/iot/integration/attribute-reference/attribute-reference-qualys
fetched_at: 2026-08-13T16:37:06Z
source: palo-alto-main
---

# Qualys Attribute Reference Clear

Qualys Attribute Reference 

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

 Qualys Attribute Reference 

 Updated on 

 Thu May 14 09:23:33 PDT 2026 

 Focus 

 Download PDF 

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

 Updated on 

 Thu May 14 09:23:33 PDT 2026 

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

 Appliance Attributes 

 Device Security collects appliance attributes from the Qualys appliance list API. Each record describes a Qualys scanner appliance deployed in the environment.
 The following table lists each Qualys attribute, its name as stored
 in Device Security , and the Device Security field it maps to (if applicable).

 Qualys Attribute 

 Device Security Attribute Name 

 Device Security Common Attribute* 

 Description 

 ACTIVATION_CODE 

 qualys.scanner.activation_code 

 — 

 Activation code for the Qualys scanner appliance 

 ASSET_GROUP_COUNT 

 qualys.scanner.asset_group_count 

 — 

 Number of asset groups associated with the scanner 

 ASSET_GROUP_LIST 

 qualys.scanner.asset_group_list 

 — 

 List of asset groups associated with the scanner 

 COMMENTS 

 qualys.scanner.comments 

 — 

 Comments or notes for the scanner appliance 

 HEARTBEATS_MISSED 

 qualys.scanner.heartbeats_missed 

 — 

 Number of missed heartbeat signals from the scanner 

 ID 

 qualys.scanner.id 

 — 

 Unique identifier of the scanner appliance 

 INTERFACE_SETTINGS.[0].DNS.DOMAIN 

 — 

 AD Domain 

 DNS domain of the scanner appliance's primary interface 

 INTERFACE_SETTINGS.[0].IP_ADDRESS 

 — 

 ipv4_address; id 

 IP address of the scanner appliance's primary interface 

 LAST_UPDATED_DATE 

 qualys.scanner.last_updated_date 

 — 

 Date the scanner appliance record was last updated 

 MAX_CAPACITY_UNITS 

 qualys.scanner.max_capacity_units 

 — 

 Maximum scan capacity units for the scanner 

 ML_LATEST 

 qualys.scanner.ml_latest 

 — 

 Latest manifest list version installed on the scanner 

 MODEL_NUMBER 

 qualys.scanner.model_number 

 — 

 Model number of the scanner appliance 

 NAME 

 qualys.scanner.name 

 — 

 Name of the scanner appliance 

 POLLING_INTERVAL 

 qualys.scanner.polling_interval 

 — 

 Polling interval for the scanner appliance 

 RUNNING_SCAN_COUNT 

 qualys.scanner.running_scan_count 

 — 

 Number of scans currently running on the scanner 

 RUNNING_SLICES_COUNT 

 qualys.scanner.running_slices_count 

 — 

 Number of scan slices currently running on the scanner 

 SERIAL_NUMBER 

 qualys.scanner.serial_number 

 — 

 Serial number of the scanner appliance 

 SOFTWARE_VERSION 

 qualys.scanner.software_version 

 — 

 Software version installed on the scanner appliance 

 SS_CONNECTION 

 qualys.scanner.ss_connection 

 — 

 Scan server connection status of the scanner 

 SS_LAST_CONNECTED 

 qualys.scanner.ss_last_connected 

 — 

 Timestamp of the scanner's last connection to the scan server 

 STATUS 

 qualys.scanner.status 

 — 

 Operational status of the scanner appliance 

 TYPE 

 qualys.scanner.type 

 — 

 Type of the scanner appliance 

 UPDATED 

 qualys.scanner.updated 

 — 

 Indicates whether the scanner appliance was recently updated 

 USER_LOGIN 

 qualys.scanner.user_login 

 — 

 Login username associated with the scanner appliance 

 Global Asset View Attributes 

 Device Security collects asset attributes from the Qualys Global AssetView API. Each record describes a discovered or managed asset in the Qualys inventory.
 The following table lists each Qualys attribute, its name as stored
 in Device Security , and the Device Security field it maps to (if applicable).

 Qualys Attribute 

 Device Security Attribute Name 

 Device Security Common Attribute* 

 Description 

 MAC 

 — 

 MAC; id 

 MAC address of the asset 

 activity.lastScannedDate 

 qualys.activity.lastscanneddate 

 — 

 Date the asset was last scanned 

 activity.source 

 qualys.activity.source 

 — 

 Source of the last scan activity 

 address 

 qualys.address 

 ipv4_address 

 IPv4 address of the asset 

 agent.activations 

 qualys.agent.activations 

 — 

 Qualys agent activation modules 

 agent.configurationProfile 

 qualys.agent.configurationprofile 

 — 

 Configuration profile assigned to the Qualys agent 

 agent.connectedFrom 

 qualys.agent.connectedfrom 

 — 

 IP address from which the Qualys agent last connected 

 agent.errorStatus 

 qualys.agent.errorstatus 

 — 

 Error status reported by the Qualys agent 

 agent.lastActivity 

 qualys.agent.lastactivity 

 — 

 Timestamp of the agent's last activity 

 agent.lastCheckedIn 

 qualys.agent.lastcheckedin 

 — 

 Timestamp of the agent's last check-in 

 agent.lastInventory 

 qualys.agent.lastinventory 

 — 

 Timestamp of the agent's last inventory collection 

 agent.udcManifestAssigned 

 qualys.agent.udcmanifestassigned 

 — 

 UDC manifest assigned to the Qualys agent 

 agent.version 

 qualys.agent.version 

 — 

 Qualys agent version 

 agentId 

 qualys.agentid 

 — 

 Qualys agent ID 

 asn 

 qualys.asn 

 — 

 Autonomous system number 

 assetId 

 qualys.assetid 

 — 

 Asset ID 

 assetName 

 qualys.assetname 

 Hostname 

 Asset name 

 assetType 

 qualys.assettype 

 — 

 Asset type 

 assetUUID 

 qualys.assetuuid 

 — 

 Asset UUID 

 assignedLocation 

 qualys.assignedlocation 

 — 

 Assigned location 

 biosAssetTag 

 qualys.biosassettag 

 — 

 BIOS asset tag 

 biosDescription 

 qualys.biosdescription 

 — 

 BIOS description 

 biosSerialNumber 

 qualys.biosserialnumber 

 Serial Number 

 BIOS serial number 

 businessAppListData 

 qualys.businessapplistdata 

 — 

 Business application list data 

 businessInformation 

 qualys.businessinformation 

 — 

 Business information associated with the asset 

 cloudProvider 

 qualys.cloudprovider 

 — 

 Cloud provider 

 container.hasSensor 

 qualys.container.hassensor 

 — 

 Indicates whether the container runtime has a sensor 

 container.noOfContainers 

 qualys.container.noofcontainers 

 — 

 Number of containers running on the asset 

 container.noOfImages 

 qualys.container.noofimages 

 — 

 Number of container images on the asset 

 container.product 

 qualys.container.product 

 — 

 Container runtime product name 

 container.version 

 qualys.container.version 

 — 

 Container runtime version 

 cpuCount 

 qualys.cpucount 

 — 

 CPU count 

 createdDate 

 qualys.createddate 

 — 

 Date the asset record was created 

 criticality.default 

 qualys.criticality.default 

 — 

 Default criticality score for the asset 

 criticality.isDefault 

 qualys.criticality.isdefault 

 — 

 Indicates whether the criticality score is the default value 

 criticality.lastUpdated 

 qualys.criticality.lastupdated 

 — 

 Timestamp of the last criticality score update 

 criticality.score 

 qualys.criticality.score 

 — 

 Criticality score 

 customAttributes 

 qualys.customattributes 

 — 

 Custom attributes 

 dnsName 

 qualys.dnsname 

 — 

 DNS name 

 domain 

 qualys.domain 

 — 

 Domain 

 domainRole 

 qualys.domainrole 

 — 

 Domain role 

 easmTags 

 qualys.easmtags 

 — 

 EASM tags 

 hardware.category 

 qualys.hardware.category 

 — 

 Hardware category 

 hardware.category1 

 qualys.hardware.category1 

 — 

 Hardware category 1 

 hardware.category2 

 qualys.hardware.category2 

 — 

 Hardware category 2 

 hardware.fullName 

 qualys.hardware.fullname 

 — 

 Hardware full name 

 hardware.lifecycle 

 qualys.hardware.lifecycle 

 — 

 Hardware lifecycle 

 hardware.manufacturer 

 qualys.hardware.manufacturer 

 — 

 Hardware manufacturer 

 hardware.model 

 qualys.hardware.model 

 Model 

 Hardware model 

 hardware.productFamily 

 qualys.hardware.productfamily 

 — 

 Hardware product family 

 hardware.productName 

 qualys.hardware.productname 

 — 

 Hardware product name 

 hardware.productUrl 

 qualys.hardware.producturl 

 — 

 Hardware product URL 

 hardware.taxonomy.category1 

 qualys.hardware.taxonomy.category1 

 — 

 Hardware taxonomy category 1 

 hardware.taxonomy.category2 

 qualys.hardware.taxonomy.category2 

 — 

 Hardware taxonomy category 2 

 hardware.taxonomy.id 

 qualys.hardware.taxonomy.id 

 — 

 Hardware taxonomy ID 

 hardware.taxonomy.name 

 qualys.hardware.taxonomy.name 

 — 

 Hardware taxonomy name 

 hostId 

 qualys.hostid 

 — 

 Qualys host ID 

 hostingCategory1 

 qualys.hostingcategory1 

 — 

 Hostingcategory1 

 hwUUID 

 qualys.hwuuid 

 — 

 Hardware UUID 

 inventory 

 qualys.inventory 

 — 

 Inventory 

 inventory.created 

 qualys.inventory.created 

 — 

 Date the asset was added to the Qualys inventory 

 inventory.lastUpdated 

 qualys.inventory.lastupdated 

 — 

 Date the asset inventory record was last updated 

 inventory.source 

 qualys.inventory.source 

 — 

 Source that added the asset to the Qualys inventory 

 inventoryListData 

 qualys.inventorylistdata 

 — 

 Inventory list data 

 isContainerHost 

 qualys.iscontainerhost 

 — 

 Indicates whether the asset is a container host 

 isp 

 qualys.isp 

 — 

 ISP 

 lastBoot 

 qualys.lastboot 

 — 

 Last boot time 

 lastLocation 

 qualys.lastlocation 

 — 

 Last known location 

 lastLoggedOnUser 

 qualys.lastloggedonuser 

 — 

 Last logged-on user 

 lastModifiedDate 

 qualys.lastmodifieddate 

 — 

 Date the asset record was last modified 

 lparId 

 qualys.lparid 

 — 

 LPAR ID 

 missingSoftware 

 qualys.missingsoftware 

 — 

 Missing software 

 netbiosName 

 qualys.netbiosname 

 — 

 NetBIOS name 

 networkInterfaceListData 

 — 

 third_party_learned_network_interfaces 

 List of network interfaces discovered on the asset 

 openPortListData 

 qualys.openportlistdata 

 — 

 Open port list data 

 operatingSystem 

 — 

 raw_os 

 Operating system name of the asset 

 operatingSystem.architecture 

 qualys.operatingsystem.architecture 

 — 

 Operating system architecture 

 operatingSystem.category 

 qualys.operatingsystem.category 

 — 

 Operating system category 

 operatingSystem.category1 

 qualys.operatingsystem.category1 

 — 

 Operating system category 1 

 operatingSystem.category2 

 qualys.operatingsystem.category2 

 — 

 Operating system category 2 

 operatingSystem.cpe 

 qualys.operatingsystem.cpe 

 — 

 Operating system CPE 

 operatingSystem.cpeId 

 qualys.operatingsystem.cpeid 

 — 

 Operating system CPE ID 

 operatingSystem.cpeType 

 qualys.operatingsystem.cpetype 

 — 

 Operating system CPE type 

 operatingSystem.edition 

 qualys.operatingsystem.edition 

 — 

 Operating system edition 

 operatingSystem.fullName 

 qualys.operatingsystem.fullname 

 — 

 Operating system full name 

 operatingSystem.installDate 

 qualys.operatingsystem.installdate 

 — 

 Operating system install date 

 operatingSystem.lifecycle 

 qualys.operatingsystem.lifecycle 

 — 

 Operating system lifecycle 

 operatingSystem.marketVersion 

 qualys.operatingsystem.marketversion 

 — 

 Operating system market version 

 operatingSystem.osName 

 qualys.operatingsystem.osname 

 — 

 Operating system name 

 operatingSystem.productFamily 

 qualys.operatingsystem.productfamily 

 — 

 Operating system product family 

 operatingSystem.productName 

 qualys.operatingsystem.productname 

 — 

 Operating system product name 

 operatingSystem.productUrl 

 qualys.operatingsystem.producturl 

 — 

 Operating system product URL 

 operatingSystem.publisher 

 qualys.operatingsystem.publisher 

 — 

 Operating system publisher 

 operatingSystem.release 

 qualys.operatingsystem.release 

 — 

 Operating system release 

 operatingSystem.taxonomy.category1 

 qualys.operatingsystem.taxonomy.category1 

 — 

 Operating system taxonomy category 1 

 operatingSystem.taxonomy.category2 

 qualys.operatingsystem.taxonomy.category2 

 — 

 Operating system taxonomy category 2 

 operatingSystem.taxonomy.id 

 qualys.operatingsystem.taxonomy.id 

 — 

 Operating system taxonomy ID 

 operatingSystem.taxonomy.name 

 qualys.operatingsystem.taxonomy.name 

 — 

 Operating system taxonomy name 

 operatingSystem.update 

 qualys.operatingsystem.update 

 — 

 Operating system update 

 operatingSystem.version 

 qualys.operatingsystem.version 

 — 

 Operating system version 

 organizationName 

 qualys.organizationname 

 — 

 Organization name 

 passiveSensor 

 qualys.passivesensor 

 — 

 Passive sensor 

 processor.coresPerSocket 

 qualys.processor.corespersocket 

 — 

 Processor cores per socket 

 processor.description 

 qualys.processor.description 

 — 

 Processor description 

 processor.multithreadingStatus 

 qualys.processor.multithreadingstatus 

 — 

 Processor multithreading status 

 processor.noOfSocket 

 qualys.processor.noofsocket 

 — 

 Number of processor sockets 

 processor.numCPUs 

 qualys.processor.numcpus 

 — 

 Number of processor CPUs 

 processor.speed 

 qualys.processor.speed 

 — 

 Processor speed 

 processor.threadsPerCore 

 qualys.processor.threadspercore 

 — 

 Processor threads per core 

 provider 

 qualys.provider 

 — 

 Provider 

 riskScore 

 qualys.riskscore 

 — 

 Risk score 

 sensor.activatedForModules 

 qualys.sensor.activatedformodules 

 — 

 Qualys sensor activation modules 

 sensor.firstEasmScanDate 

 qualys.sensor.firsteasmscandate 

 — 

 Date of the sensor's first EASM scan 

 sensor.lastComplianceScan 

 qualys.sensor.lastcompliancescan 

 — 

 Date of the sensor's last compliance scan 

 sensor.lastEasmScanDate 

 qualys.sensor.lasteasmscandate 

 — 

 Date of the sensor's last EASM scan 

 sensor.lastFullScan 

 qualys.sensor.lastfullscan 

 — 

 Date of the sensor's last full scan 

 sensor.lastPcScanDateAgent 

 qualys.sensor.lastpcscandateagent 

 — 

 Date of the sensor's last PC scan (agent) 

 sensor.lastPcScanDateScanner 

 qualys.sensor.lastpcscandatescanner 

 — 

 Date of the sensor's last PC scan (scanner) 

 sensor.lastVMScan 

 qualys.sensor.lastvmscan 

 — 

 Date of the sensor's last VM scan 

 sensor.lastVmScanDateAgent 

 qualys.sensor.lastvmscandateagent 

 — 

 Date of the sensor's last VM scan (agent) 

 sensor.lastVmScanDateScanner 

 qualys.sensor.lastvmscandatescanner 

 — 

 Date of the sensor's last VM scan (scanner) 

 sensor.pendingActivationForModules 

 qualys.sensor.pendingactivationformodules 

 — 

 Qualys sensor modules pending activation 

 sensorLastUpdatedDate 

 qualys.sensorlastupdateddate 

 — 

 Date the sensor record was last updated 

 serviceList.service 

 qualys.servicelist.service 

 — 

 Service list entry 

 softwareComponent 

 qualys.softwarecomponent 

 — 

 Software component 

 softwareListData 

 — 

 third_party_learned_installed_software 

 List of software installed on the asset 

 subdomain 

 qualys.subdomain 

 — 

 Subdomain 

 tagList.tag 

 qualys.taglist.tag 

 — 

 Tag list entry 

 timeZone 

 qualys.timezone 

 — 

 Time zone 

 totalMemory 

 qualys.totalmemory 

 — 

 Total memory 

 userAccountListData 

 qualys.useraccountlistdata 

 — 

 User account list data 

 volumeListData 

 qualys.volumelistdata 

 — 

 Volume list data 

 whois 

 qualys.whois 

 — 

 WHOIS information 

 Vulnerability Scan Device Attributes 

 Device Security collects device attributes from the Qualys vulnerability details REST analysis API. Each record describes a device as seen through the context of vulnerability scan results.
 The following table lists each Qualys attribute, its name as stored
 in Device Security , and the Device Security field it maps to (if applicable).

 Qualys Attribute 

 Device Security Attribute Name 

 Device Security Common Attribute* 

 Description 

 CLOUD_PROVIDER 

 qualys.cloud_provider 

 — 

 Cloud provider 

 CLOUD_RESOURCE_ID 

 qualys.cloud_resource_id 

 — 

 Cloud resource ID 

 CLOUD_SERVICE 

 qualys.cloud_service 

 — 

 Cloud service 

 DNS 

 qualys.dns 

 — 

 DNS 

 DNS_DATA.DOMAIN 

 qualys.dns_data.domain 

 — 

 DNS data domain 

 DNS_DATA.FQDN 

 qualys.dns_data.fqdn 

 — 

 DNS data FQDN 

 DNS_DATA.HOSTNAME 

 qualys.dns_data.hostname 

 Hostname 

 DNS data hostname 

 EC2_INSTANCE_ID 

 qualys.ec2_instance_id 

 — 

 EC2 instance ID 

 ID 

 qualys.id 

 — 

 Qualys ID 

 IP 

 qualys.IP 

 ipv4_address 

 IPv4 address of the scanned device 

 LAST_VM_AUTH_SCANNED_DATE 

 qualys.last_vm_auth_scanned_date 

 — 

 Date of the last authenticated VM scan 

 LAST_VM_AUTH_SCANNED_DURATION 

 qualys.last_vm_auth_scanned_duration 

 — 

 Duration of the last authenticated VM scan 

 METADATA.EC2.ATTRIBUTE.LAST_ERROR 

 qualys.metadata.ec2.attribute.last_error 

 — 

 Last error from the EC2 metadata attribute 

 METADATA.EC2.ATTRIBUTE.LAST_ERROR_DATE 

 qualys.metadata.ec2.attribute.last_error_date 

 — 

 Date of the last EC2 metadata attribute error 

 METADATA.EC2.ATTRIBUTE.LAST_STATUS 

 qualys.metadata.ec2.attribute.last_status 

 — 

 Last status of the EC2 metadata attribute 

 METADATA.EC2.ATTRIBUTE.LAST_SUCCESS_DATE 

 qualys.metadata.ec2.attribute.last_success_date 

 — 

 Date of the last successful EC2 metadata attribute update 

 METADATA.EC2.ATTRIBUTE.NAME 

 qualys.metadata.ec2.attribute.name 

 — 

 Name of the EC2 metadata attribute 

 METADATA.EC2.ATTRIBUTE.VALUE 

 qualys.metadata.ec2.attribute.value 

 — 

 Value of the EC2 metadata attribute 

 NETBIOS 

 qualys.netbios 

 — 

 NetBIOS name 

 OS 

 — 

 raw_os 

 Operating system name of the scanned device 

 QG_HOSTID 

 qualys.hostid 

 — 

 Qualys host ID 

 device_id 

 — 

 id; MAC 

 Device identifier used to correlate with the device inventory 

 Vulnerability Attributes 

 Device Security collects vulnerability attributes from the Qualys vulnerability details REST analysis API. Each record describes an individual vulnerability finding on a scanned asset.
 The following table lists each Qualys attribute, its name as stored
 in Device Security , and the Device Security field it maps to (if applicable).

 Qualys Attribute 

 Device Security Attribute Name 

 Device Security Common Attribute* 

 Description 

 CLOUD_PROVIDER 

 qualys.cloud_provider 

 — 

 Cloud provider 

 CLOUD_RESOURCE_ID 

 qualys.cloud_resource_id 

 — 

 Cloud resource ID 

 CLOUD_SERVICE 

 qualys.cloud_service 

 — 

 Cloud service 

 DNS 

 qualys.dns 

 — 

 DNS 

 DNS_DATA.DOMAIN 

 qualys.dns_data.domain 

 — 

 DNS data domain 

 DNS_DATA.FQDN 

 qualys.dns_data.fqdn 

 — 

 DNS data FQDN 

 DNS_DATA.HOSTNAME 

 qualys.dns_data.hostname 

 — 

 DNS data hostname 

 EC2_INSTANCE_ID 

 qualys.ec2_instance_id 

 — 

 EC2 instance ID 

 FIRST_FOUND_DATETIME 

 qualys.first_found_datetime 

 — 

 Date and time the vulnerability was first found 

 IP 

 — 

 ipv4_address 

 IPv4 address of the device with the vulnerability 

 IS_DISABLED 

 qualys.is_disabled 

 — 

 Indicates whether the vulnerability finding is disabled 

 IS_IGNORED 

 qualys.is_ignored 

 — 

 Indicates whether the vulnerability finding is ignored 

 LAST_FOUND_DATETIME 

 qualys.last_found_datetime 

 detected_time 

 Date and time the vulnerability was last found 

 LAST_PROCESSED_DATETIME 

 qualys.last_processed_datetime 

 — 

 Date and time the vulnerability was last processed 

 LAST_SCAN_DATETIME 

 qualys.last_scan_datetime 

 — 

 Date and time of the last scan for this vulnerability 

 LAST_TEST_DATETIME 

 qualys.last_test_datetime 

 — 

 Date and time of the last test for this vulnerability 

 LAST_UPDATE_DATETIME 

 qualys.last_update_datetime 

 — 

 Date and time the vulnerability record was last updated 

 LAST_VM_AUTH_SCANNED_DATE 

 qualys.last_vm_auth_scanned_date 

 — 

 Date of the last authenticated VM scan 

 LAST_VM_AUTH_SCANNED_DURATION 

 qualys.last_vm_auth_scanned_duration 

 — 

 Duration of the last authenticated VM scan 

 LAST_VM_SCANNED_DATE 

 qualys.last_vm_scanned_date 

 — 

 Date of the last VM scan 

 LAST_VM_SCANNED_DURATION 

 qualys.last_vm_scanned_duration 

 — 

 Duration of the last VM scan 

 METADATA.EC2.ATTRIBUTE.LAST_ERROR 

 qualys.metadata.ec2.attribute.last_error 

 — 

 Last error from the EC2 metadata attribute 

 METADATA.EC2.ATTRIBUTE.LAST_ERROR_DATE 

 qualys.metadata.ec2.attribute.last_error_date 

 — 

 Date of the last EC2 metadata attribute error 

 METADATA.EC2.ATTRIBUTE.LAST_STATUS 

 qualys.metadata.ec2.attribute.last_status 

 — 

 Last status of the EC2 metadata attribute 

 METADATA.EC2.ATTRIBUTE.LAST_SUCCESS_DATE 

 qualys.metadata.ec2.attribute.last_success_date 

 — 

 Date of the last successful EC2 metadata attribute update 

 METADATA.EC2.ATTRIBUTE.NAME 

 qualys.metadata.ec2.attribute.name 

 — 

 Name of the EC2 metadata attribute 

 METADATA.EC2.ATTRIBUTE.VALUE 

 qualys.metadata.ec2.attribute.value 

 — 

 Value of the EC2 metadata attribute 

 NETBIOS 

 qualys.netbios 

 — 

 NetBIOS name 

 OS 

 qualys.os 

 — 

 Operating system name 

 QG_HOSTID 

 qualys.qg_hostid 

 — 

 Qualys host ID 

 QID 

 — 

 vulnerability_id 

 Qualys vulnerability identifier 

 RESULTS 

 qualys.results 

 — 

 Scan results for the vulnerability finding 

 SEVERITY 

 — 

 risk_level 

 Severity level of the vulnerability 

 SSL 

 qualys.ssl 

 — 

 SSL 

 STATUS 

 qualys.status 

 — 

 Vulnerability finding status 

 TIMES_FOUND 

 qualys.times_found 

 — 

 Number of times the vulnerability was found 

 TRACKING_METHOD 

 qualys.tracking_method 

 — 

 Method used to track the scanned host 

 TYPE 

 qualys.type 

 — 

 Vulnerability detection type 

 UNIQUE_VULN_ID 

 qualys.unique_vuln_id 

 — 

 Unique vulnerability ID 

 cveids 

 — 

 cve 

 CVE identifiers associated with the vulnerability 

 device_id 

 — 

 id 

 Device identifier used to correlate the vulnerability with a device 

 deviceid 

 qualys.deviceid 

 — 

 Qualys device ID 

 severity 

 qualys.severity 

 Severity 

 Severity level of the vulnerability finding 

 * Only some attributes map to a Device Security Common Attribute. 

 Previous 

 Philips Focal Point Attribute Reference 

 Next 

 Rapid7 Attribute Reference 

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

 Firewalls 

 PAN-OS 

 PAN-OS SD-WAN 

 Service Provider 

 VM-Series 

 SASE 

 Prisma Access 

 Strata Multitenant Cloud Manager 

 Device Security 

 Reference 

 Cloud-Delivered Security Services 

 Integrations 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

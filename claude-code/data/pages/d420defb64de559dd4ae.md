---
url: https://docs.paloaltonetworks.com/pan-os/10-1/pan-os-panorama-api/pan-os-xml-api-request-types/pan-os-xml-api-request-types-and-actions/configuration-actions
fetched_at: 2026-08-13T17:03:24Z
source: palo-alto-main
---

# Configuration (API) Clear

Configuration (API) 

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

 Configuration (API) 

 Updated on 

 Thu Aug 28 13:33:18 PDT 2025 

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

 Thu Aug 28 13:33:18 PDT 2025 

 Focus 

 Home 

 Next-Generation Firewall 

 PAN-OS
XML API Request Types and Actions 

 Configuration (API) 

 Download PDF 

 Next-Generation Firewall 

 Configuration (API) 

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

 Asynchronous and Synchronous Requests to the PAN-OS XML API 

 Next 

 Commit 

 Configuration (API) 

 The requests examples in these topics illustrate how you can use the PAN-OS XML API to
 configure your firewall. 

 View Configuration Node Values for XPath 

 Use action=complete action along with an XPath to see possible
 values that are available with the XPath node. 

 curl -X POST 'https://firewall/api?type=config&action=complete&xpath=/config/devices/entry[@name='localhost.localdomain']/vsys&key=apikey" 

 Using XPATH to Retrieve Configuration Information 

 Use the xpath parameter to target a specific portion of the
 configuration. For example, to retrieve just the security
 rulebase: xpath=/config/devices/entry/vsys/entry/rulebase/security 

 curl -X POST 'https://firewall/api?type=config&action=show&xpath=/config/devices/entry/vsys/entry/rulebase/security"

 There is no trailing backslash character at the end of the XPath. 

 Using XPATH to Retrieve ARP Configuration 

 curl -X POST 'https://<firewall>//api/?type=op&command=<show><arp><entry name='all'/></arp></show>'

 Get Candidate Configuration 

 Get the candidate configuration from a firewall by specifying the portion of the
 configuration to get. Use the following request, including
 the xpath parameter to specify the portion of the
 configuration to get. 

 curl -X POST 'https://firewall/api?type=config&action=get&xpath=<path-to-config-node>" 

 Configuration Node 

 API Request 

 Firewall candidate configuration 

 curl -X POST 'https://firewall/api?type=config&action=get&xpath=/config/devices/entry/vsys/entry[@name='vsys1']&key=<api_key>" 

 Firewall candidate configuration through Panorama 

 curl -X POST 'https://panorama/api?type=config&action=get&xpath=/config/devices/entry/vsys/entry[@name='vsys1']&target=<serial>&key=<panorama_api_key>" 

 Firewall candidate configuration through Panorama without
 specifying a firewall 

 curl -X POST 'https://panorama/api?type=config&action=get&xpath=/config/devices/entry/*[name()!='vsys']|/config/devices/entry/vsys/entry[@name='vsys1']&key=<panorama_api_key>" 

 Address objects in a virtual system (vsys). 

 curl -X GET "https://<firewall>//api/?type=config&action=get&xpath=/config/devices/entry/vsys/entry[@name='vsys1']/address" 

 The response looks similar to the following:

 <response status="success" code="19">
 <result total-count="1" count="1">
 <address admin="name" dirtyId="8" time="2015/10/20 15:32:36"><entry name="testobject"><ip-netmask>192.0.2.2</ip-netmask></entry><entry name="test1"><ip-netmask>192.0.2.12</ip-netmask></entry>
 ...</address>
 </result>
</response>

 Pre-rules pushed from Panorama. 

 curl -X GET "https://<firewall>//api/?type=config&action=get&xpath=/config/panorama/vsys/entry[@name='vsys']/pre-rulebase/security" 

 Full list of all applications. 

 curl -X POST 'https://firewall/api?type=config&action=get&xpath=/config/predefined/application" 

 Details on the specific application. 

 curl -X POST 'https://firewall/api?type=config&action=get&xpath=/config/predefined/application/entry[@name='hotmail']" 

 Set Configuration 

 Use action=set to add or create a new object at a specified
 location in the PAN-OS configuration. Use the xpath parameter
 to specify the location of the object in the configuration. For example, if you are
 adding a new rule to the security rulebase, the xpath-value would be: 

 /config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/rulebase/security 

 Use the element parameter to specify a value for the object you
 are adding or creating using XML. 

 Configuration Node 

 API Request 

 Create a new rule called rule1 in security policy 

 curl -X POST 'https://firewall/api?type=config&action=set&key=keyvalue&xpath=xpath-value&element=element-value" 

 where the xpath-value is:

 /config/devices/entry/vsys/entry/rulebase/security/rules/entry[@name='rule1'] 

 and the element-value is:

 <source><member>src</member></source><destination><member>dst</member></destination><service><member>service</member></service><application><member>application</member></application><action>action</action><source-user><member>src-user</member></source-user><option><disable-server-response-inspection>yes-or-no</disable-server-response-inspection></option><negate-source>yes-or-no</negate-source><negate-destination>yes-or-no</negate-destination><disabled>yes-or-no</disabled><log-start>yes-or-no</log-start><log-end>yes-or-no</log-end><description>description</description><from><member>src-zone</member></from><to><member>dst-zone</member></to> 

 Add an additional member to an address group or list 

 Include the 'list' node in the xpath using
 the member[text()='name'] syntax and
 include the members in the element parameter. For example, to
 add an additional static address object
 named abc to an address group
 named test , use: 

 curl -X POST 'https://firewall/api?type=config&action=set&xpath=/config/devices/entry/vsys/entry[@name='vsys1']/address-group/entry[@name='test']&element=<static><member>abc</member></static>" 

 Create a new IP address on a specific interface 

 Specify the interface and IP address in the request: 

 curl -X GET "https://<firewall>/api?type=config&action=set&xpath=/config/devices/entry[@name='localhost.localdomain']/network/interface/ethernet/entry[@name='ethernet1/1']/layer3/ip&element=<entry name='5.5.5.5/24'/>" 

 Enable or disable a security rule 

 curl -X POST 'https://firewall/api?type=config&action=set&xpath=/config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='<vsys1>']/rulebase/security/rules/entry[@name='<rule-name>']&element=<disabled>yes</disabled>" 

 Altenatively,
 use <disabled>no</disabled> to
 enable a rule. 

 Edit Configuration 
 Use
 action=edit to replace an existing object hierarchy at a specified
 location in the configuration with a new value. Use the xpath parameter to specify the
 location of the object, including the node to be replaced. Use the element parameter to
 specify a new value for the object using its XML object hierarchy (as seen in the output
 of action=show . Replace the application(s) currently used in a rule
 rule1 with a new
 application: 

 curl -X POST 'https://firewall/api?type=config&action=edit&xpath=xpath-value&element=element-value" 

 where 

 xpath=/config/devices/entry/vsys/entry/rulebase/security/rules/entry[@name='rule1']/application&element=<application><member>app-name</member></application> 

 Use the response from the config show API request to create the
 XML body for the
 element. 

 curl -X POST 'https://firewall/api?type=config&action=show" 

 Rename Configuration 

 Use the following API query to rename an address object
 called old_address 
 to new_address 

 curl -X POST 'https://firewall/api?type=config&action=rename&xpath=/config/devices/entry/vsys/entry[@name='vsys1']/address/entry[@name='old_address']&newname=new_address" 

 Clone Configuration 

 Use action=clone to clone an existing configuration object. Use
 the xpath parameter to specify the location of the object
 to be cloned. Use the from parameter to specify the source
 object, and the newname parameter to provide a name for the
 cloned object. 

 curl -X POST 'https://firewall/api?type=config&action=clone&xpath=/config/devices/entry/vsys/entry[@name='vsys1']/rulebase/security/rules&from=/config/devices/entry/vsys/entry[@name='vsys1']/rulebase/security/rules/entry[@name='rule1']&newname=rule2" 

 Move Configuration 

 Use action=move to move the location of an existing
 configuration object. Use the xpath parameter to specify the
 location of the object to be moved, the where parameter to
 specify type of move, and dst parameter to specify the
 destination path. 

 where=after&dst=xpath 

 where=before&dst=xpath 

 where=top 

 where=bottom 

 Use the following API query to move a security policy
 called rule1 to come
 after rule2 

 curl -X POST 'https://firewall/api?type=config&action=move&xpath=/config/devices/entry/vsys/entry[@name='vsys1']/rulebase/security/rules/entry[@name='rule1']&where=after&dst=rule2" 

 Override Configuration 

 Use action=override to override a setting that was pushed to a
 firewall from a template. Use the xpath parameter to specify
 the location of the object to override. 

 curl -X POST 'https://firewall/api?type=config&action=override&xpath=/config/shared/log-settings/snmptrap&element=<entry name="snmp" src="tpl"><version src="tpl"><v2c src="tpl"><server src="tpl"><entry name="test" src="tpl"><manager src="tpl">2.2.2.2</manager><community src="tpl">test</community></entry></server></v2c></version></entry>" 

 Multi-Move and Multi-Clone 

 Use the action=multi-move 
 and action=multi-clone actions to move and clone
 addresses, address groups, services, and more across device groups and virtual
 systems. Templates do not support the multi-move and multi-clone capability. 

 The syntax for multi-move and multi-clone specifies the xpath for the destination
 where the addresses will be moved to, the xpath for the source and the list of
 objects within the specified source. It also includes a flag for displaying the
 errors when the firewall performs a referential integrity check on the multi-move or
 multi-clone action. 

 Move addresses addr1 , addr2 , to device
 group norcal from device
 group socal 

 curl -X POST 'https://firewall/api?type=config&action=multi-move&xpath=/config/devices/entry[@name='localhost.localdomain']/devicegroup/entry[@name='norcal']/address&element=<selected-list><source xpath="/config/devices/entry[@name='localhost.localdomain']/devicegroup/entry[@name='socal']/address"><member>addr1</member><member>addr2</member></source></selected-list><all-errors>no</all-errors>" 

 Clone
 addresses addr1 , addr2 , to device
 group norcal from device
 group socal 

 curl -X POST 'https://firewall/api?type=config&action=multi-clone&xpath=/config/devices/entry[@name='localhost.localdomain']/devicegroup/entry[@name='norcal']/address&element=<selected-list><source xpath="/config/devices/entry[@name='localhost.localdomain']/devicegroup/entry[@name='socal']/address"><member>addr1</member><member>addr2</member></source></selected-list><all-errors>no</all-errors>" 

 Previous 

 Asynchronous and Synchronous Requests to the PAN-OS XML API 

 Next 

 Commit 

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

 PAN-OS 

 Next-Generation Firewall 

 Reference 

 API 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

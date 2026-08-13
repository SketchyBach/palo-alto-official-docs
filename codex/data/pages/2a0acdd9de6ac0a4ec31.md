---
url: https://docs.paloaltonetworks.com/cloud-ngfw-aws/administration/firewall-as-code/cloud-formation-registry
fetched_at: 2026-08-13T15:30:38Z
source: palo-alto-main
---

# Provision Cloud NGFW Resources to Your AWS CFT Clear

Provision Cloud NGFW Resources to Your AWS CFT 

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

 Provision Cloud NGFW Resources to Your AWS CFT 

 Updated on 

 May 19, 2026 

 Focus 

 Download PDF 

 English 

 日本語 (Japanese) 

 Français (French) 

 Deutsch (German) 

 Filter

 Expand All 
 | 
 Collapse All 

 Cloud NGFW for AWS Docs 

 Getting Started 

 Deployment 

 Administration 

 Reference 

 Release Notes 

 New Features 

 Updated on 

 May 19, 2026 

 Focus 

 Home 

 Cloud NGFW for AWS 

 Cloud NGFW for AWS Administration 

 Firewall-as-Code 

 Provision Cloud NGFW Resources to Your AWS CFT 

 Download PDF 

 English 

 日本語 (Japanese) 

 Français (French) 

 Deutsch (German) 

 Cloud NGFW for AWS 

 Provision Cloud NGFW Resources to Your AWS CFT 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Cloud NGFW for AWS Docs 

 Getting Started 

 Deployment 

 Administration 

 Reference 

 Release Notes 

 New Features 

 Previous 

 Configure Automated Account Onboarding 

 Next 

 Cross-Account Role CFT Permissions for Cloud NGFW 

 Provision Cloud NGFW Resources to Your AWS CFT 

 Create Cloud NGFW resources and provision them to your AWS CloudFormation
 template. 

 Where Can I Use This? What Do I Need? 

 Cloud NGFW for AWS 

 Cloud NGFW subscription 

 Palo Alto Networks Customer Support Account (CSP) 

 AWS Marketplace account 

 User role (either tenant or administrator) 

 The Cloud NGFW provides flexibility to provision resources to your AWS
 CloudFormation template (CFT) by allowing you to create your own resources. 

 Enable Programmatic access before using CloudFormation
 Registry with the Cloud NGFW. 

 Use the
 PaloAltoNetworks::CloudNGFW::RuleStack and
 PaloAltoNetworks::CloudNGFW::NGFW schemas to integrate the Cloud NGFW into
 your AWS CloudFormation template. Use the syntax provided in this document to define
 Cloud NGFW firewall configuration settings that you can integrate with AWS CloudFormation Registry . 

 PaloAltoNetworks::CloudNGFW::RuleStack Schema 

 JSON 

 {
 "Type" : "PaloAltoNetworks::CloudNGFW::RuleStack",
 "Properties" : {
 "RuleStackName" : String,
 "RuleStack" : RuleStack,
 "RuleList" : [ Rule, ... ],
 "SecurityObjects" : SecurityObjects,
 "CustomSecurityProfiles":CustomSecurityProfiles,
 }
} 

 YAML 

 Type:PaloAltoNetworks::CloudNGFW::RuleStack
Properties:
 RuleStackName: String
 RuleStack: RuleStack
 RuleList: 
 - Rule
 SecurityObjects: SecurityObjects
 CustomSecurityProfiles: CustomSecurityProfiles
 ProgrammaticAccessToken: String 

 Element Description 

 RuleStackName Enter a descriptive Name for your
 rulestack. 
 JSON 

 “RuleStackName” : String, 

 YAML 

 RuleStackName: String 

 RuleStack Enter a Description for your rulestack. The
 description
 includes: 
 JSON 

 {
 "Scope" : String,
 "Profiles" : RuleStackProfiles,
 "Description" : String
 "Deploy" : String
} 

 YAML 

 Scope: String
Profiles: RuleStackProfiles
Description: String
Deploy: String 

 RuleStackProfiles Identify Profiles for the specified rulestack.
 Profiles
 include: 

 JSON 

 {
 "AntiSpywareProfile" : String,
 "AntiVirusProfile" : String,
 "VulnerabilityProfile" : String,
 "URLFilteringProfile" : String,
 "FileBlockingProfile" : String,
 "OutboundTrustCertificate" : String,
 "OutboundUntrustCertificate" : String
} 

 YAML 

 AntiSpywareProfile: String
AntiVirusProfile: String
VulnerabilityProfile: String
URLFilteringProfile: String
FileBlockingProfile: String
OutboundTrustCertificate: String
OutboundUntrustCertificate: String 

 Rule Establish rules for the rulestack. Rules
 include: 

 JSON 

 {
 "RuleName" : String,
 "Description" : String,
 "RuleListType" : String,
 "Priority" : Integer,
 "Enabled" : Boolean,
 "Source" : RuleSource,
 "NegateSource" : Boolean,
 "Destination" : RuleDestination,
 "NegateDestination" : Boolean,
 "Applications" : [ String, ... ],
 "Category" : UrlCategory,
 "Protocol" : String,
 "AuditComment" : String,
 "Action" : String,
 "Logging" : Boolean,
 "DecryptionRuleType" : String,
 "Tags" : [ Tag, ... ]
} 

 YAML 

 RuleName: String
Description: String
RuleListType: String
Priority: Integer
Enabled: Boolean
Source: RuleSource
NegateSource: Boolean
Destination: RuleDestination
NegateDestination: Boolean
Applications: 
 - String
Category: UrlCategory
Protocol: String
AuditComment: String
Action: String
Logging: Boolean
DecryptionRuleType: String
Tags: 
 - Tag 

 RuleSource Set the collection of rules using RuleSource .
 RuleSource
 includes: 

 JSON 

 {
 "Cidrs" : [ String, ... ],
 "PrefixLists" : [ String, ... ],
 "Countries" : [ String, ... ],
 "Feeds" : [ String, ... ]
 // RuleStackname?
 } 

 YAML 

 cidrs: 
 - String
PrefixLists: 
 - String
Countries: 
 - String
Feeds: 
 - String 

 RuleDestination Set the RuleDestination for the web service
 supporting the confirmation URL and one or more data collection
 URLs. RuleDestination
 includes: 

 JSON 

 {
 "Cidrs" : [ String, ... ],
 "FqdnLists" : [ String, ... ],
 "PrefixLists" : [ String, ... ],
 "Countries" : [ String, ... ],
 "Feeds" : [ String, ... ]
 // RuleStackname?
 } 

 YAML 

 Cidrs: 
 - String
FqdnLists: 
 - String
PrefixLists: 
 - String
Countries: 
 - String
Feeds: 
 - String 

 Tag Specify a Tag for the rulestack. A Tag
 includes: 

 JSON 

 {
 "Key" : String,
 "Value" : String
} 

 YAML 

 Key: String
Value: String 

 UrlCategory Use the UrlCategory to match criteria in
 authentication, decryption, QoS, and Security policy rules.
 UrlCategory
 includes: 

 JSON 

 {
 "URLCategoryNames" : [ String, ... ],
 "Feeds" : [ String, ... ]
} 

 YAML 

 URLCategoryNames: 
 - String
Feeds: 
 - String 

 SecurityObjects Set the SecurityObjects for the rulestack.
 SecurityObjects
 include: 

 JSON 

 {
 "PrefixLists" : PrefixList,
 "FqdnLists" : FqdnList,
 "CustomUrlCategories" : CustomUrlCategory,
 "IntelligentFeeds" : IntelligentFeed,
 "CertificateLists" : CertificateList
} 

 YAML 

 PrefixList: PrefixList
FqdnList: FqdnList
CustomUrlCategory: CustomUrlCategory
IntelligentFeed: IntelligentFeed
CertificateList: CertificateList 

 CustomSecurityProfiles Set CustomSecurityProfiles to minimize
 antivirus inspection for traffic between trusted security zones, and
 to maximize the inspection of traffic received from untrusted zones,
 such as the internet, as well as the traffic sent to highly
 sensitive destinations, such as server farms. CustomSecurityProfiles
 include: 

 JSON 

 {
 "FileBlocking" : FileBlocking
} 

 YAML 

 FileBlocking: FileBlocking 

 PrefixLists Use PrefixList to filter routes based on
 prefixes. By defining an order number and IP prefixes, a branch or a
 data center ION device can permit or deny routes. The dynamic,
 autogenerated prefix list is based on what the ION device
 advertises. Prefixes can be split or non-split. A PrefixList
 includes: 

 JSON 

 {
 "Name" : String,
 "PrefixList" : [ String, ... ],
 "AuditComment" : String,
 "Description" : String
} 

 YAML 

 Name: String
PrefixList: 
 - String
AuditComment: String
Description: String 

 FqdnLists With the FqdnLists object, DNS provides the
 FQDN resolution to the IP addresses, removing the need to know the
 IP addresses and manually updating them every time the FQDN resolves
 to a new IP address. FqdnLists
 include: 

 JSON 

 {
 "Name" : String,
 "Description" : String,
 "FqdnList" : [ String, ... ],
 "AuditComment" : String
} 

 YAML 

 Name: String
Description: String
FqdnList: 
 - String
AuditComment: String 

 CustomUrlCategories Use CustomURLCategories to create a custom URL
 filtering object to specify exceptions to URL category enforcement,
 and to create a custom URL category based on multiple URL
 categories: 
 Define exceptions to URL category enforcement—Create a
 custom list of URLs that you want to use as match criteria
 in a Security policy rule. This is a good way to specify
 exceptions to URL categories, where you’d like to enforce
 specific URLs differently than the URL category to which
 they belong. 

 Define a custom URL category based on multiple PAN-DB
 categories—This allows you to target enforcement for
 websites that match a set of categories. The website or page
 must match all the categories defined as part of the custom
 category. 

 CustomURLCategories
 include: 

 JSON 

 {
 "URLTargets" : [ String, ... ],
 "Name" : String,
 "Description" : String,
 "Action" : String,
 "AuditComment" : String
} 

 YAML 

 URLTargets: 
 - String
Name: String
Description: String
Action: String
AuditComment: String 

 IntelligentFeeds Use IntelligentFeeds to continually feed the
 most up to date threat intelligence data. IntelligentFeeds
 include: 

 JSON 

 {
 "Name" : String,
 "Description" : String,
 "Certificate" : String,
 "FeedURL" : String,
 "Type" : String,
 "Frequency" : String,
 "Time" : Integer,
 "AuditComment" : String
} 

 YAML 

 Name: String
Description: String
Certificate: String
FeedURL: String
Type: String
Frequency: String
Time: Integer
AuditComment: String 

 CertificateObjects Use CertificateObjects to define elements of
 the certificate. CertificateObjects
 includes: 

 JSON 

 {
 "Name" : String,
 "Description" : String,
 "CertificateSignerArn" : String,
 "CertificateSelfSigned" : Boolean,
 "AuditComment" : String
} 

 YAML 

 Name: String
Description: String
CertificateSignerArn: String
CertificateSelfSigned: Boolean
AuditComment: String 

 FileBlocking Use FileBlocking to identify specific file
 types that you want to block or monitor. For most traffic (including
 traffic on your internal network) you will want to block files that
 are known to carry threats or that have no real use case for upload
 or download. FileBlocking
 includes: 

 JSON 

 {
 "Direction" : String,
 "FileType" : String,
 "Description" : String,
 "Action" : String,
 "AuditComment" : String
} 

 YAML 

 Direction: String
FileType: String
Description: String
Action: String
AuditComment: String 

 PaloAltoNetworks::CloudNGFW::NGFW Schema 

 JSON 

 {
 "Type": "PaloAltoNetworks::CloudNGFW::NGFW",
 "Properties" : {
 "Description" : String,
 "EndpointMode" : String,
 "FirewallName" : String,
 "RuleStackName" : String,
 "RuleStackName" : String,
 "SubnetMappings" : [ String, ... ],
 "Tags" : [ Map, ... ],
 "VpcId" : String,
 "UpdateToken" : String,
 "LogDestinationConfigs" : [ LogProfileConfig, ... ],
 "CloudWatchMetricNamespace" : String,
} 

 YAML 

 Type: PaloAltoNetworks::CloudNGFW::NGFWProperties:
 AppIdVersion: String
 AutomaticUpgradeAppIdVersion: Boolean
 Description: String
 EndpointMode: String
 FirewallName: String
 RuleStackName: String
 RuleStackName: String
 SubnetMappings: 
 - String
 Tags: 
 - Map
 VpcId: String
 UpdateToken: String 
 LogDestinationConfigs: 
 - LogProfileConfig
 CloudWatchMetricNamespace: String
 ProgrammaticAccessToken: String 

 Element Description 

 LogProfileConfig Use LogProfileConfig to display entries for
 changes to the firewall
 configuration. 

 JSON 

 {
 "LogDestination" : String,
 "LogDestinationType" : String,
 "LogType" : String} 

 YAML 

 LogDestination: String
LogDestinationType: String
LogType: String 

 Activate Public Extensions 

 Activate both
 the PaloAltoNetworks::CloudNGFW::NGFW and
 PaloAltoNetworks::CloudNGFW::RuleStack public extensions for your
 account: 

 Create an execution role ARN for the extensions. Both extensions can use the
 same role. Establish trust relationships in the role to consume the CloudFormation
 templates: 

 After establishing the trust relationship, activate the extensions: 

 To ship logs in AWS CloudWatch , or using the Cloud NGFW for AWS . 

 Stack Outputs 

 You can access these resource attributes as stack outputs: 

 FirewallResource:

"/properties/ReadFirewall",
"/properties/ReadFirewall/AccountId",
"/properties/ReadFirewall/AppIdVersion",
"/properties/ReadFirewall/AutomaticUpgradeAppIdVersion",
"/properties/ReadFirewall/EndpointMode",
"/properties/ReadFirewall/FirewallName",
"/properties/ReadFirewall/MultiVpcEnable",
"/properties/ReadFirewall/Description",
"/properties/ReadFirewall/VpcId",
"/properties/ReadFirewall/SubnetMappings",
"/properties/ReadFirewall/LinkId",
"/properties/ReadFirewall/Attachments",
"/properties/ReadFirewall/LinkStatus",
"/properties/ReadFirewall/FirewallStatus",
"/properties/ReadFirewall/RuleStackStatus",
"/properties/ReadFirewall/FailureReason",
"/properties/ReadFirewall/EndpointServiceName",
"/properties/ReadFirewall/Tags",
"/properties/ReadFirewall/RuleStackName",
"/properties/ReadFirewall/GlobalRuleStackName"

RuleStackResource:

"/properties/RuleStackCandidate",
"/properties/RuleStackRunning",
"/properties/RuleStackCandidate/AccountId",
"/properties/RuleStackRunning/AccountId",
"/properties/RuleStackCandidate/Scope",
"/properties/RuleStackRunning/Scope",
"/properties/RuleStackCandidate/MinAppIdVersion",
"/properties/RuleStackRunning/MinAppIdVersion",
"/properties/RuleStackCandidate/Description",
"/properties/RuleStackRunning/Description",
"/properties/RuleStackRunning/Profiles/AntiSpywareProfile",
"/properties/RuleStackCandidate/Profiles/AntiSpywareProfile",
"/properties/RuleStackRunning/Profiles/AntiVirusProfile",
"/properties/RuleStackCandidate/Profiles/AntiVirusProfile",
"/properties/RuleStackCandidate/Profiles/VulnerabilityProfile",
"/properties/RuleStackRunning/Profiles/VulnerabilityProfile",
"/properties/RuleStackCandidate/Profiles/URLFilteringProfile",
"/properties/RuleStackRunning/Profiles/URLFilteringProfile",
"/properties/RuleStackCandidate/Profiles/FileBlockingProfile",
"/properties/RuleStackRunning/Profiles/FileBlockingProfile 

 Execution Role 

 Use the following for the execution role: 

 Trust relationship: 

 {
"Version": "2012-10-17",
"Statement": [
{
"Effect": "Allow",
"Principal": {
"Service": "resources.cloudformation.amazonaws.com"
},
"Action": "sts:AssumeRole",
"Condition": {
"StringEquals": {
"aws:SourceAccount": "{customer-account-id}"
},
"StringLike": {
"aws:SourceArn": "arn:aws:cloudformation:*:{customer-account-id}":type/resource/PaloAltoNetworks-CloudNGFW-NGFW/*"
}
}
},
{
"Effect": "Allow",
"Principal": {
"Service": "resources.cloudformation.amazonaws.com"
},
"Action": "sts:AssumeRole",
"Condition": {
"StringEquals": {
"aws:SourceAccount": {customer-account-id}"
},
"StringLike": {
"aws:SourceArn": "arn:aws:cloudformation:*:{customer-account-id}":type/resource/PaloAltoNetworks-CloudNGFW-RuleStack/*"
}
}
}
]
}

Tags:

CloudNGFWRulestackAdmin: Yes
CloudNGFWFirewallAdmin: Yes
CloudNGFWGlobalRulestackAdmin: Yes

Permissions:

AmazonAPIGatewayInvokeFullAccess 

 Create a role and then use the role ARN to
 configure the execution role ARN during activation. You can't create a resource
 without configuring the execution role during activation. 

 CloudFormation Firewall Resource Schema Example 

 Use the following for as an example for the rulestack
 schema: 

 {
 "typeName": "PaloAltoNetworks::CloudNGFW::NGFW",
 "description": "A Firewall resource offers Palo Alto Networks next-generation firewall capabilities with built-in resiliency, scalability, and life-cycle management.",
 "sourceUrl": "https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git",
 "definitions" : {
 "LogProfileConfig": {
 "title": "LogProfileConfig",
 "description": "Add Log profile config",
 "type": "object",
 "properties": {
 "LogDestination": {
 "title": "Logdestination",
 "minLength": 1,
 "maxLength": 128,
 "type": "string"
 },
 "LogDestinationType": {
 "title": "Logdestinationtype",
 "enum": ["S3", "CloudWatchLogs", "KinesisDataFirehose"],
 "type": "string"
 },
 "LogType": {
 "title": "Logtype",
 "enum": ["TRAFFIC", "DECRYPTION", "THREAT"],
 "type": "string"
 }
 },
 "required": ["LogDestination", "LogDestinationType", "LogType"],
 "additionalProperties": false
 },
 "SubnetMappings": {
 "type": "array",
 "items": {
 "type": "object",
 "properties": {
 "AvailabilityZone": {
 "title": "availabilityZone",
 "type": "string"
 },
 "SubnetId": {
 "title": "subnetId",
 "type": "string"
 }
 },
 "additionalProperties": false
 }
 }
 },
 "properties": {
 "AccountId": {
 "title": "Accountid",
 "pattern": "^[0-9]+$",
 "type": "string",
 "minLength": 1
 },
 "AppIdVersion": {
 "title": "Appidversion",
 "minLength": 1,
 "maxLength": 64,
 "pattern": "^[0-9]+-[0-9]+$",
 "type": "string"
 },
 "AutomaticUpgradeAppIdVersion": {
 "title": "Automaticupgradeappidversion",
 "default": true,
 "type": "boolean"
 },
 "Description": {
 "title": "Description",
 "type": "string",
 "minLength": 1
 },
 "EndpointMode": {
 "title": "Endpointmode: CustomerManaged Or ServiceManaged",
 "enum": ["ServiceManaged", "CustomerManaged"],
 "type": "string"
 },
 "FirewallName": {
 "title": "Firewallname",
 "minLength": 1,
 "maxLength": 128,
 "pattern": "^[a-zA-Z0-9-]+$",
 "type": "string"
 },
 "MultiVpcEnable": {
 "title": "MultiVpcEnable",
 "type": "boolean"
 },
 "RuleStackName": {
 "title": "Rulestackname",
 "type": "string",
 "minLength": 1
 },
 "SubnetMappings": {
 "$ref": "#/definitions/SubnetMappings"
 },
 "AssociateSubnetMappings": {
 "$ref": "#/definitions/SubnetMappings"
 },
 "DisassociateSubnetMappings": {
 "$ref": "#/definitions/SubnetMappings" 
 },
 "Tags": {
 "title": "Tags",
 "type": "array",
 "items": {
 "type": "object"
 }
 },
 "VpcId": {
 "title": "Vpcid",
 "type": "string",
 "minLength": 1
 },
 "LinkId": {
 "title": "LinkId",
 "type": "string",
 "minLength": 1
 },
 "LogDestinationConfigs": {
 "title": "Logdestinationconfigs",
 "type": "array",
 "items": {
 "$ref": "#/definitions/LogProfileConfig"
 }
 },
 "CloudWatchMetricNamespace": {
 "title": "Cloudwatchmetricnamespace",
 "type": "string",
 "minLength": 1
 }
 },
 "additionalProperties": false,
 "required": [
 "FirewallName"
 ],
 "createOnlyProperties": [
 "/properties/FirewallName"
 ],
 "primaryIdentifier": [
 "/properties/FirewallName"
 ],
 "handlers": {
 "create": {
 "permissions": [
 "execute-api:Invoke"
 ]
 },
 "read": {
 "permissions": [
 "execute-api:Invoke"
 ]
 },
 "update": {
 "permissions": [
 "execute-api:Invoke"
 ]
 },
 "delete": {
 "permissions": [
 "execute-api:Invoke"
 ]
 }
 }
}

 Rulestack Schema Example 

 Use the following as an example for the rulestack
 schema: 

 {
 "typeName": "PaloAltoNetworks::CloudNGFW::RuleStack",
 "description": "A rulestack defines the NGFW's advanced access control (APP-ID, URL Filtering) and threat prevention behavior.",
 "sourceUrl": "https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git",
 "definitions": {
 "RuleStack": {
 "title": "RuleStack",
 "type": "object",
 "properties": {
 "AccountId": {
 "title": "Accountid",
 "pattern": "^[0-9]+$",
 "type": "string",
 "minLength": 1
 },
 "Scope": {
 "title": "Scope",
 "default": "Local",
 "enum": ["Local", "Global"],
 "type": "string"
 },
 "LookupXForwardedFor": {
 "title": "LookupXForwardedFor",
 "default": "None",
 "enum": ["SecurityPolicy", "None"],
 "type": "string"
 },
 "MinAppIdVersion": {
 "title": "Minappidversion",
 "default": "8433-6838",
 "pattern": "8\\d\\d\\d\\-\\d\\d\\d\\d",
 "type": "string"
 },
 "Profiles": {
 "$ref": "#/definitions/RuleStackProfiles"
 },
 "Description": {
 "title": "Description",
 "maxLength": 512,
 "type": "string"
 },
 "Deploy": {
 "title": "Deploy",
 "description": "Deploy RuleStack YES/NO",
 "default": "YES",
 "type": "string"
 }
 },
 "additionalProperties": false
 },
 "RuleStackProfiles": {
 "title": "RuleStackProfiles",
 "type": "object",
 "properties": {
 "AntiSpywareProfile": {
 "title": "Antispywareprofile",
 "default": "BestPractice", 
 "enum": ["BestPractice", "None"],
 "type": "string"
 },
 "AntiVirusProfile": {
 "title": "Antivirusprofile",
 "default": "BestPractice",
 "enum": ["BestPractice", "None"],
 "type": "string"
 },
 "VulnerabilityProfile": {
 "title": "Vulnerabilityprofile",
 "default": "BestPractice",
 "enum": ["BestPractice", "None"],
 "type": "string"
 },
 "URLFilteringProfile": {
 "title": "Urlfilteringprofile",
 "default": "None",
 "enum": ["BestPractice", "None"],
 "type": "string"
 },
 "FileBlockingProfile": {
 "title": "Fileblockingprofile",
 "default": "BestPractice",
 "enum": ["Custom", "BestPractice", "None"],
 "type": "string"
 },
 "OutboundTrustCertificate": {
 "title": "Outboundtrustcertificate",
 "maxLength": 63,
 "type": "string"
 },
 "OutboundUntrustCertificate": {
 "title": "Outbounduntrustcertificate",
 "maxLength": 63,
 "type": "string"
 }
 },
 "additionalProperties": false
 },
 "Tag": {
 "title": "Tag",
 "type": "object",
 "properties": {
 "Key": {
 "title": "Key",
 "minLength": 1,
 "maxLength": 128,
 "type": "string"
 },
 "Value": {
 "title": "Value",
 "minLength": 1,
 "maxLength": 128,
 "type": "string"
 }
 },
 "required": ["Key", "Value"],
 "additionalProperties": false
 },
 "Rule" : {
 "title": "Rule",
 "type": "object",
 "properties": {
 "RuleName": {
 "title": "Rulename",
 "minLength": 1,
 "maxLength": 48,
 "pattern": "^[a-zA-Z0-9-]+$",
 "type": "string"
 },
 "Description": {
 "title": "Description",
 "maxLength": 512,
 "type": "string"
 },
 "RuleListType": {
 "title": "RuleListType",
 "description": "RuleList type: LocalRule, PreRule, PostRule",
 "type": "string"
 },
 "Priority": {
 "title": "Priority",
 "description": "Priority of the Rule",
 "type": "integer"
 },
 "Enabled": {
 "title": "Enabled",
 "default": true,
 "type": "boolean"
 },
 "Source": {
 "$ref": "#/definitions/RuleSource"
 },
 "NegateSource": {
 "title": "Negatesource",
 "default": false,
 "type": "boolean"
 },
 "Destination": {
 "$ref": "#/definitions/RuleDestination"
 },
 "NegateDestination": {
 "title": "Negatedestination",
 "default": false,
 "type": "boolean"
 },
 "Applications": {
 "title": "Applications",
 "default": ["any"],
 "type": "array",
 "items": {
 "type": "string",
 "maxLength": 63
 }
 },
 "Category": {
 "$ref": "#/definitions/UrlCategory"
 },
 "Protocol": {
 "title": "Protocol",
 "default": "application-default",
 "maxLength": 63,
 "type": "string"
 },
 "ProtPortList": {
 "title": "ProtPortList",
 "type": "array",
 "items": {
 "type": "string",
 "maxLength": 63
 }
 },
 "AuditComment": {
 "title": "Auditcomment",
 "maxLength": 512,
 "type": "string"
 },
 "Action": {
 "title": "Action",
 "default": "Allow",
 "enum": ["Allow", "DenySilent", "DenyResetServer", "DenyResetBoth"],
 "type": "string"
 },
 "Logging": {
 "title": "Logging",
 "default": false,
 "type": "boolean"
 },
 "DecryptionRuleType": {
 "title": "Decryptionruletype",
 "enum": ["SSLOutboundInspection", "SSLInboundInspection", "SSLOutboundNoInspection", "SSLInboundNoInspection"],
 "type": "string"
 },
 "InboundInspectionCertificate": {
 "title": "InboundInspectionCertificate",
 "type": "string",
 "maxLength": 63
 },
 "Tags": {
 "title": "Tags",
 "maxItems": 200,
 "type": "array",
 "items": {
 "$ref": "#/definitions/Tag"
 }
 }
 },
 "required": ["RuleName", "RuleListType", "Priority"],
 "additionalProperties": false
 },
 "RuleSource": {
 "title": "RuleSource",
 "type": "object",
 "properties": {
 "Cidrs": {
 "title": "Cidrs",
 "type": "array",
 "items": {
 "type": "string",
 "maxLength": 24
 }
 },
 "PrefixLists": {
 "title": "Prefixlists",
 "type": "array",
 "items": {
 "type": "string",
 "maxLength": 63
 }
 },
 "Countries": {
 "title": "Countries",
 "description": "Country code",
 "type": "array",
 "items": {
 "type": "string",
 "maxLength": 2
 }
 },
 "Feeds": {
 "title": "Feeds",
 "type": "array",
 "items": {
 "type": "string",
 "maxLength": 63
 }
 }
 },
 "additionalProperties": false
 },
 "RuleDestination": {
 "title": "RuleDestination",
 "type": "object",
 "properties": {
 "Cidrs": {
 "title": "Cidrs",
 "type": "array",
 "items": {
 "type": "string",
 "maxLength": 24
 }
 },
 "FqdnLists": {
 "title": "Fqdnlists",
 "type": "array",
 "items": {
 "type": "string",
 "maxLength": 63
 }
 },
 "PrefixLists": {
 "title": "Prefixlists",
 "type": "array",
 "items": {
 "type": "string",
 "maxLength": 63
 }
 },
 "Countries": {
 "title": "Countries",
 "description": "Country code",
 "type": "array",
 "items": {
 "type": "string",
 "maxLength": 2
 }
 },
 "Feeds": {
 "title": "Feeds",
 "type": "array",
 "items": {
 "type": "string",
 "maxLength": 63
 }
 }
 },
 "additionalProperties": false
 },
 "UrlCategory": {
 "title": "UrlCategory",
 "type": "object",
 "properties": {
 "URLCategoryNames": {
 "title": "Urlcategorynames",
 "type": "array",
 "items": {
 "type": "string",
 "maxLength": 128
 }
 },
 "Feeds": {
 "title": "Feeds",
 "type": "array",
 "items": {
 "type": "string",
 "maxLength": 63
 }
 }
 },
 "additionalProperties": false
 },
 "CustomSecurityProfiles":{
 "description": "Custom Security Profiles object",
 "type": "object",
 "properties": {
 "FileBlocking": {
 "$ref": "#/definitions/FileBlocking"
 }
 },
 "additionalProperties": false
 },
 "FileBlocking":{
 "title": "FileBlocking",
 "type": "object",
 "properties": {
 "Direction": {
 "title": "Direction",
 "default": "both",
 "enum": ["upload", "download", "both"],
 "type": "string"
 },
 "FileType": {
 "title": "FileType",
 "type": "string"
 },
 "Description": {
 "title": "Description",
 "minLength": 1,
 "maxLength": 255,
 "type": "string"
 },
 "Action": {
 "title": "Action",
 "default": "alert",
 "enum": ["alert", "block", "continue"],
 "type": "string"
 },
 "AuditComment": {
 "title": "Auditcomment",
 "type": "string"
 }
 },
 "required": ["FileType"],
 "additionalProperties": false
 },
 "SecurityObjects": {
 "description": "Security objects",
 "type": "object",
 "properties": {
 "PrefixLists": {
 "type": "array",
 "uniqueItems": false,
 "items": {
 "$ref": "#/definitions/PrefixList"
 }
 },
 "FqdnLists": {
 "type": "array",
 "uniqueItems": false,
 "items": {
 "$ref": "#/definitions/FqdnList"
 }
 },
 "CustomUrlCategories": {
 "type": "array",
 "uniqueItems": false,
 "items": {
 "$ref": "#/definitions/CustomUrlCategory"
 }
 },
 "IntelligentFeeds": {
 "type": "array",
 "uniqueItems": false,
 "items": {
 "$ref": "#/definitions/IntelligentFeed"
 }
 },
 "CertificateObjects":{
 "type": "array",
 "uniqueItems": false,
 "items": {
 "$ref": "#/definitions/CertObject"
 }
 }
 },
 "additionalProperties": false
 },
 "PrefixList": {
 "title": "PrefixList",
 "description": "SecurityObjects PrefixList",
 "type": "object",
 "properties": {
 "Name": {
 "title": "Name",
 "minLength": 1,
 "maxLength": 58,
 "pattern": "^[a-zA-Z0-9-]+$",
 "type": "string"
 },
 "PrefixList": {
 "title": "Prefixlist",
 "type": "array",
 "items": {
 "type": "string"
 }
 },
 "AuditComment": {
 "title": "Auditcomment",
 "maxLength": 512,
 "type": "string"
 },
 "Description": {
 "title": "Description",
 "maxLength": 512,
 "type": "string"
 }
 },
 "required": ["Name", "PrefixList"],
 "additionalProperties": false
 },
 "FqdnList":{
 "title": "FqdnList",
 "type": "object",
 "properties": {
 "Name": {
 "title": "Name",
 "minLength": 1,
 "maxLength": 58,
 "pattern": "^[a-zA-Z0-9-]+$",
 "type": "string"
 },
 "Description": {
 "title": "Description",
 "maxLength": 512,
 "type": "string"
 },
 "FqdnList": {
 "title": "Fqdnlist",
 "type": "array",
 "items": {
 "type": "string",
 "minLength": 1,
 "maxLength": 255,
 "pattern": "^[a-zA-Z0-9._-]+$"
 }
 },
 "AuditComment": {
 "title": "Auditcomment",
 "maxLength": 512,
 "type": "string"
 }
 },
 "required": ["Name", "FqdnList"],
 "additionalProperties": false
 },
 "CustomUrlCategory":{
 "title": "CustomURLCategory",
 "type": "object",
 "properties": {
 "URLTargets": {
 "title": "Urltargets",
 "type": "array",
 "items": {
 "type": "string",
 "minLength": 1,
 "maxLength": 255
 }
 },
 "Name": {
 "title": "Name",
 "minLength": 1,
 "maxLength": 58,
 "pattern": "^[a-zA-Z0-9-]+$",
 "type": "string"
 },
 "Description": {
 "title": "Description",
 "minLength": 1,
 "maxLength": 255,
 "type": "string"
 },
 "Action": {
 "title": "Action",
 "type": "string",
 "default": "none",
 "enum": ["none", "allow", "alert", "block"]
 },
 "AuditComment": {
 "title": "Auditcomment",
 "type": "string"
 }
 },
 "required": ["URLTargets"],
 "additionalProperties": false
 },
 "IntelligentFeed":{
 "title": "IntelligentFeed",
 "type": "object",
 "properties": {
 "Name": {
 "title": "Name",
 "minLength": 1,
 "maxLength": 63,
 "pattern": "^[a-zA-Z0-9-]+$",
 "type": "string"
 },
 "Description": {
 "title": "Description",
 "maxLength": 512,
 "type": "string"
 },
 "Certificate": {
 "title": "Certificate",
 "type": "string"
 },
 "FeedURL": {
 "title": "Feedurl",
 "minLength": 1,
 "maxLength": 255,
 "pattern": "^(http|https)://.+$",
 "type": "string"
 },
 "Type": {
 "title": "Type",
 "enum": ["IP_LIST", "URL_LIST"],
 "type": "string"
 },
 "Frequency": {
 "title": "Frequency",
 "enum": ["HOURLY", "DAILY"],
 "type": "string"
 },
 "Time": {
 "title": "Time",
 "default": 3,
 "minimum": 0,
 "maximum": 23,
 "type": "integer"
 },
 "AuditComment": {
 "title": "Auditcomment",
 "maxLength": 512,
 "type": "string"
 }
 },
 "required": ["Name", "FeedURL", "Type", "Frequency"],
 "additionalProperties": false
 },
 "CertObject":{
 "title": "Certificate Object",
 "type": "object",
 "properties": {
 "Name": {
 "title": "Name",
 "minLength": 1,
 "maxLength": 63,
 "pattern": "^[a-zA-Z0-9-]+$",
 "type": "string"
 },
 "Description": {
 "title": "Description",
 "maxLength": 512,
 "type": "string"
 },
 "CertificateSignerArn": {
 "title": "Certificatesignerarn",
 "type": "string"
 },
 "CertificateSelfSigned": {
 "title": "Certificateselfsigned",
 "default": false,
 "type": "boolean"
 },
 "AuditComment": {
 "title": "Auditcomment",
 "maxLength": 512,
 "type": "string"
 }
 },
 "required": ["Name"],
 "additionalProperties": false
 }
 },
 "properties": {
 "RuleStackName": {
 "description": "Rule stack name",
 "minLength": 1,
 "maxLength": 128,
 "pattern": "^[a-zA-Z0-9-]+$",
 "type": "string"
 },
 "RuleStack": {
 "$ref": "#/definitions/RuleStack"
 },
 "RuleList": {
 "description": "list of rules",
 "type": "array",
 "uniqueItems": false,
 "items": {
 "$ref": "#/definitions/Rule"
 }
 },
 "SecurityObjects": {
 "$ref": "#/definitions/SecurityObjects"
 },
 "CustomSecurityProfiles": {
 "$ref": "#/definitions/CustomSecurityProfiles"
 }
 },
 "additionalProperties": false,
 "required": [
 "RuleStackName"
 ],
 "createOnlyProperties": [
 "/properties/RuleStackName"
 ],
 "primaryIdentifier": [
 "/properties/RuleStackName"
 ],
 "handlers": {
 "create": {
 "permissions": [
 "execute-api:Invoke"
 ]
 },
 "read": {
 "permissions": [
 "execute-api:Invoke"
 ]
 },
 "update": {
 "permissions": [
 "execute-api:Invoke"
 ]
 },
 "delete": {
 "permissions": [
 "execute-api:Invoke"
 ]
 }
 }
}

 Previous 

 Configure Automated Account Onboarding 

 Next 

 Cross-Account Role CFT Permissions for Cloud NGFW 

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

 Firewalls 

 PAN-OS 

 PAN-OS SD-WAN 

 Service Provider 

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

 Best Practices 

 Best Practices Library 

 Experts Corner 

 Solutions Docs from Product Experts 

 Cloud NGFW for AWS 

 Administration 

 AWS 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

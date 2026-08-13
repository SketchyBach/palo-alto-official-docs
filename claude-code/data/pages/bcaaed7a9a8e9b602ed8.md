---
url: https://docs.paloaltonetworks.com/vm-series/activation-and-onboarding/vm-series-models/licensing-api/use-the-licensing-api
fetched_at: 2026-08-13T17:41:11Z
source: palo-alto-main
---

# Use the Licensing API Clear

Use the Licensing API 

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

 Use the Licensing API 

 Updated on 

 Fri Jun 19 07:15:14 PDT 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 VM-Series Firewall Docs 

 Activation & Onboarding 

 Getting Started 

 Upgrade 

 Deployment 

 Select a Document 

 Public Cloud 

 Private Cloud 

 Updated on 

 Fri Jun 19 07:15:14 PDT 2026 

 Focus 

 Home 

 VM-Series 

 VM-Series Models 

 Model-Based Licensing API 

 Use the Licensing API 

 Download PDF 

 VM-Series 

 Use the Licensing API 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 VM-Series Firewall Docs 

 Activation & Onboarding 

 Getting Started 

 Upgrade 

 Deployment 

 Select a Document 

 Public Cloud 

 Private Cloud 

 Previous 

 Manage the Licensing API Key 

 Next 

 What Happens When Licenses Expire? 

 Use the Licensing API 

 Where Can I Use This? What Do I Need? 

 VM-Series deployment 

 VM-Series 10.x or above 

 Panorama running PAN-OS 10.1.x or above versions 

 Customer Support Portal (CSP) account with one of the following
 user roles: 
 Superuser, Standard User, Limited User, Threat
 Researcher, AutoFocus Trial Role, Group superuser, Group
 Standard User, Group Limited User, Group Threat
 Researcher, Authorized Support Center (ASC) User, and
 ASC Full Service User. 

 Superuser access to the VM-Series 
 firewall 

 An API request must use the HTTP POST method, and you must include
the API key in the apikey HTTP request header and pass the request
parameters as URL-encoded form data with content-type application/x-www-form-urlencoded . 

 The API Version is optional and can include the following values—0
or 1. If specified, it must be included in the version HTTP
request header. The current API version is 1; if you do not specify
a version, or specify version 0, the request uses the current API
version. 

 All API responses are represented in json. 

 The HTTP Error Codes that the licensing server returns are as follows: 

 200 Success 

 400 Error 

 401 Invalid API Key 

 500 Server Error 

 Before you begin, get
your Licensing API key and copy it to your local drive. This
is required before you can perform any of the following tasks: 

 Activate Licenses 

 Header : apikey 

 Parameters : uuid ,
 cpuid , authCode ,
 memory , serialNumber ,
 and vCPU 

 URL :
 https://api.paloaltonetworks.com/api/license/activate 

 The parameters uuid, cpuid, authCode, and serialNumber apply for all VM-Series
 licenses, regardless of PAN-OS version. 

 The optional parameters memory and
 vCPU only apply for Flexible vCPUs (PAN-OS 10.0.4
 and later). 

 For the initial license activation, provide the parameters in the API
 request. For example: 

 curl -i -H "apikey:a103e3065360acc5e01666fb9335964fcfe668100666db6f3ff43d4544de0###" 
--data-urlencode cpuid=AWS:57060500FFFBE### 
--data-urlencode uuid=EC2278FF-F0CB-45E2-343B-E97984BAC### 
--data-urlencode authCode=D3521### 
--data-urlencode vcpu=4 
--data-urlencode memory=8388608 
https://api.paloaltonetworks.com/api/license/activate 

 If you did not save the license keys or had network connection issues during
 initial license activation, you can retrieve the license(s) for a firewall
 that you have previously activated. 

 In the API request, provide the cpuid and
 uuid , or, provide the
 serialNumber of the firewall. 

 Sample request for initial license activation using Curl: 

 curl -i -H "apikey:$APIKEY" --data-urlencode cpuid=51060400FFFBAB1F --data-urlencode uuid=564D0E5F-3F22-5FAD-DA58-47352C6229FF --data-urlencode authCode=I7115398 https://api.paloaltonetworks.com/api/license/activate 

 Sample API response : 

 [{"lfidField":"13365773","partidField":"PAN-SVC-PREM-VM-300","featureFi--eld":
"Premium","feature_descField":"24 x 7 phone support; advanced replacement hardware service","keyField":"m4iZEL1t3n6Oa+6ll1L7itDZTphYw48N1AMOZXutDgExC5f5pOA52+Qg1jmAxanB\nKOyat4FJI4k2hWiBYz9cONuKoiaNOtAGhJvAuZmYgqAZejKueWrTzCuLrwxI/iEw\nkRGR3cYG+j6o84RitR937m2iOk2v9o8RSfLVilgX28nqmcO8LcAnTqbrRWdFtwVk\nluz47AUMXauuqwpMipouQYjk0ZL7fTHHslhyL7yFjCyxBoYXOt3JiqQ0OCDdBdDI\n91RkVPylEwTKgSXm3xpzbmC2ciUR5b235gyqdyW8eQXKvaThuR8YyHr1Pdw/lAjs\npyyIVFa6FufPacfB2RHApQ==\n","auth_codeField":"","errmsgField":null,
"typeField":"SUP","regDateField":"2016-06-03T08:18:41","startDateField":"5/29/2016",
"vm_capacityField":null,"uuidField":null,"cpuidField":null,"mac_baseField":null,
"mac_countField":null,"drrField":null,"expirationField":"8/29/2016 12:00:00 AM","PropertyChanged":null},{"lfidField":"13365774","partidField":"PAN-VM-300-TP",
"featureField":"Threat Prevention","feature_descField":"Threat Prevention","keyField":"NqaXoaFG+9qj0t9Vu7FBMizDArj+pmFaQEd6I2OqfBfAibXrvuoFKeXX/K2yXtrl\n2qJhNq3kwXBDxn181z3nrUOsQd/eW68dyp4jb1MfAwEM8mlnCyLhDRM3EE+umS4b\ndZBRH5AQjPoaON7xZ46VMFovOR+asOUJXTptS/Eu1bLAI7PBp3+nm04dYTF9O50O\ndey1jmGoiBZ9wBkesvukg3dVZ7gxppDvz14+wekYEJqPfM0NZyxsC5dnoxg9pciF\ncFelhnTYlma1lXrCqjJcFdniHRwO0RE9CIKWe0g2HGo1uo2eq1XMxL9mE5t025im\nblMnhL06smrCdtXmb4jjtg==\n","auth_codeField":"",
"errmsgField":null,"typeField":"SUB","regDateField":"2016-06-03T08:18:41",
"startDateField":"5/29/2016","vm_capacityField":null,"uuidField":null,
"cpuidField":null,"mac_baseField":null,"mac_countField":null,"drrField":null,
"expirationField":"8/29/2016 12:00:00 AM","PropertyChanged":null} 
...<truncated> 

 The feature_Field in the response indicates the type of key that follows in the
 keyField. Copy each key to a text file and save it with the .key extension.
 Because the key is in json format, it does not have newlines. Make sure to
 convert it to newlines if your parser requires them. Make sure to name each key
 appropriately and save it to the /license folder of the bootstrap package. For
 example, include the authcode with the type of key to name it as
 I3306691_1pa-vm.key (for the capacity license key), I3306691_1threat.key (for
 the Threat Prevention license key), I3306691_1wildfire.key (for the WildFire
 subscription license key). 

 Sample API request for retrieving previously activated licenses using
 Curl: 

 curl -i -H "apikey:$APIKEY" --data-urlencode serialNumber=007200006142 https://api.paloaltonetworks.com/api/license/activate 

 Sample API response : 

 [{"lfidField":"13365773","partidField":"PAN-SVC-PREM-VM-300","featureField":
"Premium","feature_descField":"24 x 7 phone support; advanced replacement hardware service","keyField":"m4iZEL1t3n6Oa+6ll1L7itDZTphYw48N1AMOZXutDgExC5f5pOA52+Qg1jmAxanB\nKOyat4FJI4k2hWiBYz9cONuKoiaNOtAGhJvAuZmYgqAZejKueWrTzCuLrwxI/iEw\nkRGR3cYG+j6o84RitR937m2iOk2v9o8RSfLVilgX28nqmcO8LcAnTqbrRWdFtwVk\nluz47AUMXauuqwpMipouQYjk0ZL7fTHHslhyL7yFjCyxBoYXOt3JiqQ0OCDdBdDI\n91RkVPylEwTKgSXm3xpzbmC2ciUR5b235gyqdyW8eQXKvaThuR8YyHr1Pdw/lAjs\npyyIVFa6FufPacfB2RHApQ==\n","auth_codeField":"","errmsgField":null,
"typeField":"SUP","regDateField":"2016-06-03T08:18:41","startDateField":"5/29/2016",
"vm_capacityField":null,"uuidField":null,"cpuidField":null,"mac_baseField":null,
"mac_countField":null,"drrField":null, "expirationField":"8/29/2016 12:00:00 AM","PropertyChanged":null},{"lfidField":"13365774","partidField":"PAN-VM-300-TP",
"featureField":"Threat Prevention","feature_descField":
"Threat Prevention","keyField":
"NqaXoaFG+9qj0t9Vu7FBMizDArj+pmFaQEd6I2OqfBfAibXrvuoFKeXX/K2yXtrl\n2qJhNq3kwXBDxn181z3nrUOsQd/eW68dyp4jb1MfAwEM8mlnCyLhDRM3EE+umS4b\ndZBRH5AQjPoaON7xZ46VMFovOR+asOUJXTptS/Eu1bLAI7PBp3+nm04dYTF9O50O\ndey1jmGoiBZ9wBkesvukg3dVZ7gxppDvz14+wekYEJqPfM0NZyxsC5dnoxg9pciF\ncFelhnTYlma1lXrCqjJcFdniHRwO0RE9CIKWe0g2HGo1uo2eq1XMxL9mE5t025im\nblMnhL06smrCdtXmb4jjtg==\n","auth_codeField":"","errmsgField":null,"typeField":"SUB",
"regDateField":"2016-06-03T08:18:41","startDateField":"5/29/2016","vm_capacityField"
:null,"uuidField":null,"cpuidField":null,"mac_baseField":null,
"mac_countField":null,"drrField":null,"expirationField":"8/29/2016 12:00:00 AM","PropertyChanged":null}
...<truncated> 

 Deactivate Licenses 

 URL :
 https://api.paloaltonetworks.com/api/license/deactivate 

 Parameters : encryptedToken 

 To deactivate the license(s) on a firewall that does not have direct internet access,
 you must generate the license token file locally on the firewall and then use this
 token file in the API request. For details on generating the license token file, see
 Deactivate VM ,
 or Deactivate License (Software NGFW Credits) and Deactivate a Feature
 License or Subscription Using the CLI . 

 Header : apikey 

 Request :
 https://api.paloaltonetworks.com/api/license/deactivate?encryptedtoken@<token> 

 Sample API request for license deactivation using Curl : 

 curl -i -H "apikey:$APIKEY" --data-urlencode encryptedtoken@dact_lic.05022016.100036.tok https://api.paloaltonetworks.com/api/license/deactivate 

 Sample API response: 

 [{"serialNumField":"007200006150","featureNameField":"","issueDateField":"",
"successField":"Y","errorField":null,"isBundleField":null,"PropertyChanged":null},
{"serialNumField":"007200006150","featureNameField":"","issueDateField":"",
"successField":"Y","errorField":null,"isBundleField":null,"PropertyChanged":null},
{"serialNumField":"007200006150","featureNameField":"","issueDateField":"",
"successField":"Y","errorField":null,"isBundleField":null,"PropertyChanged":null},
{"serialNumField":"007200006150","featureNameField":"","issueDateField":"",
"successField":"Y","errorField":null,"isBundleField":null,"PropertyChanged":null},
{"serialNumField":"007200006150","featureNameField":"","issueDateField":"",
"successField":"Y","errorField":null,"isBundleField":null,"PropertyChanged":null},
{"serialNumField":"007200006150","featureNameField":"","issueDateField":"",
"successField":"Y","errorField":null,"isBundleField":null,
"PropertyChanged":null}]$ 

 Track License Usage 

 URL :
 https://api.paloaltonetworks.com/api/license/get 

 Parameters : authCode 

 Header : apikey 

 Request :
 https://api.paloaltonetworks.com/api/license/get?authCode=<authcode> 

 Sample API request for tracking license usage using Curl: 

 curl -i -H "apikey:$APIKEY" --data-urlencode authcode=I9875031 https://api.paloaltonetworks.com/api/license/get 

 Sample API response: 

 HTTP/1.1 200 OK 
Date: Thu, 05 May 2016 20:07:16 GMT 
Content-Length: 182 

{"AuthCode":"I9875031","UsedCount":4,"TotalVMCount":10,"UsedDeviceDetails":[{"UUID":"420006BD-113D-081B-F500-2E7811BE80C 
9","CPUID":"D7060200FFFBAB1F","SerialNumber":"007200006142"}]}..... 

 Previous 

 Manage the Licensing API Key 

 Next 

 What Happens When Licenses Expire? 

 On This Page 

 Activation and Onboarding 

 Strata Cloud Manager 

 Next-Generation Firewalls 

 Firewalls 

 PAN-OS 

 PAN-OS SD-WAN 

 VM-Series 

 Plugins 

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

 Shared Policy for NGFWs and Prisma Access 

 IPSec VPN 

 Security Policy 

 Quantum Security 

 Endpoints 

 GlobalProtect 

 Resources 

 All Release Notes 

 Compatibility Matrix 

 Experts Corner 

 Network Security 

 Activation & Onboarding 

 Licensing 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

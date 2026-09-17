---
url: https://cortex-docs.paloaltonetworks.com/xsoar-6-administrator-guide/6.12/onboard-cortex-xsoar/elasticsearch/elasticsearch-security/elasticsearch-security-guidelines-multi-tenant-deployments
fetched_at: 2026-09-16T08:57:18Z
source: cortex-platform
---

# Elasticsearch Security Guidelines - Multi-tenant Deployments | 6.12 (EoL) | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSOAR 6 

 Cortex XSOAR 6 Administrator Guides 

 6.12 (EoL) 

 Onboard Cortex XSOAR 

 Elasticsearch 

 Elasticsearch Security 

 Cortex XSOAR 6.12 EoL 

 Elasticsearch Security Guidelines - Multi-tenant Deployments 

 Secure multi-tenant Elasticsearch deployments in Cortex XSOAR 6.12. 

 We recommend that you implement these best practices to secure tenant accounts that use Elasticsearch indices. This is applicable for multi-tenant environments. 

 This feature allows for automatic user management in Elasticsearch for tenants, to ensure complete data segregation for multiple tenants in a single Elasticsearch cluster. 

 Note 

 If you instead use your own Elasticsearch credentials, we recommend disabling this feature to prevent any mismatches. 

 API Keys or Username, Role, and Password 

 API key 

 Due to Elasticsearch security limitations , we recommend using a username and password, rather than an Elasticsearch API key, for communication between Elasticsearch and Cortex XSOAR, in a multi-tenant deployment. 

 If you must use an API key, the main account and the host account(s) cannot create an API key with privileges to the tenants. You can force the creation of API keys for the tenants by setting " security.elasticsearch.apikey " to true . After setting to true , you have to manually add the index prefix to both the tenants and the host in the role_descriptors.indices.names section of the api_key . 

 Username, role, and password 

 When you create or restart a tenant account, Cortex XSOAR checks if the role and user for the tenant already exists (based on the tenant name). If the role and user don't exist, they are created. The user is created with a 32 character password that contains capital letters, lowercase letters, numbers, and special characters. 

 The password is then stored in the configuration file and encrypted using the route /encrypt/ . 

 Enable security features in Elasticsearch 

 In order to automatically generate unique credentials for each tenant account's index, in your elasticsearch.yml file, you need to add the following key: xpack.security.enabled: "true" . The elasticsearch.yml is the Elasticsearch service configuration file. It is not stored in the demisto folder and can exist in varied places. 

 If you do not enable XPack security, the tenant accounts will inherit the credentials of the main account. You can still create or restart a tenant account but will receive the following warning: 

 security (xpack) is not active. Will not set account user. Enable security by setting [xpack.security.enabled] to [true] in the elasticsearch.yml file and restart the node 

 Disable security features 

 If you enabled security features in Elasticsearch, you can create a server configuration in Cortex XSOAR that will override and disable the security features. 

 Go to Settings → About → Troubleshooting . 

 In the Server Configurations section click Add server configuration . 

 Security.elasticsearch.account: false 

 Previous Elasticsearch General Security Guidelines 

 Next Migration 

 Last updated 1 month ago 

 Was this helpful?

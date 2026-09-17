---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsoar-6-multi-tenant-guides/6.14/configure-multi-tenant/configure-the-multi-tenant-deployment/main-account-to-tenant-communication-encryption
fetched_at: 2026-09-16T08:58:04Z
source: cortex-platform
---

# Main Account to Tenant Communication Encryption | 6.14 | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSOAR 6 

 Cortex XSOAR 6 Multi-Tenant Guides 

 6.14 

 Configure Multi-Tenant 

 Configure the Multi-Tenant Deployment 

 Cortex XSOAR 6.14 Multi-Tenant 

 Main Account to Tenant Communication Encryption 

 Configure encrypted, two-way main-account and tenant communication in Cortex XSOAR 6.14 multi-tenant deployments. 

 In a multi-tenant deployment, communication is predominately from the main account to the host account, and then from the host to the tenants. However, when a host is first registered, communication is from the host account to the main account. 

 Two-way communication should always be available between the main account and tenant account so that replies can be sent from the tenant to the main. 

 The main host and additional hosts communicate using TLS 1.2 over port 443 (this is the default port, but can be configured). Requests to the tenants are sent through the hosts (main or other) on port 443. The hosts forward the requests to the tenant, which listens on ports 18501 and higher. 

 With a high availability deployment, port 443 is used for communication from : 

 Main account to high availability group hosts 

 High availability group hosts to the main account 

 High availability group hosts to other high availability group hosts in the same host group 

 Main account to tenants 

 Host to tenant communication is over port 1850x. 

 There is no communication between hosts in different high availability groups. 

 Encryption 

 By default, requests are encrypted using TLS using a Cortex XSOAR self-signed certificate. You can replace the certificate by creating your own certificate and private key. 

 Validation and authorization 

 Cortex XSOAR uses an internal API key so that the tenants or hosts can verify that the request originates from a main account and not from an unauthorized third party. An internal API key, kept on the main account, is used in all communications, and is passed to the tenants or host when they are created. The internal API key is passed to hosts on installer creation, and to tenants when they are created. 

 For requests that require authorization (such as when a user wants to view incidents from the main account) the user details are passed down in requests, so the tenant can decipher and query them. 

 Security 

 API keys are created by Cortex XSOAR. Requests are sent from an external source, which is received by Cortex XSOAR (usually a tenant) and interpreted as a request from an administrator. In multi-tenant environments, you need to consider where to create the API key. 

 If created on a main account, it will propagate to all tenants, so anyone with that key can send requests to any tenant in the environment. 

 If created on a tenant, you can only send requests to that tenant. 

 Previous Configure the Multi-Tenant Deployment 

 Next Add a Host 

 Last updated 2 months ago 

 Was this helpful?

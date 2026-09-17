---
url: https://cortex-docs.paloaltonetworks.com/xsoar-6-administrator-guide/6.12/reference-docs/reference/server-configurations/multi-tenant-server-configurations
fetched_at: 2026-09-16T08:57:51Z
source: cortex-platform
---

# Multi-Tenant Server Configurations | 6.12 (EoL) | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSOAR 6 

 Cortex XSOAR 6 Administrator Guides 

 6.12 (EoL) 

 Reference Docs 

 Reference 

 Server Configurations 

 Cortex XSOAR 6.12 EoL 

 Multi-Tenant Server Configurations 

 Reference multi-tenant server configurations in Cortex XSOAR 6.12. 

 Key 

 Description 

 Default 

 accounts.http.proxy 

 Whether to prevent communication from main account to tenants from going through proxy. For more information, see Configure Proxy Settings . 

 false 

 accounts.http.timeout 

 The amount of time after which the HTTP request times out (in seconds). The default value is 30. You can configure the HTTP request timeout from the main account and the timeout that you configure is applied to all tenant accounts. If you add the server configuration on tenants, it will be ignored. 

 30 

 accounts.http.websocket.proxy 

 Whether to prevent the Main account from using proxy for websockets forwarding to tenants. For more information, see Configure Proxy Settings . 

 false 

 host.communication.port 

 Changes the port for the host to connect to the main account. 

 Value: Port name 

 N/a 

 host.insecure 

 Trusts any certificate (when host accounts exists). For more information, see Configure Security Settings for Multi-Tenant Deployments . 

 true 

 host.proxy 

 Whether the host can use a proxy to connect to the main account. For more information, see Configure Proxy Settings 

 true 

 host.timeout.move 

 host.header.timeout.move 

 The amount of time which the host times out (in seconds). For more information, see Configure the Account Timeout . 

 60 

 security.tenant.use.secret 

 Generates a unique cookie session for the tenant account and main account. For more information, see Configure Security Settings for Multi-Tenant Deployments . 

 false 

 selective.propagation.enabled 

 Set to false to disable propagation labels . 

 true 

 server.config.forward.tenants 

 A comma-separated list of server configurations to forward to all tenants. For example, 

 server.config.1,server.config.2,server.config.3 

 For more information, see Forward Server Configurations to Tenant Accounts . 

 N/a 

 server.restrict.custom.locked.content.actions 

 Set to true to restrict actions for custom locked content items. For more information, see Restrict Actions for Custom Locked Content Items . 

 false 

 tenant.AcceptAnyCertificate 

 Validates the host certificate. Must be set to true if using a self signed certificate, or the main server cannot send requests to hosts. For more information, see Configure Security Settings for Multi-Tenant Deployments . 

 false 

 Previous Marketplace Server Configurations 

 Next Notification Server Configurations 

 Last updated 13 days ago 

 Was this helpful?

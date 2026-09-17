---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsoar-8-on-prem/8.12/install-cortex-xsoar/load-balancing-for-cortex-xsoar
fetched_at: 2026-09-16T08:53:51Z
source: cortex-platform
---

# Load balancing for Cortex XSOAR | 8.12 | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSOAR 8 

 Cortex XSOAR 8 On-prem Documentation 

 8.12 

 Install Cortex XSOAR 

 Cortex XSOAR 

 Load balancing for Cortex XSOAR 

 In Cortex XSOAR 8.12 On-prem, configure load balancing for reliable operation. 

 Load balancing keeps your systems running even if one of your components fails. It provides redundancy for the different components, so if a problem occurs, it has a minimal effect on your system. 

 Built-in load balancing 

 If you deploy a cluster of three nodes and set the Cortex XSOAR IP address access to either a virtual IP or the reverse proxy/ingress controller IP, the system implements built-in load balancing. This enables traffic distribution across the nodes and continuous operation if one node fails. 

 External load balancing 

 you can also use an external load balancer to integrate with your organization's existing network architecture or to leverage advanced traffic management and security features. 

 For specific load balancer configuration steps, see the documentation for your external load balancer, for example, F5 BIG-IP . 

 Important 

 When using an external load balancer, you need to configure sticky sessions (also known as session persistence) to ensure your session remains on a single server node throughout the session. This maintains application stability and proper functionality, and avoids operational issues including Single Sign-On (SSO) authentication failures where user requests may be inconsistently routed to different nodes within the cluster. 

 Recommended sticky session methods 

 There are two common ways to implement sticky sessions: cookie-based persistence and source IP persistence. The best choice depends on your specific network environment. 

 Cookie-based persistence 

 With cookie-based persistence, the load balancer inserts a unique cookie into a user's HTTP session. The load balancer then uses this cookie to ensure all subsequent requests from that user are consistently routed to the same server node. 

 This method is precise and reliable. It correctly identifies and maintains individual user sessions, even if multiple users are connecting from behind a single corporate firewall or proxy that makes them appear to have the same IP address. 

 Source IP persistence 

 With source IP persistence, the load balancer uses your source IP address to maintain session persistence, routing all requests from a single IP to the same server. 

 This method is typically the simplest to configure. However, you need to ensure that your users do not connect from behind a shared firewall or proxy (NAT). If multiple users share a source IP address, the load balancer will treat them as a single client and send them all to the same server, which can overload that server and defeat the purpose of load balancing. 

 Previous High Availability for Cortex XSOAR 

 Next System Requirements 

 Last updated 28 days ago 

 Was this helpful?

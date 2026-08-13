---
url: https://docs.paloaltonetworks.com/network-security/decryption/administration/decryption-overview/ssh-proxy
fetched_at: 2026-08-13T16:38:09Z
source: palo-alto-main
---

# SSH Proxy Clear

SSH Proxy 

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

 SSH Proxy 

 Updated on 

 Mar 13, 2026 

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

 Mar 13, 2026 

 Focus 

 Home 

 Network Security 

 Decryption Basics 

 SSH Proxy 

 Download PDF 

 Network Security 

 SSH Proxy 

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

 SSL Inbound Inspection 

 Next 

 TLS 1.3 Decryption 

 SSH Proxy 

 SSH Proxy enables decryption of inbound and outbound SSH sessions, preventing
 attackers from using SSH to tunnel potentially malicious applications and
 content. 

 Where Can I Use This? What Do I Need? 

 Prisma Access (Managed by Panorama) 

 NGFW (Managed by PAN-OS or Panorama) 

 No requirements. 

 In an SSH Proxy configuration, a Next-Generation Firewall (NGFW) sits between a client
 and a server. Configuring SSH Proxy enables
 an NGFW to decrypt inbound and outbound SSH connections, preventing
 attackers from using the SSH protocol to tunnel unwanted applications and content. SSH
 decryption does not require certificates. The NGFW automatically
 generates the key used for SSH connections when it boots up. During the boot-up process,
 the NGFW checks for an existing key. If there isn't one, the NGFW generates a key. The NGFW uses the key to decrypt SSH
 sessions for all virtual systems configured on it and all SSH v2 sessions. 

 SSH allows tunneling (or port forwarding), which is the transmission of data from a
 client to a server over an encrypted connection. Bad actors can use SSH tunneling to
 hide malicious traffic from decryption. The NGFW can't decrypt traffic
 inside an SSH tunnel. Instead, it identifies the presence of an SSH tunnel using App-ID and, depending on your Security policy
 rules, blocks all traffic in the tunnel. 

 SSH tunneling sessions can tunnel X11 Windows packets and TCP packets. A single SSH
 connection can contain multiple channels. When you apply a decryption profile for SSH
 Proxy to a Security policy rule that allows SSH traffic, the NGFW 
 determines the App-ID of the traffic in each channel to identify the channel type. The
 channel type can be: 

 session 

 X11 

 forwarded-tcpip 

 direct-tcpip 

 When the channel type is session, the NGFW identifies the traffic as
 allowed SSH traffic such as SFTP or SCP. When the channel type is X11, forwarded-tcpip,
 or direct-tcpip, the NGFW identifies the traffic as SSH tunneling traffic
 and blocks it. To block all traffic in an SSH tunnel, configure a Security policy rule for the
 ssh-tunnel application with the Action 
 set to Deny (along with a Security policy rule that allows
 traffic from the ssh application). 

 To reduce your attack surface, limit SSH use to administrators who need to manage network
 devices, log all SSH traffic, and consider enabling multi-factor authentication (MFA) to
 ensure that only legitimate users can use SSH to access devices. 

 When SSH decryption is enabled, authenticating to hosts with a certificate fails. This happens
 because the SSH client can no longer use public key authentication, preventing the
 server from completing the TLS handshake using a public key that the client decrypts
 with its private key. Use username and password authentication to initiate an SSH
 session instead. 

 For systems that must use key-based authentication, configure your SSH decryption policy rule to
 exclude systems that require public key authentication. To edit the decryption
 policy rule: 

 Go to Policies Decryption , and select the policy rule that controls SSH decryption. 

 Select the Destination tab. 

 Add the IP addresses of the systems you want to exclude from the
 rule. 

 Select Negate . 

 Click OK . 

 Commit your changes. 

 The following figure shows how SSH Proxy decryption works. 

 The client sends an SSH request to the server to initiate a session. 

 The NGFW intercepts the client’s SSH request. 

 The NGFW forwards the request to the server and initiates an SSH session with the
 server. This establishes the first of two separate sessions that the NGFW creates. Each session establishes a separate SSH tunnel. 

 The server responds to the request, which the NGFW intercepts. 

 The NGFW inserts the SSH key into the server’s response and forwards it to the
 client. This establishes the second separate session (and separate SSH tunnel)
 that the NGFW creates. 

 (First part of “7” in the diagram) After the NGFW establishes separate sessions
 with the server and the client, the NGFW acts as a proxy between
 them. 

 The NGFW checks the traffic between the client and server to see if it's routed
 normally or if it uses SSH port forwarding (SSH tunneling). If the NGFW identifies SSH port forwarding, the NGFW 
 blocks the tunneled traffic and restricts it according to the configured
 Security policy rule. The NGFW only looks for SSH port
 forwarding, it does not perform content and threat inspection on SSH
 tunnels. 

 When you configure SSH Proxy, the proxied traffic does not support DSCP code points
 or QoS. 

 Previous 

 SSL Inbound Inspection 

 Next 

 TLS 1.3 Decryption 

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

 Decryption 

 Network Security 

 PAN-OS 

 Next-Generation Firewall 

 Decryption 

 SSH Proxy 

 English 

 Strata Cloud Manager 

 © 2026 Palo Alto Networks, Inc. All rights reserved.

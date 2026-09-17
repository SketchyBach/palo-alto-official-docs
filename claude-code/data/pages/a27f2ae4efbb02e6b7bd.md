---
url: https://docs.paloaltonetworks.com/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/plan-the-cloud-identity-engine-deployment/configure-your-network-to-allow-cloud-identity-engine-traffic
fetched_at: 2026-09-16T07:55:12Z
source: idira-and-identity
---

# Configure Your Network to Allow Cloud Identity Agent Traffic Clear

Updated on 

 Thu Mar 12 10:18:33 PDT 2026 

 Focus 

 Home 

 Identity 

 Get Started with Cloud Identity Engine 

 Plan Your Cloud Identity Engine Deployment 

 Configure Your Network to Allow Cloud Identity Agent Traffic 

 Download PDF 

 Identity 

 Configure Your Network to Allow Cloud Identity Agent Traffic 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Identity Docs 

 Activation & Onboarding 

 Cloud Identity Engine 

 Help 

 Release Notes 

 New Features 

 Previous 

 Plan Your Cloud Identity Engine Deployment 

 Next 

 Configure Domains for the Cloud Identity Engine 

 Configure Your Network to Allow Cloud Identity Agent Traffic 

 Learn how to configure your network to allow traffic for the agent, your directory, and
 the Cloud Identity Engine. 

 Where Can I Use This? What Do I Need? 

 NGFW 

 Prisma Access 

 The Cloud Identity Engine service is free; however, the
 enforcement points utilizing directory data may require specific
 licenses. Click here for more
 information. 

 Depending on your network configuration and Cloud Identity Engine deployment type, allow the
 traffic for the agent (if you have an on-premises directory), your directory, and
 the Cloud Identity Engine. 

 Based on your region, allow traffic to the hostname for the region. To
 determine what region-based traffic to allow, refer to the table in Configure the Cloud Identity agent .

 Use the ssl App-ID in your Security policy (following
 our recommended Decryption Best Practices guidelines)
 to allow traffic to the Cloud Identity Engine. 

 If you have deployed a Palo Alto Networks firewall
between the agent and the Cloud Identity Engine: 

 The Cloud Identity agent version 1.7.0 and previous
 versions require direct reachability to the regional agent configuration
 endpoint and don't support proxy servers between the agent and the endpoint.
 If your network configuration uses a proxy server, you must update the Cloud Identity agent to
 version 1.7.1 or later. 

 Use the paloalto-cloud-identity App-ID
to allow traffic from the Cloud Identity agent to the Cloud Identity
Engine. This App-ID requires the ssl and web-browsing application
signatures. 

 Allow Cloud Identity agent traffic from the specified ports to the following URLs. 
 http://crl.godaddy.com on port 80. 

 http://ocsp.godaddy.com on port 80. 

 https://certs.godaddy.com on port
 443. 

 If you’re using Secure Socket Layer (SSL) decryption on the firewall, exclude the traffic between
 the agent and the Cloud Identity Engine from SSL decryption to allow the
 mutual authentication between the agent and the service. 

 If you have deployed a Palo Alto Networks firewall between the
agent and the Active Directory: 
 Depending on which protocol you select when you configure the Cloud Identity agent ,
 use one of the following App-IDs to allow traffic from the Cloud Identity agent
 to your domain controllers. 
 If the agent uses the LDAP protocol, use the ldap 
 App-ID. 

 If the agent uses the LDAPS or LDAP with STARTTLS protocol, use the
 ssl App-ID. 

 If you're using a non-Palo Alto Networks firewall: 

 Allow LDAP or LDAPS traffic to the LDAP or LDAPS port from the Cloud
 Identity agent to your Active Directory or Domain Controller. 

 Allow HTTPS traffic from the Cloud Identity agent on port 443 to your
 Cloud Identity Engine destination URL. You need to allow traffic only
 for the region that you specify for your tenant and you need to allow
 traffic for multiple regions only if you have tenants in multiple
 regions. For the region-specific agent configurations, refer to Configure the Cloud Identity
 agent . 

 Allow traffic from the Cloud Identity agent from the specified ports to
 the following URLs. 
 http://crl.godaddy.com on port 80. 

 http://ocsp.godaddy.com on port 80. 

 https://certs.godaddy.com on port
 443. 

 Previous 

 Plan Your Cloud Identity Engine Deployment 

 Next 

 Configure Domains for the Cloud Identity Engine

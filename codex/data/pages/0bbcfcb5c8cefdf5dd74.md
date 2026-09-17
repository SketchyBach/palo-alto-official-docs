---
url: https://docs.paloaltonetworks.com/advanced-wildfire/wildfire-appliance/set-up-and-manage-a-wildfire-appliance/set-up-authentication-using-custom-certs-standalone-wildfire-appliance/wildfire-appliance-and-mutual-authentication
fetched_at: 2026-09-15T15:08:05Z
source: palo-alto-main
---

# WildFire Appliance Mutual SSL Authentication Clear

Updated on 

 Mon Mar 02 18:41:58 PST 2026 

 Focus 

 Home 

 Advanced WildFire Powered by Precision AI™ 

 Set Up and Manage a WildFire Appliance 

 Set Up Authentication Using a Custom
Certificate on a Standalone WildFire Appliance 

 WildFire Appliance Mutual SSL Authentication 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 Advanced WildFire Powered by Precision AI™ 

 WildFire Appliance Mutual SSL Authentication 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Advanced WildFire 

 Administration 

 Appliance 

 Previous 

 Set Up Authentication Using a Custom Certificate on a Standalone WildFire Appliance 

 Next 

 Configure Authentication with Custom Certificates on the WildFire Appliance 

 WildFire Appliance Mutual SSL Authentication 

 You need an SSL/TLS Service Profile, a server Certificate
Profile, and a client Certificate Profile to enable mutual authentication
using custom certificates between a WildFire appliance and firewalls
or Panorama. 

 Where Can I Use
This? What Do I Need? 

 WildFire Appliance 

 WildFire License 

 When a firewall or Panorama sends a sample to a WildFire appliance
for analysis, the firewall acts as the client and the WildFire appliance
acts as the server. To mutually authenticate, each device presents
a certificate to identify itself to the other device. 

 To deploy custom certificates for mutual authentication in your
deployment, you need: 

 SSL/TLS Service Profile —An SSL/TLS service profile defines
the security of the connections by referencing your custom certificate
and establishing the SSL/TLS protocol version the server device
uses to communicate with client devices. 

 Server Certificate and Profile —A WildFire appliance
requires a certificate and certificate profile to identify itself
to firewalls. You can deploy this certificate from
your enterprise public key infrastructure (PKI), purchase one from
a trusted third-party CA, or generate a self-signed certificate
locally. The server certificate must include the IP address or FQDN
of the WildFire appliance’s management interface in the certificate
common name (CN) or Subject Alt Name. The firewall matches the CN
or Subject Alt Name in the certificate the server presents against
the WildFire appliance’s IP address or FQDN to verify the WildFire
appliance’s identity. 

 Additionally, use the certificate profile
to define certificate revocation status
(OCSP/CRL) and the actions taken based on the revocation status. 

 Client Certificates and Profile —Each firewall requires
a client certificate and certificate profile . The
client device uses its certificate to identify itself to the server
device. You can deploy certificates from
your enterprise PKI using Simple Certificate Enrollment Protocol
(SCEP), purchase one from a trusted third-party CA, or generate
a self-signed certificate locally. 

 Custom certificates can
be unique to each client device or common across all devices. The
unique device certificates uses a hash of the serial number of the managed
device and CN. The server matches the CN or the subject alt name
against the configured serial numbers of the client devices. For
client certificate validation based on the CN to occur, the username
must be set to Subject common-name. 

 Previous 

 Set Up Authentication Using a Custom Certificate on a Standalone WildFire Appliance 

 Next 

 Configure Authentication with Custom Certificates on the WildFire Appliance

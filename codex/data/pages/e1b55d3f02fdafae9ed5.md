---
url: https://docs.paloaltonetworks.com/content/techdocs/en_US/pan-os/10-0/pan-os-admin/decryption/configure-ssl-inbound-inspection.html
fetched_at: 2026-09-16T10:42:15Z
source: palo-alto-main
---

# Configure SSL Inbound Inspection Clear

Updated on 

 Jul 22, 2025 

 Focus 

 Home 

 PAN-OS 

 Decryption 

 Configure SSL Inbound Inspection 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 Configure SSL Inbound Inspection 

 Table of Contents 

 Filter

 End-of-Life (EoL)

 Previous 

 Configure SSL Forward Proxy 

 Next 

 Configure SSH Proxy 

 Configure SSL Inbound Inspection 

 SSL Inbound Inspection decryption enables the firewall
to see potential threats in inbound encrypted traffic destined for
your servers and apply security protections against those threats. 

 Use SSL Inbound Inspection to
decrypt and inspect inbound SSL traffic destined for a network server
(you can perform SSL Inbound Inspection for any server if you load
the server certificate onto the firewall). With an SSL Inbound Inspection
Decryption policy enabled, the firewall decrypts all SSL traffic
identified by the policy to clear text traffic and inspects it.
The firewall blocks, restricts, or allows the traffic based on the
Decryption profile attached to the policy and the Security policy
that applies to the traffic, including any configured Antivirus,
Vulnerability Protection, Anti-Spyware, URL Filtering, and File
Blocking profiles. As a best practice, enable the firewall to forward decrypted SSL traffic for WildFire analysis and
signature generation. 

 Configuring SSL Inbound Inspection includes: 

 Installing the targeted server certificate on the firewall. 

 Creating an SSL Inbound Inspection Decryption policy rule. 

 Applying a Decryption profile to the policy rule. 

 When
you configure SSL Inbound Inspection, the proxied traffic does not
support DSCP code points or QoS. 

 SSL Inbound Inspection
does not support Authentication Portal redirect .
To use Authentication Portal redirect and decryption, you must use SSL Forward Proxy . 

 Ensure that the appropriate interfaces are configured
as either Tap, Virtual Wire, Layer 2, or Layer 3 interfaces. 

 You cannot use a Tap mode interface for SSL Inbound
Inspection if the negotiated ciphers include PFS key exchange algorithms
(DHE and ECDHE). 

 View configured interfaces on the Network Interfaces Ethernet tab. The Interface
Type column displays if an interface is configured to
be a Virtual Wire , Layer 2 ,
or Layer 3 interface. You can select an interface
to modify its configuration, including the interface type. 

 Ensure that the targeted server certificate is installed
on the firewall. 

 On the web interface, select Device Certificate Management Certificates Device Certificates to view
certificates installed on the firewall. 

 The key exchange
algorithms and TLS versions that your web server supports determine
how you should install the server certificate and key on the firewall. 

 We
recommend uploading a certificate chain (a
single file) to the firewall if your end-entity (leaf) certificate
is signed by one or more intermediate certificates and your
web server supports TLS 1.2 and PFS key exchange algorithms. Uploading
the chain avoids client-side server certificate authentication issues. You
should arrange the certificates in the file as follows: 

 End-entity
(leaf) certificate 

 Intermediate certificates (in issuing order) 

 ( Optional ) Root certificate 

 You
can upload the server certificate and private key alone to the firewall
in the following cases: 

 Your
web server supports only TLS 1.2 and the RSA key exchange
algorithm. 

 Your web server supports TLS 1.3 connections and the server’s
certificate chain (if the leaf certificate is signed by intermediate
certificates) is installed on the server. SSL Inbound Inspection discusses
each case in more detail. 

 To import the targeted
server certificate onto the firewall: 

 On the Device Certificates tab,
select Import . 

 Enter a descriptive Certificate Name . 

 Browse for and select the targeted server Certificate
File . 

 Click OK . 

 Create a Decryption policy rule to
define traffic for the firewall to decrypt and create a Decryption profile to
apply SSL controls to the traffic. 

 Although Decryption profiles are
optional, it is best to include a Decryption profile with each Decryption
policy rule to prevent weak, vulnerable protocols and algorithms
from allowing questionable traffic on your network. 

 Select Policies Decryption , Add or
modify an existing rule, and define the traffic to be decrypted. 

 Select Options and: 

 Set the Action to Decrypt matching
traffic. 

 Set the Type to SSL Inbound
Inspection . 

 Select the Certificate for the internal
server that is the destination of the inbound SSL traffic. 

 ( Optional but a best practice ) Configure or select
an existing Decryption Profile to block and
control various aspects of the decrypted traffic (for example, create
a Decryption profile to terminate sessions with unsupported algorithms
and unsupported cipher suites). 

 When
you configure the SSL Protocol Settings Decryption
Profile for SSL Inbound Inspection traffic, create separate
profiles for servers with different security capabilities. For example,
if one set of servers supports only RSA, the SSL Protocol Settings
only need to support RSA. However, the SSL Protocol Settings for
servers that support PFS should support PFS. Configure SSL Protocol
Settings for the highest level of security that the server supports,
but check performance to ensure that the firewall resources can
handle the higher processing load that higher security protocols
and algorithms require. 

 Click OK to save. 

 Enable the firewall to forward decrypted SSL traffic for WildFire analysis . 

 This option requires an active
WildFire license and is a WildFire best practice . 

 Commit the configuration. 

 Choose your next step... 

 Enable Users to Opt Out of SSL
Decryption . 

 Configure Decryption exclusions to
disable decryption for certain types of traffic. 

 Previous 

 Configure SSL Forward Proxy 

 Next 

 Configure SSH Proxy

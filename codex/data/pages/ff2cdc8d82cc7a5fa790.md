---
url: https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-admin/certificate-management/configure-an-ssltls-service-profile/configure-an-ssltls-service-profile-pan-os
fetched_at: 2026-09-16T07:38:33Z
source: palo-alto-main
---

# Configure an SSL/TLS Service Profile (PAN-OS & Panorama) Clear

Updated on 

 Mon Aug 31 04:46:16 PDT 2026 

 Focus 

 Home 

 Next-Generation Firewall 

 Certificate Management 

 Configure an SSL/TLS Service Profile 

 Configure an SSL/TLS Service Profile (PAN-OS & Panorama) 

 Download PDF 

 Next-Generation Firewall 

 Configure an SSL/TLS Service Profile (PAN-OS & Panorama) 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Next-Generation Firewall Docs 

 Getting Started 

 Administration 

 Networking 

 Quick Start 

 Reference 

 Incidents & Alerts 

 Release Notes 

 Select a Document 

 PAN-OS 12.2 

 PAN-OS 12.1 

 PAN-OS 11.2 

 PAN-OS 11.1 

 PAN-OS 11.0 (EoL) 

 PAN-OS 10.2 

 PAN-OS 10.1 (EoL) 

 PAN-OS 10.0 (EoL) 

 PAN-OS 9.1 (EoL) 

 PAN-OS 9.0 (EoL) 

 PAN-OS 8.1 (EoL) 

 Help 

 Select a Document 

 PAN-OS 12.2 

 PAN-OS 12.1 

 PAN-OS 11.2 

 PAN-OS 11.1 

 PAN-OS 10.2 

 PAN-OS 10.1 

 New Features 

 Configure an SSL/TLS Service Profile (PAN-OS & Panorama) 

 PAN-OS: Specify a certificate, TLS protocol versions, and ciphers that you want
 connections to various Palo Alto Networks services support. 

 For each desired service, generate or import a certificate on the firewall (see
 Obtain
 Certificates ). 

 Use only signed certificates, not CA certificates, in SSL/TLS service
 profiles. 

 Select Device Certificate Management SSL/TLS Service Profile , and then click Add . 

 Enter a Name for the profile. 

 If the firewall has more than one virtual system (vsys), select the
 Location (vsys or Shared )
 where the profile is available. 

 Select the Certificate you obtained in step one . 

 PQC certificates are not available for selection. 

 Under Protocol Settings , define the range of TLS
 versions the service can use. 

 TLSv1.3 support is limited to administrative access to management
 interfaces, GlobalProtect portals and gateways, and Authentication Portal.
 You can only attach SSL/TLS service profiles that allow TLSv1.3 to the
 settings for these services. 

 Administrative
 Access, GlobalProtect Portals and Gateways, and Authentication
 Portal: 

 Set the Min Version and Max
 Version to TLSv1.3 . 

 For Min Version , select the earliest allowed
 TLS version: TLSv1.0 ,
 TLSv1.1 , TLSv1.2 ,
 or TLSv1.3 . 

 For Max Version , select the latest allowed
 TLS version: TLSv1.0 ,
 TLSv1.1 , TLSv1.2 ,
 or TLSv1.3 . 

 All Other Services: 

 Set the Min Version and Max
 Version to TLSv1.2 . 

 For the Min Version , select the earliest
 allowed TLS version: TLSv1.0 ,
 TLSv1.1 , or
 TLSv1.2 . 

 For the Max Version , select the latest
 allowed TLS version: TLSv1.0 ,
 TLSv1.1 , or
 TLSv1.2 . 

 ( Optional ) Configure Key Exchange Algorithms, Encryption Algorithms,
 and Authentication Algorithms. 

 Starting
 in PAN-OS 12.1.2, you can enable post-quantum key exchange algorithms for
 TLSv1.3 sessions. You must enable TLSv1.3 in the
 Protocol Settings. 

 To configure classical key exchange algorithms
 ( RSA , DHE , and
 ECDHE ): 

 By default, RSA ,
 DHE , and ECDHE are
 enabled. 

 ( PAN-OS 11.2 and earlier ) Enable or disable algorithms
 as needed. 

 ( PAN-OS 12.1.2 and later ) Select the
 Classical tab, and then enable or
 disable algorithms as needed. 

 ( PAN-OS 12.1.2 and later ) To specify PQC key exchange
 algorithms for TLSv1.3 sessions: 

 Select the Post-quantum Cryptography
 (PQC) tab, and then click
 Add . 

 For Algorithm , select
 ML-KEM (Module-Lattice-based Key
 Encapsulation Mechanism). 

 For each algorithm, select at least one Security
 Level : 

 Each security level corresponds to one of three ML-KEM
 parameter sets specified in FIPS 203 . Higher
 security levels offer greater protection but reduced
 performance. 

 Level 1 —ML-KEM-512 

 Level 3 —ML-KEM-768 

 Level 5 —ML-KEM-1024 

 For each algorithm, select one or more PQC
 Supported Groups . 

 The available curve groups change
 based on Algorithm and
 Security Level . You can generate
 session keys using post-quantum or hybrid post-quantum key
 exchange. Hybrid key exchange pairs Elliptic Curve
 Cryptography (ECC) with ML-KEM to protect against both
 classical and quantum threats. The following curves are
 supported for hybrid key agreement: x25519, x448, p256,
 p384, and p512. 

 Click OK and Commit your
 changes.

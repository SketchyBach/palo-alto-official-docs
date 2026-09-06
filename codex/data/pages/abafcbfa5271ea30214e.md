---
url: https://cortex-docs.paloaltonetworks.com/xsiam-data-model-schema/fields/network/tls/server-certificate
fetched_at: 2026-09-06T10:57:13Z
source: cortex-platform
---

# xdm.network.tls.server_certificate | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Schemas 

 XSIAM Data Model Schema 

 XDM Fields 

 xdm.network 

 xdm.network.tls 

 xdm.network.tls.server_certificate 

 The server certificate. 

 Datatype 

 Compound.ServerCertificate 

 Dataclass 

 Compound 

 Field groups 

 xdm.network.tls.server_certificate.subject_details 

 xdm.network.tls.server_certificate.issuer_details 

 Fields 

 xdm.network.tls.server_certificate.version 

 Description 

 The version of the server certificate. 

 Datatype 

 String 

 Dataclass 

 Scalar 

 xdm.network.tls.server_certificate.subject 

 Description 

 The subject of the server certificate. 

 Datatype 

 String 

 Dataclass 

 Scalar 

 xdm.network.tls.server_certificate.issuer 

 Description 

 The issuer of the server certificate. 

 Datatype 

 String 

 Dataclass 

 Scalar 

 xdm.network.tls.server_certificate.serial 

 Description 

 Unique identifier assigned to the certificate when it is issued. Used to distinguish the certificate from other certificates issued by the same certificate authority. The serial number is usually a positive integer encoded as an ASN.1 INTEGER value. 

 Datatype 

 String 

 Dataclass 

 Scalar 

 Examples 

 10:e6:fc:62:b7:41:8a:d5:00:5e:45:b6 

 xdm.network.tls.server_certificate.md5 

 Description 

 The MD5 hash of the server certificate. 

 Datatype 

 MD5 

 Dataclass 

 Scalar 

 xdm.network.tls.server_certificate.sha256 

 Description 

 The SHA256 hash of the server certificate. 

 Datatype 

 SHA256 

 Dataclass 

 Scalar 

 xdm.network.tls.server_certificate.sha1 

 Description 

 The SHA-1 hash of the server certificate. 

 Datatype 

 String 

 Dataclass 

 Scalar 

 xdm.network.tls.server_certificate.id 

 Description 

 The UUID hash of the server certificate 

 Datatype 

 String 

 Dataclass 

 Scalar 

 xdm.network.tls.server_certificate.not_before 

 Description 

 Indicates when the server certificate is first valid. 

 Datatype 

 UnixMillis 

 Dataclass 

 Scalar 

 xdm.network.tls.server_certificate.not_after 

 Description 

 Indicates when the server certificate is no longer valid. 

 Datatype 

 UnixMillis 

 Dataclass 

 Scalar 

 xdm.network.tls.server_certificate.algorithm 

 Description 

 The algorithm of the server certificate. 

 Datatype 

 String 

 Dataclass 

 Scalar 

 Examples 

 MD5withRSA, SHA1withRSA, SHA256withRSA, SHA256withECDSA 

 xdm.network.tls.server_certificate.public_key_bits 

 Description 

 The size of the certificate public key space in bits. 

 Datatype 

 Number 

 Dataclass 

 Scalar 

 Examples 

 2048 

 xdm.network.tls.server_certificate.formatted_issuer_org 

 Description 

 A formatted version of the certificate issuer organization. 

 Datatype 

 String 

 Dataclass 

 Scalar 

 Examples 

 DigiCert Inc, Acme Packet, Amazon 

 xdm.network.tls.server_certificate.classifications 

 Description 

 A set of cryptographic health checks performed for each certificate. 

 Datatype 

 String 

 Dataclass 

 Array 

 Examples 

 Expired, SelfSigned, ShortKey 

 xdm.network.tls.server_certificate.is_expired 

 Description 

 This field indicates whether or not the certificate has expired. 

 Datatype 

 Boolean 

 Dataclass 

 Scalar 

 Examples 

 True, False 

 xdm.network.tls.server_certificate.owner_type 

 Description 

 The type of object holding this cert. 

 Datatype 

 String 

 Dataclass 

 Scalar 

 Examples 

 User, Computer 

 xdm.network.tls.server_certificate.owner_name 

 Description 

 The name of object holding this cert. 

 Datatype 

 String 

 Dataclass 

 Scalar 

 Previous xdm.network.tls.client_certificate.issuer_details 

 Next xdm.network.tls.server_certificate.subject_details 

 Last updated 1 month ago 

 Was this helpful?

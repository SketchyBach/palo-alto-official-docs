---
url: https://docs.koi.ai/integration-guides/network/establishing-trust
fetched_at: 2026-09-06T10:20:38.530Z
source: koi-official-browser
capture_method: authenticated official browser
---

# Establishing Trust

For the complete documentation index, see llms.txt. This page is also available as Markdown.
Ask
DocumentationIntegration GuidesNetwork
Establishing Trust

Configure SSL certificate trust to enable Koi's traffic interception capabilities

This guide explains how to establish the necessary trust relationship between Koi's gateway and your organization's infrastructure. Proper trust configuration is essential for Koi to intercept and analyze SSL traffic from software marketplaces.

Why Trust Configuration is Required

Koi's gateway operates by intercepting SSL/TLS traffic between your users and software marketplaces (browser extension stores, package repositories, etc.). To accomplish this:

SSL Interception: Koi must terminate the original SSL connection and establish a new one with the marketplace on behalf of your users.

Certificate Validation: Your users' devices and security tools need to trust the certificates presented by Koi's gateway.

Seamless Operation: Without proper trust, users will see certificate warnings and connections will fail.

The trust relationship enables Koi to:

Inspect installation requests in real-time

Apply your organization's security policies

Block unauthorized software installations

Provide detailed visibility into software supply chain activity

Trust Establishment Methods

Choose the method that best fits your organization's certificate management practices and security requirements.

Method 1: Customer-Signed Certificate

 Koi chain of trust over PAC file

 Koi chain of trust over SWG

Overview: Koi provides a Certificate Signing Request (CSR) that you sign with your own organizational root CA.

How it works:

Koi generates and provides a CSR via your dedicated deployment portal

The CSR contains only the specific marketplace domains required for operation

You sign the CSR using your organizational root CA

You provide the signed certificate back to Koi

Koi's gateway uses your organization's signed certificate

Security Guarantee: The signed certificate is valid only for the marketplace domains specified in the CSR, providing cryptographic assurance that Koi cannot intercept traffic to any other domains.

Root CA Creation Support:
If your organization doesn't have a root CA, Koi can assist with:

Root CA creation and configuration

Distribution strategies for organizational devices

Best practices for certificate lifecycle management

Advantages:

Full Control: Your organization maintains complete certificate authority

Internal Trust: Uses your existing certificate trust infrastructure

Customization: Ability to set custom certificate properties and policies

Domain Restriction: Certificate is valid only for specified marketplace domains

Considerations:

Slightly More Setup: Requires one additional step of signing the CSR

Certificate Lifecycle: Your organization handles certificate renewals

PKI Requirements: Requires existing or new root CA (Koi can assist)

Best for: Organizations with strict certificate control requirements, direct device-to-Koi routing via PAC files, or those wanting cryptographic assurance that Koi can only intercept specified marketplace domains.

Method 2: Koi-Provided Root CA

Overview: Koi provides a pre-configured root Certificate Authority that you install in your existing security infrastructure.

How it works:

Koi provides you with a root CA certificate via your dedicated deployment portal

You install this root CA in your Secure Web Gateway (Zscaler, Forcepoint, etc.)

Your SWG establishes trust with Koi's gateway using the root CA

Traffic flows: Device ↔ SWG (existing trust) ↔ Koi Gateway (new trust)

Advantages:

Quick Setup: Fastest deployment option

Simplified Management: Koi handles all certificate lifecycle management

Pre-Configured: Root CA is optimized for Koi's specific use case

Considerations:

External Trust: Your organization trusts a Koi-managed root CA

Less Control: Limited ability to customize certificate properties

Dependency: Certificate management depends on Koi's infrastructure

Best for: Organizations with Secure Web Gateways (like Zscaler) that can control exactly which traffic is routed to Koi's gateway, making the additional domain-level certificate restrictions provided by the CSR method less necessary.

Choosing the Right Method
Factor
Customer-Signed
Koi Root CA

Setup Time

Minutes to Hours

Minutes

Management Overhead

Medium

Low

Organizational Control

Full

Limited

Certificate Lifecycle

Managed by Customer

Managed by Koi

Domain Restrictions

Built into Certificate

Controlled by SWG/PAC

PKI Infrastructure

Required or assisted setup

Not required

Implementation Support

Koi's technical team provides comprehensive support for both trust establishment methods:

Method 1: CSR generation, signing assistance, and PKI setup support

Method 2: Root CA delivery and SWG integration guidance

Hybrid Scenarios: Consultation for complex multi-environment deployments

Next Steps

Evaluate your organization's certificate management requirements

Choose the appropriate trust establishment method

Contact Koi Support to begin the trust configuration process

Follow the integration guide for your specific security infrastructure

Previous
Network
Next
Deploy Certificate Manually

Last updated 3 months ago

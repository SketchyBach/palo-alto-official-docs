<!-- KOI source: https://docs.koi.ai/integration-guides/network/establishing-trust.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/integration-guides/network/establishing-trust.md).

# Establishing Trust

This guide explains how to establish the necessary trust relationship between Koi's gateway and your organization's infrastructure. Proper trust configuration is **essential** for Koi to intercept and analyze SSL traffic from software marketplaces.

***

### **Why Trust Configuration is Required**

Koi's gateway operates by intercepting SSL/TLS traffic between your users and software marketplaces (browser extension stores, package repositories, etc.). To accomplish this:

1. **SSL Interception**: Koi must terminate the original SSL connection and establish a new one with the marketplace on behalf of your users.
2. **Certificate Validation**: Your users' devices and security tools need to trust the certificates presented by Koi's gateway.
3. **Seamless Operation**: Without proper trust, users will see certificate warnings and connections will fail.

**The trust relationship enables Koi to:**

* Inspect installation requests in real-time
* Apply your organization's security policies
* Block unauthorized software installations
* Provide detailed visibility into software supply chain activity

***

### **Trust Establishment Methods**

Choose the method that best fits your organization's certificate management practices and security requirements.

***

#### **Method 1: Customer-Signed Certificate**

![](https://files.readme.io/a2909bfe295cbbbad7ffb9b89cd6993ab1fea0604de064cf7bbd1017af9c7669-image.png) *Koi chain of trust over PAC file*

![](https://files.readme.io/8e2e5964eb4feed9a2f017c4343d0126c05b88bd8c435ad6eebc1135a262f633-image.png) *Koi chain of trust over SWG*

**Overview:** Koi provides a Certificate Signing Request (CSR) that you sign with your own organizational root CA.

**How it works:**

1. Koi generates and provides a CSR via your dedicated deployment portal
2. The CSR contains only the specific marketplace domains required for operation
3. You sign the CSR using your organizational root CA
4. You provide the signed certificate back to Koi
5. Koi's gateway uses your organization's signed certificate

**Security Guarantee:** The signed certificate is valid only for the marketplace domains specified in the CSR, providing cryptographic assurance that Koi cannot intercept traffic to any other domains.

**Root CA Creation Support:**\
If your organization doesn't have a root CA, Koi can assist with:

* Root CA creation and configuration
* Distribution strategies for organizational devices
* Best practices for certificate lifecycle management

**Advantages:**

* **Full Control**: Your organization maintains complete certificate authority
* **Internal Trust**: Uses your existing certificate trust infrastructure
* **Customization**: Ability to set custom certificate properties and policies
* **Domain Restriction**: Certificate is valid only for specified marketplace domains

**Considerations:**

* **Slightly More Setup**: Requires one additional step of signing the CSR
* **Certificate Lifecycle**: Your organization handles certificate renewals
* **PKI Requirements**: Requires existing or new root CA (Koi can assist)

**Best for:** Organizations with strict certificate control requirements, direct device-to-Koi routing via PAC files, or those wanting cryptographic assurance that Koi can only intercept specified marketplace domains.

***

#### **Method 2: Koi-Provided Root CA**

![](https://files.readme.io/6b9b113ddfb1b1d67d2851a3a0aaf797470519c2389ca03b1302f66c4806f6e0-image.png)

**Overview:** Koi provides a pre-configured root Certificate Authority that you install in your existing security infrastructure.

**How it works:**

1. Koi provides you with a root CA certificate via your dedicated deployment portal
2. You install this root CA in your Secure Web Gateway (Zscaler, Forcepoint, etc.)
3. Your SWG establishes trust with Koi's gateway using the root CA
4. Traffic flows: Device ↔ SWG (existing trust) ↔ Koi Gateway (new trust)

**Advantages:**

* **Quick Setup**: Fastest deployment option
* **Simplified Management**: Koi handles all certificate lifecycle management
* **Pre-Configured**: Root CA is optimized for Koi's specific use case

**Considerations:**

* **External Trust**: Your organization trusts a Koi-managed root CA
* **Less Control**: Limited ability to customize certificate properties
* **Dependency**: Certificate management depends on Koi's infrastructure

**Best for:** Organizations with Secure Web Gateways (like Zscaler) that can control exactly which traffic is routed to Koi's gateway, making the additional domain-level certificate restrictions provided by the CSR method less necessary.

***

### **Choosing the Right Method**

| Factor                     | Customer-Signed            | Koi Root CA           |
| -------------------------- | -------------------------- | --------------------- |
| **Setup Time**             | Minutes to Hours           | Minutes               |
| **Management Overhead**    | Medium                     | Low                   |
| **Organizational Control** | Full                       | Limited               |
| **Certificate Lifecycle**  | Managed by Customer        | Managed by Koi        |
| **Domain Restrictions**    | Built into Certificate     | Controlled by SWG/PAC |
| **PKI Infrastructure**     | Required or assisted setup | Not required          |

***

### **Implementation Support**

Koi's technical team provides comprehensive support for both trust establishment methods:

* **Method 1**: CSR generation, signing assistance, and PKI setup support
* **Method 2**: Root CA delivery and SWG integration guidance
* **Hybrid Scenarios**: Consultation for complex multi-environment deployments

***

### **Next Steps**

1. **Evaluate** your organization's certificate management requirements
2. **Choose** the appropriate trust establishment method
3. **Contact** Koi Support to begin the trust configuration process
4. **Follow** the integration guide for your specific security infrastructure


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/integration-guides/network/establishing-trust.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

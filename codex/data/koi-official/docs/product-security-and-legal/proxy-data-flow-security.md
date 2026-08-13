<!-- KOI source: https://docs.koi.ai/product-security-and-legal/proxy-data-flow-security.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/product-security-and-legal/proxy-data-flow-security.md).

# Proxy Data Flow & Security

### Introduction

Our Supply Chain Firewall is designed with strict limitations to ensure that **only marketplace-related data** flows through it, excluding any development activity, source code, or general web browsing.

This page explains how our proxy works, what data it processes, and why customers can trust that no sensitive or private information is inspected.

***

### How Our Proxy Works

Our proxy functions as a **Supply Chain Firewall**, streamlining and securing self-provisioned software. It is responsible for:

* **Inspecting extension-provisioning traffic** from marketplaces in IDEs, browsers, and similar platforms.
* **Enforcing policies** to allow, block, and control self-provisioned software.
* **Providing continuous visibility** into all installed self-provisioned software for security governance.

#### What Goes Through the Proxy

The proxy **only** processes marketplace-related traffic, specifically:

* **Search Requests** – When an end-user searches for items in the different marketplaces like IDE extension, Browser extensions etc...
* **Installations** – When an end-user installs an item from the marketplace.
* **Updates** – When an installed item checks for or downloads updates.

***

### Enforced Privacy by Design

Our system enforces these limitations through two primary mechanisms:

#### 1. Proxy Behavior in IDEs/Browsers is Limited By Design

* IDEs, such as Visual Studio Code, route **only** marketplace-related and IDE configuration traffic through the configured proxy. Read more ([https://code.visualstudio.com/docs/setup/network)\[here](https://code.visualstudio.com/docs/setup/network)].
* Other development-related communications (e.g., code commits, debugging, API calls) **bypass our proxy entirely**, as these operations do not respect the IDE-configured proxy settings.

#### 2. Controlled Scope via CSR (Certificate Signing Request)

* Our proxy operates with a **CSR configuration that restricts inspection to marketplace domains only**.
* We **cannot** inspect or decrypt any data outside of the specific marketplace URLs specified in the CSR that is signed by and controlled by the customer.
* Customers have full control over this configuration, ensuring transparency and trust.

***

### Security & Compliance Considerations

* **No Storage of Sensitive Data** – We do not log, retain, or analyze any personal or development-related data.
* **End-to-End Encryption** – The proxy respects TLS encryption and does not tamper with secure connections beyond the allowed marketplace scope.
* **Customer-Controlled Configuration** – Customers can audit, modify, or disable the proxy integration at any time.

***

### Data Collected and Transmitted

The following outlines the types of data collected by the Koi platform and sent from the customer’s environment to our SaaS:

* **Extension Inventory:** A list of all installed extensions per endpoint.
* **Extension ID:** Unique identifier for the VSCode or IDE extension.
* **Extension Name:** The name of the searched extension in VSCode.
* **Version Information:** The current version of the extension is installed on the endpoint.
* **Machine/Hostname:** (Optional) Identifies the device where the extension is installed for reporting purposes.
* **OS Type:** (Optional) Identifies the device operating system.
* **Username:** (Optional) Identifies the logged-in username on the device where the extension is installed for reporting purposes.

***

### Summary

* **Our proxy only handles extension marketplace data** (search, install, update).
* **No development activity, source code, or browsing data is inspected**.
* **Limitations are enforced by IDE/Browser behavior and CSR configuration**.
* **Security and privacy are built into our architecture**, ensuring transparency and customer control.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/product-security-and-legal/proxy-data-flow-security.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

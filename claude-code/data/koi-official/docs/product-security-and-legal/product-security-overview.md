<!-- KOI source: https://docs.koi.ai/product-security-and-legal/product-security-overview.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/product-security-and-legal/product-security-overview.md).

# Overview

### **Introduction**

This security overview is intended to help our customers understand how data is handled within the Koi platform and the measures we take to safeguard your organization’s assets.

![](https://files.readme.io/b9a8f25b19af5c70ba58dfd566752beefb451b0310d9de7a94f9af465d45b170-Group-411-min.png.webp)

### **Platform Architecture and Data Flow**

Koi is a SaaS-based solution that integrates seamlessly with your organization's environment with our agent-less approach. The following sections explain the key components of our architecture, data flow, and security mechanisms that protect your data.

### **Solution Diagram**

Below is a high-level overview of the Koi platform and its interactions with customer environments:

**Solution Components**

1. **Endpoint (Client-Side)**: This is where packages, extensions, MCPs, or any other software is installed and used by employees that includes a marketplace.

   ![](https://files.readme.io/5ff38c4f8f36ffca3b73e34472dad6673359a890b83de5eafc2eb13fe2e25787-image.png)
2. **Koi API**: Our API, hosted in the cloud, facilitates the communication between your environment and our platform, submitting packages and extensions' data and receiving data back for control.
3. **Koi Platform**: The management console hosted in the cloud, responsible for continuous discovery and inventory, policy configuration, risk reports, etc.

#### **Data Flow**

1. Endpoint machines send item IDs and endpoint names to the **Koi API**.
2. The **API** communicates with the **Koi Platform**, where risk scores, items behavior analysis, and other security findings are calculated.
3. The **Koi** **Platform** provides risk analysis, policy outcomes, and alerts.
4. Any detection of policy that needs to be remediated is handled by the recurring MDM script or EDR integration that checks for policies that need to be enforced.

#### **Data Collected and Transmitted**

The following outlines the types of data collected by the Koi platform and sent from the customer’s environment to our SaaS:

* **Items Inventory**: A list of all installed items per endpoint.
  * **Item ID**: Unique identifier for the marketplace/registry/app store item
  * **Item name:** The name of the searched item in the marketplace/registry/app store
  * **Version Information**: The current version of the item is installed on the endpoint.
* **Machine/Hostname**: Identifies the device where the item is installed for reporting purposes.
  * **OS Type**: Identifies the device operating system.
  * **Username**: Identifies the logged-in username on the device where the item is installed for reporting purposes.

#### **Data Protection and Security Measures**

At Koi, we take security and privacy very seriously. Generally, no sensitive data is collected by the Koi platform; most extension information is public data, and the only identifiers that may be collected are the machine name and username. To ensure the data transmitted from your environment is protected at all stages, we employ the following security measures:

* **Data Encryption in Transit**: All communication between your environment and Koi’s cloud services is encrypted using TLS 1.2 or higher. This ensures that data remains secure during transmission over the internet.
* **Data Encryption at Rest**: All collected data, including extension metadata and security findings, is encrypted at rest using AES-256 to protect against unauthorized access.
* **Data Minimization**: We only collect the minimal data necessary to perform risk analysis and enforce policies, ensuring that no unnecessary information is stored.
* **Audit Logging**: All interactions with the Koi platform are logged for audit purposes, including policy changes, extension installations, and security findings.
* **Isolation of Customer Data**: Data for each customer is logically isolated within the platform, ensuring that information from one organization is never shared with another.

Koi is committed to providing secure and comprehensive control over third-party items within your organization. Our secure architecture, strict data handling policies, and seamless integration with existing security systems ensure that your environments remain safe and productive. For additional questions or to request more information, please contact your Koi account representative.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/product-security-and-legal/product-security-overview.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

<!-- KOI source: https://docs.koi.ai/guides/protect-applications-with-koi/software-inventory-preview.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/guides/protect-applications-with-koi/software-inventory-preview.md).

# Applications - Discovery

The Koi Applications Inventory provides organizations with full visibility into applications installed across their endpoints.

This view includes details such as application name, version, publisher, OS platform, number of devices where the application was observed, and first and last seen timestamps.

In addition to standard inventory details, Koi enriches the data with application categories, so you can quickly understand what types of apps are in use across your environment, for example gaming apps or screen recording tools.

<figure><img src="/files/5yzrNnkrQfIvoHF4TqC6" alt=""><figcaption></figcaption></figure>

Use the Query Builder to filter, group, and explore the inventory data based on your needs.

***

## **What is the Applications Inventory?**

The Applications Inventory is a view into all known applications across endpoints in your organization. It helps:

* Understand what applications are in use across the organization
* Identify applications that don’t meet organizational policy (for example, gaming apps)
* Monitor how widely an application is deployed across org devices

***

## Coverage

Applications Inventory collects **installed applications** across macOS and Windows endpoints.

The inventory focuses on applications, it does not include every binary and process that may exist on a device, such as drivers, background services, CLI tools, or portable apps.

### **Inventory table fields**

| Field                               | Description                                                                                                                                                                                                                                                                          |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Name**                            | Human-readable name of the application                                                                                                                                                                                                                                               |
| **Version**                         | The application version                                                                                                                                                                                                                                                              |
| **Publisher**                       | Vendor of this application                                                                                                                                                                                                                                                           |
| **Platform**                        | OS platform (macOS or Windows)                                                                                                                                                                                                                                                       |
| **Endpoints**                       | Number of unique devices where the application was observed                                                                                                                                                                                                                          |
| **Categories**                      | The type of application (for example Security tools, Productivity, or Gaming)                                                                                                                                                                                                        |
| **Last seen**                       | Most recent time Koi observed this application in the organization                                                                                                                                                                                                                   |
| **First seen**                      | The first time Koi observed this application on any endpoint                                                                                                                                                                                                                         |
| **Last used**                       | Last time a user in the org executed this application                                                                                                                                                                                                                                |
| **Is Signed**                       | Indicates whether the application’s binary is code-signed and the signature validation succeeded. Values: True, False.                                                                                                                                                               |
| **Certificate Expiration Status**   | Status of the signing certificate based on its validity dates. Values: Valid, Expiring soon (60 days or less), Expired, Not yet valid (start date is in the future).                                                                                                                 |
| **Certificate Expiration Date**     | The signing certificate valid-until date, the date after which the certificate is no longer valid.                                                                                                                                                                                   |
| **Key Size**                        | Public key length of the signing certificate, in bits, for example 2048-bit.                                                                                                                                                                                                         |
| **Certificate Issuer**              | The Certificate Authority (CA) that issued the signing certificate, used to validate the trust chain.                                                                                                                                                                                |
| **Certificate Signature Algorithm** | The algorithm used to sign the certificate, for example SHA256\_RSA, SHA1\_RSA, MD5\_RSA.                                                                                                                                                                                            |
| **Signing Certificate Hash**        | Hash of the signing certificate (thumbprint).                                                                                                                                                                                                                                        |
| **SHA256**                          | Cryptographic hash of the binary file, uniquely identifies a specific build or version of the app.                                                                                                                                                                                   |
| **Team ID**                         | <p>Apple Developer Team identifier, a stable publisher identifier on macOS, shared across apps signed by the same developer account.<br><br>For example: <br>Team ID (Google Chrome) = <code>EQHXZ8M8AV</code><br></p>                                                               |
| **Signing ID**                      | <p>macOS code signing identifier for the application, formatted as <code>\<Team ID>:\<App Identifier></code>, used to group all versions of the same app under the same publisher.<br><br>For example: <br>Signing ID (Google Chrome)= <code>EQHXZ8M8AV:com.google.Chrome</code></p> |

***

## **Why does this matter?**

Modern organizations face application sprawl. Applications are installed through many locations, users download different applications independently, teams adopt new apps quickly, and older applications often remain deployed long after they are no longer needed.

Without a reliable applications inventory, security and IT teams can’t confidently answer basic questions such as: which applications exist in the environment, on which devices applications are installed, and which apps are risky or out of policy.

The applications inventory is the foundation for scalable app governance. It enables teams to reduce the attack surface by identifying outdated or vulnerable applications, detecting unauthorized or unwanted apps (for example, gaming applications or screen recording tools), and taking action across thousands of devices without manual investigation per endpoint.

***

## Example use cases & queries

**License management and cost optimization**\
Some applications change their licensing model based on usage scale.\
For example, tools like **Anaconda** become paid once they are installed on more than a certain number of devices.

Using the Applications Inventory, teams can:

* Filter by application name (for example, “Anaconda”)
* Group or filter by number of endpoints
* Identify applications that exceed licensing thresholds (for example, more than 200 endpoints)

This enables proactive license management, cost control, and informed conversations with procurement and legal teams.

<figure><img src="/files/uOKVExbF4DkCVY1jKO8n" alt=""><figcaption></figcaption></figure>

**Identify unused or rarely used applications**\
Applications that are installed but no longer actively used increase attack surface and operational noise.

Using the **Last used** field, teams can:

* Find applications that haven’t been used in the last 30, 60, or 90 days
* Identify candidates for removal or cleanup
* Reduce exposure to outdated or unnecessary software

<figure><img src="/files/hrCqX0ZyS79kBpwZ8xXl" alt=""><figcaption></figcaption></figure>

**Governance of remote management and access tools (RMM / Remote Access)**\
Remote access and remote management tools can pose elevated risk if not tightly governed. Different teams across the organization may adopt different tools, which can lead to the use of remote access software that is not approved by organizational policy.

Using application publisher data, teams can:

* Identify remote access or RMM tools used across the environment
* Understand how widely they are being used and on which devices
* Detect tools that are not approved

**High-risk or out-of-policy software detection**\
By combining publisher information and deployment scale, teams can:

* Identify gaming, screen recording, or file-sharing tools
* Detect software that violates organizational policy
* Prioritize remediation based on prevalence and risk

**Certificate hygiene**\
Certificates with weak properties can increase risk and reduce trust in signed applications across the organization. By using certificate fields in the Applications Inventory, teams can:

* Identify applications signed with weak signature algorithms (SHA-1, MD5)
* Identify applications using short key sizes (below 2048 bits)
* Prioritize review and remediation for applications with potentially less secure signing

**Detect unusual signing or issuer for a known application**\
Attackers and repackaged software can mimic legitimate apps but use a different signing identity or certificate.\
Using signing and certificate identifiers, teams can:

* Identify versions of the same application with a different Team ID or Signing ID
* Find outlier binaries with a different Signing Certificate Hash than expected
* Review applications signed by uncommon or unknown issuers
* Identify applications issued by internal or enterprise CAs

**Prepare for certificate expiration and reduce disruptions**\
When signing certificates expire, future updates or execution may fail validation depending on enforcement, which can cause operational disruption.\
Using Certificate Expiration Date and Certificate Expiration Status, teams can:

* Detect applications with certificates that are Expired or Expiring soon (60 days or less)
* Proactively coordinate with IT or vendors before certificates expire
* Reduce incidents caused by expired signing certificates

***

## **Key benefits**

* **Full visibility**

  See what software exists across macOS and Windows endpoints.
* **Reduce attack surface**

  Find outdated, unused, unwanted, or high-risk software.
* **Policy enforcement across the fleet (Coming soon)**

  Identify out-of-policy applications (for example, gaming, unapproved remote access tools), and enforce organizational policies consistently.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/guides/protect-applications-with-koi/software-inventory-preview.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

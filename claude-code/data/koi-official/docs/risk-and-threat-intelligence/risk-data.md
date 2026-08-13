<!-- KOI source: https://docs.koi.ai/risk-and-threat-intelligence/risk-data.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/risk-and-threat-intelligence/risk-data.md).

# Risk Data

## **Item’s Overview**

This section presents installation and activity signals as reported by the Marketplace. It reflects Marketplace sourced visibility into how the item is distributed and used, including its installation method, overall install footprint, and recent activity.&#x20;

![](https://files.readme.io/2f8bc42c9e6215f26bbf303ab569d5dea2bbe082a0a990dcf6cd6d9f7a839013-Screenshot_2025-12-25_at_9.31.00.png)

![](https://files.readme.io/b5b5933a9c0452e4b470cc444fb59d9a3487cdac32843052f34b715cf13a07f8-Screenshot_2025-12-25_at_9.34.35.png)

## Risk Data

#### Permissions

This section surfaces the permissions requested by the extension and classifies them by risk level to help assess scope and potential impact. It enumerates both API permissions and host permissions, making explicit what the extension is allowed to access or modify. Permissions are a key security signal because broader or higher-risk permissions can increase the blast radius of misuse whether intentional or through compromise and should be reviewed as part of trust, data exposure, and least-privilege assessments.

#### API Calls

This section provides an overview of the operating system (OS) API calls monitored by Koi to detect and mitigate potential risks posed by non binary software. Monitoring OS-level API interactions offers critical visibility into how non binary software access and manipulate system-level resources, ensuring a secure and compliant software ecosystem.

#### External communication

This section surfaces Marketplace-detected indicators of external communication within the item’s code. It enumerates external domains and URLs referenced by the extension, along with their code locations. The presence of external endpoints, such as github.com, indicates potential outbound communication or dependency on third-party services, which should be reviewed as part of trust, data exposure, and supply-chain risk assessments.

#### Secrets

This section outlines the various types of secrets that Koi can identify and monitor within non binary software across supported marketplaces.

Secrets are sensitive information that, if exposed, can lead to significant security risks such as unauthorized access, data breaches, or malicious activities. By tracking these secret types, Koi helps organizations maintain compliance, enforce security policies, and minimize third-party risks.

#### **Vulnerabilities**

This section surfaces security vulnerabilities in the item’s codebase and its dependencies. It highlights known Critical and High severity issues in third-party packages used by the item, with links to public advisories from OSV and the NVD. The presence of vulnerable dependencies indicates potential supply-chain risk and should be reviewed as part of overall security, trust, and maintenance assessments.

#### Code analysis

This section provides a consolidated, human-readable summary of the item’s code behavior as analyzed by the Koi Risk Engine. It explains the extension’s intended purpose, core architectural patterns, and runtime behaviors, and highlights operations that may be security relevant (such as process execution or file system access). By distinguishing standard, expected behaviors from potentially sensitive operations this section helps reviewers quickly assess whether the code’s behavior aligns with its stated functionality and whether it introduces elevated security or abuse risk.

![](https://files.readme.io/12c8e879d142f9101692909a16431f26bc2c0bfc3f8ddcbdc4f6be5c515bb97a-Screenshot_2025-12-25_at_9.38.21.png)

## Item’s data

#### Dependencies

This section lists third-party libraries the item depends on. It includes each dependency’s name, version, source repository, and license. These dependencies represent the item’s software supply chain and should be reviewed for security posture, license compatibility, and maintenance risk.

#### Repositories

This section provides repository-level metadata used to assess the provenance, ownership, and maintenance risk of the item’s source code. It surfaces signals such as repository ownership and type, primary language, license, activity timestamp, and community engagement indicators (stars, watchers, subscribers). These attributes help evaluate trust in the code’s origin, the health and responsiveness of its maintainers, and the likelihood of ongoing support or unresolved risk, independent of Marketplace-supplied information.

#### License and compliance

This section surfaces compliance signals and licensing terms identified by the Koi’s Risk Engine to support legal, regulatory, and governance risk assessments. Compliance indicators highlight declared alignment with regulations or standards (such as data protection frameworks), helping assess potential regulatory exposure and policy fit. Licensing information defines the legal rights, obligations, and limitations associated with using, modifying, or redistributing the software. Together, these signals help identify regulatory gaps, legal constraints, and usage risks that may impact approval, deployment, or ongoing compliance, independent of Marketplace metadata.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/risk-and-threat-intelligence/risk-data.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

<!-- KOI source: https://docs.koi.ai/guides/protect-code-packages-with-koi/code-packages-discovery.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/guides/protect-code-packages-with-koi/code-packages-discovery.md).

# Code Packages - Discovery

Koi provides comprehensive visibility into code packages installed on your organization's endpoints, helping you spot risky packages before they escalate into security incidents.

### Supported marketplaces

Code Package Inventory supports discovery across the following package registries:

| Marketplace             | Description                                                   |
| ----------------------- | ------------------------------------------------------------- |
| **npm**                 | Node.js package registry - JavaScript and TypeScript packages |
| **PyPI**                | Python Package Index - Python packages and libraries          |
| **Maven** (coming soon) | Java package registry                                         |
| **NuGet** (coming soon) | .NET package registry                                         |
| **Go** (coming soon)    | Go module registry                                            |

#### Supported package managers:&#x20;

**NodeJS:**

| Package manager     | Discovery | Notes                                                                              |
| ------------------- | --------- | ---------------------------------------------------------------------------------- |
| npm                 | ✅         |                                                                                    |
| Yarn (v1 / Classic) | Partial   | Global installs only, or projects with `package-lock.json` (not `yarn.lock` only). |
| Yarn (v2+ PnP)      | :x:       |                                                                                    |
| pnpm                | :x:       |                                                                                    |
| npx                 | :x:       |                                                                                    |
| bun                 | :x:       |                                                                                    |

**Python:**

| Package manager | Discovery |
| --------------- | --------- |
| pip             | ✅         |
| poetry          | ✅         |
| pipenv          | ✅         |
| conda           | ✅         |
| uv              | :x:       |

### Code Package Inventory

The Code Package Inventory presents the code packages found by Koi across endpoints in your organization, helping you understand what's installed and the [risk](https://docs.koi.ai/risk-and-threat-intelligence/wings-kois-risk-engine) each package poses. This enables you to [respond immediately to malicious packages](/guides/protect-code-packages-with-koi/code-packages-remediation.md) while enforcing policies that prevent supply chain risks before they impact your organization.

Using Koi's query builder, you can explore your code package risk on your endpoints from multiple aspects, such as:

**Malicious indications:**

* `Findings has Malicious activity detected` - code packages that were flagged for malicious activitiy
* `Findings has Malicious dependency` - code packages with a malicious direct dependency&#x20;

**Code packages risk:**

* `Risk Level = High AND Findings has low install count` - code packages that are High risk and have a low number of installs.
* `Findings has Critical CVSS vulnerability AND contains binary executable` - code packages that include a Critical CVSS vulnerability and also contain a binary executable file.

**Compliance risk:**

* `License is GPL 3.0 OR License is GPL 2.0 OR License is AGPL` - code packages licensed under GPL2, GPL3, or AGPL, which commonly cause potential license terms violations.

#### Inventory table fields

<table><thead><tr><th width="261.69921875">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Name</strong></td><td>The name of the package (e.g., <code>lodash</code>, <code>requests</code>)</td></tr><tr><td><strong>Risk Level</strong></td><td>Indicates the security risk of the package based on Koi's risk calculation function</td></tr><tr><td><strong>Governed by</strong></td><td>Shows which enforcement measure applies to this item: a policy, guardrail, or allow/block list.</td></tr><tr><td><strong>Version</strong></td><td>Installed package version</td></tr><tr><td><strong>Publisher</strong></td><td>Package maintainer or author name</td></tr><tr><td><strong>Marketplace</strong></td><td>Package registry source (npm, PyPI)</td></tr><tr><td><strong>Platforms</strong></td><td>The paclage manager the package was pulled from, e.g. npm, pip </td></tr><tr><td><strong>Endpoints</strong></td><td>Number of unique devices the package was observed on</td></tr><tr><td><strong>Categories</strong></td><td>Package categories or tags</td></tr><tr><td><strong>Installation method</strong></td><td>The installation method of the package</td></tr><tr><td><strong>Installs</strong></td><td>Installation count from marketplace (if available)</td></tr><tr><td><strong>Last Seen</strong></td><td>Most recent timestamp of activity</td></tr><tr><td><strong>First Seen</strong></td><td>First timestamp Koi observed this package on any endpoint in the organization</td></tr></tbody></table>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/guides/protect-code-packages-with-koi/code-packages-discovery.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

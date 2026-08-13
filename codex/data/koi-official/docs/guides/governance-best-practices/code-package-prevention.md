<!-- KOI source: https://docs.koi.ai/guides/governance-best-practices/code-package-prevention.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/guides/governance-best-practices/code-package-prevention.md).

# Code package prevention

Koi supports policy-based prevention and governance of code packages, starting with **npm** and **PyPI**. This gives organizations the ability to control, monitor, and block untrusted code packages before they are installed, while also offering a **progressive prevention path** for more sensitive item types.

***

### npm package prevention

Koi supports blocking **npm** packages by defining policies scoped to the `Code packages` item type.

Once enabled, you can:

* Define global block list for specific packages
* Build policies using **package metadata**, such as:
  * Package name
  * Publisher
  * Version

These rules are enforced across endpoints, enabling you to block known malicious or undesired packages before they are installed.

#### Getting started

To enable npm package prevention:

1. Reach out to your Koi point of contact.
2. Koi will guide you through network routing configuration for your environment.
3. Once enabled, you can:
   * Create policies scoped to `Code packages`
   * Use metadata conditions to allow or block npm packages
   * Leverage alert-mode policies with end-user notifications for low-friction governance
   * Global **block** list for npm packages

#### Example: Blocked npm package installation

When a npm package is on the global block list, end-users attempting to install it will encounter an error message similar to the following:

![](https://files.readme.io/15671ca76edb0221e631ca7961004b088018a49a6603063ecf6128f587369e9b-image.png)

This error clearly indicates that the package cannot be installed because it is blocked by your organization's policy, with an option to request approval.

***

### PyPI package prevention (early access)

Koi also supports early access to prevention of **PyPI** packages for Python environments.

The current capabilities include:

* Global **block** list for PyPI packages
* Build policies using **package metadata**, such as:
  * Package name
  * Publisher
  * Version

These rules are enforced across endpoints, enabling you to block known malicious or undesired packages before they are installed.

#### Getting started

To enable PyPI package prevention:

1. Contact your Koi point of contact to activate this capability.
2. Koi will assist in routing setup and provide access to allow/block list configuration.
3. Once enabled, you can:
   1. Create policies scoped to `Code packages`
   2. Use metadata conditions to allow or block PyPI packages
   3. Define global block list for specific packages

#### Example: Blocked PyPI package installation

When a PyPI package is on the global block list, end-users attempting to install it will encounter an error message similar to the following:

![](https://files.readme.io/22a36b782118dfbc86c42a17f20041f0b92721218e7ca1132df098a39f3da845-image.png)

***

### Understanding dependency visibility and blocking

Koi enforces block policies during the installation flow, whether the package is being installed as a top level package or pulled in as a dependency. When the install process reaches a dependency that matches a block policy, the Koi proxy blocks the request and the installation fails.

In the inventory you can explore the top level packages installed in your environment. Their first-level dependencies appear inside the package’s details view, providing visibility into what each top level package relies on. You can also use the **has dependency** condition in the query builder to explore your inventory from that perspective and understand where specific dependencies exist across devices.

This model allows you to prevent new installs of packages that rely on blocked dependencies while maintaining clear visibility into your dependency graph.

***

### Progressive prevention with end-user notifications

To minimize disruption from high-impact items like **code packages**, Koi supports a progressive prevention approach. Instead of immediately blocking items, organizations can start by detecting violations and **notifying end users** directly.

This allows teams to educate users, offer context, and guide remediation steps — all without enforcing removal upfront.

🔗 [Learn how to configure end-user notifications](https://success.koi.security/docs/end-user-notifications#/)

***

### Summary: Governance modes for code packages

| Mode                 | Description                                                                |
| -------------------- | -------------------------------------------------------------------------- |
| Alert + Notify       | No enforcement. Detects and notifies end users about violating items.      |
| Allow/Block policies | Enforces organization-defined rules to explicitly permit or deny packages. |
| Global lists         | Static allow or block list enforcement for known package names.            |

> Start with visibility and progressive education, then move toward stricter enforcement as needed.

***

### Important notes

* To get started, see the [Network Integration Guide for Code Packages](https://success.koi.security/docs/network-integration-for-application-specific-trust-store#/).
* Required routing domains will be provided by Koi during onboarding.
* Risk-based conditions - coming soon.

***

Need help or want access to code package prevention? 📩 Contact your Koi representative and we’ll guide you through setup.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/guides/governance-best-practices/code-package-prevention.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

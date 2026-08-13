<!-- KOI source: https://docs.koi.ai/guides/protect-code-packages-with-koi/code-package-prevention.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/guides/protect-code-packages-with-koi/code-package-prevention.md).

# Code Packages - Governance

## Code package prevention

Koi supports policy-based prevention and governance of **code packages** for **npm** and **PyPI**. Control which packages can be installed on managed devices and block untrusted or risky packages at install time - so risks are stopped before they can become active threats in your environment.

***

### Supported registries

| Registry | Description                                                 |
| -------- | ----------------------------------------------------------- |
| **npm**  | Node.js packages pulled from the NPM registry               |
| **PyPI** | <p>Python packages Pulled from the </p><p>PyPi registry</p> |

#### Supported Package Managers

Koi supports prevention of policy-violating code packages for all nodeJS and Python package managers, as long as the Koi Proxy is configured. See [below](#setting-up-code-package-prevention) for more information.

***

### How it works

1. **Traffic routing** – Installation attempts to the registry (npm or PyPI) are routed through the Koi proxy on your organization's endpoints.
2. **Policy lookup** – For each package request, the proxy looks up the package in your Governance rules (block list, allow list, guardrails, and policies).
3. **Allow or block** – The proxy allows or blocks the request accordingly.
4. **Blocked installs** – A blocked request returns an error and the installation fails. For npm, the user can be shown an option to request approval.

***

#### Setting up code package prevention

You can block or allow **npm or PyPi** packages by defining policies scoped to the **Code packages** item type and by using a global block list.

{% hint style="info" %}
**Before you start: Koi Proxy required**

To block unwanted packages at install time, code package prevention relies on a network or registry proxy integration. Learn more:

* [How to set up the Koi network proxy integration](https://docs.koi.ai/integration-guides/code-packages)
* [How to set up the Koi registry integration](https://docs.koi.ai/integration-guides/code-packages#registry-approach)
  {% endhint %}

**Capabilities:** Once Koi prevention is enabled—via registry or network-based integrations, you can apply enforcement rules to control which code packages may be installed and proactively block potentially risky or unwanted code packages before they reach your managed endpoints.

**1. Policies**

* Create allow/block policies using full Wings analysis data & findings
* Alert-mode policies with end-user notifications

<figure><img src="/files/QwSz6UrOu86oWSvCopzu" alt=""><figcaption></figcaption></figure>

**2. Guardrails**

* **Malware protection**
* **Version update cooldown** – delay before newly published versions become available (configurable).
* **Delayed access**
* **Scan-first protection** *(coming soon)*

**3. Global allow/block lists**

* Globally allow or block specific packages

{% hint style="info" %}
**Understanding dependency visibility and blocking**

Koi enforces block policies during the installation flow - whether the package is being installed as a top-level package or pulled in as a dependency. When the install process reaches a dependency that matches a block policy, the Koi proxy blocks the request and the installation fails.

In the code packages inventory you can explore the top-level packages installed in your environment. Their first-level dependencies appear inside the package's details view, providing visibility into what each top-level package relies on. You can also use the **`has dependency`** condition in the query builder to explore your inventory from that perspective and understand where specific dependencies exist across devices.

This model allows you to prevent new installs of packages that rely on blocked dependencies while maintaining clear visibility into your dependency graph.
{% endhint %}

<figure><img src="/files/mFZ1TrHQ6uoyJoTPzZqf" alt=""><figcaption></figcaption></figure>

**Example: Blocked npm package installation**

When an npm package is matches a block policy, users attempting to install it see an error indicating the package is blocked by your organization's policy, with an option to request approval.

![](https://files.readme.io/15671ca76edb0221e631ca7961004b088018a49a6603063ecf6128f587369e9b-image.png)

**Example: Blocked PyPI package installation**

When a PyPI package is on the global block list or matches a block policy, users attempting to install it receive an error (e.g. the installer may show that the package is blocked).

![](https://files.readme.io/22a36b782118dfbc86c42a17f20041f0b92721218e7ca1132df098a39f3da845-image.png)

***

### Progressive prevention with end-user notifications

To reduce disruption from high-impact items like **code packages**, Koi supports a progressive prevention approach. Instead of blocking immediately, you can start by detecting violations and **notifying end users** directly.

This lets you educate users, provide context, and guide remediation steps before enforcing blocks.

🔗 [Learn how to configure end-user notifications](https://docs.koi.ai/guides/end-user-notifications)


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/guides/protect-code-packages-with-koi/code-package-prevention.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

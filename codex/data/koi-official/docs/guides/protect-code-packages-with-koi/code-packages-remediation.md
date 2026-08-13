<!-- KOI source: https://docs.koi.ai/guides/protect-code-packages-with-koi/code-packages-remediation.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/guides/protect-code-packages-with-koi/code-packages-remediation.md).

# Code Packages - Remediation (Preview)

### Background

With the rise of the Agentic Endpoint, your enterprise devices can now install software autonomously. Agents running on your endpoints install code packages and libraries to complete tasks - which can introduce supply chain risks, as seen in the [**Shai Hulud**](https://www.koi.ai/incident/shai-hulud-npm-supply-chain-attack-crowdstrike-tinycolor) malicious NPM package campaign.

Koi's code package governance suite addresses this across the full agentic supply chain - from blocking installation to **removing critical-risk packages from the endpoint.**

### Code package remediation

Koi supports removing critical risk NPM packages from endpoints. Koi removes the package, clears caches, and blocks re-introduction of the package via the registry proxy - protecting your endpoints without manual intervention.

{% hint style="info" %}
**Why code packages are different**

Unlike other remediation types, removing code packages can break active development workflows. Removed packages that are utilized in running code may cause build failures, runtime errors, and broken developer environments.

Because of this high disruption risk, this solution is designed only for critical risk **code packages and is  manually-triggered only.** Remediation of lower-risk packages should be handled outside of Koi.
{% endhint %}

### Enable code package remediation

{% hint style="info" %}
**Recommended: Network- / Registry-based prevention:**

To ensure critical risk packages can't be reintroduced after removal, it is recommended to configure a network-based or registry-based proxy integration.

Learn more how to:&#x20;

* [Set up a Koi network integration](/integration-guides/code-packages.md)
* [Set up a Koi registry integration](/integration-guides/code-packages/registry-approach.md)
  {% endhint %}

To prevent critical risk packages from being reintroduced, remediation of code packages utilizes the Koi registry-based prevention.&#x20;

This feature is **opt-in** and disabled by default. To enable it:

1. Go to **Settings → Advanced**
2. Toggle on **Code package remediation**

<figure><img src="/files/sI9YLXpuSUUEmsMC4Tl8" alt=""><figcaption></figcaption></figure>

### How to remediate a package

1. Navigate to **Remediations → Open queue**
2. Select the critical risk package(s) you want to remove
3. Click **Remediate**
4. Review the confirmation popup showing:
   * Package name and version
   * Affected endpoints and instance count
   * The security finding
5. Click **Confirm** to proceed

***

### What happens during remediation

To remediate a critical risk code package, Koi performs these actions on each affected endpoint:

1. **Uninstalls the package**
2. **Clears package manager cache** to prevent reinstallation

{% hint style="warning" %}
**Important**

Remediating code packages is a highly disruptive action that can impact end-user workflows and cause confusion. We strongly recommend configuring end-user notifications before enabling code package remediation. These notifications will automatically alert affected developers when a package is removed, explaining the reason and who to contact - helping to prevent frustration and support issues.\
\
[Learn how to configure end-user notification](/guides/end-user-notifications.md)
{% endhint %}

{% hint style="danger" %}
**Information**

Koi reduces the risk of malware execution by detecting and removing critical risk packages from your endpoints. Our policies are built for prevention and cleanup - blocking critical risk packages before they're installed and removing them when detected.\
\
If you suspect a critical risk package was executed before removal, involve your Incident Response or security operations team.
{% endhint %}

### Best practices

1. **Review impact before confirming -** check how many endpoints will be affected
2. **Communicate with teams** when remediating packages in active projects
3. **Configure notifications** so developers understand what happened - setup guide
4. **Monitor the queue regularly** to stay ahead of threats


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/guides/protect-code-packages-with-koi/code-packages-remediation.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

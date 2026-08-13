<!-- KOI source: https://docs.koi.ai/risk-and-threat-intelligence/wings-kois-risk-engine.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/risk-and-threat-intelligence/wings-kois-risk-engine.md).

# Wings - Koi’s Risk Engine

## What is the Koi risk engine?

**Wings** is Koi's **AI-powered risk engine** designed to evaluate the **security posture of software supply chain items.** It provides continuous, automated analysis of non-binary software including IDE extensions, browser extensions, code packages, AI models, OS packages, AI artifacts for MCP servers and productivity tools extensions to detect threats ranging from malware and spyware to vulnerable dependencies, transfer of ownership, and suspicious publisher behavior.

***

## How it works?

The risk engine operates as an autonomous agent that orchestrates multiple specialized tools, including vulnerability scanners, secret detectors, sandbox environments, threat intelligence feeds, and AI-driven code comprehension.

These tools allow the engine to analyze both static structure and runtime behavior. AI-based code understanding enables detection of malicious intent even in novel or obfuscated code that bypasses traditional signature-based scanners.

The signals produced by these analyses are translated into scored security findings, which are aggregated to determine an overall risk level for each item and each version. Wings continuously re-evaluates items as new versions are released, dependencies change, or new intelligence becomes available, ensuring risk reflects the current security posture, not a historical snapshot.

<figure><img src="/files/ok2sHAZu3dfZ4FfEmOFA" alt=""><figcaption></figcaption></figure>

### Version-aware and continuous risk assessment

Wings evaluates risk at the item and version level, not just at the package or extension. Every time a new version of an item is published, Wings automatically analyzes that specific version and assigns it an independent risk assessment.

This is critical because **risk changes over time**:

* New versions may introduce malicious code, vulnerable dependencies, or risky behaviors
* Ownership transfers, compromised publishers, or new build pipelines can affect trust
* Previously safe items can become risky, and risky items can be fixed in later releases

As a result, an item is **never analyzed just once**. Wings evaluates risk per version, combining static and dynamic analysis, dependency and composition inspection, publisher and marketplace intelligence, sandboxed runtime behavior, vulnerability data, and continuously updated threat intelligence.

By tracking risk per item and per version, **Wings enables organizations to**:

* Detect risky updates immediately
* Enforce policies based on version risk, not just global item
* Prevent regressions when safe software becomes unsafe
* Make precise decisions without over-blocking productivity

***

## **Engine Tools**

The Agentic engine orchestrates multiple specialized tools to extract comprehensive security signals:

**AI Code Analysis**

Goes beyond pattern matching by using AI to read and reason about code. This enables detection of malicious intent in novel threats, zero-day attacks, and sophisticated obfuscation techniques that evade traditional signature-based scanners.

**Deep Composition Analysis**

Performs static code analysis including lifecycle hook inspection, malicious code pattern detection, dependency analysis, and de-obfuscation of intentionally obscured code.

**AI-Native Security Analysis**

For AI artifacts, Wings performs AI-native security analysis beyond traditional code inspection. Rather than only analyzing source code, Wings evaluates how each artifact is designed to operate, identifying risks unique to agentic software across four key dimensions:

* **Intent** – What is the artifact designed to accomplish, and does its implementation align with its stated purpose?
* **Expected Behavior** – What actions is the artifact intended to perform, including interactions with AI models, external services, and the local environment?
* **Capabilities** – What functionality does the artifact expose or enable, such as code execution, network communication, or access to sensitive resources?
* **Permissions** – What tools, resources, and data can the artifact access, and are those permissions appropriate for its intended function?

**Publisher Intelligence**

Gathers intelligence on item publishers including reputation history, account age, cross-marketplace presence, domain registration details, and association with known threat actors.

**Dynamic Behavior Analysis**

Executes items in isolated sandbox environments to observe runtime behavior including network communications, API calls, file system access, and data exfiltration attempts.

**Item Metadata Analysis**

Evaluates marketplace signals such as install counts, review authenticity, privacy policy completeness, GitHub repository health, version history, and download velocity patterns.

**Threat Intelligence Integration**

Correlates items against threat intelligence feeds to identify associations with known malicious campaigns, compromised domains, and emerging threat patterns.

***

## Security findings

Findings are the building blocks of our risk level. They are derived from the results of our static and dynamic analyses and the item’s marketplace listing details. Each finding is individually scored on a scale of 1 to 10, corresponding to a risk level of Low, Medium, High or Critical. These findings are aggregated to produce an overall risk level for the item.

Our research team constantly develops new security findings and detections to stay ahead of emerging threats. We continuously evolve our detection capabilities and provide up-to-date and thorough assessments of each item’s potential risk.

### **Finding Categories**

**Malicious Behaviour**\
Clear malicious intent or strong threat-intelligence confirmation. Items in this category are **actively malicious** or **strongly linked to real-world attacks**, coordinated campaigns, or confirmed abuse. These findings indicate high confidence that the item should not be trusted.

**Exploitation & Vulnerabilities**\
Technically exploitable weaknesses that attackers can leverage to gain unauthorized access, execute code, or intercept communications, **even if the item itself is not intentionally malicious**.

**Execution & Behavior**\
Dangerous runtime capabilities that are **frequently abused in attacks**, such as executing code, modifying system state, bypassing controls, or hiding behavior. These findings increase risk by expanding what an item can do if compromised or misused.

**Data Exposure & Privacy**\
Risk to secrets, sensitive data, or regulated information. Items in this category can **access, collect, or transmit data** that could expose users or organizations to privacy violations, account compromise, or data breaches.

**Publisher & Ownership Trust**\
Signals indicating that the **publisher, ownership, or source may not be trustworthy or stable**. These risks increase the likelihood of supply-chain attacks, malicious updates, or abandonment.

**Marketplace Signals**\
Indicators of **abandonment, manipulation, or instability** in how an item is distributed, maintained, or promoted. These findings don’t always indicate malicious activity, but they significantly increase long-term risk and reduce confidence.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/risk-and-threat-intelligence/wings-kois-risk-engine.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

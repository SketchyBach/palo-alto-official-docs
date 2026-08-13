<!-- KOI source: https://docs.koi.ai/risk-and-threat-intelligence/findings/index-3/vulnerable-to-prompt-injection.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/risk-and-threat-intelligence/findings/index-3/vulnerable-to-prompt-injection.md).

# Vulnerable to Prompt Injection

**Severity**

🔴 High (7)

**Short Description**\
Flags items that use Large Language Models (LLMs) in ways that allow external, untrusted, or user-controlled input to influence the model’s context, instructions, or decision-making. This exposure can enable prompt injection attacks that manipulate model behavior, bypass intended safeguards, or cause the model to invoke available tools or perform unintended actions, such as executing attacker-controlled instructions, leaking data, or producing misleading outputs - particularly when processing user content or integrating third-party or external data sources.

**Suggestion**

Review how the item integrates LLM functionality and whether untrusted input can reach the model's context. If proper input sanitization or context isolation is not implemented, consider removing the item to prevent exploitation.

**Information**

Prompt injection occurs when attackers craft input that alters an LLM's intended behavior by injecting instructions the model interprets as legitimate commands. This is particularly dangerous in items that process user-generated content, integrate external data, or grant the LLM access to tools and APIs. The risk is amplified when the LLM can access sensitive data or execute privileged actions.

**Risks of Vulnerable to Prompt Injection**

* **Instruction Hijacking**: Attackers override intended instructions, causing the LLM to follow malicious directives.
* **Data Exfiltration**: Injected prompts trick the model into revealing sensitive information from its context.
* **Tool Abuse**: If the LLM has tool access, injection can trigger unauthorized actions like sending data to attacker-controlled endpoints.
* **Safeguard Bypass**: Crafted injections can circumvent content filters and access controls.
* **Output Manipulation**: Attackers influence the model to produce misleading or fraudulent outputs.
* **Privilege Escalation**: In items where the LLM has elevated permissions, injection can perform unauthorized high-privilege actions.

**Recommended Actions**

* **Investigate the Item**:
  * Identify where LLM functionality is used and what inputs reach the model's context.
  * Determine whether untrusted or external data can influence prompts.
  * Review any tools or APIs the LLM can invoke.
* **Immediate Action**:
  * Remove or disable the item if it lacks adequate defenses and handles sensitive data.
  * Restrict the LLM's access to tools and privileged operations.
* **Mitigation**:
  * Implement input filtering and context boundaries between trusted instructions and untrusted content.
  * Apply output validation before actions are triggered.
  * Monitor for unusual model behavior or unexpected tool invocations.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/risk-and-threat-intelligence/findings/index-3/vulnerable-to-prompt-injection.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

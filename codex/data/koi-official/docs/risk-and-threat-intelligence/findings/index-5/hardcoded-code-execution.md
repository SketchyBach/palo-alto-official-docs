<!-- KOI source: https://docs.koi.ai/risk-and-threat-intelligence/findings/index-5/hardcoded-code-execution.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/risk-and-threat-intelligence/findings/index-5/hardcoded-code-execution.md).

# Hardcoded Code Execution

**Severity**\
🔵 Low (3)

**Short Description**\
Flags MCP servers whose tool handlers execute shell commands or code that is defined in the package’s own source (fixed strings, built-in scripts, or static code paths), rather than being assembled from LLM output or untrusted runtime input. This indicates real execution on the host; risk depends on *what* runs (see evidence).

**Suggestion**\
Treat this as a review signal, not automatic malice. Use the evidence to decide whether execution is expected (e.g. documented tooling) or unsafe (destructive commands, broad system access). Remove or replace the MCP if the behavior is unnecessary or unacceptable for your environment.

**Information**\
Hardcoded code execution means the MCP’s source code contains paths that can invoke operating-system commands, child processes, `eval`/dynamic code, or similar APIs, with the payload defined in the repository (fixed strings, static helpers, or developer-written logic)—not assembled from LLM output at runtime. Whether that path actually runs depends on usage: which tools get called, configuration, branches taken, and normal operation of the server. The concern is not prompt injection into the model, but trust and impact: when those paths do run, they execute with the MCP process’s privileges. The same pattern may be acceptable (documented automation) or risky (broad shell usage, destructive operations)—use the evidence to see what could execute and whether that fits your policy.

**Risks**

* Host impact: Fixed commands still run with the MCP server’s privileges and can modify files, call the network, or change system state.
* Blast radius: Poorly scoped scripts can damage data or configuration even without any LLM manipulation.
* Trust / supply chain: You must trust the publisher and every update; hardcoded execution increases the impact of a compromised or malicious package.
* Operational misuse: Legitimate automation can still violate policy (e.g. running installers, touching secrets paths) if not aligned with your standards.

**Recommended Actions**

* Read the evidence and map it to concrete APIs (e.g. `exec`, `spawn`, `subprocess`, shell helpers).
* Decide policy fit: Allow only if the fixed behavior is documented, scoped, and acceptable for your org.
* Prefer safer patterns: Replace broad shell usage with narrow, parameterized operations or APIs that do not invoke a shell.
* Least privilege: Run the MCP with minimal OS and network permissions; avoid running as an elevated account.
* Version and vendor review: Pin versions, review changelogs, and reassess after upgrades because hardcoded paths can change between releases.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/risk-and-threat-intelligence/findings/index-5/hardcoded-code-execution.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

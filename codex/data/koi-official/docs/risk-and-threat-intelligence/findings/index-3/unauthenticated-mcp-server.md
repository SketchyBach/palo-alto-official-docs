<!-- KOI source: https://docs.koi.ai/risk-and-threat-intelligence/findings/index-3/unauthenticated-mcp-server.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/risk-and-threat-intelligence/findings/index-3/unauthenticated-mcp-server.md).

# Unauthenticated MCP Server

**Severity**

🔵 Low (3)

**Short Description**

Flags MCP servers that either connect to a remote or upstream service without authentication, or remote MCP servers that can be connected to without authentication. Unauthenticated connections may expose data in transit, allow unauthorized tool invocation, or enable man-in-the-middle attacks.

**Suggestion**

Review the MCP's connection configuration and determine whether authentication can be added. Unauthenticated connections should be treated as untrusted.

**Information**

This finding covers two scenarios. First, an MCP server that connects to external services (APIs, databases, remote MCPs) without providing any authentication credentials — meaning data sent to and received from those services is not verified as coming from a trusted source. Second, a remote MCP server (typically SSE or HTTP-based) that accepts connections from any client without requiring authentication — meaning anyone who can reach the server can invoke its tools. In both cases, the lack of authentication creates opportunities for man-in-the-middle attacks, unauthorized access, and data interception.

**Risks**

* Man-in-the-Middle Attacks: Without authentication, an attacker can intercept and modify traffic between the MCP and its upstream services.
* Unauthorized Tool Invocation: An unauthenticated remote MCP server allows anyone on the network to call its tools.
* Data Exposure: Sensitive data passed to or from unauthenticated services can be intercepted or logged by intermediaries.
* Impersonation: Without authentication, the MCP cannot verify it is communicating with the intended service, enabling service impersonation.
* Credential Absence: The lack of authentication may indicate the upstream service has no access controls at all, broadening the exposure.

**Recommended Actions**

**Investigate the Item:**

* Review the MCP's connection configuration for upstream services — check for API keys, OAuth tokens, mTLS certificates, or other authentication mechanisms.
* For remote MCP servers, check whether the server requires any form of client authentication (API key, bearer token, mTLS).
* Determine whether the unauthenticated connection is intentional (e.g., public API) or an oversight.

**Immediate Action:**

* Add authentication credentials to upstream service connections where available.
* If the MCP itself is exposed remotely, configure authentication or restrict access to trusted clients.

**Mitigation:**

* Require all remote connections (both outbound and inbound) to use authenticated and encrypted channels.
* Implement mutual TLS (mTLS) for MCP-to-service communication where supported.
* Place unauthenticated remote MCP servers behind an authentication proxy or VPN.
* Regularly audit MCP connection configurations for missing credentials.

<br>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/risk-and-threat-intelligence/findings/index-3/unauthenticated-mcp-server.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

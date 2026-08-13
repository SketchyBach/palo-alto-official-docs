<!-- KOI source: https://docs.koi.ai/risk-and-threat-intelligence/findings/index-3/unrestricted-network-access.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/risk-and-threat-intelligence/findings/index-3/unrestricted-network-access.md).

# Unrestricted Network Access

**Severity**

🟡 Medium (4)

**Short Description**

Flags MCP servers that bind to 0.0.0.0 (all network interfaces), making the server accessible from any network. This increases the attack surface by exposing the server to untrusted networks.

**Suggestion**

Review whether binding to all interfaces is intentional. In most cases, MCP servers should only bind to localhost (127.0.0.1) to limit access to the local machine.

**Information**

When an MCP server binds to 0.0.0.0, it listens on every network interface — including Wi-Fi, Ethernet, VPN, and any bridged or virtual interfaces. This means any device on any connected network can reach the MCP server, not just processes on the local machine. For MCP servers that expose powerful tools (file system access, command execution, database queries), this turns a local development tool into a network-accessible service with no built-in access controls.

**Risks**

* Unauthorized Remote Access: Any device on the same network can connect to and invoke the MCP server's tools.
* Lateral Movement: An attacker on the network can use the exposed MCP server as a pivot point to access local resources.
* Data Exfiltration: Sensitive data accessible through the MCP's tools becomes reachable from remote hosts.
* Public Exposure: On cloud instances or misconfigured firewalls, binding to 0.0.0.0 can make the MCP server internet-accessible.
* No Authentication Layer: Most MCP servers lack built-in authentication, so network exposure effectively grants full access.

**Recommended Actions**

**Investigate the Item:**

* Check the MCP server's configuration for bind address settings (look for `0.0.0.0`, `::`, or wildcard host values).
* Determine whether remote access is an intentional design choice or an oversight.
* Review whether any firewall rules or network segmentation limits external access to the bound port.
* Check if this item also has the Tools Invokable Without Authentication finding — if the server binds to all interfaces *and* its tools can be invoked without authentication, any device on the network can execute tools with no access controls, significantly increasing the severity.

**Immediate Action:**

* Reconfigure the MCP server to bind to `127.0.0.1` or `localhost` if remote access is not required.
* If remote access is needed, place the server behind an authenticated reverse proxy.

**Mitigation:**

* Enforce localhost-only binding by default in MCP server configurations.
* Implement network-level access controls (firewall rules, security groups) to restrict access to the MCP port.
* Add authentication and authorization mechanisms before exposing any MCP server beyond localhost.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/risk-and-threat-intelligence/findings/index-3/unrestricted-network-access.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

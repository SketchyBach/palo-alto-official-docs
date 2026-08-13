<!-- KOI source: https://docs.koi.ai/risk-and-threat-intelligence/findings/index-5/bypasses-network-control.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/risk-and-threat-intelligence/findings/index-5/bypasses-network-control.md).

# Bypasses Network Control

**Severity**

🟠 High (7)

**Short Description**

Flags items that enable users to circumvent organizational network controls, such as firewalls, content filters, or secure gateways. Tools like VPNs or proxy extensions can obscure traffic, bypass security monitoring, and facilitate unauthorized access to restricted content or external services, introducing significant security, compliance, and data exfiltration risks.

**Suggestion**

Carefully evaluate the business necessity of this item and consider removing it if it is not essential or authorized. If the item is required for legitimate business purposes, ensure it is approved through proper IT channels and monitored closely.

**Information**

Items that enable users to bypass organizational network controls represent a significant security concern. These items typically include VPN clients, proxy tools, tunneling applications, or other technologies designed to circumvent established security perimeters such as firewalls, content filters, and secure web gateways. While some of these tools may serve legitimate purposes, their presence on endpoints can allow users to route traffic outside of monitored and protected network channels, effectively creating blind spots in security visibility. By obscuring network traffic and evading detection mechanisms, such items can facilitate unauthorized access to restricted websites, cloud services, or external networks that would otherwise be blocked by organizational security policies.

**Risks of Bypasses Network Control**

* **Evasion of Security Monitoring**: The item can obscure network traffic, preventing security tools from inspecting content and detecting threats, malware downloads, or data exfiltration attempts.
* **Bypass of Content Filtering**: Users can access restricted or inappropriate websites and services that violate acceptable use policies and expose the organization to legal and compliance risks.
* **Data Exfiltration**: Encrypted tunnels created by these items can be used to transmit sensitive organizational data to external locations without detection.
* **Compliance Violations**: Circumventing network controls may violate regulatory requirements for data protection, security monitoring, and access controls.
* **Malware Introduction**: By accessing unfiltered internet content, users may inadvertently download malware or access malicious sites that would normally be blocked.
* **Shadow IT Risks**: The item enables access to unauthorized cloud services and applications, creating shadow IT environments that are unmanaged and unprotected.

**Recommended Actions**

1. **Investigate the Item**:
   * **Verify Business Need**: Determine if the item serves a legitimate business purpose and whether it was installed with proper authorization.
   * **Identify Usage Patterns**: Review network logs to understand how the item is being used and what destinations are being accessed.
   * **Check Policy Compliance**: Verify whether the item violates organizational acceptable use policies or security standards.
2. **Immediate Action**:
   * **Remove If Unauthorized**: If the item was installed without approval or lacks a valid business justification, remove it from the endpoint.
   * **Enforce Policy Controls**: Use endpoint management tools to prevent unauthorized installation of network circumvention tools.
   * **User Education**: Inform users about the risks and policy violations associated with using such items.
3. **Long-term Prevention**:
   * **Implement Application Control**: Deploy allowlisting policies to prevent installation of unauthorized network tools.
   * **Monitor for Circumvention Attempts**: Use network analytics to detect signs of tunneling, proxy usage, or other evasion techniques.
   * **Establish Approved Alternatives**: If remote access or specific network capabilities are needed, provide approved, monitored solutions that maintain security visibility.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/risk-and-threat-intelligence/findings/index-5/bypasses-network-control.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

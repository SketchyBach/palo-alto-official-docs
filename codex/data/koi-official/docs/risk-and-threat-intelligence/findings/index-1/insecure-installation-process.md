<!-- KOI source: https://docs.koi.ai/risk-and-threat-intelligence/findings/index-1/insecure-installation-process.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/risk-and-threat-intelligence/findings/index-1/insecure-installation-process.md).

# Insecure Installation Process

**Severity**

🟡 Medium (6)

**Short Description**

Flags items that perform installation or fetch resources over unencrypted channels. This behavior exposes the installation process to potential interception or tampering, increasing the risk of man-in-the-middle attacks or unauthorized modifications.

**Suggestion**

Review the item's installation process and verify whether it can be configured to use secure, encrypted channels (HTTPS) for all downloads and updates. If the item does not support secure installation methods, consider replacing it with a more secure alternative or removing it from the endpoint.

**Information**

Items that perform installation or fetch resources over unencrypted channels (such as HTTP instead of HTTPS) expose the endpoint to significant security risks during the installation and update process. Without encryption, the data transmitted between the endpoint and remote servers can be intercepted, read, or modified by malicious actors positioned along the network path. This vulnerability is particularly concerning because installation processes often involve downloading executable code, configuration files, or scripts that will be executed with elevated privileges on the endpoint. If these resources are tampered with during transit, the compromised components will be installed and executed, potentially giving attackers control over the endpoint.

**Risks of Insecure Installation Process**

* **Man-in-the-Middle Attacks**: Unencrypted installation channels allow attackers to intercept network traffic and inject malicious code into downloaded resources before they reach the endpoint.
* **Code Tampering**: Installation packages, scripts, or executables can be modified in transit, replacing legitimate components with malicious payloads without detection.
* **Credential Exposure**: If the installation process transmits authentication tokens or credentials over unencrypted channels, these can be captured and used for unauthorized access.
* **Supply Chain Compromise**: Tampered installations can serve as entry points for broader supply chain attacks, affecting not just the immediate endpoint but potentially spreading to connected systems.
* **Persistence of Compromise**: Malicious code injected during installation may establish persistent backdoors that survive system reboots and are difficult to detect.

**Recommended Actions**

1. **Investigate the Item**:
   * **Identify Insecure Channels**: Determine which specific resources or endpoints are being accessed over unencrypted channels during installation.
   * **Check Configuration Options**: Review whether the item can be configured to enforce secure (HTTPS) connections for all resource fetching.
   * **Assess Publisher Practices**: Evaluate whether the publisher has a history of security-conscious development practices.
2. **Immediate Action**:
   * **Enable Secure Channels**: If the item supports HTTPS or other encrypted protocols, configure it to use only secure channels.
   * **Consider Alternatives**: If secure installation is not supported, identify and evaluate alternative items that provide similar functionality with proper security measures.
   * **Remove If Necessary**: If no secure configuration is available and the item handles sensitive operations, remove it from the endpoint to prevent exploitation.
3. **Prevention and Monitoring**:
   * **Network Monitoring**: Deploy network monitoring tools to detect and alert on unencrypted downloads or installations.
   * **Enforce Security Policies**: Implement endpoint security policies that restrict or flag items using insecure installation methods.
   * **Regular Audits**: Periodically review installed items to ensure they maintain secure update and installation practices.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/risk-and-threat-intelligence/findings/index-1/insecure-installation-process.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

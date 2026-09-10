---
url: https://docs.koi.ai/get-started/frequently-asked-questions
fetched_at: 2026-09-06T09:12:09.739Z
source: koi-official-browser
capture_method: authenticated official browser
---

# Frequently asked questions

For the complete documentation index, see llms.txt. This page is also available as Markdown.
Ask
DocumentationGet Started
Frequently asked questions
Product features and functionality
Discovery

How does the discovery of items work?

Koi leverages your existing MDM or EDR to run a lightweight script package that detects marketplace-sourced items on your endpoints.

Can we track how many users have already installed a specific item?

Koi provides visibility into item usage across your organization, showing how many users have a specific item installed and on which devices. This insight helps you understand the actual exposure and potential impact of each item, making it easier to assess risk and manage your organization’s attack surface.

What is the basis for the risk scores Koi provides?

Koi’s risk assessment is grounded in a comprehensive, research-driven framework built on three core pillars, designed to uncover the true risk each item introduces into your environment:

Publisher identity - Analysis of who is behind the item, including their reputation, credibility, history, and exposure in known data breaches.

Deep composition analysis - Inspection of the item’s code and structure for vulnerabilities, malicious code snippets, exposed secrets, and anomalies, including advanced source code evaluation using LLM-powered techniques.

Behavioral insights - Detection of runtime activity such as sensitive API calls, external communications, and suspicious behavior patterns.

These signals are continuously enriched by Koi’s research team, which curates and publishes actionable findings. These findings serve as the foundation for a dynamic, context-aware risk level that reflects real-world threats. The result is a dynamic evolving risk level that empowers security teams quickly understand exposure, prioritize remediation, and confidently enforce guardrails and policies at scale.

Does Koi detect and handle malicious items or malware post-installation?

Yes, Koi has built-in mechanisms to detect malicious items. If Malware protection guardrail is enabled, malicious items will be remediated automatically in the next script package run.

Does Koi assist in monitoring private or non-marketplace items?

Koi scans public items from marketplaces. Private or non-marketplace items (like internal or self-hosted extensions) are treated as proprietary and are not scanned by our risk engine. Therefore no automatic remediation is ever applied to those.

Governance

How does the enforcement of policies work?

Koi is your supply chain gateway, via network proxy the traffic that goes to marketplaces domains only is transferred through Koi. According to your guardrails and policies configurations Koi is scanning, filtering and preventing threat from getting into your organization. Rest of network traffic remains the same with no impact or visibility to Koi's Gateway, it is transparent for the end user that can continue working as usual, but with security in place. Koi integrates with the common secure web gateways such as Zscaler ZIA and Palo Alto Prisma Access, complete list of supported integrations can be found here.

Policies can take up to 60 minutes to be updated and applied across the network. Specifically, Homebrew prevention is managed via the Koi Script Package, meaning that adding a package to the blocklist is enforced on endpoints based on the next script run.

What happens if I create a blocking policy for an item already installed on endpoints?

If a blocking policy is created it will prevent future installations of the item. However, existing items that match the policy conditions will not be automatically remediated unless they are deemed malicious or delisted, and the corresponding guardrails are enabled. It won’t impact any existing installations to ensure continuous productivity, these existing items will be suggested for remediation and appear in the Remediation page Open tab, allowing you to review and control the remediation.

Can we enforce different policies for different users or teams?

Koi supports policy scoping based on device groups. By creating groups (e.g., developers, finance, interns) you can apply different rules to each group, allowing some users access while restricting others. This ensures granular control based on role, department, or security level.

What will a developer experience when an item is blocked from IDE, and how can they request approval?

Browsers: Blocked items will be presented with a “Request Approval” button.

IDEs:

In their web marketplace(e.g., VS Code) - the button changes to “Request Approval.”

Inside the IDE itself:

By default, the blocked item will be hidden in the IDE.

For VS Code, Cursor, and Windsurf - this experience can be customized, organizations can configure Koi to show the item as blocked by policy and allow developers to request approval directly from within the IDE. Koi admins can configure from the Settings page to display blocked items with a clear “Blocked by organizational policy” message. (Note: The button itself cannot be changed, but the items will still be blocked from installation).

Homebrew packages: Blocked packages cannot be downloaded. Instead, end users will see a CLI message indicating the block, along with a link to the Request Approval form.

How does Koi automate the governance of marketplace items to reduce manual vetting by security admins?

Koi simplifies governance by allowing you to set policies that automatically approve highly used, low-risk items with business justification, ensuring productivity. Common allow policies include items from first-party publishers or those with low-risk by Koi. Additionally, the query builder enables the creation of granular policies based on Koi's detailed risk analysis.

Remediation

How does Koi assist with the remediation processes?

With the Script Package running via MDM or EDR, items approved for remediation will be removed from the target endpoint during the next script run.

Koi automates remediation by using guardrails that identify and act on malicious items during scheduled script package runs. These can be customized based on your organization's security policies.

Automatic remediation only applies to:

Malware Protection Guardrail

Auto-remediate Delisted Guardrail
Items flagged by these guardrails move to the Pending tab in the Remediation page and will be automatically removed on the next script run.

For other blocking policies, items are surfaced in the Open tab in the Remediation page, where Koi admins can manually trigger removal.

This approach balances automation with control, ensuring critical threats are handled automatically while admins retain governance over policy-driven cleanups.

Can we receive alerts for malicious items without enabling auto-remediation?

Yes. From the Notifications tab in the Settings page, you can enable alerts for malicious items without turning on auto-remediation. This will send you email notifications whenever a new malicious item is detected in your environment. No automatic action will be taken - giving you full visibility and allowing you to handle remediation through your internal process.

How does Koi handle remediation in special cases?

Extensions in use on Windows devices:

By default, Koi does not terminate active processes (JetBrains IDEs, Notepad++). Remediation takes place only when the application is closed.

If desired, admins can request to enforce removal even when the process is open (contact account manager to enable).

Dependencies:

Brew packages and VSCode extensions can have dependencies (e.g., an extension pack).

If a targeted item is a dependency of another installed item, Koi will not execute remediation to avoid breaking functionality.

Chrome extensions:

Extensions are tied to user profiles.

Simple file deletion may cause Chrome to reinstall them.

Koi prevents reinstallation by adding them to Chrome’s local block-list, ensuring the item is disabled and cannot be re-enabled.

General

Where can I see which platforms and marketplaces Koi supports?

Koi continuously expands its protection across browsers, IDEs, code registries, OS package managers, and application stores. To help you understand exactly which capabilities are supported for each platform and marketplace, we maintain a dedicated coverage page. View full coverage documentation.

Which notifications are supported from your product?

Koi supports notifications for both end users and security administrators. End users can receive alerts when an item is removed from their device, delivered via OS-level notifications or communication platforms like Slack, Microsoft Teams, or email. Security administrators are notified about high-risk events such as detection of malicious items. Notifications are fully configurable, allowing teams to tailor what events trigger alerts and how they are delivered based on their operational needs.

Which APIs does Koi support?

Koi is an API-first solution, everything available in the product is also exposed via API. This includes functionalities like risk analysis for marketplace items. Through the API, you can trigger actions such as rescanning to get updated risk analysis for an item, remediating items from endpoints, or allowing and blocking specific items requests . You can find more details in the API documentation.

Does Koi support remote development environments (such as VS Code Remote SSH, Coder, Dev Containers, WSL, JetBrains Gateway)?

Yes. Koi supports full deployment in Coder workspaces - including discovery, prevention, and remediation. To set up Koi in Coder, see here.

In addition, when you run connect to a remote  dev environment via a Koi-supported IDE (VS Code, Cursor, Windsurf, JetBrains) on a Koi-protected machine, Koi's prevention proxy applies on the remove environments. Your policies and guardrails apply to the local machine's traffic, ensuring consistent enforcement across remote development workflows.

Koi also protects package managers and tooling on remote hosts (pip, npm in WSL or remote servers). We configure these based on your architecture and security requirements - Reach out to your dedicated account manager to learn more.

Deployment and Integrations

Which EDR/MDM integrations are supported?

Any EDR or MDM solution with script execution capabilities is supported. The script must run on a recurring schedule (recommended: once per hour) to ensure continuous protection and visibility. List of popular EDR or MDM integrations can be found at EDR and MDM integration guides.

How can Koi integrate with my SIEM?

Koi supports SIEM integration by allowing you to forward notifications using webhooks or by ingesting relevant data through the Alerts and Audit Log APIs. Full API documentation is available here.

Does Koi support single sign-on?

Koi provides seamless integration with Okta and other major Identity Providers using SSO. Detailed setup instructions can be found in the Koi API documentation linked here.

Why does Koi require a signed CSR and private key, and how are they managed securely?

Koi requires a signed Certificate Signing Request (CSR) and private key to manage encrypted traffic to marketplace domains via the Koi Gateway. This is essential for inspecting SSL-encrypted traffic in order to identify extensions being accessed or installed within the organization.
The CSR is domain-scoped, only valid for specific marketplace domains - so Koi can decrypt, inspect, and enforce policies on that traffic. Koi cannot and does not intercept or decrypt general organizational traffic, only traffic to supported marketplaces. Koi securely manages these credentials using AWS Secrets Manager, a trusted vault service, with strict access controls and encryption to ensure confidentiality and integrity.

How to export your API inventory into your SIEM? 

Search Inventory API supports advanced filters, nested groups, and AND/OR logic, mirroring the query builder experience in the UI. You can programmatically ask complex questions such as “show all high-risk items installed manually across production endpoints” and get structured results in near real time. This enables automated investigations, policy validation checks, and daily syncs into downstream systems without human intervention.

Reports API allows you to trigger a full inventory export via POST /api/external/v2/reports, poll for completion, and retrieve a presigned download_url valid for 12 hours. In practice, this means you can define your query conditions, generate a report, and automatically pull it into your SIEM on a schedule. The result is a continuously refreshed dataset that threat hunters, IR, and governance teams can reference during investigations without re-querying Koi manually.

By combining the advanced Search Inventory API with the asynchronous Reports API, you can now:
1. Trigger a report with precise query conditions.
2. Poll until it is ready.
3. Ingest the full dataset into your destination system.

Previous
Be Successful with Koi
Next
Capabilities coverage

Last updated 3 months ago

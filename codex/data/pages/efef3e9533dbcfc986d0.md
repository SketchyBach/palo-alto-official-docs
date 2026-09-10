---
url: https://docs.koi.ai/integration-guides/remote-development-environments/coder
fetched_at: 2026-09-06T10:25:44.338Z
source: koi-official-browser
capture_method: authenticated official browser
---

# Coder

For the complete documentation index, see llms.txt. This page is also available as Markdown.
Ask
DocumentationIntegration GuidesRemote Development Environments
Coder
What is Coder?

Coder is a remote development platform that allows developers to work inside cloud-hosted development workspaces instead of on their local machines. Each Coder workspace is a fully functional development environment where developers write code, install packages, run AI agents, and interact with tools such as IDEs, package managers, and MCP servers.

From a security perspective, a Coder workspace behaves much like a developer endpoint, it is where development activity actually takes place, even though it runs remotely.

Koi Support for Coder

Koi provides native support for Coder workspaces, enabling organizations to extend endpoint protection to remote development environments.

By deploying the Koi script inside a Coder workspace, you can enable:

Discovery of AI and development artifacts

Risk analysis across supported inventories

Remediation workflows for identified risks

Items discovered inside Coder workspaces are processed through Koi's standard risk pipeline and are available throughout the product, including inventory views, dashboards, reports, and APIs.

For the scrip deployment instructions, see the Deploying Koi on Coder workspacesguide.

Prevention

Prevention is supported separately from the Coder deployment.

When developers connect to a Coder workspace (or another remote development environment) using a Koi-supported IDE (VS Code, Cursor, Windsurf, or JetBrains) from a Koi-protected machine, Koi's prevention proxy applies to the remote development session. Your configured guardrails and runtime policies continue to protect IDE traffic throughout the session. See the Networkintegration guide. 

Koi can also protect package managers and development tooling running on remote hosts (such as pip and npm in Coder). This integration is configured based on your architecture and security requirements. Contact your Koi account team for deployment guidance.

How Coder Workspaces Appear in Koi

Koi treats each Coder workspace as a first-class Endpoint.

This allows security teams to manage remote development environments alongside physical devices using the same workflows, policies, and reporting.

Coder endpoints:

Appear in the Endpoints inventory.

Participate in dashboards and reporting.

Surface discovered artifacts in the appropriate inventory views.

Support the same policy enforcement, prevention, and remediation capabilities as supported local endpoints.

This unified model provides consistent visibility and governance across both local and cloud-based development environments.

Previous
Remote Development Environments
Next
Deploying Koi on Coder workspaces

Last updated 1 month ago

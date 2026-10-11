# KOI, Agentic Endpoint Security, and Prisma AIRS update — 11 October 2026

This was a focused authenticated KOI review plus a fresh official Prisma AIRS sitemap refresh. It does not claim a new full capture of every authenticated KOI page. Four current KOI pages were captured through the authenticated documentation session, SHA-256 verified, and imported into the corpus.

## Product boundary

KOI documentation describes Agentic Endpoint Security (AES) as the endpoint-focused capability for discovering AI components, assessing risk, enforcing policy, and remediating violations. Prisma AIRS remains a separate product family for AI runtime, gateway, model, application, agent, and supply-chain security. The products integrate, but the names should not be treated as interchangeable.

## Newly verified KOI material

The October 2026 release notes add skills discovery and risk assessment for Codex, Antigravity, Claude Cowork, OpenCode, and Kiro; an AI Agents Inventory Preview; expansion of the destructive-command guardrail from 23 to 109 commands; and Kiro runtime control in Preview.

The new Koi MCP Server guide documents a remote Streamable HTTP endpoint at `https://api.prod.koi.security/api/external/v2/mcp`. It uses the same bearer API key as External API v2. The guide warns that keys are tenant-wide full-access credentials, documents write-capable tools, and specifies a rate limit of 30 requests per minute per customer per endpoint path. Store the key in a secret manager and review the available tools before connecting an AI client.

The renamed Prisma AIRS Runtime Enforcement integration guide and the non-preview risky-path guardrail URL are now present in the corpus. The risky-path guardrail currently documents macOS support, Santa-based enforcement, Impact Check, endpoint-group scoping, and an administrator-editable path list.

## Prisma AIRS and AES refresh result

Fresh sitemap discovery found 517 current Prisma AIRS URLs with indexed bodies. The refresh attempted 521 URLs: 502 succeeded and 19 returned HTTP 404. The failed fetches and receipts were retained for auditability; this update therefore does not claim that every historical URL remains live. Four current Cortex XDR/XSIAM pages covering Agentic Endpoint Security capabilities and agent-settings profiles were also refreshed.

## Official sources checked live on 11 October 2026

- [KOI What's new](https://docs.koi.ai/get-started/whats-new-in-koi)
- [KOI MCP Server](https://docs.koi.ai/guides/koi-mcp-server)
- [KOI Block Execution from Risky Paths](https://docs.koi.ai/guardrails/block-execution-from-risky-paths)
- [KOI Prisma AIRS Runtime Enforcement](https://docs.koi.ai/integration-guides/prisma-airs-runtime-enforcement)
- [KOI Activate AES Module on the Cortex Agent](https://docs.koi.ai/integration-guides/endpoint-integration/deploy-koi-to-your-endpoints/activate-aes-module-on-the-cortex-agent)
- [Prisma AIRS AI Gateway Routing Configurations](https://docs.paloaltonetworks.com/ai-runtime-security/administration/configure-ai-gateway)
- [Cortex XDR Endpoint Protection Capabilities](https://docs-cortex.paloaltonetworks.com/r/Cortex-XDR/Cortex-XDR-5.x-Documentation/Endpoint-Protection-Capabilities)
- [Cortex XDR Agent Settings Profiles](https://docs-cortex.paloaltonetworks.com/r/Cortex-XDR/Cortex-XDR-5.x-Documentation/Set-up-Agent-Settings-Profiles)
